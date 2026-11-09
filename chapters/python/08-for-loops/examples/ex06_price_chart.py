# file: examples/ex06_price_chart.py
tea_price = 3.5
print("Teas   Price")
for teas in range(1, 11):
    free = teas // 5
    cost = (teas - free) * tea_price
    print(f"{teas:>4} {cost:>7.2f}")
print("Every 5th tea is free.")
