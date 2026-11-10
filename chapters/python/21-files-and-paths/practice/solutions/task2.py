# file: practice/solutions/task2.py
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Closed at 18:00\n")

with open("log.txt", encoding="utf-8") as file:
    print(file.read().strip())
