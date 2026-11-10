# file: examples/ai_mine.py
TRUSTED = ["requests", "tabulate", "pytest"]


def name_check(name):
    if name in TRUSTED:
        return "trusted"
    return "unknown: check pypi.org"


print("requests ->", name_check("requests"))
print("reqeusts ->", name_check("reqeusts"))
