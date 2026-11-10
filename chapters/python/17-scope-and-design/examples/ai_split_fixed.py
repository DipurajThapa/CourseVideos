# file: examples/ai_split_fixed.py
def day_total(prices):
    total = 0
    for price in prices:
        total += round(price * 1.1, 2)
    return round(total, 2)

def report_line(day, prices):
    total = day_total(prices)
    return f"{day:<8} {len(prices)} sales {total:>6.2f}"

monday = [3.5, 4.0, 2.75]
tuesday = [4.25, 3.5]
print(report_line("Monday", monday))
print(report_line("Tuesday", tuesday))
week_total = day_total(monday) + day_total(tuesday)
print(f"Week {week_total:>17.2f}")
