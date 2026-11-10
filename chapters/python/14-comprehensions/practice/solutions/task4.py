# file: practice/solutions/task4.py
prices = [3.5, 4.0, 4.25, 2.75]
labels = ["sale" if price >= 4 else "full price" for price in prices]
print(labels)
