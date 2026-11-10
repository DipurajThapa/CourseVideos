# file: examples/ai_mine.py
import json
from pathlib import Path


def price_of(data, name):
    for item in data["items"]:
        if item["name"] == name:
            return float(item["price"])
    return None


text = Path("prices.json").read_text(encoding="utf-8")
data = json.loads(text)
print(price_of(data, "milk"))
print(price_of(data, "flour"))
