# Chapter 18: Modules and the Standard Library

> Quest: move your tools into their own file, import them into any program, and use Python's ready-made modules for maths, time and file names. Reward: 100 XP and the **Librarian** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Import a module in three ways: `import math`, `from math import ceil` and `import math as m`.
- Write your own module, import it into two programs, and protect its test lines with `if __name__ == "__main__":`.
- Use `math`, `datetime` and `pathlib` from the standard library to round up, add times and read file names.
- Check an AI's suggested module or function in the official documentation, then run it.
- Fix the errors that beginners meet with imports.

## Why this matters

At the end of Chapter 17, Asha's `with_tax()` function was good. But every new program at the Corner Cafe needed it, so she copied it again and again. If she finds a bug, she must fix every copy.

A **module** is a Python file whose functions other programs can use. You write `with_tax()` once, in one file, and every program imports it. Fix it once, and every program gets the fix.

Python also comes with a large set of modules that are already written and tested. This set is called the **standard library**. You met one module in Chapter 10: `random`. Professional programmers reuse modules like these instead of writing everything themselves.

## The idea

**Importing** is the action that makes a module's functions available in your program. Python finds the module file, runs it once, and gives you a name for it.

```text
 cafe_tools.py               day_report.py
+------------------+        +------------------------------+
| def with_tax()   | <----- | import cafe_tools            |
| def money()      |        | cafe_tools.with_tax(4.0)     |
+------------------+        +------------------------------+
   written once               used here, and in any other
                              program in the same folder
```

There are three common ways to import:

| You write | Then you call | Use it when |
|---|---|---|
| `import math` | `math.ceil(2.1)` | You want to see where each function comes from. |
| `from math import ceil` | `ceil(2.1)` | You use one or two functions often. |
| `import math as m` | `m.ceil(2.1)` | The module name is long and you want a short one. |

Think of a module as a toolbox on a shelf. `import` takes the whole box to your table; you still say which tool you want, as in `math.ceil`. The comparison stops working at one point: Python reads the whole module file when it imports it, so any `print()` at the bottom of that file runs too.

## Build it step by step

**Step 1: Import a standard module.** Asha orders biscuits in boxes of 12. She needs 40 biscuits. The `math` module has functions for rounding up and down.

```python
# file: examples/ex01_import_math.py
import math

biscuits = 40
per_box = 12
print(biscuits / per_box)
print(math.ceil(biscuits / per_box))
print(math.floor(biscuits / per_box))
print(math.sqrt(49))
```

<!-- output: examples/ex01_import_math.expected -->
```output
3.3333333333333335
4
3
7.0
```

`math.ceil()` rounds up to the next whole number, so Asha orders 4 boxes. `math.floor()` rounds down. `math.sqrt()` gives the square root. The dot means "the `ceil` function that lives in the `math` module".

**Step 2: Three ways to import.** All three lines below call the same function.

```python
# file: examples/ex02_import_forms.py
import math
from math import ceil
import math as m

print(math.ceil(2.1))
print(ceil(2.1))
print(m.ceil(2.1))
```

<!-- output: examples/ex02_import_forms.expected -->
```output
3
3
3
```

`from math import ceil` brings only `ceil` into your program, so you call it without `math.` in front. `import math as m` gives the module a shorter name, an **alias**. Use one style per program, so readers are not confused.

**Step 3: Write your own module.** Asha moves her tools into a file called `cafe_tools.py`. The name of a module is its file name without `.py`.

```python
# file: examples/cafe_tools.py
"""Small tools for the Corner Cafe programs."""

def with_tax(price, rate=1.1):
    """Return the price with tax, rounded to cents."""
    return round(price * rate, 2)

def money(amount):
    """Return an amount as text with two decimal places."""
    return f"{amount:.2f}"

if __name__ == "__main__":
    print("Checking cafe_tools")
    print(with_tax(3.5) == 3.85)
    print(money(4) == "4.00")
```

When you run `cafe_tools.py` itself, it checks its own tools:

<!-- output: examples/cafe_tools.expected -->
```output
Checking cafe_tools
True
True
```

Python gives every file a variable called `__name__`. When you run the file directly, `__name__` is `"__main__"`. When another program imports it, `__name__` is the module's name, `"cafe_tools"`. So the three check lines run only when Asha runs the module herself, never when another program imports it.

Now a program in the same folder imports the module:

```python
# file: examples/ex03_use_tools.py
import cafe_tools

price = cafe_tools.with_tax(4.0)
print(price)
print(cafe_tools.money(price))
```

<!-- output: examples/ex03_use_tools.expected -->
```output
4.4
4.40
```

The check lines did not appear, because the guard skipped them. A second program can use `from ... import` instead:

```python
# file: examples/ex04_from_tools.py
from cafe_tools import with_tax, money

for price in [3.5, 4.0, 2.75]:
    print(money(with_tax(price)))
```

<!-- output: examples/ex04_from_tools.expected -->
```output
3.85
4.40
3.03
```

Python looks for `cafe_tools.py` in the same folder as the program you run. Keep your module next to the programs that import it.

**Step 4: Add times with `datetime`.** The cafe opens 8 hours after midnight and stays open for 9 hours and 30 minutes. A `timedelta` is a length of time.

```python
# file: examples/ex05_hours.py
from datetime import timedelta

opens = timedelta(hours=8)
open_for = timedelta(hours=9, minutes=30)
closes = opens + open_for
print("Closes at", closes)
print("Minutes open:", open_for.total_seconds() / 60)
```

<!-- output: examples/ex05_hours.expected -->
```output
Closes at 17:30:00
Minutes open: 570.0
```

You can add two lengths of time, and Python carries the minutes into hours for you. `total_seconds()` returns the length in seconds, so dividing by 60 gives minutes.

**Step 5: Read file names with `pathlib`.** In Chapter 21 you will save reports to files. First, `pathlib` helps you build and read file names without touching any file.

```python
# file: examples/ex06_paths.py
from pathlib import Path

report = Path("reports") / "monday.txt"
print(report.name)
print(report.stem)
print(report.suffix)
print(report.as_posix())
```

<!-- output: examples/ex06_paths.expected -->
```output
monday.txt
monday
.txt
reports/monday.txt
```

A **path** is the address of a file: its folders and its name. The `/` operator joins parts of a path. `name` is the file name, `stem` is the name without the ending, and `suffix` is the ending. Windows writes paths with backslashes, so `as_posix()` shows the path with forward slashes on every system.

## See the outcome

Here is Asha's day report. It imports her own module and three standard modules.

```python
# file: examples/ex07_day_report.py
import math
from datetime import timedelta
from pathlib import Path
from cafe_tools import with_tax, money

sales = [3.5, 4.0, 2.75]
total = sum([with_tax(price) for price in sales])
boxes = math.ceil(40 / 12)
closes = timedelta(hours=8) + timedelta(hours=9, minutes=30)
report = Path("reports") / "monday.txt"

print("Total:", money(total))
print("Biscuit boxes:", boxes)
print("Closes at", closes)
print("Saved as", report.as_posix())
```

<!-- output: examples/ex07_day_report.expected -->
```output
Total: 11.28
Biscuit boxes: 4
Closes at 17:30:00
Saved as reports/monday.txt
```

Lines 2 to 5 put all the imports at the top, which is the PEP 8 style. The program has no copy of `with_tax()`. If Asha changes the tax rate in `cafe_tools.py`, this report and every other program that imports it change too. Line 11 builds the file name only; it does not save a file yet.

## Work with AI

The AI skill for this chapter is asking an AI assistant which standard module fits a task, then confirming the answer in the official documentation at docs.python.org. AI assistants sometimes name functions that do not exist. The documentation and a real run decide.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe the task and ask which standard module and function fit. Then find that function in the official documentation. |
| Write | Write your own version first. Then compare it with a version that uses the module, on several inputs. |
| Generate | Ask for a function for your own module, with a docstring and the exact output for an example call. |
| Test | Write test cases with expected results. Run them before and after every fix. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask for one improvement. Check every function it names in the documentation before you run it. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha wants a `boxes_needed()` function for her module: biscuits come in boxes of 12, and she always rounds up. First she wrote her own version without any module:

```python
# file: examples/ai_own_boxes.py
def boxes_needed(biscuits, per_box=12):
    """Return how many boxes to order."""
    return biscuits // per_box + 1

print(boxes_needed(40))
```

<!-- output: examples/ai_own_boxes.expected -->
```output
4
```

An AI assistant told her that `math.ceil()` fits the task, and she found it in the documentation of the `math` module. The AI said her version and a `math.ceil()` version give the same answer for every number of biscuits. Asha tested two numbers:

```python
# file: examples/ai_compare_boxes.py
import math

for biscuits in [40, 24]:
    mine = biscuits // 12 + 1
    with_ceil = math.ceil(biscuits / 12)
    print(biscuits, "biscuits:", mine, with_ceil)
```

<!-- output: examples/ai_compare_boxes.expected -->
```output
40 biscuits: 4 4
24 biscuits: 3 2
```

The AI was wrong. For 24 biscuits, her version orders 3 boxes when 2 are enough. Then she asked the AI to write the function for her module. It wrote this and said it rounds up:

```python
# file: examples/ai_boxes_flawed.py
def boxes_needed(biscuits, per_box=12):
    """Return how many boxes to order, rounded up."""
    return round(biscuits / per_box)

print(boxes_needed(40))
```

<!-- output: examples/ai_boxes_flawed.expected -->
```output
3
```

`round()` goes to the nearest whole number, so 3.33 becomes 3, and Asha is short of biscuits. Her test cases show the problem:

```python
# file: examples/ai_boxes_tests_flawed.py
def boxes_needed(biscuits, per_box=12):
    return round(biscuits / per_box)

cases = {40: 4, 24: 2, 1: 1, 0: 0}
for biscuits, expected in cases.items():
    result = boxes_needed(biscuits)
    check = "pass" if result == expected else "FAIL"
    print(biscuits, "->", result, check)
```

<!-- output: examples/ai_boxes_tests_flawed.expected -->
```output
40 -> 3 FAIL
24 -> 2 pass
1 -> 0 FAIL
0 -> 0 pass
```

With `math.ceil()` and its import, every case passes:

```python
# file: examples/ai_boxes_tests_fixed.py
import math

def boxes_needed(biscuits, per_box=12):
    return math.ceil(biscuits / per_box)

cases = {40: 4, 24: 2, 1: 1, 0: 0}
for biscuits, expected in cases.items():
    result = boxes_needed(biscuits)
    check = "pass" if result == expected else "FAIL"
    print(biscuits, "->", result, check)
```

<!-- output: examples/ai_boxes_tests_fixed.expected -->
```output
40 -> 4 pass
24 -> 2 pass
1 -> 1 pass
0 -> 0 pass
```

Later, the AI suggested `math.ceildiv(40, 12)` as a shorter way. Asha searched the documentation of the `math` module and found no such function. A run agrees:

```python
# file: examples/ai_ceildiv.py
import math

print(math.ceildiv(40, 12))
```

<!-- error: examples/ai_ceildiv.expected_error -->
```output
Traceback (most recent call last):
  File "ai_ceildiv.py", line 4, in <module>
    print(math.ceildiv(40, 12))
          ^^^^^^^^^^^^
AttributeError: module 'math' has no attribute 'ceildiv'
```

An `AttributeError` here means the module has no function with that name. Check every function an AI names in the official documentation before you build on it.

## Common mistakes

**Mistake 1: a typing error in the module name.** Python looks for a file with exactly that name.

```python
# file: examples/err01_module_typo.py
import cafe_tool

print(cafe_tool.money(4))
```

<!-- error: examples/err01_module_typo.expected_error -->
```output
Traceback (most recent call last):
  File "err01_module_typo.py", line 2, in <module>
    import cafe_tool
ModuleNotFoundError: No module named 'cafe_tool'
```

Fix: spell the module name like its file, `cafe_tools`, and keep the file in the same folder as your program. Newer versions of Python add a suggestion such as `Did you mean: 'cafe_tools'?`.

**Mistake 2: calling a function without its module name.** After `import math`, the function's full name is `math.ceil`.

```python
# file: examples/err02_no_prefix.py
import math

print(ceil(2.1))
```

<!-- error: examples/err02_no_prefix.expected_error -->
```output
Traceback (most recent call last):
  File "err02_no_prefix.py", line 4, in <module>
    print(ceil(2.1))
          ^^^^
NameError: name 'ceil' is not defined
```

Fix: write `math.ceil(2.1)`, or import it with `from math import ceil`.

**Mistake 3: naming your own file like a standard module.** Asha saved a test file as `random.py` in the folder of her game. Now `import random` finds her file first, not Python's module.

```python
# file: examples/shadow/random.py
print("Asha's random test file")
```

```python
# file: examples/shadow/err03_shadow.py
import random

print(random.randint(1, 20))
```

<!-- error: examples/shadow/err03_shadow.expected_error -->
```output
Asha's random test file
Traceback (most recent call last):
  File "err03_shadow.py", line 4, in <module>
    print(random.randint(1, 20))
          ^^^^^^^^^^^^^^
AttributeError: module 'random' has no attribute 'randint' (consider renaming 'random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
```

The first output line shows that Python ran her file. Fix: rename the file, for example to `random_test.py`. Python 3.13 and newer add the "consider renaming" advice, with the full path of the file.

**Mistake 4: test lines without the guard.** This module prints a test line at the bottom, with no `if __name__ == "__main__":`.

```python
# file: examples/noguard/menu_tools.py
def money(amount):
    return f"{amount:.2f}"

print("Test:", money(4))
```

```python
# file: examples/noguard/ex08_no_guard.py
from menu_tools import money

print("Tea:", money(3.5))
```

<!-- output: examples/noguard/ex08_no_guard.expected -->
```output
Test: 4.00
Tea: 3.50
```

There is no error, but the test line appears in every program that imports the module, because importing runs the whole file. Fix: put test lines under `if __name__ == "__main__":`.

## Think beyond

1. Asha wants to pick a random winner from a list of customer names. Which function of the `random` module fits? Ask an AI assistant, then find the function in the official documentation and run it.
2. Asha has two folders of programs, and both need `cafe_tools.py`. What happens if she copies the module into both folders and later fixes a bug in one copy? What does that tell you about where a shared module should live?

## Recap

- A module is a Python file whose functions other programs can import. The standard library is the set of modules that comes with Python.
- `import math` keeps the module name in front, `from math import ceil` brings one function in, and `import math as m` gives the module an alias.
- Your own module lives in the same folder as the programs that import it. Importing runs the whole file once.
- `if __name__ == "__main__":` keeps test lines from running when the file is imported.
- `math.ceil()` rounds up, `timedelta` adds lengths of time, and `Path` builds and reads file names.
- When an AI names a module or function, find it in the official documentation and run it before you trust it.

You earned **100 XP** and the **Librarian** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 19, you will turn Asha's quick checks into real tests with `assert` and `pytest`, so you know your modules still work after every change.
