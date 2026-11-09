# file: examples/ex05_print_debug.py
total = 0
for sale in range(1, 4):
    price = float(input(f"Price of sale {sale}: "))
    total = total + sale
    print(f"DEBUG sale={sale} price={price} total={total}")
print(f"Total: {total:.2f}")
