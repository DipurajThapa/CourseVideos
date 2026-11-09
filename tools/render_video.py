#!/usr/bin/env python3
"""Render a chapter's full walkthrough video from video/storyboard.json.

Usage:
  python3 tools/render_video.py --setup                    install and check the video toolchain
  python3 tools/render_video.py <chapter-dir> --preview DIR draw every beat as a PNG plus a contact sheet
  python3 tools/render_video.py <chapter-dir>               render the video (writes the files below)
  python3 tools/render_video.py <chapter-dir> --script      only regenerate video/script.md

Outputs, all inside <chapter-dir>/video/:
  chapter.mp4      1920x1080, 30 fps, H.264 + AAC, soft English captions and scene chapters
  chapter.srt      captions (also for upload to a video platform)
  description.md   upload description with scene timestamps and the synthetic-voice disclosure
  render.json      what was rendered, from which inputs, with which voice and tool versions
  script.md        the human-readable script with real timings

The renderer follows the video-making skill: one encoded file per scene with the
same size, frame rate and encoder settings, joined with the concat demuxer and
-c copy, sound added with -c:v copy, scenes written to temporary names and
renamed only when ffmpeg exits 0, and stills held without zoom.

Narration uses Piper, a free neural text-to-speech engine that runs offline, with
one pinned voice so every chapter sounds the same.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import storyboard as sb  # noqa: E402
from common import ROOT, load_json, now_iso, save_json  # noqa: E402

RENDERER_VERSION = "1.0.0"
W, H, FPS = 1920, 1080, 30
PIPER_VERSION = "1.8.0"
VOICE = "en_US-lessac-medium"
VOICE_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/"
VOICE_SHA256 = "5efe09e69902187827af646e1a6e9d269dee769f9877d17b16b1b46eeaaf019f"
LENGTH_SCALE = "1.18"           # slower than default, for second-language listeners
SENTENCE_PAUSE = 0.35           # seconds of silence between sentences
CACHE = Path(os.environ.get("COURSE_VIDEO_CACHE", Path.home() / ".cache" / "coursevideos"))
FONTS = Path(__file__).resolve().parent / "video" / "fonts"
MAX_MB = 90                     # GitHub rejects files over 100 MB

# Spoken forms for words the voice reads badly. Applied to audio only; captions keep the original.
PRONOUNCE = {
    r"\bAI\b": "A.I.", r"\bXP\b": "X P", r"\bPEP 8\b": "pep eight", r"\bChatGPT\b": "Chat G P T",
    r"\bf-strings?\b": "f strings", r"\bint\b": "int", r"\bstr\b": "string", r"\bbool\b": "bool",
    r"\bNameError\b": "Name Error", r"\bTypeError\b": "Type Error", r"\bSyntaxError\b": "Syntax Error",
    r"\bIDLE\b": "idle", r"\bUSD\b": "U S D",
}

C = {  # colours
    "bg": "#F6F5F0", "ink": "#1F2933", "muted": "#5B6770", "accent": "#0F766E", "accent_soft": "#D7EFEC",
    "bar": "#E4E2DA", "code_bg": "#1E2230", "code_fg": "#E6E6E6", "gutter": "#6B7280",
    "hl": "#3A4255", "out_bg": "#101418", "out_fg": "#D9F99D", "err": "#FCA5A5", "inline_bg": "#E7E5DC",
    "pause_bg": "#0F766E", "white": "#FFFFFF", "table_head": "#D7EFEC", "rule": "#CFCBBE",
}


# ---------------------------------------------------------------- setup

def sh(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def voice_paths() -> tuple[Path, Path]:
    folder = CACHE / "piper"
    return folder / f"{VOICE}.onnx", folder / f"{VOICE}.onnx.json"


def file_sha(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def setup() -> int:
    problems = []
    for exe in ("ffmpeg", "ffprobe"):
        if not shutil.which(exe):
            problems.append(f"{exe} is not installed")
    for module, package in (("PIL", "pillow"), ("pygments", "pygments"), ("piper", f"piper-tts=={PIPER_VERSION}")):
        try:
            __import__(module)
        except ImportError:
            sh([sys.executable, "-m", "pip", "install", "--quiet", "--break-system-packages", package])
            try:
                __import__(module)
            except ImportError:
                problems.append(f"could not install {package}")
    model, config = voice_paths()
    model.parent.mkdir(parents=True, exist_ok=True)
    for path in (model, config):
        if not path.exists():
            try:
                tmp = path.with_suffix(path.suffix + ".part")
                urllib.request.urlretrieve(VOICE_URL + path.name, tmp)
                tmp.rename(path)
            except Exception as exc:  # network or TLS failure
                problems.append(f"could not download {path.name}: {exc}")
    if model.exists() and file_sha(model) != VOICE_SHA256:
        problems.append(f"voice model checksum mismatch for {model}; delete it and run --setup again")
    for font in ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSansMono.ttf", "DejaVuSansMono-Bold.ttf"):
        if not (FONTS / font).exists():
            problems.append(f"missing font {font}")
    if not problems:
        test = synthesize("Video setup check.")
        if not test or wav_seconds(test) < 0.3:
            problems.append("Piper produced no audio")
    if problems:
        print("\n".join(problems))
        return 1
    ffmpeg = sh(["ffmpeg", "-version"]).stdout.splitlines()[0].split(" ")[2]
    print(f"ffmpeg {ffmpeg}, piper {PIPER_VERSION}, voice {VOICE}")
    return 0


# ---------------------------------------------------------------- audio

def spoken(text: str) -> str:
    for pattern, replacement in PRONOUNCE.items():
        text = re.sub(pattern, replacement, text)
    return text


_VOICE = None


def synthesize(text: str) -> Path | None:
    """Speak text with Piper, one sentence at a time with a short pause between sentences.

    Results are cached by content, so re-rendering after a small storyboard change is fast.
    The voice model loads once per process.
    """
    global _VOICE
    model, _ = voice_paths()
    key = hashlib.sha256(f"{VOICE}|{LENGTH_SCALE}|{SENTENCE_PAUSE}|{spoken(text)}".encode()).hexdigest()[:24]
    out = CACHE / "tts" / f"{key}.wav"
    if out.exists():
        return out
    out.parent.mkdir(parents=True, exist_ok=True)
    from piper import PiperVoice, SynthesisConfig
    if _VOICE is None:
        _VOICE = PiperVoice.load(str(model))
    config = SynthesisConfig(length_scale=float(LENGTH_SCALE))
    sentences = [spoken(s) for s in re.split(r"(?<=[.!?:])\s+", text.strip()) if s]
    tmp = out.with_suffix(".part.wav")
    with wave.open(str(tmp), "wb") as wf:
        rate = _VOICE.config.sample_rate
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        for i, sentence in enumerate(sentences):
            if i:
                wf.writeframes(b"\0\0" * int(SENTENCE_PAUSE * rate))
            for chunk in _VOICE.synthesize(sentence, syn_config=config):
                wf.writeframes(chunk.audio_int16_bytes)
    tmp.rename(out)
    return out


def wav_seconds(path: Path) -> float:
    with wave.open(str(path)) as wf:
        return wf.getnframes() / wf.getframerate()


def frames(seconds: float) -> int:
    return max(1, math.ceil(seconds * FPS - 1e-6))


# ---------------------------------------------------------------- drawing

def font(kind: str, size: int):
    from PIL import ImageFont
    name = {"sans": "DejaVuSans.ttf", "bold": "DejaVuSans-Bold.ttf", "mono": "DejaVuSansMono.ttf",
            "monob": "DejaVuSansMono-Bold.ttf"}[kind]
    return ImageFont.truetype(str(FONTS / name), size)


RICH = re.compile(r"(`[^`]+`|\*\*[^*]+\*\*)")


def rich_runs(text: str) -> list[tuple[str, str]]:
    runs = []
    for part in RICH.split(text):
        if not part:
            continue
        if part.startswith("`"):
            runs.append(("code", part[1:-1]))
        elif part.startswith("**"):
            runs.append(("bold", part[2:-2]))
        else:
            runs.append(("text", part))
    return runs


def layout_rich(text: str, size: int, width: int) -> list[list[tuple[str, str, int]]]:
    """Split rich text into lines of (kind, word, pixel width) that fit `width`."""
    fonts = {"text": font("sans", size), "bold": font("bold", size), "code": font("mono", int(size * 0.92))}
    space = fonts["text"].getlength(" ")
    lines, line, used = [], [], 0.0
    for kind, chunk in rich_runs(text):
        words = re.findall(r"\S+|\s+", chunk)
        for word in words:
            if word.isspace():
                if line:
                    gap = fonts["code"].getlength(" ") if kind == "code" else space
                    line.append(("codespace" if kind == "code" else "space", " ", gap))
                    used += gap
                continue
            pad = 0
            if kind == "code" and not (line and line[-1][0] == "codespace"):
                pad = 16
            wlen = fonts[kind].getlength(word) + pad
            if line and used + wlen > width:
                while line and line[-1][0] in ("space", "codespace"):
                    used -= line.pop()[2]
                lines.append(line)
                line, used = [], 0.0
            line.append((kind, word, wlen))
            used += wlen
    if line:
        lines.append(line)
    return lines


def draw_rich(draw, x: int, y: int, text: str, size: int, width: int, color: str = C["ink"],
              line_gap: float = 1.45) -> int:
    fonts = {"text": font("sans", size), "bold": font("bold", size), "code": font("mono", int(size * 0.92))}
    for line in layout_rich(text, size, width):
        # merge neighbouring code pieces into one pill
        groups: list[list] = []
        for kind, word, wlen in line:
            is_code = kind in ("code", "codespace")
            if groups and groups[-1][0] == is_code and (is_code or kind == groups[-1][1]):
                groups[-1][2] += word
                groups[-1][3] += wlen
            else:
                groups.append([is_code, kind, word, wlen])
        cx = x
        for is_code, kind, word, wlen in groups:
            if is_code:
                word = word.strip()
                wlen = fonts["code"].getlength(word) + 16
                draw.rounded_rectangle([cx, y + 2, cx + wlen, y + size * 1.25], radius=6, fill=C["inline_bg"])
                draw.text((cx + 8, y + size * 0.12), word, font=fonts["code"], fill=C["accent"])
            elif kind != "space":
                draw.text((cx, y), word, font=fonts[kind], fill=color)
            cx += wlen
        y += int(size * line_gap)
    return y


def rich_height(text: str, size: int, width: int, line_gap: float = 1.45) -> int:
    return len(layout_rich(text, size, width)) * int(size * line_gap)


class Frame:
    def __init__(self, ctx: dict, section: str, bg: str = C["bg"]):
        from PIL import Image, ImageDraw
        self.img = Image.new("RGB", (W, H), bg)
        self.d = ImageDraw.Draw(self.img)
        self.ctx = ctx
        self.section = section

    def chrome(self, progress: float, dark: bool = False) -> None:
        fg = C["white"] if dark else C["muted"]
        self.d.text((60, 34), self.ctx["brand"], font=font("bold", 24), fill=C["white"] if dark else C["accent"])
        self.d.text((W - 60, 34), self.section, font=font("sans", 24), fill=fg, anchor="ra")
        self.d.rectangle([0, H - 10, W, H], fill=C["bar"] if not dark else "#0B5A54")
        self.d.rectangle([0, H - 10, int(W * progress), H], fill=C["accent"] if not dark else C["white"])

    def heading(self, text: str, y: int = 96, size: int = 54) -> int:
        return draw_rich(self.d, 60, y, text, size, W - 120, line_gap=1.25) + 18

    def save(self, path: Path) -> None:
        self.img.save(path, "PNG", optimize=False)


def token_colours(path: Path, source: str):
    from pygments import lex
    from pygments.lexers import get_lexer_for_filename
    from pygments.styles import get_style_by_name
    style = get_style_by_name("one-dark")
    lines: list[list[tuple[str, str]]] = [[]]
    for ttype, value in lex(source, get_lexer_for_filename(path.name)):
        spec = style.style_for_token(ttype)
        colour = f"#{spec['color']}" if spec.get("color") else C["code_fg"]
        for i, piece in enumerate(value.split("\n")):
            if i:
                lines.append([])
            if piece:
                lines[-1].append((piece, colour))
    while lines and not lines[-1]:
        lines.pop()
    return lines


def wrap_plain(text: str, chars: int) -> list[str]:
    out = []
    for raw in text.split("\n"):
        while len(raw) > chars:
            cut = raw.rfind(" ", 0, chars)
            cut = cut if cut > chars // 2 else chars
            out.append(raw[:cut])
            raw = "  " + raw[cut:].lstrip()
        out.append(raw)
    return out


_ERRORS: dict[str, str] = {}


def real_error_line(chapter: Path, rel: str, needle: str) -> str:
    """Run the file on the first configured toolchain and return the real last error line.

    The line is shown only if it contains the verified `.expected_error` text, so the video
    shows the full message a learner sees without showing anything unverified.
    """
    key = f"{chapter}/{rel}"
    if key not in _ERRORS:
        import verify_chapter as vc
        chains = vc.toolchains(chapter.parent.name)
        line = needle
        if chains:
            _, out, err = vc.run_file(chapter / rel, chains[0])
            lines = [x for x in (err or out).strip().splitlines() if x.strip()]
            if lines and needle in lines[-1]:
                line = lines[-1].strip()
        _ERRORS[key] = line
    return _ERRORS[key]


def panel(d, box, title: str, title_colour: str, bg: str) -> None:
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=18, fill=bg)
    d.text((x0 + 28, y0 + 18), title, font=font("bold", 24), fill=title_colour)


def draw_code_beat(fr: Frame, chapter: Path, v: dict) -> None:
    top = fr.heading(v.get("heading", ""), size=46) if v.get("heading") else 96
    if v.get("note"):
        top = draw_rich(fr.d, 60, top - 6, v["note"], 30, W - 120, color=C["muted"]) + 8
    src_path = chapter / v["file"]
    source = src_path.read_text(encoding="utf-8").rstrip("\n")
    code_lines = token_colours(src_path, source)
    has_side = bool(v.get("output") or v.get("error") or v.get("output_hidden", True))
    has_side = has_side and not v.get("code_only")
    bottom = H - 60
    side_chars = 30
    if v.get("output"):
        side_chars = max(side_chars, *(len(x) for x in (chapter / v["output"]).read_text(encoding="utf-8").split("\n")))
    if v.get("error"):
        side_chars = max(side_chars, len(real_error_line(chapter, v["file"],
                                                         (chapter / v["error"]).read_text(encoding="utf-8").strip())))
    side_w = int(min(820, max(560, side_chars * 30 * 0.602 + 80)))
    split = W - 60 - side_w - 30
    code_box = [60, top, (split if has_side else W - 60), bottom]
    out_box = [split + 30, top, W - 60, bottom]
    # fit the code
    max_chars = max((sum(len(p) for p, _ in ln) for ln in code_lines), default=1) + 5
    avail_h = code_box[3] - code_box[1] - 90
    avail_w = code_box[2] - code_box[0] - 60
    size = 34
    while size > 16 and (len(code_lines) * size * 1.45 > avail_h or max_chars * size * 0.602 > avail_w):
        size -= 1
    panel(fr.d, code_box, Path(v["file"]).name, "#9CA3AF", C["code_bg"])
    mono = font("mono", size)
    y = code_box[1] + 70
    highlight = set(v.get("highlight", []))
    for number, line in enumerate(code_lines, start=1):
        if number in highlight:
            fr.d.rectangle([code_box[0] + 8, y - 4, code_box[2] - 8, y + size * 1.3], fill=C["hl"])
            fr.d.rectangle([code_box[0] + 8, y - 4, code_box[0] + 14, y + size * 1.3], fill="#F59E0B")
        fr.d.text((code_box[0] + 24, y), f"{number:>2}", font=mono, fill=C["gutter"])
        x = code_box[0] + 24 + size * 0.602 * 4
        for piece, colour in line:
            fr.d.text((x, y), piece, font=mono, fill=colour)
            x += mono.getlength(piece)
        y += int(size * 1.45)
    if not has_side:
        return
    if v.get("error"):
        before = (chapter / v["error"]).with_suffix(".expected")
        shown = before.read_text(encoding="utf-8").rstrip("\n").split("\n") if before.exists() else []
        err_line = real_error_line(chapter, v["file"], (chapter / v["error"]).read_text(encoding="utf-8").strip())
        panel(fr.d, out_box, "Error", C["err"], C["out_bg"])
        body = [(line, C["out_fg"]) for line in shown if line] + ([("...", C["gutter"])] if shown else [])
        body += [(err_line, C["err"])]
    elif v.get("output"):
        text = (chapter / v["output"]).read_text(encoding="utf-8").rstrip("\n")
        panel(fr.d, out_box, "Output", "#A3E635", C["out_bg"])
        body = [(line, C["out_fg"]) for line in text.split("\n")]
    else:
        panel(fr.d, out_box, "Output", "#A3E635", C["out_bg"])
        draw_rich(fr.d, out_box[0] + 30, (out_box[1] + out_box[3]) // 2 - 60,
                  v.get("hidden_text", "Predict the output, then run it."), 32,
                  out_box[2] - out_box[0] - 60, color="#9CA3AF")
        return
    width = out_box[2] - out_box[0] - 60
    osize = 32
    while True:
        chars = int(width / (osize * 0.602))
        wrapped = [(seg, colour) for line, colour in body for seg in wrap_plain(line, chars)]
        if len(wrapped) * osize * 1.5 <= out_box[3] - out_box[1] - 90 or osize <= 16:
            break
        osize -= 1
    omono = font("mono", osize)
    y = out_box[1] + 70
    for seg, colour in wrapped:
        fr.d.text((out_box[0] + 30, y), seg, font=omono, fill=colour)
        y += int(osize * 1.5)


def settle(top: int, content_h: int) -> int:
    """Place a short block in the upper-middle of the free area instead of hugging the heading."""
    free = H - 70 - top
    return top + max(0, int((free - content_h) / 3))


def draw_table(fr: Frame, v: dict) -> None:
    top = fr.heading(v.get("heading", ""))
    cols = v.get("columns", [])
    rows = v["rows"]
    table_w = W - 120
    plain = lambda s: re.sub(r"[`*]", "", str(s))  # noqa: E731
    weights = [min(40, max(len(plain(c)), *(len(plain(r[i])) for r in rows))) + 6 for i, c in enumerate(cols)]
    widths = [int(table_w * w / sum(weights)) for w in weights]
    size = 40
    while size > 20:
        heights = [max(rich_height(f"**{cell}**" if r == 0 else str(cell), size, widths[i] - 40)
                       for i, cell in enumerate(row)) + 32 for r, row in enumerate([cols] + rows)]
        if top + sum(heights) < H - 80:
            break
        size -= 2
    y = settle(top, sum(heights))
    for r, row in enumerate([cols] + rows):
        hgt = heights[r]
        fr.d.rectangle([60, y, 60 + table_w, y + hgt], fill=C["table_head"] if r == 0 else
                       (C["white"] if r % 2 else C["bg"]))
        x = 60
        for i, cell in enumerate(row):
            text = f"**{cell}**" if r == 0 else str(cell)
            draw_rich(fr.d, x + 20, y + 14, text, size, widths[i] - 40)
            x += widths[i]
        fr.d.line([60, y + hgt, 60 + table_w, y + hgt], fill=C["rule"], width=2)
        y += hgt


def draw_bullets(fr: Frame, v: dict) -> None:
    top = fr.heading(v.get("heading", ""))
    items = v["items"]
    reveal = v.get("reveal", len(items))
    size = 46
    while size > 24 and sum(rich_height(i, size, W - 220) + 30 for i in items) > H - top - 80:
        size -= 2
    y = settle(top, sum(rich_height(i, size, W - 220) + 30 for i in items))
    for index, item in enumerate(items[:reveal]):
        current = index == reveal - 1 and reveal < len(items) or (v.get("focus") == index)
        dot = C["accent"] if current or reveal == len(items) else C["muted"]
        fr.d.ellipse([70, y + size * 0.35, 70 + size * 0.45, y + size * 0.8], fill=dot)
        y = draw_rich(fr.d, 130, y, item, size, W - 220) + 30


def draw_text(fr: Frame, v: dict) -> None:
    top = fr.heading(v.get("heading", ""))
    body = v.get("body", [])
    body = [body] if isinstance(body, str) else body
    lines = v["pre"].split("\n") if v.get("pre") else []
    body_h = sum(rich_height(p, 42, W - 120) + 20 for p in body)
    size = 38
    while lines and size > 18 and (len(lines) * size * 1.4 + 80 > H - top - body_h - 90 or
                                   max(len(x) for x in lines) * size * 0.602 > W - 240):
        size -= 1
    box_h = len(lines) * size * 1.4 + 60 if lines else 0
    y = settle(top, body_h + box_h + 20)
    for para in body:
        y = draw_rich(fr.d, 60, y, para, 42, W - 120) + 20
    if lines:
        box_w = max(900, max(len(x) for x in lines) * size * 0.602 + 100)
        fr.d.rounded_rectangle([60, y + 10, 60 + box_w, y + 10 + box_h], radius=18, fill=C["white"],
                               outline=C["rule"], width=2)
        yy = y + 40
        for line in lines:
            fr.d.text((100, yy), line, font=font("mono", size), fill=C["ink"])
            yy += int(size * 1.4)


def draw_prompt(fr: Frame, v: dict) -> None:
    top = fr.heading(v.get("heading", "AI prompt"))
    if v.get("label"):
        fr.d.rounded_rectangle([60, top, 60 + font("bold", 30).getlength(v["label"]) + 50, top + 56], radius=28,
                               fill=C["accent"])
        fr.d.text((85, top + 10), v["label"], font=font("bold", 30), fill=C["white"])
        top += 86
    prompt_h = rich_height(v["prompt"], 40, W - 260) + 70
    fr.d.rounded_rectangle([60, top, W - 60, top + prompt_h], radius=20, fill=C["white"], outline=C["accent"],
                           width=3)
    fr.d.text((88, top + 6), "“", font=font("bold", 80), fill=C["accent"])
    y = draw_rich(fr.d, 150, top + 35, v["prompt"], 40, W - 260)
    y = max(y, top + prompt_h) + 30
    if v.get("check"):
        draw_rich(fr.d, 60, y, "**Check it:** " + v["check"], 36, W - 120, color=C["muted"])


def draw_title(fr: Frame, v: dict) -> None:
    fr.d.text((W // 2, 260), v.get("kicker", ""), font=font("bold", 36), fill=C["accent"], anchor="mm")
    y = 330
    for line in layout_rich(v.get("title", ""), 76, W - 300):
        text = "".join(w for _, w, _ in line)
        fr.d.text((W // 2, y), text, font=font("bold", 76), fill=C["ink"], anchor="ma")
        y += 100
    y += 20
    for line in layout_rich(v.get("subtitle", ""), 36, W - 400):
        text = "".join(w for _, w, _ in line)
        fr.d.text((W // 2, y), text, font=font("sans", 36), fill=C["muted"], anchor="ma")
        y += 52
    if v.get("badge"):
        label = v["badge"]
        tw = font("bold", 32).getlength(label)
        fr.d.rounded_rectangle([W // 2 - tw / 2 - 40, y + 40, W // 2 + tw / 2 + 40, y + 110], radius=35,
                               fill=C["accent_soft"], outline=C["accent"], width=3)
        fr.d.text((W // 2, y + 75), label, font=font("bold", 32), fill=C["accent"], anchor="mm")


def draw_pause(fr: Frame, v: dict, count: int | None) -> None:
    qlines = layout_rich(v["question"], 56, W - 360)
    y = 360 - len(qlines) * 39
    fr.d.text((W // 2, y - 80), "PAUSE AND THINK", font=font("bold", 36), fill="#A7F3D0", anchor="mm")
    for line in qlines:
        text = "".join(w for _, w, _ in line)
        fr.d.text((W // 2, y), text, font=font("bold", 56), fill=C["white"], anchor="ma")
        y += 78
    if count is not None:
        cy = min(y + 190, H - 170)
        fr.d.ellipse([W // 2 - 90, cy - 90, W // 2 + 90, cy + 90], outline=C["white"], width=8)
        fr.d.text((W // 2, cy), str(count), font=font("bold", 96), fill=C["white"], anchor="mm")


def draw_visual(fr: Frame, chapter: Path, v: dict, count: int | None = None) -> None:
    kind = v["type"]
    if kind == "code":
        draw_code_beat(fr, chapter, v)
    elif kind == "table":
        draw_table(fr, v)
    elif kind == "bullets":
        draw_bullets(fr, v)
    elif kind in ("text",):
        draw_text(fr, v)
    elif kind == "prompt":
        draw_prompt(fr, v)
    elif kind in ("title", "end"):
        draw_title(fr, v)
    elif kind == "pause":
        draw_pause(fr, v, count)


# ---------------------------------------------------------------- planning

def runnable_set(chapter: Path) -> set[str]:
    found = set()
    for folder in ("examples", "practice/solutions", "project"):
        base = chapter / folder
        if base.exists():
            for p in base.rglob("*"):
                if p.is_file() and (p.with_suffix(".expected").exists() or p.with_suffix(".expected_error").exists()) \
                        and p.suffix not in (".expected", ".expected_error", ".stdin"):
                    found.add(p.relative_to(chapter).as_posix())
    return found


def chapter_kind(chapter: Path) -> str:
    meta = load_json(chapter / "meta.json")
    return meta.get("type", "lesson")


def plan(chapter: Path, board: dict) -> list[dict]:
    """Synthesize narration and work out the exact frame count of every beat."""
    beats = []
    for scene in board["scenes"]:
        for index, beat in enumerate(scene["beats"]):
            visual = beat["visual"]
            text = beat.get("narration", "").strip()
            wav = synthesize(text) if text else None
            speech = wav_seconds(wav) if wav else 0.0
            lead = 0.4 if index == 0 else 0.15
            seconds = lead + speech + sb.BEAT_GAP_SECONDS + float(beat.get("hold", 0))
            count = int(visual.get("seconds", 5)) if visual["type"] == "pause" else 0
            beats.append({"scene": scene, "beat": beat, "visual": visual, "wav": wav, "lead": lead,
                          "speech": speech, "talk_frames": frames(seconds), "count": count,
                          "frames": frames(seconds) + count * FPS})
    start = 0
    for b in beats:
        b["start_frame"] = start
        start += b["frames"]
    return beats


def context(chapter: Path, board: dict) -> dict:
    language = chapter.parent.name
    display = load_json(ROOT / "curriculum" / f"{language}.json").get("display_name", language.title())
    return {"brand": f"CODE QUEST  ·  {display}  ·  Chapter {board.get('number', '')}"}


def draw_beats(chapter: Path, board: dict, beats: list[dict], out: Path) -> list[list[tuple[Path, float]]]:
    """Draw every still. Returns, per scene, a list of (png, seconds)."""
    ctx = context(chapter, board)
    total = sum(b["frames"] for b in beats)
    scenes: dict[str, list[tuple[Path, float]]] = {}
    for n, b in enumerate(beats):
        scene, v = b["scene"], b["visual"]
        dark = v["type"] == "pause"
        progress = b["start_frame"] / total
        stills = []
        fr = Frame(ctx, scene["section"], C["pause_bg"] if dark else C["bg"])
        fr.chrome(progress, dark)
        draw_visual(fr, chapter, v)
        path = out / f"b{n:03d}.png"
        fr.save(path)
        stills.append((path, b["talk_frames"] / FPS))
        for k in range(b["count"], 0, -1):
            fr = Frame(ctx, scene["section"], C["pause_bg"])
            fr.chrome(progress, True)
            draw_visual(fr, chapter, v, count=k)
            path = out / f"b{n:03d}_{k}.png"
            fr.save(path)
            stills.append((path, 1.0))
        scenes.setdefault(scene["id"], []).extend(stills)
    return [scenes[s["id"]] for s in board["scenes"]]


# ---------------------------------------------------------------- outputs

def srt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def captions(beats: list[dict]) -> str:
    cues = []
    for b in beats:
        text = b["beat"].get("narration", "").strip()
        if not text:
            continue
        sentences = re.split(r"(?<=[.!?])\s+", text)
        chunks = []
        for sentence in sentences:
            words = sentence.split()
            while words:
                take = len(words) if len(words) <= 14 else min(12, len(words) // 2 + 1)
                chunks.append(" ".join(words[:take]))
                words = words[take:]
        total_words = sum(len(c.split()) for c in chunks)
        t = b["start_frame"] / FPS + b["lead"]
        for chunk in chunks:
            dur = b["speech"] * len(chunk.split()) / total_words
            cues.append((t, t + dur, chunk))
            t += dur
    lines = []
    for i, (a, z, text) in enumerate(cues, start=1):
        words = text.split()
        if len(text) > 42 and len(words) > 3:
            mid = len(words) // 2
            text = " ".join(words[:mid]) + "\n" + " ".join(words[mid:])
        lines += [str(i), f"{srt_time(a)} --> {srt_time(z)}", text, ""]
    return "\n".join(lines)


def clock(seconds: float) -> str:
    seconds = int(seconds)
    return f"{seconds // 60}:{seconds % 60:02d}"


def scene_timings(board: dict, beats: list[dict]) -> list[dict]:
    out = []
    for scene in board["scenes"]:
        own = [b for b in beats if b["scene"] is scene]
        start = own[0]["start_frame"] / FPS
        end = (own[-1]["start_frame"] + own[-1]["frames"]) / FPS
        out.append({"id": scene["id"], "title": scene.get("title", scene["section"]), "section": scene["section"],
                    "start": round(start, 3), "end": round(end, 3)})
    return out


def description(board: dict, timings: list[dict], chapter: Path) -> str:
    rel = chapter.relative_to(ROOT).as_posix()
    lines = [f"# {board.get('video_title', board.get('title', ''))}", "", board.get("summary", ""), "",
             "## Chapters", ""]
    for t in timings:
        lines.append(f"{clock(t['start'])} {t['title']}")
    lines += ["", "## Links", "",
              f"- Lesson, code and practice: `{rel}` in the DipurajThapa/CourseVideos repository.",
              "- Every code example in this video was run and checked by the course verification tool.",
              "", "## Disclosure", "",
              f"The narration is a synthetic voice (Piper text-to-speech, voice {VOICE}). "
              "English captions are included.", ""]
    return "\n".join(lines)


def write_audio(beats: list[dict], path: Path) -> None:
    rate = 22050
    for b in beats:
        if b["wav"]:
            with wave.open(str(b["wav"])) as wf:
                rate = wf.getframerate()
            break
    with wave.open(str(path), "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(rate)
        for b in beats:
            total = round(b["frames"] / FPS * rate)
            lead = round(b["lead"] * rate)
            data = b""
            if b["wav"]:
                with wave.open(str(b["wav"])) as wf:
                    data = wf.readframes(wf.getnframes())
            pcm = b"\0\0" * lead + data
            pcm = pcm[: total * 2] + b"\0\0" * max(0, total - len(pcm) // 2)
            out.writeframes(pcm)


def ffmpeg(args: list[str]) -> None:
    proc = sh(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"] + args)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {proc.stderr[-800:]}")


def encode_scene(stills: list[tuple[Path, float]], out: Path, work: Path) -> float:
    listing = work / (out.stem + ".txt")
    total = sum(d for _, d in stills)
    body = "".join(f"file '{p.as_posix()}'\nduration {d:.6f}\n" for p, d in stills)
    listing.write_text(body + f"file '{stills[-1][0].as_posix()}'\n", encoding="utf-8")
    fade = f"fade=t=in:st=0:d=0.3,fade=t=out:st={max(0, total - 0.3):.3f}:d=0.3"
    tmp = out.with_name(out.stem + ".tmp.mp4")
    ffmpeg(["-f", "concat", "-safe", "0", "-i", str(listing), "-vf", f"fps={FPS},format=yuv420p,{fade}",
            "-t", f"{total:.6f}", "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-tune", "stillimage",
            "-r", str(FPS), "-g", str(FPS * 10), "-pix_fmt", "yuv420p", str(tmp)])
    tmp.rename(out)
    return total


def probe(path: Path) -> dict:
    proc = sh(["ffprobe", "-v", "error", "-show_entries",
               "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate", "-of", "json", str(path)])
    return json.loads(proc.stdout or "{}")


def render(chapter: Path) -> int:
    board = sb.load(chapter)
    problems = sb.validate(chapter, board, chapter_kind(chapter), runnable_set(chapter))
    if problems:
        print("Storyboard problems:\n- " + "\n- ".join(problems))
        return 1
    beats = plan(chapter, board)
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        scene_stills = draw_beats(chapter, board, beats, work)
        parts = []
        for i, stills in enumerate(scene_stills):
            part = work / f"scene{i:02d}.mp4"
            encode_scene(stills, part, work)
            parts.append(part)
        (work / "scenes.txt").write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
        ffmpeg(["-f", "concat", "-safe", "0", "-i", str(work / "scenes.txt"), "-c", "copy", str(work / "video.mp4")])
        write_audio(beats, work / "audio.wav")
        timings = scene_timings(board, beats)
        srt = captions(beats)
        (chapter / sb.CAPTIONS_FILE).write_text(srt, encoding="utf-8")
        meta = [";FFMETADATA1", f"title={board.get('video_title', board.get('title', ''))}"]
        for t in timings:
            meta += ["[CHAPTER]", "TIMEBASE=1/1000", f"START={int(t['start'] * 1000)}", f"END={int(t['end'] * 1000)}",
                     f"title={t['title']}"]
        (work / "meta.txt").write_text("\n".join(meta) + "\n", encoding="utf-8")
        final_tmp = work / "chapter.mp4"
        ffmpeg(["-i", str(work / "video.mp4"), "-i", str(work / "audio.wav"), "-i", str(chapter / sb.CAPTIONS_FILE),
                "-f", "ffmetadata", "-i", str(work / "meta.txt"),
                "-map", "0:v", "-map", "1:a", "-map", "2:s", "-map_metadata", "3", "-map_chapters", "3",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-c:s", "mov_text",
                "-metadata:s:s:0", "language=eng", "-metadata:s:a:0", "language=eng",
                "-movflags", "+faststart", str(final_tmp)])
        shutil.move(str(final_tmp), chapter / sb.VIDEO_FILE)
    video = chapter / sb.VIDEO_FILE
    info = probe(video)
    duration = float(info.get("format", {}).get("duration", 0))
    expected = sum(b["frames"] for b in beats) / FPS
    size_mb = video.stat().st_size / 1e6
    if abs(duration - expected) > 1.0 or size_mb > MAX_MB:
        print(f"render check failed: duration {duration:.2f}s vs planned {expected:.2f}s, size {size_mb:.1f} MB")
        return 1
    model, _ = voice_paths()
    manifest = {
        "chapter_id": board.get("chapter_id"),
        "rendered_at": now_iso(),
        "renderer_version": RENDERER_VERSION,
        "storyboard_sha256": sb.storyboard_sha(chapter),
        "inputs_sha256": sb.inputs_sha(chapter, board),
        "video_sha256": file_sha(video),
        "duration_seconds": round(duration, 3),
        "size_mb": round(size_mb, 2),
        "format": {"width": W, "height": H, "fps": FPS, "video": "h264", "audio": "aac", "captions": "mov_text"},
        "voice": {"engine": f"piper-tts {PIPER_VERSION}", "model": VOICE, "model_sha256": file_sha(model),
                  "length_scale": LENGTH_SCALE},
        "ffmpeg": sh(["ffmpeg", "-version"]).stdout.splitlines()[0],
        "beats": len(beats),
        "pauses": sum(1 for b in beats if b["count"]),
        "scenes": timings,
    }
    save_json(chapter / sb.RENDER_MANIFEST, manifest)
    (chapter / sb.DESCRIPTION_FILE).write_text(description(board, timings, chapter), encoding="utf-8")
    (chapter / sb.SCRIPT_FILE).write_text(sb.script_markdown(board, manifest), encoding="utf-8")
    print(f"Rendered {video.relative_to(ROOT)}: {clock(duration)} ({duration:.1f}s), {size_mb:.1f} MB, "
          f"{len(timings)} scenes, {len(beats)} beats")
    return 0


def preview(chapter: Path, out: Path) -> int:
    from PIL import Image
    board = sb.load(chapter)
    problems = sb.validate(chapter, board, chapter_kind(chapter), runnable_set(chapter))
    for p in problems:
        print("WARN:", p)
    out.mkdir(parents=True, exist_ok=True)
    fake = []
    for scene in board["scenes"]:
        for beat in scene["beats"]:
            fake.append({"scene": scene, "beat": beat, "visual": beat["visual"], "talk_frames": FPS, "count": 0,
                         "frames": FPS, "start_frame": len(fake) * FPS})
    scene_stills = draw_beats(chapter, board, fake, out)
    paths = [p for stills in scene_stills for p, _ in stills]
    cols, tw, th = 4, 480, 270
    for sheet in range(math.ceil(len(paths) / 16)):
        batch = paths[sheet * 16:(sheet + 1) * 16]
        img = Image.new("RGB", (cols * tw, math.ceil(len(batch) / cols) * th), "white")
        for i, p in enumerate(batch):
            img.paste(Image.open(p).resize((tw, th)), ((i % cols) * tw, (i // cols) * th))
        img.save(out / f"contact_{sheet + 1}.png")
    print(f"Drew {len(paths)} beats into {out}; estimated length {clock(sb.estimate_seconds(board))}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("chapter", nargs="?")
    parser.add_argument("--setup", action="store_true")
    parser.add_argument("--preview", metavar="DIR")
    parser.add_argument("--script", action="store_true")
    args = parser.parse_args()
    if args.setup:
        return setup()
    if not args.chapter:
        parser.print_help()
        return 2
    chapter = Path(args.chapter)
    chapter = chapter if chapter.is_absolute() else (ROOT / chapter).resolve()
    if args.preview:
        return preview(chapter, Path(args.preview))
    if args.script:
        manifest = load_json(chapter / sb.RENDER_MANIFEST) if (chapter / sb.RENDER_MANIFEST).exists() else None
        (chapter / sb.SCRIPT_FILE).write_text(sb.script_markdown(sb.load(chapter), manifest), encoding="utf-8")
        return 0
    return render(chapter)


if __name__ == "__main__":
    sys.exit(main())
