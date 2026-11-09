# file: practice/solutions/task6.py
bill = float(input("Bill total: "))
paid = float(input("Amount paid with tip: "))
tip = paid - bill
tip_percent = tip / bill * 100
print(f"Tip: {tip:.2f}")
print(f"That is a {tip_percent:.1f}% tip.")
