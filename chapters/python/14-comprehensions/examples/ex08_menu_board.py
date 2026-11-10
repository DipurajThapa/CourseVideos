# file: examples/ex08_menu_board.py
menu = [("Tea", 3.5, True),
        ("Coffee", 4.0, True),
        ("Carrot cake", 4.25, False),
        ("Scone", 2.75, False)]
board = {name: round(price * 1.1, 2) for name, price, is_vegan in menu}
vegan = [name for name, price, is_vegan in menu if is_vegan]
under_4 = [name for name, price in board.items() if price < 4]
for name, price in board.items():
    print(f"{name:<12}{price:>6.2f}")
print("Vegan:", vegan)
print("Under 4.00 with tax:", under_4)
