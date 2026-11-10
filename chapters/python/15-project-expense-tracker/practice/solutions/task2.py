# file: practice/solutions/task2.py
amount_text = input("Amount: ").strip()
print("Valid amount:", amount_text.replace(".", "", 1).isdigit())
