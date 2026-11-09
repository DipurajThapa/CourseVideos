#!/usr/bin/env python3
"""Check the toolchains a run needs and record them in .toolchains.json.

For Python, the tool also tries to install the newest stable CPython with uv, so
examples are verified on the current release as well as the system interpreter.
Pre-releases (alpha, beta, release candidate) are never used.
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
    if not shutil.which("uv"):
        sh([sys.executable, "-m", "pip", "install", "--quiet", "--break-system-packages", "uv"])
    if not shutil.which("uv"):
        return None
    for minor in CANDIDATE_PYTHONS:
        sh(["uv", "python", "install", minor])
        found = sh(["uv", "python", "find", minor])
        exe = found.stdout.strip()
        if found.returncode == 0 and exe:
            version = sh([exe, "--version"]).stdout.strip()
            if is_stable(version):
                return exe
            sh(["uv", "python", "uninstall", minor])
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
