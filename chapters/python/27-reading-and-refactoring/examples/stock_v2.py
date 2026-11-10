# file: examples/stock_v2.py
LOW_LIMIT = 3


def low_stock(stock, order):
    low = []
    for item in order:
        if stock[item] - order[item] < LOW_LIMIT:
            low.append(item)
    return low
