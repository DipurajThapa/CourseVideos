# file: examples/ex06_logic_fixed.py
total = 0
for sale in range(1, 4):
    price = float(input(f"Price of sale {sale}: "))
    total = total + price
print(f"Total: {total:.2f}")
