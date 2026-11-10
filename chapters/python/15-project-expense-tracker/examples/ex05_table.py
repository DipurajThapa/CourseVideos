# file: examples/ex05_table.py
expenses = [("milk", 12.5), ("beans", 30.0), ("milk", 8.0), ("cups", 6.25)]
totals = {"milk": 20.5, "beans": 30.0, "cups": 6.25}
for category in sorted(totals):
    print(f"{category:<8}{totals[category]:>7.2f}")
print(f"Expenses: {len(expenses)}  Total: {sum(totals.values()):.2f}")
