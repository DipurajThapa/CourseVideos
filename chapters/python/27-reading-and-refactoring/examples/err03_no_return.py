# file: examples/err03_no_return.py
def subtotal(items):
    total = 0
    for name, price, count in items:
        total = total + price * count


def order_total(items):
    return round(subtotal(items) * 1.1, 2)


print(order_total([("Tea", 3.5, 2)]))
