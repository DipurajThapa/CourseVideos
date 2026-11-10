# file: examples/ex09_return_too_early.py
def day_total(prices):
    total = 0
    for price in prices:
        total += price
        return total

print(day_total([3.5, 4.0, 2.75]))
