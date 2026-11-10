# file: practice/solutions/task8.py
def is_pinned(line):
    return "==" in line


for line in ["tabulate==0.9.0", "requests>=2.31", "pytest"]:
    print(f"{line:<16} {is_pinned(line)}")
