# file: examples/ai_tests_final.py
from difflib import get_close_matches

TRUSTED = ["requests", "tabulate", "pytest"]


def name_check(name):
    name = name.strip().lower()
    if name in TRUSTED:
        return "trusted"
    close = get_close_matches(name, TRUSTED, cutoff=0.8)
    if close:
        return f"look-alike of {close[0]}"
    return "unknown: check pypi.org"


cases = [("requests", "trusted"),
         ("reqeusts", "look-alike of requests"),
         ("Requests", "trusted"),
         ("numpy", "unknown: check pypi.org"),
         (" requests ", "trusted")]
for name, expected in cases:
    result = name_check(name)
    status = "pass" if result == expected else "FAIL"
    print(f"{name:<10} {status}: {result}")
