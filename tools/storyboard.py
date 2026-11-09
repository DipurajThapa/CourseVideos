"""Storyboard model for chapter videos. Standard library only.

A chapter video is a full walkthrough of the chapter. Its direction lives in
`video/storyboard.json`: an ordered list of scenes, each made of beats. A beat
is one piece of narration plus the exact picture shown while it is spoken.
Every code, output and error panel points at a verified file in the chapter,
so the video can only show content that tools/verify_chapter.py has run.

This module validates storyboards, computes the hashes that tie a rendered
video to its inputs, and writes the human-readable `video/script.md`.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

STORYBOARD = "video/storyboard.json"
RENDER_MANIFEST = "video/render.json"
VIDEO_FILE = "video/chapter.mp4"
CAPTIONS_FILE = "video/chapter.srt"
DESCRIPTION_FILE = "video/description.md"
SCRIPT_FILE = "video/script.md"
VIDEO_OUTPUTS = {VIDEO_FILE, CAPTIONS_FILE, RENDER_MANIFEST, DESCRIPTION_FILE, SCRIPT_FILE}

VISUAL_TYPES = {"title", "bullets", "text", "table", "code", "prompt", "pause", "end"}
WORDS_PER_SECOND = 2.45         # Piper lessac-medium, length scale 1.18 with sentence pauses, measured 2026-11-09
BEAT_GAP_SECONDS = 0.6          # silence after each beat
MIN_MINUTES, MAX_MINUTES = 8, 20
MIN_PAUSES = 3
MAX_SENTENCE_WORDS = 30
# Narration is spoken text. These characters are not speakable, so a beat that
# contains them is rejected: write the spoken form instead ("tea price", "double slash").
UNSPEAKABLE = re.compile(r"[`*#=/%<>{}\[\]|\\~^_]")

LESSON_SECTIONS = ["Learning goals", "Why this matters", "The idea", "Build it step by step", "See the outcome",
                   "Work with AI", "Common mistakes", "Think beyond", "Recap", "Practice", "What's next"]
PROJECT_SECTIONS = ["The mission", "What you will build", "Acceptance criteria", "Plan it with AI",
                    "Build it step by step", "Test it", "Improve it with AI", "Recap", "What's next"]


def load(chapter_dir: Path) -> dict:
    with open(chapter_dir / STORYBOARD, encoding="utf-8") as fh:
        return json.load(fh)


def beats(board: dict):
    for scene in board.get("scenes", []):
        for beat in scene.get("beats", []):
            yield scene, beat


def referenced_files(board: dict) -> list[str]:
    files = []
    for _, beat in beats(board):
        visual = beat.get("visual", {})
        for key in ("file", "output", "error"):
            if visual.get(key):
                files.append(visual[key])
        if visual.get("error"):
            before = Path(visual["error"]).with_suffix(".expected").as_posix()
            files.append(before)
    return list(dict.fromkeys(files))


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def storyboard_sha(chapter_dir: Path) -> str:
    return sha_text((chapter_dir / STORYBOARD).read_text(encoding="utf-8"))


def inputs_sha(chapter_dir: Path, board: dict) -> str:
    """Hash of every verified file the video shows, so a changed example forces a re-render."""
    digest = hashlib.sha256()
    for rel in sorted(referenced_files(board)):
        path = chapter_dir / rel
        digest.update(rel.encode("utf-8") + b"\0")
        if path.exists():
            digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def estimate_seconds(board: dict) -> float:
    total = 0.0
    for _, beat in beats(board):
        words = len(beat.get("narration", "").split())
        total += words / WORDS_PER_SECOND + BEAT_GAP_SECONDS + float(beat.get("hold", 0))
        if beat.get("visual", {}).get("type") == "pause":
            total += int(beat["visual"].get("seconds", 5))
    return total


def validate(chapter_dir: Path, board: dict, kind: str, runnable: set[str]) -> list[str]:
    """Return a list of problems. `runnable` holds the chapter-relative paths of verified source files."""
    problems: list[str] = []
    scenes = board.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        return ["storyboard has no scenes"]
    wanted = PROJECT_SECTIONS if kind == "project" else LESSON_SECTIONS
    sections = [s.get("section") for s in scenes]
    for section in wanted:
        if section not in sections:
            problems.append(f"no scene covers the section '{section}'")
    order = [s for s in sections if s in wanted]
    if order != sorted(order, key=wanted.index):
        problems.append("scenes must follow the order of the chapter sections")
    ids = [s.get("id") for s in scenes]
    if len(set(ids)) != len(ids) or not all(ids):
        problems.append("every scene needs a unique id")
    pauses = 0
    shown_code: set[str] = set()
    for scene, beat in beats(board):
        where = f"scene {scene.get('id')}"
        visual = beat.get("visual") or {}
        vtype = visual.get("type")
        narration = beat.get("narration", "")
        if vtype not in VISUAL_TYPES:
            problems.append(f"{where}: unknown visual type {vtype!r}")
            continue
        if vtype == "pause":
            pauses += 1
            if not visual.get("question"):
                problems.append(f"{where}: a pause beat needs a question")
        elif not narration.strip():
            problems.append(f"{where}: a {vtype} beat needs narration")
        for sentence in re.split(r"(?<=[.!?])\s+", narration):
            if len(sentence.split()) > MAX_SENTENCE_WORDS:
                problems.append(f"{where}: narration sentence over {MAX_SENTENCE_WORDS} words: {sentence[:70]!r}")
        bad = UNSPEAKABLE.findall(narration)
        if bad:
            problems.append(f"{where}: narration contains unspeakable characters {sorted(set(bad))}: "
                            f"{narration[:70]!r}")
        if vtype == "code":
            src = visual.get("file")
            if not src:
                problems.append(f"{where}: a code beat needs 'file'")
            elif src not in runnable:
                problems.append(f"{where}: {src} is not a verified runnable file of this chapter")
            else:
                shown_code.add(src)
            out, err = visual.get("output"), visual.get("error")
            if out and not (out.endswith(".expected") and (chapter_dir / out).exists()):
                problems.append(f"{where}: output {out} must be an existing .expected file")
            if err and not (err.endswith(".expected_error") and (chapter_dir / err).exists()):
                problems.append(f"{where}: error {err} must be an existing .expected_error file")
            for key in (out, err):
                if key and src and Path(key).with_suffix("").as_posix() != Path(src).with_suffix("").as_posix():
                    problems.append(f"{where}: {key} does not belong to {src}")
        if vtype == "table" and not visual.get("rows"):
            problems.append(f"{where}: a table beat needs rows")
        if vtype == "bullets" and not visual.get("items"):
            problems.append(f"{where}: a bullets beat needs items")
    if pauses < MIN_PAUSES:
        problems.append(f"need at least {MIN_PAUSES} pause beats (interaction points), found {pauses}")
    minutes = estimate_seconds(board) / 60
    if not MIN_MINUTES <= minutes <= MAX_MINUTES:
        problems.append(f"estimated length {minutes:.1f} min is outside {MIN_MINUTES} to {MAX_MINUTES} min")
    return problems


def _clock(seconds: float) -> str:
    seconds = int(round(seconds))
    return f"{seconds // 60}:{seconds % 60:02d}"


def _describe(visual: dict) -> str:
    vtype = visual.get("type")
    if vtype == "code":
        parts = [f"Code `{visual['file']}`"]
        if visual.get("highlight"):
            parts.append(f"lines {', '.join(str(n) for n in visual['highlight'])} highlighted")
        if visual.get("output"):
            parts.append(f"output `{visual['output']}`")
        if visual.get("error"):
            parts.append(f"error `{visual['error']}`")
        if not visual.get("output") and not visual.get("error"):
            parts.append("output hidden (predict first)")
        return ", ".join(parts)
    if vtype == "pause":
        return f"Pause card: \"{visual.get('question')}\" with a {visual.get('seconds', 5)}-second countdown"
    if vtype == "table":
        return f"Table: {visual.get('heading', '')} ({len(visual.get('rows', []))} rows)"
    if vtype == "bullets":
        shown = visual.get("items", [])[: visual.get("reveal", len(visual.get("items", [])))]
        return f"{visual.get('heading', '')}" + "".join(f"\n    - {item}" for item in shown)
    if vtype == "prompt":
        return f"Prompt card ({visual.get('label', '')}): \"{visual.get('prompt', '')}\""
    return " ".join(str(visual.get(k, "")) for k in ("heading", "title", "subtitle", "body") if visual.get(k)).strip()


def script_markdown(board: dict, manifest: dict | None) -> str:
    """The human-readable script, generated from the storyboard and (when rendered) real timings."""
    timings = {s["id"]: s for s in (manifest or {}).get("scenes", [])}
    total = (manifest or {}).get("duration_seconds") or estimate_seconds(board)
    lines = [
        f"# Video Script: {board.get('title', '')}",
        "",
        "Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: "
        "change the storyboard and render again.",
        "",
        f"Format: full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: {_clock(total)}"
        + ("" if manifest else " (estimate, not rendered yet)") + ".",
        "",
    ]
    for number, scene in enumerate(board.get("scenes", []), start=1):
        timing = timings.get(scene["id"])
        when = f" ({_clock(timing['start'])} to {_clock(timing['end'])})" if timing else ""
        lines += [f"## Scene {number}: {scene.get('title', scene.get('section'))}{when}", "",
                  f"**Section:** {scene.get('section')}", ""]
        if scene.get("direction"):
            lines += [f"**Direction:** {scene['direction']}", ""]
        for beat in scene.get("beats", []):
            visual = beat.get("visual", {})
            if beat.get("narration"):
                lines.append(f"- **Narration:** {beat['narration']}")
            lines.append(f"  **On screen:** {_describe(visual)}")
            if visual.get("type") == "pause":
                lines.append("  **Interaction:** the learner pauses and answers before the reveal.")
        lines.append("")
    return "\n".join(lines)
