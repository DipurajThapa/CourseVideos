# file: examples/ai_welcome_regression.py
cases = {"normal": ["Omar", "Lina", "Omar", "Sam"],
         "spelling": ["Omar", "omar ", "Lina"],
         "empty": []}
for case, today in cases.items():
    print(f"Case: {case}")
    seen = set()
    for name in today:
        name = name.strip().title()
        if name not in seen:
            print(f"Welcome, {name}!")
            seen.add(name)
    print(f"New today: {len(seen)}")
