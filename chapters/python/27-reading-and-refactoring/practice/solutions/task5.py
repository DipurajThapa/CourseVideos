# file: practice/solutions/task5.py
def receipt(customer, items):
    print(f"Receipt for {customer}")
    total = 0
    for name, price in items:
        print(f"  {name:<6}{price:>6.2f}")
        total = total + price
    print(f"  {'Total':<6}{total:>6.2f}")


receipt("Lina", [("Tea", 3.5), ("Cake", 4.25)])
receipt("Omar", [("Latte", 3.85)])
