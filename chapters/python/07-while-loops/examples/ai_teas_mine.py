# file: examples/ai_teas_mine.py
teas = int(input("How many teas? (1 to 10) "))
while teas < 1 or teas > 10:
    print("Please type a number from 1 to 10.")
    teas = int(input("How many teas? (1 to 10) "))
print(f"Teas: {teas}")
