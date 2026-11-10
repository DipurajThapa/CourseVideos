# Video Script: Chapter 25: Boss Level 5: The Data Report Generator

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:59.

## Scene 1: Introduction (0:00 to 0:38)

**Section:** Introduction

**Direction:** Open on Friday's hour of adding by hand, and the messy files. Then the boss level title and the stake.

- **Narration:** Every evening, the till at the Corner Cafe saves the day's sales as a file. On Friday, Asha adds four files up by hand. It takes an hour.
  **On screen:** Friday: one hour of adding
- **Narration:** And the files are messy. One price is a word. One row has no price at all. One file is empty.
  **On screen:** Friday: one hour of adding
- **Narration:** Welcome to Chapter 25, the fifth boss level!
  **On screen:** The Data Report Generator
- **Narration:** Asha will build a report generator that reads every file, survives the bad rows, and saves a clean report.
  **On screen:** The Data Report Generator Messy files in. A clean report out.
- **Narration:** An AI assistant will write part of it, and make it look perfect. It will report nothing at all, and say nothing. Her tests will catch it.
  **On screen:** The Data Report Generator Messy files in. A clean report out.

## Scene 2: The mission (0:38 to 1:27)

**Section:** The mission

**Direction:** The report's job, then the chapters it uses, row by row.

- **Narration:** Here is the mission. Read every till file in one folder.
  **On screen:** The weekly report
    - Read every till file in one folder.
- **Narration:** Skip the bad rows, and count them, so Asha knows how many.
  **On screen:** The weekly report
    - Read every till file in one folder.
    - Skip the bad rows, and count them.
- **Narration:** Keep the currency and the tax rate in a settings file, so the owner can change them without touching the code.
  **On screen:** The weekly report
    - Read every till file in one folder.
    - Skip the bad rows, and count them.
    - Currency and tax rate in a settings file.
- **Narration:** And when something is wrong, say what is wrong. Never crash.
  **On screen:** The weekly report
    - Read every till file in one folder.
    - Skip the bad rows, and count them.
    - Currency and tax rate in a settings file.
    - A clear message, never a crash.
- **Narration:** Every piece comes from Module 5. CSV files and text files from Chapter 21.
  **On screen:** Table: Everything from Module 5 (row 1 in focus)
- **Narration:** Small try blocks, and raise value error with a clear message, from Chapter 22.
  **On screen:** Table: Everything from Module 5 (row 2 in focus)
- **Narration:** JSON from Chapter 23.
  **On screen:** Table: Everything from Module 5 (row 3 in focus)
- **Narration:** And from Chapter 24, a project folder. This project needs only the standard library and pytest, so nothing new to install.
  **On screen:** Table: Everything from Module 5 (row 4 in focus)
- **Narration:** Plus one new tool. Glob finds every file in a folder whose name matches a pattern, such as star dot c s v.
  **On screen:** Table: Everything from Module 5 (row 5 in focus)

## Scene 3: What you will build (1:27 to 2:02)

**Section:** What you will build

**Direction:** The files and their jobs, then the finished report as the destination.

- **Narration:** Report tools holds the rules.
  **On screen:** Table: Two code files, one job each (row 1 in focus)
- **Narration:** Report dot p y runs the rules and saves two reports.
  **On screen:** Table: Two code files, one job each (row 2 in focus)
- **Narration:** A test file checks the rules.
  **On screen:** Table: Two code files, one job each (row 3 in focus)
- **Narration:** The settings file holds the currency and the tax rate: 8 percent.
  **On screen:** Table: Two code files, one job each (row 4 in focus)
- **Narration:** And the data folder holds the till files. Each name starts with a number, so the days stay in order when they are sorted.
  **On screen:** Table: Two code files, one job each (row 5 in focus)
- **Narration:** Here is the finished report. One line per day.
  **On screen:** Code `project/report.py`, output `project/report.expected`
- **Narration:** The total, the tax, and the total with tax.
  **On screen:** Code `project/report.py`, output `project/report.expected`
- **Narration:** And how many rows were skipped.
  **On screen:** Code `project/report.py`, output `project/report.expected`
- **Narration:** The program itself is about twenty lines. The rules live in the other file.
  **On screen:** Code `project/report.py`, output `project/report.expected`

## Scene 4: Acceptance criteria (2:02 to 3:06)

**Section:** Acceptance criteria

**Direction:** Seven criteria in groups, a quiz on the clear-message criterion, then a breather.

- **Narration:** Asha writes down what done means.
  **On screen:** Done means all eight are true
- **Narration:** One. Read every file, in day order, even an empty one.
  **On screen:** Done means all eight are true
    - Read every CSV file in `data`, in day order, even an empty one.
- **Narration:** Two and three. Skip and count a row with a bad price or no price, and refuse a negative price.
  **On screen:** Done means all eight are true
    - Read every CSV file in `data`, in day order, even an empty one.
    - Skip and count a row with a bad price or no price.
    - Refuse a negative price.
- **Narration:** Four and five. The settings come from a file, and a problem with them gives one clear line.
  **On screen:** Done means all eight are true
    - Read every CSV file in `data`, in day order, even an empty one.
    - Skip and count a row with a bad price or no price.
    - Refuse a negative price.
    - Currency and tax rate come from `config.json`.
    - Missing or broken settings: one clear line, no traceback.
- **Narration:** Six and seven. The report, saved twice, and seven tests that pass.
  **On screen:** Done means all eight are true
    - Read every CSV file in `data`, in day order, even an empty one.
    - Skip and count a row with a bad price or no price.
    - Refuse a negative price.
    - Currency and tax rate come from `config.json`.
    - Missing or broken settings: one clear line, no traceback.
    - Report each day, the total, the tax and the skipped rows.
    - Save `report.txt` and `report.json`. Seven tests pass.
- **Narration:** And eight. Nothing is rounded before it is added up.
  **On screen:** Done means all eight are true
    - Read every CSV file in `data`, in day order, even an empty one.
    - Skip and count a row with a bad price or no price.
    - Refuse a negative price.
    - Currency and tax rate come from `config.json`.
    - Missing or broken settings: one clear line, no traceback.
    - Report each day, the total, the tax and the skipped rows.
    - Save `report.txt` and `report.json`. Seven tests pass.
    - Nothing is rounded before it is added up.
- **Narration:** Quick check, from Chapter 22. The settings file is missing. What should a person see?
  **On screen:** Quick check: "The settings file is missing. What should a person see?" (options shown)
- **Interaction:** "The settings file is missing. What should a person see?" stays on screen with a 10-second timer.
- **Narration:** D. One clear line that says what is wrong. A traceback is for developers, and silence hides the problem.
  **On screen:** Quick check: "The settings file is missing. What should a person see?" (answer revealed: One clear line that says what is wrong)
- **Narration:** Take a breather. You know the files, and what done means.
  **On screen:** Breather card
    - Two code files, one job each.
    - Bad rows are skipped and counted.
    - A problem gives one clear line.
- **Narration:** Next, Asha plans the functions with an AI assistant.
  **On screen:** Breather card
    - Two code files, one job each.
    - Bad rows are skipped and counted.
    - A problem gives one clear line.
- **Breather:** 4 quiet seconds.

## Scene 5: Plan it with AI (3:06 to 3:45)

**Section:** Plan it with AI

**Direction:** Stage 1: the AI's plan, one big function inside except Exception. Asha checks it against Chapters 17 and 22 and asks for small parts.

- **Narration:** In this project, all six AI stages help build one module: the report rules. Stage 1: plan. Asha asks for a plan, and says: no code yet.
  **On screen:** AI chat, stage 1: Plan: functions and errors
    - You: I am a beginner. I know files, CSV, JSON, try and except, functions and pytest. I want a weekly report from a folder of till CSV files with the columns item and amount. Some rows are damaged. Do not write code. Plan the functions, and say how to handle errors.
- **Narration:** The AI suggests one function that does everything, inside one big try, with except Exception. Its promise: it never crashes.
  **On screen:** AI chat, stage 1: Plan: functions and errors
    - You: I am a beginner. I know files, CSV, JSON, try and except, functions and pytest. I want a weekly report from a folder of till CSV files with the columns item and amount. Some rows are damaged. Do not write code. Plan the functions, and say how to handle errors.
    - AI (example answer): Write one function, `make_report()`, that reads every file, adds up the amounts and writes the report. Put the whole body inside `try`, with `except Exception: print("Something went wrong")`, so it never crashes.
- **Narration:** Asha checks it against Chapters 17 and 22. One big function cannot be tested in parts. And except Exception hides the real problem: the program never crashes, but it never says why.
  **On screen:** AI chat, stage 1: Plan: functions and errors
    - You: I am a beginner. I know files, CSV, JSON, try and except, functions and pytest. I want a weekly report from a folder of till CSV files with the columns item and amount. Some rows are damaged. Do not write code. Plan the functions, and say how to handle errors.
    - AI (example answer): Write one function, `make_report()`, that reads every file, adds up the amounts and writes the report. Put the whole body inside `try`, with `except Exception: print("Something went wrong")`, so it never crashes.
- **Narration:** So she asks for small functions with one job each, and a small try around the one line that can fail.
  **On screen:** AI chat, stage 1: Plan: functions and errors
    - You: I am a beginner. I know files, CSV, JSON, try and except, functions and pytest. I want a weekly report from a folder of till CSV files with the columns item and amount. Some rows are damaged. Do not write code. Plan the functions, and say how to handle errors.
    - AI (example answer): Write one function, `make_report()`, that reads every file, adds up the amounts and writes the report. Put the whole body inside `try`, with `except Exception: print("Something went wrong")`, so it never crashes.

## Scene 6: Step 1: Look at the real files (3:45 to 4:41)

**Section:** Build it step by step

**Direction:** Print two real files row by row before any rule. Ask about the short row, then reveal.

- **Narration:** Time to build. Step 1: before any rule, Asha looks at the real data. She prints two of the files, row by row.
  **On screen:** Code `examples/step1/read_days.py`, line 5 highlighted, output hidden
- **Narration:** Every till file starts with the same line: item comma amount. Those are the column names, in small letters.
  **On screen:** Code `examples/step1/read_days.py`, line 5 highlighted, output hidden
- **Narration:** Line 6 joins the folder and the file name with a slash, as in Chapter 21. Line 8 reads each row as a dictionary, with the column names as keys.
  **On screen:** Code `examples/step1/read_days.py`, line 6, 8 highlighted, output hidden
- **Narration:** One rule to know first. When a row is shorter than the first line, Dict reader fills each missing value with None.
  **On screen:** Code `examples/step1/read_days.py`, line 9 highlighted, output hidden
- **Interaction:** "Wednesday has a row with only `cake`. What does line 9 print for it?" stays on screen with a 10-second timer.
- **Narration:** 3 wednesday dot c s v, cake, None.
  **On screen:** Code `examples/step1/read_days.py`, line 9 highlighted, output `examples/step1/read_days.expected`
- **Narration:** And on Tuesday, the amount is the word four. Two damaged rows. Every good amount is still text.
  **On screen:** Code `examples/step1/read_days.py`, line 9 highlighted, output `examples/step1/read_days.expected`

## Scene 7: Step 2: Settings with a clear message (4:41 to 5:28)

**Section:** Build it step by step

**Direction:** Walk load_config: two small try blocks, each turning an error into one ValueError message. Then a check run.

- **Narration:** Step 2: the settings. Load config has two small try blocks. The first reads the file. A missing file raises file not found error.
  **On screen:** Code `project/report_tools.py`, line 9, 10, 11 highlighted, output hidden
- **Narration:** Line 12 turns it into a value error with a message a person can act on: missing settings file, and its name.
  **On screen:** Code `project/report_tools.py`, line 12 highlighted, output hidden
- **Narration:** The second try reads the JSON. A broken file raises a JSON decode error. Line 16 turns it into one clear value error too.
  **On screen:** Code `project/report_tools.py`, line 13, 14, 15, 16 highlighted, output hidden
- **Narration:** Error dot msg is the short reason from the JSON module. So the main program needs to catch only one kind of error.
  **On screen:** Code `project/report_tools.py`, line 16 highlighted, output hidden
- **Narration:** When the file is fine, the settings come back as a dictionary.
  **On screen:** Code `examples/step2/config_check.py`, line 5 highlighted, output `examples/step2/config_check.expected`
- **Narration:** The currency is U S D, and the tax rate is 0.08, which is 8 percent.
  **On screen:** Code `examples/step2/config_check.py`, line 7, 8 highlighted, output `examples/step2/config_check.expected`

## Scene 8: Step 3: One amount at a time (5:28 to 7:08)

**Section:** Build it step by step

**Direction:** parse_amount refuses words and negatives; predict the third line. Then stage 2: the AI's version, compared on three amounts.

- **Narration:** Step 3: one amount at a time. Asha writes parse amount herself. Line 21: float turns the text into a number. A word already raises a value error here.
  **On screen:** Code `project/report_tools.py`, line 21 highlighted, output hidden
- **Narration:** Lines 22 and 23: a price below zero is refused, with its own value error.
  **On screen:** Code `project/report_tools.py`, line 22, 23 highlighted, output hidden
- **Narration:** She tries three amounts: 3.50, the word four, and minus 2. Line 7 catches the value error, and line 8 prints its message.
  **On screen:** Code `examples/step3/amount_check.py`, line 7, 8 highlighted, output hidden
- **Interaction:** "What does the program print for `'-2.00'`?" stays on screen with a 10-second timer.
- **Narration:** Minus 2 refused: negative amount. The message from line 23 of the module.
  **On screen:** Code `examples/step3/amount_check.py`, line 7, 8 highlighted, output `examples/step3/amount_check.expected`
- **Narration:** And the word four is refused by float, with Python's own message.
  **On screen:** Code `examples/step3/amount_check.py`, line 7, 8 highlighted, output `examples/step3/amount_check.expected`
- **Narration:** Stage 2: write. Asha wrote her version first. Now she asks the AI for its own, without showing hers.
  **On screen:** AI chat, stage 2: Write it yourself, then compare
    - You: Write a function parse_amount(text) that turns a price such as '3.50' into a float, and raises ValueError for a word or a negative price. Show only the function.
- **Narration:** The AI's version is one line, with strip for spaces. Asha renames it ai version, so both can sit in one file.
  **On screen:** AI chat, stage 2: Write it yourself, then compare
    - You: Write a function parse_amount(text) that turns a price such as '3.50' into a float, and raises ValueError for a word or a negative price. Show only the function.
    - AI (example answer): Here it is. `strip()` also allows spaces around the price: [code `examples/ai/write_compare.py`]
- **Narration:** She runs both on the same three amounts.
  **On screen:** Code `examples/ai/write_compare.py`, line 13 highlighted, output `examples/ai/write_compare.expected`
- **Narration:** 3.50 and 2.75 with a space: both agree.
  **On screen:** Code `examples/ai/write_compare.py`, line 13 highlighted, output `examples/ai/write_compare.expected`
- **Narration:** But minus 2. The AI's version returns minus 2.0. A negative price. Hers refuses it. Asha keeps her own.
  **On screen:** Code `examples/ai/write_compare.py`, line 10 highlighted, output `examples/ai/write_compare.expected`
- **Narration:** Breather. Relax your shoulders. The settings and the amounts are safe.
  **On screen:** Breather card
    - Look at the real data first.
    - Settings errors become one clear message.
    - A negative price is refused.
- **Narration:** Next, Asha writes her tests, and lets the AI write the reading code.
  **On screen:** Breather card
    - Look at the real data first.
    - Settings errors become one clear message.
    - A negative price is refused.
- **Breather:** 4 quiet seconds.

## Scene 9: Step 4: Let the tests judge the AI (7:08 to 9:39)

**Section:** Build it step by step

**Direction:** The six tests, stage 3: the AI's read_sales and its promise, ask; the run, the row counts, the cause, the fix, six passed. Quiz.

- **Narration:** Step 4. As in Chapter 20, Asha writes the tests first. Four check the amounts and the money format. These two check the whole week.
  **On screen:** Code `examples/ai/flawed/test_report_tools.py`, line 29, 30 highlighted, output hidden
- **Narration:** The week total must be 37.25, and exactly two rows must be skipped.
  **On screen:** Code `examples/ai/flawed/test_report_tools.py`, line 29, 30 highlighted, output hidden
- **Narration:** And Tuesday must be 11.25, not rounded.
  **On screen:** Code `examples/ai/flawed/test_report_tools.py`, line 35 highlighted, output hidden
- **Narration:** Stage 3: generate. Asha pastes her tests and asks for the reading code. Do not change my tests.
  **On screen:** AI chat, stage 3: Generate: code that must pass my tests
    - You: Here are my six tests. Write read_sales(path), which returns the good sales in one CSV file and the number of bad rows, and build_week(folder). Do not change my tests. [code `examples/ai/flawed/test_report_tools.py`]
- **Narration:** The AI writes read sales, and says: it skips only the two damaged rows, so your tests pass. It sounds sure.
  **On screen:** AI chat, stage 3: Generate: code that must pass my tests
    - You: Here are my six tests. Write read_sales(path), which returns the good sales in one CSV file and the number of bad rows, and build_week(folder). Do not change my tests. [code `examples/ai/flawed/test_report_tools.py`]
    - AI (example answer): Here is `read_sales()`. It skips only the two damaged rows, so your tests pass. [code `examples/ai/flawed/report_tools.py`]
- **Narration:** Look at line 33. Then remember the first line of every till file, from step 1: item comma amount, in small letters.
  **On screen:** Code `examples/ai/flawed/report_tools.py`, line 33 highlighted, output hidden
- **Narration:** And line 35 catches every kind of exception.
  **On screen:** Code `examples/ai/flawed/report_tools.py`, line 35 highlighted, output hidden
- **Interaction:** "The till files say `item,amount`. What happens on line 33 for every row?" stays on screen with a 10-second timer.
- **Narration:** Line 33 asks for Amount, with a capital A. There is no such key, so every row raises a key error. And except Exception hides it.
  **On screen:** Code `examples/ai/flawed/report_tools.py`, line 35 highlighted, output hidden
- **Narration:** Asha does not argue. She counts the good and bad rows in each file.
  **On screen:** Code `examples/ai/flawed/rows_check.py`, line 6 highlighted, output `examples/ai/flawed/rows_check.expected`
- **Narration:** Zero good. Every row is bad. The program ran with no error, and it would report nothing.
  **On screen:** Code `examples/ai/flawed/rows_check.py`, line 6 highlighted, output `examples/ai/flawed/rows_check.expected`
- **Narration:** Her six tests agree. The first four pass, and both week tests fail.
  **On screen:** Code `examples/ai/flawed/test_report_tools.py`, output `examples/ai/flawed/test_report_tools.expected`
- **Narration:** Asha fixes it with the rule from Chapter 22: catch only the exceptions you expect. Line 33: the right key, and her own parse amount.
  **On screen:** Code `examples/ai/fixed/report_tools.py`, line 33 highlighted, output hidden
- **Narration:** Line 34 catches only the two exceptions she expects. Value error for the word four. And type error for the missing price, because float of None raises a type error, the same as the short row in Chapter 22.
  **On screen:** Code `examples/ai/fixed/report_tools.py`, line 34, 35 highlighted, output hidden
- **Narration:** Line 37 adds the sale only when nothing went wrong, in else.
  **On screen:** Code `examples/ai/fixed/report_tools.py`, line 36, 37 highlighted, output hidden
- **Narration:** Now Monday has four good rows. Tuesday and Wednesday each have one bad row. Thursday is empty.
  **On screen:** Code `examples/ai/fixed/rows_check.py`, line 6 highlighted, output `examples/ai/fixed/rows_check.expected`
- **Narration:** And she runs all six tests again. Six passed.
  **On screen:** Code `examples/ai/fixed/test_report_tools.py`, output `examples/ai/fixed/test_report_tools.expected`
- **Narration:** Quick check. A row has no price, so its amount is None. Which exception does float of None raise?
  **On screen:** Quick check: "A row has no price, so the amount is `None`. Which exception does `float(None)` raise?" (options shown)
- **Interaction:** "A row has no price, so the amount is `None`. Which exception does `float(None)` raise?" stays on screen with a 10-second timer.
- **Narration:** C. Type error. None is the wrong type of value. A word such as four is a string, so it gives a value error instead.
  **On screen:** Quick check: "A row has no price, so the amount is `None`. Which exception does `float(None)` raise?" (answer revealed: `TypeError`)

## Scene 10: Step 5: The week and the report (9:39 to 11:50)

**Section:** Build it step by step

**Direction:** build_week with glob, the day name from the file name, the week check run, then the main program in groups.

- **Narration:** Step 5. Build week puts it all together. Line 44: glob finds every file ending in dot c s v. Glob gives no fixed order, so sorted puts them in name order.
  **On screen:** Code `examples/step5/report_tools.py`, line 44 highlighted, output hidden
- **Narration:** Line 45 reads each file. Line 46 adds its bad rows to the count.
  **On screen:** Code `examples/step5/report_tools.py`, line 45, 46 highlighted, output hidden
- **Narration:** Lines 48 to 51 add each amount to its item and to the day, with get, as in Chapter 12.
  **On screen:** Code `examples/step5/report_tools.py`, line 48, 49, 50, 51 highlighted, output hidden
- **Narration:** Line 52 makes the day name from the file name. Stem drops dot c s v, split takes the part after the dash, and title gives a capital letter.
  **On screen:** Code `examples/step5/report_tools.py`, line 52 highlighted, output hidden
- **Narration:** Quick check. Why does build week sort the paths from glob?
  **On screen:** Quick check: "Why does `build_week()` sort the paths from `glob()`?" (options shown)
- **Interaction:** "Why does `build_week()` sort the paths from `glob()`?" stays on screen with a 10-second timer.
- **Narration:** A. Glob gives no fixed order. Sorted puts the names in order, and the number at the start keeps the days in order.
  **On screen:** Quick check: "Why does `build_week()` sort the paths from `glob()`?" (answer revealed: `glob()` gives no fixed order)
- **Narration:** Asha prints the days as JSON, with an indent of two, as in Chapter 23.
  **On screen:** Code `examples/step5/week_check.py`, line 7 highlighted, output hidden
- **Narration:** Thursday's file is empty, so build week adds nothing for it.
  **On screen:** Code `examples/step5/week_check.py`, line 6 highlighted, output hidden
- **Interaction:** "What total does line 8 print for the whole week?" stays on screen with a 10-second timer.
- **Narration:** 37.25. 14, plus 11.25, plus 12, plus 0 for Thursday.
  **On screen:** Code `examples/step5/week_check.py`, line 8 highlighted, output `examples/step5/week_check.expected`
- **Narration:** And two rows skipped.
  **On screen:** Code `examples/step5/week_check.py`, line 9 highlighted, output `examples/step5/week_check.expected`
- **Narration:** The main program is short. The try block holds two lines, and both raise only value error, with a clear message.
  **On screen:** Code `project/report.py`, line 7, 8, 9 highlighted, output `project/report.expected`
- **Narration:** Lines 10 and 11 catch it once, and print Report stopped, and the message.
  **On screen:** Code `project/report.py`, line 10, 11 highlighted, output `project/report.expected`
- **Narration:** The else block runs only when both worked. Lines 13 to 15 write the report, one line at a time.
  **On screen:** Code `project/report.py`, line 12, 13, 14, 15 highlighted, output `project/report.expected`
- **Narration:** Lines 16 and 17 save the week as JSON. And line 18 reads the text report back, so the screen shows exactly what was saved.
  **On screen:** Code `project/report.py`, line 16, 17, 18 highlighted, output `project/report.expected`
- **Narration:** Breather. The report works on the real week.
  **On screen:** Breather card
    - The tests caught the AI's hidden KeyError.
    - Catch only the exceptions you expect.
    - The week is built from every file.
- **Narration:** Next, Asha tries to break it with new test data.
  **On screen:** Breather card
    - The tests caught the AI's hidden KeyError.
    - Catch only the exceptions you expect.
    - The week is built from every file.
- **Breather:** 4 quiet seconds.

## Scene 11: Test it (11:50 to 14:25)

**Section:** Test it

**Direction:** Stage 4: AI test data that claims her format; compare first lines; the crash. Stage 5: the cause first, the column check, seven tests, three known-result runs.

- **Narration:** Stage 4: test. Asha asks the AI for realistic test data, in the same format as her till.
  **On screen:** AI chat, stage 4: Test: realistic test data
    - You: My real till files start with the line item,amount. Give me a small CSV file of realistic test data for my report, in the same format.
- **Narration:** The AI gives her a small file, and says it is in her till's format.
  **On screen:** AI chat, stage 4: Test: realistic test data
    - You: My real till files start with the line item,amount. Give me a small CSV file of realistic test data for my report, in the same format.
    - AI (example answer): Here is test data in your till's format. Use it as a fifth day: `Item,Amount` `Tea,$3.50` `Scone,"2,75"` `Cake,4.25`
- **Narration:** Asha compares the first line with a real till file, letter by letter.
  **On screen:** Compare the first lines
- **Narration:** The real file starts item comma amount, in small letters. Now look at the AI's first line.
  **On screen:** Compare the first lines
- **Interaction:** "What will Asha's report do with the AI's file?" stays on screen with a 10-second timer.
- **Narration:** It crashes with a key error. The AI's columns start with capital letters, so there is no key amount. And her except catches only value error and type error, not key error. Asha saves the file as a fifth day, and runs the report to see.
  **On screen:** Compare the first lines
- **Narration:** It crashes. A key error. Read the last line first: the key amount is missing.
  **On screen:** Code `examples/ai/testdata/report.py`, line 9 highlighted, error `examples/ai/testdata/report.expected_error`
- **Narration:** Then the last file line shows where: line 33 of report tools, inside read sales. On your computer, these lines show the full path of each file.
  **On screen:** Code `examples/ai/testdata/report.py`, line 9 highlighted, error `examples/ai/testdata/report.expected_error`
- **Narration:** Her except catches value error and type error, not key error. That is right: a whole file in the wrong format is not a damaged row.
  **On screen:** Code `examples/ai/testdata/report.py`, line 9 highlighted, error `examples/ai/testdata/report.expected_error`
- **Narration:** Stage 5: debug. Asha pastes the error, and asks for the cause first, then the smallest fix.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: My report crashed with KeyError: 'amount' on a file you gave me. First explain the cause. Then show the smallest fix.
- **Narration:** The AI explains: Dict reader uses the first line as the keys, exactly as written. Its fix checks the column names before the loop.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: My report crashed with KeyError: 'amount' on a file you gave me. First explain the cause. Then show the smallest fix.
    - AI (example answer): `DictReader` uses the first line as the keys, exactly as written. That file says `Amount`, so there is no key `amount`. The fix: check the column names before the loop, and raise a `ValueError` with a clear message. [code `project/report_tools.py`]
- **Narration:** Field names is the list of names from the first line. An empty file has none, so if columns lets Thursday through.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: My report crashed with KeyError: 'amount' on a file you gave me. First explain the cause. Then show the smallest fix.
    - AI (example answer): `DictReader` uses the first line as the keys, exactly as written. That file says `Amount`, so there is no key `amount`. The fix: check the column names before the loop, and raise a `ValueError` with a clear message. [code `project/report_tools.py`]
- **Narration:** She runs the report on the same file. One clear line: the file needs item and amount. No crash.
  **On screen:** Code `examples/ai/debug/report.py`, line 10, 11 highlighted, output `examples/ai/debug/report.expected`
- **Narration:** Asha keeps the AI's file as test data, and adds a seventh test. Read sales must raise a value error for it.
  **On screen:** Code `project/test_report_tools.py`, line 40, 41 highlighted, output `project/test_report_tools.expected`
- **Narration:** Then she runs every test again. Seven passed.
  **On screen:** Code `project/test_report_tools.py`, line 40, 41 highlighted, output `project/test_report_tools.expected`
- **Narration:** Last, Asha runs the whole report on three more folders. She writes the expected result first.
  **On screen:** Table: Three more runs, with known results
- **Narration:** No settings file at all.
  **On screen:** Table: Three more runs, with known results (row 1 in focus)
- **Narration:** A settings file that is missing a comma.
  **On screen:** Table: Three more runs, with known results (row 2 in focus)
- **Narration:** And a week where the cafe was closed every day but Thursday's empty file.
  **On screen:** Table: Three more runs, with known results (row 3 in focus)
- **Narration:** No settings file. One clear line. Pass.
  **On screen:** Code `examples/cases/missing_config/report.py`, line 8 highlighted, output `examples/cases/missing_config/report.expected`
- **Narration:** Broken settings. The JSON module's reason: expecting a comma. Pass.
  **On screen:** Code `examples/cases/bad_json/report.py`, line 8 highlighted, output `examples/cases/bad_json/report.expected`
- **Narration:** And the closed week. Only Thursday, and every amount is 0.00. Pass. All three match.
  **On screen:** Code `examples/cases/closed_week/report.py`, line 9 highlighted, output `examples/cases/closed_week/report.expected`

## Scene 12: Improve it with AI (14:25 to 16:07)

**Section:** Improve it with AI

**Direction:** Stage 6: round each day. Ask what Tuesday becomes, then the test run. Six stages table, breather.

- **Narration:** Stage 6: improve. All seven tests pass. Asha asks for one improvement, and says: do not change what the totals are.
  **On screen:** AI chat, stage 6: Improve: a clearer report
    - You: All seven tests pass. Suggest one improvement that makes the report clearer. Do not change what the totals are.
- **Narration:** The AI says: round each day's total to a whole number before you store it. Tidy amounts.
  **On screen:** AI chat, stage 6: Improve: a clearer report
    - You: All seven tests pass. Suggest one improvement that makes the report clearer. Do not change what the totals are.
    - AI (example answer): Round each day's total to a whole number before you store it: `day_total = round(day_total)`. The report will show tidy amounts.
- **Narration:** Here is the AI's change, on line 56. Tuesday's real total is 11.25. Round with no second value gives the nearest whole number, as in Chapter 18.
  **On screen:** Code `examples/ai/improve/report_tools.py`, line 56 highlighted, output hidden
- **Interaction:** "With the AI's line 56, what is Tuesday's total?" stays on screen with a 10-second timer.
- **Narration:** 11. And the week becomes 37 instead of 37.25. Asha runs her tests to be sure.
  **On screen:** Code `examples/ai/improve/report_tools.py`, line 56 highlighted, output hidden
- **Narration:** Two tests fail: the week total, and the day that must not be rounded.
  **On screen:** Code `examples/ai/improve/test_report_tools.py`, line 30, 36 highlighted, output `examples/ai/improve/test_report_tools.expected`
- **Narration:** The suggestion broke her rule: it changed the totals. Rounding belongs in the display, and money already shows two decimal places. Asha keeps her version.
  **On screen:** Code `examples/ai/improve/test_report_tools.py`, line 30, 36 highlighted, output `examples/ai/improve/test_report_tools.expected`
- **Narration:** Here are all six stages, on one module of rules.
  **On screen:** Table: Six stages, one module of rules
- **Narration:** The AI helped at every stage, from the plan to the improvement.
  **On screen:** Table: Six stages, one module of rules (row 1 in focus)
- **Narration:** And it was confidently wrong five times: the plan, a negative price, a hidden key error, test data in the wrong format, and rounding.
  **On screen:** Table: Six stages, one module of rules (row 3 in focus)
- **Narration:** Every time, something Asha did first caught it: looking at real files, comparing, and her tests.
  **On screen:** Table: Six stages, one module of rules (row 6 in focus)
- **Narration:** Last breather. Before she pasted any code into the chat, Asha checked it for private data. The till files hold only items and amounts.
  **On screen:** Breather card
    - AI test data must match your real files.
    - A clear message beats a crash and a silence.
    - Round only for display.
- **Narration:** Let's recap.
  **On screen:** Breather card
    - AI test data must match your real files.
    - A clear message beats a crash and a silence.
    - Round only for display.
- **Breather:** 4 quiet seconds.

## Scene 13: Recap (16:07 to 17:34)

**Section:** Recap

**Direction:** Recap points one by one, a final quiz on rounding, the badge and the practice table.

- **Narration:** Here is what you used in this boss level.
  **On screen:** Recap
- **Narration:** Look at the real data first. Damaged rows are normal.
  **On screen:** Recap
    - Look at the real data first. Damaged rows are normal.
- **Narration:** Small functions, and a small try around the one line that can fail.
  **On screen:** Recap
    - Look at the real data first. Damaged rows are normal.
    - Small functions, and a small `try` around the one line that can fail.
- **Narration:** Catch the exceptions you expect. Except Exception can hide a bug.
  **On screen:** Recap
    - Look at the real data first. Damaged rows are normal.
    - Small functions, and a small `try` around the one line that can fail.
    - Catch the exceptions you expect. `except Exception` can hide a bug.
- **Narration:** Turn file and JSON errors into one clear message, and catch it once.
  **On screen:** Recap
    - Look at the real data first. Damaged rows are normal.
    - Small functions, and a small `try` around the one line that can fail.
    - Catch the exceptions you expect. `except Exception` can hide a bug.
    - Turn file and JSON errors into one clear message, caught once.
- **Narration:** Check AI test data against a real file, and keep it as a test.
  **On screen:** Recap
    - Look at the real data first. Damaged rows are normal.
    - Small functions, and a small `try` around the one line that can fail.
    - Catch the exceptions you expect. `except Exception` can hide a bug.
    - Turn file and JSON errors into one clear message, caught once.
    - Check AI test data against a real file, and keep it as a test.
- **Narration:** And round only when you display a number.
  **On screen:** Recap
    - Look at the real data first. Damaged rows are normal.
    - Small functions, and a small `try` around the one line that can fail.
    - Catch the exceptions you expect. `except Exception` can hide a bug.
    - Turn file and JSON errors into one clear message, caught once.
    - Check AI test data against a real file, and keep it as a test.
    - Round only when you display a number.
- **Narration:** One last check. Monday is 2.4 and Tuesday is 2.4. Which line shows the correct total?
  **On screen:** Quick check: "Monday is 2.4 and Tuesday is 2.4. Which line shows the correct total?" (options shown)
- **Interaction:** "Monday is 2.4 and Tuesday is 2.4. Which line shows the correct total?" stays on screen with a 10-second timer.
- **Narration:** B. Add the exact amounts first: 4.8. Then show it with two decimal places.
  **On screen:** Quick check: "Monday is 2.4 and Tuesday is 2.4. Which line shows the correct total?" (answer revealed: Add, then show with `:.2f`: 4.80)
- **Narration:** Boss level complete! You earned 300 XP and the Report Master badge. And Module 5 is done.
  **On screen:** Report Master You earned 300 XP. Module 5 is complete.
- **Breather:** 2 quiet seconds.
- **Narration:** The practice file has eight more tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-ups, worth 10 XP each, such as reading one till file.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including a clear message for missing settings.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's report that rounds before it adds.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Look at your data first, then write the rule.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 14: What's next (17:34 to 17:59)

**Section:** What's next

**Direction:** End card. Tease classes: a sale is a pair, a day a dictionary; next, types with their own data and rules. Hold quietly.

- **Narration:** Asha's report keeps each sale as a pair of an item and an amount, and each day as a dictionary. The rules live somewhere else.
  **On screen:** Classes and Objects: Modelling Real Things Your own types, with their data and their rules together.
- **Narration:** In Chapter 26, you will build your own types with classes, so a sale or a day carries its data and its own rules together.
  **On screen:** Classes and Objects: Modelling Real Things Your own types, with their data and their rules together.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Classes and Objects: Modelling Real Things Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 26.
  **On screen:** Classes and Objects: Modelling Real Things Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
