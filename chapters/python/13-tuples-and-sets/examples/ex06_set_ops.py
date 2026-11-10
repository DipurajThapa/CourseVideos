# file: examples/ex06_set_ops.py
today = {"Omar", "Lina", "Sam"}
yesterday = {"Lina", "Ravi", "Sam"}
print(sorted(today | yesterday))
print(sorted(today & yesterday))
print(sorted(today - yesterday))
print(sorted(today ^ yesterday))
