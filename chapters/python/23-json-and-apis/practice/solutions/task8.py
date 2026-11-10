# file: practice/solutions/task8.py
import json
from pathlib import Path


def current_temp(data):
    return data.get("current", {}).get("temp_c")


weather = json.loads(Path("weather_sample.json").read_text(encoding="utf-8"))
print(current_temp(weather))
print(current_temp({"location": {"name": "Hilltop"}}))
