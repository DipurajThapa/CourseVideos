# file: examples/err04_text_numbers.py
import csv

total = 0.0
with open("sales.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        total = total + row["price"]
print(total)
