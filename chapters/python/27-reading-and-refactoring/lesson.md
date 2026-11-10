# Chapter 27: Reading and Improving Code with AI

> Quest: read a program someone else wrote, pin down what it does with tests, and improve it in small, safe steps with an AI assistant. Reward: 100 XP and the **Code Reviewer** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Read an unfamiliar program from the top, and trace one input through it.
- Write characterization tests that record what a program does now.
- Refactor in small steps: rename, replace magic numbers, extract a function, and run the tests after each step.
- Read a unified diff and find the changed line that can change a result.
- Review an AI assistant's refactoring with your tests before you accept it.

## Why this matters

Most programming work is changing code that already exists. That code was often written by someone else, or by an AI assistant. It may have short names, no comments and no tests, and it still has to keep working.

**Refactoring** means changing the structure of code without changing what it does. A clearer program is easier to fix and to extend. But every change can break something, so you need a way to prove that the behaviour stayed the same. In this chapter, that proof is a set of tests that you write before you change anything.

At the Corner Cafe, Asha has found the old till code. Sam, who helped before her, wrote it in a hurry. It works, but nobody can read it.

## The idea

A safe refactoring loop has four parts, and you go round it once for every small change.

```text
  1. Tests first        record what the code does now
          |
  2. One small change   rename, a constant, a new function
          |
  3. Run the tests      same results?  yes -> keep it
          |                            no  -> undo it
  4. Review             read the change, then repeat
```

A **characterization test** is a test that records what a program does now, even the odd parts. It does not ask whether the result is right. It asks whether the result is the same as before. If you want to change a behaviour, that is a separate change, made on purpose, after the refactoring.

A **diff** shows two versions of a file side by side, line by line. Lines that start with `-` were removed, and lines that start with `+` were added. Lines that start with a space did not change.

Think of refactoring like rearranging a cafe kitchen. The shelves move, but every recipe must taste the same afterwards. The comparison stops working at one point: in code, you can check every "recipe" automatically with tests, every time you move a shelf.

## Build it step by step

**Step 1: Read from the top, and trace one input.** Here is Sam's till code. Before you change anything, read it from the first line to the last, and say in words what each part does.

```python
# file: examples/till_old.py
def f(a, b):
    t = 0
    for x in a:
        t = t + x[1] * x[2]
    if b:
        t = t - t * 0.1
    t2 = t * 1.1
    return round(t2, 2)


if __name__ == "__main__":
    o = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]
    print(f(o, False))
    print(f(o, True))
    print(f([], True))
```

<!-- output: examples/till_old.expected -->
```output
12.38
11.14
0.0
```

Line 2 defines `f`, which takes a list `a` and a value `b`. Lines 4 and 5 go through the list. Each item is a tuple, so `x[1]` and `x[2]` are its second and third values. Line 6 checks `b`, and line 7 takes 10 percent off. Line 8 adds tax, and line 9 rounds the result. So `a` is an order of (name, price, count) tuples, and `b` says whether the customer is a member.

To check your reading, trace one input. Print the running total inside the loop, as in Chapter 9:

```python
# file: examples/ex02_trace.py
from till_old import f

o = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]
t = 0
for x in o:
    t = t + x[1] * x[2]
    print(x[0], x[1], x[2], "t =", t)
print("Result:", f(o, False))
```

<!-- output: examples/ex02_trace.expected -->
```output
Tea 3.5 2 t = 7.0
Cake 4.25 1 t = 11.25
Result: 12.38
```

Two teas at 3.5 make 7.0, and one cake makes 11.25. With tax, the result is 12.38. Your reading of the code was right.

**Step 2: Write characterization tests.** Now record what `f` does today, before any change. Use the three results from Step 1, including the odd one: an empty order gives `0.0`.

```python
# file: examples/test_till_old.py
from till_old import f

ORDER = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]


def test_normal_order():
    assert f(ORDER, False) == 12.38


def test_member_order():
    assert f(ORDER, True) == 11.14


def test_empty_order():
    assert f([], True) == 0.0
```

<!-- output: examples/test_till_old.expected -->
```output
...                                              [100%]
3 passed in 0.01s
```

All three pass, because they describe the program as it is. From now on, any change that breaks one of them has changed the behaviour.

**Step 3: Rename for the reader.** The first change is the names. `f` becomes `order_total`, `a` becomes `items` and `b` becomes `is_member`. Line 4 unpacks each tuple into `name, price, count`, which you learned in Chapter 13, so `x[1]` and `x[2]` disappear.

```python
# file: examples/till_v2.py
def order_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + price * count
    if is_member:
        total = total - total * 0.1
    with_tax = total * 1.1
    return round(with_tax, 2)
```

The tests change in one way only: they call the new name. The expected values stay exactly the same.

```python
# file: examples/test_till_v2.py
from till_v2 import order_total

ORDER = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]


def test_normal_order():
    assert order_total(ORDER, False) == 12.38


def test_member_order():
    assert order_total(ORDER, True) == 11.14


def test_empty_order():
    assert order_total([], True) == 0.0
```

<!-- output: examples/test_till_v2.expected -->
```output
...                                              [100%]
3 passed in 0.01s
```

**Step 4: Replace magic numbers with constants, and read the diff.** A **magic number** is a number in the code with no name, such as `0.1` or `1.1`. A reader cannot tell what it means. A constant gives it a name. In Python, constants are written in capital letters at the top of the file.

```python
# file: examples/till_v3.py
MEMBER_DISCOUNT = 0.1
TAX_RATE = 1.1


def order_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + price * count
    if is_member:
        total = total - total * MEMBER_DISCOUNT
    with_tax = total * TAX_RATE
    return round(with_tax, 2)
```

<!-- output: examples/test_till_v3.expected -->
```output
...                                              [100%]
3 passed in 0.01s
```

The `difflib` module in the standard library shows the difference between two versions. This program compares Step 3 with Step 4, and skips the first line of each file, the `# file:` comment.

```python
# file: examples/ex05_diff.py
import difflib
from pathlib import Path

old = Path("till_v2.py").read_text(encoding="utf-8")
new = Path("till_v3.py").read_text(encoding="utf-8")
old_lines = old.splitlines()[1:]
new_lines = new.splitlines()[1:]
diff = difflib.unified_diff(old_lines, new_lines, "v2", "v3",
                            lineterm="", n=1)
for line in diff:
    print(line)
```

<!-- output: examples/ex05_diff.expected -->
```output
--- v2
+++ v3
@@ -1 +1,5 @@
+MEMBER_DISCOUNT = 0.1
+TAX_RATE = 1.1
+
+
 def order_total(items, is_member):
@@ -5,4 +9,4 @@
     if is_member:
-        total = total - total * 0.1
-    with_tax = total * 1.1
+        total = total - total * MEMBER_DISCOUNT
+    with_tax = total * TAX_RATE
     return round(with_tax, 2)
```

The two `---` and `+++` lines name the old and the new version. Each `@@` line says where a group of changes starts. Here, the `+` lines add the two constants, and the `-` and `+` pairs swap `0.1` and `1.1` for their names. Every other line is unchanged.

## See the outcome

Step 5 extracts a function. The loop that adds up the order becomes its own function, `subtotal`, with a docstring. Here is the finished till module.

```python
# file: examples/till_final.py
"""Order totals for the Corner Cafe till."""
MEMBER_DISCOUNT = 0.1
TAX_RATE = 1.1


def subtotal(items):
    """Return the price of every item times its count, added up."""
    total = 0
    for name, price, count in items:
        total = total + price * count
    return total


def order_total(items, is_member):
    """Return the total to pay, with the member discount and tax."""
    total = subtotal(items)
    if is_member:
        total = total - total * MEMBER_DISCOUNT
    return round(total * TAX_RATE, 2)
```

The tests pass on the final version too.

<!-- output: examples/test_till_final.expected -->
```output
...                                              [100%]
3 passed in 0.01s
```

To be sure, Asha runs Sam's old function and her new one side by side, on three orders, with and without the member discount:

```python
# file: examples/ex07_same.py
from till_old import f
from till_final import order_total

orders = [[("Tea", 3.5, 2), ("Cake", 4.25, 1)], [("Juice", 2.75, 3)], []]
for order in orders:
    for member in [False, True]:
        old = f(order, member)
        new = order_total(order, member)
        print(old, new, old == new)
```

<!-- output: examples/ex07_same.expected -->
```output
12.38 12.38 True
11.14 11.14 True
9.08 9.08 True
8.17 8.17 True
0.0 0.0 True
0.0 0.0 True
```

Every pair is equal. The code is easier to read, and it does exactly what Sam's code did.

## Work with AI

The AI skill for this chapter is a safe refactoring loop with an AI assistant: tests first, then the AI's suggestion, then your review, then the tests again. An AI can read unfamiliar code quickly, but it can also explain it wrongly or change its behaviour while it "tidies" it. Never accept an explanation or a change that you have not checked with a real run.

Never paste private data into an AI tool. Use made-up stock numbers and names, not a real supplier's data.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Ask the AI to explain the code, without changing it. Check every claim with a run. |
| Write | Write your own characterization tests first, including the edge cases. |
| Generate | Ask for one refactoring that keeps the behaviour. Read the change as a diff. |
| Test | Run your tests on the AI's version. A failing test means the behaviour changed. |
| Debug | Paste the code and the full error report. Ask for the cause before the fix. |
| Improve | Ask for one more improvement, then run every test again before you accept it. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Sam also left a stock checker with very short names:

```python
# file: examples/stock_old.py
def chk(s, o):
    r = []
    for k in o:
        if s[k] - o[k] < 3:
            r.append(k)
    return r
```

Asha asked an AI assistant: "Explain what this function does. Do not change it." The AI answered that `chk` returns the items that will run out after an order. Asha checked the claim with a run:

```python
# file: examples/ai_explain_check.py
from stock_old import chk

stock = {"Tea": 10, "Cake": 4, "Scone": 5}
order = {"Tea": 2, "Cake": 2, "Scone": 2}
print(chk(stock, order))
for item in order:
    print(item, "left:", stock[item] - order[item])
```

<!-- output: examples/ai_explain_check.expected -->
```output
['Cake']
Tea left: 8
Cake left: 2
Scone left: 3
```

Cake has 2 left, so it has not run out, but it is in the list. Scone has exactly 3 left, and it is not. So `chk` returns the items that will have fewer than 3 left. The AI's explanation was close, but wrong. Asha wrote her own tests first, with the boundary case of exactly 3 left:

```python
# file: examples/test_stock.py
from stock_old import chk

STOCK = {"Tea": 10, "Cake": 4, "Scone": 5}


def test_plenty_left():
    assert chk(STOCK, {"Tea": 2}) == []


def test_exactly_three_left():
    assert chk(STOCK, {"Scone": 2}) == []


def test_two_left():
    assert chk(STOCK, {"Cake": 2}) == ["Cake"]


def test_keeps_order_of_the_order():
    order = {"Scone": 3, "Cake": 3}
    assert chk(STOCK, order) == ["Scone", "Cake"]


def test_empty_order():
    assert chk(STOCK, {}) == []
```

<!-- output: examples/test_stock.expected -->
```output
.....                                            [100%]
5 passed in 0.01s
```

Then she asked: "Refactor this function with clear names. Keep the behaviour exactly the same." The AI answered with this version and said the behaviour was the same:

```python
# file: examples/stock_ai.py
LOW_LIMIT = 3


def low_stock(stock, order):
    low = []
    for item in order:
        if stock[item] - order[item] <= LOW_LIMIT:
            low.append(item)
    return low
```

Because the name changed, the diff shows every line as changed. Asha read it carefully:

```python
# file: examples/ai_diff.py
import difflib
from pathlib import Path

old = Path("stock_old.py").read_text(encoding="utf-8")
new = Path("stock_ai.py").read_text(encoding="utf-8")
old_lines = old.splitlines()[1:]
new_lines = new.splitlines()[1:]
diff = difflib.unified_diff(old_lines, new_lines, "old", "ai",
                            lineterm="", n=0)
for line in diff:
    print(line)
```

<!-- output: examples/ai_diff.expected -->
```output
--- old
+++ ai
@@ -1,6 +1,9 @@
-def chk(s, o):
-    r = []
-    for k in o:
-        if s[k] - o[k] < 3:
-            r.append(k)
-    return r
+LOW_LIMIT = 3
+
+
+def low_stock(stock, order):
+    low = []
+    for item in order:
+        if stock[item] - order[item] <= LOW_LIMIT:
+            low.append(item)
+    return low
```

The old line says `< 3` and the new line says `<= LOW_LIMIT`. With `<=`, an item with exactly 3 left now counts as low. Her tests, pointed at the AI's function, show it:

```python
# file: examples/test_stock_ai.py
from stock_ai import low_stock as chk

STOCK = {"Tea": 10, "Cake": 4, "Scone": 5}


def test_plenty_left():
    assert chk(STOCK, {"Tea": 2}) == []


def test_exactly_three_left():
    assert chk(STOCK, {"Scone": 2}) == []


def test_two_left():
    assert chk(STOCK, {"Cake": 2}) == ["Cake"]


def test_keeps_order_of_the_order():
    order = {"Scone": 3, "Cake": 3}
    assert chk(STOCK, order) == ["Scone", "Cake"]


def test_empty_order():
    assert chk(STOCK, {}) == []
```

<!-- output: examples/test_stock_ai.expected -->
```output
.F...                                            [100%]
=============== short test summary info ================
FAILED test_stock_ai.py::test_exactly_three_left - As...
1 failed, 4 passed in 0.01s
```

The test for exactly 3 left fails. The AI's refactoring changed the behaviour, and it sounded sure that it had not. Asha changed `<=` back to `<` and kept the clear names.

```python
# file: examples/stock_v2.py
LOW_LIMIT = 3


def low_stock(stock, order):
    low = []
    for item in order:
        if stock[item] - order[item] < LOW_LIMIT:
            low.append(item)
    return low
```

<!-- output: examples/test_stock_v2.expected -->
```output
.....                                            [100%]
5 passed in 0.01s
```

Then her daily report stopped working, because it still used the old name:

```python
# file: examples/ai_report_crash.py
from stock_v2 import chk

stock = {"Tea": 10, "Cake": 4}
print("Order more:", chk(stock, {"Cake": 2}))
```

<!-- error: examples/ai_report_crash.expected_error -->
```output
Traceback (most recent call last):
  File "ai_report_crash.py", line 2, in <module>
    from stock_v2 import chk
ImportError: cannot import name 'chk' from 'stock_v2'
```

Renaming a function breaks every program that uses the old name. Asha kept the old name as a second name for the same function, on the last line:

```python
# file: examples/stock_final.py
LOW_LIMIT = 3


def low_stock(stock, order):
    """Return the ordered items that will have fewer than 3 left."""
    low = []
    for item in order:
        if stock[item] - order[item] < LOW_LIMIT:
            low.append(item)
    return low


chk = low_stock  # the old name, for code that still uses it
```

<!-- output: examples/ai_report.expected -->
```output
Order more: ['Cake']
```

<!-- output: examples/test_stock_final.expected -->
```output
.....                                            [100%]
5 passed in 0.01s
```

Last, she asked the AI for one more improvement. It suggested a comprehension and `sorted()`, "so the list is tidier". Sorting was a new feature that nobody asked for, and her test for the order of the items caught it:

```python
# file: examples/stock_sorted.py
LOW_LIMIT = 3


def low_stock(stock, order):
    """Return the ordered items that will have fewer than 3 left."""
    low = [item for item in order
           if stock[item] - order[item] < LOW_LIMIT]
    return sorted(low)


chk = low_stock  # the old name, for code that still uses it
```

<!-- output: examples/test_stock_sorted.expected -->
```output
...F.                                            [100%]
=============== short test summary info ================
FAILED test_stock_sorted.py::test_keeps_order_of_the_order
1 failed, 4 passed in 0.01s
```

Asha kept `stock_final.py`. A refactoring that changes the output is not a refactoring.

## Common mistakes

**Mistake 1: tests that cover too few cases.** This "tidy" version rounds each line before the discount. It passes all three tests from Step 2, but a different order shows the change.

```python
# file: examples/err01_tidy_rounding.py
from till_old import f


def order_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + round(price * count * 1.1, 2)
    if is_member:
        total = total - total * 0.1
    return round(total, 2)


for teas in [2, 1]:
    order = [("Tea", 3.5, teas), ("Cake", 4.25, 1)]
    print(f(order, True), order_total(order, True))
```

<!-- output: examples/err01_tidy_rounding.expected -->
```output
11.14 11.14
7.67 7.68
```

With two teas both results are 11.14, but with one tea they are 7.67 and 7.68. Fix: test several different inputs, not only the one in the example, and never move rounding into a loop during a refactoring.

**Mistake 2: renaming a function, but not every call.** Python only knows the new name:

```python
# file: examples/err02_old_name.py
def order_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + price * count
    return total


print(f([("Tea", 3.5, 2)], False))
```

<!-- error: examples/err02_old_name.expected_error -->
```output
Traceback (most recent call last):
  File "err02_old_name.py", line 9, in <module>
    print(f([("Tea", 3.5, 2)], False))
          ^
NameError: name 'f' is not defined
```

Fix: change every call to the new name, or keep the old name as a second name, as Asha did with `chk = low_stock`.

**Mistake 3: an extracted function with no return.** When you move code into a new function, the result must come back out.

```python
# file: examples/err03_no_return.py
def subtotal(items):
    total = 0
    for name, price, count in items:
        total = total + price * count


def order_total(items):
    return round(subtotal(items) * 1.1, 2)


print(order_total([("Tea", 3.5, 2)]))
```

<!-- error: examples/err03_no_return.expected_error -->
```output
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
```

`subtotal` has no `return`, so it gives back `None`, and line 9 cannot multiply `None` by `1.1`. Fix: add `return total` at the end of `subtotal`, as in the finished till module.

**Mistake 4: changing a test to match new output.** This version forgot the member discount:

```python
# file: examples/err04_changed_test.py
from till_old import f


def tidy_total(items, is_member):
    total = 0
    for name, price, count in items:
        total = total + price * count
    return round(total * 1.1, 2)


order = [("Tea", 3.5, 2), ("Cake", 4.25, 1)]
print("Old:", f(order, True))
print("New:", tidy_total(order, True))
```

<!-- output: examples/err04_changed_test.expected -->
```output
Old: 11.14
New: 12.38
```

A test for the member order would now fail. It is tempting to change the expected value in the test from 11.14 to 12.38, so it passes. That hides the bug. Fix: during a refactoring, never change the expected values. A failing test means your change broke something, so undo the change and try a smaller one.

## Think beyond

1. Sam's code also has a function that adds up the day's sales and prints a report in the same loop. How would you split it into a function that calculates and one that prints, and which tests would you write first?
2. Sometimes refactoring is not worth it, for example code that will be deleted next week. What questions would you ask before you decide to refactor someone else's code?

## Recap

- Read unfamiliar code from the top, say what each part does, and trace one input to check your reading.
- A characterization test records what the code does now, even the odd parts. Write these tests before you change anything.
- Refactor in small steps: rename, replace magic numbers with constants, extract a function. Run the tests after every step.
- In a diff, `-` lines were removed and `+` lines were added. Look for the changed line that can change a result.
- An AI can explain code wrongly and change behaviour while it tidies. Check every claim with a run, and every change with your tests.

You earned **100 XP** and the **Code Reviewer** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 28, the Final Boss, you will build a complete personal task manager with an AI assistant, from the plan to the tests, the review and the improvements.
