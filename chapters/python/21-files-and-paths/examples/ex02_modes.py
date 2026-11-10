# file: examples/ex02_modes.py
with open("today.txt", "w", encoding="utf-8") as file:
    file.write("Asha 4\n")
    file.write("Omar 3\n")

with open("today.txt", "a", encoding="utf-8") as file:
    file.write("Lina 2\n")

with open("today.txt", encoding="utf-8") as file:
    print(file.read(), end="")
