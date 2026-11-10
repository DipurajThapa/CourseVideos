# file: examples/ai_welcome_suggest.py
today = ["Omar", "Lina", "Omar", "Sam"]
seen = set(today)
for name in today:
    name = name.strip().title()
    if name not in seen:
        print(f"Welcome, {name}!")
print(f"New today: {len(seen)}")
