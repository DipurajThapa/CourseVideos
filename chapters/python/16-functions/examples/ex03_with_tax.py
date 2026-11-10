# file: examples/ex03_with_tax.py
def with_tax(price):
    return round(price * 1.1, 2)

tea = with_tax(3.5)
print(tea)
print(with_tax(4.0))
print(with_tax(2.75) > 3)
