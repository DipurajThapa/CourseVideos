# file: examples/ex01_questions.py
print(f"{' BILL SPLITTER ':=^24}")
bill = float(input("Bill total: "))
tip_percent = int(input("Tip percent: "))
people = int(input("Number of people: "))
print(type(bill), type(tip_percent), type(people))
