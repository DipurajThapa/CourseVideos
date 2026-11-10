# file: practice/solutions/task8.py
days = {"Monday": [3.5, 2.75, 3.5, 4.25], "Tuesday": [3.5, 5.0, 2.75]}

ai_total = 0
for day, amounts in days.items():
    ai_total += round(sum(amounts))

total = 0
for day, amounts in days.items():
    total += sum(amounts)

print("AI total:", ai_total)
print(f"Fixed total: {total:.2f}")
