"""Narration voices for the chapter videos. Free and open source, CPU only.

Engines (choose with the COURSE_VOICE_ENGINE environment variable):
  kokoro  (default) Kokoro-82M, Apache-2.0. Natural, expressive, about 0.65 s of compute per
          second of audio on 2 CPU cores. Voice "bm_lewis" (deep, calm, British), chosen by
          the course owner after a measured comparison of ten voices.
  clone   Chatterbox, MIT. Clones a voice from a clean 10 to 30 second recording set in
          COURSE_VOICE_REF. About 6 s of compute per second of audio on CPU (1.5 to 2 hours
          per chapter). Its output carries Resemble AI's imperceptible Perth watermark.

Fluency: a "run" is all the narration of a beat up to its question (or to its end). Each run
is spoken in ONE take, so intonation flows across sentences. The renderer still needs to know
where each segment starts (to move highlights in sync), so segment boundaries are predicted
from text length and then snapped to the nearest natural pause in the take.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import wave
from pathlib import Path

import numpy as np

CACHE = Path(os.environ.get("COURSE_VIDEO_CACHE", Path.home() / ".cache" / "coursevideos"))
ENGINE = os.environ.get("COURSE_VOICE_ENGINE", "kokoro")
CLONE_REF = os.environ.get("COURSE_VOICE_REF", "")

KOKORO_VERSION = "kokoro-onnx 0.6.1, model v1.0"
KOKORO_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
KOKORO_FILES = {"kokoro-v1.0.onnx": None, "voices-v1.0.bin": None}
KOKORO_VOICE = "bm_lewis"
KOKORO_LANG = "en-gb"
KOKORO_SPEED = 0.95             # unhurried for second-language listeners, still lively

CLONE_EXAGGERATION = 0.6        # Chatterbox emotion intensity: 0.5 neutral, higher is livelier
CLONE_CFG = 0.5

# Spoken forms for words the voice reads badly. Applied to audio only; captions keep the original.
PRONOUNCE = {
    r"\bXP\b": "X P", r"\bPEP 8\b": "pep eight", r"\bChatGPT\b": "Chat G P T", r"\bstr\b": "string",
    r"\bNameError\b": "Name Error", r"\bTypeError\b": "Type Error", r"\bSyntaxError\b": "Syntax Error",
    r"\bIDLE\b": "idle", r"\bUSD\b": "U S D", r"\bpytest\b": "pie test", r"\bAssertionError\b": "Assertion Error",
}


def spoken(text: str) -> str:
    for pattern, replacement in PRONOUNCE.items():
        text = re.sub(pattern, replacement, text)
    return text


def describe() -> dict:
    if ENGINE == "clone":
        return {"engine": "chatterbox (MIT)", "voice": f"clone of {Path(CLONE_REF).name}",
                "exaggeration": CLONE_EXAGGERATION, "watermark": "Resemble Perth (imperceptible)"}
    return {"engine": KOKORO_VERSION + " (Apache-2.0)", "voice": KOKORO_VOICE, "language": KOKORO_LANG,
            "speed": KOKORO_SPEED}


# ---------------------------------------------------------------- setup

def setup() -> list[str]:
    problems = []
    try:
        import kokoro_onnx  # noqa: F401
    except ImportError:
        os.system("python3 -m pip install --quiet --break-system-packages kokoro-onnx==0.6.1 soundfile")
        try:
            import kokoro_onnx  # noqa: F401
        except ImportError:
            problems.append("could not install kokoro-onnx")
    folder = CACHE / "kokoro"
    folder.mkdir(parents=True, exist_ok=True)
    import urllib.request
    for name in KOKORO_FILES:
        path = folder / name
        if not path.exists():
            try:
                tmp = path.with_suffix(path.suffix + ".part")
                urllib.request.urlretrieve(KOKORO_URL + name, tmp)
                tmp.rename(path)
            except Exception as exc:
                problems.append(f"could not download {name}: {exc}")
    if ENGINE == "clone":
        if not CLONE_REF or not Path(CLONE_REF).exists():
            problems.append("COURSE_VOICE_ENGINE=clone needs COURSE_VOICE_REF set to a recording")
        try:
            import chatterbox  # noqa: F401
        except ImportError:
            problems.append("clone engine needs chatterbox-tts (see tools/voice.py)")
    if not problems:
        path, _ = synth_run(["Voice check."])
        if not path.exists():
            problems.append("the voice produced no audio")
    return problems


# ---------------------------------------------------------------- engines

_KOKORO = None
_CLONE = None


def _kokoro(text: str) -> tuple[np.ndarray, int]:
    global _KOKORO
    if _KOKORO is None:
        from kokoro_onnx import Kokoro
        _KOKORO = Kokoro(str(CACHE / "kokoro" / "kokoro-v1.0.onnx"), str(CACHE / "kokoro" / "voices-v1.0.bin"))
    samples, rate = _KOKORO.create(text, voice=KOKORO_VOICE, speed=KOKORO_SPEED, lang=KOKORO_LANG)
    return np.asarray(samples, dtype=np.float32), rate


def _clone(text: str) -> tuple[np.ndarray, int]:
    global _CLONE
    if _CLONE is None:
        from chatterbox.tts import ChatterboxTTS
        _CLONE = ChatterboxTTS.from_pretrained(device="cpu")
    # Chatterbox works best on passages of a few sentences.
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks, cur = [], ""
    for s in sentences:
        if cur and len(cur) + len(s) > 260:
            chunks.append(cur)
            cur = s
        else:
            cur = f"{cur} {s}".strip()
    if cur:
        chunks.append(cur)
    parts = []
    for chunk in chunks:
        wav = _CLONE.generate(chunk, audio_prompt_path=CLONE_REF, exaggeration=CLONE_EXAGGERATION,
                              cfg_weight=CLONE_CFG)
        parts.append(wav.squeeze().numpy().astype(np.float32))
        parts.append(np.zeros(int(_CLONE.sr * 0.22), dtype=np.float32))
    return np.concatenate(parts[:-1]) if parts else np.zeros(1, np.float32), _CLONE.sr


def _speak(text: str) -> tuple[np.ndarray, int]:
    return _clone(text) if ENGINE == "clone" else _kokoro(text)


# ---------------------------------------------------------------- runs

def _trim(x: np.ndarray, rate: int, head: float = 0.04, tail: float = 0.12) -> np.ndarray:
    loud = np.where(np.abs(x) > 0.01)[0]
    if not len(loud):
        return x
    a = max(0, loud[0] - int(head * rate))
    b = min(len(x), loud[-1] + int(tail * rate))
    return x[a:b]


def _snap(x: np.ndarray, rate: int, guesses: list[float]) -> list[float]:
    """Move each predicted boundary to the quietest 120 ms within 0.7 s, keeping them in order."""
    hop = int(0.01 * rate)
    win = int(0.12 * rate)
    env = np.sqrt(np.convolve(x ** 2, np.ones(win) / win, mode="same"))[::hop]
    out, last = [], 0.25
    for g in guesses:
        lo = max(int((g - 0.7) * 100), int((last + 0.3) * 100))
        hi = min(int((g + 0.7) * 100), len(env) - 1)
        if hi <= lo:
            t = max(g, last + 0.3)
        else:
            t = (lo + int(np.argmin(env[lo:hi]))) / 100
        out.append(t)
        last = t
    return out


def synth_run(texts: list[str]) -> tuple[Path, list[tuple[float, float]]]:
    """Speak several segments as one take. Returns the wav and each segment's (start, end) in seconds."""
    texts = [t.strip() for t in texts]
    ident = json.dumps([ENGINE, describe(), [spoken(t) for t in texts]], sort_keys=True)
    key = hashlib.sha256(ident.encode()).hexdigest()[:24]
    folder = CACHE / "runs"
    folder.mkdir(parents=True, exist_ok=True)
    wav_path, meta_path = folder / f"{key}.wav", folder / f"{key}.json"
    if wav_path.exists() and meta_path.exists():
        return wav_path, [tuple(s) for s in json.loads(meta_path.read_text())]
    x, rate = _speak(" ".join(spoken(t) for t in texts))
    x = _trim(x, rate)
    total = len(x) / rate
    weights = [max(1, len(t)) + 12 for t in texts]          # each sentence end adds a pause
    cum = np.cumsum(weights) / sum(weights)
    bounds = _snap(x, rate, [total * c for c in cum[:-1]]) + [total]
    slices, start = [], 0.0
    for b in bounds:
        slices.append((round(start, 3), round(b, 3)))
        start = b
    pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    tmp = wav_path.with_suffix(".part.wav")
    with wave.open(str(tmp), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(pcm.tobytes())
    tmp.rename(wav_path)
    meta_path.write_text(json.dumps(slices))
    return wav_path, slices
