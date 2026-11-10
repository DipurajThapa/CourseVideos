# file: examples/err01_tidy_rounding.py
from till_old import f


def order_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + round(price * count * 1.1, 2)
    if is_member:
        total = total - total * 0.1
    return round(total, 2)


for teas in [2, 1]:
    order = [("Tea", 3.5, teas), ("Cake", 4.25, 1)]
    print(f(order, True), order_total(order, True))
