# file: examples/ex04_week_sales.py
total = 0
for day in range(1, 4):
    sales = float(input(f"Sales on day {day}: "))
    total += sales
print(f"Total: {total:.2f}")
print(f"Average: {total / 3:.2f}")
