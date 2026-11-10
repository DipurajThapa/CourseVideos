# file: examples/ai_tests_flawed.py
from ai_load_flawed import load_scores

cases = [("Normal", "case_normal.csv", 2),
         ("Damaged row", "case_damaged.csv", 2),
         ("Header only", "case_empty.csv", 0)]
for name, path, expected in cases:
    count = len(load_scores(path))
    result = "pass" if count == expected else "FAIL"
    print(f"{name}: found {count}, expected {expected}: {result}")
