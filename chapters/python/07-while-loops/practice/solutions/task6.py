# file: practice/solutions/task6.py
total = 0
count = 0
score = int(input("Score (-1 to finish): "))
while score != -1:
    total += score
    count += 1
    score = int(input("Score (-1 to finish): "))
if count > 0:
    print(f"Scores: {count}")
    print(f"Average: {total / count:.1f}")
else:
    print("No scores entered.")
