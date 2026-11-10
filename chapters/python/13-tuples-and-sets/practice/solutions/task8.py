# file: practice/solutions/task8.py
orders = ["tea", "cake", "tea", "scone", "cake"]
items = set()
for item in orders:
    items.add(item)
first = sorted(items)[0]
print(f"Different items: {len(items)}")
print(f"First in order: {first}")
