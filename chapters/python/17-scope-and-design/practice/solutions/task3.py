# file: practice/solutions/task3.py
rate = 1.1

def with_tax(price):
    return round(price * rate, 2)

print(with_tax(10.0))
rate = 1.2
print(with_tax(10.0))
print(round(10.0 * rate, 2))
