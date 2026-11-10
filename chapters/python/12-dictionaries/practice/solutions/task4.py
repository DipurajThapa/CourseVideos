# file: practice/solutions/task4.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
item = input("Which item? ").strip().lower()
if item in menu:
    print(f"{item} costs {menu[item]:.2f}")
else:
    print(f"Sorry, {item} is not on the menu.")
