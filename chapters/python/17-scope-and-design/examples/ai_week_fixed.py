# file: examples/ai_week_fixed.py
def add_to_week(week_total, total):
    return round(week_total + total, 2)

week_total = 0
week_total = add_to_week(week_total, 11.28)
week_total = add_to_week(week_total, 8.53)
print(week_total)
