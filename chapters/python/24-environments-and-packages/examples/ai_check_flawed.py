# file: examples/ai_check_flawed.py
from difflib import get_close_matches

TRUSTED = ["requests", "tabulate", "pytest"]


def name_check(name):
    if name in TRUSTED:
        return "trusted"
    close = get_close_matches(name, TRUSTED, cutoff=0.9)
    if close:
        return f"look-alike of {close[0]}"
    return "unknown: check pypi.org"


print("reqeusts ->", name_check("reqeusts"))
