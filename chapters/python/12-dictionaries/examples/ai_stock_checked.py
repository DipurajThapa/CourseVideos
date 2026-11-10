# file: examples/ai_stock_checked.py
stock = {"cake": 6, "scone": 4, "sandwich": 5}
sold = ["cake", "muffin"]
for item in sold:
    if item in stock:
        stock[item] = stock[item] - 1
    else:
        print(f"No {item} in stock.")
for item, count in stock.items():
    print(f"{item}: {count} left")
