# file: examples/ex04_filter.py
menu = [("Tea", 3.5, True),
        ("Coffee", 4.0, True),
        ("Carrot cake", 4.25, False),
        ("Scone", 2.75, False)]
vegan = [name for name, price, is_vegan in menu if is_vegan]
cheap = [name for name, price, is_vegan in menu if price < 4]
print(vegan)
print(cheap)
