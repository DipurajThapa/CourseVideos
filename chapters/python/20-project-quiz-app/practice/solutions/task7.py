# file: practice/solutions/task7.py
questions = [
    {"topic": "prices", "answer": "3.50"},
    {"topic": "allergens", "answer": "carrot"},
    {"topic": "prices", "answer": "2.75"},
    {"topic": "allergens", "answer": "walnut"},
]
given = ["3.50", "lemon", "2.75", " Walnut"]
points = {}
for i in range(len(questions)):
    topic = questions[i]["topic"]
    right = given[i].strip().lower() == questions[i]["answer"]
    points[topic] = points.get(topic, 0) + (1 if right else 0)
for topic in sorted(points):
    print(f"{topic}: {points[topic]}/2")
