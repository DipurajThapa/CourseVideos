# file: examples/test_one_person.py
print(f"{' BILL SPLITTER ':=^24}")
bill = float(input("Bill total: "))
tip_percent = int(input("Tip percent: "))
people = int(input("Number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
total_cents = round(total * 100)
share_cents = total_cents // people
extra_cents = total_cents % people
share = share_cents / 100

tip_label = f"Tip {tip_percent}%"
line = "-" * 24
print(line)
print(f"{'Bill':<16}{bill:>8.2f}")
print(f"{tip_label:<16}{tip:>8.2f}")
print(f"{'Total':<16}{total:>8.2f}")
print(line)
print(f"{'Each pays':<16}{share:>8.2f}")
print(f"{'Extra cents':<16}{extra_cents:>8}")
