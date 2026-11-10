# file: practice/solutions/task5.py
sales = [18.5, 22.0, 9.75, 31.25, 14.0]
total = sum(sales)
print(f"Total: {total:.2f}")
print(f"Average: {total / len(sales):.2f}")
print(f"Biggest: {max(sales):.2f}")
print(f"Smallest: {min(sales):.2f}")
print(f"Biggest first: {sorted(sales, reverse=True)}")
