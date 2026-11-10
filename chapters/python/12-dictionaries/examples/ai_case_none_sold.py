# file: examples/ai_case_none_sold.py
stock = {"cake": 6, "scone": 4, "sandwich": 5}
sold = []
for item in sold:
    stock[item] = stock[item] - 1
for item, count in stock.items():
    print(f"{item}: {count} left")
