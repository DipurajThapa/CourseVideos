# file: examples/ex01_read_requirements.py
from pathlib import Path

path = Path("requirements.txt")
text = path.read_text(encoding="utf-8")
for line in text.splitlines():
    line = line.strip()
    if line == "" or line.startswith("#"):
        continue
    name, version = line.split("==")
    print(f"{name:<10} {version}")
