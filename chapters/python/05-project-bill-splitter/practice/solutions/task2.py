# file: practice/solutions/task2.py
amount = float(input("Amount: "))
cents = round(amount * 100)
print("In cents:", cents)
print(f"Back to money: {cents / 100:.2f}")
