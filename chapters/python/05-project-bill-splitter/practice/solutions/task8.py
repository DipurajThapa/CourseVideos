# file: practice/solutions/task8.py
bill = float(input("Bill total: "))
tip_percent = int(input("Tip percent: "))
people = int(input("Number of people: "))
tip = bill * tip_percent / 100
share = (bill + tip) / people
print(f"Each pays: {share:.2f}")
