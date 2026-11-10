# file: examples/step4/save_check.py
from pathlib import Path
from tasks_core import TaskList, load_tasks, save_tasks

tasks = TaskList()
tasks.add("Open the cafe", 1)
tasks.add("Restock milk")
tasks.complete(1)
save_tasks(Path("tasks.json"), tasks)
print(Path("tasks.json").read_text(encoding="utf-8"))
again = load_tasks(Path("tasks.json"))
print(again.lines())
