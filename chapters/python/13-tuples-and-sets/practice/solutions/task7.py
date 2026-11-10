# file: practice/solutions/task7.py
visits = ["Omar", "lina", "Omar", "Sam ", "Lina", "Omar", "Lina", "sam"]
seen = set()
counts = {}
for name in visits:
    name = name.strip().title()
    if name not in seen:
        print(f"Welcome, {name}!")
        seen.add(name)
    counts[name] = counts.get(name, 0) + 1
regulars = set()
for name, count in counts.items():
    if count >= 3:
        regulars.add(name)
print("Free tea for:", sorted(regulars))
