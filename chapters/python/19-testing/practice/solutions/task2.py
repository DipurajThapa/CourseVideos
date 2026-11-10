# file: practice/solutions/task2.py
def cups_left(cups, sold):
    return cups - sold

assert cups_left(20, 5) == 15, "20 cups, 5 sold should leave 15"
assert cups_left(10, 10) == 0, "selling every cup should leave 0"
print("Both checks passed")
