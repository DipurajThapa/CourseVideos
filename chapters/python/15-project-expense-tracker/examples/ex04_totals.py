# file: examples/ex04_totals.py
expenses = [("milk", 12.5), ("beans", 30.0), ("milk", 8.0), ("cups", 6.25)]
totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount
print(totals)
