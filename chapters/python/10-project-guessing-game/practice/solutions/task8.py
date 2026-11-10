# file: practice/solutions/task8.py
secret = 7
tries = 0
while tries < 3:
    guess = int(input("Your guess: "))
    tries += 1
    if guess == secret:
        print("Correct!")
        break
    else:
        print(f"Wrong. Tries left: {3 - tries}")
