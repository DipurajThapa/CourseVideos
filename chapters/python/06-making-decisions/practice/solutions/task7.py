# file: practice/solutions/task7.py
total = float(input("Bill total: "))
people = int(input("Number of people: "))
if people <= 0:
    print("The number of people must be 1 or more.")
else:
    total_cents = round(total * 100)
    share = total_cents // people / 100
    extra_cents = total_cents % people
    print(f"Each pays: {share:.2f}")
    print(f"Extra cents: {extra_cents}")
