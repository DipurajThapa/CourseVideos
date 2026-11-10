# file: examples/ex06_safe_get.py
import json
from pathlib import Path

text = Path("weather_sample.json").read_text(encoding="utf-8")
current = json.loads(text)["current"]
print(current.get("condition", "unknown"))
print(current.get("wind_kph", "not in this response"))
print(current["wind_kph"])
