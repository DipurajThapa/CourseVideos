# file: examples/till_v3.py
MEMBER_DISCOUNT = 0.1
TAX_RATE = 1.1


def order_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + price * count
    if is_member:
        total = total - total * MEMBER_DISCOUNT
    with_tax = total * TAX_RATE
    return round(with_tax, 2)
