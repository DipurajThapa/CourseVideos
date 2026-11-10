# Chapter 19: Testing Your Code: assert and pytest

> Quest: turn Asha's quick checks into real tests that stop loudly when something breaks, and check that an AI's tests can really fail. Reward: 100 XP and the **Quality Guard** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write an `assert` statement, with a message, that stops a program when a check fails.
- Write a test file for `pytest` and run it from the terminal.
- Read a `pytest` report and find the test, the line and the values that failed.
- Choose edge cases for a function, and test decimal results with `round()` or `pytest.approx()`.
- Check that tests written by an AI can really fail, by breaking the code on purpose.

## Why this matters

In Chapter 18, Asha's module checked itself with lines that print `True`. If a change made one of them print `False`, the program carried on, and nobody noticed.

A **test** is a small piece of code that runs your code with a known input and checks the result against the answer you expect. If the result is wrong, the test fails loudly.

Tests prove that code works today, and they keep it working tomorrow. Every time you, a colleague or an AI assistant changes the code, you run the tests again. Professional teams run thousands of tests before every change goes live.

## The idea

Every test has the same three parts.

```text
  known input        run the code          compare
  boxes for 40  -->  boxes_needed(40)  -->  is it 4?
                                            yes: pass   no: FAIL
```

There are three ways to check a result, from weakest to strongest.

| Check | What happens when the result is wrong |
|---|---|
| `print(result == 4)` | It prints `False`, and the program carries on. |
| `assert result == 4` | The program stops with an `AssertionError`. |
| A `pytest` test | `pytest` runs every test, then reports each failure by name, line and value. |

Think of a test as a smoke alarm in the cafe kitchen. It stays quiet while everything is fine, and it makes a loud noise the moment something goes wrong. The comparison stops working at one point: a smoke alarm checks every room, but a test checks only the inputs you wrote. An input you never tested can still give a wrong answer.

## Build it step by step

**Step 1: See why a printed check is not enough.** Someone typed `1.01` instead of `1.1` as the tax rate.

```python
# file: examples/ex01_print_checks.py
def with_tax(price, rate=1.01):
    return round(price * rate, 2)

print(with_tax(3.5) == 3.85)
print("Report saved")
```

<!-- output: examples/ex01_print_checks.expected -->
```output
False
Report saved
```

Line 5 prints `False`, but line 6 still saves the report. A printed check only helps if somebody reads it.

**Step 2: Stop the program with `assert`.** An **assertion** is a statement that a condition must be true. If it is true, `assert` does nothing. If it is false, Python stops with an `AssertionError`.

```python
# file: examples/ex02_assert_pass.py
def with_tax(price, rate=1.1):
    return round(price * rate, 2)

assert with_tax(3.5) == 3.85
assert with_tax(4.0) == 4.4
print("Report saved")
```

<!-- output: examples/ex02_assert_pass.expected -->
```output
Report saved
```

Both checks pass, so the assertions stay silent. Now the same check with the wrong tax rate. After the comma, you can add a message that explains what went wrong.

```python
# file: examples/ex03_assert_fail.py
def with_tax(price, rate=1.01):
    return round(price * rate, 2)

assert with_tax(3.5) == 3.85, "tea with tax should be 3.85"
print("Report saved")
```

<!-- error: examples/ex03_assert_fail.expected_error -->
```output
Traceback (most recent call last):
  File "ex03_assert_fail.py", line 5, in <module>
    assert with_tax(3.5) == 3.85, "tea with tax should be 3.85"
           ^^^^^^^^^^^^^^^^^^^^^
AssertionError: tea with tax should be 3.85
```

The report is never saved, because line 5 stopped the program. The message tells you exactly which value was wrong.

**Step 3: Write your first `pytest` file.** `pytest` is a popular testing tool for Python. It is not part of the standard library, so you install it once with `pip`. That is the package installer that comes with Python.

```bash
python -m pip install -U pytest
```

On macOS and Linux, type `python3` instead of `python`. You will learn more about installing packages in Chapter 24.

Here is Asha's module from Chapter 18, with `boxes_needed()` added to it. She removes the old printed checks at the bottom of the file, because tests will replace them.

```python
# file: examples/cafe_tools.py
"""Small tools for the Corner Cafe programs."""
import math


def with_tax(price, rate=1.1):
    """Return the price with tax, rounded to cents."""
    return round(price * rate, 2)


def money(amount):
    """Return an amount as text with two decimal places."""
    return f"{amount:.2f}"


def boxes_needed(biscuits, per_box=12):
    """Return how many boxes hold the biscuits."""
    return math.ceil(biscuits / per_box)
```

The safe rule for names has two parts. Each test is a function whose name starts with `test_`, and the file name starts with `test_` too. When you give `pytest` a folder instead of a file, it looks for file names that start with `test_` or end with `_test.py`. Inside each test, a plain `assert` does the checking.

```python
# file: examples/test_cafe_tools.py
from cafe_tools import with_tax, money, boxes_needed


def test_tea_with_tax():
    assert with_tax(3.5) == 3.85


def test_money_has_two_decimals():
    assert money(4) == "4.00"


def test_boxes_for_40_biscuits():
    assert boxes_needed(40) == 4
```

Run it from the folder that holds both files. The `-q` option asks for a short, quiet report.

```bash
python -m pytest -q test_cafe_tools.py
```

<!-- output: examples/test_cafe_tools.expected -->
```output
...                                              [100%]
3 passed in 0.01s
```

Each dot is one passing test. The last line counts them and shows how long the run took. The time changes on every run.

**Step 4: Read a failure.** To see what a failure looks like, Asha copies both files into a folder called `broken`. In the copy, she changes line 18 of the module to use `round()`. That is the mistake an AI made in Chapter 18.

```python
# file: examples/broken/cafe_tools.py
"""Small tools for the Corner Cafe programs."""
import math


def with_tax(price, rate=1.1):
    """Return the price with tax, rounded to cents."""
    return round(price * rate, 2)


def money(amount):
    """Return an amount as text with two decimal places."""
    return f"{amount:.2f}"


def boxes_needed(biscuits, per_box=12):
    """Return how many boxes hold the biscuits."""
    return round(biscuits / per_box)
```

She runs the same tests on the broken copy. The option `--tb=short` keeps the report short.

```bash
python -m pytest -q --tb=short test_cafe_tools.py
```

<!-- output: examples/broken/test_cafe_tools.expected -->
```output
..F                                              [100%]
======================= FAILURES =======================
______________ test_boxes_for_40_biscuits ______________
test_cafe_tools.py:14: in test_boxes_for_40_biscuits
    assert boxes_needed(40) == 4
E   assert 3 == 4
E    +  where 3 = boxes_needed(40)
=============== short test summary info ================
FAILED test_cafe_tools.py::test_boxes_for_40_biscuits
1 failed, 2 passed in 0.01s
```

Read the report from the top. The `F` in the first line is the failing test. The report names the test, `test_boxes_for_40_biscuits`, and its line, 14. The line starting with `E` shows the values: the function returned 3, but the test expected 4. The other two tests still passed.

**Step 5: Test the edge cases.** An **edge case** is an unusual input at the limit of what a function must handle. For `boxes_needed()`, the edges are no biscuits, exactly one full box, and one biscuit more than a box.

```python
# file: examples/test_edges.py
from cafe_tools import boxes_needed


def test_no_biscuits():
    assert boxes_needed(0) == 0


def test_exactly_one_box():
    assert boxes_needed(12) == 1


def test_one_more_than_a_box():
    assert boxes_needed(13) == 2
```

<!-- output: examples/test_edges.expected -->
```output
...                                              [100%]
3 passed in 0.01s
```

On the broken copy, only the last edge case fails, because `round()` turns 13 divided by 12 into 1.

<!-- output: examples/broken/test_edges.expected -->
```output
..F                                              [100%]
======================= FAILURES =======================
_______________ test_one_more_than_a_box _______________
test_edges.py:14: in test_one_more_than_a_box
    assert boxes_needed(13) == 2
E   assert 1 == 2
E    +  where 1 = boxes_needed(13)
=============== short test summary info ================
FAILED test_edges.py::test_one_more_than_a_box - asse...
1 failed, 2 passed in 0.01s
```

The test for 40 biscuits and the test for 13 biscuits catch the same mistake from different sides. Good tests cover normal values and edge values.

**Step 6: Test decimal results safely.** In Chapter 2, you saw that `0.1 + 0.1 + 0.1` is not exactly `0.3`. A test that compares decimals exactly can fail even when the code is right.

```python
# file: examples/test_floats.py
import pytest


def test_exact():
    total = 0.1 * 3
    assert total == 0.3


def test_rounded():
    total = 0.1 * 3
    assert round(total, 2) == 0.3


def test_approx():
    total = 0.1 * 3
    assert total == pytest.approx(0.3)
```

<!-- output: examples/test_floats.expected -->
```output
F..                                              [100%]
======================= FAILURES =======================
______________________ test_exact ______________________
test_floats.py:7: in test_exact
    assert total == 0.3
E   assert 0.30000000000000004 == 0.3
=============== short test summary info ================
FAILED test_floats.py::test_exact - assert 0.30000000...
1 failed, 2 passed in 0.01s
```

The first test fails, because the total is a tiny bit more than 0.3: `0.30000000000000004`. The second test rounds the result to two decimal places first. The third uses `pytest.approx()`, which accepts a value that is very close to the expected one.

**Step 7: Write the test first.** The cafe owner wants every price label to start with `USD`. Before Asha changes `money()`, she writes the test for the new rule.

```python
# file: examples/testfirst/test_money_usd.py
from cafe_tools import money


def test_money_shows_usd():
    assert money(4) == "USD 4.00"
```

She runs it on her current module, and it fails, as expected.

<!-- output: examples/testfirst/test_money_usd.expected -->
```output
F                                                [100%]
======================= FAILURES =======================
_________________ test_money_shows_usd _________________
test_money_usd.py:6: in test_money_shows_usd
    assert money(4) == "USD 4.00"
E   AssertionError: assert '4.00' == 'USD 4.00'
E
E     - USD 4.00
E     + 4.00
=============== short test summary info ================
FAILED test_money_usd.py::test_money_shows_usd - Asse...
1 failed in 0.01s
```

The `-` line shows what the test expected and the `+` line shows what the function returned. Now she changes line 13 of `cafe_tools.py` and runs the test again. It passes.

```python
# file: examples/final/test_money_usd.py
from cafe_tools import money


def test_money_shows_usd():
    assert money(4) == "USD 4.00"
```

<!-- output: examples/final/test_money_usd.expected -->
```output
.                                                [100%]
1 passed in 0.01s
```

Writing the test first is called **test-first thinking**. A test that fails before the change and passes after it proves that the change really did the job.

One more run is needed. Asha's test file from Step 3 still expects `"4.00"`, so it now fails on the new module.

<!-- output: examples/usd/test_cafe_tools.expected -->
```output
.F.                                              [100%]
======================= FAILURES =======================
_____________ test_money_has_two_decimals ______________
test_cafe_tools.py:10: in test_money_has_two_decimals
    assert money(4) == "4.00"
E   AssertionError: assert 'USD 4.00' == '4.00'
E
E     - 4.00
E     + USD 4.00
=============== short test summary info ================
FAILED test_cafe_tools.py::test_money_has_two_decimals
1 failed, 2 passed in 0.01s
```

The rule changed on purpose, so the old test is out of date. Asha updates it to expect `"USD 4.00"`. When a rule changes, its tests change with it.

## See the outcome

Here is Asha's finished module, with the `USD` rule.

```python
# file: examples/final/cafe_tools.py
"""Small tools for the Corner Cafe programs."""
import math


def with_tax(price, rate=1.1):
    """Return the price with tax, rounded to cents."""
    return round(price * rate, 2)


def money(amount):
    """Return an amount as text, such as USD 4.00."""
    return f"USD {amount:.2f}"


def boxes_needed(biscuits, per_box=12):
    """Return how many boxes hold the biscuits."""
    return math.ceil(biscuits / per_box)
```

And here is her complete test file. Two of the tests check several values each.

```python
# file: examples/final/test_cafe_tools.py
from cafe_tools import with_tax, money, boxes_needed


def test_tea_with_tax():
    assert with_tax(3.5) == 3.85


def test_two_items():
    total = with_tax(1.0) + with_tax(2.0)
    assert round(total, 2) == 3.3


def test_money_shows_usd():
    assert money(4) == "USD 4.00"


def test_boxes_full_and_part():
    assert boxes_needed(24) == 2
    assert boxes_needed(40) == 4


def test_boxes_edges():
    assert boxes_needed(0) == 0
    assert boxes_needed(12) == 1
    assert boxes_needed(13) == 2
```

```bash
python -m pytest -q test_cafe_tools.py
```

<!-- output: examples/final/test_cafe_tools.expected -->
```output
.....                                            [100%]
5 passed in 0.01s
```

Five tests pass. From now on, after every change to `cafe_tools.py`, Asha runs this one command. If any tool breaks, a test fails and names it.

## Work with AI

The AI skill for this chapter is checking AI tests. An AI assistant can write many tests very quickly. But a test that can never fail looks exactly like a test that passes. Your job is to check that each test really tests the right behaviour.

The safety habits still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Ask AI to list the behaviours and edge cases to test, with the expected result for each, before any code. |
| Write | Write a few tests yourself first. Then ask AI for its tests and compare. |
| Generate | Ask AI for a `pytest` file with one behaviour per test and an exact expected value in every `assert`. |
| Test | Break a copy of your code on purpose and run the AI's tests on it. Good tests fail. |
| Debug | Paste the failing test and the `pytest` report. Ask whether the code or the test is wrong, and why. |
| Improve | Ask AI to review your tests. Before you delete any test, check which mistake it catches. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha asked an AI assistant: "Write pytest tests for my cafe_tools module. They must catch any mistake in boxes_needed." The AI answered with this file. It said: "These tests will catch any mistake in `boxes_needed`."

```python
# file: examples/ai/test_ai_tools.py
from cafe_tools import with_tax, boxes_needed


def test_tax():
    assert with_tax(3.5) == 3.85


def test_boxes():
    result = boxes_needed(24)
    assert result == 2


def test_zero():
    boxes_needed(0)
```

Asha ran them on her module, and all three passed.

<!-- output: examples/ai/test_ai_tools.expected -->
```output
...                                              [100%]
3 passed in 0.01s
```

That looks good, but it proves nothing yet. Asha made a broken copy of her finished module, with `round()` on line 18, as in Step 4. She ran the same tests on it.

<!-- output: examples/ai/broken/test_ai_tools.expected -->
```output
...                                              [100%]
3 passed in 0.01s
```

All three still pass, so these tests cannot catch the `round()` mistake. The test for 24 biscuits divides exactly, so `round()` gives the right answer too. The test for 0 biscuits has no `assert` at all, so it can never fail. Asha's own test for 40 biscuits does fail on the broken copy.

Asha asked for a better file, with exact expected values, normal cases and the edge cases from her plan. After one fix to a decimal comparison, the AI's file looked like this.

```python
# file: examples/ai/test_ai_v2.py
from cafe_tools import with_tax, money, boxes_needed


def test_tax():
    assert with_tax(3.5) == 3.85


def test_two_items():
    total = with_tax(1.0) + with_tax(2.0)
    assert round(total, 2) == 3.3


def test_money():
    assert money(4) == "USD 4.00"


def test_full_boxes():
    assert boxes_needed(24) == 2


def test_part_box():
    assert boxes_needed(40) == 4


def test_zero():
    assert boxes_needed(0) == 0


def test_just_over():
    assert boxes_needed(13) == 2
```

<!-- output: examples/ai/test_ai_v2.expected -->
```output
.......                                          [100%]
7 passed in 0.01s
```

On the broken copy, two of these tests now fail, as they should.

<!-- output: examples/ai/broken/test_ai_v2.expected -->
```output
....F.F                                          [100%]
=============== short test summary info ================
FAILED test_ai_v2.py::test_part_box - assert 3 == 4
FAILED test_ai_v2.py::test_just_over - assert 1 == 2
2 failed, 5 passed in 0.01s
```

A quick rule catches this kind of flaw: break the code on purpose, then run the tests. A good test fails on broken code.

## Common mistakes

**Mistake 1: a test function without the `test_` prefix.** `pytest` only runs functions whose names start with `test_`.

```python
# file: examples/err01_no_prefix.py
from cafe_tools import with_tax


def tea_tax():
    assert with_tax(3.5) == 3.85
```

<!-- error: examples/err01_no_prefix.expected_error -->
```output
no tests ran in 0.01s
```

Fix: rename the function to `test_tea_tax`. If `pytest` says "no tests ran", check the names first.

**Mistake 2: a test with no `assert`.** A test that only calls a function, like `test_zero` in the AI pair moment, always passes. Fix: every test needs an `assert` with an exact expected value.

**Mistake 3: comparing decimals exactly.** As Step 6 showed, `0.1 * 3 == 0.3` is `False`. Fix: round the result to two decimal places, or use `pytest.approx()`.

**Mistake 4: forgetting to import the function you test.**

```python
# file: examples/err02_missing_import.py
from cafe_tools import with_tax


def test_boxes():
    assert boxes_needed(40) == 4
```

<!-- error: examples/err02_missing_import.expected_error -->
```output
F                                                [100%]
======================= FAILURES =======================
______________________ test_boxes ______________________
err02_missing_import.py:6: in test_boxes
    assert boxes_needed(40) == 4
           ^^^^^^^^^^^^
E   NameError: name 'boxes_needed' is not defined
=============== short test summary info ================
FAILED err02_missing_import.py::test_boxes - NameErro...
1 failed in 0.01s
```

Fix: add `boxes_needed` to the import on line 2. The report points at line 6 of the test file, not at the module. A `NameError` inside a test means the test itself is wrong, not the code it tests.

## Think beyond

1. With the finished module, `money(-2)` returns `"USD -2.00"`. Should a refund be shown like that? Write a test for the label you would want, run it, and decide whether the test or the code should change.
2. You have ten tests and they all pass. How could you find out whether they would catch a mistake in `with_tax()`? Try it with a broken copy.

## Recap

- A test runs code with a known input and compares the result with the answer you expect.
- `assert condition, "message"` stops the program with an `AssertionError` when the condition is false.
- `pytest` runs every function whose name starts with `test_` in a file whose name starts with `test_`, and reports each failure by name, line and value.
- Test normal values and edge cases. Compare decimals with `round()` or `pytest.approx()`.
- Write the test first: it fails before the change and passes after it.
- Break a copy of the code on purpose to check that tests, including AI tests, can really fail.

You earned **100 XP** and the **Quality Guard** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 20, the Boss Level, you will build a quiz app from several modules, and write its tests first.
