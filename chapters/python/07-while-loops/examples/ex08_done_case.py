# file: examples/ex08_done_case.py
item = input("Item (or done): ")
while item != "done":
    print(f"Added: {item}")
    item = input("Item (or done): ")
print("Order closed.")
