# file: examples/stock_v3.py
LOW_LIMIT = 3


def low_stock(stock, order):
    """Return the ordered items that will have fewer than 3 left."""
    low = [item for item in order
           if stock[item] - order[item] < LOW_LIMIT]
    return low


chk = low_stock  # the old name, for code that still uses it
