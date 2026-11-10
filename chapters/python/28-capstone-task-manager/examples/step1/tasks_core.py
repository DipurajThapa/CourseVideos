# file: examples/step1/tasks_core.py
"""Empty rules: the tests come first."""
from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: int = 2
    done: bool = False


class TaskList:
    def __init__(self, tasks=None):
        self.tasks = []

    def add(self, title, priority=2):
        pass

    def complete(self, number):
        pass

    def open_tasks(self):
        return []

    def lines(self):
        return []


def save_tasks(path, task_list):
    pass


def load_tasks(path):
    return TaskList()
