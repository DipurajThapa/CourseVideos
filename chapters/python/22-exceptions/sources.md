# Sources: Chapter 22

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: Errors and Exceptions | https://docs.python.org/3/tutorial/errors.html | 2026-11-10 | The difference between syntax errors and exceptions; how `try` runs and jumps to the first matching `except`; that an unmatched exception stops the program; `except ... as name`; that `else` runs only when the `try` block raised nothing and is better than adding code to `try`; that `finally` always runs; and that `raise` takes an exception instance or class with a message. |
| Python library: Built-in exceptions | https://docs.python.org/3/library/exceptions.html | 2026-11-10 | `ValueError` is raised for a value of the right type but wrong content, such as `int("four")`; `TypeError` for an operation on the wrong type; `FileNotFoundError`, `NameError` and `KeyError`; and that every exception derives from `BaseException`, so `raise` with a plain string gives a `TypeError`. |
| PEP 8: Style Guide for Python Code, Programming Recommendations | https://peps.python.org/pep-0008/#programming-recommendations | 2026-11-10 | Catch specific exceptions instead of a bare `except:`, which also catches errors you did not mean to handle; and keep the `try` clause to the minimum code needed, so bugs are not hidden. |
| pytest documentation: How to write and report assertions in tests | https://docs.pytest.org/en/latest/how-to/assert.html | 2026-11-10 | `pytest.raises(ExpectedException)` used as a context manager makes a test pass only if the indented code raises that exception; otherwise the test fails with "DID NOT RAISE". |
| Real Python: Python Exceptions, An Introduction | https://realpython.com/python-exceptions/ | 2026-11-10 | A teaching explanation of `try`, `except`, `else`, `finally` and `raise`, and why catching every exception hides problems. |
| Python, real runs during this chapter | Python 3.15.2 and Python 3.13.18, with pytest | 2026-11-10 | Every output and error in the lesson, including the `SyntaxError: expected 'except' or 'finally' block` wording, the `TypeError` from `int(None)` for a short CSV row, and the pytest report for a function that does not raise. |
