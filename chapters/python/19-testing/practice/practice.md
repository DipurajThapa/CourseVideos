# Practice: Chapter 19

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but every check should pass in the same way.

## Warm-up (10 XP each)

### Task 1: Assert it

**Goal:** Write a function `double(number)` that returns the number times 2. Add three `assert` lines that check 4, 0 and -3, then print a message.

**Run it:**
```bash
python solutions/task1.py
```

**Expected output:**
```text
All checks passed
```

**Hint:** An `assert` with a true condition does nothing, so the message prints only if every check passes.

**AI variant:** Ask an AI assistant for two more inputs to check `double()` with. Work out each expected result yourself before you add it.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: A message that helps

**Goal:** Write `cups_left(cups, sold)` and two assertions, each with a message after the comma that says what should happen.

**Run it:**
```bash
python solutions/task2.py
```

**Expected output:**
```text
Both checks passed
```

**Hint:** The message appears only when the assertion fails. Change one expected value to see it, then change it back.

**AI variant:** Ask an AI assistant to improve your two messages. Check that each message still names the input and the expected result.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Your first pytest file

**Goal:** Write `minutes_to_hours(minutes)` and two `pytest` tests in the same file: 120 minutes and 30 minutes. Run the file with `pytest`.

**Run it:**
```bash
python -m pytest -q solutions/task3.py
```

**Expected output:**
```text
..                                               [100%]
2 passed in 0.01s
```

**Hint:** Start every test function name with `test_`. When you give `pytest` the file name, as in the command above, it runs that file even if the name does not start with `test_`.

**AI variant:** Ask an AI assistant why `120 / 60` gives `2.0` and why the test `== 2` still passes. Check the answer by running the test.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Edge cases for free teas

**Goal:** A customer earns one free tea for every 10 cups. Write `free_teas(cups)` and four tests: 0, 9, 10 and 25 cups.

**Run it:**
```bash
python -m pytest -q solutions/task4.py
```

**Expected output:**
```text
....                                             [100%]
4 passed in 0.01s
```

**Hint:** Floor division `//` from Chapter 2 counts whole groups of 10.

**AI variant:** Ask an AI assistant for the edge cases of this rule. Did it include 9 and 10? Add any case it found that you missed.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Decimals that pass

**Goal:** Write `order_total(prices)` that returns the sum of a list of prices. Test it with `[0.1, 0.2]` using `round()`, and with `[1.1, 2.2]` using `pytest.approx()`.

**Run it:**
```bash
python -m pytest -q solutions/task5.py
```

**Expected output:**
```text
..                                               [100%]
2 passed in 0.01s
```

**Hint:** Add `import pytest` at the top of the file to use `pytest.approx()`.

**AI variant:** Ask an AI assistant to write the exact test `order_total([0.1, 0.2]) == 0.3`. Run it, and explain the failure.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Test first

**Goal:** Write three tests first for `loyalty_level(points)`: 100 points is Gold, 50 is Silver and 49 is Bronze. Run them and watch them fail. Then write the function with `if`, `elif` and `else`.

**Run it:**
```bash
python -m pytest -q solutions/task6.py
```

**Expected output:**
```text
...                                              [100%]
3 passed in 0.01s
```

**Hint:** Before the function exists, write a placeholder that returns an empty string, so the tests run and fail.

**AI variant:** Ask an AI assistant for the function after your tests are written. Run your tests on its code before you accept it.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Break it on purpose

**Goal:** Write `seats_needed(guests, per_table=4)` that returns how many tables the guests need, without the `math` module. Write three tests. Then make a broken copy that uses `guests // per_table` and check that at least one test fails on it.

**Run it:**
```bash
python -m pytest -q solutions/task7.py
```

**Expected output:**
```text
...                                              [100%]
3 passed in 0.01s
```

**Hint:** Adding `per_table - 1` before the floor division rounds up for every positive number of guests.

**AI variant:** Ask an AI assistant whether your three tests are enough. Check its answer with your broken copy.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's tests

**Goal:** An AI assistant wrote these tests for `tip(total, percent=10)`: `test_ten_percent` calls `tip(40)` with no `assert`, and `test_decimal_bill` checks `tip(12.3) == 1.23` exactly. Write the function and three correct tests.

**Run it:**
```bash
python -m pytest -q solutions/task8.py
```

**Expected output:**
```text
...                                              [100%]
3 passed in 0.01s
```

**Hint:** A test needs an `assert` with an exact expected value. For decimals, use `pytest.approx()`.

**AI variant:** Show the AI its own two tests and ask why each one is weak. Did it name the missing `assert` and the exact decimal comparison?

**Solution:** [solutions/task8.py](solutions/task8.py)
