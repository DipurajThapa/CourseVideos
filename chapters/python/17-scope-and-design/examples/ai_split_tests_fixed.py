# file: examples/ai_split_tests_fixed.py
def day_total(prices):
    total = 0
    for price in prices:
        total += round(price * 1.1, 2)
    return round(total, 2)

def report_line(day, prices):
    return f"{day:<8} {len(prices)} sales {day_total(prices):>6.2f}"

cases = [("Monday", [3.5, 4.0, 2.75], "Monday   3 sales  11.28"),
         ("Sunday", [], "Sunday   0 sales   0.00"),
         ("Friday", [2.0], "Friday   1 sales   2.20")]
for day, prices, expected in cases:
    result = report_line(day, prices)
    print(day, "pass" if result == expected else "FAIL")
