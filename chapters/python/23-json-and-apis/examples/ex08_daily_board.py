# file: examples/ex08_daily_board.py
import json
from pathlib import Path


def load_json(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


weather = load_json("weather_sample.json")
temp = weather["current"]["temp_c"]
drink = "Iced tea" if temp >= 30 else "Hot tea"
rain = [slot["hour"] for slot in weather["forecast"] if slot["rain_chance"] >= 30]
board = {"drink": drink, "temp_c": temp, "rain_hours": rain, "tip": "Café au lait"}

text = json.dumps(board, indent=2, ensure_ascii=False)
Path("board.json").write_text(text, encoding="utf-8")
print(Path("board.json").read_text(encoding="utf-8"))
