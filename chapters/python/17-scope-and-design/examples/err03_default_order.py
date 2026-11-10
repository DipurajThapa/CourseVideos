# file: examples/err03_default_order.py
def with_tax(rate=1.1, price):
    return round(price * rate, 2)

print(with_tax(price=3.5))
