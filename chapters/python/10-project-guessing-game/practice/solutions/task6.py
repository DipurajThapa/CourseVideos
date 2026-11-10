# file: practice/solutions/task6.py
secret = 4
tries = 0
while tries < 4:
    guess = int(input("Price of a cake: "))
    tries += 1
    if guess == secret:
        print(f"Correct in {tries} tries!")
        break
    elif guess < secret:
        print("Higher!")
    else:
        print("Lower!")
