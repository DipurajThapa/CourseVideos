# file: examples/ai_own_total.py
def day_total(prices):
    total = 0
    for price in prices:
        total += round(price * 1.1, 2)
    return round(total, 2)

print(day_total([3.5, 4.0, 2.75]))
print(day_total([4.25, 3.5]))
