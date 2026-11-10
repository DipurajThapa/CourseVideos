# file: practice/solutions/task4.py
shopping = []
for number in range(1, 4):
    item = input(f"Item {number}: ")
    shopping.append(item.strip())
print("Your list:")
count = 1
for item in shopping:
    print(f"{count}. {item}")
    count += 1
print(f"{len(shopping)} items")
