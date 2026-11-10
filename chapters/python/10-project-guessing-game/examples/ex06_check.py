# file: examples/ex06_check.py
answer = input("Your guess: ").strip()
if not answer.isdigit():
    print("Please type a whole number, like 12.")
elif int(answer) < 1 or int(answer) > 20:
    print("The jar holds 1 to 20 biscuits.")
else:
    guess = int(answer)
    print("A fair guess:", guess)
