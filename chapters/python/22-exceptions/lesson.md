# Chapter 22: Handling Errors: try, except and Clear Messages

> Quest: make the Corner Cafe's score board survive a missing file and a damaged row, and give every problem a clear message instead of a crash. Reward: 100 XP and the **Safety Net** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Catch an error with `try` and `except`, and show a clear message instead of a crash.
- Use `else` for the code that runs when nothing went wrong, and `finally` for the code that always runs.
- Catch the specific error you expect, and explain why a bare `except:` hides bugs.
- Raise your own error with a clear message, and test it with `pytest.raises`.
- Ask an AI assistant what could go wrong in your code, then handle and test each case.

## Why this matters

At the end of Chapter 21, Asha's score board still had a weak spot. If `scores.csv` was missing, or one row said `three` instead of `3`, the program stopped with a long error report. The staff saw a wall of red text and no way forward.

An **exception** is an error that happens while a program runs, such as `ValueError` or `FileNotFoundError`. You have read many exception reports since Chapter 9. In this chapter, your program catches them and decides what to do.

Every real program meets bad data: a customer types "two" instead of 2, a file was deleted, a network is down. Good programs expect these problems, say clearly what happened, and carry on when they can.

## The idea

A `try` block runs code that might fail. If an exception happens inside it, Python stops that block and jumps to a matching `except` block.

```text
  try:                       runs first
      score = int(answer)    if this fails ...
  except ValueError:         ... Python jumps here
      print("Please type a whole number.")
  else:                      runs only if nothing failed
      print("Saved.")
  finally:                   runs always, at the end
      print("Done.")
```

The `except` line names the exception it catches. An exception of another type is not caught, and the program stops as before.

| Part | When it runs |
|---|---|
| `try` | Always first. It stops at the first exception. |
| `except ValueError:` | Only when a `ValueError` happened in `try`. |
| `else` | Only when `try` finished with no exception. |
| `finally` | Always, last, even after an exception that was not caught. |

Think of a safety net under a trapeze. The act goes on as planned, and the net catches the artist only after a fall. The comparison stops working at one point: a real net catches anyone, but `except` catches only the type of error it names.

## Build it step by step

**Step 1: Catch a bad number.** In Chapter 4, `int("two")` stopped the program with a `ValueError`. Here the same mistake gives a message instead.

```python
# file: examples/ex01_try_except.py
answers = ["4", "four", " 3 "]
for answer in answers:
    try:
        score = int(answer)
        print(f"Saved score: {score}")
    except ValueError:
        print(f"Not a whole number: {answer!r}")
```

<!-- output: examples/ex01_try_except.expected -->
```output
Saved score: 4
Not a whole number: 'four'
Saved score: 3
```

When `int("four")` fails, line 6 never runs: Python jumps straight to line 8. The loop then goes on with the next answer. `int()` ignores the spaces around `" 3 "`, as you saw in Chapter 4. `!r`, from Chapter 20, shows the value with its quotation marks.

**Step 2: Add else and finally.** Loading a file can fail with `FileNotFoundError`. `else` holds the code that needs the file, and `finally` holds the code that must run either way.

```python
# file: examples/ex02_else_finally.py
from pathlib import Path


def load(name):
    try:
        text = Path(name).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"{name}: no scores yet")
    else:
        print(text, end="")
    finally:
        print(f"{name}: done")


load("week.csv")
load("month.csv")
```

<!-- output: examples/ex02_else_finally.expected -->
```output
name,score
Asha,4
Omar,3
week.csv: done
month.csv: no scores yet
month.csv: done
```

`week.csv` exists, so `else` prints it. `month.csv` does not exist, so `except` prints a message and `else` is skipped. `finally` runs both times. Keep the `try` block small: only the line that can fail belongs inside it.

**Step 3: Ask again until the answer is valid.** In Chapter 7, a `while True` loop asked until the answer was valid. With `try` inside the loop, a word no longer crashes it.

```python
# file: examples/ex03_ask_again.py
while True:
    answer = input("Score (0 to 4): ")
    try:
        score = int(answer)
    except ValueError:
        print("Please type a whole number, like 3.")
    else:
        if score >= 0 and score <= 4:
            break
        print("Please type a number from 0 to 4.")
print(f"Saved: {score}")
```

The user types `four`, then `7`, then `3`:

<!-- output: examples/ex03_ask_again.expected -->
```output
Score (0 to 4): four
Please type a whole number, like 3.
Score (0 to 4): 7
Please type a number from 0 to 4.
Score (0 to 4): 3
Saved: 3
```

`7` is a whole number, so no exception happens, but it is still not a valid score. `try` catches the wrong type of answer, and `if` catches the wrong value. Each message says what to type next.

**Step 4: Raise your own error.** A function can refuse bad input with `raise`. It creates an exception with a message and stops the function.

```python
# file: examples/ex04_raise.py
def with_tax(price):
    if price < 0:
        raise ValueError(f"price cannot be negative: {price}")
    return round(price * 1.1, 2)


print(with_tax(3.5))
try:
    print(with_tax(-1))
except ValueError as error:
    print(f"Not saved: {error}")
```

<!-- output: examples/ex04_raise.expected -->
```output
3.85
Not saved: price cannot be negative: -1
```

`except ValueError as error:` keeps the exception in the name `error`, so line 12 can show its message. A clear message names the problem and the value. Compare "price cannot be negative: -1" with "Error!": only the first one helps someone fix the input.

**Step 5: Catch the error you expect.** A bare `except:` catches every exception, including the ones that come from your own bugs. Line 5 has a spelling mistake: `anser` instead of `answer`.

```python
# file: examples/ex05_bare_except.py
answers = ["4", "four"]
for answer in answers:
    try:
        score = int(anser)
        print(f"Saved score: {score}")
    except:
        print("Please type a whole number.")
```

<!-- output: examples/ex05_bare_except.expected -->
```output
Please type a whole number.
Please type a whole number.
```

Even `"4"` is refused, and nothing tells you why. The `NameError` from the spelling mistake was caught and hidden. Now the same code catches only `ValueError`:

```python
# file: examples/ex06_specific.py
answers = ["4", "four"]
for answer in answers:
    try:
        score = int(anser)
        print(f"Saved score: {score}")
    except ValueError:
        print("Please type a whole number.")
```

<!-- error: examples/ex06_specific.expected_error -->
```output
Traceback (most recent call last):
  File "ex06_specific.py", line 5, in <module>
    score = int(anser)
                ^^^^^
NameError: name 'anser' is not defined. Did you mean: 'answer'?
```

The bug is no longer hidden: the report names line 5 and even suggests the right name. Catch the exceptions you expect from the data. Let the others stop the program, so you can find and fix them. A bare `except:` even catches Ctrl+C, the keys you press to stop a program.

**Step 6: Test that an error is raised.** In Chapter 19, tests checked return values. `pytest.raises` checks that a function raises an exception. Asha keeps `with_tax()` in her `cafe_tools` module.

```python
# file: examples/cafe_tools.py
def with_tax(price):
    """Return the price with 10 percent tax, rounded to cents."""
    if price < 0:
        raise ValueError(f"price cannot be negative: {price}")
    return round(price * 1.1, 2)
```

```python
# file: examples/test_errors.py
import pytest
from cafe_tools import with_tax


def test_tea_price():
    assert with_tax(3.5) == 3.85


def test_negative_price_is_refused():
    with pytest.raises(ValueError):
        with_tax(-1)
```

<!-- output: examples/test_errors.expected -->
```output
..                                               [100%]
2 passed in 0.01s
```

The test passes only if the indented line raises a `ValueError`. If the function forgets to raise, the test fails. This older `with_tax()` has no check.

```python
# file: examples/test_errors_missing.py
import pytest


def with_tax(price):
    return round(price * 1.1, 2)


def test_negative_price_is_refused():
    with pytest.raises(ValueError):
        with_tax(-1)
```

<!-- error: examples/test_errors_missing.expected_error -->
```output
F                                                [100%]
======================= FAILURES =======================
____________ test_negative_price_is_refused ____________
test_errors_missing.py:10: in test_negative_price_is_refused
    with pytest.raises(ValueError):
         ^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: DID NOT RAISE ValueError
=============== short test summary info ================
FAILED test_errors_missing.py::test_negative_price_is_refused
1 failed in 0.01s
```

The report says "DID NOT RAISE ValueError". It means the function returned a value when it should have refused the input.

## See the outcome

Asha's score board now loads `scores.csv` without crashing. One row is damaged:

```text
name,score
Asha,4
Omar,three
Lina,4
```

```python
# file: examples/ex07_score_board.py
import csv

loaded = 0
try:
    with open("scores.csv", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                score = int(row["score"])
            except ValueError:
                print(f"Skipped {row['name']}: {row['score']!r} is not a score")
            else:
                print(f"{row['name']:<6}{score} of 4")
                loaded += 1
except FileNotFoundError:
    print("No scores yet. Play a round first.")
print(f"Scores loaded: {loaded}")
```

<!-- output: examples/ex07_score_board.expected -->
```output
Asha  4 of 4
Skipped Omar: 'three' is not a score
Lina  4 of 4
Scores loaded: 2
```

The inner `try` protects one row at a time, so the damaged row is skipped and Lina still loads. The outer `try` handles a missing file. Each message names the problem and the value, so Asha knows exactly which row to correct.

## Work with AI

The AI skill for this chapter is asking an AI assistant to list what could go wrong in your code. Then you decide how to handle each case, and test it. An AI list is a starting point: check every case with a real run.

Never paste private data into an AI tool. A real score file with staff names is private, so paste a small made-up sample.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Ask what could go wrong when the code runs, and what the program should do in each case. |
| Write | Write your own error handling first, then ask the AI to check which cases it covers. |
| Generate | Ask for code that names the exceptions it catches and keeps each `try` block small. |
| Test | Make one test file for each problem, write the expected result, and run every case. |
| Debug | Paste the code and the full error report. Ask for the cause before the fix. |
| Improve | Ask for one improvement, then check it would not hide a bug, and run every test again. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha asked an AI assistant: "Write load_scores(path) that reads a score file and returns a list of (name, score). It must never crash, and it must skip a damaged row." The AI said its function handles every problem.

```python
# file: examples/ai_load_flawed.py
import csv


def load_scores(path):
    scores = []
    try:
        with open(path, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                scores.append((row["name"], int(row["score"])))
    except:
        pass
    return scores


if __name__ == "__main__":
    print(load_scores("case_damaged.csv"))
```

<!-- output: examples/ai_load_flawed.expected -->
```output
[('Asha', 4)]
```

Lina is missing, with no message. The `try` block holds the whole loop, so the damaged row stopped the loop, and the bare `except:` with `pass` hid what happened. Asha's test cases caught it:

<!-- output: examples/ai_tests_flawed.expected -->
```output
Normal: found 2, expected 2: pass
Damaged row: found 1, expected 2: FAIL
Header only: found 0, expected 0: pass
```

The fixed function puts a small `try` around one row, catches `ValueError` only, and gives a message for a missing file.

```python
# file: examples/ai_load_fixed.py
import csv


def load_scores(path):
    scores = []
    try:
        with open(path, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    scores.append((row["name"], int(row["score"])))
                except ValueError:
                    print(f"Skipped {row['name']}: not a score")
    except FileNotFoundError:
        print(f"{path} not found: starting with no scores")
    return scores
```

<!-- output: examples/ai_tests_fixed.expected -->
```output
Normal: found 2, expected 2: pass
Skipped Omar: not a score
Damaged row: found 2, expected 2: pass
Header only: found 0, expected 0: pass
```

Then Asha found a gap that her own version had too. In a new test file, one row says only `Ben`, with no comma. `DictReader` gives that row no score, so `row["score"]` is `None`, and `int(None)` raises a `TypeError`. The fix catches both exceptions as a **tuple**: the names inside round brackets, like the tuples in Chapter 13.

```python
# file: examples/ai_load_final.py
import csv


def load_scores(path):
    scores = []
    try:
        with open(path, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    scores.append((row["name"], int(row["score"])))
                except (ValueError, TypeError):
                    print(f"Skipped {row['name']}: not a score")
    except FileNotFoundError:
        print(f"{path} not found: starting with no scores")
    return scores
```

She added the short row as a fourth test case and ran every case again:

<!-- output: examples/ai_tests_final.expected -->
```output
Normal: found 2, expected 2: pass
Skipped Omar: not a score
Damaged row: found 2, expected 2: pass
Header only: found 0, expected 0: pass
Skipped Ben: not a score
Short row: found 2, expected 2: pass
```

Later, the AI suggested `except Exception:` "so no future error can crash it". `Exception` is the parent of almost every exception type, so it catches nearly every error. Asha tested the idea with a deliberate spelling mistake, `row["scor"]`, and the broad version skipped every row with a wrong message. A specific `except` lets that `KeyError` stop the program and point at the line, so she kept it.

## Common mistakes

**Mistake 1: catching the wrong exception type.** `int("four")` raises `ValueError`, not `TypeError`.

```python
# file: examples/err01_wrong_type.py
answer = "four"
try:
    score = int(answer)
except TypeError:
    print("Please type a whole number.")
```

<!-- error: examples/err01_wrong_type.expected_error -->
```output
Traceback (most recent call last):
  File "err01_wrong_type.py", line 4, in <module>
    score = int(answer)
ValueError: invalid literal for int() with base 10: 'four'
```

Fix: catch the type that the error report names, `except ValueError:`. Run the code once without `try` to see which exception it raises.

**Mistake 2: using a name that the try block never created.**

```python
# file: examples/err02_unset.py
answer = "four"
try:
    score = int(answer)
except ValueError:
    print("Not a whole number.")
print(score + 1)
```

<!-- error: examples/err02_unset.expected_error -->
```output
Not a whole number.
Traceback (most recent call last):
  File "err02_unset.py", line 7, in <module>
    print(score + 1)
          ^^^^^
NameError: name 'score' is not defined
```

`int(answer)` failed, so `score` was never created. Fix: put the code that needs `score` in `else`, or give `score` a value in the `except` block.

**Mistake 3: a try with no except or finally.**

```python
# file: examples/err03_no_except.py
try:
    score = int("4")
print(score)
```

<!-- error: examples/err03_no_except.expected_error -->
```output
  File "err03_no_except.py", line 4
    print(score)
    ^^^^^
SyntaxError: expected 'except' or 'finally' block
```

Fix: every `try` needs at least one `except` or a `finally` block straight after it.

**Mistake 4: raising a string.**

```python
# file: examples/err04_raise_text.py
price = -1
if price < 0:
    raise "price cannot be negative"
```

<!-- error: examples/err04_raise_text.expected_error -->
```output
Traceback (most recent call last):
  File "err04_raise_text.py", line 4, in <module>
    raise "price cannot be negative"
TypeError: exceptions must derive from BaseException
```

`raise` needs an exception, not text. Fix: put the message inside an exception, `raise ValueError("price cannot be negative")`.

## Think beyond

1. A customer types "3.5" for the number of teas. Which line of `ex03_ask_again.py` handles it, and what message do they see? How would you change the message so it says that only whole teas can be ordered?
2. Asha's score board skips damaged rows. When would it be better to stop the whole program instead of skipping a row? Think about a file of bank payments.

## Recap

- An exception is an error while the program runs. `try` and `except` catch it and let you show a clear message.
- `else` runs when nothing went wrong, and `finally` runs always.
- Catch the specific exception you expect. A bare `except:` also hides your own bugs, such as a spelling mistake.
- Keep each `try` block small, so one bad row does not stop the rest.
- `raise ValueError("message")` refuses bad input. A clear message names the problem and the value.
- `pytest.raises` tests that a function raises the exception it should.

You earned **100 XP** and the **Safety Net** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 23, you will save structured data as JSON and read data that other programs send, such as a weather service.
