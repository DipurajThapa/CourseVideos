# file: practice/solutions/task5.py
from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool = False


def summary(tasks):
    done = len([task for task in tasks if task.done])
    return f"{len(tasks) - done} open, {done} done"


tasks = [Task("Open the cafe", True), Task("Restock milk"),
         Task("Call the supplier")]
print(summary(tasks))
print(summary([]))
