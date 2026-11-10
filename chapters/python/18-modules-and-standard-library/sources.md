# Sources: Chapter 18

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: Modules | https://docs.python.org/3/tutorial/modules.html | 2026-11-10 | A module is a file of definitions whose name is the file name without `.py`; `import`, `from ... import` and `import ... as` forms; a module's code runs once when it is first imported; the script's own folder is searched first; `__name__` is `"__main__"` when a file is run as a script. |
| Python library: `__main__`, Top-level code environment | https://docs.python.org/3/library/__main__.html | 2026-11-10 | The `if __name__ == "__main__":` block runs only when the file is run directly, not when it is imported. |
| Python library: `math`, Mathematical functions | https://docs.python.org/3/library/math.html | 2026-11-10 | `math.ceil()` returns the smallest integer greater than or equal to x, `math.floor()` the largest integer less than or equal to x, and `math.sqrt()` the square root; the module has no `ceildiv` or `round_up` function. |
| Python library: `datetime`, `timedelta` objects | https://docs.python.org/3/library/datetime.html | 2026-11-10 | A `timedelta` is a duration; `timedelta` values can be added and subtracted; `total_seconds()` returns the duration in seconds; `str()` of a duration shows hours, minutes and seconds. |
| Python library: `pathlib`, Object-oriented filesystem paths | https://docs.python.org/3/library/pathlib.html | 2026-11-10 | The `/` operator joins path parts; `name`, `stem` and `suffix` give parts of the final component; `as_posix()` returns the path with forward slashes; pure path operations do not access the file system. |
| Python library: `random` | https://docs.python.org/3/library/random.html | 2026-11-10 | `random.choice()` picks one item from a sequence; `random.seed()` makes the sequence repeat; the documentation promises repeatable `random()` results for a seed, not identical results of every function across versions. |
| What's New In Python 3.13 | https://docs.python.org/3/whatsnew/3.13.html | 2026-11-10 | Python 3.13 added the hint to rename a script that has the same name as a standard library module, which is shown in Mistake 3. |
| PEP 8: Style Guide for Python Code, Imports | https://peps.python.org/pep-0008/#imports | 2026-11-10 | Imports go at the top of the file, one module per line, before other code. |
| Real Python: Python Modules and Packages, An Introduction | https://realpython.com/python-modules-packages/ | 2026-11-10 | A teaching explanation of writing a module, importing it from the same folder, the three import forms and the `__name__` guard. |
