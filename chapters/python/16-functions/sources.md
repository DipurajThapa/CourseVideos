# Sources: Chapter 16

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: More Control Flow Tools, Defining Functions | https://docs.python.org/3/tutorial/controlflow.html#defining-functions | 2026-11-10 | `def` introduces a function definition; the body is indented; a function without `return` returns `None`; arguments are matched to parameters in order. |
| Python tutorial: Documentation Strings | https://docs.python.org/3/tutorial/controlflow.html#documentation-strings | 2026-11-10 | A docstring is a string on the first line of a function body; it is kept in the function's `__doc__` attribute and read by tools. |
| Python FAQ: What is the difference between arguments and parameters? | https://docs.python.org/3/faq/programming.html#what-is-the-difference-between-arguments-and-parameters | 2026-11-10 | Parameters are the names in a function definition; arguments are the values passed when the function is called. |
| Python reference: The return statement | https://docs.python.org/3/reference/simple_stmts.html#the-return-statement | 2026-11-10 | `return` leaves the current function call with the value of its expression, or `None` when there is no expression. |
| pythontutorial.net: Python Functions | https://www.pythontutorial.net/python-basics/python-functions/ | 2026-11-10 | A beginner explanation of defining and calling functions, parameters versus arguments, and returning a value. |
| University of Pennsylvania CIS 110: Functions (lecture notes) | https://www.cis.upenn.edu/~cis110/current/py/lectures/functions.pdf | 2026-11-10 | A university teaching reference on the difference between printing a value and returning it, and on functions calling other functions. |

## Removed or corrected during research

- Default and keyword arguments, local and global scope are left to Chapter 17, as the curriculum plans.
- Printing a function without calling it shows a memory address that changes on every run, so Mistake 2 shows the deterministic `TypeError` from adding a number to a function instead.
- The error messages shown come from Python 3.12 and newer, checked on the newest release and on 3.13; the `~` and `^` markers under the code need Python 3.11 or newer.
