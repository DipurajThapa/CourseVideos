# file: practice/solutions/task4.py
amounts = ["3.50", "four", "2.75", "", "5.00"]
total, bad = 0, 0
for text in amounts:
    try:
        total += float(text)
    except ValueError:
        bad += 1
print(f"Total: {total:.2f}")
print("Bad rows:", bad)
