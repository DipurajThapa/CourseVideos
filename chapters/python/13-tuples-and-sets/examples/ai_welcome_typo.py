# file: examples/ai_welcome_typo.py
today = ["Omar", "omar ", "Lina"]
seen = set()
for name in today:
    name = name.strip().title()
    if name not in seen:
        print(f"Welcome, {name}!")
        seen.add[name]
print(f"New today: {len(seen)}")
