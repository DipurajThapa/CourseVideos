# file: examples/till_final.py
"""Order totals for the Corner Cafe till."""
MEMBER_DISCOUNT = 0.1
TAX_RATE = 1.1


def subtotal(items):
    """Return the price of every item times its count, added up."""
    total = 0
    for name, price, count in items:
        total = total + price * count
    return total


def order_total(items, is_member):
    """Return the total to pay, with the member discount and tax."""
    total = subtotal(items)
    if is_member:
        total = total - total * MEMBER_DISCOUNT
    return round(total * TAX_RATE, 2)
