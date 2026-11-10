# file: examples/ex02_tax_comp.py
prices = [3.5, 4.0, 4.25, 2.75]
with_tax = [round(price * 1.1, 2) for price in prices]
print(with_tax)
print(len(with_tax), len(prices))
