# Video Script: Chapter 22: Handling Errors: try, except and Clear Messages

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:19 (estimate, not rendered yet).

## Scene 1: Introduction

**Section:** Introduction

**Direction:** Open on the Chapter 21 weak spot: one damaged row crashes the score board. Then the title and the AI tease, then the mission code with no output.

- **Narration:** At the Corner Cafe, someone typed the word three into Asha's score file, instead of the number 3.
  **On screen:** One bad row, and everything stops
- **Narration:** The score board prints one line. Then a wall of red text, and nothing else. The staff have no idea what to do.
  **On screen:** One bad row, and everything stops
- **Narration:** This is Code Quest, Chapter 22. Today, your programs learn to handle problems.
  **On screen:** Handling Errors: try, except and Clear Messages
- **Narration:** And an AI assistant will promise code that never crashes. It will sound sure. Your tests will decide.
  **On screen:** Handling Errors: try, except and Clear Messages Catch it. Explain it. Carry on.
- **Narration:** Here is today's mission: the same score board, now ready for bad data, with clear messages.
  **On screen:** Code `examples/ex07_score_board.py`, line 8, 9, 10, 11 highlighted, output hidden
- **Narration:** And a missing file gets a message too. Let's build it, piece by piece.
  **On screen:** Code `examples/ex07_score_board.py`, line 15, 16 highlighted, output hidden

## Scene 2: Learning goals

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Catch an error, and show a clear message instead.
  **On screen:** By the end, you will be able to:
    - Catch an error with `try` and `except`, and show a clear message.
- **Narration:** Use else and finally.
  **On screen:** By the end, you will be able to:
    - Catch an error with `try` and `except`, and show a clear message.
    - Use `else` and `finally`.
- **Narration:** Catch the specific error you expect.
  **On screen:** By the end, you will be able to:
    - Catch an error with `try` and `except`, and show a clear message.
    - Use `else` and `finally`.
    - Catch the specific error you expect.
- **Narration:** Raise your own error, and test it.
  **On screen:** By the end, you will be able to:
    - Catch an error with `try` and `except`, and show a clear message.
    - Use `else` and `finally`.
    - Catch the specific error you expect.
    - Raise your own error, and test it with `pytest.raises`.
- **Narration:** And ask an AI what could go wrong, then test each case.
  **On screen:** By the end, you will be able to:
    - Catch an error with `try` and `except`, and show a clear message.
    - Use `else` and `finally`.
    - Catch the specific error you expect.
    - Raise your own error, and test it with `pytest.raises`.
    - Ask an AI what could go wrong, then handle and test each case.

## Scene 3: Why this matters

**Section:** Why this matters

**Direction:** Define an exception, then real uses.

- **Narration:** An exception is an error that happens while a program runs, like a value error, or file not found.
  **On screen:** Why this matters
    - An **exception** is an error while the program runs.
- **Narration:** You have read exception reports since Chapter 9. Now your program catches them, and decides what to do.
  **On screen:** Why this matters
    - An **exception** is an error while the program runs.
    - You have read exception reports since Chapter 9. Now you catch them.
- **Narration:** Customers type words instead of numbers. Files get deleted. Good programs expect this, and carry on when they can.
  **On screen:** Why this matters
    - An **exception** is an error while the program runs.
    - You have read exception reports since Chapter 9. Now you catch them.
    - Good programs expect bad data, say what happened, and carry on.

## Scene 4: The idea: try, except, else, finally

**Section:** The idea

**Direction:** Teach the flow with the diagram and the table, then the analogy. Quiz on else. Breather.

- **Narration:** A try block runs code that might fail. If an exception happens inside it, Python stops that block, and jumps to a matching except block.
  **On screen:** Try first, catch if it fails
- **Narration:** The except line names the exception it catches. An exception of another type is not caught, and the program stops, as before.
  **On screen:** Try first, catch if it fails
- **Narration:** Try always runs first. It stops at the first exception.
  **On screen:** Table: Four parts, and when each one runs (row 1 in focus)
- **Narration:** Except value error runs only when a value error happened in try.
  **On screen:** Table: Four parts, and when each one runs (row 2 in focus)
- **Narration:** Else runs only when try finished with no exception at all.
  **On screen:** Table: Four parts, and when each one runs (row 3 in focus)
- **Narration:** And finally runs always, last, whatever happened.
  **On screen:** Table: Four parts, and when each one runs (row 4 in focus)
- **Narration:** Think of the safety net under a trapeze. The act goes on as planned, and the net catches the artist only after a fall.
  **On screen:** Like a safety net
    - The act goes on as planned. The net catches only after a fall.
- **Narration:** But a real net catches anyone. Except catches only the type of error it names.
  **On screen:** Like a safety net
    - The act goes on as planned. The net catches only after a fall.
    - Unlike a real net, `except` catches only the error type it names.
- **Narration:** Quick check. When does the else block run?
  **On screen:** Quick check: "When does the `else` block run?" (options shown)
- **Interaction:** "When does the `else` block run?" stays on screen with a 10-second timer.
- **Narration:** C. Only when try raised no exception. Finally is the one that always runs.
  **On screen:** Quick check: "When does the `else` block run?" (answer revealed: Only when `try` raised no exception)
- **Narration:** Breather. Four parts, and you know when each one runs.
  **On screen:** Breather card
    - `try` runs code that might fail.
    - `except` catches the error it names.
    - `else` if nothing failed, `finally` always.
- **Narration:** Next, Asha catches her first error.
  **On screen:** Breather card
    - `try` runs code that might fail.
    - `except` catches the error it names.
    - `else` if nothing failed, `finally` always.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Catch a bad number

**Section:** Build it step by step

**Direction:** Teach the jump before the ask. Ask which lines run for four. Reveal.

- **Narration:** Step 1. In Chapter 4, int of the word two stopped the program with a value error. Line 2 holds three answers, and the loop tries each one.
  **On screen:** Code `examples/ex01_try_except.py`, line 2 highlighted, output hidden
- **Narration:** Line 5 tries to turn the answer into a whole number. Line 6 prints it.
  **On screen:** Code `examples/ex01_try_except.py`, line 4, 5, 6 highlighted, output hidden
- **Narration:** If line 5 fails, Python skips the rest of the try block, and jumps to the except block on line 7.
  **On screen:** Code `examples/ex01_try_except.py`, line 5, 7 highlighted, output hidden
- **Interaction:** "For the answer `"four"`, which line prints: line 6, line 8, or both?" stays on screen with a 10-second timer.
- **Narration:** Only line 8. Line 5 failed, so line 6 never ran. And the loop went on with the next answer.
  **On screen:** Code `examples/ex01_try_except.py`, line 8 highlighted, output `examples/ex01_try_except.expected`
- **Narration:** Int ignores the spaces around 3, as you saw in Chapter 4. And exclamation r, from Chapter 20, shows the quotation marks.
  **On screen:** Code `examples/ex01_try_except.py`, line 5, 8 highlighted, output `examples/ex01_try_except.expected`

## Scene 6: Step 2: else and finally

**Section:** Build it step by step

**Direction:** Teach else and finally on a missing file. Ask what month.csv prints.

- **Narration:** Step 2. Line 7 reads a file. That can fail with file not found.
  **On screen:** Code `examples/ex02_else_finally.py`, line 7 highlighted, output hidden
- **Narration:** Lines 8 and 9 catch it, with a message.
  **On screen:** Code `examples/ex02_else_finally.py`, line 8, 9 highlighted, output hidden
- **Narration:** Else, on line 10, runs only when the file was read. Finally, on line 12, runs every time.
  **On screen:** Code `examples/ex02_else_finally.py`, line 10, 11, 12, 13 highlighted, output hidden
- **Narration:** Lines 16 and 17 call it twice: with week, and with month.
  **On screen:** Code `examples/ex02_else_finally.py`, line 16, 17 highlighted, output hidden
- **Interaction:** "What do the two lines for `month.csv` say?" stays on screen with a 10-second timer.
- **Narration:** No scores yet, then done. The except block ran, else was skipped, and finally ran anyway.
  **On screen:** Code `examples/ex02_else_finally.py`, line 9, 13 highlighted, output `examples/ex02_else_finally.expected`
- **Narration:** For week, else printed the file, and finally printed done.
  **On screen:** Code `examples/ex02_else_finally.py`, line 11, 13 highlighted, output `examples/ex02_else_finally.expected`
- **Narration:** Keep the try block small. Only the line that can fail belongs inside it.
  **On screen:** Code `examples/ex02_else_finally.py`, line 7 highlighted, output `examples/ex02_else_finally.expected`

## Scene 7: Step 3: Ask again until it is valid

**Section:** Build it step by step

**Direction:** Callback to Chapter 7. Try inside a while loop. Ask about the answer 7. Then a breather.

- **Narration:** Step 3. In Chapter 7, a while true loop asked until the answer was valid. Now try sits inside the loop.
  **On screen:** Code `examples/ex03_ask_again.py`, line 2, 3 highlighted, output hidden
- **Narration:** A word gives a value error, and line 7 asks for a whole number.
  **On screen:** Code `examples/ex03_ask_again.py`, line 4, 5, 6, 7 highlighted, output hidden
- **Narration:** If the number is from 0 to 4, break ends the loop. Otherwise line 11 explains the range.
  **On screen:** Code `examples/ex03_ask_again.py`, line 8, 9, 10, 11 highlighted, output hidden
- **Interaction:** "The user types `7`. Which message does the program show?" stays on screen with a 10-second timer.
- **Narration:** Please type a number from 0 to 4. Seven is a whole number, so no exception. But the if on line 9 catches the wrong value.
  **On screen:** Code `examples/ex03_ask_again.py`, line 9, 11 highlighted, output `examples/ex03_ask_again.expected`
- **Narration:** Try catches an answer that is not a number. If catches a number outside the range. And each message says what to type next.
  **On screen:** Code `examples/ex03_ask_again.py`, line 12 highlighted, output `examples/ex03_ask_again.expected`
- **Narration:** Breather. A word no longer crashes Asha's program.
  **On screen:** Breather card
    - `except` catches the error it names.
    - `else` holds the code that needs success.
    - Try inside a loop, and ask again.
- **Narration:** Next, Asha's own functions learn to refuse bad input.
  **On screen:** Breather card
    - `except` catches the error it names.
    - `else` holds the code that needs success.
    - Try inside a loop, and ask again.
- **Breather:** 4 quiet seconds.

## Scene 8: Steps 4 and 5: Raise, and catch what you expect

**Section:** Build it step by step

**Direction:** Teach raise and as error, then the bare except trap with a spot-it ask, then the specific version and a quiz.

- **Narration:** Step 4. A function can refuse bad input with raise. Line 4 creates a value error, with a message that names the price.
  **On screen:** Code `examples/ex04_raise.py`, line 3, 4 highlighted, output hidden
- **Narration:** Line 11 catches it. As error keeps the exception in a variable called error.
  **On screen:** Code `examples/ex04_raise.py`, line 9, 10, 11 highlighted, output hidden
- **Narration:** Line 12 prints that message.
  **On screen:** Code `examples/ex04_raise.py`, line 12 highlighted, output hidden
- **Interaction:** "Line 12 prints a message. What does it say?" stays on screen with a 10-second timer.
- **Narration:** Not saved: price cannot be negative: minus 1. The message from line 4 arrives at line 12.
  **On screen:** Code `examples/ex04_raise.py`, line 4, 12 highlighted, output `examples/ex04_raise.expected`
- **Narration:** A clear message names the problem and the value. Error, with nothing else, helps nobody.
  **On screen:** Code `examples/ex04_raise.py`, line 4, 12 highlighted, output `examples/ex04_raise.expected`
- **Narration:** Step 5. Line 7 is a bare except: no error type at all. It catches every exception, even the ones your own bugs cause.
  **On screen:** Code `examples/ex05_bare_except.py`, line 7 highlighted, output hidden
- **Narration:** Look closely at line 5.
  **On screen:** Code `examples/ex05_bare_except.py`, line 5 highlighted, output hidden
- **Interaction:** "What happens to the answer `"4"`?" stays on screen with a 10-second timer.
- **Narration:** It is refused too! Line 5 says anser, not answer. That name error was caught, and hidden.
  **On screen:** Code `examples/ex05_bare_except.py`, line 5, 7 highlighted, output `examples/ex05_bare_except.expected`
- **Narration:** Now line 7 catches value error only. The spelling mistake is no longer hidden.
  **On screen:** Code `examples/ex06_specific.py`, line 7 highlighted, error `examples/ex06_specific.expected_error`
- **Narration:** The report names line 5, and even suggests the right name. Catch the errors you expect from the data. Let your own bugs show.
  **On screen:** Code `examples/ex06_specific.py`, line 5 highlighted, error `examples/ex06_specific.expected_error`
- **Narration:** Quick check. Which except line can hide a spelling mistake in your own code?
  **On screen:** Quick check: "Which `except` line can hide a spelling mistake in your own code?" (options shown)
- **Interaction:** "Which `except` line can hide a spelling mistake in your own code?" stays on screen with a 10-second timer.
- **Narration:** B. The bare except. It catches everything, including your bugs. It even catches Control C, the keys you press to stop a program.
  **On screen:** Quick check: "Which `except` line can hide a spelling mistake in your own code?" (answer revealed: `except:`)

## Scene 9: Step 6: Test that an error is raised

**Section:** Build it step by step

**Direction:** Callback to Chapter 19. pytest.raises on cafe_tools, then a version that forgets to raise. Ask, reveal, breather.

- **Narration:** Step 6. Asha keeps with tax in her cafe tools module, with the new check on lines 4 and 5.
  **On screen:** Code `examples/cafe_tools.py`, line 4, 5 highlighted, output hidden
- **Narration:** In Chapter 19, tests checked return values. Line 11 checks an error. The test passes only if line 12 raises a value error.
  **On screen:** Code `examples/test_errors.py`, line 10, 11, 12 highlighted, output `examples/test_errors.expected`
- **Narration:** Both tests pass: two dots.
  **On screen:** Code `examples/test_errors.py`, line 10, 11, 12 highlighted, output `examples/test_errors.expected`
- **Narration:** Here is an older with tax. Lines 5 and 6 have no check for a negative price.
  **On screen:** Code `examples/test_errors_missing.py`, line 5, 6 highlighted, output hidden
- **Narration:** The test on lines 9 to 11 is the same as before.
  **On screen:** Code `examples/test_errors_missing.py`, line 9, 10, 11 highlighted, output hidden
- **Interaction:** "Will this test pass?" stays on screen with a 10-second timer.
- **Narration:** No. The function returned a value instead of refusing. Pytest reports: did not raise value error.
  **On screen:** Code `examples/test_errors_missing.py`, line 10 highlighted, output `examples/test_errors_missing.expected`
- **Narration:** Breather. You can catch, raise, and test errors.
  **On screen:** Breather card
    - `raise` refuses bad input with a message.
    - Catch the error you expect, not every error.
    - `pytest.raises` checks that the error happens.
- **Narration:** Now, back to the mission.
  **On screen:** Breather card
    - `raise` refuses bad input with a message.
    - Catch the error you expect, not every error.
    - `pytest.raises` checks that the error happens.
- **Breather:** 4 quiet seconds.

## Scene 10: See the outcome: the score board

**Section:** See the outcome

**Direction:** Show the damaged file, walk the two try blocks, ask how many scores load, reveal, hand over to the AI.

- **Narration:** Back to the mission. Here is the score file, with Omar's damaged row.
  **On screen:** The score file
- **Narration:** Line 4 starts a counter. The outer try, on lines 5 and 6, opens the file.
  **On screen:** Code `examples/ex07_score_board.py`, line 5, 6 highlighted, output hidden
- **Narration:** Inside the loop, a small try on lines 8 and 9 protects one row at a time.
  **On screen:** Code `examples/ex07_score_board.py`, line 7, 8, 9 highlighted, output hidden
- **Narration:** A bad score prints a message that names the row and the value.
  **On screen:** Code `examples/ex07_score_board.py`, line 10, 11 highlighted, output hidden
- **Narration:** A good score is printed and counted, in else.
  **On screen:** Code `examples/ex07_score_board.py`, line 12, 13, 14 highlighted, output hidden
- **Narration:** Lines 15 and 16 handle a missing file. Line 17 prints the count.
  **On screen:** Code `examples/ex07_score_board.py`, line 15, 16, 17 highlighted, output hidden
- **Interaction:** "How many scores does line 17 report?" stays on screen with a 10-second timer.
- **Narration:** 2. Omar's row is skipped with a message, and Lina still loads, because the try protects one row at a time.
  **On screen:** Code `examples/ex07_score_board.py`, line 17 highlighted, output `examples/ex07_score_board.expected`
- **Narration:** Now Asha wants this as a function, load scores, for the quiz app. She builds it with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex07_score_board.py`, output `examples/ex07_score_board.expected`

## Scene 11: Work with AI: a loader that handles every problem

**Section:** Work with AI

**Direction:** Safety first. Six stages on load_scores. Stage 3 plants the bare except around the loop; tests catch it; debug a short row; improve suggests except Exception.

- **Narration:** This chapter's AI skill: ask what could go wrong in your code.
  **On screen:** This chapter's AI skill: what could go wrong?
    - Ask the AI to list what could go wrong.
- **Narration:** Then make one test case for each problem, and run it.
  **On screen:** This chapter's AI skill: what could go wrong?
    - Ask the AI to list what could go wrong.
    - Make one test case for each problem, and run it.
- **Narration:** And never paste private data. A real file of staff names is private, so paste a made-up sample.
  **On screen:** This chapter's AI skill: what could go wrong?
    - Ask the AI to list what could go wrong.
    - Make one test case for each problem, and run it.
    - A real score file is private: paste a made-up sample.
- **Narration:** Stage 1: plan. Asha asks what could go wrong, and what the program should do each time. No code yet.
  **On screen:** AI chat, stage 1: Plan: what could go wrong?
    - You: My function load_scores reads scores.csv and turns each score into an int. Do not write code yet. What could go wrong, and what should the program do each time?
- **Narration:** The AI lists three problems: a missing file, a score that is not a number, and a file with only the header.
  **On screen:** AI chat, stage 1: Plan: what could go wrong?
    - You: My function load_scores reads scores.csv and turns each score into an int. Do not write code yet. What could go wrong, and what should the program do each time?
    - AI (example answer): 1. The file is missing: FileNotFoundError. Give a message, return no scores. 2. A score is not a number: ValueError. Skip that row with a message. 3. The file has only the header: no error, return no scores.
- **Narration:** Stage 2: write. Asha writes her own load scores first, and asks which lines handle each problem.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote this myself. Do not rewrite it. Which lines handle problems 1 and 2? [code `examples/ai_mine.py`]
- **Narration:** The AI names lines 12 to 15. That matches what she meant.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote this myself. Do not rewrite it. Which lines handle problems 1 and 2? [code `examples/ai_mine.py`]
    - AI (example answer): Problem 1: lines 14 and 15 catch FileNotFoundError. Problem 2: lines 12 and 13 catch ValueError for one row, so the loop goes on.
- **Narration:** Stage 3: generate. To compare, Asha asks the AI for the same function, from a short request.
  **On screen:** AI chat, stage 3: Generate: a loader from a request
    - You: Write load_scores(path). It returns a list of (name, score). It must never crash, and it must skip a damaged row.
- **Narration:** The AI is sure: it handles every problem, and never crashes.
  **On screen:** AI chat, stage 3: Generate: a loader from a request
    - You: Write load_scores(path). It returns a list of (name, score). It must never crash, and it must skip a damaged row.
    - AI (example answer): Here it is. It handles every problem, and it never crashes. [code `examples/ai_load_flawed.py`]
- **Narration:** Look where the try starts, on line 7, and where it ends. Lines 11 and 12 catch everything, and do nothing.
  **On screen:** Code `examples/ai_load_flawed.py`, line 7, 11, 12 highlighted, output hidden
- **Narration:** Line 17 loads the damaged file: Asha, Omar with three, and Lina.
  **On screen:** Code `examples/ai_load_flawed.py`, line 17 highlighted, output hidden
- **Interaction:** "The AI says it handles every problem. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Only Asha loads. The try block holds the whole loop, so Omar's row stopped it, and Lina was lost, with no message.
  **On screen:** Code `examples/ai_load_flawed.py`, line 7, 9 highlighted, output `examples/ai_load_flawed.expected`
- **Narration:** A better request names the exceptions to catch, and asks for a small try block.
  **On screen:** Code `examples/ai_load_flawed.py`, output `examples/ai_load_flawed.expected`
- **Narration:** Stage 4: test. Asha asks for test cases, each with the file and the number of scores it should return.
  **On screen:** AI chat, stage 4: Test: one case for each problem
    - You: Give me test cases for load_scores. For each one, write the file contents and how many scores it should return.
- **Narration:** The AI lists three. They match the three problems from the plan.
  **On screen:** AI chat, stage 4: Test: one case for each problem
    - You: Give me test cases for load_scores. For each one, write the file contents and how many scores it should return.
    - AI (example answer): 1. Normal: Asha and Lina. Expect 2. 2. Damaged row: Asha, Omar with three, Lina. Expect 2. 3. Header only: expect 0.
- **Narration:** She runs all three cases on the AI's loader. The damaged row case fails: it found 1 score, not 2.
  **On screen:** Code `examples/ai_tests_flawed.py`, line 4, 5, 6 highlighted, output `examples/ai_tests_flawed.expected`
- **Narration:** Asha shows the AI the failing case, and asks for the cause, then a fix.
  **On screen:** AI chat, stage 4: Test: report the failure, ask for a fix
    - You: The damaged row case fails: it found 1 score, not 2, with no message. Explain why, then fix it.
- **Narration:** The AI explains: the whole loop was inside try, and the bare except hid the error. The fix puts a small try around one row, the same idea as Asha's own version.
  **On screen:** AI chat, stage 4: Test: report the failure, ask for a fix
    - You: The damaged row case fails: it found 1 score, not 2, with no message. Explain why, then fix it.
    - AI (example answer): The try block holds the whole loop, so the damaged row stopped it. The bare except with pass hid the error. Fix: a small try around one row, catching ValueError only, and a message for a missing file.
- **Narration:** She runs all three cases again, on the fixed loader. All three pass, and Omar's row gets a message.
  **On screen:** Code `examples/ai_tests_fixed.py`, line 2 highlighted, output `examples/ai_tests_fixed.expected`
- **Narration:** Stage 5: debug. In a new test file, one row says only Ben, with no comma and no score. Her own version has the same gap.
  **On screen:** Code `examples/ai_short_crash.py`, line 4 highlighted, error `examples/ai_short_crash.expected_error`
- **Narration:** Type error! The report points at line 11 of the loader: int of row score.
  **On screen:** Code `examples/ai_short_crash.py`, line 4 highlighted, error `examples/ai_short_crash.expected_error`
- **Narration:** Asha pastes the error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: A row in my file says only Ben. Now load_scores crashes on line 11 with: TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'. Explain the cause first. Then show the smallest fix.
- **Narration:** Ben's row has no score, so the value is None, and int of None raises a type error. The fix catches both errors as a tuple: the two names inside round brackets, like the tuples from Chapter 13.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: A row in my file says only Ben. Now load_scores crashes on line 11 with: TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'. Explain the cause first. Then show the smallest fix.
    - AI (example answer): Ben's row has no score, so row["score"] is None, and int(None) raises TypeError. Fix: catch both on line 12: except (ValueError, TypeError).
- **Narration:** She adds the short row as case 4, and runs every case again. All four pass.
  **On screen:** Code `examples/ai_tests_final.py`, line 7 highlighted, output `examples/ai_tests_final.expected`
- **Narration:** Stage 6: improve. Asha asks for one improvement.
  **On screen:** AI chat, stage 6: Improve: one suggestion, then test it
    - You: All four cases pass. Suggest one improvement, with one reason.
- **Narration:** The AI suggests: except Exception, so no future error can ever crash it.
  **On screen:** AI chat, stage 6: Improve: one suggestion, then test it
    - You: All four cases pass. Suggest one improvement, with one reason.
    - AI (example answer): Use except Exception instead of except (ValueError, TypeError), so no future error can ever crash it.
- **Narration:** Exception, with a capital E, is the parent of almost every error type. So except Exception catches nearly every error, your bugs included.
  **On screen:** AI chat, stage 6: Improve: one suggestion, then test it
    - You: All four cases pass. Suggest one improvement, with one reason.
    - AI (example answer): Use except Exception instead of except (ValueError, TypeError), so no future error can ever crash it.
- **Narration:** Asha tests the idea. She adds a spelling mistake on purpose: line 10 says scor, not score. Line 11 catches Exception.
  **On screen:** Code `examples/ai_typo_broad.py`, line 10, 11 highlighted, output hidden
- **Narration:** Line 16 loads the normal file, with two good rows.
  **On screen:** Code `examples/ai_typo_broad.py`, line 16 highlighted, output hidden
- **Interaction:** "Will Asha see her spelling mistake?" stays on screen with a 10-second timer.
- **Narration:** No. Every row is skipped with a wrong message, and the list is empty. The bug is hidden.
  **On screen:** Code `examples/ai_typo_broad.py`, line 10, 11 highlighted, output `examples/ai_typo_broad.expected`
- **Narration:** With her specific except, the key error stops the program, and points at line 10. She finds the spelling mistake at once. So she keeps the specific except.
  **On screen:** Code `examples/ai_typo_specific.py`, line 10, 11 highlighted, error `examples/ai_typo_specific.expected_error`
- **Narration:** Quick check. A score loader reads a file. Which except should catch a damaged score?
  **On screen:** Quick check: "A score loader reads a file. Which `except` should catch a damaged score?" (options shown)
- **Interaction:** "A score loader reads a file. Which `except` should catch a damaged score?" stays on screen with a 10-second timer.
- **Narration:** D. Value error. That is the error a damaged score raises. Let every other error show.
  **On screen:** Quick check: "A score loader reads a file. Which `except` should catch a damaged score?" (answer revealed: `except ValueError:`)
- **Narration:** Breather. The AI made two confident mistakes, and Asha's tests caught both.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - A small `try` keeps one bad row from stopping the rest.
    - Test that a change does not hide your bugs.
- **Narration:** Next, four mistakes beginners make with try and except.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - A small `try` keeps one bad row from stopping the rest.
    - Test that a change does not hide your bugs.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes

**Section:** Common mistakes

**Direction:** Mistakes 1 and 3 are spot-it asks. Mistakes 2 and 4 are explained.

- **Narration:** Mistake 1. You try. Line 4 turns the word four into a whole number. Line 5 catches an error.
  **On screen:** Code `examples/err01_wrong_type.py`, line 5 highlighted, output hidden
- **Interaction:** "Will line 5 catch the error from line 4?" stays on screen with a 10-second timer.
- **Narration:** No. Int of four raises a value error, not a type error. So the program still stops.
  **On screen:** Code `examples/err01_wrong_type.py`, line 5 highlighted, error `examples/err01_wrong_type.expected_error`
- **Narration:** The fix: catch the type the report names. Run the code once without try, to see it.
  **On screen:** Code `examples/err01_wrong_type.py`, line 5 highlighted, error `examples/err01_wrong_type.expected_error`
- **Narration:** Mistake 2. Line 4 failed, so score was never created. Line 7 still uses it: name error.
  **On screen:** Code `examples/err02_unset.py`, line 7 highlighted, error `examples/err02_unset.expected_error`
- **Narration:** The fix: put the code that needs score in else.
  **On screen:** Code `examples/err02_unset.py`, line 7 highlighted, error `examples/err02_unset.expected_error`
- **Narration:** Mistake 3. Remember the four parts. Look at what follows the try block.
  **On screen:** Code `examples/err03_no_except.py`, line 2 highlighted, output hidden
- **Interaction:** "What is missing after line 3?" stays on screen with a 10-second timer.
- **Narration:** An except or a finally block. Every try needs one, straight after it. Python cannot even read the file.
  **On screen:** Code `examples/err03_no_except.py`, line 2 highlighted, error `examples/err03_no_except.expected_error`
- **Narration:** Mistake 4. Raise needs an exception, not text. Python stops with a type error.
  **On screen:** Code `examples/err04_raise_text.py`, line 4 highlighted, error `examples/err04_raise_text.expected_error`
- **Narration:** The fix: put the message inside a value error.
  **On screen:** Code `examples/err04_raise_text.py`, line 4 highlighted, error `examples/err04_raise_text.expected_error`
- **Narration:** Last breather. Errors are now part of your plan, not a surprise.
  **On screen:** Breather card
    - Catch the type the report names.
    - Code that needs the result goes in `else`.
    - `raise` needs an exception, with a message.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - Catch the type the report names.
    - Code that needs the result goes in `else`.
    - `raise` needs an exception, with a message.
- **Breather:** 4 quiet seconds.

## Scene 13: Think beyond

**Section:** Think beyond

**Direction:** Two open questions. No answers are given.

- **Narration:** First. In the ask again program, a player types 3.5 as the score. Which message do they see, and how would you make it clearer?
  **On screen:** Question card: "In `ex03`, a player types `3.5` as the score. Which message do they see, and how would you make it clearer?"
- **Interaction:** "In `ex03`, a player types `3.5` as the score. Which message do they see, and how would you make it clearer?" stays on screen with a 10-second timer.
- **Narration:** Try it after the video, and write your new message.
  **On screen:** Question card: "In `ex03`, a player types `3.5` as the score. Which message do they see, and how would you make it clearer?"
- **Narration:** Second. When is it better to stop the whole program, instead of skipping a damaged row? Think about a file of bank payments.
  **On screen:** Question card: "When is it better to stop the whole program than to skip a damaged row?"
- **Interaction:** "When is it better to stop the whole program than to skip a damaged row?" stays on screen with a 10-second timer.
- **Narration:** Keep your answer. It is a design choice, not a rule.
  **On screen:** Question card: "When is it better to stop the whole program than to skip a damaged row?"

## Scene 14: Recap

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then the badge.

- **Narration:** Let's recap. Try and except catch an exception, and show a clear message.
  **On screen:** Recap
    - `try` and `except` catch an exception and show a clear message.
- **Narration:** Else runs when nothing failed. Finally runs always.
  **On screen:** Recap
    - `try` and `except` catch an exception and show a clear message.
    - `else` runs when nothing failed. `finally` runs always.
- **Narration:** Catch the exception you expect. A bare except hides your bugs.
  **On screen:** Recap
    - `try` and `except` catch an exception and show a clear message.
    - `else` runs when nothing failed. `finally` runs always.
    - Catch the exception you expect. A bare `except:` hides your bugs.
- **Narration:** Keep each try block small.
  **On screen:** Recap
    - `try` and `except` catch an exception and show a clear message.
    - `else` runs when nothing failed. `finally` runs always.
    - Catch the exception you expect. A bare `except:` hides your bugs.
    - Keep each `try` block small.
- **Narration:** Raise refuses bad input, with a message.
  **On screen:** Recap
    - `try` and `except` catch an exception and show a clear message.
    - `else` runs when nothing failed. `finally` runs always.
    - Catch the exception you expect. A bare `except:` hides your bugs.
    - Keep each `try` block small.
    - `raise ValueError("message")` refuses bad input.
- **Narration:** And pytest raises tests that the error happens.
  **On screen:** Recap
    - `try` and `except` catch an exception and show a clear message.
    - `else` runs when nothing failed. `finally` runs always.
    - Catch the exception you expect. A bare `except:` hides your bugs.
    - Keep each `try` block small.
    - `raise ValueError("message")` refuses bad input.
    - `pytest.raises` tests that the error is raised.
- **Narration:** Mission complete! You earned 100 XP and the Safety Net badge.
  **On screen:** Safety Net You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including an order that asks again until it is valid.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's menu loader that loses items.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 16: What's next

**Section:** What's next

**Direction:** End card. Tease JSON as the next step for structured data. Hold quietly.

- **Narration:** Asha's scores are safe now. But a C S V row holds only flat values. Her quiz needs questions, answers and settings, inside each other.
  **On screen:** JSON and APIs: Talking to Other Programs Save structured data, and read data from other programs.
- **Narration:** In Chapter 23, you will save structured data as JSON, and read data that other programs send, through web A P Is.
  **On screen:** JSON and APIs: Talking to Other Programs Save structured data, and read data from other programs.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** JSON and APIs: Talking to Other Programs Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 23.
  **On screen:** JSON and APIs: Talking to Other Programs Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
