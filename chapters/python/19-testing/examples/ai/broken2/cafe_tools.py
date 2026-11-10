# file: examples/ai/broken2/cafe_tools.py
"""Small tools for the Corner Cafe programs."""
import math


def with_tax(price, rate=1.1):
    """Return the price with tax, rounded to cents."""
    return round(price * rate, 2)


def money(amount):
    """Return an amount as text, such as USD 4.00."""
    return f"USD {amount:.2f}"


def boxes_needed(biscuits, per_box=12):
    """Return how many boxes hold the biscuits."""
    return biscuits // per_box + 1
