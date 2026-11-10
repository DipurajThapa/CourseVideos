# file: examples/ai_biggest_fixed.py
totals = {"milk": 20.5, "beans": 30.0, "cups": 6.25}
biggest = "none"
for category in totals:
    if biggest == "none" or totals[category] > totals[biggest]:
        biggest = category
print("Biggest:", biggest)
