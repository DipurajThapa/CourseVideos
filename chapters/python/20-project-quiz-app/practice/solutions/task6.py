# file: practice/solutions/task6.py
def change_due(paid, price):
    """Return the change, rounded to cents."""
    return round(paid - price, 2)


assert change_due(5, 3.5) == 1.5
assert change_due(10, 2.75) == 7.25
assert change_due(3.5, 3.5) == 0
print("3 checks passed")
