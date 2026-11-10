# file: examples/step3/done_check.py
from tasks_core import TaskList

tasks = TaskList()
tasks.add("Open the cafe", 1)
tasks.add("Restock milk")
tasks.add("Call the supplier", 3)
tasks.complete(1)
for line in tasks.lines():
    print(line)
print(len(tasks.open_tasks()), "open tasks")
try:
    tasks.complete(4)
except ValueError as error:
    print("Refused:", error)
