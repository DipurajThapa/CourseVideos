# file: examples/ex07_traceback.py
def with_tax(price):
    return round(price * 1.1, 2)

def day_total(prices):
    total = 0
    for price in prices:
        total += with_tax(price)
    return round(total, 2)

print(day_total([3.5, "4.0"]))
