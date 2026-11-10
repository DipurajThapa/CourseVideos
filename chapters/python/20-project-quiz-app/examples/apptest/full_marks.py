# file: examples/apptest/full_marks.py
"""The Corner Cafe staff quiz."""
from quiz_data import QUESTIONS
from quiz_logic import check_answer, result_line

points = 0
for item in QUESTIONS:
    given = input(item["question"] + " ")
    if check_answer(given, item["answer"]):
        print("Correct!")
        points += 1
    else:
        print("The answer is", item["answer"])
print(result_line(points, len(QUESTIONS)))
