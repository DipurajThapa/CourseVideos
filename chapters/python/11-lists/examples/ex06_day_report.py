# file: examples/ex06_day_report.py
sales = [12.5, 8.0, 15.75, 9.25, 21.0]
sales.append(6.5)
total = sum(sales)
print(f"Sales today: {len(sales)}")
print(f"Total: {total:.2f}")
print(f"Average: {total / len(sales):.2f}")
print(f"Biggest: {max(sales):.2f}")
print(f"Smallest: {min(sales):.2f}")
print(f"Last three: {sales[-3:]}")
best = sorted(sales, reverse=True)
print(f"Best two: {best[:2]}")
print(f"In order of the day: {sales}")
