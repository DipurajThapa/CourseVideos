# file: examples/ex01_tax_loop.py
prices = [3.5, 4.0, 4.25, 2.75]
with_tax = []
for price in prices:
    with_tax.append(round(price * 1.1, 2))
print(with_tax)
