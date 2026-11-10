# file: practice/solutions/task8.py
expenses = [("milk", 12.5), ("beans", 30.0), ("milk", 8.0)]
totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount
print(totals)
