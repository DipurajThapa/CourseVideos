# file: examples/ex04_loop_menu.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
for name in menu:
    print(name)
for name, price in menu.items():
    print(f"{name:<8}{price:>6.2f}")
print(list(menu.keys()))
print(list(menu.values()))
print(sum(menu.values()))
