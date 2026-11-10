# file: examples/ai_diff.py
import difflib
from pathlib import Path

old = Path("stock_old.py").read_text(encoding="utf-8").splitlines()[1:]
new = Path("stock_ai.py").read_text(encoding="utf-8").splitlines()[1:]
for line in difflib.unified_diff(old, new, "old", "ai", lineterm="", n=0):
    print(line)
