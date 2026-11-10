# file: practice/solutions/task6.py
import csv

cups = 0
with open("sales.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        cups += int(row["qty"])
print(f"Items sold today: {cups}")
