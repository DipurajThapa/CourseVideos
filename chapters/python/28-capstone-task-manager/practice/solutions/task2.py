# file: practice/solutions/task2.py
import json

tasks = [
    {"title": "Restock milk", "priority": 2, "done": False},
    {"title": "Call the supplier", "priority": 3, "done": True},
]
text = json.dumps(tasks)
print(text)
again = json.loads(text)
for task in again:
    print(task["title"], "done:", task["done"])
