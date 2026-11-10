# file: examples/ex07_loyalty.py
today = ["Omar", "Lina", "Omar", "Sam", "Omar", "Lina", "Omar"]
yesterday = {"Lina", "Ravi", "Sam"}
opens, closes = (8, 18)
customers = set(today)
print(f"Open {opens}:00 to {closes}:00")
print(f"Visits today: {len(today)}")
print(f"Different customers: {len(customers)}")
print("Both days:", sorted(customers & yesterday))
print("New today:", sorted(customers - yesterday))
print("Missed today:", sorted(yesterday - customers))
print("Omar came today:", "Omar" in customers)
