# file: examples/ex02_categories.py
allowed = {"milk", "beans", "cups", "repairs"}
count = 0
while True:
    category = input("Category (or done): ").strip().lower()
    if category == "done":
        break
    elif category not in allowed:
        print("Use milk, beans, cups or repairs.")
    else:
        count += 1
        print("OK:", category)
print("Categories entered:", count)
