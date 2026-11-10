# Sources: Chapter 12

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: Data Structures, Dictionaries | https://docs.python.org/3/tutorial/datastructures.html#dictionaries | 2026-11-10 | Dictionaries are indexed by keys, keys are unique, storing a value under an existing key replaces the old value, `del` removes a key, `in` checks keys, and `list(d)` gives the keys in insertion order. |
| Python tutorial: Data Structures, Looping Techniques | https://docs.python.org/3/tutorial/datastructures.html#looping-techniques | 2026-11-10 | `items()` gives each key and value together when looping over a dictionary. |
| Python library: Built-in Types, Mapping Types (dict) | https://docs.python.org/3/library/stdtypes.html#mapping-types-dict | 2026-11-10 | `d[key]` raises `KeyError` for a missing key; `get(key, default)` returns the default or `None` and never raises; `pop(key)` removes a key and returns its value; `keys()`, `values()` and `items()` are views; dictionaries keep insertion order. |
| Real Python: Dictionaries in Python | https://realpython.com/python-dicts/ | 2026-11-10 | Beginner explanations of creating dictionaries, accessing and updating values, `get()` with a default, looping with `items()` and nested dictionaries. |
| W3Schools: Python Dictionaries | https://www.w3schools.com/python/python_dictionaries.asp | 2026-11-10 | A second beginner reference for dictionary syntax, duplicate keys overwriting earlier values, and `len()` on a dictionary. |

## Removed or corrected during research

- Dictionary order is described as "the order you added the items", with no version number, because the course minimum (Python 3.12) keeps insertion order and the lesson stays evergreen.
- A missing colon after a key gives different error messages on different Python versions (checked on the toolchains in `verification.json`), so it was replaced as Mistake 4 by looping over a dictionary when you need its values.
- `setdefault()`, `update()`, dictionary comprehensions, `collections.Counter` and `defaultdict` are left out. Comprehensions come in Chapter 14.
