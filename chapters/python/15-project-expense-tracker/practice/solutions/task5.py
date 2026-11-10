# file: practice/solutions/task5.py
while True:
    amount_text = input("Amount: ").strip()
    if amount_text.replace(".", "", 1).isdigit():
        break
    print("Type an amount like 12.50.")
amount = float(amount_text)
print(f"Saved: {amount:.2f}")
