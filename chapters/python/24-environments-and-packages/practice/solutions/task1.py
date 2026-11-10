# file: practice/solutions/task1.py
from pathlib import Path

text = Path("requirements.txt").read_text(encoding="utf-8")
count = 0
for line in text.splitlines():
    line = line.strip()
    if line and not line.startswith("#"):
        count += 1
print(f"Packages listed: {count}")
