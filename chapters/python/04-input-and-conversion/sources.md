# Sources: Chapter 4

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python library: Built-in Functions, input(), int(), float() and str() (3.15.2) | https://docs.python.org/3/library/functions.html | 2026-11-09 | `input()` writes its prompt without a newline, reads one line, removes the trailing newline and returns it as a string; `int()` builds an integer from a number or from text that looks like a whole number, and leading and trailing spaces are allowed; `int()` on a float truncates towards zero; `float()` builds a decimal number from a number or from text; `str()` returns the text version of a value. |
| Python library: Built-in Exceptions, TypeError and ValueError (3.15.2) | https://docs.python.org/3/library/exceptions.html | 2026-11-09 | `TypeError` is raised when an operation is applied to a value of the wrong type, such as subtracting a float from a string; `ValueError` is raised when a value has the right type but an unsuitable content, such as `int("two")`. |
| Python tutorial: Errors and Exceptions (3.15.2) | https://docs.python.org/3/tutorial/errors.html | 2026-11-09 | A syntax error is reported before the program runs, with the line and a caret; an exception stops the program with a traceback whose last line names the exception. |
| Microsoft Learn: Introduction to Python, Reading keyboard input | https://learn.microsoft.com/en-us/training/modules/intro-to-python/6-input | 2026-11-09 | Beginner explanation that `input()` always returns text, and that the text must be converted with `int()` or `float()` before calculating. |
| Real Python: How to Read User Input From the Keyboard in Python | https://realpython.com/python-keyboard-input/ | 2026-11-09 | Using a prompt string with `input()`, converting answers with `int()` and `float()`, and the `ValueError` raised for text that is not a number. |
| Cafiero, "Input from the console", University of Vermont CS1210 textbook | https://uvm.edu/~cbcafier/cs1210/book/07_console_io/input.html | 2026-11-09 | Ending a prompt with a space, and converting console input before arithmetic. |

## Removed or corrected during research

- The verifier now echoes each typed answer after its prompt when a Python example reads from a `.stdin` file. Without the echo, the expected output would show the prompts run together with the program's output, which is not what a learner sees in the terminal.
- `int()` is described as cutting off the decimal part, not as rounding, because `int(3.9)` gives 3 (confirmed by running `ex05_conversions.py`).
