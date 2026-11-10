# file: examples/till_v2.py
def order_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + price * count
    if is_member:
        total = total - total * 0.1
    with_tax = total * 1.1
    return round(with_tax, 2)
