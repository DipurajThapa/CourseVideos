# file: practice/solutions/task6.py
cake = {"egg", "milk", "wheat"}
scone = {"milk", "wheat"}
print("Cake has egg:", "egg" in cake)
print("Scone has egg:", "egg" in scone)
print("In either:", sorted(cake | scone))
print("Only in cake:", sorted(cake - scone))
