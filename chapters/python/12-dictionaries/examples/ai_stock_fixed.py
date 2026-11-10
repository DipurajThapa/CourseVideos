# file: examples/ai_stock_fixed.py
stock = {"cake": 6, "scone": 4, "sandwich": 5}
sold = ["cake", "scone", "cake"]
for item in sold:
    stock[item] = stock[item] - 1
for item, count in stock.items():
    print(f"{item}: {count} left")
