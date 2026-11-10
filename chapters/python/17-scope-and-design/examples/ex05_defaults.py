# file: examples/ex05_defaults.py
def with_tax(price, rate=1.1):
    return round(price * rate, 2)

print(with_tax(3.5))
print(with_tax(3.5, 1.2))
print(with_tax(4.0))
