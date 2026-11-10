# file: examples/ex05_paths.py
from pathlib import Path

report = Path("reports") / "sales.csv"
print(report.as_posix())
print(report.name, report.suffix)
print(report.parent.as_posix())
print(report.exists())
