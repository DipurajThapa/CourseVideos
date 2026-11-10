# file: practice/solutions/task1.py
import csv
from pathlib import Path

Path("day.csv").write_text("item,amount\ntea,3.50\ncake,4.25\n", encoding="utf-8")
with open("day.csv", encoding="utf-8", newline="") as file:
    for row in csv.DictReader(file):
        print(row["item"], "costs", row["amount"])
