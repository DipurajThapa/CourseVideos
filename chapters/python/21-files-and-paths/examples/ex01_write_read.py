# file: examples/ex01_write_read.py
from pathlib import Path

note = Path("note.txt")
note.write_text("Asha: 4 out of 4\n", encoding="utf-8")
print(note.read_text(encoding="utf-8"))
print(note.exists())
