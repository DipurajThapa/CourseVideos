# file: practice/solutions/task8.py
from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool = False


def clear_done(tasks):
    """Return the open tasks, and how many done tasks were removed."""
    kept = [task for task in tasks if not task.done]
    return kept, len(tasks) - len(kept)


tasks = [Task("Open the cafe", True), Task("Restock milk"),
         Task("Wipe the tables", True)]
tasks, removed = clear_done(tasks)
print("Removed:", removed)
print([task.title for task in tasks])
tasks, removed = clear_done(tasks)
print("Removed:", removed)
assert clear_done([]) == ([], 0)
print("All checks passed")
