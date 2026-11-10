# file: examples/ai_case_last_cake.py
stock = {"cake": 2, "scone": 4, "sandwich": 5}
sold = ["cake", "cake"]
for item in sold:
    stock[item] = stock[item] - 1
for item, count in stock.items():
    print(f"{item}: {count} left")
