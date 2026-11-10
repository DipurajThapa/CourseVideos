# file: examples/err04_shared_list.py
class Order:
    items = []

    def __init__(self, customer):
        self.customer = customer

    def add(self, item):
        self.items.append(item)


lina = Order("Lina")
omar = Order("Omar")
lina.add("Tea")
print(omar.customer, omar.items)
