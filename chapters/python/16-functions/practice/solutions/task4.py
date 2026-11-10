# file: practice/solutions/task4.py
def change(paid, cost):
    """Return the change to give back, rounded to cents."""
    return round(paid - cost, 2)

print(change(10.0, 7.25))
print(change(20.0, 11.28))
print(change(5.0, 5.0))
