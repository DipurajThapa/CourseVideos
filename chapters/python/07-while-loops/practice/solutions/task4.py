# file: practice/solutions/task4.py
age = int(input("Your age (0 to 120): "))
while age < 0 or age > 120:
    print("Please type an age from 0 to 120.")
    age = int(input("Your age (0 to 120): "))
print(f"Age saved: {age}")
