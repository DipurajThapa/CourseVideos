# file: practice/solutions/task5.py
monday = {"Omar", "Lina", "Sam", "Zoe"}
tuesday = {"Lina", "Ravi", "Zoe"}
print("Both days:", sorted(monday & tuesday))
print("Only Monday:", sorted(monday - tuesday))
print("Everyone:", len(monday | tuesday))
