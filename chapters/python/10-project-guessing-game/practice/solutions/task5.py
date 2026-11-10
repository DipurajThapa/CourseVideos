# file: practice/solutions/task5.py
pin = "2468"
tries = 0
while tries < 3:
    typed = input("PIN: ").strip()
    tries += 1
    if typed == pin:
        print("Welcome, manager.")
        break
    else:
        print(f"Wrong PIN. Tries left: {3 - tries}")
