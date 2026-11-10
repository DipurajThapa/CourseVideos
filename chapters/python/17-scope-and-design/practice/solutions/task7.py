# file: practice/solutions/task7.py
def day_total(prices, rate=1.1):
    total = 0
    for price in prices:
        total += round(price * rate, 2)
    return round(total, 2)

def week_lines(days, rate=1.1):
    lines = []
    week = 0
    for day, prices in days.items():
        total = day_total(prices, rate)
        week = round(week + total, 2)
        lines.append(f"{day:<8} {total:>6.2f}")
    lines.append(f"{'Week':<8} {week:>6.2f}")
    return lines

days = {"Monday": [3.5, 4.0, 2.75], "Tuesday": [4.25, 3.5], "Sunday": []}
for line in week_lines(days):
    print(line)
