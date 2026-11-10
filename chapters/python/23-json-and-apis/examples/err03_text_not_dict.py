# file: examples/err03_text_not_dict.py
from pathlib import Path

path = Path("scone.json")
text = path.read_text(encoding="utf-8")
print(text["item"])
