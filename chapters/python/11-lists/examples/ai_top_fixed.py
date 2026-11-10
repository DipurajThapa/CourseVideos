# file: examples/ai_top_fixed.py
sales = [12.5, 8.0, 15.75, 9.25, 21.0, 6.5]
sales.sort(reverse=True)
top_three = sales[:3]
print(f"Top three: {top_three}")
