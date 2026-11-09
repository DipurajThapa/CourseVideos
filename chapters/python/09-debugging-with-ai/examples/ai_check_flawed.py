# file: examples/ai_check_flawed.py
print("Corner Cafe: end of day")
sales = int(input("How many sales today? "))
total = 0
for sale in range(1, sales + 1):
    price = float(input(f"Price of sale {sale}: "))
    total = total + price
if sales >= 0:
    average = total / sales
    print(f"Sales:   {sales}")
    print(f"Total:   {total:.2f}")
    print(f"Average: {average:.2f}")
else:
    print("No sales today.")
