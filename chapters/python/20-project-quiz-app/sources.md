# Sources: Chapter 20

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example on two Python versions (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: Modules (3.15.2) | https://docs.python.org/3/tutorial/modules.html | 2026-11-10 | A module is a file of definitions that another program imports; `from module import name` brings in chosen names; the folder of the running script is searched first. |
| Python library: Built-in Types, str.strip() and str.lower() (3.15.2) | https://docs.python.org/3/library/stdtypes.html | 2026-11-10 | `strip()` removes leading and trailing whitespace; `lower()` returns a copy in small letters; comparing strings with `==` is exact. |
| Python library: Built-in Functions, round() (3.15.2) | https://docs.python.org/3/library/functions.html#round | 2026-11-10 | `round(x)` with no second value returns the nearest whole number. |
| pytest documentation: Good Integration Practices, test discovery | https://docs.pytest.org/en/stable/explanation/goodpractices.html | 2026-11-10 | pytest collects `test_*.py` files and functions whose names start with `test`. |
| pytest documentation: How to invoke pytest and command-line options (`-q`, `--tb`, `-r`) | https://docs.pytest.org/en/stable/how-to/output.html | 2026-11-10 | `--tb=no` turns off tracebacks and `--tb=short` shows a shorter traceback; the short test summary lists failed tests by default. |
| Real Python glossary: test-driven development (TDD) | https://realpython.com/ref/software-engineering-glossary/test-driven-development-tdd/ | 2026-11-10 | A teaching source describing writing a failing test first, then the code that makes it pass, then improving the code while the tests keep passing. |

## Removed or corrected during research

- The AI's first plan put `input()` inside a rule. The project keeps every rule pure, as Chapter 17 taught, because a test cannot type an answer.
- The quiz compares answers as text after `strip()` and `lower()`. Comparing prices as numbers needs `float()`, which can fail on a word; that case waits for `try` and `except` in Chapter 22, and Practice Task 2 shows the idea.
- The stub module uses functions whose body is only a docstring. Such a function returns `None`, so tests can run before any rule exists; `pass` is not needed.
- `--tb=no` keeps the failure reports short on screen; pytest's short summary already lists each failed test, so `-rf` is not needed. The debug step uses `--tb=short` from Chapter 19 to show the wrong value.
