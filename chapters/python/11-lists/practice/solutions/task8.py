# file: practice/solutions/task8.py
scores = [72, 95, 64, 88, 91]
ranked = sorted(scores, reverse=True)
print(f"Best score: {ranked[0]}")
print(f"Top three: {ranked[:3]}")
print(f"In the order they were played: {scores}")
