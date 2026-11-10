# file: practice/solutions/task4.py
specials = [("Soup", 5.5), ("Salad", 7.0), ("Toast", 3.25), ("Juice", 3.0)]
total = 0
for name, price in specials:
    print(f"{name:<8}{price:>6.2f}")
    total += price
print(f"{'Items':<8}{len(specials):>6}")
print(f"{'Total':<8}{total:>6.2f}")
