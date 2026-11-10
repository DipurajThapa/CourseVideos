# file: examples/ex04_guesses.py
guesses = []
for turn in range(1, 4):
    guess = int(input(f"Guess {turn}: "))
    guesses.append(guess)
print(f"Your guesses: {guesses}")
for guess in guesses:
    print(f"- {guess}")
if 12 in guesses:
    print("You tried 12.")
print(20 in guesses)
