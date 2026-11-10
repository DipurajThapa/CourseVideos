# file: practice/solutions/task7.py
menu = {"tea": 3.5, "cake": 4.25, "sandwich": 6.0}
order = {}
while True:
    item = input("Item (or done): ").strip().lower()
    if item == "done":
        break
    if item not in menu:
        print("Not on the menu.")
    else:
        count = int(input("How many? "))
        order[item] = order.get(item, 0) + count
total = 0
for item, count in order.items():
    total += count * menu[item]
    print(f"{item}: {count}")
print(f"Total: {total:.2f}")
