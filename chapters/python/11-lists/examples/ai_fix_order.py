# file: examples/ai_fix_order.py
sales = [12.5, 8.0, 15.75, 9.25, 21.0, 6.5]
sales.sort(reverse=True)
print(f"Top three: {sales[:3]}")
print(f"Day order: {sales}")
