# file: examples/ai_biggest_regression.py
days = [{"milk": 20.5, "beans": 30.0, "cups": 6.25},
        {"cups": 9.0},
        {"beans": 5.0, "repairs": 45.0},
        {}]
for totals in days:
    biggest = "none"
    for category in totals:
        if biggest == "none" or totals[category] > totals[biggest]:
            biggest = category
    print("Biggest:", biggest)
