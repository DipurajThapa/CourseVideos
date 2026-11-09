# file: examples/ex06_order_loop.py
total = 0
items = 0
while True:
    item = input("Item (tea, cake or done): ").strip().lower()
    if item == "done":
        break
    if item == "tea":
        total += 3.5
        items += 1
    elif item == "cake":
        total += 4.0
        items += 1
    else:
        print("Sorry, we only have tea and cake.")
print(f"Items: {items}")
print(f"Total: {total:.2f}")
