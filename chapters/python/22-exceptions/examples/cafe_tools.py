# file: examples/cafe_tools.py
def with_tax(price):
    """Return the price with 10 percent tax, rounded to cents."""
    if price < 0:
        raise ValueError(f"price cannot be negative: {price}")
    return round(price * 1.1, 2)
