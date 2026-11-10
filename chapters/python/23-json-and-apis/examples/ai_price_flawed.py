# file: examples/ai_price_flawed.py
import json
from pathlib import Path


def price_of(data, name):
    return float(data["items"][name]["price"])


data = json.loads(Path("prices.json").read_text(encoding="utf-8"))
print(price_of(data, "milk"))
