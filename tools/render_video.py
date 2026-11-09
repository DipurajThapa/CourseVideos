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

RENDERER_VERSION = "2.0.0"
LUFS = -14                       # web and YouTube loudness target (ai-film-studio B12)
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


def layout_rich(text: str, size: int, width: int, bold: bool = False) -> list[list[tuple[str, str, int]]]:
    """Split rich text into lines of (kind, word, pixel width) that fit `width`."""
    fonts = {"text": font("bold" if bold else "sans", size), "bold": font("bold", size), "code": font("mono", int(size * 0.92))}
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
              line_gap: float = 1.45, bold: bool = False) -> int:
    fonts = {"text": font("bold" if bold else "sans", size), "bold": font("bold", size), "code": font("mono", int(size * 0.92))}
    for line in layout_rich(text, size, width, bold):
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


_TRACES: dict[str, list[str]] = {}


def real_traceback(chapter: Path, rel: str, needle: str) -> list[str]:
    """Standard output before the error plus the full error report, as a learner sees it.

    The run uses the first configured toolchain; the last line must contain the verified
    `.expected_error` text, otherwise only that verified line is shown.
    """
    key = f"{chapter}/{rel}"
    if key not in _TRACES:
        import verify_chapter as vc
        chains = vc.toolchains(chapter.parent.name)
        lines = [needle]
        if chains:
            _, out, err = vc.run_file(chapter / rel, chains[0])
            errs = [x.rstrip() for x in err.rstrip().splitlines() if x.strip()]
            if errs and needle in errs[-1]:
                errs = [re.sub(r'File "[^"]*[/\\]([^/\\"]+)"', r'File "\1"', x) for x in errs]
                lines = [x for x in out.rstrip().splitlines()] + errs
        _TRACES[key] = lines
    return _TRACES[key]


def side_panel_lines(chapter: Path, rel: str) -> list[str]:
    """Every line the side panel can ever show for this file, so its width never changes."""
    stem = (chapter / rel).with_suffix("")
    out = []
    if stem.with_suffix(".expected").exists():
        out += stem.with_suffix(".expected").read_text(encoding="utf-8").split("\n")
    if stem.with_suffix(".expected_error").exists():
        out += real_traceback(chapter, rel, stem.with_suffix(".expected_error").read_text(encoding="utf-8").strip())
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


def digital_timer(d, cx: int, cy: int, value: int, total: int, scale: float = 1.0, dark: bool = True,
                  fraction: float | None = None) -> None:
    """A digital countdown: 00:10 in a pill, with a bar that empties as time runs out."""
    w, h = int(300 * scale), int(118 * scale)
    warn = value <= 3
    fill = "#111827" if dark else C["white"]
    edge = "#F59E0B" if warn else (C["white"] if dark else C["accent"])
    d.rounded_rectangle([cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2], radius=int(26 * scale), fill=fill,
                        outline=edge, width=max(3, int(5 * scale)))
    colour = "#FBBF24" if warn else ("#A7F3D0" if dark else C["accent"])
    d.text((cx, cy - int(6 * scale)), f"00:{value:02d}", font=font("monob", int(70 * scale)), fill=colour, anchor="mm")
    bar_w = w - int(60 * scale)
    bx, by = cx - bar_w // 2, cy + h // 2 - int(20 * scale)
    d.rounded_rectangle([bx, by, bx + bar_w, by + int(8 * scale)], radius=4, fill="#374151" if dark else C["bar"])
    share = value / total if fraction is None else fraction
    if share > 0:
        d.rounded_rectangle([bx, by, bx + max(8, int(bar_w * share)), by + int(8 * scale)], radius=4, fill=colour)


def ask_card(fr: "Frame", box: list[int], question: str, value: int, total: int, fraction: float | None = None) -> None:
    """The question and its timer, together, inside `box`."""
    x0, y0, x1, y1 = box
    fr.d.rounded_rectangle(box, radius=22, fill="#0B3B37", outline="#34D399", width=4)
    fr.d.text((x0 + 34, y0 + 26), "YOUR TURN" if value else "TIME'S UP", font=font("bold", 28), fill="#A7F3D0")
    width = x1 - x0 - 68
    size = 50
    room = (y1 - y0) - 330
    while size > 26 and rich_height(question, size, width, 1.3) > room:
        size -= 2
    qh = rich_height(question, size, width, 1.3)
    y = y0 + 90 + max(0, (room - qh) // 2)
    draw_rich(fr.d, x0 + 34, y, question, size, width, color=C["white"], line_gap=1.3, bold=True)
    if value:
        fr.d.text(((x0 + x1) // 2, y1 - 190), "Pause the video if you need more time.", font=font("sans", 24),
                  fill="#99F6E4", anchor="mm")
    digital_timer(fr.d, (x0 + x1) // 2, y1 - 95, value, total, 0.95, fraction=fraction)


def ask_band(fr: "Frame", question: str, value: int, total: int, fraction: float | None = None) -> None:
    """For slides without a side panel: a band across the bottom with the question and the timer."""
    y0 = H - 250
    fr.d.rectangle([0, y0, W, H - 10], fill="#0B3B37")
    fr.d.text((60, y0 + 28), "YOUR TURN" if value else "TIME'S UP", font=font("bold", 28), fill="#A7F3D0")
    y = y0 + 76
    for line in layout_rich(question, 40, W - 560)[:3]:
        fr.d.text((60, y), "".join(w for _, w, _ in line), font=font("bold", 40), fill=C["white"])
        y += 52
    digital_timer(fr.d, W - 230, y0 + 120, value, total, 1.0, fraction=fraction)


def draw_code_beat(fr: "Frame", chapter: Path, v: dict, ask: dict | None = None) -> None:
    top = fr.heading(v.get("heading", ""), size=46) if v.get("heading") else 96
    if v.get("note"):
        top = draw_rich(fr.d, 60, top - 6, v["note"], 30, W - 120, color=C["muted"]) + 8
    src_path = chapter / v["file"]
    source = src_path.read_text(encoding="utf-8").rstrip("\n")
    code_lines = token_colours(src_path, source)
    visible = int(v.get("lines") or len(code_lines))
    bottom = H - 60
    stem = src_path.with_suffix("")
    side_lines = side_panel_lines(chapter, v["file"])
    side_chars = max([30] + [len(x) for x in side_lines])
    side_w = int(min(860, max(600, side_chars * 26 * 0.602 + 80)))
    band = bool(ask) and bool(v.get("output") or v.get("error"))
    bottom = H - 300 if band else H - 60
    split = W - 60 - side_w - 30
    code_box = [60, top, split, bottom]
    out_box = [split + 30, top, W - 60, bottom]
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
        if number > visible:
            break
        lit = number in highlight
        if lit:
            fr.d.rectangle([code_box[0] + 8, y - 4, code_box[2] - 8, y + size * 1.3], fill=C["hl"])
            fr.d.rectangle([code_box[0] + 8, y - 4, code_box[0] + 16, y + size * 1.3], fill="#F59E0B")
            fr.d.text((code_box[2] - 24, y + size * 0.62), "◀", font=font("bold", int(size * 0.8)),
                      fill="#F59E0B", anchor="rm")
        dim = bool(highlight) and not lit
        fr.d.text((code_box[0] + 26, y), f"{number:>2}", font=mono, fill="#F59E0B" if lit else C["gutter"])
        x = code_box[0] + 26 + size * 0.602 * 4
        for piece, colour in line:
            fr.d.text((x, y), piece, font=mono, fill=_mute(colour) if dim else colour)
            x += mono.getlength(piece)
        if number == visible and visible < len(code_lines):
            fr.d.rectangle([x + 4, y, x + 4 + size * 0.55, y + size * 1.2], fill="#E5E7EB")  # typing cursor
        y += int(size * 1.45)
    if ask and not band:
        ask_card(fr, out_box, ask["question"], ask["value"], ask["total"], ask.get("fraction"))
        return
    if band:
        ask_band(fr, ask["question"], ask["value"], ask["total"], ask.get("fraction"))
    focus_out = set(v.get("out_highlight", []))
    if v.get("error"):
        n_lines = len(real_traceback(chapter, v["file"], (chapter / v["error"]).read_text(encoding="utf-8").strip()))
        focus_out = {k if k > 0 else n_lines + 1 + k for k in focus_out}
        lines = real_traceback(chapter, v["file"], (chapter / v["error"]).read_text(encoding="utf-8").strip())
        panel(fr.d, out_box, "Error", C["err"], C["out_bg"])
        lit_err = {f"line {n}" for n in v.get("err_highlight", [])}
        body = [(line, C["err"] if i == len(lines) - 1 else "#E5E7EB",
                 any(f"{key}," in line or line.rstrip().endswith(key) for key in lit_err) or (i + 1) in focus_out)
                for i, line in enumerate(lines)]
    elif v.get("output"):
        text = (chapter / v["output"]).read_text(encoding="utf-8").rstrip("\n").split("\n")
        panel(fr.d, out_box, "Output", "#A3E635", C["out_bg"])
        body = [(line, C["out_fg"], i + 1 in focus_out) for i, line in enumerate(text[: int(v.get("out_lines") or len(text))])]
    else:
        panel(fr.d, out_box, "Output", "#A3E635", C["out_bg"])
        draw_rich(fr.d, out_box[0] + 30, (out_box[1] + out_box[3]) // 2 - 60,
                  v.get("hidden_text", "Predict the output, then run it."), 32,
                  out_box[2] - out_box[0] - 60, color="#9CA3AF")
        return
    width = out_box[2] - out_box[0] - 100          # room on the right for the highlight marker
    osize = 32
    is_error = bool(v.get("error"))
    floor = 26 if is_error else 14
    while True:
        chars = max(10, int(width / (osize * 0.602)))
        # outputs never wrap (a wrapped line looks like two lines); error reports may
        rows = [(seg, colour, lit) for line, colour, lit in body
                for seg in (wrap_plain(line, chars) if is_error else [line])]
        longest = max((len(r[0]) for r in rows), default=1)
        fits = len(rows) * osize * 1.5 <= out_box[3] - out_box[1] - 90
        if (fits and (is_error or longest <= chars)) or osize <= floor:
            break
        osize -= 1
    omono = font("mono", osize)
    any_lit = any(lit for _, _, lit in rows)
    y = out_box[1] + 70
    for line, colour, lit in rows:
        if lit:
            fr.d.rectangle([out_box[0] + 8, y - 4, out_box[2] - 8, y + osize * 1.3], fill="#3A4255")
            fr.d.rectangle([out_box[0] + 8, y - 4, out_box[0] + 16, y + osize * 1.3], fill="#F59E0B")
            fr.d.text((out_box[2] - 22, y + osize * 0.62), "\u25c0", font=font("bold", int(osize * 0.8)),
                      fill="#F59E0B", anchor="rm")
        shade = colour if (lit or not any_lit) else _mute(colour, (0x10, 0x14, 0x18))
        fr.d.text((out_box[0] + 30, y), line, font=omono, fill=shade)
        y += int(osize * 1.5)


def _mute(colour: str, bg: tuple = (0x1E, 0x22, 0x30)) -> str:
    """Dim a colour towards the panel background so the highlighted line stands out."""
    colour = colour.lstrip("#")
    r, g, b = (int(colour[i:i + 2], 16) for i in (0, 2, 4))
    k = 0.55
    return "#%02x%02x%02x" % tuple(int(bg[i] + (c - bg[i]) * k) for i, c in enumerate((r, g, b)))


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
        focus = v.get("focus_row")
        lit = focus is not None and r == focus + 1
        fr.d.rectangle([60, y, 60 + table_w, y + hgt], fill=C["table_head"] if r == 0 else
                       ("#FEF3C7" if lit else (C["white"] if r % 2 else C["bg"])))
        if lit:
            fr.d.rectangle([60, y, 70, y + hgt], fill="#F59E0B")
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
    focus = v.get("focus", reveal - 1 if reveal < len(items) else None)
    size = 46
    while size > 24 and sum(rich_height(i, size, W - 260) + 34 for i in items) > H - top - 80:
        size -= 2
    y = settle(top, sum(rich_height(i, size, W - 260) + 34 for i in items))
    for index, item in enumerate(items[:reveal]):
        h = rich_height(item, size, W - 260)
        lit = focus == index
        if lit:
            fr.d.rounded_rectangle([90, y - 12, W - 60, y + h + 2], radius=14, fill="#FEF3C7")
            fr.d.rectangle([90, y - 12, 100, y + h + 2], fill="#F59E0B")
        dot = C["accent"] if (lit or focus is None) else C["muted"]
        fr.d.ellipse([120, y + size * 0.35, 120 + size * 0.45, y + size * 0.8], fill=dot)
        colour = C["ink"] if (lit or focus is None) else C["muted"]
        y = draw_rich(fr.d, 180, y, item, size, W - 260, color=colour) + 34


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
        lit = v.get("focus") == "pre"
        fr.d.rounded_rectangle([60, y + 10, 60 + box_w, y + 10 + box_h], radius=18,
                               fill="#FFFBEB" if lit else C["white"], outline="#F59E0B" if lit else C["rule"],
                               width=5 if lit else 2)
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
    text = v["prompt"]
    if v.get("focus") is not None and v["focus"] != "check":
        parts = re.split(r"(?<=[.!?])\s+", text)
        k = int(v["focus"])
        text = " ".join(f"**{re.sub('`', '', p)}**" if i == k else p for i, p in enumerate(parts))
    prompt_h = rich_height(text, 40, W - 260) + 70
    fr.d.rounded_rectangle([60, top, W - 60, top + prompt_h], radius=20, fill=C["white"], outline=C["accent"],
                           width=3)
    fr.d.text((88, top + 6), "“", font=font("bold", 80), fill=C["accent"])
    if v.get("focus") is not None and v["focus"] != "check":
        fr.d.rectangle([60, top, 72, top + prompt_h], fill="#F59E0B")
    y = draw_rich(fr.d, 150, top + 35, text, 40, W - 260)
    y = max(y, top + prompt_h) + 30
    if v.get("check"):
        lit = v.get("focus") == "check"
        if lit:
            ch = rich_height("**Check it:** " + v["check"], 36, W - 140)
            fr.d.rounded_rectangle([50, y - 12, W - 60, y + ch], radius=14, fill="#FEF3C7")
            fr.d.rectangle([50, y - 12, 60, y + ch], fill="#F59E0B")
        draw_rich(fr.d, 80 if lit else 60, y, "**Check it:** " + v["check"], 36, W - 140,
                  color=C["ink"] if lit else C["muted"])


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


def draw_pause(fr: "Frame", v: dict, ask: dict | None) -> None:
    """A question card. The question stays on screen above its timer the whole time."""
    question = ask["question"] if ask else v["question"]
    qlines = layout_rich(question, 60, W - 360)
    y = 330 - len(qlines) * 42
    fr.d.text((W // 2, y - 90), "PAUSE AND THINK", font=font("bold", 36), fill="#A7F3D0", anchor="mm")
    for line in qlines:
        fr.d.text((W // 2, y), "".join(w for _, w, _ in line), font=font("bold", 60), fill=C["white"], anchor="ma")
        y += 84
    if v.get("hint"):
        draw_rich(fr.d, 260, y + 20, f"Hint: {v['hint']}", 36, W - 520, color="#CCFBF1")
    if ask:
        digital_timer(fr.d, W // 2, min(y + 230, H - 150), ask["value"], ask["total"], 1.3, fraction=ask.get("fraction"))


def draw_quiz(fr: "Frame", v: dict, ask: dict | None) -> None:
    fr.d.text((60, 100), "QUICK CHECK", font=font("bold", 30), fill=C["accent"])
    y = draw_rich(fr.d, 60, 150, v["question"], 50, W - 520, line_gap=1.3) + 30
    if ask:
        digital_timer(fr.d, W - 230, 200, ask["value"], ask["total"], 1.0, dark=False, fraction=ask.get("fraction"))
    revealed = v.get("revealed")
    letters = "ABCD"
    for i, option in enumerate(v["options"]):
        right = revealed and i == v["answer"]
        wrong = revealed and i != v["answer"]
        h = rich_height(option, 40, W - 400) + 44
        fill = "#DCFCE7" if right else ("#EFEEE8" if wrong else C["white"])
        edge = "#16A34A" if right else (C["rule"] if wrong else C["accent"])
        fr.d.rounded_rectangle([60, y, W - 60, y + h], radius=20, fill=fill, outline=edge, width=4 if right else 2)
        fr.d.ellipse([90, y + h // 2 - 32, 154, y + h // 2 + 32], fill=edge)
        fr.d.text((122, y + h // 2), letters[i], font=font("bold", 36), fill=C["white"], anchor="mm")
        draw_rich(fr.d, 190, y + 22, option, 40, W - 400, color=C["muted"] if wrong else C["ink"])
        if right:
            fr.d.text((W - 110, y + h // 2), "✔", font=font("bold", 56), fill="#16A34A", anchor="mm")
        y += h + 22
    if revealed and v.get("explain"):
        draw_rich(fr.d, 60, y + 10, "**Why:** " + v["explain"], 36, W - 120, color=C["ink"])


def draw_breather(fr: "Frame", v: dict, ctx: dict, section: str) -> None:
    fr.d.text((120, 150), v.get("label", "BREATHER"), font=font("bold", 32), fill=C["accent"])
    fr.d.text((120, 200), v.get("title", "Take a breath. You have learned:"), font=font("bold", 58), fill=C["ink"])
    y = 330
    for item in v["items"]:
        fr.d.ellipse([120, y + 4, 172, y + 56], fill=C["accent"])
        fr.d.text((146, y + 30), "✔", font=font("bold", 32), fill=C["white"], anchor="mm")
        y = draw_rich(fr.d, 200, y + 6, item, 40, 1000) + 34
    # progress map of the chapter sections
    x0, top = 1320, 170
    fr.d.rounded_rectangle([x0 - 40, top - 40, W - 80, H - 120], radius=26, fill=C["white"], outline=C["rule"], width=2)
    fr.d.text((x0, top), "YOUR PROGRESS", font=font("bold", 26), fill=C["muted"])
    sections = ctx["sections"]
    done_until = sections.index(section) if section in sections else -1
    yy = top + 60
    step = min(64, (H - 220 - yy) // max(1, len(sections)))
    for i, name in enumerate(sections):
        done = i <= done_until
        fr.d.ellipse([x0, yy + 6, x0 + 30, yy + 36], fill=C["accent"] if done else C["bar"])
        if done:
            fr.d.text((x0 + 15, yy + 21), "✔", font=font("bold", 18), fill=C["white"], anchor="mm")
        fr.d.text((x0 + 50, yy + 4), name, font=font("bold" if i == done_until else "sans", 28),
                  fill=C["ink"] if done else C["muted"])
        yy += step


def draw_visual(fr: "Frame", chapter: Path, v: dict, ask: dict | None = None, section: str = "") -> None:
    kind = v["type"]
    side_ask = None
    if kind == "code":
        draw_code_beat(fr, chapter, v, ask)
        return
    if kind == "pause":
        draw_pause(fr, v, ask)
        return
    if kind == "quiz":
        draw_quiz(fr, v, ask)
        return
    if kind == "breather":
        draw_breather(fr, v, fr.ctx, section)
    elif kind == "table":
        draw_table(fr, v)
    elif kind == "bullets":
        draw_bullets(fr, v)
    elif kind == "text":
        draw_text(fr, v)
    elif kind == "prompt":
        draw_prompt(fr, v)
    elif kind in ("title", "end"):
        draw_title(fr, v)
    if ask:
        ask_band(fr, ask["question"], ask["value"], ask["total"], ask.get("fraction"))


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


def plan(chapter: Path, board: dict, synth: bool = True) -> list[dict]:
    """Expand every beat into timed states: one picture each, with its audio and caption.

    With synth=False (preview) durations are estimates and no audio is made.
    """
    states: list[dict] = []
    for scene in board["scenes"]:
        for b_index, beat in enumerate(scene["beats"]):
            ph = sb.phases(beat)
            for p_index, phase in enumerate(ph):
                last = p_index == len(ph) - 1
                base = {"scene": scene, "visual": phase["visual"], "ask": None, "wav": None, "lead": 0.0,
                        "speech": 0.0, "text": "", "sound": None, "blend": True}
                if phase["kind"] == "say":
                    lead = (0.2 if b_index == 0 else 0.1) if p_index == 0 else 0.0
                    wav = synthesize(phase["text"]) if (synth and phase["text"]) else None
                    speech = wav_seconds(wav) if wav else len(phase["text"].split()) / sb.WORDS_PER_SECOND
                    scene_end = last and b_index == len(scene["beats"]) - 1
                    gap = 0.35 if scene_end else (sb.BEAT_GAP_SECONDS if last else sb.SEGMENT_GAP_SECONDS)
                    states.append({**base, "wav": wav, "lead": lead, "speech": speech, "text": phase["text"],
                                   "frames": frames(lead + speech + gap)})
                elif phase["kind"] == "ask":
                    total = phase["seconds"]
                    steps = TIMER_STEPS if synth else 1
                    for k in range(total * steps + 1):
                        remaining = total - k / steps
                        value = math.ceil(remaining - 1e-9)
                        states.append({**base, "ask": {"question": phase["question"], "value": value, "total": total,
                                                       "fraction": remaining / total},
                                       "sound": ("tick" if value else "done") if k % steps == 0 else None,
                                       "blend": k == 0, "frames": frames(1.0 / steps if remaining > 0 else 0.8)})
                else:
                    states.append({**base, "sound": "pad", "blend": False, "frames": frames(phase["seconds"])})
    start = 0
    for s in states:
        s["start_frame"] = start
        start += s["frames"]
    return states


def context(chapter: Path, board: dict) -> dict:
    language = chapter.parent.name
    display = load_json(ROOT / "curriculum" / f"{language}.json").get("display_name", language.title())
    wanted = sb.PROJECT_SECTIONS if chapter_kind(chapter) == "project" else sb.LESSON_SECTIONS
    return {"brand": f"CODE QUEST  ·  {display}  ·  Chapter {board.get('number', '')}", "sections": wanted}


def state_key(s: dict) -> str:
    return json.dumps([s["scene"]["section"], s["visual"], s["ask"]], sort_keys=True, default=str)


def draw_states(chapter: Path, board: dict, states: list[dict], out: Path) -> None:
    """Draw one PNG per distinct picture; states that look the same share a file."""
    ctx = context(chapter, board)
    total = sum(s["frames"] for s in states)
    cache: dict[str, Path] = {}
    for n, s in enumerate(states):
        progress = s["start_frame"] / total
        key = state_key(s) + f"|{round(progress, 2)}"
        if key in cache:
            s["png"] = cache[key]
            continue
        v = s["visual"]
        dark = v["type"] == "pause"
        bg = C["pause_bg"] if dark else ("#EEF6F2" if v["type"] == "breather" else C["bg"])
        fr = Frame(ctx, s["scene"]["section"], bg)
        fr.chrome(progress, dark)
        draw_visual(fr, chapter, v, s["ask"], s["scene"]["section"])
        path = out / f"s{n:04d}.png"
        fr.img.save(path, "PNG", compress_level=1)
        cache[key] = path
        s["png"] = path


# ---------------------------------------------------------------- outputs

def srt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def caption_cues(text: str, max_line: int = 42) -> list[list[str]]:
    """Break text into cues of at most two lines of 42 characters, preferring clause ends."""
    cues: list[list[str]] = []
    for sentence in re.split(r"(?<=[.!?])\s+", text.strip()):
        lines, cur = [], ""
        for word in sentence.split():
            if cur and len(cur) + 1 + len(word) > max_line:
                lines.append(cur)
                cur = word
            else:
                cur = f"{cur} {word}".strip()
        if cur:
            lines.append(cur)
        for i in range(0, len(lines), 2):
            cues.append(lines[i:i + 2])
    return cues


def captions(states: list[dict]) -> str:
    out, n = [], 0
    for s in states:
        if not s["text"]:
            continue
        cues = caption_cues(s["text"])
        chars = sum(len(" ".join(c)) for c in cues) or 1
        t = s["start_frame"] / FPS + s["lead"]
        state_end = (s["start_frame"] + s["frames"]) / FPS
        for k, cue in enumerate(cues):
            d = s["speech"] * len(" ".join(cue)) / chars
            shown = d
            if k == len(cues) - 1:
                shown = min(max(d, len(" ".join(cue)) / 18), state_end - t)
            n += 1
            out += [str(n), f"{srt_time(t)} --> {srt_time(t + max(shown, 0.05) - 0.02)}", "\n".join(cue), ""]
            t += d
    return "\n".join(out)


def clock(seconds: float) -> str:
    seconds = int(seconds)
    return f"{seconds // 60}:{seconds % 60:02d}"


def scene_timings(board: dict, states: list[dict]) -> list[dict]:
    out = []
    for scene in board["scenes"]:
        own = [s for s in states if s["scene"] is scene]
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
    lines += ["", "## How to use this video", "",
              "- When a question appears with a 10-second timer, pause the video if you need more time.",
              "- Say or write your answer before the reveal. Breather cards are a moment to rest and review.",
              "", "## Links", "",
              f"- Lesson, code and practice: `{rel}` in the DipurajThapa/CourseVideos repository.",
              "- Every code example in this video was run and checked by the course verification tool.",
              "", "## Disclosure", "",
              f"The narration is a synthetic voice (Piper text-to-speech, voice {VOICE}). The timer ticks and the "
              "soft tone on breather cards are generated in code. English captions are included.", ""]
    return "\n".join(lines)


def _tone(rate: int, seconds: float, freqs: list[float], amp: float, decay: float | None = None):
    import numpy as np
    t = np.arange(int(rate * seconds)) / rate
    wave_ = sum(np.sin(2 * np.pi * f * t) for f in freqs) / len(freqs)
    if decay:
        env = np.exp(-t / decay)
    else:
        fade = min(len(t) // 3, int(rate * 0.8))
        env = np.ones_like(t)
        env[:fade] = np.linspace(0, 1, fade)
        env[-fade:] = np.linspace(1, 0, fade)
    return (amp * wave_ * env).astype(np.float32)


def write_audio(states: list[dict], path: Path) -> None:
    import numpy as np
    rate = 22050
    for s in states:
        if s["wav"]:
            with wave.open(str(s["wav"])) as wf:
                rate = wf.getframerate()
            break
    total = sum(s["frames"] for s in states)
    track = np.zeros(int(total / FPS * rate) + rate, dtype=np.float32)
    tick = _tone(rate, 0.06, [1320], 0.10, decay=0.012)
    done = np.concatenate([_tone(rate, 0.12, [880], 0.12, decay=0.05), _tone(rate, 0.25, [1175], 0.12, decay=0.08)])
    for s in states:
        at = int(s["start_frame"] / FPS * rate)
        if s["wav"]:
            with wave.open(str(s["wav"])) as wf:
                pcm = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
            st = at + int(s["lead"] * rate)
            track[st:st + len(pcm)] += pcm[: len(track) - st]
        elif s["sound"] in ("tick", "done"):
            snd = tick if s["sound"] == "tick" else done
            track[at:at + len(snd)] += snd[: len(track) - at]
        elif s["sound"] == "pad":
            snd = _tone(rate, s["frames"] / FPS, [220.0, 277.18, 329.63], 0.035)
            track[at:at + len(snd)] += snd[: len(track) - at]
    track = track[: int(total / FPS * rate)]
    pcm16 = (np.clip(track, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(rate)
        out.writeframes(pcm16.tobytes())


def ffmpeg(args: list[str]) -> None:
    proc = sh(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"] + args)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {proc.stderr[-800:]}")


BLEND_FRAMES = 7
TIMER_STEPS = 5                 # the timer bar drains five times a second


def encode_scene(states: list[dict], out: Path, work: Path) -> float:
    """Encode one scene. A short crossfade eases each change of picture (not timer ticks)."""
    from PIL import Image
    entries: list[tuple[Path, float]] = []
    prev = None
    for s in states:
        n = s["frames"]
        if prev is not None and s["blend"] and prev != s["png"] and n > BLEND_FRAMES + 2:
            a, b = Image.open(prev).convert("RGB"), Image.open(s["png"]).convert("RGB")
            for k in range(1, BLEND_FRAMES + 1):
                p = work / f"bl_{s['png'].stem}_{prev.stem}_{k}.png"
                if not p.exists():
                    Image.blend(a, b, k / (BLEND_FRAMES + 1)).save(p, "PNG", compress_level=1)
                entries.append((p, 1 / FPS))
            n -= BLEND_FRAMES
        entries.append((s["png"], n / FPS))
        prev = s["png"]
    listing = work / (out.stem + ".txt")
    total = sum(s["frames"] for s in states) / FPS
    body = "".join(f"file '{p.as_posix()}'\nduration {d:.6f}\n" for p, d in entries)
    listing.write_text(body + f"file '{entries[-1][0].as_posix()}'\n", encoding="utf-8")
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
    states = plan(chapter, board)
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        draw_states(chapter, board, states, work)
        parts = []
        for i, scene in enumerate(board["scenes"]):
            part = work / f"scene{i:02d}.mp4"
            encode_scene([s for s in states if s["scene"] is scene], part, work)
            parts.append(part)
        (work / "scenes.txt").write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
        ffmpeg(["-f", "concat", "-safe", "0", "-i", str(work / "scenes.txt"), "-c", "copy", str(work / "video.mp4")])
        write_audio(states, work / "audio.wav")
        timings = scene_timings(board, states)
        (chapter / sb.CAPTIONS_FILE).write_text(captions(states), encoding="utf-8")
        meta = [";FFMETADATA1", f"title={board.get('video_title', board.get('title', ''))}"]
        for t in timings:
            meta += ["[CHAPTER]", "TIMEBASE=1/1000", f"START={int(t['start'] * 1000)}", f"END={int(t['end'] * 1000)}",
                     f"title={t['title']}"]
        (work / "meta.txt").write_text("\n".join(meta) + "\n", encoding="utf-8")
        final_tmp = work / "chapter.mp4"
        ffmpeg(["-i", str(work / "video.mp4"), "-i", str(work / "audio.wav"), "-i", str(chapter / sb.CAPTIONS_FILE),
                "-f", "ffmetadata", "-i", str(work / "meta.txt"),
                "-map", "0:v", "-map", "1:a", "-map", "2:s", "-map_metadata", "3", "-map_chapters", "3",
                "-c:v", "copy", "-af", f"loudnorm=I={LUFS}:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k",
                "-ar", "48000", "-c:s", "mov_text",
                "-metadata:s:s:0", "language=eng", "-metadata:s:a:0", "language=eng",
                "-movflags", "+faststart", str(final_tmp)])
        shutil.move(str(final_tmp), chapter / sb.VIDEO_FILE)
    video = chapter / sb.VIDEO_FILE
    info = probe(video)
    duration = float(info.get("format", {}).get("duration", 0))
    expected = sum(s["frames"] for s in states) / FPS
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
        "format": {"width": W, "height": H, "fps": FPS, "video": "h264", "audio": "aac", "captions": "mov_text",
                   "loudness_lufs": LUFS},
        "voice": {"engine": f"piper-tts {PIPER_VERSION}", "model": VOICE, "model_sha256": file_sha(model),
                  "length_scale": LENGTH_SCALE},
        "ffmpeg": sh(["ffmpeg", "-version"]).stdout.splitlines()[0],
        "states": len(states),
        "questions": sum(1 for _, b in sb.beats(board) if sb.ask_of(b)),
        "breathers": sum(1 for _, b in sb.beats(board) if b["visual"]["type"] == "breather"),
        "scenes": timings,
    }
    save_json(chapter / sb.RENDER_MANIFEST, manifest)
    (chapter / sb.DESCRIPTION_FILE).write_text(description(board, timings, chapter), encoding="utf-8")
    (chapter / sb.SCRIPT_FILE).write_text(sb.script_markdown(board, manifest), encoding="utf-8")
    print(f"Rendered {video.relative_to(ROOT)}: {clock(duration)} ({duration:.1f}s), {size_mb:.1f} MB, "
          f"{len(timings)} scenes, {len(states)} states, {manifest['questions']} questions, "
          f"{manifest['breathers']} breathers")
    return 0


def preview(chapter: Path, out: Path) -> int:
    """Draw every distinct picture (first and last timer frame only) and contact sheets, without audio."""
    from PIL import Image
    board = sb.load(chapter)
    problems = sb.validate(chapter, board, chapter_kind(chapter), runnable_set(chapter))
    for p in problems:
        print("WARN:", p)
    out.mkdir(parents=True, exist_ok=True)
    states = [s for s in plan(chapter, board, synth=False)
              if not s["ask"] or s["ask"]["value"] in (s["ask"]["total"], 3, 0)]
    draw_states(chapter, board, states, out)
    paths = list(dict.fromkeys(s["png"] for s in states))
    cols, tw, th = 4, 480, 270
    for sheet in range(math.ceil(len(paths) / 16)):
        batch = paths[sheet * 16:(sheet + 1) * 16]
        img = Image.new("RGB", (cols * tw, math.ceil(len(batch) / cols) * th), "white")
        for i, p in enumerate(batch):
            img.paste(Image.open(p).resize((tw, th)), ((i % cols) * tw, (i // cols) * th))
        img.save(out / f"contact_{sheet + 1}.png")
    print(f"Drew {len(paths)} pictures into {out}; estimated length {clock(sb.estimate_seconds(board))}")
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
