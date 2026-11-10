# file: practice/solutions/task8.py
import csv


def load_menu(path):
    menu = {}
    try:
        with open(path, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    menu[row["item"]] = float(row["price"])
                except ValueError:
                    print(f"Skipped {row['item']}: not a price")
    except FileNotFoundError:
        print(f"{path} not found: the menu is empty")
    return menu


print(load_menu("prices.csv"))
print(load_menu("old_prices.csv"))
