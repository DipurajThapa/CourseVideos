# Sources: Chapter 26

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: Classes | https://docs.python.org/3/tutorial/classes.html | 2026-11-10 | A class definition creates a new type; calling the class creates an instance and runs `__init__`; the instance is passed as the first argument of a method, called `self` by convention; and, in "Class and Instance Variables", that a mutable object such as a list in the class body is shared by all instances, while one created in `__init__` belongs to each instance. |
| Python library: dataclasses | https://docs.python.org/3/library/dataclasses.html | 2026-11-10 | `@dataclass` generates `__init__`, `__repr__` and `__eq__` from the annotated fields; `__eq__` compares the fields in order; a mutable default such as `[]` raises `ValueError` and `field(default_factory=list)` creates a new list for each instance. |
| Python reference: Data model, basic customisation | https://docs.python.org/3/reference/datamodel.html#object.__str__ | 2026-11-10 | `__str__` returns the informal, readable string used by `print()`, `str()` and formatting; `__repr__` returns the official string form, which a data class generates. |
| PEP 8: Style Guide for Python Code, Naming Conventions | https://peps.python.org/pep-0008/#naming-conventions | 2026-11-10 | Class names use CapitalisedWords (`MenuItem`), and the first argument of an instance method is always named `self`. |
| Real Python: Python Classes, The Power of Object-Oriented Programming | https://realpython.com/python-classes/ | 2026-11-10 | A teaching explanation of classes, instances, attributes, methods and `self`, and of instance attributes versus class attributes. |
| Real Python: When Should You Use .__repr__() vs .__str__() in Python? | https://realpython.com/python-repr-vs-str/ | 2026-11-10 | `__str__` is meant for users of a program and `__repr__` for programmers; `print()` uses `__str__`, and falls back to `__repr__` when a class has no `__str__`. |
| Python, real runs during this chapter | Python 3.15.2 and Python 3.13.18, with pytest | 2026-11-10 | Every output and error in the lesson, including `MenuItem.with_tax() takes 0 positional arguments but 1 was given`, `type object 'MenuItem' has no attribute 'price'`, the data class `ValueError` for a list default, and the different wording of the "Did you mean" suggestion on Python 3.15 and 3.13. |
