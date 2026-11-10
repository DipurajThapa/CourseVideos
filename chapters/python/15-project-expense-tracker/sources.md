# Sources: Chapter 15

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example on two Python versions (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python library: Built-in Functions, max(), sum(), sorted(), float() (3.15.2) | https://docs.python.org/3/library/functions.html | 2026-11-10 | `max()` returns the largest item of an iterable and raises `ValueError` when the iterable is empty and no default is given; `sum()` adds the items of an iterable; `sorted()` returns a new sorted list; `float()` converts a string that looks like a number. |
| Python library: Built-in Types, str.replace(), str.isdigit(), dict.get() and dict views (3.15.2) | https://docs.python.org/3/library/stdtypes.html | 2026-11-10 | `replace(old, new, count)` replaces only the first `count` occurrences when `count` is given; `isdigit()` is `True` only for a non-empty string of digits; `get(key, default)` returns the default when the key is missing; iterating over a dictionary gives its keys. |
| Python tutorial: Data Structures, looping techniques and dictionaries (3.15.2) | https://docs.python.org/3/tutorial/datastructures.html | 2026-11-10 | Dictionary keys are unique, so storing a value under an existing key replaces the old value; a `for` loop can unpack tuples into several variables. |
| Real Python: Python's min() and max(): Find Smallest and Largest Values | https://realpython.com/python-min-and-max/ | 2026-11-10 | A teaching source showing that `max()` on a dictionary works on the keys by default, and that an empty iterable raises `ValueError`. |
| Programiz: Python max() | https://www.programiz.com/python-programming/methods/built-in/max | 2026-11-10 | A teaching source with examples of `max()` on lists and dictionaries, where a dictionary gives the largest key. |

## Removed or corrected during research

- `max(totals, key=totals.get)` finds the key with the biggest value in one line, but `key=` with a function has not been taught yet (functions arrive in Chapter 16). The project uses a loop that keeps the biggest category so far, which also handles an empty day.
- The amount check `replace(".", "", 1).isdigit()` rejects negative amounts and amounts with a comma. It also accepts `12.` and `.5`, which `float()` converts without an error, so the program never crashes on them.
- `try` and `except` would also catch a bad amount, but they arrive in Chapter 22. The project checks text before converting it, as Chapter 10 did.
- The wording of the `ValueError` from `max()` on an empty dictionary was checked on Python 3.15.2 and 3.13. The test checks only the shared part, `ValueError: max()`.
