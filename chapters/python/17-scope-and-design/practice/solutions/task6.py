# file: practice/solutions/task6.py
def order_total(prices):
    total = 0
    for price in prices:
        total += price
    return round(total, 2)

def summary_text(name, total):
    return f"{name} pays {total:.2f}"

total = order_total([3.5, 4.0, 2.75])
print(summary_text("Lina", total))
print(total == 10.25)
print(order_total([]) == 0)
