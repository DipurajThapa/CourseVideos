# file: examples/ex03_running_total.py
total = 0
count = 0
price = float(input("Price (0 to finish): "))
while price != 0:
    total += price
    count += 1
    price = float(input("Price (0 to finish): "))
print(f"Items: {count}")
print(f"Total: {total:.2f}")
