# file: examples/err01_missing_file.py
print("Loading scores")
with open("score.csv", encoding="utf-8") as file:
    print(file.read())
