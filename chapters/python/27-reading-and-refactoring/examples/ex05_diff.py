# file: examples/ex05_diff.py
import difflib
from pathlib import Path

old = Path("till_v2.py").read_text(encoding="utf-8")
new = Path("till_v3.py").read_text(encoding="utf-8")
old_lines = old.splitlines()[1:]
new_lines = new.splitlines()[1:]
diff = difflib.unified_diff(old_lines, new_lines, "v2", "v3",
                            lineterm="", n=1)
for line in diff:
    print(line)
