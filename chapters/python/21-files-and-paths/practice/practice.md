# Practice: Chapter 21

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match. Work in a folder with copies of the data files from `solutions/`, so a mistake never damages the originals.

## Warm-up (10 XP each)

### Task 1: Save a note

**Goal:** Use `Path.write_text()` to save today's special, "Carrot cake", in `special.txt`. Then read the file back and print it without the extra empty line.

**Run it:**
```bash
python task1.py
```

**Expected output:**
```text
Today's special: Carrot cake
```

**Hint:** `read_text()` gives the text with its newline at the end. `strip()` removes it.

**AI variant:** Ask an AI assistant what happens to `special.txt` if you run the program twice. Then run it twice and check the file yourself.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Add to the log

**Goal:** `log.txt` has two lines. Add the line "Closed at 18:00" to the end without losing the first two, then print the whole log.

**Run it:**
```bash
python task2.py
```

**Expected output:**
```text
Opened at 08:00
Milk delivered
Closed at 18:00
```

**Hint:** Mode `"a"` adds to the end. Remember to end the new line with `\n`.

**AI variant:** Ask an AI assistant to explain the difference between modes `"w"` and `"a"` with an example. Check its example on a copy of the log.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Number the menu

**Goal:** Read `menu.txt` line by line. Print each item with a number, then the number of items.

**Run it:**
```bash
python task3.py
```

**Expected output:**
```text
1. Tea
2. Café latte
3. Scone
4. Muffin
4 items on the menu
```

**Hint:** A counter from Chapter 7 goes up by 1 for each line. Use `strip()` on each line.

**AI variant:** Ask an AI assistant to write this program in a different way. Run its version and check that the output is exactly the same.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Count the visits

**Goal:** Keep a visit counter in `visits.txt`. If the file exists, read the number in it; otherwise start at 0. Add 1, save the new number, and print it.

**Run it:**
```bash
python task4.py
```

**Expected output (first run):**
```text
Visit number 1
```

**Hint:** A file holds text, so convert with `int()` after reading and with `str()` before writing.

**AI variant:** Ask an AI assistant what your program prints on the third run. Run it three times and check.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Save the order as CSV

**Goal:** An order is a list of tuples, such as `("Tea", 2)`. Write it to `order.csv` with a header row, using the `csv` module. Then print the file.

**Run it:**
```bash
python task5.py
```

**Expected output:**
```text
item,qty
Tea,2
Scone,1
Café latte,1
```

**Hint:** Unpack each tuple in the `for` loop, as in Chapter 13, and pass a list to `writerow()`.

**AI variant:** Ask an AI assistant why the `csv` module is safer than joining values with commas yourself. Ask for one value that would break a hand-made CSV line.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Items sold today

**Goal:** Read `sales.csv` with `csv.DictReader` and add up the `qty` column.

**Run it:**
```bash
python task6.py
```

**Expected output:**
```text
Items sold today: 25
```

**Hint:** Every CSV value is text. Convert `row["qty"]` with `int()` before you add it.

**AI variant:** Paste the error you get when you forget `int()`, and ask an AI assistant for the cause before the fix.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: A daily report file

**Goal:** Read `sales.csv`, work out each item's amount (quantity times price), and write one line per item to `report.txt`. Then print the report.

**Run it:**
```bash
python task7.py
```

**Expected output:**
```text
Tea: 42.00
Café latte: 21.00
Scone: 22.00
```

**Hint:** You can open two files in one program: one to read and one to write. Format each amount with `:.2f`.

**AI variant:** Ask an AI assistant for a test case with a new item in `sales.csv`. Add the row to a copy of the file and check the new report line by hand.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's log saver

**Goal:** An AI assistant wrote `log_event(text)` with `open("log.txt", "w")`. After two calls, only the last event was left in the log. Fix it so that `log.txt` keeps its first two lines and gains two new ones.

**Run it:**
```bash
python task8.py
```

**Expected output:**
```text
Opened at 08:00
Milk delivered
Tea urn cleaned
Closed at 18:00
```

**Hint:** Count the lines before and after each call. A function that adds data must never use mode `"w"`.

**AI variant:** Show the AI its own function and the real log after two calls. Ask it to explain the cause before the fix, then test its fix on a copy of the log.

**Solution:** [solutions/task8.py](solutions/task8.py)
