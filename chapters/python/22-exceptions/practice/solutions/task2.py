# file: practice/solutions/task2.py
from pathlib import Path

try:
    special = Path("special.txt").read_text(encoding="utf-8")
except FileNotFoundError:
    print("No special today.")
else:
    print(f"Today's special: {special.strip()}")
