# file: examples/ex08_day_report.py
def with_tax(price):
    """Return the price with 10 percent tax, rounded to cents."""
    return round(price * 1.1, 2)

def day_total(prices):
    """Return the total of a day's prices, with tax."""
    total = 0
    for price in prices:
        total += with_tax(price)
    return round(total, 2)

def report(day, prices):
    """Print one summary line for one day."""
    print(f"{day:<9} {len(prices)} sales  {day_total(prices):>6.2f}")

report("Monday", [3.5, 4.0, 2.75])
report("Tuesday", [4.25, 3.5])
report("Friday", [])
