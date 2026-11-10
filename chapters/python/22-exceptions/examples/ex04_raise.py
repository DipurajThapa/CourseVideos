# file: examples/ex04_raise.py
def with_tax(price):
    if price < 0:
        raise ValueError(f"price cannot be negative: {price}")
    return round(price * 1.1, 2)


print(with_tax(3.5))
try:
    print(with_tax(-1))
except ValueError as error:
    print(f"Not saved: {error}")
