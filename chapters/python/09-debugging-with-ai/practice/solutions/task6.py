# file: practice/solutions/task6.py
count = int(input("How many cakes were rated? "))
points = 0
for cake in range(1, count + 1):
    points = points + int(input(f"Points for cake {cake}: "))
if count > 0:
    print(f"Average points: {points / count:.1f}")
else:
    print("No ratings yet.")
