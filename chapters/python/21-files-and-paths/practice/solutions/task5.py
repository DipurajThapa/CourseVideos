# file: practice/solutions/task5.py
import csv

order = [("Tea", 2), ("Scone", 1), ("Café latte", 1)]
with open("order.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["item", "qty"])
    for item, qty in order:
        writer.writerow([item, qty])

with open("order.csv", encoding="utf-8") as file:
    print(file.read().strip())
