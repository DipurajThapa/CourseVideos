# file: practice/solutions/task3.py
prices = ["3.50", "4.20", "free"]
total = 0.0
try:
    for price in prices:
        total += float(price)
except ValueError:
    print(f"Stopped at a bad price: {price!r}")
finally:
    print(f"Total so far: {total:.2f}")
