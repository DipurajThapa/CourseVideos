# file: examples/ex02_assert_pass.py
def with_tax(price, rate=1.1):
    return round(price * rate, 2)

assert with_tax(3.5) == 3.85
assert with_tax(4.0) == 4.4
print("Report saved")
