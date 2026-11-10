# file: examples/ex03_names.py
items = ["tea", "coffee", "carrot cake", "scone"]
titles = [item.title() for item in items]
lengths = [len(item) for item in items]
print(titles)
print(lengths)
print(items)
