# file: project/tasks_core.py
"""Tasks, a task list, and saving them as JSON."""
import json
from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: int = 2
    done: bool = False

    def to_dict(self):
        """Return the task as a dict that JSON can save."""
        return {"title": self.title,
                "priority": self.priority,
                "done": self.done}


class TaskList:
    """Tasks in the order added, numbered from 1."""

    def __init__(self, tasks=None):
        self.tasks = list(tasks or [])

    def add(self, title, priority=2):
        title = title.strip()
        if not title:
            raise ValueError("a task needs a title")
        if priority not in (1, 2, 3):
            raise ValueError("priority must be 1, 2 or 3")
        self.tasks.append(Task(title, priority))

    def complete(self, number):
        if number < 1 or number > len(self.tasks):
            raise ValueError(f"there is no task {number}")
        self.tasks[number - 1].done = True

    def open_tasks(self):
        return [t for t in self.tasks if not t.done]

    def lines(self):
        result = []
        for number in range(1, len(self.tasks) + 1):
            task = self.tasks[number - 1]
            mark = "x" if task.done else " "
            line = f"{number}. [{mark}] {task.title}"
            result.append(f"{line} (P{task.priority})")
        return result


def save_tasks(path, task_list):
    rows = [task.to_dict() for task in task_list.tasks]
    text = json.dumps(rows, indent=2)
    path.write_text(text, encoding="utf-8")


def load_tasks(path):
    """Return the saved TaskList, or raise ValueError."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return TaskList()
    if not text.strip():
        return TaskList()
    try:
        rows = json.loads(text)
    except json.JSONDecodeError as error:
        name = path.name
        raise ValueError(f"{name} is not valid JSON: {error.msg}")
    task_list = TaskList()
    for row in rows:
        task = Task(row["title"], row["priority"],
                    row["done"])
        task_list.tasks.append(task)
    return task_list
