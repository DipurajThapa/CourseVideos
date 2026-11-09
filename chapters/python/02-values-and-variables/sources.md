# Sources: Chapter 2

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: An Informal Introduction to Python (3.15.2) | https://docs.python.org/3/tutorial/introduction.html | 2026-11-09 | `=` assigns a value to a variable; `/` always returns a float; `//` is floor division and `%` is the remainder; `**` is power; mixed int and float operands give a float; multiplication happens before subtraction (`50 - 5*6` is 20); an undefined name raises `NameError: name '...' is not defined`. |
| Python docs: Built-in Types, numeric types (3.15.2) | https://docs.python.org/3/library/stdtypes.html | 2026-11-09 | The numeric types int, float and complex; Booleans are a subtype of integers; a literal with a decimal point gives a float; the operations `//`, `%` and `**`; `//` rounds toward minus infinity. |
| Python tutorial: Floating-Point Arithmetic, Issues and Limitations (3.15.2) | https://docs.python.org/3/tutorial/floatingpoint.html | 2026-11-09 | Decimal fractions such as 0.1 are stored as binary approximations, so `0.1 + 0.1 + 0.1` is not exactly 0.3; `round()` helps when displaying or roughly comparing results. |
| Python reference: Lexical analysis, identifiers and keywords (3.15.2) | https://docs.python.org/3/reference/lexical_analysis.html | 2026-11-09 | Names contain letters, digits and underscores, cannot start with a digit and are case-sensitive; `True`, `False`, `None` and `class` are reserved keywords. |
| PEP 8: Style Guide for Python Code | https://peps.python.org/pep-0008/ | 2026-11-09 | Variable names use lowercase words joined by underscores; avoid the single-letter names l, O and I; put one space on each side of `=` and arithmetic assignment. |
| Python downloads page | https://www.python.org/downloads/ | 2026-11-09 | The latest stable release is Python 3.15.2 (released 2026-10-25). |
| Real Python: Variables in Python, Usage and Best Practices | https://realpython.com/python-variables/ | 2026-11-09 | Variables are names that refer to values; reassignment can change the type; naming rules and the snake_case convention. |
| Cafiero, "Names, variables, and assignment", University of Vermont CS1210 textbook | https://uvm.edu/~cbcafier/cs1210/book/04_variables,_statements,_and_expressions/variables.html | 2026-11-09 | Read `=` as assignment, not equality; Python evaluates the right-hand side first, then binds the name; two names can refer to the same value, and reassigning one does not change the other. |
| Imperial College London, Python Programming: Arithmetic operators | https://python.pages.doc.ic.ac.uk/lessons/core02/05-operator/01-operators.html | 2026-11-09 | The seven arithmetic operators and beginner examples such as `7 // 2` is 3 and `7 % 2` is 1. |

## Removed or corrected during research

- A planned example using `0.1 + 0.2` was replaced with `0.1 + 0.1 + 0.1`, the example the official floating-point tutorial uses.
- The cafe bill example first produced a total ending in 5 that `round()` rounded down (12.825 to 12.82). Prices were changed so the result is exact, because explaining binary rounding of halves is beyond this chapter.
