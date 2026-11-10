# Practice: Chapter 27

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: Read before you run

**Goal:** Read this function without running it: `def g(p, n):` sets `r = 0`, then `for i in range(n): r = r + p`, then returns `r`. Write in one sentence what it does. Predict what `g(3.5, 2)` and `g(4.25, 0)` print, then run it.

**Run it:**
```bash
python task1.py
```

**Expected output:**
```text
7.0
0
```

**Hint:** Trace the loop for `g(3.5, 2)`. How many times does it run, and what is `r` after each pass? For `g(4.25, 0)`, does the loop run at all?

**AI variant:** Ask an AI assistant to explain what `g` does. Check each claim it makes with a run, including the `0` result.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Rename for the reader

**Goal:** Sam wrote `def a(b, c): return b * c`. Rename it to `line_total(price, count)`, and use it in a second function `line_text(name, price, count)` that returns text such as `Tea x2: 7.00`.

**Run it:**
```bash
python task2.py
```

**Expected output:**
```text
Tea x2: 7.00
Cake x1: 4.25
```

**Hint:** Use an f-string with `:.2f` from Chapter 3 for the price.

**AI variant:** Ask an AI assistant for three better names for `a`, `b` and `c`. Choose the ones a new helper would understand without asking you.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Record what a function does now

**Goal:** Sam's function `d(t, m)` returns `t - 2` when `m` is true and `t` is more than 20, and `t` otherwise. Write four `assert` lines that record what it does now, including `t` exactly 20. Print `All checks passed` at the end.

**Run it:**
```bash
python task3.py
```

**Expected output:**
```text
All checks passed
```

**Hint:** Test a member over 20, a non-member over 20, a member at exactly 20 and a member under 20.

**AI variant:** Ask an AI assistant which input your four checks do not cover. Run it and add a fifth check with the real result.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Name the magic numbers

**Goal:** A loyalty function returns `stamps // 10 * 3.5`. Replace `10` and `3.5` with constants called `STAMPS_FOR_FREE_TEA` and `FREE_TEA_PRICE`. Print the value for 9 stamps and for 25 stamps.

**Run it:**
```bash
python task4.py
```

**Expected output:**
```text
0.0
7.0
```

**Hint:** Constants go at the top of the file, in capital letters. The results must be the same before and after your change.

**AI variant:** Ask an AI assistant to find every magic number in a function of yours. Decide which ones need a name and which ones, such as `0`, are clear already.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Extract a function

**Goal:** A script prints two receipts with the same eight lines of code copied twice. Extract one function `receipt(customer, items)` that prints a receipt, and call it twice.

**Run it:**
```bash
python task5.py
```

**Expected output:**
```text
Receipt for Lina
  Tea     3.50
  Cake    4.25
  Total   7.75
Receipt for Omar
  Latte   3.85
  Total   3.85
```

**Hint:** The parts that are different in the two copies become the parameters. Use `:<6` and `:>6.2f` to line up the columns.

**AI variant:** Ask an AI assistant to extract the function for you. Run your old script and the new one, and compare every line of the output.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Read a diff

**Goal:** Use `difflib.unified_diff` to compare two versions of a three-line program, stored as two lists of strings. Show only the changed lines, with no lines of context.

**Run it:**
```bash
python task6.py
```

**Expected output:**
```text
--- old
+++ new
@@ -1 +1 @@
-price = 3.5
+TEA_PRICE = 3.5
@@ -3 +3 @@
-print(price * count)
+print(TEA_PRICE * count)
```

**Hint:** Pass `lineterm=""` and `n=0`, as in the lesson. Line 2 did not change, so it does not appear.

**AI variant:** Ask an AI assistant what each `@@` line means. Check its answer against your own diff output.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Refactor safely, with proof

**Goal:** Sam's `s(l)` adds up the positive numbers in a list and rounds the result. Write a clearer `day_sales(amounts)` with a docstring and a comprehension. Then run both on four lists, including an empty list and a list with a negative amount, and print both results and whether they are equal.

**Run it:**
```bash
python task7.py
```

**Expected output:**
```text
7.75 7.75 True
0 0 True
6.6 6.6 True
0.3 0.3 True
```

**Hint:** `sum()` of a comprehension with `if amount > 0` does the same job as the loop. The empty list must still give `0`.

**AI variant:** Ask an AI assistant for the shorter version. Run your four lists on it before you accept it.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's refactor

**Goal:** `can_seat(free_chairs, group)` returns `group <= free_chairs`. An AI "tidied" it to `group < free_chairs` and said nothing changed. Test both on four cases, find the case that fails, fix the AI's version and show that every case passes.

**Run it:**
```bash
python task8.py
```

**Expected output:**
```text
AI:    ['pass', 'FAIL', 'pass', 'pass']
Fixed: ['pass', 'pass', 'pass', 'pass']
```

**Hint:** Include a group that exactly fills the free chairs. That is the boundary.

**AI variant:** Show the AI its own version and your failing case. Ask it which line changed the behaviour, and check that it names the comparison.

**Solution:** [solutions/task8.py](solutions/task8.py)
