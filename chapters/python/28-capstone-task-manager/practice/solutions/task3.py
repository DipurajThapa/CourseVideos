# file: practice/solutions/task3.py
def task_line(number, title, done):
    mark = "x" if done else " "
    return f"{number}. [{mark}] {title}"


print(task_line(1, "Open the cafe", True))
print(task_line(2, "Restock milk", False))
