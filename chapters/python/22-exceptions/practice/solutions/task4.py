# file: practice/solutions/task4.py
while True:
    answer = input("How many teas (1 to 10)? ")
    try:
        teas = int(answer)
    except ValueError:
        print("Please type a whole number, like 2.")
    else:
        if teas >= 1 and teas <= 10:
            break
        print("Please type a number from 1 to 10.")
print(f"Order: {teas} teas")
