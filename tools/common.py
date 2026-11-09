"""Shared helpers for the course tools. Standard library only."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "state" / "progress.json"
CURRICULUM_DIR = ROOT / "curriculum"
CHAPTERS_DIR = ROOT / "chapters"
TOOLCHAINS_FILE = ROOT / ".toolchains.json"

EXCLUDED_FROM_FINGERPRINT = {"verification.json"}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def load_state() -> dict:
    return load_json(STATE_FILE)


def save_state(state: dict) -> None:
    state["updated"] = now_iso()
    save_json(STATE_FILE, state)


def load_curriculum(language: str) -> dict:
    return load_json(CURRICULUM_DIR / f"{language}.json")


def curriculum_chapters(curriculum: dict) -> list[dict]:
    chapters = []
    for module in curriculum["modules"]:
        for chapter in module["chapters"]:
            chapters.append({**chapter, "module_id": module["id"], "module_title": module["title"]})
    return sorted(chapters, key=lambda c: c["number"])


def chapter_dir_name(chapter: dict) -> str:
    return f"{chapter['number']:02d}-{chapter['slug']}"


def chapter_path(language: str, chapter: dict) -> Path:
    return CHAPTERS_DIR / language / chapter_dir_name(chapter)


def fingerprint(chapter_dir: Path) -> str:
    """Hash every file in the chapter except verification.json, in a stable order."""
    digest = hashlib.sha256()
    for path in sorted(p for p in chapter_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(chapter_dir).as_posix()
        if rel in EXCLUDED_FROM_FINGERPRINT or "__pycache__" in rel or rel.endswith(".class"):
            continue
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()
