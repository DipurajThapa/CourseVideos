# Chapter 21: Files and Paths: Saving and Loading Data

> Quest: make the Corner Cafe's quiz scores and sales survive when the program closes, by saving them to files and loading them again. Reward: 100 XP and the **Archivist** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write text to a file and read it back with `pathlib` and with `open()`.
- Choose the right mode: `"w"` to write a new file, `"a"` to add to the end, `"r"` to read.
- Read a file line by line, and remove the newline at the end of each line.
- Save and load table data as a CSV file with the `csv` module.
- Explain the common file errors and fix them, with help from an AI assistant.

## Why this matters

In Chapter 20, the staff quiz worked well. But when the program closed, every score disappeared. Variables live in the computer's memory, and that memory is cleared when the program stops.

A **file** is data saved on the disk, with a name. It stays there after the program closes, so the next run can load it again. Your photos, documents and app settings are all files.

Saving and loading files is the simplest way to make data last. Shops keep the day's sales in files, games keep saved progress, and spreadsheets export their tables as CSV files.

## The idea

A program and a file talk in three steps: open the file, read or write, then close it.

```text
   program                         disk
  +---------+   open("scores.csv")  +--------------+
  | memory  | --------------------> | scores.csv   |
  | (lost   | <---- read ---------  | name,score   |
  |  at the | ----- write ------->  | Asha,4       |
  |  end)   |       close           | (stays)      |
  +---------+                       +--------------+
```

The **mode** tells Python what you want to do with the file.

| Mode | Name | What it does |
|---|---|---|
| `"r"` | read | Reads the file. This is the default. The file must exist. |
| `"w"` | write | Creates the file, or **empties** it first if it exists. |
| `"a"` | append | Adds to the end. Creates the file if it does not exist. |

A file is like the cafe's order book. You can read it, start a new empty book, or add a line at the end of the old one. The comparison stops working at one point: a person would never tear out every page by accident, but mode `"w"` empties the file with no warning.

**Text and encoding.** A file stores bytes, not letters. An **encoding** is the rule that turns letters into bytes and back. UTF-8 is the standard encoding: it can store every language, including the "é" in "Café". Always write `encoding="utf-8"` when you open a text file. Python 3.15 and newer use UTF-8 by default, but older versions may use a different encoding on some computers, so writing it every time keeps your program the same everywhere.

## Build it step by step

**Step 1: Write and read with pathlib.** You met `Path` in Chapter 18. A `Path` object can also write a whole text file and read it back.

```python
# file: examples/ex01_write_read.py
from pathlib import Path

note = Path("note.txt")
note.write_text("Asha: 4 out of 4\n", encoding="utf-8")
print(note.read_text(encoding="utf-8"))
print(note.exists())
```

<!-- output: examples/ex01_write_read.expected -->
```output
Asha: 4 out of 4

True
```

`write_text()` creates the file, or replaces everything in it. `read_text()` returns the whole file as one string. The empty line appears because the text already ends with a newline, `\n`, and `print()` adds another one.

**Step 2: Open a file with a mode.** The `with` statement opens a file and closes it again when the indented block ends, even if an error happens inside.

```python
# file: examples/ex02_modes.py
with open("today.txt", "w", encoding="utf-8") as file:
    file.write("Asha 4\n")
    file.write("Omar 3\n")

with open("today.txt", "a", encoding="utf-8") as file:
    file.write("Lina 2\n")

with open("today.txt", encoding="utf-8") as file:
    print(file.read(), end="")
```

<!-- output: examples/ex02_modes.expected -->
```output
Asha 4
Omar 3
Lina 2
```

`write()` does not add a newline by itself, so each line ends with `\n`. Mode `"a"` added Lina at the end and kept the other two lines. The last block has no mode, so it reads. `end=""` from Chapter 1 stops `print()` from adding a second newline.

**Step 3: Read line by line.** A file opened for reading works like a list of lines in a `for` loop. The cafe menu is a small text file.

```text
Tea
Café latte
Scone
```

```python
# file: examples/ex03_lines.py
with open("menu.txt", encoding="utf-8") as file:
    for line in file:
        name = line.strip()
        print(f"- {name} ({len(name)} letters)")
```

<!-- output: examples/ex03_lines.expected -->
```output
- Tea (3 letters)
- Café latte (10 letters)
- Scone (5 letters)
```

Each `line` ends with `\n`. `strip()` from Chapter 3 removes it, so "Tea" has 3 letters, not 4. "Café" keeps its "é" because the file was read as UTF-8.

**Step 4: Check that a file exists.** Reading a missing file stops the program. `exists()` lets you check first, and choose what to do with `if` and `else`.

```python
# file: examples/ex04_exists.py
from pathlib import Path

saved = Path("scores.txt")
if saved.exists():
    print(saved.read_text(encoding="utf-8"))
else:
    print("No scores yet. Play a round first.")
```

<!-- output: examples/ex04_exists.expected -->
```output
No scores yet. Play a round first.
```

**Step 5: Build paths.** A **relative path** such as `"scores.txt"` is looked up in the **working directory**: the folder you run the program from. The `/` operator joins folder and file names, on every operating system.

```python
# file: examples/ex05_paths.py
from pathlib import Path

report = Path("reports") / "sales.csv"
print(report.as_posix())
print(report.name, report.suffix)
print(report.parent.as_posix())
print(report.exists())
```

<!-- output: examples/ex05_paths.expected -->
```output
reports/sales.csv
sales.csv .csv
reports
False
```

`parent` is the folder part of the path. `as_posix()` shows the path with forward slashes, as Chapter 18 did. The file does not exist yet, so `exists()` gives `False`.

**Step 6: Write a CSV file.** A **CSV file** stores a table as text: one row per line, with commas between the values. The `csv` module writes it correctly, even when a value contains a comma.

```python
# file: examples/ex06_csv_write.py
import csv

with open("orders.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["item", "qty"])
    writer.writerow(["Tea", 2])
    writer.writerow(["Café latte", 1])

with open("orders.csv", encoding="utf-8") as file:
    print(file.read(), end="")
```

<!-- output: examples/ex06_csv_write.expected -->
```output
item,qty
Tea,2
Café latte,1
```

`writerow()` takes a list and writes one row. The first row is the **header**: the names of the columns. The Python documentation says to open CSV files with `newline=""`, so the `csv` module controls the line endings itself.

**Step 7: Read a CSV file.** `csv.DictReader` reads the header, then gives each row as a dictionary with the column names as keys. The day's sales are in `sales.csv`.

```text
item,qty,price
Tea,12,3.50
Café latte,5,4.20
Scone,8,2.75
```

```python
# file: examples/ex07_csv_read.py
import csv

total = 0.0
with open("sales.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        amount = int(row["qty"]) * float(row["price"])
        total += amount
        print(f"{row['item']:<11}{amount:>7.2f}")
print(f"{'Total':<11}{total:>7.2f}")
```

<!-- output: examples/ex07_csv_read.expected -->
```output
Tea          42.00
Café latte   21.00
Scone        22.00
Total        85.00
```

Every value from a CSV file is a string, even `"12"`. `int()` and `float()` from Chapter 4 turn them into numbers before the calculation.

## See the outcome

Asha's score board saves each new quiz score and loads every score from earlier rounds. `scores.csv` starts with two rows.

```text
name,score
Asha,4
Omar,3
```

```python
# file: examples/ex08_score_board.py
import csv

new_name = "Lina"
new_score = 4

with open("scores.csv", "a", newline="", encoding="utf-8") as file:
    csv.writer(file).writerow([new_name, new_score])

best_name, best_score = "", -1
with open("scores.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        score = int(row["score"])
        print(f"{row['name']:<6}{score} of 4")
        if score > best_score:
            best_name, best_score = row["name"], score

print(f"Best: {best_name} with {best_score} of 4")
```

<!-- output: examples/ex08_score_board.expected -->
```output
Asha  4 of 4
Omar  3 of 4
Lina  4 of 4
Best: Asha with 4 of 4
```

Mode `"a"` keeps the old rows, so the scores from earlier rounds are still there. Lina ties with Asha, but `>` only replaces the best score with a bigger one, so the first 4 stays best. Run the program again, and Lina appears twice: the file remembers every run.

## Work with AI

The AI skill for this chapter is asking an AI assistant to explain file errors and safe file handling. File mistakes are dangerous because some of them destroy data with no error at all. So test every file function on a copy of real data, and check the file afterwards.

Never paste private data into an AI tool. A file of customer names or scores is private data, so paste a small made-up sample instead.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe the data to save and ask for the steps: which file, which mode, which format. |
| Write | Write your own save function first, then ask the AI to check it and name any risk. |
| Generate | Ask for a function with exact rules: the mode, the encoding, the header and the file name as a parameter. |
| Test | Run the function on a new file, on two saves and on an old file, and compare the file's text with the expected text. |
| Debug | Paste the code and the full error report. Ask for the cause before the fix. |
| Improve | Ask for one improvement, then run every test again before you accept it. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha asked an AI assistant: "Write a function save_score(path, name, score) that saves a quiz score to a CSV file with a header. It must keep every score." The AI said its function keeps every score.

```python
# file: examples/ai_save_flawed.py
from pathlib import Path


def save_score(path, name, score):
    with open(path, "w", encoding="utf-8") as file:
        file.write("name,score\n")
        file.write(f"{name},{score}\n")


save_score("week.csv", "Asha", 4)
save_score("week.csv", "Omar", 3)
print(Path("week.csv").read_text(encoding="utf-8"), end="")
```

<!-- output: examples/ai_save_flawed.expected -->
```output
name,score
Omar,3
```

Asha's score is gone. Mode `"w"` empties the file every time the function runs, so only the last save survives. Her test cases caught it.

<!-- output: examples/ai_tests_flawed.expected -->
```output
1 New file: pass
2 Two saves: FAIL
3 Old file: FAIL
```

The fixed function appends with mode `"a"`, and writes the header only when the file is new.

```python
# file: examples/ai_save_fixed.py
import csv
from pathlib import Path


def save_score(path, name, score):
    new_file = not Path(path).exists()
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if new_file:
            writer.writerow(["name", "score"])
        writer.writerow([name, score])


save_score("week.csv", "Asha", 4)
save_score("week.csv", "Omar", 3)
print(Path("week.csv").read_text(encoding="utf-8"), end="")
```

<!-- output: examples/ai_save_fixed.expected -->
```output
name,score
Asha,4
Omar,3
```

Later, the AI suggested writing the header on every save, "because CSV readers skip repeated headers". That is not true: `DictReader` uses only the first row as the header, and every later header becomes a data row. When Asha ran her tests again, cases 2 and 3 failed, so she kept the `exists()` check.

## Common mistakes

**Mistake 1: a file name that does not match.** The file is called `scores.csv`, but the program asks for `score.csv`.

```python
# file: examples/err01_missing_file.py
print("Loading scores")
with open("score.csv", encoding="utf-8") as file:
    print(file.read())
```

<!-- error: examples/err01_missing_file.expected_error -->
```output
Loading scores
Traceback (most recent call last):
  File "err01_missing_file.py", line 3, in <module>
    with open("score.csv", encoding="utf-8") as file:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'score.csv'
```

Fix: check the spelling, and run the program from the folder that holds the file. A relative path is looked up in the working directory, not in the folder of the `.py` file.

**Mistake 2: mode "w" when you meant "a".** The cafe log has three lines. This program meant to add one more.

```python
# file: examples/err02_w_erases.py
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("Closed at 18:00\n")

with open("log.txt", encoding="utf-8") as file:
    print(file.read(), end="")
```

<!-- output: examples/err02_w_erases.expected -->
```output
Closed at 18:00
```

There is no error, but the three old lines are gone. Fix: use `"a"` to add to a file. Use `"w"` only when you want to start again.

**Mistake 3: the wrong encoding.** An old cash register saved its menu with a different encoding. Reading it as UTF-8 fails at the "é".

```python
# file: examples/err03_encoding.py
with open("old_menu.txt", encoding="utf-8") as file:
    print(file.read())
```

<!-- error: examples/err03_encoding.expected_error -->
```output
Traceback (most recent call last):
  File "err03_encoding.py", line 3, in <module>
    print(file.read())
          ~~~~~~~~~^^
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 7: invalid continuation byte
```

Fix: find out which encoding saved the file, read it once with that encoding, and save it again as UTF-8. Write your own files with `encoding="utf-8"`, so this never happens to them.

**Mistake 4: using CSV values as numbers.** Every value from a CSV file is text.

```python
# file: examples/err04_text_numbers.py
import csv

total = 0.0
with open("sales.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        total = total + row["price"]
print(total)
```

<!-- error: examples/err04_text_numbers.expected_error -->
```output
Traceback (most recent call last):
  File "err04_text_numbers.py", line 7, in <module>
    total = total + row["price"]
            ~~~~~~^~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'float' and 'str'
```

Fix: convert first, `total = total + float(row["price"])`.

## Think beyond

1. Asha runs the score board three times. How many rows does `scores.csv` have now, and how could she stop the same score being saved twice?
2. A program crashes halfway through a `with` block that writes a file. What does the `with` statement guarantee, and what could still be missing from the file?

## Recap

- A file keeps data after the program stops. Open it, read or write, then close it.
- `Path.write_text()` and `Path.read_text()` write and read a whole file in one line.
- `with open(...) as file:` closes the file for you. Mode `"r"` reads, `"w"` empties and writes, `"a"` adds to the end.
- Always write `encoding="utf-8"`, and use `strip()` to remove the newline from each line.
- The `csv` module writes rows with `csv.writer` and reads them as dictionaries with `csv.DictReader`. Every value comes back as text.
- Test file functions on a copy, and check the file afterwards: some file mistakes destroy data with no error.

You earned **100 XP** and the **Archivist** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 22, you will use `try` and `except` so a missing file or a bad value gives a clear message instead of a crash.
