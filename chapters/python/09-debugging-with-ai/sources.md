# Sources: Chapter 9

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour and every error message were confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: Errors and Exceptions (3.15.2) | https://docs.python.org/3/tutorial/errors.html | 2026-11-09 | There are two kinds of errors Python reports, syntax errors and exceptions; a syntax error is reported with the file, the line and a marker; an exception that is not handled stops the program and prints a traceback whose last line names the exception type and message. |
| Python library: Built-in Exceptions (3.15.2) | https://docs.python.org/3/library/exceptions.html | 2026-11-09 | `TypeError`, `NameError`, `ValueError`, `ZeroDivisionError`, `SyntaxError` and `IndentationError` are built-in exceptions and what each one means. |
| Real Python: Understanding the Python Traceback | https://realpython.com/python-traceback/ | 2026-11-09 | Beginner guide to reading a traceback from the bottom up: the last line names the error, the lines above give the file, line number and code, and "most recent call last" means the newest step is at the bottom. |
| OpenClassrooms: Identify the Three Different Types of Bugs | https://openclassrooms.com/en/courses/7744266-debug-your-python-project/7913773-identify-the-three-different-types-of-bugs | 2026-11-09 | Teaching explanation of syntax errors, runtime errors and logic errors, and that logic errors give no message. |
| LaunchCode: Types of Errors | https://education.launchcode.org/lchs/chapters/errors-and-debugging/error-types.html | 2026-11-09 | Beginner explanation of the three error types and of adding print statements to inspect values while debugging. |

## Removed or corrected during research

- `try` and `except` are not used: handling exceptions is taught in Chapter 22. This chapter reads errors and fixes their causes instead.
- Debugger tools (breakpoints) are left out; print debugging works in every editor and needs no setup.
- Tracebacks in this chapter have one step, because functions arrive in Chapter 16.
- Every error message was checked on the toolchains in `verification.json`. The newer messages with suggestions, such as "Perhaps you forgot a comma?" and "'(' was never closed", need Python 3.10 or newer; the course minimum is 3.12.
