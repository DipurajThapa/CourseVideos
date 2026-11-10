# file: practice/solutions/task2.py
class Customer:
    def __init__(self, name, visits):
        self.name = name
        self.visits = visits

    def greeting(self):
        return f"Welcome back, {self.name}! Visit number {self.visits + 1}."


print(Customer("Lina", 4).greeting())
