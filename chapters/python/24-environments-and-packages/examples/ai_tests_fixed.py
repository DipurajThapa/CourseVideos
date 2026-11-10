# file: examples/ai_tests_fixed.py
import difflib

TRUSTED = ["requests", "tabulate", "pytest"]


def name_check(name):
    name = name.lower()
    if name in TRUSTED:
        return "trusted"
    close = difflib.get_close_matches(name, TRUSTED, n=1, cutoff=0.8)
    if close:
        return f"look-alike of {close[0]}"
    return "unknown: check pypi.org"


cases = [("requests", "trusted"), ("reqeusts", "look-alike of requests"),
         ("Requests", "trusted"), ("numpy", "unknown: check pypi.org")]
for name, expected in cases:
    result = name_check(name)
    print(f"{name:<9} {'pass' if result == expected else 'FAIL'}: {result}")
