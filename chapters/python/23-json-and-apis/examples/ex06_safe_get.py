# file: examples/ex06_safe_get.py
import json
from pathlib import Path

path = Path("weather_sample.json")
data = json.loads(path.read_text(encoding="utf-8"))
current = data["current"]
print(current.get("condition", "unknown"))
print(current.get("wind_kph", "not sent"))
print(current["wind_kph"])
