# file: practice/solutions/task6.py
import difflib

trusted = ["requests", "tabulate", "pytest", "rich"]
suggested = ["tabluate", "rich", "pytset", "flask"]
for name in suggested:
    close = difflib.get_close_matches(name, trusted, n=1, cutoff=0.8)
    if name in trusted:
        print(f"{name}: trusted")
    elif close:
        print(f"{name}: look-alike of {close[0]}")
    else:
        print(f"{name}: unknown, check pypi.org")
