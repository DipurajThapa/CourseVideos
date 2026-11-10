# file: examples/ai_debug_check.py
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


print("reqeusts ->", name_check("reqeusts"))
print("requests ->", name_check("requests"))
