# file: practice/solutions/task5.py
import json
from pathlib import Path

weather = json.loads(Path("weather_sample.json").read_text(encoding="utf-8"))
rainy = [slot["hour"] for slot in weather["forecast"] if slot["rain_chance"] >= 30]
if rainy:
    print("Rain likely at:", rainy)
else:
    print("No rain expected.")
