# file: examples/ex05_diff.py
import difflib
from pathlib import Path

old = Path("till_v2.py").read_text(encoding="utf-8").splitlines()[1:]
new = Path("till_v3.py").read_text(encoding="utf-8").splitlines()[1:]
for line in difflib.unified_diff(old, new, "v2", "v3", lineterm="", n=1):
    print(line)
