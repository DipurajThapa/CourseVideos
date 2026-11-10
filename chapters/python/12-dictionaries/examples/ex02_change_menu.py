# file: examples/ex02_change_menu.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
menu["scone"] = 2.75
print(menu)
menu["tea"] = 3.75
print(menu)
del menu["coffee"]
print(menu)
price = menu.pop("cake")
print(price, menu)
