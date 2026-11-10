# file: practice/solutions/task2.py
def tea_price(size="small"):
    if size == "large":
        return 3.5
    return 3.0

print(tea_price())
print(tea_price("large"))
print(tea_price(size="small"))
