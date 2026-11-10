# file: examples/ex05_bare_except.py
answers = ["4", "four"]
for answer in answers:
    try:
        score = int(anser)
        print(f"Saved score: {score}")
    except:
        print("Please type a whole number.")
