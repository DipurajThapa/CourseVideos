# file: examples/err04_changed_test.py
from till_old import f


def tidy_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + price * count
    return round(total * 1.1, 2)


order = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]
print("Old:", f(order, True))
print("New:", tidy_total(order, True))
