# file: practice/solutions/task5.py
votes = ["cake", "scone", "cake", "muffin", "cake", "scone"]
counts = {}
for vote in votes:
    counts[vote] = counts.get(vote, 0) + 1
for name, count in counts.items():
    print(f"{name}: {count}")
