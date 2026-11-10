# file: examples/ai_top_regression.py
sales = [12.5, 8.0, 15.75, 9.25, 21.0, 6.5]
top = sorted(sales, reverse=True)
print(top[:3], sales)
sales = [5.0, 5.0, 5.0, 1.0]
top = sorted(sales, reverse=True)
print(top[:3], sales)
sales = [4.0, 9.0]
top = sorted(sales, reverse=True)
print(top[:3], sales)
