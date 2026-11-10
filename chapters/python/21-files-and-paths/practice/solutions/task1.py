# file: practice/solutions/task1.py
from pathlib import Path

note = Path("special.txt")
note.write_text("Today's special: Carrot cake\n", encoding="utf-8")
print(note.read_text(encoding="utf-8").strip())
