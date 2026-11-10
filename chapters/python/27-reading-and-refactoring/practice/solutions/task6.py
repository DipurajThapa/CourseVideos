# file: practice/solutions/task6.py
import difflib

old = ["price = 3.5", "count = 2", "print(price * count)"]
new = ["TEA_PRICE = 3.5", "count = 2", "print(TEA_PRICE * count)"]
for line in difflib.unified_diff(old, new, "old", "new", lineterm="", n=0):
    print(line)
