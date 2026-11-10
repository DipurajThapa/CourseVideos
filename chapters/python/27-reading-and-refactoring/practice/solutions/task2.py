# file: practice/solutions/task2.py
def line_total(price, count):
    return price * count


def line_text(name, price, count):
    return f"{name} x{count}: {line_total(price, count):.2f}"


print(line_text("Tea", 3.5, 2))
print(line_text("Cake", 4.25, 1))
