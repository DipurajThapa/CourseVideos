# file: examples/ai_close_day_original.py
week_total = 0

def close_day(day, prices):
    global week_total
    total = 0
    for price in prices:
        total += round(price * 1.1, 2)
    total = round(total, 2)
    print(f"{day:<8} {len(prices)} sales {total:>6.2f}")
    week_total = round(week_total + total, 2)

close_day("Monday", [3.5, 4.0, 2.75])
close_day("Tuesday", [4.25, 3.5])
print(f"Week {week_total:>17.2f}")
