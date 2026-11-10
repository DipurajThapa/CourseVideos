# file: examples/err04_shared_list.py
def new_order(item, order=[]):
    order.append(item)
    return order

lina = new_order("Tea")
omar = new_order("Cake")
print("Lina:", lina)
print("Omar:", omar)
