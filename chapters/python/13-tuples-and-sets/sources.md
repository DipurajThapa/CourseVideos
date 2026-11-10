# Sources: Chapter 13

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: Data Structures, Tuples and Sequences | https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences | 2026-11-10 | Tuples are written with commas, usually inside round brackets; they cannot be changed but can hold changeable objects such as lists; a one-item tuple needs a trailing comma; sequence unpacking needs as many names as values. |
| Python tutorial: Data Structures, Sets | https://docs.python.org/3/tutorial/datastructures.html#sets | 2026-11-10 | A set is an unordered collection with no repeated items; it supports fast membership tests and union, intersection, difference and symmetric difference; `set()` makes an empty set because `{}` makes an empty dictionary. |
| Python library: Built-in Types, Set Types (set, frozenset) | https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset | 2026-11-10 | `add()`, `discard()` (no error for a missing item) and `remove()`; the operators `\|`, `&`, `-` and `^`; sets do not support indexing because they have no order. |
| Python library: Built-in Types, Tuples | https://docs.python.org/3/library/stdtypes.html#tuples | 2026-11-10 | Tuples are immutable sequences; the comma makes the tuple, not the brackets, except for the empty tuple `()`. |
| Python Tutorial (pythontutorial.net): Unpacking a tuple | https://www.pythontutorial.net/python-basics/python-unpacking-tuple/ | 2026-11-10 | A beginner explanation of unpacking a tuple into variables and of swapping two variables with `a, b = b, a`. |
| Imperial College London, Python programming lessons: Sets | https://python.pages.doc.ic.ac.uk/lessons/core08/02-set/01-set.html | 2026-11-10 | A second beginner reference for creating sets, removing duplicates from a list and using membership tests. |

## Removed or corrected during research

- Printing a set of strings directly can show its items in a different order on each run, so every example prints `sorted(...)` instead. This keeps the expected outputs exact.
- The unpacking error message differs between versions: newer Python versions add how many values they got (`expected 2, got 3`), older ones end after `expected 2`. The lesson says so, and the check looks only for the shared part.
- `remove()` on a set, `frozenset`, set comprehensions and tuple methods such as `count()` and `index()` are left out to keep one new idea per step.
