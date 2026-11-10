# file: examples/test_edges.py
import random
print("BISCUIT JAR: guess 1 to 20. Five tries!")
secret = 20  # fixed for this test
tries = 0
while tries < 5:
    answer = input("Your guess: ").strip()
    if not answer.isdigit():
        print("Please type a whole number, like 12.")
    elif int(answer) < 1 or int(answer) > 20:
        print("The jar holds 1 to 20 biscuits.")
    else:
        guess = int(answer)
        tries += 1
        if guess == secret:
            print(f"Correct! Free tea! Tries: {tries}")
            break
        elif guess < secret:
            print(f"Too low! Tries left: {5 - tries}")
        else:
            print(f"Too high! Tries left: {5 - tries}")
if guess != secret:
    print(f"Out of tries. It was {secret}.")
