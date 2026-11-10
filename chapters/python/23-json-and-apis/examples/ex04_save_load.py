# file: examples/ex04_save_load.py
import json

quiz = {"title": "Menu quiz", "pass_mark": 2, "questions": [
    {"ask": "Price of tea?", "answer": "3.50"},
    {"ask": "Which cake has nuts?", "answer": "carrot"},
]}

with open("quiz.json", "w", encoding="utf-8") as file:
    json.dump(quiz, file, indent=2)

with open("quiz.json", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded["title"], "has", len(loaded["questions"]), "questions")
print(loaded["questions"][1]["ask"])
print(loaded == quiz)
