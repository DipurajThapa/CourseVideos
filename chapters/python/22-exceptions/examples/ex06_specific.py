# file: examples/ex06_specific.py
answers = ["4", "four"]
for answer in answers:
    try:
        score = int(anser)
        print(f"Saved score: {score}")
    except ValueError:
        print("Please type a whole number.")
