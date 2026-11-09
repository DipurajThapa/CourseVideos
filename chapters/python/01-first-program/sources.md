# Sources: Chapter 1

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python Developer's Guide: Status of Python versions | https://devguide.python.org/versions/ | 2026-11-09 | 3.14 and 3.15 are the bugfix (current) branches; 3.12 and 3.13 receive security fixes, so 3.12 is a safe minimum. |
| Python 3.15.2 release page | https://www.python.org/downloads/release/python-3152/ | 2026-11-09 | 3.15.2 was released on 2026-10-25 and is the latest maintenance release of 3.15. |
| Python docs: Using Python on Windows (3.15.2) | https://docs.python.org/3/using/windows.html | 2026-11-09 | The Python install manager (python.org or Microsoft Store) is the recommended way to install; the traditional installer is deprecated since 3.14 and ends with 3.16; `python` and `py` commands. |
| Python docs: Using Python on macOS (3.15.2) | https://docs.python.org/3/using/mac.html | 2026-11-09 | Install with the `.pkg` from python.org; run scripts with `python3 file.py`. |
| Python tutorial: Using the Python Interpreter (3.15) | https://docs.python.org/3.15/tutorial/interpreter.html | 2026-11-09 | Python reads and executes a script file; the interactive prompt; source files are UTF-8 by default. |
| Real Python: print() reference | https://realpython.com/ref/builtin-functions/print/ | 2026-11-09 | The signature `print(*objects, sep=" ", end="\n", file=None, flush=False)` and the defaults of `sep` and `end`. |
| Liu et al., "Teaching CS50 with AI", SIGCSE 2024 | https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf | 2026-11-09 | AI tutors designed to guide rather than give answers; the authors report that the tools sometimes gave wrong advice while sounding confident. |

## Removed or corrected during research

- Older guidance to install Python on Windows with the traditional `.exe` installer was replaced with the Python install manager, following the current official documentation.
