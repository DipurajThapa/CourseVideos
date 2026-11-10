# file: examples/ai/write/write_compare.py
from tasks_core import Task


def asha_complete(tasks, number):
    if number < 1 or number > len(tasks):
        raise ValueError(f"there is no task {number}")
    tasks[number - 1].done = True


def ai_complete(tasks, number):
    tasks[number].done = True


pairs = [("Asha", asha_complete), ("AI", ai_complete)]
for who, complete in pairs:
    tasks = [Task("Open the cafe"), Task("Restock milk")]
    complete(tasks, 1)
    done = [task.title for task in tasks if task.done]
    print(who, "marked", done)
