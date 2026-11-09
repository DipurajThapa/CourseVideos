# Sources: Chapter 8

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: More Control Flow Tools, for statements and the range() function (3.15.2) | https://docs.python.org/3/tutorial/controlflow.html | 2026-11-09 | A `for` statement iterates over the items of a sequence in order; `range()` produces arithmetic progressions, and the given end point is never part of the sequence. |
| Python library: Built-in Types, ranges (3.15.2) | https://docs.python.org/3/library/stdtypes.html#ranges | 2026-11-09 | `range(stop)` and `range(start, stop[, step])`; the arguments must be integers; a negative step counts down and the sequence stops before `stop`. |
| Python reference: Compound statements, the for statement (3.15.2) | https://docs.python.org/3/reference/compound_stmts.html | 2026-11-09 | The block of a `for` statement runs once for each item, with the item assigned to the target variable; the loop ends when the items are used up. |
| Real Python: Python range(): Represent Numerical Ranges | https://realpython.com/python-range/ | 2026-11-09 | Beginner explanation of the one-, two- and three-argument forms of `range()`, counting down with a negative step, and why the stop value is excluded. |
| Dataquest: How to Write a For Loop in Python | https://www.dataquest.io/blog/tutorial-how-to-write-a-for-loop-in-python/ | 2026-11-09 | Beginner explanation of looping over strings and ranges and keeping a running total inside a `for` loop. |

## Removed or corrected during research

- Lists are not used: they arrive in Chapter 11. Every loop goes over a `range()` or a string.
- `continue`, the `else` clause of a loop and nested loops are left out to keep one new idea per step.
- `str.isdigit()` and the `in` operator are not used, because they have not been taught. Step 3 counts hyphens with `==`.
- Error messages were checked on the toolchains in `verification.json`; `range()` with a decimal number raises `TypeError: 'float' object cannot be interpreted as an integer`.
