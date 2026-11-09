#!/usr/bin/env python3
"""Course progress state machine.

Usage:
  python3 tools/state.py next
  python3 tools/state.py status
  python3 tools/state.py start <chapter-id>
  python3 tools/state.py complete <chapter-id>
  python3 tools/state.py block <chapter-id> "<reason>"
  python3 tools/state.py approve <chapter-id|language>
  python3 tools/state.py request-changes <chapter-id> "<notes>"
  python3 tools/state.py add-language <language>

State changes are made only on the main branch (see RUNBOOK.md).
"""
from __future__ import annotations

import json
import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ROOT,
    chapter_path,
    curriculum_chapters,
    fingerprint,
    load_curriculum,
    load_json,
    load_state,
    now_iso,
    save_json,
    save_state,
)

RESUMABLE = ("in_progress", "blocked")


def ordered_chapters(state: dict) -> list[tuple[str, dict]]:
    order = {lang: i for i, lang in enumerate(state["language_order"])}
    items = list(state["chapters"].items())
    return sorted(items, key=lambda kv: (order.get(kv[1]["language"], 99), kv[1]["number"]))


def find_curriculum_entry(language: str, chapter_id: str) -> dict:
    for chapter in curriculum_chapters(load_curriculum(language)):
        if chapter["id"] == chapter_id:
            return chapter
    raise SystemExit(f"error: {chapter_id} is not in curriculum/{language}.json")


def describe(chapter_id: str, info: dict) -> dict:
    entry = find_curriculum_entry(info["language"], chapter_id)
    return {
        "chapter_id": chapter_id,
        "language": info["language"],
        "number": info["number"],
        "type": entry["type"],
        "title": entry["title"],
        "path": str(chapter_path(info["language"], entry).relative_to(ROOT)),
        "branch": f"wip/{chapter_id}",
        "status": info["status"],
        "notes": info.get("notes", ""),
    }


def cmd_next(state: dict) -> dict:
    chapters = ordered_chapters(state)
    for cid, info in chapters:
        if info["status"] in RESUMABLE:
            return {"action": "resume", **describe(cid, info)}
    for cid, info in chapters:
        if info["status"] == "changes_requested":
            return {"action": "revise", **describe(cid, info)}
    for cid, info in chapters:
        if info["status"] == "pending":
            return {"action": "chapter", **describe(cid, info)}
    for language in state["language_order"]:
        if language not in state["languages"]:
            return {
                "action": "curriculum",
                "language": language,
                "path": f"curriculum/{language}.json",
                "template": "curriculum/python.json",
            }
    return {"action": "done"}


def require(state: dict, chapter_id: str) -> dict:
    if chapter_id not in state["chapters"]:
        raise SystemExit(f"error: unknown chapter {chapter_id}")
    return state["chapters"][chapter_id]


def cmd_start(state: dict, chapter_id: str) -> dict:
    info = require(state, chapter_id)
    expected = cmd_next(state)
    if expected.get("chapter_id") != chapter_id:
        raise SystemExit(
            f"error: the next item is {json.dumps(expected)}; refusing to start {chapter_id} out of order"
        )
    if info["status"] == "approved":
        raise SystemExit(f"error: {chapter_id} is approved and read-only")
    run_id = f"{now_iso()[:10]}-{uuid.uuid4().hex[:6]}"
    previous = info["status"]
    info["status"] = "in_progress"
    info["current_run_id"] = run_id
    info.setdefault("runs", []).append({"run_id": run_id, "started": now_iso(), "from_status": previous})
    save_state(state)
    return {"started": chapter_id, "run_id": run_id, "resumed": previous != "pending", **describe(chapter_id, info)}


def cmd_complete(state: dict, chapter_id: str) -> dict:
    info = require(state, chapter_id)
    if info["status"] != "in_progress":
        raise SystemExit(f"error: {chapter_id} is {info['status']}, not in_progress")
    entry = find_curriculum_entry(info["language"], chapter_id)
    cdir = chapter_path(info["language"], entry)
    vfile = cdir / "verification.json"
    if not vfile.exists():
        raise SystemExit(f"error: {vfile.relative_to(ROOT)} is missing; run tools/verify_chapter.py")
    report = load_json(vfile)
    problems = []
    if not report.get("passed"):
        problems.append("verification did not pass")
    if report.get("run_id") != info.get("current_run_id"):
        problems.append(
            f"verification belongs to run {report.get('run_id')}, current run is {info.get('current_run_id')}"
        )
    if report.get("fingerprint") != fingerprint(cdir):
        problems.append("chapter files changed after verification; re-run tools/verify_chapter.py")
    if problems:
        raise SystemExit("error: cannot complete: " + "; ".join(problems))
    info["status"] = "in_review"
    info["path"] = str(cdir.relative_to(ROOT))
    info["completed"] = now_iso()
    info["runs"][-1].update({"ended": now_iso(), "result": "in_review"})
    info.pop("block_reason", None)
    save_state(state)
    return {"completed": chapter_id, "status": "in_review", "path": info["path"]}


def cmd_block(state: dict, chapter_id: str, reason: str) -> dict:
    info = require(state, chapter_id)
    if info["status"] == "approved":
        raise SystemExit(f"error: {chapter_id} is approved")
    info["status"] = "blocked"
    info["block_reason"] = reason
    if info.get("runs"):
        info["runs"][-1].update({"ended": now_iso(), "result": "blocked", "reason": reason})
    save_state(state)
    return {"blocked": chapter_id, "reason": reason}


def cmd_approve(state: dict, target: str) -> dict:
    if target in state["languages"]:
        state["languages"][target]["curriculum_status"] = "approved"
        cfile = ROOT / state["languages"][target]["curriculum"]
        data = load_json(cfile)
        data["status"] = "approved"
        save_json(cfile, data)
        save_state(state)
        return {"approved_curriculum": target}
    info = require(state, target)
    if info["status"] != "in_review":
        raise SystemExit(f"error: {target} is {info['status']}; only in_review chapters can be approved")
    info["status"] = "approved"
    info["approved"] = now_iso()
    save_state(state)
    return {"approved": target}


def cmd_request_changes(state: dict, chapter_id: str, notes: str) -> dict:
    info = require(state, chapter_id)
    if info["status"] not in ("in_review", "approved"):
        raise SystemExit(f"error: {chapter_id} is {info['status']}")
    info["status"] = "changes_requested"
    info["notes"] = notes
    save_state(state)
    return {"changes_requested": chapter_id, "notes": notes}


def cmd_add_language(state: dict, language: str) -> dict:
    curriculum = load_curriculum(language)
    if language in state["languages"]:
        raise SystemExit(f"error: {language} is already registered")
    if language not in state["language_order"]:
        raise SystemExit(f"error: {language} is not in language_order")
    added = []
    for chapter in curriculum_chapters(curriculum):
        if chapter["id"] in state["chapters"]:
            raise SystemExit(f"error: duplicate chapter id {chapter['id']}")
        state["chapters"][chapter["id"]] = {
            "language": language,
            "number": chapter["number"],
            "status": "pending",
            "runs": [],
        }
        added.append(chapter["id"])
    state["languages"][language] = {
        "curriculum": f"curriculum/{language}.json",
        "curriculum_status": curriculum.get("status", "in_review"),
        "registered": now_iso(),
    }
    save_state(state)
    return {"language": language, "chapters_added": len(added)}


def cmd_status(state: dict) -> dict:
    summary: dict[str, dict[str, int]] = {}
    for _, info in state["chapters"].items():
        lang = summary.setdefault(info["language"], {})
        lang[info["status"]] = lang.get(info["status"], 0) + 1
    return {"languages": state["languages"], "chapters_by_status": summary, "next": cmd_next(state)}


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        raise SystemExit(__doc__)
    command, args = argv[1], argv[2:]
    state = load_state()
    handlers = {
        "next": lambda: cmd_next(state),
        "status": lambda: cmd_status(state),
        "start": lambda: cmd_start(state, args[0]),
        "complete": lambda: cmd_complete(state, args[0]),
        "block": lambda: cmd_block(state, args[0], " ".join(args[1:]) or "no reason given"),
        "approve": lambda: cmd_approve(state, args[0]),
        "request-changes": lambda: cmd_request_changes(state, args[0], " ".join(args[1:])),
        "add-language": lambda: cmd_add_language(state, args[0]),
    }
    if command not in handlers:
        raise SystemExit(__doc__)
    print(json.dumps(handlers[command](), indent=2))


if __name__ == "__main__":
    main(sys.argv)
