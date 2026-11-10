# file: practice/solutions/task6.py
def menu_line(name, price):
    """Return one menu line: the name on the left, the price on the right."""
    return f"{name:<12}{price:>6.2f}"

menu = [("Tea", 3.5), ("Coffee", 4.0), ("Carrot cake", 4.25)]
for name, price in menu:
    print(menu_line(name, price))
