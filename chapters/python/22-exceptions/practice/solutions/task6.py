# file: practice/solutions/task6.py
import csv

total = 0.0
with open("prices.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        try:
            total += float(row["price"])
        except ValueError:
            print(f"Skipped {row['item']}: {row['price']!r} is not a price")
print(f"Total of good prices: {total:.2f}")
