# file: examples/ai/debug/save_crash.py
from pathlib import Path
from tasks_core import TaskList, save_tasks

tasks = TaskList()
tasks.add("Restock milk")
save_tasks(Path("tasks.json"), tasks)
print("Saved")
