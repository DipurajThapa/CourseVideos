# file: practice/solutions/task7.py
total = 0
items = 0
while True:
    item = input("Item (tea, cake, juice, help or done): ").strip().lower()
    if item == "done":
        break
    if item == "help":
        print("Menu: tea 3.50, cake 4.00, juice 2.75")
    elif item == "tea":
        total += 3.5
        items += 1
    elif item == "cake":
        total += 4.0
        items += 1
    elif item == "juice":
        total += 2.75
        items += 1
    else:
        print("Sorry, that is not on the menu. Type help.")
print(f"Items: {items}")
print(f"Total: {total:.2f}")
