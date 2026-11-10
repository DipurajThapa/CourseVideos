# Sources: Chapter 14

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: Data Structures, List Comprehensions | https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions | 2026-11-10 | A list comprehension is an expression followed by a `for` clause and optional `if` clauses; it gives the same list as the matching loop and leaves the original list unchanged. |
| Python tutorial: Data Structures, Dictionaries | https://docs.python.org/3/tutorial/datastructures.html#dictionaries | 2026-11-10 | Dictionary comprehensions build a dictionary from key and value expressions; curly brackets with a colon make a dictionary. |
| Python tutorial: Data Structures, Sets | https://docs.python.org/3/tutorial/datastructures.html#sets | 2026-11-10 | Curly brackets without a colon in a comprehension make a set comprehension; a set keeps each value once and has no fixed order. |
| Python reference: Expressions, Displays for lists, sets and dictionaries | https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries | 2026-11-10 | The grammar of comprehensions: the `for` and `if` clauses after the first expression; a conditional expression `x if c else y` always needs `else`. |
| Loyola University Chicago, Introduction to Computer Science in Python: List Comprehensions | https://introcs-python.cs.luc.edu/for/listcomprehensions.html | 2026-11-10 | A university teaching reference for rewriting a loop that appends to a list as a comprehension, with and without a filter. |
| freeCodeCamp: List Comprehension in Python | https://www.freecodecamp.org/news/list-comprehension-in-python/ | 2026-11-10 | A beginner explanation of filtering with `if` at the end versus choosing values with `if ... else` at the start, and of when a normal loop is clearer. |

## Removed or corrected during research

- Nested comprehensions with two `for` parts and generator expressions are left out of the lesson steps, to keep one new idea per step. Two `for` parts appear only as a "Think beyond" question.
- Every price with tax is rounded inside the comprehension, because `price * 1.1` stores some results with a tiny error, as the lesson's Mistake 4 shows.
- Set comprehensions appear only as a mistake, because the curriculum covers list and dictionary comprehensions. The set examples print values whose order was checked on every toolchain.
