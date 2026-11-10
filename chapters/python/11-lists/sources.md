# Sources: Chapter 11

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: Data Structures, More on Lists | https://docs.python.org/3/tutorial/datastructures.html | 2026-11-10 | The list methods `append()`, `insert()`, `remove()` (removes the first match and raises `ValueError` when there is none), `pop()` (removes and returns the last item) and `sort()`; methods that change a list in place return `None`. |
| Python tutorial: An Informal Introduction, Lists | https://docs.python.org/3/tutorial/introduction.html#lists | 2026-11-10 | Lists are written as comma-separated items in square brackets, can be indexed and sliced, and are mutable, unlike strings. |
| Python library: Built-in Types, sequence types and lists | https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range | 2026-11-10 | Indexing with negative numbers, slices `s[i:j]` that stop before `j`, slices that are cut at the end of the sequence, the `in` test, and `len()`, `min()` and `max()` on sequences. |
| Python HOWTO: Sorting Techniques | https://docs.python.org/3/howto/sorting.html | 2026-11-10 | `sorted()` returns a new sorted list and leaves the original unchanged; `list.sort()` sorts in place and returns `None`; `reverse=True` sorts from largest to smallest. |
| Python reference: Lexical analysis, string literal concatenation | https://docs.python.org/3/reference/lexical_analysis.html#string-literal-concatenation | 2026-11-10 | Two string literals next to each other are joined into one, which is why a missing comma in a list of strings joins two items. |
| Real Python: Python's list Data Type | https://realpython.com/python-list/ | 2026-11-10 | Beginner explanations of creating lists, indexing and slicing, adding and removing items, and the difference between `sorted()` and `.sort()`. |

## Removed or corrected during research

- Nested lists, list comprehensions, `extend()`, `index()`, `count()` and `del` are left out. Comprehensions come in Chapter 14.
- `enumerate()` is not used. The practice task numbers items with a counter, as in Chapter 7.
- The error messages were checked on the toolchains in `verification.json`.
