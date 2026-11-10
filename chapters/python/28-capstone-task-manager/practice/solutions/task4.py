# file: practice/solutions/task4.py
class TaskList:
    def __init__(self):
        self.titles = []

    def add(self, title):
        self.titles.append(title)

    def remove(self, number):
        if number < 1 or number > len(self.titles):
            raise ValueError(f"there is no task {number}")
        return self.titles.pop(number - 1)


tasks = TaskList()
for title in ["Open the cafe", "Restock milk", "Call the supplier"]:
    tasks.add(title)
print("Removed:", tasks.remove(2))
print(tasks.titles)
try:
    tasks.remove(5)
except ValueError as error:
    print("Refused:", error)
