# file: practice/solutions/task8.py
order = float(input("Order total: "))
if order >= 30:
    fee = 0
else:
    fee = 2.5
print(f"Delivery fee: {fee:.2f}")
print(f"To pay: {order + fee:.2f}")
