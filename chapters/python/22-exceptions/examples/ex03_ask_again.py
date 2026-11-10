# file: examples/ex03_ask_again.py
while True:
    answer = input("Score (0 to 4): ")
    try:
        score = int(answer)
    except ValueError:
        print("Please type a whole number, like 3.")
    else:
        if score >= 0 and score <= 4:
            break
        print("Please type a number from 0 to 4.")
print(f"Saved: {score}")
