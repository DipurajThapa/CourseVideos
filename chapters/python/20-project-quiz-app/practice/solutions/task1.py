# file: practice/solutions/task1.py
questions = [
    {"question": "Price of a tea?", "answer": "3.50"},
    {"question": "Which cake has nuts?", "answer": "carrot"},
]
questions.append({"question": "Is the bread fresh today?", "answer": "yes"})
print(len(questions), "questions")
print("Last:", questions[-1]["question"])
