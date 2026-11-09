# file: examples/ex04_logic.py
total = 0
for sale in range(1, 4):
    price = float(input(f"Price of sale {sale}: "))
    total = total + sale
print(f"Total: {total:.2f}")
