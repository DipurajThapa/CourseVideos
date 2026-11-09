# file: practice/solutions/task4.py
bill = float(input("Bill total: "))
people = int(input("Number of people: "))
bill_cents = round(bill * 100)
share_cents = bill_cents // people
extra_cents = bill_cents % people
print("-" * 24)
print(f"{'Bill':<16}{bill:>8.2f}")
print(f"{'Each pays':<16}{share_cents / 100:>8.2f}")
print(f"{'Extra cents':<16}{extra_cents:>8}")
