# file: practice/solutions/task3.py
menu = {"tea": 3.5, "cake": 4.25, "sandwich": 6.0}
print("MENU")
for name, price in menu.items():
    print(f"{name:<10}{price:>6.2f}")
print(f"Items: {len(menu)}")
