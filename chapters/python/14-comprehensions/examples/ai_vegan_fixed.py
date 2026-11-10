# file: examples/ai_vegan_fixed.py
menu = [("Tea", 3.5, True),
        ("Coffee", 4.0, True),
        ("Carrot cake", 4.25, False),
        ("Scone", 2.75, False)]
taxed = [round(price * 1.1, 2) for name, price, vegan in menu if vegan]
print(taxed)
