# file: practice/solutions/task7.py
import json
from pathlib import Path

report = {}
for line in Path("requirements.txt").read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line == "" or line.startswith("#"):
        continue
    name, version = line.split("==")
    report[name] = version
Path("report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(Path("report.json").read_text(encoding="utf-8"))
