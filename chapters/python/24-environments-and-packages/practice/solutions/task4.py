# file: practice/solutions/task4.py
from pathlib import Path

seen = set()
text = Path("dup_requirements.txt").read_text(encoding="utf-8")
for line in text.splitlines():
    name = line.split("==")[0].lower()
    if name in seen:
        print(f"Listed twice: {name}")
    seen.add(name)
print(f"Different packages: {len(seen)}")
