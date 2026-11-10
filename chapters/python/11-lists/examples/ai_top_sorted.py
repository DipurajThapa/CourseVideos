# file: examples/ai_top_sorted.py
sales = [12.5, 8.0, 15.75, 9.25, 21.0, 6.5]
top = sorted(sales, reverse=True)
print(f"Top three: {top[:3]}")
print(f"Day order: {sales}")
