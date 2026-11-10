# file: practice/solutions/task3.py
class Basket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)


first = Basket()
second = Basket()
first.add("Scone")
first.add("Tea")
second.add("Juice")
print(len(first.items), len(second.items))
