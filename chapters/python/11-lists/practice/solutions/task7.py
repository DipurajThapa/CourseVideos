# file: practice/solutions/task7.py
secret = 9
guesses = []
while len(guesses) < 4:
    guess = int(input("Your guess: "))
    if guess in guesses:
        print(f"You already guessed {guess}.")
    elif guess == secret:
        guesses.append(guess)
        print("Correct!")
        break
    else:
        guesses.append(guess)
        print("Not this one.")
print(f"Your guesses: {guesses}")
