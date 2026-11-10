# file: practice/solutions/task3.py
count = 0
with open("menu.txt", encoding="utf-8") as file:
    for line in file:
        count += 1
        print(f"{count}. {line.strip()}")
print(f"{count} items on the menu")
