# file: practice/solutions/task1.py
from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: int = 2
    done: bool = False


first = Task("Open the cafe", 1)
second = Task("Wipe the tables")
print(first)
print(second)
print(first == Task("Open the cafe", 1))
