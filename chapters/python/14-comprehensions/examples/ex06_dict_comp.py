# file: examples/ex06_dict_comp.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25, "scone": 2.75}
with_tax = {name: round(price * 1.1, 2) for name, price in menu.items()}
print(with_tax)
print(with_tax["cake"])
print(menu["cake"])
