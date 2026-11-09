# file: examples/ex03_cents.py
total = 43.07
people = 4
total_cents = round(total * 100)
share_cents = total_cents // people
extra_cents = total_cents % people
print("Total in cents:", total_cents)
print("Each pays (cents):", share_cents)
print("Extra cents:", extra_cents)
print("Check:", share_cents * people + extra_cents)
