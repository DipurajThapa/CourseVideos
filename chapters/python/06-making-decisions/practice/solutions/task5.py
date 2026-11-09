# file: practice/solutions/task5.py
score = int(input("Quiz score (0 to 100): "))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "Try again"
print(f"Grade: {grade}")
