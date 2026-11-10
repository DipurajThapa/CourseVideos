# Video Script: Chapter 21: Files and Paths: Saving and Loading Data

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:41.

## Scene 1: Introduction (0:00 to 0:41)

**Section:** Introduction

**Direction:** Open on the Chapter 20 problem: the quiz forgets every score. Then the title and the AI tease, then the mission code with no output.

- **Narration:** At the Corner Cafe, Asha's staff quiz from Chapter 20 works well. Lina scores 4 out of 4.
  **On screen:** Every score disappears
- **Narration:** Then the app closes. The next morning, Asha runs it again, and every score is gone.
  **On screen:** Every score disappears
- **Narration:** This is Code Quest, Chapter 21. Today, data learns to survive.
  **On screen:** Files and Paths: Saving and Loading Data
- **Narration:** And an AI assistant will promise a function that keeps every score. It will sound completely sure. You will check the file yourself.
  **On screen:** Files and Paths: Saving and Loading Data Save it. Load it. Check the file.
- **Narration:** Here is today's mission: Asha's score board. Lines 7 and 8 save the new score to a file.
  **On screen:** Code `examples/ex08_score_board.py`, line 7, 8 highlighted, output hidden
- **Narration:** Lines 11 to 16 load every score from earlier rounds. Let's build it, piece by piece.
  **On screen:** Code `examples/ex08_score_board.py`, line 11, 12, 13, 14, 15, 16 highlighted, output hidden

## Scene 2: Learning goals (0:41 to 0:56)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Write a text file, and read it back.
  **On screen:** By the end, you will be able to:
    - Write and read a text file with `pathlib` and `open()`.
- **Narration:** Choose the right mode: write, add or read.
  **On screen:** By the end, you will be able to:
    - Write and read a text file with `pathlib` and `open()`.
    - Choose the mode: `"w"` writes new, `"a"` adds, `"r"` reads.
- **Narration:** Read a file line by line.
  **On screen:** By the end, you will be able to:
    - Write and read a text file with `pathlib` and `open()`.
    - Choose the mode: `"w"` writes new, `"a"` adds, `"r"` reads.
    - Read a file line by line and remove each newline.
- **Narration:** Save and load tables as CSV files.
  **On screen:** By the end, you will be able to:
    - Write and read a text file with `pathlib` and `open()`.
    - Choose the mode: `"w"` writes new, `"a"` adds, `"r"` reads.
    - Read a file line by line and remove each newline.
    - Save and load table data as a CSV file.
- **Narration:** And fix the common file errors, with an AI assistant.
  **On screen:** By the end, you will be able to:
    - Write and read a text file with `pathlib` and `open()`.
    - Choose the mode: `"w"` writes new, `"a"` adds, `"r"` reads.
    - Read a file line by line and remove each newline.
    - Save and load table data as a CSV file.
    - Explain common file errors and fix them, with an AI assistant.

## Scene 3: Why this matters (0:56 to 1:15)

**Section:** Why this matters

**Direction:** Memory versus disk, then real uses.

- **Narration:** Why did the scores vanish? Variables live in the computer's memory, and memory is cleared when the program stops.
  **On screen:** Why this matters
    - Variables live in memory. Memory is cleared when the program stops.
- **Narration:** A file is data saved on the disk, with a name. It stays there, so the next run can load it.
  **On screen:** Why this matters
    - Variables live in memory. Memory is cleared when the program stops.
    - A **file** is data saved on the disk, with a name. It stays.
- **Narration:** Saved games, app settings, a shop's sales: they are all files.
  **On screen:** Why this matters
    - Variables live in memory. Memory is cleared when the program stops.
    - A **file** is data saved on the disk, with a name. It stays.
    - Saved games, settings, sales and spreadsheets are all files.

## Scene 4: The idea: open, read or write, close (1:15 to 2:54)

**Section:** The idea

**Direction:** Teach the three steps, the three modes, the order-book analogy and encoding. Quiz on modes. Breather.

- **Narration:** A program talks to a file in three steps. Open the file. Read from it, or write to it. Then close it.
  **On screen:** Open, read or write, close
- **Narration:** The memory side is lost at the end. The disk side stays.
  **On screen:** Open, read or write, close
- **Narration:** When you open a file, the mode says what you want to do.
  **On screen:** Table: The mode says what you want
- **Narration:** R reads. It is the default, and the file must already exist.
  **On screen:** Table: The mode says what you want (row 1 in focus)
- **Narration:** W writes. It creates the file, or empties it first if it already exists.
  **On screen:** Table: The mode says what you want (row 2 in focus)
- **Narration:** A appends. It adds to the end, and creates the file if it is missing.
  **On screen:** Table: The mode says what you want (row 3 in focus)
- **Narration:** Think of the cafe's order book. You can read it, start a new empty book, or add a line at the end.
  **On screen:** A file is like the cafe's order book
    - You can read it, start a new book, or add a line at the end.
- **Narration:** But a person would never tear out every page by accident. Mode W empties the file with no warning.
  **On screen:** A file is like the cafe's order book
    - You can read it, start a new book, or add a line at the end.
    - Unlike a person, mode `"w"` empties the book with no warning.
- **Narration:** One more idea. A file stores bytes, not letters. An encoding is the rule that turns letters into bytes, and back.
  **On screen:** Text and encoding
- **Narration:** UTF-8 is the standard. It stores every language, including the e with an accent in Café. Older versions of Python can use a different encoding on some computers, mostly on Windows. So always write encoding equals utf 8.
  **On screen:** Text and encoding
- **Narration:** Quick check. Asha wants to add a line and keep the old ones. Which mode?
  **On screen:** Quick check: "Asha wants to add a line to the end of a file and keep the old lines. Which mode?" (options shown)
- **Interaction:** "Asha wants to add a line to the end of a file and keep the old lines. Which mode?" stays on screen with a 10-second timer.
- **Narration:** B. Append. W would empty the file first.
  **On screen:** Quick check: "Asha wants to add a line to the end of a file and keep the old lines. Which mode?" (answer revealed: `"a"`)
- **Narration:** Breather. Three steps, three modes. That is the whole idea.
  **On screen:** Breather card
    - Memory is lost; files stay.
    - Open, read or write, close.
    - `"w"` empties, `"a"` adds, `"r"` reads.
- **Narration:** Next, Asha writes her first file.
  **On screen:** Breather card
    - Memory is lost; files stay.
    - Open, read or write, close.
    - `"w"` empties, `"a"` adds, `"r"` reads.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Write and read with pathlib (2:54 to 3:36)

**Section:** Build it step by step

**Direction:** The code types in. Teach exists() before the ask. Reveal, then explain the empty line.

- **Narration:** Step 1. You met Path in Chapter 18. Line 4 makes a path for a file called note dot t x t.
  **On screen:** Code `examples/ex01_write_read.py`, lines 1 to 4 typed in, line 4 highlighted, output hidden
- **Narration:** Line 5 writes the whole text into the file. The text ends with backslash n, a new line.
  **On screen:** Code `examples/ex01_write_read.py`, lines 1 to 5 typed in, line 5 highlighted, output hidden
- **Narration:** Line 6 reads the whole file back as one string, and prints it.
  **On screen:** Code `examples/ex01_write_read.py`, lines 1 to 6 typed in, line 6 highlighted, output hidden
- **Narration:** Line 7 asks: does this file exist now?
  **On screen:** Code `examples/ex01_write_read.py`, lines 1 to 7 typed in, line 7 highlighted, output hidden
- **Interaction:** "What does line 7 print?" stays on screen with a 10-second timer.
- **Narration:** True. Line 5 created the file.
  **On screen:** Code `examples/ex01_write_read.py`, lines 1 to 7 typed in, line 7 highlighted, output `examples/ex01_write_read.expected`
- **Narration:** And see the empty line? The text already ends with a new line, and print adds another one.
  **On screen:** Code `examples/ex01_write_read.py`, lines 1 to 7 typed in, line 6 highlighted, output `examples/ex01_write_read.expected`

## Scene 6: Step 2: Modes and the with statement (3:36 to 4:20)

**Section:** Build it step by step

**Direction:** Teach with and the three blocks, then predict the read.

- **Narration:** Step 2. The with statement opens a file, and closes it again when the indented block ends, even if an error happens.
  **On screen:** Code `examples/ex02_modes.py`, line 2 highlighted, output hidden
- **Narration:** Lines 2 to 4 use mode W, and write two lines. Write does not add a new line by itself, so each text ends with backslash n.
  **On screen:** Code `examples/ex02_modes.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Lines 6 and 7 use mode A, and write Lina.
  **On screen:** Code `examples/ex02_modes.py`, line 6, 7 highlighted, output hidden
- **Narration:** Line 9 has no mode, so it reads.
  **On screen:** Code `examples/ex02_modes.py`, line 9, 10 highlighted, output hidden
- **Interaction:** "What does line 10 print?" stays on screen with a 10-second timer.
- **Narration:** All three names. Mode A added Lina, and kept Asha and Omar.
  **On screen:** Code `examples/ex02_modes.py`, line 6, 7 highlighted, output `examples/ex02_modes.expected`
- **Narration:** And end equals empty, from Chapter 1, stops print from adding that extra empty line.
  **On screen:** Code `examples/ex02_modes.py`, line 10 highlighted, output `examples/ex02_modes.expected`

## Scene 7: Step 3: Read line by line (4:20 to 5:04)

**Section:** Build it step by step

**Direction:** Show the menu file, then the loop. Teach that each line ends with a newline before the ask.

- **Narration:** Step 3. The cafe menu is a small text file, one item per line.
  **On screen:** The menu file
- **Narration:** A file opened for reading works in a for loop. Line 3 gives one line at a time.
  **On screen:** Code `examples/ex03_lines.py`, line 3 highlighted, output hidden
- **Narration:** Each line ends with its new line. Strip, from Chapter 3, removes spaces and new lines from both ends.
  **On screen:** Code `examples/ex03_lines.py`, line 4 highlighted, output hidden
- **Narration:** Line 5 prints the name and its number of letters.
  **On screen:** Code `examples/ex03_lines.py`, line 5 highlighted, output hidden
- **Interaction:** "How many letters does line 5 report for Tea?" stays on screen with a 10-second timer.
- **Narration:** 3. Without strip, the hidden new line would make it 4.
  **On screen:** Code `examples/ex03_lines.py`, line 5 highlighted, output `examples/ex03_lines.expected`
- **Narration:** And Café keeps its accent, because the file was read as UTF-8.
  **On screen:** Code `examples/ex03_lines.py`, line 2 highlighted, output `examples/ex03_lines.expected`

## Scene 8: Steps 4 and 5: Check first, and build paths (5:04 to 6:08)

**Section:** Build it step by step

**Direction:** exists() with if and else, then relative paths. One ask, then a breather.

- **Narration:** Step 4. Reading a missing file stops the program. So line 5 checks first, with exists and an if.
  **On screen:** Code `examples/ex04_exists.py`, line 5 highlighted, output hidden
- **Narration:** Read lines 5 to 8, and the note above the code.
  **On screen:** Code `examples/ex04_exists.py`, line 5, 6, 7, 8 highlighted, output hidden
- **Interaction:** "Which line prints: line 6 or line 8?" stays on screen with a 10-second timer.
- **Narration:** Line 8. The file does not exist, so the else block runs.
  **On screen:** Code `examples/ex04_exists.py`, line 8 highlighted, output `examples/ex04_exists.expected`
- **Narration:** Step 5. A relative path, like scores dot csv, is looked up in the working directory: the folder you run the program from.
  **On screen:** Code `examples/ex05_paths.py`, line 4 highlighted, output hidden
- **Narration:** Line 4 joins a folder and a file name with a slash. It works on every computer.
  **On screen:** Code `examples/ex05_paths.py`, line 4 highlighted, output hidden
- **Narration:** Lines 5 to 8 print the path, its name and suffix, its parent folder, and whether it exists.
  **On screen:** Code `examples/ex05_paths.py`, line 5, 6, 7, 8 highlighted, output `examples/ex05_paths.expected`
- **Narration:** There is no reports folder yet, so exists is False.
  **On screen:** Code `examples/ex05_paths.py`, line 8 highlighted, output `examples/ex05_paths.expected`
- **Narration:** Breather. You can write, add, read, and check a file.
  **On screen:** Breather card
    - `with open()` closes the file for you.
    - `strip()` removes each line's newline.
    - Check with `exists()` before you read.
- **Narration:** Now, tables. The cafe's sales live in a CSV file.
  **On screen:** Breather card
    - `with open()` closes the file for you.
    - `strip()` removes each line's newline.
    - Check with `exists()` before you read.
- **Breather:** 4 quiet seconds.

## Scene 9: Steps 6 and 7: CSV files (6:08 to 7:51)

**Section:** Build it step by step

**Direction:** Write a CSV file, then read one with DictReader. Teach strings before the ask and the quiz.

- **Narration:** Step 6. A CSV file stores a table as text: one row per line, with commas between the values.
  **On screen:** Code `examples/ex06_csv_write.py`, line 4 highlighted, output hidden
- **Narration:** Line 4 opens it with newline equals empty. The Python documentation asks for this, so the C S V module controls the line endings.
  **On screen:** Code `examples/ex06_csv_write.py`, line 4 highlighted, output hidden
- **Narration:** Line 5 makes a writer. Each writerow takes a list, and writes one row. The first row is the header: the column names.
  **On screen:** Code `examples/ex06_csv_write.py`, line 5, 6, 7, 8 highlighted, output hidden
- **Narration:** Line 10 reads it back as plain text, not with the C S V module, so it opens the file normally.
  **On screen:** Code `examples/ex06_csv_write.py`, line 10, 11 highlighted, output `examples/ex06_csv_write.expected`
- **Narration:** Step 7. Here are the day's sales: item, quantity and price.
  **On screen:** The day's sales
- **Narration:** Line 6 uses DictReader. It reads the header, then gives each row as a dictionary, with the column names as keys.
  **On screen:** Code `examples/ex07_csv_read.py`, line 6 highlighted, output hidden
- **Narration:** Every value comes back as text, even twelve. So line 7 converts with int and float, from Chapter 4.
  **On screen:** Code `examples/ex07_csv_read.py`, line 7 highlighted, output hidden
- **Narration:** Line 8 adds each amount to the total, and line 9 prints the item and its amount.
  **On screen:** Code `examples/ex07_csv_read.py`, line 8, 9 highlighted, output hidden
- **Interaction:** "What amount does output line 1 show for Tea?" stays on screen with a 10-second timer.
- **Narration:** 42.00. Twelve teas at 3.50.
  **On screen:** Code `examples/ex07_csv_read.py`, line 7 highlighted, output `examples/ex07_csv_read.expected`
- **Narration:** And line 10 prints the total, 85.00.
  **On screen:** Code `examples/ex07_csv_read.py`, line 10 highlighted, output `examples/ex07_csv_read.expected`
- **Narration:** Quick check. Dict reader reads the row: tea, twelve, three fifty. What type is the quantity?
  **On screen:** Quick check: "`DictReader` reads the row `Tea,12,3.50`. What type is `row["qty"]`?" (options shown)
- **Interaction:** "`DictReader` reads the row `Tea,12,3.50`. What type is `row["qty"]`?" stays on screen with a 10-second timer.
- **Narration:** C. A string. Every value from a C S V file is text.
  **On screen:** Quick check: "`DictReader` reads the row `Tea,12,3.50`. What type is `row["qty"]`?" (answer revealed: `str`)

## Scene 10: See the outcome: the score board (7:51 to 8:47)

**Section:** See the outcome

**Direction:** Return to the mission. Show the starting file, walk the code, ask about the tie, reveal, then hand over to the AI.

- **Narration:** Back to the mission. The score file already holds two rounds: Asha with 4, and Omar with 3.
  **On screen:** The score file before the run
- **Narration:** Lines 4 and 5 hold today's new score: Lina, with 4.
  **On screen:** Code `examples/ex08_score_board.py`, line 4, 5 highlighted, output hidden
- **Narration:** Lines 7 and 8 append it, in mode A, so the old rows stay.
  **On screen:** Code `examples/ex08_score_board.py`, line 7, 8 highlighted, output hidden
- **Narration:** Lines 11 to 14 read every row, convert the score, and print it.
  **On screen:** Code `examples/ex08_score_board.py`, line 11, 12, 13, 14 highlighted, output hidden
- **Narration:** Line 15 replaces the best score only when a score is bigger.
  **On screen:** Code `examples/ex08_score_board.py`, line 15, 16 highlighted, output hidden
- **Interaction:** "Asha and Lina both have 4. Who does line 18 name as best?" stays on screen with a 10-second timer.
- **Narration:** Asha. Lina's 4 is not bigger than 4, so the first one stays.
  **On screen:** Code `examples/ex08_score_board.py`, line 18 highlighted, output `examples/ex08_score_board.expected`
- **Narration:** And Lina is saved. Run it again, and she appears twice. The file remembers every run!
  **On screen:** Code `examples/ex08_score_board.py`, line 7, 8 highlighted, output `examples/ex08_score_board.expected`
- **Narration:** Now Asha wants the quiz app itself to save each score. She builds a save function with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex08_score_board.py`, output `examples/ex08_score_board.expected`

## Scene 11: Work with AI: a save function that keeps every score (8:47 to 13:09)

**Section:** Work with AI

**Direction:** Safety first. Six stages on save_score. Stage 3 plants mode w; tests catch it; debug a missing folder; improve breaks the header rule.

- **Narration:** This chapter's AI skill is safe file handling. Some file mistakes destroy data with no error at all.
  **On screen:** This chapter's AI skill: safe file handling
    - Some file mistakes destroy data with no error.
- **Narration:** So test file code on a copy, and read the file afterwards.
  **On screen:** This chapter's AI skill: safe file handling
    - Some file mistakes destroy data with no error.
    - Test file code on a copy, then read the file afterwards.
- **Narration:** And never paste private data. A file of real names and scores is private, so paste a made-up sample.
  **On screen:** This chapter's AI skill: safe file handling
    - Some file mistakes destroy data with no error.
    - Test file code on a copy, then read the file afterwards.
    - Customer names and scores are private: paste a made-up sample.
- **Narration:** Stage 1: plan. Asha describes the data to save, and asks for no code yet.
  **On screen:** AI chat, stage 1: Plan: file, format and mode
    - You: I am a beginner. My quiz app must save a name and a score after every round, so the next run can load them. Do not write code yet. Which file, format and mode should I use?
- **Narration:** The AI suggests a C S V file, mode A, and a header only when the file is new. That matches what you learned.
  **On screen:** AI chat, stage 1: Plan: file, format and mode
    - You: I am a beginner. My quiz app must save a name and a score after every round, so the next run can load them. Do not write code yet. Which file, format and mode should I use?
    - AI (example answer): 1. A CSV file, scores.csv, with the header name,score. 2. Mode "a", so the old rows stay. 3. Write the header only when the file is new. 4. Open it with newline="" and encoding="utf-8".
- **Narration:** Stage 2: write. Asha writes her own save function first. Line 7 asks if the file is new. Lines 10 and 11 write the header only then.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote this function myself. Do not rewrite it. What happens to the file on the first call, and on the second? [code `examples/ai_mine.py`]
- **Narration:** She asks the AI to explain what each call does to the file, without rewriting it.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote this function myself. Do not rewrite it. What happens to the file on the first call, and on the second? [code `examples/ai_mine.py`]
    - AI (example answer): First call: the file is new, so it writes the header, then Asha's row. Second call: the file exists, so it adds only Omar's row.
- **Narration:** She calls it twice, and reads the file. It matches the explanation.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote this function myself. Do not rewrite it. What happens to the file on the first call, and on the second? [code `examples/ai_mine.py`]
    - AI (example answer): First call: the file is new, so it writes the header, then Asha's row. Second call: the file exists, so it adds only Omar's row.
    - You: I called it twice and read the file. It matches:
- **Narration:** Stage 3: generate. Asha wants to compare. She asks the AI for the same function, from a short request.
  **On screen:** AI chat, stage 3: Generate: a function from a request
    - You: Write save_score(path, name, score). It saves a quiz score to a CSV file with a header. It must keep every score.
- **Narration:** The AI answers with confidence: it keeps every score you save.
  **On screen:** AI chat, stage 3: Generate: a function from a request
    - You: Write save_score(path, name, score). It saves a quiz score to a CSV file with a header. It must keep every score.
    - AI (example answer): Here it is. It keeps every score you save. [code `examples/ai_save_flawed.py`]
- **Narration:** Look at line 6, and remember the three modes. Lines 11 and 12 save Asha, then Omar.
  **On screen:** Code `examples/ai_save_flawed.py`, line 6, 11, 12 highlighted, output hidden
- **Interaction:** "The AI says it keeps every score. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Asha's score is gone. Mode W empties the file on every call, so only Omar survives.
  **On screen:** Code `examples/ai_save_flawed.py`, line 6 highlighted, output `examples/ai_save_flawed.expected`
- **Narration:** Stage 4: test. Asha asks for test cases, each with the exact text the file should hold.
  **On screen:** AI chat, stage 4: Test: the exact file after each case
    - You: Give me test cases for save_score. For each one, write the exact text the file should hold afterwards.
- **Narration:** The AI lists three: a new file, two saves, and an old file with data in it.
  **On screen:** AI chat, stage 4: Test: the exact file after each case
    - You: Give me test cases for save_score. For each one, write the exact text the file should hold afterwards.
    - AI (example answer): 1. New file, save Asha: the header, then Asha,4. 2. Two saves, Asha then Omar: the header and both rows. 3. An old file with Asha, save Lina: Lina after Asha.
- **Narration:** She runs all three cases on the AI's function. Case 1 passes. Cases 2 and 3 fail: both lost a row, with no error.
  **On screen:** Code `examples/ai_tests_flawed.py`, line 6 highlighted, output `examples/ai_tests_flawed.expected`
- **Narration:** Asha shows the AI its failing cases, and asks for the cause, then a fix.
  **On screen:** AI chat, stage 4: Test: report the failures, ask for a fix
    - You: Cases 2 and 3 fail on your function: each lost a row, with no error. Explain why, then fix it so every case passes.
- **Narration:** The AI names mode W, and suggests mode A, with the header only for a new file.
  **On screen:** AI chat, stage 4: Test: report the failures, ask for a fix
    - You: Cases 2 and 3 fail on your function: each lost a row, with no error. Explain why, then fix it so every case passes.
    - AI (example answer): Mode "w" empties the file on every call. Use mode "a", and write the header only when the file is new.
- **Narration:** Here is the fix: mode A, and the header only when the file is new. The same idea as Asha's own version.
  **On screen:** Code `examples/ai_save_fixed.py`, line 7, 8, 10, 11 highlighted, output `examples/ai_save_fixed.expected`
- **Narration:** Two saves now keep both rows.
  **On screen:** Code `examples/ai_save_fixed.py`, line 15, 16 highlighted, output `examples/ai_save_fixed.expected`
- **Narration:** And she runs all three cases again. All three pass.
  **On screen:** Code `examples/ai_tests_append.py`, line 7, 8 highlighted, output `examples/ai_tests_append.expected`
- **Narration:** Stage 5: debug. Asha moves the scores into a data folder. Line 15 saves to data, slash, week dot c s v.
  **On screen:** Code `examples/ai_folder_crash.py`, line 15 highlighted, error `examples/ai_folder_crash.expected_error`
- **Narration:** File not found! The report points at line 8, inside the function.
  **On screen:** Code `examples/ai_folder_crash.py`, line 8 highlighted, error `examples/ai_folder_crash.expected_error`
- **Narration:** She pastes the error into the chat, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I moved the scores into a data folder. Line 15 now saves to data/week.csv, and I got FileNotFoundError: No such file or directory: 'data/week.csv'. First explain the cause. Then show the smallest fix.
- **Narration:** The AI explains. Mode A creates a missing file, but not a missing folder. The fix makes the folder, only if it is missing.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I moved the scores into a data folder. Line 15 now saves to data/week.csv, and I got FileNotFoundError: No such file or directory: 'data/week.csv'. First explain the cause. Then show the smallest fix.
    - AI (example answer): Line 8 opens data/week.csv, but there is no data folder. Mode "a" creates a missing file, not a missing folder. Fix: start the function with Path(path).parent.mkdir(exist_ok=True). It makes the folder only if it is missing. For a folder inside a folder, add parents=True too.
- **Narration:** Line 7 is the fix. Then Asha runs every case again, plus a fourth: a file in a folder. All four pass.
  **On screen:** Code `examples/ai_tests_fixed.py`, line 7 highlighted, output `examples/ai_tests_fixed.expected`
- **Narration:** Stage 6: improve. Asha asks for one improvement that does not change the file.
  **On screen:** AI chat, stage 6: Improve: one suggestion, then every test
    - You: All four cases pass. Suggest at most one improvement, with one reason. Do not change what the file contains.
- **Narration:** The AI says: write the header on every save, because C S V readers skip repeated headers.
  **On screen:** AI chat, stage 6: Improve: one suggestion, then every test
    - You: All four cases pass. Suggest at most one improvement, with one reason. Do not change what the file contains.
    - AI (example answer): Remove the exists check and write the header on every save. It is simpler, and CSV readers skip repeated headers.
- **Narration:** Here is the shorter version. Line 10 runs on every call. Picture the file after two saves.
  **On screen:** Code `examples/ai_tests_improve.py`, line 10 highlighted, output hidden
- **Interaction:** "Will case 2, two saves, still pass?" stays on screen with a 10-second timer.
- **Narration:** No. Cases 2 and 3 fail: the header is written twice.
  **On screen:** Code `examples/ai_tests_improve.py`, line 10 highlighted, output `examples/ai_tests_improve.expected`
- **Narration:** And Dict reader uses only the first row as the header, so the second header becomes a data row. The AI was wrong again. Asha keeps her check.
  **On screen:** Code `examples/ai_tests_improve.py`, line 10 highlighted, output `examples/ai_tests_improve.expected`
- **Narration:** Quick check. An AI's file function runs with no error. What shows that it keeps every row?
  **On screen:** Quick check: "An AI's file function runs with no error. What shows that it keeps every row?" (options shown)
- **Interaction:** "An AI's file function runs with no error. What shows that it keeps every row?" stays on screen with a 10-second timer.
- **Narration:** D. Read the file after two saves. No error does not mean no data lost.
  **On screen:** Quick check: "An AI's file function runs with no error. What shows that it keeps every row?" (answer revealed: Reading the file after two saves)
- **Narration:** Breather. The AI made two confident mistakes, and Asha's tests caught both.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Mode `"w"` can lose data with no error.
    - Read the file after every test.
- **Narration:** Next, the four file mistakes every beginner meets.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Mode `"w"` can lose data with no error.
    - Read the file after every test.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes (13:09 to 15:32)

**Section:** Common mistakes

**Direction:** Mistake 1 is a typo in a file name. Mistakes 2 and 4 are spot-it asks. Then a table and a quiz.

- **Narration:** Mistake 1. The file is called scores, with an s. Line 3 asks for score, without one.
  **On screen:** Code `examples/err01_missing_file.py`, line 3 highlighted, error `examples/err01_missing_file.expected_error`
- **Narration:** Line 2 printed, then Python stopped: file not found, with the exact name it looked for.
  **On screen:** Code `examples/err01_missing_file.py`, line 3 highlighted, error `examples/err01_missing_file.expected_error`
- **Narration:** Check the spelling, and run the program from the folder that holds the file. A relative path is looked up in the working directory.
  **On screen:** Code `examples/err01_missing_file.py`, line 3 highlighted, error `examples/err01_missing_file.expected_error`
- **Narration:** Now you try. The cafe log has three lines. This program meant to add one more.
  **On screen:** Code `examples/err02_w_erases.py`, line 2 highlighted, output hidden
- **Interaction:** "How many lines does the log have after this program runs?" stays on screen with a 10-second timer.
- **Narration:** One. Mode W emptied the file first. There was no error, and the three old lines are gone.
  **On screen:** Code `examples/err02_w_erases.py`, line 2 highlighted, output `examples/err02_w_erases.expected`
- **Narration:** The fix: use A to add. Use W only when you want to start again.
  **On screen:** Code `examples/err02_w_erases.py`, line 2 highlighted, output `examples/err02_w_erases.expected`
- **Narration:** Mistake 3. An old cash register saved its menu with a different encoding. Line 3 reads it as UTF-8, and fails at the e with an accent.
  **On screen:** Code `examples/err03_encoding.py`, line 3 highlighted, error `examples/err03_encoding.expected_error`
- **Narration:** Find out which encoding saved the file, read it once with that encoding, and save it again as UTF-8.
  **On screen:** Code `examples/err03_encoding.py`, line 3 highlighted, error `examples/err03_encoding.expected_error`
- **Narration:** One more. Remember what Dict reader gives back.
  **On screen:** Code `examples/err04_text_numbers.py`, line 7 highlighted, output hidden
- **Interaction:** "What is wrong with line 7?" stays on screen with a 10-second timer.
- **Narration:** The price is text, and Python cannot add text to a float.
  **On screen:** Code `examples/err04_text_numbers.py`, line 7 highlighted, error `examples/err04_text_numbers.expected_error`
- **Narration:** The fix: convert first, with float.
  **On screen:** Code `examples/err04_text_numbers.py`, line 7 highlighted, error `examples/err04_text_numbers.expected_error`
- **Narration:** Here are all four.
  **On screen:** Table: Four file mistakes
- **Narration:** File not found: a wrong name, folder or working directory.
  **On screen:** Table: Four file mistakes (row 1 in focus)
- **Narration:** No error, but data gone: W instead of A.
  **On screen:** Table: Four file mistakes (row 2 in focus)
- **Narration:** Unicode decode error: the file used another encoding.
  **On screen:** Table: Four file mistakes (row 3 in focus)
- **Narration:** And a type error with a string: a C S V value is text.
  **On screen:** Table: Four file mistakes (row 4 in focus)
- **Narration:** Quick check. A program asks for menu dot text, instead of menu dot t x t. What do you see?
  **On screen:** Quick check: "A program asks for `menu.text` instead of `menu.txt`. What do you see?" (options shown)
- **Interaction:** "A program asks for `menu.text` instead of `menu.txt`. What do you see?" stays on screen with a 10-second timer.
- **Narration:** A. File not found. Python names the file it looked for.
  **On screen:** Quick check: "A program asks for `menu.text` instead of `menu.txt`. What do you see?" (answer revealed: `FileNotFoundError`)
- **Narration:** Last breather. You can now read file errors, and the silent mistake too.
  **On screen:** Breather card
    - Check the file name and the working directory.
    - Use `"a"` to add.
    - CSV values are text.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - Check the file name and the working directory.
    - Use `"a"` to add.
    - CSV values are text.
- **Breather:** 4 quiet seconds.

## Scene 13: Think beyond (15:32 to 16:24)

**Section:** Think beyond

**Direction:** Two open questions. No answers are given.

- **Narration:** First. The score file starts with two scores. Asha runs the score board three times. How many score rows, not counting the header, does it have now?
  **On screen:** Question card: "`scores.csv` starts with two scores. Asha runs the score board three times. How many score rows, not counting the header, does it have now?"
- **Interaction:** "`scores.csv` starts with two scores. Asha runs the score board three times. How many score rows, not counting the header, does it have now?" stays on screen with a 10-second timer.
- **Narration:** Then think: how could she stop the same score being saved twice? Try it on a copy of the file.
  **On screen:** Question card: "`scores.csv` starts with two scores. Asha runs the score board three times. How many score rows, not counting the header, does it have now?"
- **Narration:** Second. A program crashes halfway through a with block that writes a file. What does with still do, and what could be missing from the file?
  **On screen:** Question card: "A program crashes halfway through a `with` block that writes a file. What does `with` still do, and what could be missing?"
- **Interaction:** "A program crashes halfway through a `with` block that writes a file. What does `with` still do, and what could be missing?" stays on screen with a 10-second timer.
- **Narration:** Keep your answer. Chapter 22 builds on it.
  **On screen:** Question card: "A program crashes halfway through a `with` block that writes a file. What does `with` still do, and what could be missing?"

## Scene 14: Recap (16:24 to 16:56)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then the badge.

- **Narration:** Let's recap. A file keeps data after the program stops.
  **On screen:** Recap
    - A file keeps data after the program stops.
- **Narration:** Write text and read text work on a whole file.
  **On screen:** Recap
    - A file keeps data after the program stops.
    - `write_text()` and `read_text()` write and read a whole file.
- **Narration:** With open closes the file for you. W empties, A adds, R reads.
  **On screen:** Recap
    - A file keeps data after the program stops.
    - `write_text()` and `read_text()` write and read a whole file.
    - `with open(...)` closes the file for you. `"w"` empties, `"a"` adds, `"r"` reads.
- **Narration:** Always write encoding equals utf 8, and strip each line.
  **On screen:** Recap
    - A file keeps data after the program stops.
    - `write_text()` and `read_text()` write and read a whole file.
    - `with open(...)` closes the file for you. `"w"` empties, `"a"` adds, `"r"` reads.
    - Always write `encoding="utf-8"`. `strip()` removes each line's newline.
- **Narration:** The C S V module writes rows, and reads them as dictionaries of text.
  **On screen:** Recap
    - A file keeps data after the program stops.
    - `write_text()` and `read_text()` write and read a whole file.
    - `with open(...)` closes the file for you. `"w"` empties, `"a"` adds, `"r"` reads.
    - Always write `encoding="utf-8"`. `strip()` removes each line's newline.
    - `csv.writer` writes rows. `csv.DictReader` reads them as dictionaries of text.
- **Narration:** And test file code on a copy, then read the file.
  **On screen:** Recap
    - A file keeps data after the program stops.
    - `write_text()` and `read_text()` write and read a whole file.
    - `with open(...)` closes the file for you. `"w"` empties, `"a"` adds, `"r"` reads.
    - Always write `encoding="utf-8"`. `strip()` removes each line's newline.
    - `csv.writer` writes rows. `csv.DictReader` reads them as dictionaries of text.
    - Test file code on a copy, and read the file afterwards.
- **Narration:** Mission complete! You earned 100 XP and the Archivist badge.
  **On screen:** Archivist You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice (16:56 to 17:19)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including a visit counter that survives every run.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's log saver that loses data.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Work on copies of the data files, so a mistake never damages the originals.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 16: What's next (17:19 to 17:41)

**Section:** What's next

**Direction:** End card. Tease try and except as the fix for crashes on missing files. Hold quietly.

- **Narration:** One problem is left. If the score file is missing or damaged, the program still crashes with a long error report.
  **On screen:** Handling Errors: try, except and Clear Messages A missing file should give a clear message, not a crash.
- **Narration:** In Chapter 22, you will catch errors with try and except, and show a clear message instead.
  **On screen:** Handling Errors: try, except and Clear Messages A missing file should give a clear message, not a crash.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Handling Errors: try, except and Clear Messages Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 22.
  **On screen:** Handling Errors: try, except and Clear Messages Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
