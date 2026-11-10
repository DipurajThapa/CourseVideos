# file: examples/ex07_same.py
from till_old import f
from till_final import order_total

orders = [[("Tea", 3.5, 2), ("Cake", 4.25, 1)], [("Juice", 2.75, 3)], []]
for order in orders:
    for member in [False, True]:
        old = f(order, member)
        new = order_total(order, member)
        print(old, new, old == new)
