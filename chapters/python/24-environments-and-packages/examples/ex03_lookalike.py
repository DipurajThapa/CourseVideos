# file: examples/ex03_lookalike.py
import difflib

trusted = ["requests", "tabulate", "pytest"]
score = difflib.SequenceMatcher(None, "reqeusts", "requests").ratio()
print(round(score, 3))
print(difflib.get_close_matches("reqeusts", trusted, n=1, cutoff=0.8))
print(difflib.get_close_matches("numpy", trusted, n=1, cutoff=0.8))
