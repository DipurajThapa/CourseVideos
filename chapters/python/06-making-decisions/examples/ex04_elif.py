# file: examples/ex04_elif.py
to_pay = float(input("Amount to pay: "))
if to_pay >= 50:
    print("Reward: a free cake")
elif to_pay >= 15:
    print("Reward: a free biscuit")
else:
    print("Reward: none this time")
