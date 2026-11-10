# file: examples/ex07_csv_read.py
import csv

total = 0.0
with open("sales.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        amount = int(row["qty"]) * float(row["price"])
        total += amount
        print(f"{row['item']:<11}{amount:>7.2f}")
print(f"{'Total':<11}{total:>7.2f}")
