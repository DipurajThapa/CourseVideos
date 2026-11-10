# file: practice/solutions/task4.py
from pathlib import Path

visits = Path("visits.txt")
if visits.exists():
    count = int(visits.read_text(encoding="utf-8"))
else:
    count = 0
count += 1
visits.write_text(str(count), encoding="utf-8")
print(f"Visit number {count}")
