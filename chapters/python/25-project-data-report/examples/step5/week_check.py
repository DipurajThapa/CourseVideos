# file: examples/step5/week_check.py
import json
from pathlib import Path
from report_tools import build_week

week = build_week(Path("data"))
print(json.dumps(week["days"], indent=2))
print("Total:", week["total"])
print("Skipped:", week["skipped"])
