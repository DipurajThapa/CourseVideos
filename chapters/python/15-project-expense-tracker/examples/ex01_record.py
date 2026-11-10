# file: examples/ex01_record.py
expenses = []
expenses.append(("milk", 12.5))
expenses.append(("beans", 30.0))
print(expenses)
print(len(expenses), "expenses")
category, amount = expenses[0]
print(category, amount)
