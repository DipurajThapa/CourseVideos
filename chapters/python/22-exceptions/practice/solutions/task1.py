# file: practice/solutions/task1.py
entries = ["12", "twelve", "7"]
for entry in entries:
    try:
        cups = int(entry)
        print(f"Cups: {cups}")
    except ValueError:
        print(f"{entry!r} is not a number of cups")
