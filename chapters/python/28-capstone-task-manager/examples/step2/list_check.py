# file: examples/step2/list_check.py
from tasks_core import TaskList

tasks = TaskList()
tasks.add("Open the cafe", 1)
tasks.add("  Restock milk  ")
tasks.add("Call the supplier", 3)
for line in tasks.lines():
    print(line)
try:
    tasks.add("   ")
except ValueError as error:
    print("Refused:", error)
