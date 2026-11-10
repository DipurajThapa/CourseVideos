# file: examples/ai/fixed/rows_check.py
from pathlib import Path
from report_tools import read_sales

for path in sorted(Path("data").glob("*.csv")):
    sales, bad = read_sales(path)
    print(f"{path.name}: {len(sales)} good, {bad} bad")
