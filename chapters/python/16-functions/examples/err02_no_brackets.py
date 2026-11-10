# file: examples/err02_no_brackets.py
def with_tax(price):
    return round(price * 1.1, 2)

tea = with_tax
print(tea + 1)
