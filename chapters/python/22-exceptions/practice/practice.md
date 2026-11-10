# Practice: Chapter 22

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match. Work in a folder with a copy of `prices.csv` from `solutions/`.

## Warm-up (10 XP each)

### Task 1: Count the cups safely

**Goal:** Loop over the entries `"12"`, `"twelve"` and `"7"`. Turn each one into an `int` and print it. When an entry is not a whole number, print a message that shows the entry, instead of crashing.

**Run it:**
```bash
python task1.py
```

**Expected output:**
```text
Cups: 12
'twelve' is not a number of cups
Cups: 7
```

**Hint:** Put only the `int()` line and the line that uses its result inside `try`. Catch `ValueError`.

**AI variant:** Ask an AI assistant which exception `int("twelve")` raises. Run it without `try` to check the answer.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: The missing special

**Goal:** Read today's special from `special.txt` with `Path.read_text()`. The file does not exist yet, so print "No special today." instead of crashing. When the file exists, print "Today's special: " and its text.

**Run it:**
```bash
python task2.py
```

**Expected output:**
```text
No special today.
```

**Hint:** Catch `FileNotFoundError`, and put the line that prints the special in `else`.

**AI variant:** Ask an AI assistant what changes if you create `special.txt` with "Carrot cake" in it. Create the file and check its answer.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: A total that always prints

**Goal:** Add the prices `"3.50"`, `"4.20"` and `"free"` with `float()`. Stop at the bad price with a message, and use `finally` so the total so far is always printed.

**Run it:**
```bash
python task3.py
```

**Expected output:**
```text
Stopped at a bad price: 'free'
Total so far: 7.70
```

**Hint:** Here the whole loop is inside `try`, so the loop stops at the first bad price. That is what this task wants.

**AI variant:** Ask an AI assistant to change the program so it skips the bad price and keeps adding. Check that it moves `try` inside the loop.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Ask again for the teas

**Goal:** Ask "How many teas (1 to 10)? " until the answer is a whole number from 1 to 10. A word and a number outside the range each get their own clear message.

**Run it:** type `two`, then `0`, then `3`.
```bash
python task4.py
```

**Expected output:**
```text
How many teas (1 to 10)? two
Please type a whole number, like 2.
How many teas (1 to 10)? 0
Please type a number from 1 to 10.
How many teas (1 to 10)? 3
Order: 3 teas
```

**Hint:** Use `while True`, with `try` and `except ValueError` inside it. Check the range in `else`, and `break` when the answer is valid.

**AI variant:** Ask an AI assistant for three more answers that could break your program. Type each one and check the message.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Refuse an empty order

**Goal:** Write `order_total(quantity, price)`. It raises `ValueError` with a clear message when `quantity` is less than 1. Call it with 2 and with 0, and catch the error with `except ValueError as error`.

**Run it:**
```bash
python task5.py
```

**Expected output:**
```text
Total: 7.00
Order refused: quantity must be at least 1, not 0
```

**Hint:** Put the value into the message with an f-string, so the reader sees what was wrong.

**AI variant:** Ask an AI assistant to make your error message clearer. Keep its suggestion only if it still names the value.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Total the good prices

**Goal:** `prices.csv` has a damaged row. Read it with `csv.DictReader`, skip the row whose price is not a number with a message, and print the total of the good prices.

```text
item,price
Tea,3.50
Scone,two
Cake,4.25
```

**Run it:**
```bash
python task6.py
```

**Expected output:**
```text
Skipped Scone: 'two' is not a price
Total of good prices: 7.75
```

**Hint:** Put a small `try` around the `float()` line inside the loop, so the loop goes on after the bad row.

**AI variant:** Ask an AI assistant what happens if the file is missing. Rename your copy of the file to check.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Test the refusal

**Goal:** Put `order_total()` from Task 5 in a file with three pytest tests: two teas cost 7.0, a quantity of 0 raises `ValueError`, and a quantity of -1 raises `ValueError`.

**Run it:**
```bash
python -m pytest -q solutions/task7.py
```

**Expected output:**
```text
...                                              [100%]
3 passed in 0.01s
```

**Hint:** `with pytest.raises(ValueError):` followed by an indented call passes only if the call raises.

**AI variant:** Ask an AI assistant to write the tests. Then remove the `raise` line from your function and check that both refusal tests fail.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's menu loader

**Goal:** An AI assistant wrote `load_menu(path)` with one `try` around the whole loop and `except: pass`. A damaged row made it lose every item after it, with no message. Write `load_menu(path)` that returns a dictionary of good prices, skips a damaged row with a message, and handles a missing file.

**Run it:**
```bash
python task8.py
```

**Expected output:**
```text
Skipped Scone: not a price
{'Tea': 3.5, 'Cake': 4.25}
old_prices.csv not found: the menu is empty
{}
```

**Hint:** Use two `try` blocks: a small one around one row, and an outer one for `FileNotFoundError`. Catch named exceptions only.

**AI variant:** Show the AI its own function and your test results. Ask it to explain why Cake was lost, then compare its fix with yours.

**Solution:** [solutions/task8.py](solutions/task8.py)
