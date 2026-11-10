# file: examples/ai_no_strip.py
import random

print(f"{' BISCUIT JAR GAME ':=^30}")
print("Guess the biscuits in the jar: 1 to 20.")
print("You have 5 tries. Win a free tea!")
secret = 7  # fixed for this test
tries = 0
won = False
while tries < 5:
    answer = input("Your guess: ")
    if not answer.isdigit():
        print("Please type a whole number, like 12.")
    elif int(answer) < 1 or int(answer) > 20:
        print("The jar holds 1 to 20 biscuits.")
    else:
        guess = int(answer)
        tries += 1
        if guess == secret:
            won = True
            break
        elif guess < secret:
            print(f"Too low! Tries left: {5 - tries}")
        else:
            print(f"Too high! Tries left: {5 - tries}")
if won:
    print(f"Correct! It was {secret}. Guesses used: {tries}. Free tea!")
else:
    print(f"Out of tries. It was {secret}.")
