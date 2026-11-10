# file: examples/ai_case_empty.py
today = []
seen = set()
for name in today:
    if name not in seen:
        print(f"Welcome, {name}!")
        seen.add(name)
print(f"New today: {len(seen)}")
