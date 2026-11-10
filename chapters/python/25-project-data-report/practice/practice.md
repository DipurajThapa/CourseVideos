# Practice: Chapter 25

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: Read one till file

**Goal:** Write a small CSV file with the columns `item` and `amount` and two rows. Read it back with `csv.DictReader`, and print each item and its amount.

**Expected output:**
```text
tea costs 3.50
cake costs 4.25
```

**Hint:** `Path.write_text()` writes the file in one line. Open it again with `newline=""`, as Chapter 21 taught.

**AI variant:** Ask an AI assistant what `DictReader` uses as the keys of each row. Check its answer by printing one row.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Number or not

**Goal:** For the texts `"2.75"`, `"two"` and `""`, try `float()`. Print the number, or a clear line when the text is not a number.

**Expected output:**
```text
'2.75' is 2.75
'two' is not a number
'' is not a number
```

**Hint:** Put only the `float()` line inside `try`, and print the number in `else`.

**AI variant:** Ask an AI assistant which exception `float("")` raises. Predict it, then run it.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Money with a currency

**Goal:** Write `money(amount, currency)` that returns text such as `EUR 7.50`. Take the currency from a settings dictionary.

**Expected output:**
```text
EUR 7.50
EUR 12.00
```

**Hint:** The format code `:.2f` always shows two decimal places, as in Chapter 3.

**AI variant:** Ask an AI assistant for a test for `money()`. Check that the test would fail if the function printed only one decimal place.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Count the bad rows

**Goal:** Add up the amounts in the list `["3.50", "four", "2.75", "", "5.00"]`. Skip each text that is not a number, and count it.

**Expected output:**
```text
Total: 11.25
Bad rows: 2
```

**Hint:** Start with `total, bad = 0, 0`. Add 1 to `bad` in the `except` block.

**AI variant:** Ask an AI assistant to write this with `except Exception`. Then add a spelling mistake inside the `try` block, and see what each version reports.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Totals per item

**Goal:** From a list of `(item, amount)` pairs, build a dictionary of totals per item, and print it as a neat table.

**Expected output:**
```text
tea     7.00
cake    4.25
soup    5.00
```

**Hint:** `items.get(item, 0) + amount` starts each new item at 0, as `build_week()` does.

**AI variant:** Ask an AI assistant for a version with a comprehension. Run both versions on the same list and compare every line.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: A clear message for missing settings

**Goal:** Write `load_settings(path)` that reads a JSON file. When the file is missing, raise a `ValueError` with a clear message. Catch it once and print `Stopped:` and the message.

**Expected output:**
```text
Stopped: missing settings file shop.json
```

**Hint:** Copy the shape of `load_config()` from Step 2 of the project.

**AI variant:** Ask an AI assistant what else can go wrong when reading a settings file. Add one more case and a message for it.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Save the week twice

**Goal:** Save a small week of totals as a text file, one line per day, and as a JSON file. Read both files back and print them.

**Expected output:**
```text
Monday: 14.00
Tuesday: 11.25
{'Monday': 14.0, 'Tuesday': 11.25}
```

**Hint:** Use `file.write()` inside `with open(..., "w")` for the text file, and `json.dumps()` with `write_text()` for the JSON file.

**AI variant:** Ask an AI assistant when a report should be text and when it should be JSON. Check its answer against who will read each file: a person or a program.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's rounded report

**Goal:** An AI's report rounds each day's total before it adds the days up. Show the AI's total and the correct total for two days of sales.

**Expected output:**
```text
AI total: 25
Fixed total: 25.25
```

**Hint:** Add the exact numbers first. Round only when you print, with `:.2f`.

**AI variant:** Show the AI its own code and both totals. Ask it to explain the difference before it suggests a fix. Did it name rounding before adding?

**Solution:** [solutions/task8.py](solutions/task8.py)
