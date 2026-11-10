# file: examples/ex01_menu_item.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


tea = MenuItem("Tea", 3.5)
cake = MenuItem("Cake", 4.25)
print(tea.name, tea.price)
print(cake.name, cake.price)
