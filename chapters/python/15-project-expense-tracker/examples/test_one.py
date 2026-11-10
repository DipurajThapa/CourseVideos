# file: examples/test_one.py
allowed = {"milk", "beans", "cups", "repairs"}
expenses = []
while True:
    category = input("Category (or done): ").strip().lower()
    if category == "done":
        break
    elif category not in allowed:
        print("Use milk, beans, cups or repairs.")
    else:
        amount_text = input("Amount: ").strip()
        if amount_text.replace(".", "", 1).isdigit():
            expenses.append((category, float(amount_text)))
        else:
            print("Type an amount like 12.50.")
totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount
biggest = "none"
for category in sorted(totals):
    print(f"{category:<8}{totals[category]:>7.2f}")
    if biggest == "none" or totals[category] > totals[biggest]:
        biggest = category
print(f"Expenses: {len(expenses)}  Total: {sum(totals.values()):.2f}")
print("Biggest:", biggest)
