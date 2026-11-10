# file: examples/ex06_csv_write.py
import csv

with open("orders.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["item", "qty"])
    writer.writerow(["Tea", 2])
    writer.writerow(["Café latte", 1])

with open("orders.csv", encoding="utf-8") as file:
    print(file.read(), end="")
