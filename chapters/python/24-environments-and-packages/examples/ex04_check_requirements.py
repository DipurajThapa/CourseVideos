# file: examples/ex04_check_requirements.py
from difflib import get_close_matches
from pathlib import Path

TRUSTED = ["requests", "tabulate", "pytest"]
path = Path("board_requirements.txt")
text = path.read_text(encoding="utf-8")
problems = 0
for line in text.splitlines():
    line = line.strip()
    if line == "" or line.startswith("#"):
        continue
    name = line.split("==")[0].lower()
    if "==" not in line:
        print(f"{line}: not pinned")
        problems += 1
    elif name not in TRUSTED:
        close = get_close_matches(name, TRUSTED, cutoff=0.8)
        hint = close[0] if close else "no trusted name"
        print(f"{line}: unknown, close to {hint}")
        problems += 1
    else:
        print(f"{line}: OK")
print(f"Problems found: {problems}")
