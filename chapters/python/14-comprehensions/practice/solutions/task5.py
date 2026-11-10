# file: practice/solutions/task5.py
stock = {"tea": 40, "cake": 3, "scone": 0, "coffee": 25}
in_stock = {name: count for name, count in stock.items() if count > 0}
low = [name for name, count in stock.items() if count < 5]
print(in_stock)
print("Order more:", low)
