# file: practice/solutions/task5.py
goal = 100
weekly = 15
saved = 0
weeks = 0
while saved < goal:
    saved += weekly
    weeks += 1
print(f"Weeks: {weeks}")
print(f"Saved: {saved}")
