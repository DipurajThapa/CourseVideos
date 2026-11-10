# file: examples/ex08_day_report.py
def with_tax(price, rate=1.1):
    """Return the price with tax, rounded to cents."""
    return round(price * rate, 2)

def day_total(prices, rate=1.1):
    """Return the day's total with tax."""
    total = 0
    for price in prices:
        total += with_tax(price, rate)
    return round(total, 2)

def report_line(day, prices, rate=1.1):
    """Return one report line as text."""
    return f"{day:<8} {len(prices)} sales {day_total(prices, rate):>6.2f}"

print(report_line("Monday", [3.5, 4.0, 2.75]))
print(report_line("Friday", [4.25, 3.5], rate=1.2))
print(day_total([3.5, 4.0, 2.75]) == 11.28)
