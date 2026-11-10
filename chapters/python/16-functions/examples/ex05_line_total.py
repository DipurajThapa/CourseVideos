# file: examples/ex05_line_total.py
def line_total(price, count):
    """Return the price of count items, rounded to cents."""
    return round(price * count, 2)

print(line_total(3.5, 2))
print(line_total(2.75, 3))
print(line_total.__doc__)
