# file: examples/ex05_weather.py
import json
from pathlib import Path

path = Path("weather_sample.json")
data = json.loads(path.read_text(encoding="utf-8"))
place = data["location"]["name"]
print(place, data["current"]["temp_c"])
print(data["current"]["condition"])
for slot in data["forecast"]:
    print(slot["hour"], "rain:", slot["rain_chance"])
