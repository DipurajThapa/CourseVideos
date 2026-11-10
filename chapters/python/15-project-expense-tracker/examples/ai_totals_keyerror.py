# file: examples/ai_totals_keyerror.py
expenses = [("milk", 12.5), ("beans", 30.0), ("milk", 8.0)]
totals = {}
for category, amount in expenses:
    totals[category] += amount
print(totals)
