# file: examples/stock_final.py
LOW_LIMIT = 3


def low_stock(stock, order):
    """Return the ordered items that will have fewer than 3 left."""
    low = []
    for item in order:
        if stock[item] - order[item] < LOW_LIMIT:
            low.append(item)
    return low


chk = low_stock  # the old name, for code that still uses it
