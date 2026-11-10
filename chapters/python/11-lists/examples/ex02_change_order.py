# file: examples/ex02_change_order.py
order = ["tea", "cake"]
order.append("sandwich")
print(order)
order.insert(0, "juice")
print(order)
order[1] = "green tea"
print(order)
order.remove("cake")
print(order)
last = order.pop()
print(last, order)
