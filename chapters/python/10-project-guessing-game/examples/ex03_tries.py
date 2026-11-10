# file: examples/ex03_tries.py
secret = 7
tries = 0
won = False
while tries < 5:
    guess = int(input("Your guess: "))
    tries += 1
    if guess == secret:
        won = True
        break
    elif guess < secret:
        print(f"Too low! Tries left: {5 - tries}")
    else:
        print(f"Too high! Tries left: {5 - tries}")
print("Won:", won, "Tries:", tries)
