# file: examples/ai_tests_final.py
import json
from pathlib import Path


def price_of(data, name):
    for item in data["items"]:
        if item["name"] == name:
            if item["price"] is None:
                return None
            return float(item["price"])
    return None


cases = [
    ("prices.json", "milk", 1.2),
    ("prices.json", "oat milk", 1.85),
    ("prices.json", "flour", None),
    ("prices_today.json", "oat milk", None),
]
for path, name, expected in cases:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    got = price_of(data, name)
    result = "pass" if got == expected else "FAIL"
    print(f"{path} {name}: expected {expected!r}, got {got!r}: {result}")
