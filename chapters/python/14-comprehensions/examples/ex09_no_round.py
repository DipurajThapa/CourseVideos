# file: examples/ex09_no_round.py
prices = [3.5, 4.25]
with_tax = [price * 1.1 for price in prices]
print(with_tax)
print([round(price * 1.1, 2) for price in prices])
