# file: examples/ai_tests_flawed.py
import json
from pathlib import Path


def price_of(data, name):
    for item in data["items"]:
        if item["name"] == name:
            return item["price"]
    return None


data = json.loads(Path("prices.json").read_text(encoding="utf-8"))
cases = [("milk", 1.2), ("oat milk", 1.85), ("flour", None)]
for name, expected in cases:
    got = price_of(data, name)
    result = "pass" if got == expected else "FAIL"
    print(f"{name}: expected {expected!r}, got {got!r}: {result}")
