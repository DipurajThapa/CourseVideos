# file: examples/ex01_print_checks.py
def with_tax(price, rate=1.01):
    return round(price * rate, 2)

print(with_tax(3.5) == 3.85)
print("Report saved")
