# file: examples/err02_old_name.py
def order_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + price * count
    return total


print(f([("Tea", 3.5, 2)], False))
