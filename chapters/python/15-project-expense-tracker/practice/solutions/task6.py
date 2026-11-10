# file: practice/solutions/task6.py
days = [{"milk": 20.5, "beans": 30.0, "cups": 6.25}, {}]
for totals in days:
    smallest = "none"
    for category in totals:
        if smallest == "none" or totals[category] < totals[smallest]:
            smallest = category
    print("Smallest:", smallest)
