# file: examples/ex01_try_except.py
answers = ["4", "four", " 3 "]
for answer in answers:
    try:
        score = int(answer)
        print(f"Saved score: {score}")
    except ValueError:
        print(f"Not a whole number: {answer!r}")
