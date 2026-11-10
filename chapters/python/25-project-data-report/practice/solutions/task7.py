# file: practice/solutions/task7.py
import json
from pathlib import Path

week = {"Monday": 14.0, "Tuesday": 11.25}
with open("summary.txt", "w", encoding="utf-8") as file:
    for day, amount in week.items():
        file.write(f"{day}: {amount:.2f}\n")
Path("summary.json").write_text(json.dumps(week), encoding="utf-8")

print(Path("summary.txt").read_text(encoding="utf-8"), end="")
print(json.loads(Path("summary.json").read_text(encoding="utf-8")))
