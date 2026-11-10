# file: examples/ex06_paths.py
from pathlib import Path

report = Path("reports") / "monday.txt"
print(report.name)
print(report.stem)
print(report.suffix)
print(report.as_posix())
