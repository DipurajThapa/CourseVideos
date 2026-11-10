# Chapter 25: Boss Level 5: The Data Report Generator

> Quest: turn a folder of messy till files into a clean weekly report, with clear messages instead of crashes, and let tests judge every line an AI writes. Reward: 300 XP and the **Report Master** badge.

## The mission

Every evening, the till at the Corner Cafe saves the day's sales as a CSV file. On Friday, Asha opens four files and adds them up by hand. It takes an hour, and the files are not clean. One row says `four` instead of a price. One row has no price at all. On Thursday the cafe was closed, so that file is empty.

Asha wants a program that reads every file in the folder, skips the bad rows and counts them, and writes a weekly report. The currency and the tax rate must live in a settings file, so the owner can change them without touching the code. When something is wrong with the settings, the program must say what is wrong, not crash.

This boss level uses everything from Module 5.

| Chapter | What you use from it |
|---|---|
| 21 | Reading CSV files with `csv.DictReader`, and writing a text file |
| 22 | Small `try` blocks, specific exceptions, `else`, and `raise ValueError` with a clear message |
| 23 | Reading settings with `json.loads()`, and saving data with `json.dumps()` |
| 24 | A project folder that can have its own virtual environment; this project needs only the standard library and `pytest` |
| New | `Path.glob("*.csv")` finds every CSV file in a folder |

## What you will build

Two code files, one test file, one settings file and a folder of till files work together.

| File | Its job |
|---|---|
| `report_tools.py` | The rules: load the settings, read one file, build the week, and make the report lines |
| `report.py` | Runs the rules and writes `report.txt` and `report.json` |
| `test_report_tools.py` | Seven tests for the rules |
| `config.json` | The settings: `{"currency": "USD", "tax_rate": 0.08}` |
| `data/` | The till files `1-monday.csv` to `4-thursday.csv` |

The number at the start of each file name keeps the days in order, because `sorted()` puts names in alphabetical order. Here is the finished report.

<!-- output: project/report.expected -->
```output
CORNER CAFE: WEEK REPORT
Monday         USD 14.00
Tuesday        USD 11.25
Wednesday      USD 12.00
Thursday        USD 0.00
Total          USD 37.25
Tax             USD 2.98
With tax       USD 40.23
Rows skipped: 2
Saved report.txt and report.json
```

## Acceptance criteria

Your report generator is finished when all of these are true.

1. It reads every CSV file in the `data` folder, in day order, including an empty file.
2. A row with a price that is not a number, or no price at all, is skipped and counted. The other rows still count.
3. A negative price is refused.
4. The currency and the tax rate come from `config.json`.
5. A missing or broken `config.json` gives one clear line that starts with `Report stopped:`, and no traceback.
6. The report shows each day, the total, the tax, the total with tax and the number of skipped rows, with two decimal places.
7. It saves the report as text in `report.txt` and as data in `report.json`.
8. All seven tests pass, and nothing is rounded before it is added up.

## Plan it with AI

Before any code, Asha asked an AI assistant for a plan. This chapter's AI skill is to ask AI to review your error handling and to generate test data, then to check both against your real files.

> "I am a beginner. I know files, CSV, JSON, try and except, functions and pytest. I want a weekly report from a folder of till CSV files with the columns item and amount. Some rows are damaged. Do not write code. Plan the functions, and say how to handle errors."

An example answer looked like this:

> Write one function, `make_report()`. It reads every file, adds up the amounts and writes the report. Put the whole function body inside `try`, and add `except Exception: print("Something went wrong")`, so the program never crashes.

The plan would never crash, but it would never say why. Asha checked it against Chapters 17 and 22. One big function cannot be tested in parts, and `except Exception` around everything hides the real problem. She asked for small functions instead, each with one job, and a small `try` around the one line that can fail.

## Build it step by step

**Step 1: Look at the real till files.** Before writing any rule, Asha prints two of the files, row by row.

```python
# file: examples/step1/read_days.py
import csv
from pathlib import Path

for name in ["2-tuesday.csv", "3-wednesday.csv"]:
    path = Path("data") / name
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            print(name, row["item"], row["amount"])
```

<!-- output: examples/step1/read_days.expected -->
```output
2-tuesday.csv tea 3.50
2-tuesday.csv soup 5.00
2-tuesday.csv cake four
2-tuesday.csv scone 2.75
3-wednesday.csv tea 3.50
3-wednesday.csv cake None
3-wednesday.csv tea 3.50
3-wednesday.csv soup 5.00
```

Two rows are damaged. On Tuesday, the amount is the word `four`. On Wednesday, the row has no comma, so `DictReader` fills the missing amount with `None`. Every good amount is still text, such as `'3.50'`.

**Step 2: Load the settings, with a clear message.** `load_config()` in `report_tools.py` reads `config.json`. It catches the two errors that can happen and raises a `ValueError` with a message a person can act on.

```python
# illustrative: lines 7 to 16 of project/report_tools.py
def load_config(path):
    """Return the settings in a JSON file, or raise ValueError."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ValueError(f"missing settings file {path.name}")
    try:
        return json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"{path.name} is not valid JSON: {error.msg}")
```

`error.msg` is the short reason from the `json` module, without line and column numbers. When the file is fine, the settings come back as a dictionary:

```python
# file: examples/step2/config_check.py
from pathlib import Path
from report_tools import load_config

config = load_config(Path("config.json"))
print(config)
print("Currency:", config["currency"])
print("Tax rate:", config["tax_rate"])
```

<!-- output: examples/step2/config_check.expected -->
```output
{'currency': 'USD', 'tax_rate': 0.08}
Currency: USD
Tax rate: 0.08
```

**Step 3: One amount at a time.** `parse_amount()` turns the text into a number and refuses a negative price. A word such as `four` already raises a `ValueError` inside `float()`.

```python
# file: examples/step3/amount_check.py
from report_tools import parse_amount

for text in ["3.50", "four", "-2.00"]:
    try:
        print(f"{text!r} gives", parse_amount(text))
    except ValueError as error:
        print(f"{text!r} refused:", error)
```

<!-- output: examples/step3/amount_check.expected -->
```output
'3.50' gives 3.5
'four' refused: could not convert string to float: 'four'
'-2.00' refused: negative amount '-2.00'
```

**Step 4: Tests first, then let AI write the reading code.** Asha wrote six tests for the rules before the reading code existed, as in Chapter 20. Two of them check the whole week: the total must be 37.25, two rows must be skipped, and Tuesday must be 11.25, not rounded. Then she asked the AI to write `read_sales()` and `build_week()`, and to run them against her tests. The full exchange is in [Test it](#test-it).

**Step 5: Build the week, then the report.** `build_week()` finds every CSV file with `glob()`, reads it with `read_sales()` and adds each amount to the day, the item and the week. `glob("*.csv")` returns the paths of all files whose names end in `.csv`, and `sorted()` puts them in name order.

```python
# file: examples/step5/week_check.py
import json
from pathlib import Path
from report_tools import build_week

week = build_week(Path("data"))
print(json.dumps(week["days"], indent=2))
print("Total:", week["total"])
print("Skipped:", week["skipped"])
```

<!-- output: examples/step5/week_check.expected -->
```output
{
  "Monday": 14.0,
  "Tuesday": 11.25,
  "Wednesday": 12.0,
  "Thursday": 0
}
Total: 37.25
Skipped: 2
```

Thursday's file is empty, so nothing is added and its total stays `0`. The day name comes from the file name: `path.stem` is `"2-tuesday"`, `split("-")[1]` is `"tuesday"`, and `title()` gives `"Tuesday"`.

The finished module holds all the rules. `report.py` only runs them and saves the results:

```python
# file: project/report.py
"""Corner Cafe week report: reads data/*.csv, writes two files."""
import json
from pathlib import Path
from report_tools import build_week, load_config, report_lines

try:
    config = load_config(Path("config.json"))
    week = build_week(Path("data"))
except ValueError as error:
    print("Report stopped:", error)
else:
    with open("report.txt", "w", encoding="utf-8") as file:
        for line in report_lines(week, config):
            file.write(line + "\n")
    saved = json.dumps(week, indent=2)
    Path("report.json").write_text(saved, encoding="utf-8")
    print(Path("report.txt").read_text(encoding="utf-8"), end="")
    print("Saved report.txt and report.json")
```

The `try` block holds two lines, and both raise only `ValueError` with a clear message. The `else` block runs only when both worked. Line 18 reads `report.txt` back, so the report on screen is exactly what was saved.

## Test it

**AI pair moment.** In Step 4, the AI wrote this `read_sales()` and said, "This skips only the two damaged rows." Asha did not argue. She ran her six tests.

```python
# illustrative: lines 27 to 37 of examples/ai/flawed/report_tools.py
def read_sales(path):
    """Return the good sales in a CSV file, and the bad count."""
    sales, bad = [], 0
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            try:
                amount = float(row["Amount"])
                sales.append((row["item"], amount))
            except Exception:
                bad += 1
    return sales, bad
```

<!-- output: examples/ai/flawed/test_report_tools.expected -->
```output
....FF                                           [100%]
=============== short test summary info ================
FAILED test_report_tools.py::test_week_total_and_skipped
FAILED test_report_tools.py::test_days_are_not_rounded
2 failed, 4 passed in 0.01s
```

Both week tests fail. To see why, she counted good and bad rows in each file:

<!-- output: examples/ai/flawed/rows_check.expected -->
```output
1-monday.csv: 0 good, 4 bad
2-tuesday.csv: 0 good, 4 bad
3-wednesday.csv: 0 good, 4 bad
4-thursday.csv: 0 good, 0 bad
```

Every row is bad. The column is called `amount`, but the AI wrote `row["Amount"]`, with a capital A. That raises a `KeyError` on every row, and `except Exception` hides it, so the program runs with no error and reports nothing. Asha fixed it with the rule from Chapter 22: the right key, her own `parse_amount()`, and only the two exceptions she expects.

```python
# illustrative: lines 27 to 38 of examples/ai/fixed/report_tools.py
def read_sales(path):
    """Return the good sales in a CSV file, and the bad count."""
    sales, bad = [], 0
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            try:
                amount = parse_amount(row["amount"])
            except (ValueError, TypeError):
                bad += 1
            else:
                sales.append((row["item"], amount))
    return sales, bad
```

`ValueError` covers `four`, and `TypeError` covers the missing amount, because `float(None)` raises a `TypeError`. All six tests passed.

<!-- output: examples/ai/fixed/test_report_tools.expected -->
```output
......                                           [100%]
6 passed in 0.01s
```

**Test data from the AI.** Next, Asha asked the AI for realistic test data. It gave her a file and said it matched her till:

```text
Item,Amount
Tea,$3.50
Scone,"2,75"
Cake,4.25
```

Asha compared the first line with a real till file, which starts `item,amount`. The AI's columns have capital letters. She saved the AI's file as a fifth day and ran the report on it:

<!-- error: examples/ai/testdata/report.expected_error -->
```output
Traceback (most recent call last):
  File "report.py", line 9, in <module>
    week = build_week(Path("data"))
  File "report_tools.py", line 45, in build_week
    sales, bad = read_sales(path)
                 ~~~~~~~~~~^^^^^^
  File "report_tools.py", line 33, in read_sales
    amount = parse_amount(row["amount"])
                          ~~~^^^^^^^^^^
KeyError: 'amount'
```

The report crashed. The last line names the missing key, and the last `File` line shows where. On your computer, the `File` lines show the full path of each file. Asha pasted the code and the error into the chat and asked for the cause first. The AI explained that `DictReader` uses the first line as the keys, exactly as written, so a file with `Amount` has no key `amount`. The smallest fix is to check the columns before the loop:

```python
# illustrative: lines 31 to 34 of project/report_tools.py
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        if columns and columns != ["item", "amount"]:
            raise ValueError(f"{path.name} needs item and amount")
```

`reader.fieldnames` is the list of column names from the first line. An empty file has none, so `if columns` lets Thursday through. With the fix, the same file gives one clear line:

<!-- output: examples/ai/debug/report.expected -->
```output
Report stopped: 5-friday.csv needs item and amount
```

Asha kept the AI's file as test data and added a seventh test: `read_sales()` must raise a `ValueError` for it. Then she ran every test again.

<!-- output: project/test_report_tools.expected -->
```output
.......                                          [100%]
7 passed in 0.01s
```

She also ran the whole report on three more folders whose results she knew in advance.

| Case | Folder | Expected |
|---|---|---|
| Normal week | `project` | The full report, 2 rows skipped |
| No settings file | `cases/missing_config` | `Report stopped: missing settings file config.json` |
| Broken settings | `cases/bad_json` | `Report stopped: config.json is not valid JSON: ...` |
| Closed all week | `cases/closed_week` | Only Thursday, every amount `USD 0.00` |

<!-- output: examples/cases/missing_config/report.expected -->
```output
Report stopped: missing settings file config.json
```

<!-- output: examples/cases/bad_json/report.expected -->
```output
Report stopped: config.json is not valid JSON: Expecting ',' delimiter
```

The broken settings file is missing a comma between its two settings. The closed week has only the empty Thursday file:

<!-- output: examples/cases/closed_week/report.expected -->
```output
CORNER CAFE: WEEK REPORT
Thursday        USD 0.00
Total           USD 0.00
Tax             USD 0.00
With tax        USD 0.00
Rows skipped: 0
Saved report.txt and report.json
```

All four results matched.

## Improve it with AI

Asha asked the AI to review her finished module: "Suggest one improvement that makes the report clearer. Do not change what the totals are." The AI answered:

> Round each day's total to a whole number before you store it. The report will show tidy amounts, and the week total will be simpler.

Asha ran her tests on the AI's version, which added `day_total = round(day_total)` to `build_week()`:

<!-- output: examples/ai/improve/test_report_tools.expected -->
```output
....FF.                                          [100%]
=============== short test summary info ================
FAILED test_report_tools.py::test_week_total_and_skipped
FAILED test_report_tools.py::test_days_are_not_rounded
2 failed, 5 passed in 0.01s
```

Tuesday became 11 instead of 11.25, and the week became 37 instead of 37.25. The suggestion broke her rule: it changed the totals. Rounding belongs in the display, and `money()` already shows two decimal places. Asha kept her version.

Before she pasted any code into the chat, she had checked it for private data. The till files hold only items and amounts, with no names or card numbers.

These are the six ways AI helped with this project. The full prompts are in [ai-prompts.md](ai-prompts.md).

| Stage | How AI helped |
|---|---|
| Plan | Suggested one big function inside `except Exception`. Asha asked for small functions and small `try` blocks instead. |
| Write | Wrote its own `parse_amount()` to compare with Asha's. It accepted `-2.00`, so Asha kept hers. |
| Generate | Wrote `read_sales()` and `build_week()`. `row["Amount"]` inside `except Exception` skipped every row, and two tests failed. |
| Test | Generated realistic test data. Its capital-letter columns crashed the report with a `KeyError`. |
| Debug | Explained the cause first: `DictReader` keys are the first line, exactly as written. A column check fixed it, and all seven tests passed. |
| Improve | Suggested rounding each day. Two tests failed, so Asha kept her version. |

The Write stage compared the two versions on three amounts:

<!-- output: examples/ai/write_compare.expected -->
```output
'3.50' AI: 3.5
'3.50' Asha: 3.5
' 2.75' AI: 2.75
' 2.75' Asha: 2.75
'-2.00' AI: -2.0
'-2.00' Asha: refused
```

## Recap

- Look at the real data before you write a rule. Damaged rows are normal.
- Put the rules in small functions, and keep each `try` block around the one line that can fail.
- Catch the exceptions you expect, such as `ValueError` and `TypeError`. `except Exception` can hide a bug that makes every row look bad.
- Turn file and JSON errors into one clear message with `raise ValueError(...)`, and catch it once in the main program.
- Check AI test data against a real file, and keep it as a test when it finds a problem.
- Round only when you display a number, never before you add it up.

You earned **300 XP** and the **Report Master** badge. Module 5 is complete.

The practice tasks for this chapter are in [practice/practice.md](practice/practice.md).

## What's next

Asha's report keeps each sale as a pair of an item and an amount, and each day as a dictionary. In Chapter 26, you will build your own types with classes, so a sale or a day can carry its data and its own rules together.
