# file: examples/ex07_loop_clearer.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25, "scone": 2.75}
total = 0
for name, price in menu.items():
    if price >= 4:
        price = price - 0.5
        name = name + " (offer)"
    print(f"{name:<16}{price:>6.2f}")
    total += price
print(f"{'Total':<16}{total:>6.2f}")
