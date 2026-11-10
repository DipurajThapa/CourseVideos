# file: examples/err02_else_at_end.py
prices = [3.5, 4.0, 4.25, 2.75]
labels = [price for price in prices if price < 4 else 0]
print(labels)
