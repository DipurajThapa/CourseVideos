# file: examples/ai_diff.py
import difflib
from pathlib import Path

old = Path("stock_old.py").read_text(encoding="utf-8")
new = Path("stock_ai.py").read_text(encoding="utf-8")
old_lines = old.splitlines()[1:]
new_lines = new.splitlines()[1:]
diff = difflib.unified_diff(old_lines, new_lines, "old", "ai",
                            lineterm="", n=0)
for line in diff:
    print(line)
