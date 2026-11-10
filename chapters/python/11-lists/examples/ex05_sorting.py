# file: examples/ex05_sorting.py
sales = [12.5, 8.0, 15.75, 9.25]
print(sorted(sales))
print(sales)
sales.sort()
print(sales)
print(sorted(sales, reverse=True))
print(sum(sales), min(sales), max(sales))
