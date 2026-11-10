# file: examples/ex03_assert_fail.py
def with_tax(price, rate=1.01):
    return round(price * rate, 2)

assert with_tax(3.5) == 3.85, "tea with tax should be 3.85"
print("Report saved")
