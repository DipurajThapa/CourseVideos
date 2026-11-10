# file: examples/ex09_no_round.py
prices = [3.5, 4.0, 4.25, 2.75]
with_tax = [price * 1.1 for price in prices]
print(with_tax)
print([round(price, 2) for price in with_tax])
