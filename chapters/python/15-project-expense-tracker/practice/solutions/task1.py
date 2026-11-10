# file: practice/solutions/task1.py
expenses = []
expenses.append(("cups", 6.25))
expenses.append(("repairs", 45.0))
print(expenses)
category, amount = expenses[1]
print(f"Second expense: {category} {amount:.2f}")
