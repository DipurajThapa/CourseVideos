# file: examples/ex07_order_by_name.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25, "sandwich": 6.0}
order = {}
while True:
    item = input("Item (or done): ").strip().lower()
    if item == "done":
        break
    if item in menu:
        order[item] = order.get(item, 0) + 1
    else:
        print(f"Sorry, no {item} today.")
total = 0
for item, count in order.items():
    cost = count * menu[item]
    total += cost
    print(f"{count} x {item:<10}{cost:>6.2f}")
print(f"{'Total':<14}{total:>6.2f}")
