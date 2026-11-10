# file: examples/ex03_own_data.py
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add(self, item):
        self.items.append(item)


lina = Order("Lina")
omar = Order("Omar")
lina.add("Tea")
lina.add("Cake")
omar.add("Juice")
print(lina.customer, lina.items)
print(omar.customer, omar.items)
