# file: practice/solutions/task4.py
cups = 0
for order in range(1, 4):
    in_order = int(input(f"Cups in order {order}: "))
    cups = cups + in_order
print(f"Cups sold: {cups}")
