# file: examples/err01_braces.py
prices = [3.5, 3.5, 4.0, 2.75]
with_tax = {round(price * 1.1, 2) for price in prices}
print(with_tax)
print(type(with_tax))
print(len(with_tax), len(prices))
