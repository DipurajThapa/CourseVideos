# file: examples/ex07_day_report.py
import math
from datetime import timedelta
from pathlib import Path
from cafe_tools import with_tax, money

sales = [3.5, 4.0, 2.75]
total = sum([with_tax(price) for price in sales])
boxes = math.ceil(40 / 12)
closes = timedelta(hours=8) + timedelta(hours=9, minutes=30)
report = Path("reports") / "monday.txt"

print("Total:", money(total))
print("Biscuit boxes:", boxes)
print("Closes at", closes)
print("Saved as", report.as_posix())
