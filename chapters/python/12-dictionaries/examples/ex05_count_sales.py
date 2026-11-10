# file: examples/ex05_count_sales.py
sold = ["tea", "cake", "tea", "scone", "tea", "cake"]
counts = {}
for item in sold:
    counts[item] = counts.get(item, 0) + 1
print(counts)
print(counts["tea"])
