#!/usr/bin/env python3
"""Rebuild REVIEW.md: chapters waiting for the course owner."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, curriculum_chapters, load_curriculum, load_state, now_iso  # noqa: E402

SECTIONS = [
    ("in_review", "Ready for review"),
    ("changes_requested", "Changes requested"),
    ("blocked", "Blocked"),
    ("in_progress", "In progress"),
]


def main() -> None:
    state = load_state()
    titles = {}
    for language in state["languages"]:
        for chapter in curriculum_chapters(load_curriculum(language)):
            titles[chapter["id"]] = chapter["title"]
    lines = [
        "# Review Queue",
        "",
        f"Generated {now_iso()} by `tools/build_review_queue.py`. Do not edit by hand.",
        "",
        "To approve a chapter: `python3 tools/state.py approve <chapter-id>`.",
        "To ask for changes: `python3 tools/state.py request-changes <chapter-id> \"<what to change>\"`.",
        "You can also ask Claude to do either.",
        "",
        "## Curricula",
        "",
    ]
    for language, info in state["languages"].items():
        lines.append(f"- {language}: `{info['curriculum']}` ({info['curriculum_status']})")
    for status, heading in SECTIONS:
        rows = [(cid, info) for cid, info in state["chapters"].items() if info["status"] == status]
        lines += ["", f"## {heading}", ""]
        if not rows:
            lines.append("None.")
            continue
        for cid, info in rows:
            extra = info.get("block_reason") or info.get("notes") or ""
            path = info.get("path")
            link = f" ([{path}]({path}))" if path else ""
            if path and (ROOT / path / "video" / "chapter.mp4").exists():
                link += f", video: [{path}/video/chapter.mp4]({path}/video/chapter.mp4)"
            lines.append(f"- **{cid}**: {titles.get(cid, '')}{link}" + (f". {extra}" if extra else ""))
    lines += [
        "",
        "## Review checklist",
        "",
        "- Is every fact correct and current? Check `sources.md`.",
        "- Does each example run and teach one clear idea? See `verification.json`.",
        "- Is the language simple, specific and free of filler?",
        "- Does `## Work with AI` give prompts a beginner can use today?",
        "- Watch `video/chapter.mp4`: is the narration clear, does every picture match what is said, and is it free of errors?",
        "- Is the difficulty right after the previous chapter?",
        "",
    ]
    (ROOT / "REVIEW.md").write_text("\n".join(lines), encoding="utf-8")
    print("REVIEW.md updated")


if __name__ == "__main__":
    main()
