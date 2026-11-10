# file: examples/ex02_global_read.py
tax_rate = 1.1

def with_tax(price):
    return round(price * tax_rate, 2)

print(with_tax(3.5))
tax_rate = 1.2
print(with_tax(3.5))
