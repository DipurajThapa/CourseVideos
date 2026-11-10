# file: practice/solutions/task6.py
menu = ["tea", "coffee", "cake", "sandwich"]
wanted = input("What would you like? ").strip().lower()
if wanted in menu:
    print(f"Yes, we have {wanted}.")
else:
    print(f"Sorry, there is no {wanted} today.")
