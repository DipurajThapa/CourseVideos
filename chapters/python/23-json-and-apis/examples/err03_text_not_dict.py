# file: examples/err03_text_not_dict.py
from pathlib import Path

text = Path("scone.json").read_text(encoding="utf-8")
print(text["item"])
