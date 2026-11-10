# file: examples/ex02_unpacking.py
hours = (8, 18)
opens, closes = hours
print(f"Open {opens}:00 to {closes}:00")
name, price = ("Scone", 2.75)
print(f"{name}: {price:.2f}")
first = "Omar"
second = "Lina"
first, second = second, first
print(first, second)
