# Sources: Chapter 5

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example on two Python versions (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python library: Built-in Functions, input(), int(), float() and round() (3.15.2) | https://docs.python.org/3/library/functions.html | 2026-11-09 | `input()` returns the typed line as a string; `int()` and `float()` convert text to numbers; `round(x)` with no second argument returns the nearest whole number as an `int`, and `round(x, 2)` rounds to two decimal places. |
| Python library: Built-in Types, numeric operations (3.15.2) | https://docs.python.org/3/library/stdtypes.html | 2026-11-09 | `//` is floor division and `%` is the remainder, and for positive whole numbers `(x // y) * y + x % y` equals `x`; `/` always gives a float. |
| Python library: Built-in Exceptions, ZeroDivisionError (3.15.2) | https://docs.python.org/3/library/exceptions.html | 2026-11-09 | `ZeroDivisionError` is raised when the second operand of a division or remainder operation is zero. |
| Python tutorial: Floating-Point Arithmetic, Issues and Limitations (3.15.2) | https://docs.python.org/3/tutorial/floatingpoint.html | 2026-11-09 | Decimal values such as 0.1 are stored as close binary approximations, so results like `total * 100` can be a tiny amount away from the expected whole number. |
| Python library: string, Format Specification Mini-Language (3.15.2) | https://docs.python.org/3/library/string.html | 2026-11-09 | `.2f` shows two decimal places, and `<`, `>` and `^` with a width align text left, right and centre. |
| Modern Treasury Journal: Floats Don't Work for Storing Cents | https://moderntreasury.com/journal/floats-dont-work-for-storing-cents | 2026-11-09 | Payment software stores money as whole numbers of the smallest unit, such as cents, because floats cannot represent most decimal amounts exactly. |

## Removed or corrected during research

- The wording of the last line of a `ZeroDivisionError` depends on the Python version: Python 3.15 prints `division by zero`, while Python 3.13 prints `integer division or modulo by zero` (both confirmed by running `test_zero_people.py`). The project explains both, and the verifier checks only the error name.
- The bill splitter shares money in whole cents with `//` and `%`, instead of rounding each share, because rounding each share can make the payments add up to one cent more than the total (confirmed by running `ai_round_share.py`).
