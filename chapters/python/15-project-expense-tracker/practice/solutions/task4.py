# file: practice/solutions/task4.py
expenses = [("cups", 6.25), ("milk", 9.0), ("cups", 4.5), ("repairs", 45.0)]
totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount
for category in sorted(totals):
    print(f"{category:<8}{totals[category]:>7.2f}")
