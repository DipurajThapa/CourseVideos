# file: practice/solutions/task3.py
def percentage(points, total):
    """Return the score as a whole percentage."""
    return round(points / total * 100)


assert percentage(1, 4) == 25
assert percentage(4, 4) == 100
assert percentage(0, 4) == 0
print("All checks passed")
