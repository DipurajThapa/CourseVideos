# Sources: Chapter 28

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example on two Python versions (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python library: dataclasses (3.15.2) | https://docs.python.org/3/library/dataclasses.html | 2026-11-10 | `@dataclass` writes `__init__`, `__repr__` and `__eq__` from the fields; fields can have default values. |
| Python library: json (3.15.2) | https://docs.python.org/3/library/json.html | 2026-11-10 | `json.dumps()` turns dicts, lists, strings, numbers, `True`, `False` and `None` into JSON and raises `TypeError` for other objects; `json.loads()` raises `JSONDecodeError`, whose `msg` is the reason; `indent=2` writes indented JSON. |
| Python library: pathlib (3.15.2) | https://docs.python.org/3/library/pathlib.html | 2026-11-10 | `Path.read_text()` and `Path.write_text()` read and write a whole text file, with an `encoding` argument. |
| Python library: Built-in Exceptions (3.15.2) | https://docs.python.org/3/library/exceptions.html | 2026-11-10 | `FileNotFoundError` is raised for a missing file; `ValueError` for a value of the right type but a wrong value, such as `int("high")`; `TypeError` for an operation on a type that does not support it. |
| pytest API reference: pytest.raises | https://docs.pytest.org/en/stable/reference/reference.html#pytest-raises | 2026-11-10 | `with pytest.raises(ValueError):` passes only when the block raises that exception. |
| Real Python: Encoding Custom Types to JSON | https://realpython.com/lessons/encoding-custom-types-json/ | 2026-11-10 | Custom objects must be turned into built-in types, such as a dictionary, before `json` can save them. |
