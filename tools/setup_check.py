#!/usr/bin/env python3
"""Check the toolchains a run needs and record them in .toolchains.json.

For Python, the tool also tries to install the newest stable CPython with uv, so
examples are verified on the current release as well as the system interpreter.
Pre-releases (alpha, beta, release candidate) are never used.

uv is always upgraded with pip and run as `python3 -m uv`. An older uv binary
earlier on PATH has a stale list of Python builds and silently misses new
releases (this is why Python 3.15.2 was missed on 2026-11-09).

It also prepares the video toolchain (ffmpeg, ffprobe, Pillow, Piper and the
pinned narration voice) by calling tools/render_video.py --setup.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import TOOLCHAINS_FILE, save_json  # noqa: E402

CANDIDATE_PYTHONS = ["3.16", "3.15", "3.14", "3.13"]


def sh(cmd: list[str], timeout: int = 300) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def is_stable(version_text: str) -> bool:
    return bool(re.fullmatch(r"Python \d+\.\d+\.\d+", version_text.strip()))


def newest_stable_python() -> str | None:
    sh([sys.executable, "-m", "pip", "install", "--quiet", "--upgrade", "--break-system-packages", "uv"])
    uv = [sys.executable, "-m", "uv"]
    if sh(uv + ["--version"]).returncode != 0:
        return None
    for minor in CANDIDATE_PYTHONS:
        sh(uv + ["python", "install", minor])
        found = sh(uv + ["python", "find", minor])
        exe = found.stdout.strip()
        if found.returncode == 0 and exe:
            version = sh([exe, "--version"]).stdout.strip()
            if is_stable(version):
                return exe
            sh(uv + ["python", "uninstall", minor])
    return None


def main() -> int:
    report: dict = {}
    pythons = [shutil.which("python3")]
    latest = newest_stable_python()
    if latest:
        pythons.insert(0, latest)
    report["python"] = [p for p in dict.fromkeys(pythons) if p]
    for name in ("node", "java", "gcc", "g++"):
        report[name] = shutil.which(name)
    video = sh([sys.executable, str(Path(__file__).resolve().parent / "render_video.py"), "--setup"], timeout=900)
    report["video"] = video.stdout.strip().splitlines()[-1] if video.returncode == 0 and video.stdout.strip() else None
    if video.returncode != 0:
        print("Video setup failed:\n" + (video.stdout + video.stderr)[-1500:])
    save_json(TOOLCHAINS_FILE, report)

    print(json.dumps(report, indent=2))
    missing = [k for k, v in report.items() if not v]
    for exe in report["python"]:
        print(exe, sh([exe, "--version"]).stdout.strip())
    if missing:
        print(f"MISSING: {', '.join(missing)}")
        return 1
    print("All toolchains available.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
