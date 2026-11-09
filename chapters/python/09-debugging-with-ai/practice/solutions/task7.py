# file: practice/solutions/task7.py
print("Weekly tea report")
days = int(input("How many days? "))
cups = 0
for day in range(1, days + 1):
    sold = int(input(f"Cups on day {day}: "))
    cups = cups + sold
print(f"Cups this week: {cups}")
print(f"Tea money: {cups * 3.5:.2f}")
