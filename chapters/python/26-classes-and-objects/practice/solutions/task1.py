# file: practice/solutions/task1.py
class Customer:
    def __init__(self, name, visits):
        self.name = name
        self.visits = visits


lina = Customer("Lina", 4)
omar = Customer("Omar", 9)
print(lina.name, lina.visits)
print(omar.name, omar.visits)
