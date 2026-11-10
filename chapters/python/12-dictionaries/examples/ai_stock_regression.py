# file: examples/ai_stock_regression.py
cases = {
    "none sold": [],
    "last cake": ["cake", "cake"],
    "muffin": ["cake", "muffin"],
}
for name, sold in cases.items():
    print(f"Case: {name}")
    stock = {"cake": 2, "scone": 4, "sandwich": 5}
    for item in sold:
        if item in stock:
            stock[item] = stock[item] - 1
        else:
            print(f"No {item} in stock.")
    for item, count in stock.items():
        print(f"{item}: {count} left")
