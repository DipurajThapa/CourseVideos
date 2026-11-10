# file: practice/solutions/task3.py
allowed = {"milk", "beans", "cups", "repairs"}
category = input("Category: ").strip().lower()
if category in allowed:
    print(f"{category} is allowed.")
else:
    print(f"{category} is not a category.")
