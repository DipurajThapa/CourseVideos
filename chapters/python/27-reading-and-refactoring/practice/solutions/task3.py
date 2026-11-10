# file: practice/solutions/task3.py
def d(t, m):
    if m and t > 20:
        return t - 2
    return t


assert d(25, True) == 23
assert d(25, False) == 25
assert d(20, True) == 20
assert d(10, True) == 10
print("All checks passed")
