# file: examples/step1/read_days.py
import csv
from pathlib import Path

for name in ["2-tuesday.csv", "3-wednesday.csv"]:
    path = Path("data") / name
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            print(name, row["item"], row["amount"])
