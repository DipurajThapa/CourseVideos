# file: examples/ex02_one_guess.py
secret = 7
guess = int(input("Your guess: "))
if guess == secret:
    print("Correct!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")
