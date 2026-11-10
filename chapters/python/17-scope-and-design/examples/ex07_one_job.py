# file: examples/ex07_one_job.py
def day_total(prices):
    total = 0
    for price in prices:
        total += price
    return round(total, 2)

def total_line(day, total):
    return f"{day}: {total:.2f}"

monday = day_total([3.85, 4.4, 3.03])
print(total_line("Monday", monday))
print(monday == 11.28)
