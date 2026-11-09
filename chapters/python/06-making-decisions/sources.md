# Sources: Chapter 6

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: More Control Flow Tools, if statements (3.15.2) | https://docs.python.org/3/tutorial/controlflow.html | 2026-11-09 | An `if` statement can have zero or more `elif` parts and an optional `else` part; `elif` is short for "else if"; Python runs the block of the first condition that is true. |
| Python library: Built-in Types, truth value testing, boolean operations and comparisons (3.15.2) | https://docs.python.org/3/builtins/stdtypes.html | 2026-11-09 | The comparison operators `<`, `<=`, `>`, `>=`, `==` and `!=` and their meanings; comparisons give `True` or `False`; `and`, `or` and `not` and their results; `str.lower()` and `str.strip()` return new strings. |
| Python tutorial: Errors and Exceptions, syntax errors (3.15.2) | https://docs.python.org/3/tutorial/errors.html | 2026-11-09 | A syntax error is reported before the program runs, with the line and a caret that marks where Python noticed the problem. |
| Real Python: Operators and Expressions in Python | https://realpython.com/python-operators-expressions/ | 2026-11-09 | Beginner explanation of comparison operators, the difference between `=` and `==`, and how `and`, `or` and `not` combine conditions. |
| Real Python: How to Properly Indent Python Code | https://realpython.com/how-to-indent-in-python/ | 2026-11-09 | Python uses indentation to group the lines of a block; 4 spaces per level is the recommended style; a missing indented block causes an `IndentationError`. |

## Removed or corrected during research

- The lesson does not teach chained comparisons such as `8 <= hour < 18`. Practice task 4 uses two comparisons joined with `and`, which matches what the lesson teaches.
- Nested `if` blocks are left to a later chapter. Practice task 7 puts every division inside the `else` block instead.
- The `:=` operator, which appears in the `SyntaxError` hint for a single `=`, is mentioned only as a feature this course does not use.
