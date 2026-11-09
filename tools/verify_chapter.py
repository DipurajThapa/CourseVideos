#!/usr/bin/env python3
"""Verify one chapter and write verification.json.

Usage: python3 tools/verify_chapter.py chapters/<language>/<NN>-<slug>

Checks:
  structure      required files, headings and meta.json fields
  code           every runnable file runs on every available toolchain and matches .expected
  lesson_blocks  code and output blocks in the lesson match the verified files
  ai_pair        the flawed AI example really behaves differently from the fixed one
  practice       exactly 8 tasks in three tiers, each with a verified solution
  ai_prompts     all six AI activities are covered
  sources        at least 3 dated sources, at least 1 official
  language       banned phrases, em dashes, sentence length
  video          storyboard covers every section with verified code; the rendered
                 chapter.mp4 (narration, captions, 1080p) matches the storyboard and files

Only a full pass sets "passed": true. Never edit verification.json by hand.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, TOOLCHAINS_FILE, fingerprint, load_json, load_state, now_iso, save_json  # noqa: E402
import storyboard as sb  # noqa: E402

TIMEOUT = 15
SOURCE_EXTENSIONS = {
    "python": [".py"],
    "javascript": [".js", ".mjs"],
    "java": [".java"],
    "c": [".c"],
    "cpp": [".cpp"],
}
FENCE_LANGS = {
    "python": {"python", "py"},
    "javascript": {"javascript", "js"},
    "java": {"java"},
    "c": {"c"},
    "cpp": {"cpp", "c++"},
}
COMMENT = {"python": "#", "javascript": "//", "java": "//", "c": "//", "cpp": "//"}
LESSON_HEADINGS = [
    "Learning goals", "Why this matters", "The idea", "Build it step by step", "See the outcome",
    "Work with AI", "Common mistakes", "Think beyond", "Recap", "Practice", "What's next",
]
PROJECT_HEADINGS = [
    "The mission", "What you will build", "Acceptance criteria", "Plan it with AI",
    "Build it step by step", "Test it", "Improve it with AI", "Recap", "What's next",
]
AI_ACTIVITIES = ["Plan", "Write", "Generate", "Debug", "Test", "Improve"]
META_KEYS = [
    "id", "title", "language", "type", "badge", "xp", "concepts", "prerequisites",
    "ai_pair_moment", "research_date", "changes", "outstanding_issues",
]
MAX_AVG_SENTENCE = 18
MAX_SENTENCE = 30


class Report:
    def __init__(self) -> None:
        self.checks: list[dict] = []

    def add(self, name: str, problems: list[str], details: dict | None = None) -> None:
        self.checks.append({"name": name, "passed": not problems, "problems": problems, "details": details or {}})

    @property
    def passed(self) -> bool:
        return all(c["passed"] for c in self.checks)


# ---------------------------------------------------------------- toolchains

def toolchains(language: str) -> list[dict]:
    """Return the toolchains to run each file on, with a label and version."""
    configured = load_json(TOOLCHAINS_FILE) if TOOLCHAINS_FILE.exists() else {}
    found: list[dict] = []
    if language == "python":
        candidates = configured.get("python") or [shutil.which("python3")]
        seen = set()
        for exe in candidates:
            if not exe or not Path(exe).exists():
                continue
            version = run([exe, "--version"]).stdout.strip() or run([exe, "--version"]).stderr.strip()
            if version in seen:
                continue
            seen.add(version)
            found.append({"label": version, "cmd": lambda f, exe=exe: [[exe, f.name]]})
    elif language == "javascript" and shutil.which("node"):
        version = "Node " + run(["node", "--version"]).stdout.strip()
        found.append({"label": version, "cmd": lambda f: [["node", f.name]]})
    elif language == "java" and shutil.which("java"):
        version = run(["java", "--version"]).stdout.splitlines()[0]
        found.append({"label": version, "cmd": lambda f: [["java", f.name]]})
    elif language == "c" and shutil.which("gcc"):
        version = run(["gcc", "--version"]).stdout.splitlines()[0]
        found.append({"label": version, "cmd": lambda f: [
            ["gcc", "-std=c17", "-Wall", "-Wextra", "-Werror", "-o", "prog.out", f.name, "-lm"], ["./prog.out"]]})
    elif language == "cpp" and shutil.which("g++"):
        version = run(["g++", "--version"]).stdout.splitlines()[0]
        found.append({"label": version, "cmd": lambda f: [
            ["g++", "-std=c++20", "-Wall", "-Wextra", "-Werror", "-o", "prog.out", f.name], ["./prog.out"]]})
    return found


def run(cmd: list[str], cwd: Path | None = None, stdin: str | None = None,
        extra_env: dict | None = None) -> subprocess.CompletedProcess:
    env = {"PATH": os.environ.get("PATH", "/usr/local/bin:/usr/bin:/bin"), "LANG": "C.UTF-8", "PYTHONIOENCODING": "utf-8",
           "PYTHONDONTWRITEBYTECODE": "1", "HOME": tempfile.gettempdir()}
    env.update(extra_env or {})
    return subprocess.run(cmd, cwd=cwd, input=stdin, capture_output=True, text=True, timeout=TIMEOUT, env=env)


# When a Python file reads input from a .stdin file, the typed answers are echoed into the
# output, so .expected shows exactly what the learner sees in the terminal:
#   How many teas? 2
# A sitecustomize module replaces input() before the program starts, so tracebacks stay clean.
ECHO_INPUT = """import builtins, sys
def _echo_input(prompt=""):
    sys.stdout.write(str(prompt))
    sys.stdout.flush()
    line = sys.stdin.readline()
    if not line:
        raise EOFError("EOF when reading a line")
    line = line.rstrip("\\n")
    sys.stdout.write(line + "\\n")
    return line
builtins.input = _echo_input
"""


def normalise(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
    return "\n".join(lines).strip("\n")


def run_file(source: Path, chain: dict) -> tuple[int, str, str]:
    """Copy the file's folder to a temp dir (so runs never write into the repo) and run it."""
    stdin_file = source.with_suffix(".stdin")
    stdin = stdin_file.read_text(encoding="utf-8") if stdin_file.exists() else ""
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "work"
        shutil.copytree(source.parent, work)
        target = work / source.name
        extra_env = None
        if stdin_file.exists() and source.suffix == ".py":
            hook = Path(tmp) / "echo_input"
            hook.mkdir()
            (hook / "sitecustomize.py").write_text(ECHO_INPUT, encoding="utf-8")
            extra_env = {"PYTHONPATH": str(hook)}
        code, out, err = 0, "", ""
        for step in chain["cmd"](target):
            try:
                proc = run(step, cwd=work, stdin=stdin, extra_env=extra_env)
            except subprocess.TimeoutExpired:
                return 124, out, f"timed out after {TIMEOUT}s"
            code, out, err = proc.returncode, proc.stdout, proc.stderr
            if code != 0:
                break
        return code, out, err


# ---------------------------------------------------------------- checks

def check_structure(cdir: Path, meta: dict, report: Report) -> str:
    problems = []
    kind = meta.get("type", "lesson")
    main_doc = "project.md" if kind == "project" else "lesson.md"
    for rel in [main_doc, "ai-prompts.md", "practice/practice.md", "sources.md", "video/storyboard.json", "meta.json"]:
        if not (cdir / rel).exists():
            problems.append(f"missing {rel}")
    missing_keys = [k for k in META_KEYS if k not in meta]
    if missing_keys:
        problems.append(f"meta.json missing keys: {', '.join(missing_keys)}")
    doc = cdir / main_doc
    if doc.exists():
        headings = re.findall(r"^## (.+?)\s*$", doc.read_text(encoding="utf-8"), re.M)
        wanted = PROJECT_HEADINGS if kind == "project" else LESSON_HEADINGS
        if headings != wanted:
            problems.append(f"{main_doc} headings must be exactly {wanted}; found {headings}")
        if not re.search(r"^# .+", doc.read_text(encoding="utf-8"), re.M):
            problems.append(f"{main_doc} needs a level-1 title")
    report.add("structure", problems)
    return main_doc


def runnable_files(cdir: Path, language: str) -> tuple[list[Path], list[str]]:
    exts = SOURCE_EXTENSIONS[language]
    files, problems = [], []
    meta = load_json(cdir / "meta.json")
    support = {s for s in meta.get("support_files", [])}
    for folder in ("examples", "practice/solutions", "project"):
        base = cdir / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if path.suffix not in exts or "__pycache__" in path.parts:
                continue
            rel = path.relative_to(cdir).as_posix()
            has_expected = path.with_suffix(".expected").exists() or path.with_suffix(".expected_error").exists()
            if has_expected:
                files.append(path)
            elif rel not in support:
                problems.append(f"{rel} has no .expected or .expected_error and is not listed in support_files")
    return files, problems


def check_code(cdir: Path, language: str, report: Report) -> dict:
    chains = toolchains(language)
    files, problems = runnable_files(cdir, language)
    results: dict[str, dict] = {}
    if not chains:
        problems.append(f"no toolchain available for {language}; nothing was executed")
    for source in files:
        rel = source.relative_to(cdir).as_posix()
        results[rel] = {}
        expected_out = source.with_suffix(".expected")
        expected_err = source.with_suffix(".expected_error")
        for chain in chains:
            code, out, err = run_file(source, chain)
            ok = True
            if expected_err.exists():
                needle = expected_err.read_text(encoding="utf-8").strip()
                if code == 0 or needle not in (err + out):
                    ok = False
                    problems.append(f"{rel} [{chain['label']}]: expected an error containing {needle!r}; "
                                    f"exit {code}, stderr tail: {err.strip()[-300:]!r}")
                if expected_out.exists() and normalise(out) != normalise(expected_out.read_text(encoding="utf-8")):
                    ok = False
                    problems.append(f"{rel} [{chain['label']}]: output before the error differs from .expected")
            else:
                want = normalise(expected_out.read_text(encoding="utf-8"))
                if code != 0:
                    ok = False
                    problems.append(f"{rel} [{chain['label']}]: exit {code}: {err.strip()[-400:]}")
                elif normalise(out) != want:
                    ok = False
                    problems.append(f"{rel} [{chain['label']}]: output differs.\n--- expected\n{want}\n--- actual\n"
                                    f"{normalise(out)}")
            results[rel][chain["label"]] = "pass" if ok else "fail"
    report.add("code", problems, {"files_run": len(files), "toolchains": [c["label"] for c in chains],
                                  "results": results})
    return {"toolchains": [c["label"] for c in chains]}


FENCE_RE = re.compile(r"^```([^\n]*)\n(.*?)^```\s*$", re.S | re.M)


def check_lesson_blocks(cdir: Path, main_doc: str, language: str, report: Report) -> None:
    problems = []
    text = (cdir / main_doc).read_text(encoding="utf-8")
    comment = COMMENT[language]
    code_blocks = output_blocks = 0
    for match in FENCE_RE.finditer(text):
        info, body = match.group(1).strip().lower(), match.group(2)
        before = text[: match.start()].rstrip().splitlines()
        marker_line = before[-1].strip() if before else ""
        if info in FENCE_LANGS[language]:
            code_blocks += 1
            first = body.splitlines()[0].strip() if body.strip() else ""
            if first.startswith(f"{comment} illustrative"):
                continue
            m = re.match(rf"{re.escape(comment)} file: (\S+)$", first)
            if not m:
                problems.append(f"code block starting {first[:60]!r} needs '{comment} file: <path>' "
                                f"or '{comment} illustrative' as its first line")
                continue
            path = cdir / m.group(1)
            if not path.exists():
                problems.append(f"code block refers to missing file {m.group(1)}")
            elif normalise(path.read_text(encoding="utf-8")) != normalise(body):
                problems.append(f"code block for {m.group(1)} does not match the file")
        elif info == "output":
            output_blocks += 1
            m = re.match(r"<!-- (output|error): (\S+) -->", marker_line)
            if not m:
                problems.append("an ```output block needs '<!-- output: <file>.expected -->' or "
                                "'<!-- error: <file>.expected_error -->' on the line before it")
                continue
            kind, rel = m.groups()
            path = cdir / rel
            if not path.exists():
                problems.append(f"output block refers to missing file {rel}")
            elif kind == "output" and normalise(path.read_text(encoding="utf-8")) != normalise(body):
                problems.append(f"output block for {rel} does not match the file")
            elif kind == "error" and path.read_text(encoding="utf-8").strip() not in body:
                problems.append(f"error block does not contain the verified error line from {rel}")
        elif info and info not in {"text", "bash", "console", "shell", "powershell", "markdown", "json"}:
            problems.append(f"unknown fence language {info!r}")
    report.add("lesson_blocks", problems, {"code_blocks": code_blocks, "output_blocks": output_blocks})


def check_ai_pair(cdir: Path, meta: dict, report: Report) -> None:
    problems = []
    pair = meta.get("ai_pair_moment") or {}
    flawed, fixed = pair.get("flawed_file"), pair.get("fixed_file")
    if not flawed or not fixed:
        problems.append("meta.json ai_pair_moment needs flawed_file and fixed_file")
    else:
        fp, xp = cdir / flawed, cdir / fixed
        for p in (fp, xp):
            if not p.exists():
                problems.append(f"missing {p.relative_to(cdir)}")
        if not problems:
            f_out = fp.with_suffix(".expected")
            x_out = xp.with_suffix(".expected")
            flawed_errors = fp.with_suffix(".expected_error").exists()
            same = (f_out.exists() and x_out.exists()
                    and normalise(f_out.read_text(encoding="utf-8")) == normalise(x_out.read_text(encoding="utf-8")))
            if not flawed_errors and same:
                problems.append("the flawed and fixed files produce the same result, so the flaw is not demonstrated")
    report.add("ai_pair", problems)


def check_practice(cdir: Path, language: str, report: Report) -> None:
    problems = []
    path = cdir / "practice" / "practice.md"
    if not path.exists():
        report.add("practice", ["missing practice/practice.md"])
        return
    text = path.read_text(encoding="utf-8")
    tiers = re.findall(r"^## (.+?)\s*$", text, re.M)
    for tier in ("Warm-up", "Apply", "Stretch"):
        if not any(t.startswith(tier) for t in tiers):
            problems.append(f"missing tier heading '## {tier}'")
    tasks = re.findall(r"^### Task (\d+): .+$", text, re.M)
    if len(tasks) != 8:
        problems.append(f"expected exactly 8 tasks, found {len(tasks)}")
    sections = re.split(r"^### Task \d+: .+$", text, flags=re.M)[1:]
    for number, section in zip(tasks, sections):
        for label in ("Expected output", "Hint", "AI variant", "Solution"):
            if f"**{label}" not in section:
                problems.append(f"Task {number} is missing '**{label}**'")
        for link in re.findall(r"\]\((solutions/[^)]+)\)", section):
            target = cdir / "practice" / link
            if not target.exists():
                problems.append(f"Task {number} links to missing {link}")
            elif target.suffix in SOURCE_EXTENSIONS[language] and not (
                    target.with_suffix(".expected").exists() or target.with_suffix(".expected_error").exists()):
                problems.append(f"Task {number} solution {link} has no .expected file")
    report.add("practice", problems, {"tasks": len(tasks)})


def check_ai_prompts(cdir: Path, report: Report) -> None:
    path = cdir / "ai-prompts.md"
    if not path.exists():
        report.add("ai_prompts", ["missing ai-prompts.md"])
        return
    headings = re.findall(r"^## (.+?)\s*$", path.read_text(encoding="utf-8"), re.M)
    problems = [f"missing a '## {a}: ...' prompt card" for a in AI_ACTIVITIES
                if not any(h.startswith(a) for h in headings)]
    text = path.read_text(encoding="utf-8")
    for label in ("Prompt", "Use it when", "A good answer", "Check it"):
        if text.count(f"**{label}") < len(AI_ACTIVITIES):
            problems.append(f"each prompt card needs a '**{label}**' line")
    report.add("ai_prompts", problems)


def check_sources(cdir: Path, language: str, report: Report) -> None:
    path = cdir / "sources.md"
    if not path.exists():
        report.add("sources", ["missing sources.md"])
        return
    official = load_json(ROOT / "tools" / "official_domains.json").get(language, [])
    rows = [line for line in path.read_text(encoding="utf-8").splitlines()
            if line.startswith("|") and "http" in line]
    problems = []
    if len(rows) < 3:
        problems.append(f"need at least 3 sources in the table, found {len(rows)}")
    if not any(any(domain in row for domain in official) for row in rows):
        problems.append(f"need at least one official source from {official}")
    for row in rows:
        if not re.search(r"\b20\d\d-\d\d-\d\d\b", row):
            problems.append(f"source row has no access date: {row[:80]}")
    report.add("sources", problems, {"sources": len(rows)})


def prose_sentences(markdown: str) -> list[str]:
    text = FENCE_RE.sub(" ", markdown)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    kept = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "|", "---")):
            continue
        s = re.sub(r"^([-*]|\d+\.)\s+", "", s)
        s = re.sub(r"`[^`]*`", "Code", s)
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
        s = re.sub(r"[*_>]", "", s)
        kept.append(s if re.search(r"[.!?:]$", s) else s + ".")
    joined = " ".join(kept)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", joined)
    return [p for p in parts if re.search(r"[A-Za-z]", p)]


def check_language(cdir: Path, main_doc: str, report: Report) -> None:
    problems = []
    banned = [b.strip().lower() for b in (ROOT / "tools" / "banned_phrases.txt").read_text(encoding="utf-8").splitlines()
              if b.strip() and not b.startswith("#")]
    for md in sorted(cdir.rglob("*.md")):
        rel = md.relative_to(cdir).as_posix()
        text = md.read_text(encoding="utf-8")
        if "—" in text:
            problems.append(f"{rel} contains an em dash")
        lowered = text.lower()
        for phrase in banned:
            if re.search(rf"\b{re.escape(phrase)}\b", lowered):
                problems.append(f"{rel} uses banned phrase {phrase!r}")
    stats = {}
    for rel in (main_doc, "video/script.md"):
        path = cdir / rel
        if not path.exists():
            continue
        sentences = prose_sentences(path.read_text(encoding="utf-8"))
        lengths = [len(s.split()) for s in sentences]
        avg = sum(lengths) / len(lengths) if lengths else 0
        stats[rel] = {"sentences": len(lengths), "average_words": round(avg, 1), "longest": max(lengths, default=0)}
        if avg > MAX_AVG_SENTENCE:
            problems.append(f"{rel}: average sentence length {avg:.1f} words exceeds {MAX_AVG_SENTENCE}")
        for s, n in zip(sentences, lengths):
            if n > MAX_SENTENCE:
                problems.append(f"{rel}: {n}-word sentence: {s[:120]!r}")
    report.add("language", problems, stats)


def check_video(cdir: Path, report: Report, kind: str) -> None:
    """The storyboard is valid and the rendered video matches it and the verified files."""
    problems: list[str] = []
    details: dict = {}
    if not (cdir / sb.STORYBOARD).exists():
        report.add("video", [f"missing {sb.STORYBOARD}"])
        return
    try:
        board = sb.load(cdir)
    except json.JSONDecodeError as exc:
        report.add("video", [f"{sb.STORYBOARD} is not valid JSON: {exc}"])
        return
    language = cdir.parent.name
    files, _ = runnable_files(cdir, language)
    runnable = {f.relative_to(cdir).as_posix() for f in files}
    problems += sb.validate(cdir, board, kind, runnable)
    details["estimated_minutes"] = round(sb.estimate_seconds(board) / 60, 1)
    for rel in (sb.VIDEO_FILE, sb.CAPTIONS_FILE, sb.RENDER_MANIFEST, sb.DESCRIPTION_FILE, sb.SCRIPT_FILE):
        if not (cdir / rel).exists():
            problems.append(f"missing {rel}: run python3 tools/render_video.py {cdir.relative_to(ROOT).as_posix()}")
    if problems:
        report.add("video", problems, details)
        return
    manifest = load_json(cdir / sb.RENDER_MANIFEST)
    if manifest.get("storyboard_sha256") != sb.storyboard_sha(cdir):
        problems.append("storyboard.json changed after the video was rendered; render again")
    if manifest.get("inputs_sha256") != sb.inputs_sha(cdir, board):
        problems.append("a code or output file shown in the video changed after rendering; render again")
    video = cdir / sb.VIDEO_FILE
    if manifest.get("video_sha256") != hashlib.sha256(video.read_bytes()).hexdigest():
        problems.append("chapter.mp4 does not match render.json; render again")
    if (cdir / sb.SCRIPT_FILE).read_text(encoding="utf-8") != sb.script_markdown(board, manifest):
        problems.append("video/script.md is out of date; run tools/render_video.py --script")
    if shutil.which("ffprobe"):
        probe = run(["ffprobe", "-v", "error", "-show_entries",
                     "format=duration:stream=codec_type,codec_name,width,height", "-of", "json", str(video)])
        info = json.loads(probe.stdout or "{}")
        kinds = {s.get("codec_type"): s for s in info.get("streams", [])}
        duration = float(info.get("format", {}).get("duration", 0))
        if "video" not in kinds or (kinds["video"].get("width"), kinds["video"].get("height")) != (1920, 1080):
            problems.append("chapter.mp4 needs a 1920x1080 video stream")
        if "audio" not in kinds:
            problems.append("chapter.mp4 has no narration audio")
        if "subtitle" not in kinds:
            problems.append("chapter.mp4 has no caption track")
        if abs(duration - float(manifest.get("duration_seconds", 0))) > 1:
            problems.append("chapter.mp4 duration does not match render.json")
        if not sb.MIN_MINUTES * 60 <= duration <= sb.MAX_MINUTES * 60:
            problems.append(f"video length {duration / 60:.1f} min is outside {sb.MIN_MINUTES} to "
                            f"{sb.MAX_MINUTES} min")
        details.update({"duration_seconds": round(duration, 1), "size_mb": manifest.get("size_mb"),
                        "scenes": len(manifest.get("scenes", [])), "voice": manifest.get("voice", {}).get("model")})
    else:
        problems.append("ffprobe is not available, so the video could not be checked")
    report.add("video", problems, details)


# ---------------------------------------------------------------- main

def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    cdir = (ROOT / sys.argv[1]).resolve() if not Path(sys.argv[1]).is_absolute() else Path(sys.argv[1])
    language = cdir.parent.name
    if language not in SOURCE_EXTENSIONS:
        print(f"error: unknown language folder {language!r}")
        return 2
    meta = load_json(cdir / "meta.json")
    report = Report()
    main_doc = check_structure(cdir, meta, report)
    chains = check_code(cdir, language, report)
    if (cdir / main_doc).exists():
        check_lesson_blocks(cdir, main_doc, language, report)
    check_ai_pair(cdir, meta, report)
    check_practice(cdir, language, report)
    check_ai_prompts(cdir, report)
    check_sources(cdir, language, report)
    check_language(cdir, main_doc, report)
    check_video(cdir, report, meta.get("type", "lesson"))

    state = load_state()
    run_id = state["chapters"].get(meta.get("id", ""), {}).get("current_run_id")
    result = {
        "chapter_id": meta.get("id"),
        "run_id": run_id,
        "verified_at": now_iso(),
        "passed": report.passed,
        "toolchains": chains["toolchains"],
        "checks": report.checks,
        "fingerprint": fingerprint(cdir),
    }
    save_json(cdir / "verification.json", result)
    for check in report.checks:
        mark = "PASS" if check["passed"] else "FAIL"
        print(f"[{mark}] {check['name']}")
        for problem in check["problems"]:
            print(f"       - {problem}")
    print(f"\nOverall: {'PASSED' if report.passed else 'FAILED'} (run {run_id}); wrote verification.json")
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main())
