# file: practice/solutions/task4.py
while True:
    answer = input("Pick a table, 1 to 10: ").strip()
    if not answer.isdigit():
        print("Please type a whole number.")
    elif int(answer) < 1 or int(answer) > 10:
        print("We have tables 1 to 10.")
    else:
        break
print("Table", answer, "is yours.")
