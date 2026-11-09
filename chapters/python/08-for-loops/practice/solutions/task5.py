# file: practice/solutions/task5.py
total = 0
for shift in range(1, 5):
    tips = float(input(f"Tips for shift {shift}: "))
    total += tips
print(f"Total tips: {total:.2f}")
