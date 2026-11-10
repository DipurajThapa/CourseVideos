# file: examples/ex03_lookalike.py
from difflib import SequenceMatcher, get_close_matches

trusted = ["requests", "tabulate", "pytest"]
pair = SequenceMatcher(None, "reqeusts", "requests")
print(round(pair.ratio(), 3))
print(get_close_matches("reqeusts", trusted, cutoff=0.8))
print(get_close_matches("numpy", trusted, cutoff=0.8))
