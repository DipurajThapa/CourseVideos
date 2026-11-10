# Sources: Chapter 17

All sources were read during the run on the date shown. Content is paraphrased, not copied. Code behaviour was confirmed by running every example (see `verification.json`), not by sources alone.

| Source | URL | Accessed | What it confirmed |
|---|---|---|---|
| Python tutorial: More Control Flow Tools, Default Argument Values | https://docs.python.org/3/tutorial/controlflow.html#default-argument-values | 2026-11-10 | A parameter can have a default value used when the call leaves it out; the default value is evaluated only once, so a list default is shared between calls. |
| Python tutorial: More Control Flow Tools, Keyword Arguments | https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments | 2026-11-10 | Arguments can be passed as `name=value`; keyword arguments must follow positional arguments, and their order does not matter. |
| Python FAQ: What are the rules for local and global variables? / Why am I getting an UnboundLocalError? | https://docs.python.org/3/faq/programming.html | 2026-11-10 | A name assigned anywhere in a function body is local to that function unless declared global; reading it before the assignment raises `UnboundLocalError`; a function can read a global without declaring it. |
| Python reference: Execution model, Naming and binding | https://docs.python.org/3/reference/executionmodel.html | 2026-11-10 | A block's local names are determined by binding operations in the block; names used but not bound locally are looked up in the global scope. |
| Real Python: Python Scope and the LEGB Rule | https://realpython.com/python-scope-legb-rule/ | 2026-11-10 | A teaching explanation of local and global scope and why relying on globals makes code harder to understand and test. |
| Real Python: Namespaces and Scope in Python | https://realpython.com/python-namespaces-scope/ | 2026-11-10 | Each function call has its own local namespace that disappears when the call ends. |

## Removed or corrected during research

- The enclosing scope (functions inside functions) and the `nonlocal` keyword are left out; no example in this course needs nested functions yet.
- The `global` keyword is mentioned once, in the original program Asha splits, as a habit to avoid; the chapter teaches passing values in and returning results instead.
- The usual fix for a list default (`None` and an `is` test) uses the `is` operator, which the course has not taught; the chapter removes the default and passes a new list instead.
- All error messages shown were checked on the newest Python release and on 3.13; their wording is the same in both.
