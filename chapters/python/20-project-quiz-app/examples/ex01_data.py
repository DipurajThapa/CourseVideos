# file: examples/ex01_data.py
from quiz_data import QUESTIONS

print(len(QUESTIONS), "questions")
first = QUESTIONS[0]
print(first["question"])
print(first["answer"])
