# file: examples/ex04_unique.py
visits = ["Omar", "Lina", "Omar", "Sam", "Omar"]
customers = set(visits)
print(len(visits))
print(len(customers))
print(sorted(customers))
print("Lina" in customers)
print("Ravi" in customers)
