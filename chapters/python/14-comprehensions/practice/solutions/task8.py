# file: practice/solutions/task8.py
orders = [12.5, 8.0, 15.25, 10.0, 22.0]
big = []
for order in orders:
    if order > 10:
        big.append(round(order * 0.9, 2))
print("Loop:", big)
ai = {round(order * 0.9, 2) for order in orders}
print("AI:", sorted(ai), "same:", sorted(ai) == big)
fixed = [round(order * 0.9, 2) for order in orders if order > 10]
print("Fixed:", fixed, "same:", fixed == big)
