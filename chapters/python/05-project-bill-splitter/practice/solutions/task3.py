# file: practice/solutions/task3.py
sweets = int(input("How many sweets? "))
children = int(input("How many children? "))
each = sweets // children
left = sweets % children
print(f"Each child gets {each} sweets.")
print(f"{left} sweets are left over.")
