"""Storyboard model for chapter videos. Standard library only.

A chapter video is a full walkthrough of the chapter. Its direction lives in
`video/storyboard.json`: an ordered list of scenes, each made of beats. Every
code, output and error panel points at a verified file in the chapter, so the
video can only show content that tools/verify_chapter.py has run.

A beat is one picture that changes in step with its narration:

    {"visual": {...},                      the starting picture
     "narration": "...",                   one block of speech, or
     "segments": [{"say": "...", ...}],    speech split into parts; the other keys of each part
                                           change the picture while that part is spoken
                                           (highlight, lines, output, reveal, focus, focus_row ...)
     "ask": {"question": "...", "seconds": 10},
                                           an on-screen question with a digital timer; the
                                           picture stays visible underneath
     "after": [{"say": "...", ...}],       parts spoken after the timer (the reveal)
     "hold": 2}                            extra quiet seconds at the end

Changes accumulate: a part keeps every change made by the parts before it.
`pause` and `quiz` beats ask automatically; a quiz reveals its answer in `after`.
A `breather` beat is a calm recap card with a progress map and a short quiet hold.

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

VISUAL_TYPES = {"title", "bullets", "text", "table", "code", "prompt", "pause", "quiz", "breather", "chat", "end"}
WORDS_PER_SECOND = 2.75         # Kokoro bm_lewis at speed 0.95, one take per beat (measured on Chapter 1; re-measure after a voice change)
BEAT_GAP_SECONDS = 0.6          # silence after each beat
SEGMENT_GAP_SECONDS = 0.35      # silence between parts of one beat
ASK_SECONDS = 10                # every on-screen question gets a 10-second digital timer
BREATHER_HOLD = 4.0             # quiet seconds on a breather card
MIN_MINUTES, MAX_MINUTES = 8, 20
MIN_ASKS = 6                    # on-screen questions (asks, pauses and quizzes)
MIN_QUIZZES = 2
MAX_STRETCH_SECONDS = 180       # never more than 3 minutes without a question or a breather
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


def ask_of(beat: dict) -> dict | None:
    """The beat's on-screen question, if any. Pause and quiz beats always ask."""
    visual = beat.get("visual", {})
    if beat.get("ask"):
        return {"question": beat["ask"].get("question", ""), "seconds": int(beat["ask"].get("seconds", ASK_SECONDS))}
    if visual.get("type") in ("pause", "quiz"):
        return {"question": visual.get("question", ""), "seconds": int(visual.get("seconds", ASK_SECONDS))}
    return None


def phases(beat: dict) -> list[dict]:
    """Expand a beat into ordered phases: {"kind": "say"|"ask"|"hold", "text", "visual", ...}.

    Picture changes accumulate from one phase to the next.
    """
    visual = dict(beat.get("visual", {}))
    out: list[dict] = []
    parts = beat.get("segments") or ([{"say": beat["narration"]}] if beat.get("narration") else [])
    if not parts and not ask_of(beat):
        parts = [{"say": ""}]
    for part in parts:
        visual = {**visual, **{k: v for k, v in part.items() if k != "say"}}
        out.append({"kind": "say", "text": part.get("say", "").strip(), "visual": dict(visual)})
    ask = ask_of(beat)
    if ask:
        out.append({"kind": "ask", "text": "", "question": ask["question"], "seconds": ask["seconds"],
                    "visual": dict(visual)})
        for part in beat.get("after", []):
            extra = {"revealed": True} if visual.get("type") == "quiz" else {}
            visual = {**visual, **extra, **{k: v for k, v in part.items() if k != "say"}}
            out.append({"kind": "say", "text": part.get("say", "").strip(), "visual": dict(visual)})
    if ask:
        # Reserve the question's space for the whole beat, so nothing on screen moves when the timer appears.
        at_ask = next(p["visual"] for p in out if p["kind"] == "ask")
        strip = at_ask.get("type") in ("table", "text") or (
            at_ask.get("type") == "code" and bool(at_ask.get("output") or at_ask.get("error")))
        for p in out:
            p["visual"]["_ask_layout"] = "strip" if strip else "side"
        visual = {**visual, "_ask_layout": "strip" if strip else "side"}
    hold = float(beat.get("hold", BREATHER_HOLD if visual.get("type") == "breather" else 0))
    if hold:
        out.append({"kind": "hold", "text": "", "seconds": hold, "visual": dict(visual)})
    return out


def spoken_text(beat: dict) -> str:
    return " ".join(p["text"] for p in phases(beat) if p["kind"] == "say" and p["text"])


def referenced_files(board: dict) -> list[str]:
    files = []
    for _, beat in beats(board):
        for phase in phases(beat):
            visual = phase["visual"]
            for item in [visual] + list(visual.get("messages", [])):
                for key in ("file", "output", "error", "code"):
                    if item.get(key):
                        files.append(item[key])
                if item.get("error"):
                    files.append(Path(item["error"]).with_suffix(".expected").as_posix())
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


def phase_seconds(phase: dict) -> float:
    if phase["kind"] == "ask":
        return phase["seconds"] + 0.5
    if phase["kind"] == "hold":
        return phase["seconds"]
    return len(phase["text"].split()) / WORDS_PER_SECOND + SEGMENT_GAP_SECONDS


def estimate_seconds(board: dict) -> float:
    total = 0.0
    for _, beat in beats(board):
        total += sum(phase_seconds(p) for p in phases(beat)) + BEAT_GAP_SECONDS
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
    banned = [b.strip().lower() for b in (Path(__file__).resolve().parent / "banned_phrases.txt")
              .read_text(encoding="utf-8").splitlines() if b.strip() and not b.startswith("#")]
    for scene in scenes:
        texts = [scene.get("direction", ""), scene.get("title", "")] + [spoken_text(b) for b in scene.get("beats", [])]
        for text in texts:
            low = text.lower()
            for phrase in banned:
                if re.search(rf"\b{re.escape(phrase)}\b", low):
                    problems.append(f"scene {scene.get('id')}: banned phrase {phrase!r} in {text[:60]!r}")
            if "\u2014" in text:
                problems.append(f"scene {scene.get('id')}: em dash in {text[:60]!r}")
            for sentence in re.split(r"(?<=[.!?])\s+", scene.get("direction", "")):
                if len(sentence.split()) > MAX_SENTENCE_WORDS:
                    problems.append(f"scene {scene.get('id')}: direction sentence over {MAX_SENTENCE_WORDS} words")
                    break
    asks = quizzes = breathers = 0
    since_break, longest_stretch = 0.0, 0.0
    for scene, beat in beats(board):
        where = f"scene {scene.get('id')}"
        base_type = beat.get("visual", {}).get("type")
        if base_type not in VISUAL_TYPES:
            problems.append(f"{where}: unknown visual type {base_type!r}")
            continue
        if beat.get("narration") and beat.get("segments"):
            problems.append(f"{where}: use either narration or segments, not both")
        if beat.get("after") and not ask_of(beat):
            problems.append(f"{where}: 'after' needs an ask")
        ask = ask_of(beat)
        if ask:
            asks += 1
            if not ask["question"]:
                problems.append(f"{where}: an on-screen question needs its text")
            if ask["seconds"] != ASK_SECONDS:
                problems.append(f"{where}: timers run for {ASK_SECONDS} seconds, found {ask['seconds']}")
        if base_type == "quiz":
            quizzes += 1
            visual = beat["visual"]
            if not visual.get("options") or not isinstance(visual.get("answer"), int) \
                    or not 0 <= visual["answer"] < len(visual["options"]):
                problems.append(f"{where}: a quiz needs options and a valid answer index")
            if not beat.get("after"):
                problems.append(f"{where}: a quiz needs an 'after' part that reveals and explains the answer")
        if base_type == "breather":
            breathers += 1
            if not beat["visual"].get("items"):
                problems.append(f"{where}: a breather needs recap items")
        text = spoken_text(beat)
        if base_type not in ("pause",) and not text:
            problems.append(f"{where}: a {base_type} beat needs narration")
        for sentence in re.split(r"(?<=[.!?])\s+", text):
            if len(sentence.split()) > MAX_SENTENCE_WORDS:
                problems.append(f"{where}: narration sentence over {MAX_SENTENCE_WORDS} words: {sentence[:70]!r}")
        bad = UNSPEAKABLE.findall(text)
        if bad:
            problems.append(f"{where}: narration contains unspeakable characters {sorted(set(bad))}: {text[:70]!r}")
        for phase in phases(beat):
            v = phase["visual"]
            if v.get("type") == "code":
                src = v.get("file")
                if not src:
                    problems.append(f"{where}: a code beat needs 'file'")
                elif src not in runnable:
                    problems.append(f"{where}: {src} is not a verified runnable file of this chapter")
                for key, suffix in (("output", ".expected"), ("error", ".expected_error")):
                    target = v.get(key)
                    if not target:
                        continue
                    if not (target.endswith(suffix) and (chapter_dir / target).exists()):
                        problems.append(f"{where}: {key} {target} must be an existing {suffix} file")
                    elif src and Path(target).with_suffix("").as_posix() != Path(src).with_suffix("").as_posix():
                        problems.append(f"{where}: {target} does not belong to {src}")
            if v.get("type") == "chat":
                if not v.get("messages"):
                    problems.append(f"{where}: a chat needs messages")
                for m in v.get("messages", []):
                    if m.get("role") not in ("you", "ai"):
                        problems.append(f"{where}: chat message role must be 'you' or 'ai'")
                    if m.get("code") and m["code"] not in runnable:
                        problems.append(f"{where}: chat code {m['code']} is not a verified runnable file")
                    if m.get("output") and not (str(m["output"]).endswith(".expected") and (chapter_dir / m["output"]).exists()):
                        problems.append(f"{where}: chat output {m['output']} must be an existing .expected file")
                    if m.get("error") and not (m.get("file") in runnable and (chapter_dir / m["error"]).exists()):
                        problems.append(f"{where}: a pasted error needs a verified 'file' and its .expected_error")
            if v.get("type") == "table" and not v.get("rows"):
                problems.append(f"{where}: a table beat needs rows")
            if v.get("type") == "bullets" and not v.get("items"):
                problems.append(f"{where}: a bullets beat needs items")
        seconds = sum(phase_seconds(p) for p in phases(beat)) + BEAT_GAP_SECONDS
        if ask or base_type == "breather":
            longest_stretch = max(longest_stretch, since_break)
            since_break = 0.0
        else:
            since_break += seconds
    longest_stretch = max(longest_stretch, since_break)
    if asks < MIN_ASKS:
        problems.append(f"need at least {MIN_ASKS} on-screen questions with a timer, found {asks}")
    if quizzes < MIN_QUIZZES:
        problems.append(f"need at least {MIN_QUIZZES} quick-check quizzes, found {quizzes}")
    minutes = estimate_seconds(board) / 60
    if breathers < max(2, int(minutes // 4)):
        problems.append(f"need at least {max(2, int(minutes // 4))} breathers for {minutes:.0f} minutes, found {breathers}")
    if longest_stretch > MAX_STRETCH_SECONDS:
        problems.append(f"a stretch of about {longest_stretch:.0f} s has no question or breather "
                        f"(limit {MAX_STRETCH_SECONDS} s)")
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
        if visual.get("lines"):
            parts.append(f"lines 1 to {visual['lines']} typed in")
        if visual.get("highlight"):
            parts.append(f"line {', '.join(str(n) for n in visual['highlight'])} highlighted")
        if visual.get("output"):
            parts.append(f"output `{visual['output']}`")
        if visual.get("error"):
            parts.append(f"error `{visual['error']}`")
        if not visual.get("output") and not visual.get("error"):
            parts.append("output hidden")
        return ", ".join(parts)
    if vtype == "pause":
        return f"Question card: \"{visual.get('question')}\""
    if vtype == "quiz":
        opts = visual.get("options", [])
        state = f"answer revealed: {opts[visual['answer']]}" if visual.get("revealed") else "options shown"
        return f"Quick check: \"{visual.get('question')}\" ({state})"
    if vtype == "breather":
        return "Breather card" + "".join(f"\n    - {item}" for item in visual.get("items", []))
    if vtype == "table":
        focus = visual.get("focus_row")
        return f"Table: {visual.get('heading', '')}" + (f" (row {focus + 1} in focus)" if focus is not None else "")
    if vtype == "bullets":
        shown = visual.get("items", [])[: visual.get("reveal", len(visual.get("items", [])))]
        return f"{visual.get('heading', '')}" + "".join(f"\n    - {item}" for item in shown)
    if vtype == "prompt":
        return f"Prompt card ({visual.get('label', '')})"
    if vtype == "chat":
        shown = visual.get("messages", [])[: visual.get("reveal", len(visual.get("messages", [])))]
        lines = []
        for m in shown:
            who = "You" if m["role"] == "you" else "AI (example answer)"
            extra = f" [code `{m['code']}`]" if m.get("code") else (f" [pasted error from `{m['file']}`]" if m.get("error") else "")
            lines.append(f"\n    - {who}: {m.get('text', '').replace(chr(10), ' ')}{extra}")
        return f"AI chat, stage {visual.get('stage', '-')}: {visual.get('heading', '')}" + "".join(lines)
    return " ".join(str(visual.get(k, "")) for k in ("heading", "title", "subtitle") if visual.get(k)).strip()


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
        f"Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: {_clock(total)}"
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
            for phase in phases(beat):
                if phase["kind"] == "say":
                    if phase["text"]:
                        lines.append(f"- **Narration:** {phase['text']}")
                    lines.append(f"  **On screen:** {_describe(phase['visual'])}")
                elif phase["kind"] == "ask":
                    lines.append(f"- **Interaction:** \"{phase['question']}\" stays on screen with a "
                                 f"{phase['seconds']}-second timer.")
                else:
                    lines.append(f"- **Breather:** {phase['seconds']:.0f} quiet seconds.")
        lines.append("")
    return "\n".join(lines)
