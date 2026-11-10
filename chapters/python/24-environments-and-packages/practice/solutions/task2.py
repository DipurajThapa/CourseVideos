# file: practice/solutions/task2.py
lines = ["rich==13.9.4", "tabulate", "requests>=2.31", "pytest==8.3.4"]
pinned = [line for line in lines if "==" in line]
loose = [line for line in lines if "==" not in line]
print("Pinned:", pinned)
print("Not pinned:", loose)
