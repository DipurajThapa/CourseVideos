# file: examples/ai_unit_price.py
import json
from pathlib import Path


def price_of(data, name):
    for item in data["items"]:
        if item["name"] == name:
            if item["unit_price"] is None:
                return None
            return float(item["unit_price"])
    return None


data = json.loads(Path("prices.json").read_text(encoding="utf-8"))
print(price_of(data, "milk"))
