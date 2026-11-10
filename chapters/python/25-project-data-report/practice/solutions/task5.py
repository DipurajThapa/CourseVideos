# file: practice/solutions/task5.py
sales = [("tea", 3.5), ("cake", 4.25), ("tea", 3.5), ("soup", 5.0)]
items = {}
for item, amount in sales:
    items[item] = items.get(item, 0) + amount
for item, amount in items.items():
    print(f"{item:<6}{amount:>6.2f}")
