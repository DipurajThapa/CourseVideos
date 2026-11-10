# Sources: Chapter 19

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python reference: Simple statements, the assert statement | https://docs.python.org/3/reference/simple_stmts.html | 2026-11-10 | `assert expression` raises `AssertionError` when the expression is false; `assert expression1, expression2` passes the second expression as the error message; assertions are skipped when Python runs with optimisation (`-O`). |
| Python tutorial: Floating-point arithmetic, issues and limitations | https://docs.python.org/3/tutorial/floatingpoint.html | 2026-11-10 | Decimal fractions such as 0.1 are stored as binary approximations, so sums such as 0.1 three times are not exactly 0.3; rounding or a closeness test is the safe way to compare. |
| pytest documentation: Get Started | https://docs.pytest.org/en/stable/getting-started.html | 2026-11-10 | Install with `pip install -U pytest`; pytest runs files named `test_*.py` or `*_test.py` and functions whose names start with `test`; plain `assert` statements are used; `-q` gives a quiet report. |
| pytest documentation: How to write and report assertions in tests | https://docs.pytest.org/en/stable/how-to/assert.html | 2026-11-10 | pytest rewrites `assert` statements so a failure shows the values on both sides of the comparison. |
| pytest documentation: API Reference, `pytest.approx` | https://docs.pytest.org/en/stable/reference/reference.html | 2026-11-10 | `pytest.approx()` compares numbers within a small tolerance (a relative tolerance of one millionth by default), so decimal results can be tested safely. |
| Real Python: Effective Python Testing With pytest | https://realpython.com/pytest-python-testing/ | 2026-11-10 | A teaching explanation of test files, test functions, plain `assert` statements and reading pytest's failure reports. |
| pytest, real runs during this chapter | Python 3.15.2 with pytest 9.2.0, Python 3.13.18 with pytest 9.1.1 | 2026-11-10 | Report formats used in the lesson: dots and `F` per test, `--tb=short` failure blocks, the `-`/`+` diff for strings, "no tests ran" when no function starts with `test_`, and that a file passed by name is run even if its name does not start with `test_`. |
