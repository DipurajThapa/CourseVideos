# Sources: Chapter 25

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example on two Python versions (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python library: csv, DictReader (3.15.2) | https://docs.python.org/3/library/csv.html | 2026-11-10 | `DictReader` uses the first row as the field names, exactly as written; a short row fills the missing fields with `None`; `fieldnames` holds the names; open the file with `newline=""`. |
| Python library: json (3.15.2) | https://docs.python.org/3/library/json.html | 2026-11-10 | `json.loads()` raises `JSONDecodeError`, a subclass of `ValueError`, whose `msg` attribute is the reason without the position; `json.dumps(..., indent=2)` writes indented JSON. |
| Python library: pathlib, Path.glob() and Path.stem (3.15.2) | https://docs.python.org/3/library/pathlib.html | 2026-11-10 | `Path.glob("*.csv")` yields the paths in a folder that match the pattern, in no guaranteed order; `stem` is the file name without its suffix; `read_text()` raises `FileNotFoundError` for a missing file. |
| Python tutorial: Errors and Exceptions (3.15.2) | https://docs.python.org/3/tutorial/errors.html | 2026-11-10 | `else` runs when the `try` block raised nothing; raising a new exception inside `except` is allowed; catching specific exceptions is preferred. |
| Python library: Built-in Functions, float() and round() (3.15.2) | https://docs.python.org/3/library/functions.html | 2026-11-10 | `float()` raises `ValueError` for text that is not a number and `TypeError` for `None`; `round(x)` returns the nearest whole number. |
| pytest documentation: How to write and report assertions, pytest.raises | https://docs.pytest.org/en/stable/how-to/assert.html | 2026-11-10 | `with pytest.raises(ValueError):` passes only when the block raises that exception. |
| Real Python: Reading and Writing CSV Files in Python | https://realpython.com/python-csv/ | 2026-11-10 | A teaching source describing `csv.DictReader`, the header row as keys and common problems with real CSV data. |

## Removed or corrected during research

- `Path.glob()` gives no guaranteed order, so the project sorts the paths and starts each file name with a number, such as `1-monday.csv`, to keep the days in order.
- The bad settings file is missing a comma. Its message, `Expecting ',' delimiter`, is the same on every Python version tested; a trailing comma gives different wording on older versions.
- `"\n".join()` was not taught in earlier chapters, so `report.py` writes the report one line at a time with `file.write()`, as Chapter 21 taught.
- The report rounds only for display, with `:.2f`. Rounding each day before adding changes the week total, which the AI's Improve suggestion shows.
