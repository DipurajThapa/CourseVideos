# file: practice/solutions/task2.py
secret = 9
guess = int(input("Guess the price: "))
if guess == secret:
    print("Correct!")
elif guess < secret:
    print("Higher!")
else:
    print("Lower!")
