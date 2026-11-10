# file: examples/ex03_specials.py
specials = [("Tea", 3.5),
            ("Scone", 2.75),
            ("Cake", 4.25)]
total = 0
for name, price in specials:
    print(f"{name:<8}{price:>6.2f}")
    total += price
print(f"{'Total':<8}{total:>6.2f}")
print(specials[1][0])
