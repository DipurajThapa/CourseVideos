# file: examples/ex07_checkout.py
name = input("Name: ")
teas = int(input("How many teas? "))
member = input("Member? ").strip().lower()

bill = teas * 3.5
if member == "yes":
    discount = bill * 0.1
else:
    discount = 0
to_pay = bill - discount

print(f"Bill for {name}: {bill:.2f}")
print(f"Discount: {discount:.2f}")
print(f"To pay: {to_pay:.2f}")
if to_pay >= 15:
    print("Reward: a free biscuit")
else:
    print("Thank you, see you soon!")
