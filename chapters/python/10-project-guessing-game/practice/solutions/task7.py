# file: practice/solutions/task7.py
secret = 13
tries = 0
points = 0
while tries < 5:
    guess = int(input("Your guess: "))
    tries += 1
    if guess == secret:
        points = 6 - tries
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
print(f"Guesses: {tries}. Points: {points}")
