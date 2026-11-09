# Sources: Chapter 3

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: An Informal Introduction to Python, Text (3.15.2) | https://docs.python.org/3/tutorial/introduction.html | 2026-11-09 | Strings are joined with `+` and repeated with `*`; indexes start at 0 and negative indexes count from the right; an index that is too large raises an error; strings are immutable, so assigning to an index position fails; `len()` returns the length of a string. |
| Python tutorial: Input and Output, Formatted String Literals (3.15.2) | https://docs.python.org/3/tutorial/inputoutput.html | 2026-11-09 | An f-string starts with `f` or `F`; expressions inside `{ }` are evaluated and inserted; an optional format specifier after a colon controls the display, such as a number of decimal places or a minimum width for lining up columns. |
| Python library: string, Format Specification Mini-Language (3.15.2) | https://docs.python.org/3/library/string.html | 2026-11-09 | `<`, `>` and `^` align left, right and centre; a fill character can come before the alignment; the width is a minimum; `f` is fixed-point notation, with a precision of digits after the point; a precision without a type uses significant digits and may switch to scientific notation. |
| Python library: Built-in Types, String Methods (3.15.2) | https://docs.python.org/3/library/stdtypes.html | 2026-11-09 | `strip()`, `title()`, `upper()`, `lower()` and `replace(old, new)` each return a copy of the string; the original is not changed. |
| Real Python: Python's F-String for String Interpolation and Formatting | https://realpython.com/python-f-strings/ | 2026-11-09 | Beginner explanation of f-strings, embedding expressions, and format specifiers for decimals, width and alignment. |
| Cafiero, "Format specifiers: a quick reference", University of Vermont CS1210 textbook | https://uvm.edu/~cbcafier/cs1210/book/07_console_io/format_specifiers.html | 2026-11-09 | `.2f` gives two places after the decimal point; width and alignment codes for building tables of output. |

## Removed or corrected during research

- A planned example of the AI's `.2` mistake used the whole number 6. Python refuses a precision for an integer with `ValueError: Precision not allowed in integer format specifier`, so the example uses the decimal prices 3.5 and 12.5, which show the real problem: `.2` gives `1.2e+01` for 12.5.
- Centred text with spaces as the fill would leave invisible spaces at the end of the receipt's title line. The receipt uses `=` as the fill character instead, so every character of the output is visible.
