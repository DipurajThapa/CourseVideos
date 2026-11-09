# file: practice/solutions/task6.py
answer = input("Do you want a receipt? (yes/no) ").strip().lower()
if answer == "yes" or answer == "y":
    print("Printing your receipt.")
else:
    print("No receipt.")
