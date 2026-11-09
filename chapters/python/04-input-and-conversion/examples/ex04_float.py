# file: examples/ex04_float.py
cake_price = float(input("Price of one cake? "))
cake_count = int(input("How many cakes? "))
total = cake_price * cake_count
print(f"{cake_count} cakes cost {total:.2f}")
