# file: practice/solutions/task6.py
item = input("Item: ")
price = float(input("Price of one: "))
count = int(input("How many: "))
total = price * count
label = f"{item.strip().title()} x {count}"
print(f"{label:<16}{total:>8.2f}")
