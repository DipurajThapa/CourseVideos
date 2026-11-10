# file: practice/solutions/task2.py
import json
from pathlib import Path

hours = json.loads(Path("hours.json").read_text(encoding="utf-8"))
print(f"Open {hours['open']} to {hours['close']}, closed on {hours['closed_days'][0]}")
