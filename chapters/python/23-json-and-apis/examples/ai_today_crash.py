# file: examples/ai_today_crash.py
import json
from pathlib import Path


def price_of(data, name):
    for item in data["items"]:
        if item["name"] == name:
            return float(item["price"])
    return None


data = json.loads(Path("prices_today.json").read_text(encoding="utf-8"))
print(price_of(data, "milk"))
print(price_of(data, "oat milk"))
