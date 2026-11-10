# file: examples/err02_w_erases.py
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("Closed at 18:00\n")

with open("log.txt", encoding="utf-8") as file:
    print(file.read(), end="")
