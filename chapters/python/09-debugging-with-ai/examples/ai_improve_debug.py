# file: examples/ai_improve_debug.py
print("Corner Cafe: end of day")
sales = int(input("How many sales today? "))
total = 0
for sale_number in range(1, sales + 1):
    price = float(input(f"Price of sale {sale_number}: "))
    total = total + price
    print(f"DEBUG total={total}")
if sales > 0:
    average = total / sales
    print(f"Sales:   {sales}")
    print(f"Total:   {total:.2f}")
    print(f"Average: {average:.2f}")
else:
    print("No sales today.")
