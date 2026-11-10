# file: examples/ex03_lookups.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
print("tea" in menu)
print("juice" in menu)
print(3.5 in menu)
print(menu.get("cake"))
print(menu.get("juice"))
print(menu.get("juice", 0))
