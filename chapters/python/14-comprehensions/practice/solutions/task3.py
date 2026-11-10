# file: practice/solutions/task3.py
items = ["Tea", "Coffee", "Scone", "Carrot cake"]
short = [item for item in items if len(item) <= 5]
print(short)
print(len(short), "of", len(items))
