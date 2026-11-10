# file: examples/ai_split_final.py
def day_total(prices):
    total = 0
    for price in prices:
        total += round(price * 1.1, 2)
    return round(total, 2)

def report_line(day, prices):
    total = day_total(prices)
    return f"{day:<8} {len(prices)} sales {total:>6.2f}"

def add_to_week(week_total, total):
    return round(week_total + total, 2)

monday = [3.5, 4.0, 2.75]
tuesday = [4.25, 3.5]
print(report_line("Monday", monday))
print(report_line("Tuesday", tuesday))
week_total = add_to_week(0, day_total(monday))
week_total = add_to_week(week_total, day_total(tuesday))
print(f"Week {week_total:>17.2f}")
cases = [("Monday", monday, "Monday   3 sales  11.28"),
         ("Sunday", [], "Sunday   0 sales   0.00"),
         ("Friday", [2.0], "Friday   1 sales   2.20")]
for day, prices, expected in cases:
    print(day, "pass" if report_line(day, prices) == expected else "FAIL")
