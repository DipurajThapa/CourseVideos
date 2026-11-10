# file: practice/solutions/task8.py
prices = {"tea": 3.5, "cake": 4.25}
order = ["tea", "cake", "juice", "tea"]
total = 0
for item in order:
    if item in prices:
        total += prices[item]
    else:
        print(f"Skipped: {item}")
print(f"Total: {total:.2f}")
