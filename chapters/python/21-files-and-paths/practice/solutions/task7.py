# file: practice/solutions/task7.py
import csv
from pathlib import Path

with open("sales.csv", newline="", encoding="utf-8") as sales:
    with open("report.txt", "w", encoding="utf-8") as report:
        for row in csv.DictReader(sales):
            amount = int(row["qty"]) * float(row["price"])
            report.write(f"{row['item']}: {amount:.2f}\n")

print(Path("report.txt").read_text(encoding="utf-8").strip())
