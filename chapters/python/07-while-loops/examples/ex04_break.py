# file: examples/ex04_break.py
while True:
    item = input("Item (or done): ").strip().lower()
    if item == "done":
        break
    print(f"Added: {item}")
print("Order closed.")
