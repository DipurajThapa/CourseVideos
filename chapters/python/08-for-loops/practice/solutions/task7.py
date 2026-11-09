# file: practice/solutions/task7.py
cake_price = 4.0
print("Cakes   Price")
for cakes in range(1, 9):
    cost = cakes * cake_price
    if cakes >= 5:
        cost = cost * 0.9
    print(f"{cakes:>5} {cost:>7.2f}")
