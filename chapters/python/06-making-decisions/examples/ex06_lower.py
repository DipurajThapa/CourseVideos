# file: examples/ex06_lower.py
answer = input("Are you a member? (yes/no) ")
if answer.strip().lower() == "yes":
    print("Member discount: 10%")
else:
    print("No discount")
