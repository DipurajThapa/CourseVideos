# file: examples/ai_fix_case_11_5.py
tries = 1
teas = int(input("How many teas? (1 to 10) "))
while (teas < 1 or teas > 10) and tries < 3:
    print("Please type a number from 1 to 10.")
    teas = int(input("How many teas? (1 to 10) "))
    tries += 1
if teas < 1 or teas > 10:
    print("Too many tries. Using 1 tea.")
    teas = 1
print(f"Teas: {teas}")
