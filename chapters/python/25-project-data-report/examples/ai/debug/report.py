# file: examples/ai/debug/report.py
"""Corner Cafe week report: reads data/*.csv, writes two files."""
import json
from pathlib import Path
from report_tools import build_week, load_config, report_lines

try:
    config = load_config(Path("config.json"))
    week = build_week(Path("data"))
except ValueError as error:
    print("Report stopped:", error)
else:
    with open("report.txt", "w", encoding="utf-8") as file:
        for line in report_lines(week, config):
            file.write(line + "\n")
    saved = json.dumps(week, indent=2)
    Path("report.json").write_text(saved, encoding="utf-8")
    print(Path("report.txt").read_text(encoding="utf-8"), end="")
    print("Saved report.txt and report.json")
