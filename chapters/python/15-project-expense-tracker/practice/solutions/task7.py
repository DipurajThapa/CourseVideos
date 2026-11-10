# file: practice/solutions/task7.py
totals = {"milk": 20.5, "beans": 30.0, "cups": 6.25}
budget = {"milk": 15.0, "beans": 40.0, "cups": 5.0}
over = [category for category in sorted(totals) if totals[category] > budget[category]]
for category in sorted(totals):
    print(f"{category:<8}{totals[category]:>7.2f} of {budget[category]:.2f}")
print("Over budget:", over)
print("Categories over budget:", len(over))
