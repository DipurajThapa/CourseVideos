# file: project/task_app.py
"""Corner Cafe tasks: add, done, list or quit."""
from pathlib import Path
from tasks_core import load_tasks, save_tasks

PATH = Path("tasks.json")


def run(tasks):
    """Ask for commands until the user types quit."""
    while True:
        command = input("Command: ").strip().lower()
        if command == "quit":
            return
        try:
            if command == "add":
                title = input("Title: ")
                priority = int(input("Priority 1-3: "))
                tasks.add(title, priority)
            elif command == "done":
                tasks.complete(int(input("Number: ")))
            elif command == "list":
                for line in tasks.lines():
                    print(line)
            else:
                print("Commands: add, done, list, quit")
        except ValueError as error:
            print("Not done:", error)


try:
    tasks = load_tasks(PATH)
except ValueError as error:
    print("Tasks not loaded:", error)
else:
    print(len(tasks.open_tasks()), "open tasks")
    run(tasks)
    save_tasks(PATH, tasks)
    print("Saved", PATH.name)
