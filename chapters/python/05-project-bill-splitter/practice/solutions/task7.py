# file: practice/solutions/task7.py
bill = float(input("Bill total: "))
tip_percent = int(input("Tip percent: "))
people = int(input("Number of people: "))
bill_cents = round(bill * 100)
tip_cents = round(bill_cents * tip_percent / 100)
food_share = bill_cents // people
tip_share = tip_cents // people
extra_cents = bill_cents % people + tip_cents % people
print(f"{'Food each':<16}{food_share / 100:>8.2f}")
print(f"{'Tip each':<16}{tip_share / 100:>8.2f}")
print(f"{'Extra cents':<16}{extra_cents:>8}")
