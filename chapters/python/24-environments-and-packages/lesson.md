# Chapter 24: Virtual Environments and Packages

> Quest: give your project its own Python, install a package into it, record exactly what you installed, and check every package name before you trust it. Reward: 100 XP and the **Toolsmith** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Create a virtual environment with `venv`, then activate and deactivate it.
- Install a package with `python -m pip` and check what is installed.
- Write a `requirements.txt` file with pinned versions and install from it.
- Check that a package name is real and trustworthy before you install it.
- Use an AI assistant to suggest packages, then check every name it gives you.

## Why this matters

At the end of Chapter 23, Asha's weather board read a saved sample response. To fetch live weather, she needs `requests`. To print a neat table, she wants `tabulate`. Neither comes with Python. They are **packages**: code that other people wrote and shared.

Most packages live on **PyPI**, the Python Package Index at pypi.org. Anyone can publish there. That makes PyPI a huge help, and a risk: a package with a name one letter away from a famous one can contain harmful code.

Asha also has two computers: the cafe laptop and her laptop at home. Her board must run the same way on both. So she needs three habits: give each project its own place for packages, write down exactly which versions it uses, and check every name before installing.

## The idea

A **virtual environment** is a folder that holds a private copy of the Python setup for one project, with its own packages. You install packages into it, not into the Python that the whole computer shares.

```text
  Without a virtual environment       With one per project
  -----------------------------       ---------------------------------
  Computer Python                     weather_board/
    requests 2.31                       .venv/   requests 2.32.3, tabulate
    tabulate                          quiz_app/
    everything from every project       .venv/   pytest
```

Think of it as a separate toolbox for each project. The quiz app's tools never get mixed up with the weather board's tools. The comparison stops working at one point: you cannot carry a toolbox to another computer. A virtual environment is built for one computer, so you build a new one there from a list of what it needs.

That list is **`requirements.txt`**: a text file with one package per line. A **pinned** line names an exact version with `==`, such as `tabulate==0.9.0`, so every computer installs the same code.

| Word | Meaning |
|---|---|
| package | Code from someone else that you install, such as `requests` |
| PyPI | The Python Package Index at pypi.org, where most packages are published |
| pip | The tool that installs packages from PyPI |
| virtual environment | A project folder, usually `.venv`, with its own Python and packages |
| pinned version | An exact version written with `==` in `requirements.txt` |

## Build it step by step

**Step 1: Create a virtual environment.** Open a terminal in your project folder. Run `venv`, the standard module that makes virtual environments, and name the folder `.venv`:

| System | Type this |
|---|---|
| Windows | `py -m venv .venv` |
| macOS and Linux | `python3 -m venv .venv` |

Nothing prints, but a new `.venv` folder appears. On macOS and Linux it holds a `bin` folder with its own `python` and `pip`. On Windows the same programs are in a `Scripts` folder.

**Step 2: Activate it.** **Activating** tells your terminal to use the Python inside `.venv`:

| System | Type this |
|---|---|
| Windows (Command Prompt or PowerShell) | `.venv\Scripts\activate` |
| macOS and Linux | `source .venv/bin/activate` |

The prompt now starts with `(.venv)`. You can check that you are inside it:

```console
(.venv) $ python -c "import sys; print(sys.prefix != sys.base_prefix)"
True
```

`sys.prefix` is the folder of the Python that is running, and `sys.base_prefix` is the computer's own Python. They differ only inside a virtual environment. Type `deactivate` to leave it. Activate it again each time you open a new terminal.

**Step 3: Install a package.** With the environment active, install with `python -m pip`. Writing `python -m` makes sure that pip installs into the Python you are running:

```console
(.venv) $ python -m pip install tabulate
(.venv) $ python -m pip list
Package  Version
-------- -------
pip      26.2.2
tabulate 0.9.0
```

`pip list` shows what is installed in this environment. Your pip version can differ. `python -m pip show tabulate` prints details, including `Requires:`, the other packages it needs. `tabulate` needs none. In version 2.32.3, `requests` needs four helper packages, and pip installs them for you.

**Step 4: Record and reinstall.** `pip freeze` prints every installed package as a pinned line. Save it into `requirements.txt` with `>`.

```console
(.venv) $ python -m pip freeze > requirements.txt
```

On another computer, Asha creates and activates a new `.venv`, then installs exactly the same versions.

```console
(.venv) $ python -m pip install -r requirements.txt
```

Asha's board file lists the two packages it uses. The `#` line is a comment. Her program reads the file and shows each name and version:

```text
# Packages for the weather board
requests==2.32.3
tabulate==0.9.0
```

The versions in this chapter are examples. Check pypi.org for the version you want.

```python
# file: examples/ex01_read_requirements.py
from pathlib import Path

path = Path("requirements.txt")
text = path.read_text(encoding="utf-8")
for line in text.splitlines():
    line = line.strip()
    if line == "" or line.startswith("#"):
        continue
    name, version = line.split("==")
    print(f"{name:<10} {version}")
```

<!-- output: examples/ex01_read_requirements.expected -->
```output
requests   2.32.3
tabulate   0.9.0
```

Line 10 splits each pinned line at `==`, so `name` gets the package and `version` gets the number.

**Step 5: Pinned or not?** A line without `==` lets pip choose a version, and that version can change next month. `pytest>=8` means "8 or newer", which is not exact either.

```python
# file: examples/ex02_pins.py
lines = ["requests==2.32.3", "tabulate", "pytest>=8"]
for line in lines:
    if "==" in line:
        print(f"{line:<18} pinned")
    else:
        print(f"{line:<18} not pinned")
```

<!-- output: examples/ex02_pins.expected -->
```output
requests==2.32.3   pinned
tabulate           not pinned
pytest>=8          not pinned
```

**Step 6: Check a name before you install it.** Before you install a package, check four things on its pypi.org page:

| Check | What to look for |
|---|---|
| The exact name | Every letter matches the package you meant. PyPI names ignore capital letters. |
| Project links | A link to its source code and documentation |
| Release history | How long it has existed, and when it was last updated |
| Maintainers | Who publishes it, and whether the documentation names the same people |

A name one or two letters away from a famous package, such as `reqeusts`, is a warning sign. People publish look-alike names on purpose, hoping for a spelling mistake. Python's standard module `difflib` can measure how similar two names are. Its score goes from 0 (nothing alike) to 1 (the same):

```python
# file: examples/ex03_lookalike.py
from difflib import SequenceMatcher, get_close_matches

trusted = ["requests", "tabulate", "pytest"]
pair = SequenceMatcher(None, "reqeusts", "requests")
print(round(pair.ratio(), 3))
print(get_close_matches("reqeusts", trusted, cutoff=0.8))
print(get_close_matches("numpy", trusted, cutoff=0.8))
```

<!-- output: examples/ex03_lookalike.expected -->
```output
0.875
['requests']
[]
```

The swapped letters still score 0.875. `get_close_matches()` returns the trusted names whose score is at least `cutoff`, so `reqeusts` matches `requests`, and `numpy` matches nothing.

## See the outcome

Asha's check reads a draft requirements file for the board. It reports unpinned lines and names that are not on her trusted list, with the closest trusted name.

```text
# Weather board packages
requests==2.32.3
tabulate
reqeusts==2.32.3
pytest>=8
```

```python
# file: examples/ex04_check_requirements.py
from difflib import get_close_matches
from pathlib import Path

TRUSTED = ["requests", "tabulate", "pytest"]
path = Path("board_requirements.txt")
text = path.read_text(encoding="utf-8")
problems = 0
for line in text.splitlines():
    line = line.strip()
    if line == "" or line.startswith("#"):
        continue
    name = line.split("==")[0].lower()
    if "==" not in line:
        print(f"{line}: not pinned")
        problems += 1
    elif name not in TRUSTED:
        close = get_close_matches(name, TRUSTED, cutoff=0.8)
        hint = close[0] if close else "no trusted name"
        print(f"{line}: unknown, close to {hint}")
        problems += 1
    else:
        print(f"{line}: OK")
print(f"Problems found: {problems}")
```

<!-- output: examples/ex04_check_requirements.expected -->
```output
requests==2.32.3: OK
tabulate: not pinned
reqeusts==2.32.3: unknown, close to requests
pytest>=8: not pinned
Problems found: 3
```

Three lines need work before Asha installs anything. She pins `tabulate`, pins `pytest`, and fixes the spelling of `requests`.

## Work with AI

The AI skill for this chapter is checking every package an AI suggests. An AI assistant may name a package that does not exist, or one with a spelling error. Attackers can publish packages with exactly those names. So never install a name from a chat before you check it on pypi.org.

Never paste API keys, passwords or private data into an AI tool. Run every install command inside your virtual environment.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Ask for the steps to add a package to a project safely, then check that a name check is one of them. |
| Write | Write your own name check first, then ask the AI what it prints for a misspelled name. |
| Generate | Ask for a version that warns about look-alike names, and ask what it prints. Run it. |
| Test | Run your own cases on the AI's code: an exact name, a look-alike, capital letters and an unknown name. |
| Debug | Paste the code and the full error, and ask for the cause. Check any package name in the answer. |
| Improve | Ask for one improvement to your setup, then check it against the virtual environment rule. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha wrote her own `name_check()`. It only knows exact names:

```python
# file: examples/ai_mine.py
TRUSTED = ["requests", "tabulate", "pytest"]


def name_check(name):
    if name in TRUSTED:
        return "trusted"
    return "unknown: check pypi.org"


print("requests ->", name_check("requests"))
print("reqeusts ->", name_check("reqeusts"))
```

<!-- output: examples/ai_mine.expected -->
```output
requests -> trusted
reqeusts -> unknown: check pypi.org
```

She asked an AI assistant for a version that also warns about look-alike names. The AI used `difflib` and said that `reqeusts` returns `look-alike of requests`.

```python
# file: examples/ai_check_flawed.py
from difflib import get_close_matches

TRUSTED = ["requests", "tabulate", "pytest"]


def name_check(name):
    if name in TRUSTED:
        return "trusted"
    close = get_close_matches(name, TRUSTED, cutoff=0.9)
    if close:
        return f"look-alike of {close[0]}"
    return "unknown: check pypi.org"


print("reqeusts ->", name_check("reqeusts"))
```

<!-- output: examples/ai_check_flawed.expected -->
```output
reqeusts -> unknown: check pypi.org
```

The AI was wrong. Its `cutoff` is 0.9, and `reqeusts` scores only 0.875, as Step 6 showed. Asha ran her four test cases on the AI's code. Two failed: the look-alike, and `Requests` with a capital R, which PyPI treats as the same name.

```python
# file: examples/ai_tests_flawed.py
from difflib import get_close_matches

TRUSTED = ["requests", "tabulate", "pytest"]


def name_check(name):
    if name in TRUSTED:
        return "trusted"
    close = get_close_matches(name, TRUSTED, cutoff=0.9)
    if close:
        return f"look-alike of {close[0]}"
    return "unknown: check pypi.org"


cases = [("requests", "trusted"),
         ("reqeusts", "look-alike of requests"),
         ("Requests", "trusted"),
         ("numpy", "unknown: check pypi.org")]
for name, expected in cases:
    result = name_check(name)
    status = "pass" if result == expected else "FAIL"
    print(f"{name:<9} {status}: {result}")
```

<!-- output: examples/ai_tests_flawed.expected -->
```output
requests  pass: trusted
reqeusts  FAIL: unknown: check pypi.org
Requests  FAIL: unknown: check pypi.org
numpy     pass: unknown: check pypi.org
```

She pasted the two failures and asked for the cause first. The AI changed the name to small letters with `lower()` and set `cutoff` to 0.8. Every case passed:

```python
# file: examples/ai_tests_fixed.py
from difflib import get_close_matches

TRUSTED = ["requests", "tabulate", "pytest"]


def name_check(name):
    name = name.lower()
    if name in TRUSTED:
        return "trusted"
    close = get_close_matches(name, TRUSTED, cutoff=0.8)
    if close:
        return f"look-alike of {close[0]}"
    return "unknown: check pypi.org"


cases = [("requests", "trusted"),
         ("reqeusts", "look-alike of requests"),
         ("Requests", "trusted"),
         ("numpy", "unknown: check pypi.org")]
for name, expected in cases:
    result = name_check(name)
    status = "pass" if result == expected else "FAIL"
    print(f"{name:<9} {status}: {result}")
```

<!-- output: examples/ai_tests_fixed.expected -->
```output
requests  pass: trusted
reqeusts  pass: look-alike of requests
Requests  pass: trusted
numpy     pass: unknown: check pypi.org
```

Later, Asha copied an import line from a chat into her weather script. It stopped with an error:

```python
# file: examples/ai_debug_crash.py
import reqeusts

print("Fetching the weather...")
```

<!-- error: examples/ai_debug_crash.expected_error -->
```output
Traceback (most recent call last):
  File "ai_debug_crash.py", line 2, in <module>
    import reqeusts
ModuleNotFoundError: No module named 'reqeusts'
```

The AI said: "The package is not installed. Run `python -m pip install reqeusts`." That advice is dangerous. Asha checked the name first:

```python
# file: examples/ai_debug_check.py
from difflib import get_close_matches

TRUSTED = ["requests", "tabulate", "pytest"]


def name_check(name):
    name = name.lower()
    if name in TRUSTED:
        return "trusted"
    close = get_close_matches(name, TRUSTED, cutoff=0.8)
    if close:
        return f"look-alike of {close[0]}"
    return "unknown: check pypi.org"


print("reqeusts ->", name_check("reqeusts"))
print("requests ->", name_check("requests"))
```

<!-- output: examples/ai_debug_check.expected -->
```output
reqeusts -> look-alike of requests
requests -> trusted
```

The real problem was a spelling mistake in the import line, not a missing package. She fixed the spelling to `requests` and installed `requests` inside her virtual environment. Installing the look-alike could have run someone else's code on the cafe laptop.

## Common mistakes

**Mistake 1: the environment is not active.** Asha installs a package in her virtual environment, opens a new terminal and runs her program. It stops:

```python
# file: examples/err01_missing_module.py
import weather_tables

print("Board ready")
```

<!-- error: examples/err01_missing_module.expected_error -->
```output
Traceback (most recent call last):
  File "err01_missing_module.py", line 2, in <module>
    import weather_tables
ModuleNotFoundError: No module named 'weather_tables'
```

Fix: check the prompt. Without `(.venv)` at the start, the terminal uses the computer's own Python, where the package is not installed. Activate the environment, then run the program again. If the prompt does show `(.venv)`, check the spelling of the name.

**Mistake 2: one equals sign in a pin.** A pin needs two equals signs. With one, the line has no `==`. So splitting at `==` gives only one part.

```python
# file: examples/err02_one_equals.py
line = "tabulate=0.9.0"
name, version = line.split("==")
print(name, version)
```

<!-- error: examples/err02_one_equals.expected_error -->
```output
Traceback (most recent call last):
  File "err02_one_equals.py", line 3, in <module>
    name, version = line.split("==")
    ^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected 2, got 1)
```

Fix: write `tabulate==0.9.0`. pip also refuses a line with one equals sign, so check the file before you share it.

**Mistake 3: installing into the computer's Python.** Some systems refuse a plain `pip install` outside a virtual environment:

```text
error: externally-managed-environment
```

Fix: do not force it with `sudo` or `--break-system-packages`. Create and activate a virtual environment, then install there. The message protects the Python that your computer's own tools need.

**Mistake 4: copying the `.venv` folder.** A virtual environment contains paths for one computer. Copied to another computer, or into a different folder, it may stop working.

Fix: never copy or share `.venv`. Share `requirements.txt`, and build a new environment on each computer with `python -m pip install -r requirements.txt`.

## Think beyond

1. Asha's board works with `tabulate==0.9.0`. A new version comes out. How could she try it safely without breaking the cafe laptop? Think about a second environment and your tests from Chapter 19.
2. An AI suggests a package called `cafe-weather-easy` that does everything her board needs. List the checks you would make on its pypi.org page before you install it, and what result of each check would make you stop.

## Recap

- A virtual environment is a folder, usually `.venv`, with its own Python and packages for one project.
- Create it with `python -m venv .venv`, activate it, and look for `(.venv)` in the prompt. Type `deactivate` to leave.
- Install with `python -m pip install`, and list what is installed with `python -m pip list`.
- `requirements.txt` records pinned versions with `==`. `pip install -r` installs them on another computer.
- Check every package name on pypi.org before you install it. A look-alike name is a warning sign.
- Never install a package name from an AI before you check it.

You earned **100 XP** and the **Toolsmith** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 25, Boss Level 5, you will build the Data Report Generator: a tool that reads a data file, handles bad data and writes a clear report.
