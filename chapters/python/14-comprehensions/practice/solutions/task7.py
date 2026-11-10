# file: practice/solutions/task7.py
menu = [("Tea", 3.5, True),
        ("Coffee", 4.0, True),
        ("Carrot cake", 4.25, False),
        ("Scone", 2.75, False)]
labels = {name: f"{price * 1.1:.2f}" + (" V" if is_vegan else "")
          for name, price, is_vegan in menu}
for name, label in labels.items():
    print(f"{name:<12}{label}")
print("Items:", len(labels))
