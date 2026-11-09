# Sources: Chapter 7

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python reference: Compound statements, the while statement (3.15.2) | https://docs.python.org/3/reference/compound_stmts.html | 2026-11-09 | A `while` statement repeatedly tests its expression and runs its block while the expression is true; `break` in the block ends the loop. |
| Python tutorial: More Control Flow Tools, break and continue (3.15.2) | https://docs.python.org/3/tutorial/controlflow.html | 2026-11-09 | `break` exits the innermost enclosing loop immediately. |
| Python reference: Simple statements, augmented assignment statements (3.15.2) | https://docs.python.org/3/reference/simple_stmts.html | 2026-11-09 | `x += 1` and `x -= 1` are augmented assignments that combine an operation and an assignment. |
| Python library: Built-in Exceptions, KeyboardInterrupt (3.15.2) | https://docs.python.org/3/library/exceptions.html | 2026-11-09 | `KeyboardInterrupt` is raised when the user presses the interrupt key, normally Ctrl+C. |
| Real Python: Python while Loops: Repeating Tasks Conditionally | https://realpython.com/python-while-loop/ | 2026-11-09 | Beginner explanation of `while` loops, loop conditions, `while True` with `break`, and how a loop whose condition never changes runs forever. |

## Removed or corrected during research

- `continue` and the `else` clause of a loop are left out: the curriculum lists `while`, conditions, counters and `break`, and one new idea per step keeps the chapter focused.
- `str.isdigit()` is not used for input checks, because it has not been taught. Answers are converted with `int()` as in Chapter 4, and the examples type whole numbers.
- The infinite loop in Mistake 3 is shown as an illustrative fragment, not a runnable file, so that the verification tool never runs a program that does not end.
