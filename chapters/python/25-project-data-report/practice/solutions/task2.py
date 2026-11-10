# file: practice/solutions/task2.py
for text in ["2.75", "two", ""]:
    try:
        amount = float(text)
    except ValueError:
        print(f"{text!r} is not a number")
    else:
        print(f"{text!r} is {amount}")
