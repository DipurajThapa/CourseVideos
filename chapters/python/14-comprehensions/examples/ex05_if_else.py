# file: examples/ex05_if_else.py
prices = [3.5, 4.0, 4.25, 2.75]
under_4 = [price for price in prices if price < 4]
labels = ["snack" if price < 4 else "treat" for price in prices]
print(under_4)
print(labels)
