# file: practice/solutions/task6.py
sentence = "Two teas and one cake for table four"
spaces = 0
for character in sentence:
    if character == " ":
        spaces += 1
print(f"Words: {spaces + 1}")
