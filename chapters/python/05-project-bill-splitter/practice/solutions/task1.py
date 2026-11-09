# file: practice/solutions/task1.py
bill = float(input("Bill total: "))
tip_percent = int(input("Tip percent: "))
tip = bill * tip_percent / 100
print(f"Tip: {tip:.2f}")
