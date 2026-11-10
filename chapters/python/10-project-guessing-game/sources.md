# Sources: Chapter 10

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example on two Python versions (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python library: random, Generate pseudo-random numbers (3.15.2) | https://docs.python.org/3/library/random.html | 2026-11-10 | `randint(a, b)` returns a whole number N with a <= N <= b, so both ends are included; `randrange(start, stop)` works like `range()` and never returns `stop`; `seed()` starts the generator from a fixed value so the same sequence repeats; the module is not meant for security purposes. |
| Python library: Built-in Types, str.isdigit() and str.strip() (3.15.2) | https://docs.python.org/3/library/stdtypes.html | 2026-11-10 | `isdigit()` returns `True` only if every character is a digit and there is at least one character; `strip()` returns a copy without the leading and trailing spaces. |
| Python tutorial: Modules (3.15.2) | https://docs.python.org/3/tutorial/modules.html | 2026-11-10 | A module is a file of Python definitions; `import` makes a module's names available as `module.name`. |
| Python library: Built-in Functions, int() and input() (3.15.2) | https://docs.python.org/3/library/functions.html | 2026-11-10 | `input()` returns the typed line as a string; `int()` raises `ValueError` for text that is not a whole number. |
| note.nkmk.me: Generate random numbers (int and float) in Python | https://note.nkmk.me/en/python-random-randrange-randint/ | 2026-11-10 | A teaching source that contrasts `randrange()` (end value excluded) with `randint()` (end value included), with examples. |
| Programiz: Python String isdigit() | https://www.programiz.com/python-programming/methods/string/isdigit | 2026-11-10 | A teaching source showing that `isdigit()` returns `False` for text with spaces, signs or a decimal point. |

## Removed or corrected during research

- The official documentation guarantees that a seed repeats the same sequence for `random()`, but not that every other function gives the same numbers on every future Python version. The seeded examples (`ex01_random.py`, `ai_secret_*.py`, practice task 3) were run on Python 3.13, 3.14 and 3.15, and gave the same numbers on all three. The tests of the finished game use a fixed secret instead of a seed, so they do not depend on the version at all.
- `isdigit()` also accepts some special digit characters, such as superscript two, which `int()` cannot convert. Players are very unlikely to type them, so the project does not cover them; the official documentation describes the difference between `isdigit()` and `isdecimal()`.
- `continue` and a loop's `else` were left out, as in Chapter 7. The game uses `if`, `elif` and `else` inside the loop instead.
