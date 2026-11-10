# file: practice/solutions/task6.py
from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: int = 2


tasks = [Task("Call the supplier", 3), Task("Open the cafe", 1),
         Task("Restock milk", 2), Task("Bake scones", 1)]
for priority in (1, 2, 3):
    for task in tasks:
        if task.priority == priority:
            print(f"P{priority} {task.title}")
