# file: examples/ex02_loads.py
import json
from pathlib import Path

text = Path("scone.json").read_text(encoding="utf-8")
data = json.loads(text)
print(type(text), type(data))
print(data["sizes"][1])
print(data["vegan"], data["offer"])
print(data["offer"] is None)
