# file: examples/ex05_weather.py
import json
from pathlib import Path

text = Path("weather_sample.json").read_text(encoding="utf-8")
data = json.loads(text)
print(data["location"]["name"], data["current"]["temp_c"])
print(data["current"]["condition"])
for slot in data["forecast"]:
    print(slot["hour"], slot["temp_c"], "rain:", slot["rain_chance"])
