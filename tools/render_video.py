#!/usr/bin/env python3
"""Render a chapter's full walkthrough video from video/storyboard.json.

Usage:
  python3 tools/render_video.py --setup                    install and check the video toolchain
  python3 tools/render_video.py <chapter-dir> --preview DIR draw every beat as a PNG plus a contact sheet
  python3 tools/render_video.py <chapter-dir>               render the video (writes the files below)
  python3 tools/render_video.py <chapter-dir> --script      only regenerate video/script.md
  python3 tools/render_video.py <chapter-dir> --sample F    render only the first 60 s to F (for an early look)

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

RENDERER_VERSION = "3.0.0"
LUFS = -14                       # web and YouTube loudness target (ai-film-studio B12)
W, H, FPS = 1920, 1080, 30
PIPER_VERSION = "1.8.0"
VOICE = "en_US-john-medium"     # deep, calm male voice chosen by the owner from three tested voices (2026-11-09)
VOICE_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/john/medium/"
VOICE_SHA256 = "789c6c875726e627ddee93d51d8727859abe9c091c3d141591f4b83c2072e988"
LENGTH_SCALE = "1.1"            # calm, unhurried pace for second-language listeners
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
    for module, package in (("PIL", "pillow"), ("pygments", "pygments"), ("numpy", "numpy")):
        try:
            __import__(module)
        except ImportError:
            sh([sys.executable, "-m", "pip", "install", "--quiet", "--break-system-packages", package])
            try:
                __import__(module)
            except ImportError:
                problems.append(f"could not install {package}")
    import video_theme
    for name in video_theme.REQUIRED_FONTS:
        if not (FONTS / name).exists():
            problems.append(f"missing font {name}")
    if not problems:
        import voice
        problems += voice.setup()
    if problems:
        print("\n".join(problems))
        return 1
    import voice
    ffmpeg_v = sh(["ffmpeg", "-version"]).stdout.splitlines()[0].split(" ")[2]
    d = voice.describe()
    print(f"ffmpeg {ffmpeg_v}, {d['engine']}, voice {d['voice']}")
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
# All screen design lives in tools/video_theme.py.
import video_theme as theme  # noqa: E402

real_traceback = theme.real_traceback


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

    Consecutive spoken segments of a beat form one "run", spoken in a single take (tools/voice.py),
    so the narration flows. Each segment's state plays its slice of that take.
    With synth=False (preview) durations are estimates and no audio is made.
    """
    import voice
    states: list[dict] = []
    for scene in board["scenes"]:
        for b_index, beat in enumerate(scene["beats"]):
            ph = sb.phases(beat)
            i = 0
            while i < len(ph):
                phase = ph[i]
                base = {"scene": scene, "visual": phase["visual"], "ask": None, "wav": None, "lead": 0.0,
                        "speech": 0.0, "text": "", "sound": None, "blend": True, "slice": None}
                if phase["kind"] == "say":
                    j = i
                    while j < len(ph) and ph[j]["kind"] == "say":
                        j += 1
                    run = ph[i:j]
                    texts = [p["text"] for p in run]
                    spoken_texts = [x for x in texts if x]
                    if synth and spoken_texts:
                        wav, slices = voice.synth_run(spoken_texts)
                    else:
                        wav, slices = None, None
                    k = 0
                    for r_index, p in enumerate(run):
                        lead = (0.25 if b_index == 0 else 0.12) if (r_index == 0 and i == 0) else (0.08 if r_index == 0 else 0.0)
                        if p["text"] and slices:
                            a0, a1 = slices[k]
                            k += 1
                            speech = a1 - a0
                            sl = (a0, a1)
                        else:
                            speech = len(p["text"].split()) / sb.WORDS_PER_SECOND if p["text"] else 0.6
                            sl = None
                        run_end = r_index == len(run) - 1
                        beat_end = run_end and j == len(ph)
                        scene_end = beat_end and b_index == len(scene["beats"]) - 1
                        gap = 0.3 if scene_end else (0.45 if run_end else (0.0 if synth else 0.3))
                        states.append({**base, "visual": p["visual"], "wav": wav if sl else None, "slice": sl,
                                       "lead": lead, "speech": speech, "text": p["text"],
                                       "frames": frames(lead + speech + gap)})
                    i = j
                    continue
                if phase["kind"] == "ask":
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
                i += 1
    start = 0
    for s in states:
        s["start_frame"] = start
        start += s["frames"]
    return states


def context(chapter: Path, board: dict) -> dict:
    language = chapter.parent.name
    display = load_json(ROOT / "curriculum" / f"{language}.json").get("display_name", language.title())
    wanted = sb.PROJECT_SECTIONS if chapter_kind(chapter) == "project" else sb.LESSON_SECTIONS
    return {"brand": f"Code Quest  ·  {display}", "language": display, "number": board.get("number", 0),
            "sections": wanted}


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
        img = theme.render_state(ctx, chapter, s["scene"]["section"], s["visual"], s["ask"], progress)
        path = out / f"s{n:04d}.png"
        img.save(path, "PNG", compress_level=1)
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
              f"The narration is a synthetic voice ({__import__('voice').describe()['engine']}, voice "
              f"{__import__('voice').describe()['voice']}). The timer ticks, the breather tone and the quiet background "
              "pad are generated in code. English captions are included.", ""]
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


def _ambient_bed(rate: int, seconds: float):
    """A very quiet, slowly moving pad under the whole video, so there is never dead silence
    between lines. Generated in code (no licence needed), about 40 dB below the voice."""
    import numpy as np
    n = int(rate * seconds)
    tt = np.arange(n) / rate
    chords = [[110.0, 164.81, 220.0, 277.18], [98.0, 146.83, 196.0, 246.94],
              [87.31, 130.81, 174.61, 220.0], [98.0, 146.83, 196.0, 293.66]]
    bed = np.zeros(n, dtype=np.float32)
    span = 8.0
    for c, freqs in enumerate(chords):
        env = np.clip(1 - np.abs(((tt / span - c) % len(chords)) - 0.5) * 1.6, 0, 1) ** 2
        for f in freqs:
            bed += (np.sin(2 * np.pi * f * tt) + 0.5 * np.sin(2 * np.pi * f * 1.003 * tt)).astype(np.float32) * env
    bed *= 0.0025 * (1 + 0.25 * np.sin(2 * np.pi * tt / 11.0))
    return bed.astype(np.float32)


def write_audio(states: list[dict], path: Path) -> None:
    import numpy as np
    rate = 24000
    for s in states:
        if s["wav"]:
            with wave.open(str(s["wav"])) as wf:
                rate = wf.getframerate()
            break
    total = sum(s["frames"] for s in states)
    track = np.zeros(int(total / FPS * rate) + rate, dtype=np.float32)
    tick = _tone(rate, 0.06, [1320], 0.10, decay=0.012)
    done = np.concatenate([_tone(rate, 0.12, [880], 0.12, decay=0.05), _tone(rate, 0.25, [1175], 0.12, decay=0.08)])
    takes: dict[str, np.ndarray] = {}
    for s in states:
        at = int(s["start_frame"] / FPS * rate)
        if s["wav"] and s.get("slice"):
            key = str(s["wav"])
            if key not in takes:
                with wave.open(key) as wf:
                    takes[key] = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
            a0, a1 = s["slice"]
            pcm = takes[key][int(a0 * rate):int(a1 * rate)]
            st = at + int(s["lead"] * rate)
            track[st:st + len(pcm)] += pcm[: max(0, len(track) - st)]
        elif s["sound"] in ("tick", "done"):
            snd = tick if s["sound"] == "tick" else done
            track[at:at + len(snd)] += snd[: len(track) - at]
        elif s["sound"] == "pad":
            snd = _tone(rate, s["frames"] / FPS, [220.0, 277.18, 329.63], 0.03)
            track[at:at + len(snd)] += snd[: len(track) - at]
    track = track[: int(total / FPS * rate)]
    track += _ambient_bed(rate, len(track) / rate)[: len(track)]
    pcm16 = (np.clip(track, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(rate)
        out.writeframes(pcm16.tobytes())


# A light vocal polish: remove rumble, add a little warmth and presence, even out the level,
# then normalise to the web loudness target.
VOICE_CHAIN = ("highpass=f=70,equalizer=f=170:t=q:w=1:g=1.5,equalizer=f=3200:t=q:w=1.2:g=2.5,"
               "acompressor=threshold=-21dB:ratio=2.5:attack=12:release=180:makeup=2,"
               f"loudnorm=I={LUFS}:TP=-2:LRA=9")


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


def render_sample(chapter: Path, out: Path, seconds: float) -> int:
    """Render only the opening `seconds` of the video to `out`, for an early look. Writes nothing in the chapter."""
    board = sb.load(chapter)
    states = []
    for s in plan(chapter, board):
        if s["start_frame"] / FPS >= seconds:
            break
        states.append(s)
    scenes = [sc for sc in board["scenes"] if any(s["scene"] is sc for s in states)]
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        draw_states(chapter, board, states, work)
        parts = []
        for i, scene in enumerate(scenes):
            part = work / f"scene{i:02d}.mp4"
            encode_scene([s for s in states if s["scene"] is scene], part, work)
            parts.append(part)
        (work / "scenes.txt").write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
        ffmpeg(["-f", "concat", "-safe", "0", "-i", str(work / "scenes.txt"), "-c", "copy", str(work / "video.mp4")])
        write_audio(states, work / "audio.wav")
        (work / "sample.srt").write_text(captions(states), encoding="utf-8")
        out.parent.mkdir(parents=True, exist_ok=True)
        ffmpeg(["-i", str(work / "video.mp4"), "-i", str(work / "audio.wav"), "-i", str(work / "sample.srt"),
                "-map", "0:v", "-map", "1:a", "-map", "2:s", "-c:v", "copy",
                "-af", VOICE_CHAIN, "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-c:s", "mov_text", "-movflags", "+faststart", str(out)])
    print(f"Sample written to {out} ({sum(s['frames'] for s in states) / FPS:.1f}s)")
    return 0


def measure_lufs(path: Path) -> tuple[float, float]:
    """Integrated loudness and true peak of a media file (ebur128)."""
    err = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", err)
    tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", err)
    return (float(i[-1]) if i else 0.0, float(tp[-1]) if tp else 0.0)


def relevel(chapter: Path, quiet: bool = False) -> int:
    """Bring the finished video to the loudness target with a measured gain (picture, captions and
    chapters are copied untouched), then update render.json. Single-pass loudnorm can undershoot."""
    video = chapter / sb.VIDEO_FILE
    lufs, peak = measure_lufs(video)
    gain = LUFS - lufs
    if abs(gain) <= 0.5:
        if not quiet:
            print(f"loudness {lufs:.1f} LUFS, peak {peak:.1f} dBTP: no change")
        return 0
    tmp = video.with_name("chapter.relevel.mp4")
    ffmpeg(["-i", str(video), "-map", "0", "-c:v", "copy", "-c:s", "copy", "-map_metadata", "0", "-map_chapters", "0",
            "-af", f"volume={gain:.2f}dB,alimiter=limit=0.70:attack=5:release=50:level=false",  # ceiling about -3 dBFS; AAC adds intersample peaks
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart",
            str(tmp)])
    tmp.replace(video)
    new_lufs, new_peak = measure_lufs(video)
    manifest_path = chapter / sb.RENDER_MANIFEST
    if manifest_path.exists():
        manifest = load_json(manifest_path)
        manifest["video_sha256"] = file_sha(video)
        manifest["size_mb"] = round(video.stat().st_size / 1e6, 2)
        manifest["format"]["measured_lufs"] = round(new_lufs, 1)
        manifest["format"]["true_peak_dbtp"] = round(new_peak, 1)
        save_json(manifest_path, manifest)
        (chapter / sb.SCRIPT_FILE).write_text(sb.script_markdown(sb.load(chapter), manifest), encoding="utf-8")
    print(f"loudness {lufs:.1f} -> {new_lufs:.1f} LUFS (gain {gain:+.2f} dB), true peak {new_peak:.1f} dBTP")
    return 0


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
                "-c:v", "copy", "-af", VOICE_CHAIN, "-c:a", "aac", "-b:a", "192k",
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
        "voice": __import__("voice").describe(),
        "ffmpeg": sh(["ffmpeg", "-version"]).stdout.splitlines()[0],
        "states": len(states),
        "questions": sum(1 for _, b in sb.beats(board) if sb.ask_of(b)),
        "breathers": sum(1 for _, b in sb.beats(board) if b["visual"]["type"] == "breather"),
        "scenes": timings,
    }
    save_json(chapter / sb.RENDER_MANIFEST, manifest)
    (chapter / sb.DESCRIPTION_FILE).write_text(description(board, timings, chapter), encoding="utf-8")
    (chapter / sb.SCRIPT_FILE).write_text(sb.script_markdown(board, manifest), encoding="utf-8")
    relevel(chapter, quiet=True)
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
    parser.add_argument("--sample", metavar="FILE", help="render only the opening to FILE (default 60 s)")
    parser.add_argument("--seconds", type=float, default=60.0)
    parser.add_argument("--relevel", action="store_true", help="re-measure and fix the loudness of the rendered video")
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
    if args.relevel:
        return relevel(chapter)
    if args.sample:
        return render_sample(chapter, Path(args.sample), args.seconds)
    if args.script:
        manifest = load_json(chapter / sb.RENDER_MANIFEST) if (chapter / sb.RENDER_MANIFEST).exists() else None
        (chapter / sb.SCRIPT_FILE).write_text(sb.script_markdown(sb.load(chapter), manifest), encoding="utf-8")
        return 0
    return render(chapter)


if __name__ == "__main__":
    sys.exit(main())
