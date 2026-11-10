# file: examples/ex04_exists.py
from pathlib import Path

saved = Path("scores.txt")
if saved.exists():
    print(saved.read_text(encoding="utf-8"))
else:
    print("No scores yet. Play a round first.")
