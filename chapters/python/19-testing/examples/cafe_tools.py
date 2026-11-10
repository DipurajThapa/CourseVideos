# file: examples/cafe_tools.py
"""Small tools for the Corner Cafe programs."""
import math


def with_tax(price, rate=1.1):
    """Return the price with tax, rounded to cents."""
    return round(price * rate, 2)


def money(amount):
    """Return an amount as text with two decimal places."""
    return f"{amount:.2f}"


def boxes_needed(biscuits, per_box=12):
    """Return how many boxes hold the biscuits."""
    return math.ceil(biscuits / per_box)
