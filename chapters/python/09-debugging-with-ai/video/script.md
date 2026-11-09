# Video Script: Chapter 9: Debugging with AI: Reading Errors and Tracebacks

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:22.

## Scene 1: Introduction (0:00 to 0:38)

**Section:** Introduction

**Direction:** Open on the silent bug: a wrong total with no error. Then the title and the AI tease, then the working report as the mission.

- **Narration:** One evening, Asha runs her end-of-day report. It prints a total that is much too small.
  **On screen:** A report that is wrong
    - Asha's end-of-day report adds up the cafe's sales.
    - It prints a total that is much too small.
- **Narration:** But there is no error, and no crash. Nothing looks broken. How do you find a bug that hides?
  **On screen:** A report that is wrong
    - Asha's end-of-day report adds up the cafe's sales.
    - It prints a total that is much too small.
    - No error. No crash. Nothing looks broken.
- **Narration:** This is Code Quest, Chapter 9. Today you become a bug hunter.
  **On screen:** Debugging with AI: Reading Errors and Tracebacks
- **Narration:** And an AI assistant will promise to stop a crash. Its fix will crash on the same division.
  **On screen:** Debugging with AI: Reading Errors and Tracebacks Find the cause. Then fix it.
- **Narration:** So here is today's mission. Asha's end-of-day report, with three bugs found and fixed.
  **On screen:** Code `examples/ex07_day_report.py`, line 3, 6 highlighted, output hidden
- **Narration:** When it works, its total matches the money she took, and she can explain why. Let's start hunting.
  **On screen:** Code `examples/ex07_day_report.py`, output hidden

## Scene 2: Learning goals (0:38 to 0:55)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Tell the three kinds of bugs apart.
  **On screen:** By the end, you will be able to:
    - Tell a syntax error, a runtime error and a logic error apart.
- **Narration:** Read a traceback, from the bottom up.
  **On screen:** By the end, you will be able to:
    - Tell a syntax error, a runtime error and a logic error apart.
    - Read a traceback from the bottom up.
- **Narration:** Find a hidden bug by printing values inside a loop.
  **On screen:** By the end, you will be able to:
    - Tell a syntax error, a runtime error and a logic error apart.
    - Read a traceback from the bottom up.
    - Find a logic error by printing values inside a loop.
- **Narration:** Write a debugging prompt that gives an AI everything it needs.
  **On screen:** By the end, you will be able to:
    - Tell a syntax error, a runtime error and a logic error apart.
    - Read a traceback from the bottom up.
    - Find a logic error by printing values inside a loop.
    - Write a debugging prompt with the code, the exact error, the expected and the actual result.
- **Narration:** And test a fix with several cases, including the one that failed.
  **On screen:** By the end, you will be able to:
    - Tell a syntax error, a runtime error and a logic error apart.
    - Read a traceback from the bottom up.
    - Find a logic error by printing values inside a loop.
    - Write a debugging prompt with the code, the exact error, the expected and the actual result.
    - Test a fix with several cases, including the one that failed.

## Scene 3: Why this matters (0:55 to 1:12)

**Section:** Why this matters

**Direction:** Define a bug, then the speed point, then the vague AI question.

- **Narration:** A bug is a mistake that makes a program stop, or give a wrong result. Every programmer writes bugs, every day.
  **On screen:** Why this matters
    - A **bug** is a mistake that makes a program stop or give a wrong result.
    - Every programmer writes bugs. Good programmers find them fast.
- **Narration:** And here is the AI part. A vague question, like my code is wrong, fix it, often gets a confident fix for the wrong problem.
  **On screen:** Why this matters
    - A **bug** is a mistake that makes a program stop or give a wrong result.
    - Every programmer writes bugs. Good programmers find them fast.
    - A vague question to an AI often gets a confident fix for the wrong problem.

## Scene 4: The idea: three kinds of bugs (1:12 to 2:11)

**Section:** The idea

**Direction:** Teach the three kinds with the table. Then a quiz and a breather.

- **Narration:** Bugs come in three kinds, and each one shows itself in a different way.
  **On screen:** Table: Three kinds of bugs
- **Narration:** A syntax error means Python cannot read the file. So it runs nothing at all, not even the first print.
  **On screen:** Table: Three kinds of bugs (row 1 in focus)
- **Narration:** A runtime error happens while the program runs. Some lines print, then Python stops and prints a report.
  **On screen:** Table: Three kinds of bugs (row 2 in focus)
- **Narration:** A logic error is the sneakiest. The program finishes, with no message. But the result is wrong.
  **On screen:** Table: Three kinds of bugs (row 3 in focus)
- **Narration:** Quick check. A program prints two lines, then stops with an error report. Which kind of bug is it?
  **On screen:** Quick check: "A program prints two lines, then stops with an error report. Which kind of bug is it?" (options shown)
- **Interaction:** "A program prints two lines, then stops with an error report. Which kind of bug is it?" stays on screen with a 10-second timer.
- **Narration:** A. A runtime error. Some lines ran first, so Python could read the file.
  **On screen:** Quick check: "A program prints two lines, then stops with an error report. Which kind of bug is it?" (answer revealed: A runtime error)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - Syntax error: nothing runs.
    - Runtime error: it stops partway.
    - Logic error: a wrong result, no message.
- **Narration:** Next, Asha meets each kind of bug in her report.
  **On screen:** Breather card
    - Syntax error: nothing runs.
    - Runtime error: it stops partway.
    - Logic error: a wrong result, no message.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: A syntax error stops everything (2:11 to 3:00)

**Section:** Build it step by step

**Direction:** Show the file with the missing bracket, ask whether line 2 prints, then read the report.

- **Narration:** Step 1. Asha's report starts with three lines. Line 2 prints the heading. It is correct.
  **On screen:** Code `examples/ex01_syntax.py`, line 2 highlighted, output hidden
- **Narration:** Line 4 prints the tea price. Look at its end: the closing bracket is missing.
  **On screen:** Code `examples/ex01_syntax.py`, line 4 highlighted, output hidden
- **Interaction:** "Line 2 is correct. Does it print before Python reports the error?" stays on screen with a 10-second timer.
- **Narration:** No. Nothing prints at all. Python reads the whole file before it runs any line, and it could not read line 4.
  **On screen:** Code `examples/ex01_syntax.py`, line 2 highlighted, error `examples/ex01_syntax.expected_error`
- **Narration:** The report names the file and line 4. The marker points at the opening bracket, the one that was never closed.
  **On screen:** Code `examples/ex01_syntax.py`, line 4 highlighted, error `examples/ex01_syntax.expected_error`
- **Narration:** The fix goes at the end of the line: a closing bracket.
  **On screen:** Code `examples/ex01_syntax.py`, line 4 highlighted, error `examples/ex01_syntax.expected_error`
- **Narration:** These messages come from Python 3.12 and newer. Older versions word some of them differently.
  **On screen:** Code `examples/ex01_syntax.py`, line 4 highlighted, error `examples/ex01_syntax.expected_error`

## Scene 6: Step 2: Read a traceback from the bottom up (3:00 to 4:26)

**Section:** Build it step by step

**Direction:** Predict which lines print before the crash. Then read the traceback from the bottom up, one line at a time. Then find the cause on an earlier line and show the fix.

- **Narration:** Step 2. Line 3 asks how many cups of tea were sold. Remember Chapter 4: input always gives back text.
  **On screen:** Code `examples/ex02_runtime.py`, line 3 highlighted, output hidden
- **Narration:** Line 4 prints the answer. Line 5 multiplies the cups by the tea price, 3.5.
  **On screen:** Code `examples/ex02_runtime.py`, line 4, 5 highlighted, output hidden
- **Interaction:** "The user types 12. Which lines print before Python stops?" stays on screen with a 10-second timer.
- **Narration:** Lines 2, 3 and 4 run, so their output appears. Then Python stops at line 5.
  **On screen:** Code `examples/ex02_runtime.py`, line 2, 3, 4 highlighted, error `examples/ex02_runtime.expected_error`
- **Narration:** This report is called a traceback. Read it from the bottom up. The last line names the kind of error, a Type Error. A sequence is a value made of parts in order, like a string.
  **On screen:** Code `examples/ex02_runtime.py`, line 5 highlighted, error `examples/ex02_runtime.expected_error`
- **Narration:** The two lines above show the code, and the markers point at the part that failed: cups times 3.5.
  **On screen:** Code `examples/ex02_runtime.py`, line 5 highlighted, error `examples/ex02_runtime.expected_error`
- **Narration:** Above that: the file, and line 5.
  **On screen:** Code `examples/ex02_runtime.py`, line 5 highlighted, error `examples/ex02_runtime.expected_error`
- **Narration:** And the first line says: most recent call last. It means the newest step is at the bottom. In programs this size, there is only one step. In Chapter 16, when you write functions, tracebacks grow longer.
  **On screen:** Code `examples/ex02_runtime.py`, line 5 highlighted, error `examples/ex02_runtime.expected_error`
- **Narration:** Here is the key idea. The line Python names is where it noticed the problem. The cause can be earlier.
  **On screen:** Code `examples/ex03_runtime_fixed.py`, line 3 highlighted, output `examples/ex03_runtime_fixed.expected`
- **Narration:** Line 3 stored the answer as text. So the fix is on line 3: int, around the input.
  **On screen:** Code `examples/ex03_runtime_fixed.py`, line 3 highlighted, output `examples/ex03_runtime_fixed.expected`
- **Narration:** Now 12 cups cost 42.00.
  **On screen:** Code `examples/ex03_runtime_fixed.py`, line 5 highlighted, output `examples/ex03_runtime_fixed.expected`

## Scene 7: Step 3: Spot a logic error (4:26 to 5:10)

**Section:** Build it step by step

**Direction:** Teach: work out the expected result first. Ask for the expected total, then reveal the wrong one.

- **Narration:** Step 3. This loop adds up three sales. Line 2 starts the total at 0.
  **On screen:** Code `examples/ex04_logic.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 makes three passes. Line 4 asks for the price of each sale. Line 5 adds to the total.
  **On screen:** Code `examples/ex04_logic.py`, line 3, 4, 5 highlighted, output hidden
- **Narration:** Before you run any program, work out the expected result by hand. Otherwise, a wrong answer looks fine.
  **On screen:** Code `examples/ex04_logic.py`, output hidden
- **Interaction:** "The user types 4.50, 6.00 and 3.50. What total should the program print?" stays on screen with a 10-second timer.
- **Narration:** It should print 14.00. But it prints 6.00!
  **On screen:** Code `examples/ex04_logic.py`, output `examples/ex04_logic.expected`
- **Narration:** No error, no crash. Only a wrong number. That is a logic error, and only your expected result caught it.
  **On screen:** Code `examples/ex04_logic.py`, output `examples/ex04_logic.expected`

## Scene 8: Step 4: Print debugging (5:10 to 6:09)

**Section:** Build it step by step

**Direction:** Teach print debugging with one debug line, ask what it shows after sale 1, reveal, find the cause, fix.

- **Narration:** Step 4. To find a hidden bug, print the values of your variables while the program runs. This is called print debugging.
  **On screen:** Code `examples/ex05_print_debug.py`, line 6 highlighted, output hidden
- **Narration:** Asha adds line 6 inside the loop. It shows sale, price and total on every pass. It starts with the word DEBUG, so she can find it and remove it later.
  **On screen:** Code `examples/ex05_print_debug.py`, line 6 highlighted, output hidden
- **Narration:** Line 5 runs before the debug line, so you see the total after it changes.
  **On screen:** Code `examples/ex05_print_debug.py`, line 5, 6 highlighted, output hidden
- **Interaction:** "On the first pass, sale is 1 and price is 4.5. What total does the DEBUG line show?" stays on screen with a 10-second timer.
- **Narration:** Total is 1. It should be 4.5.
  **On screen:** Code `examples/ex05_print_debug.py`, line 6 highlighted, output `examples/ex05_print_debug.expected`
- **Narration:** Then 3, then 6. The total grows by the sale number, 1, 2 and 3, not by the price.
  **On screen:** Code `examples/ex05_print_debug.py`, line 6 highlighted, output `examples/ex05_print_debug.expected`
- **Narration:** So line 5 adds sale, where it should add price.
  **On screen:** Code `examples/ex05_print_debug.py`, line 5 highlighted, output `examples/ex05_print_debug.expected`
- **Narration:** Asha changes line 5 to add price, and removes the debug line. The total is 14.00, exactly as expected.
  **On screen:** Code `examples/ex06_logic_fixed.py`, line 5 highlighted, output `examples/ex06_logic_fixed.expected`

## Scene 9: Step 5: A debugging prompt that works (6:09 to 7:06)

**Section:** Build it step by step

**Direction:** Teach the four parts of the prompt, row by row, then the cause-first rule. Quiz, then a breather.

- **Narration:** Step 5. An AI cannot see your screen. So give it four things. The code, and the exact error. If there is none, say: no error message.
  **On screen:** Table: Step 5: Four parts of a debugging prompt (row 2 in focus)
- **Narration:** Then the expected result, worked out by hand, and the actual result. The difference points at the bug.
  **On screen:** Table: Step 5: Four parts of a debugging prompt (row 4 in focus)
- **Narration:** Then ask for the cause before the fix. A cause you understand teaches you something.
  **On screen:** Table: Step 5: Four parts of a debugging prompt
- **Narration:** Quick check. Your program prints a wrong total, and no error. Which parts of the prompt matter most?
  **On screen:** Quick check: "Your program prints a wrong total and no error. Which parts of the prompt matter most?" (options shown)
- **Interaction:** "Your program prints a wrong total and no error. Which parts of the prompt matter most?" stays on screen with a 10-second timer.
- **Narration:** B. The expected result and the actual result. With no error message, their difference is the only clue.
  **On screen:** Quick check: "Your program prints a wrong total and no error. Which parts of the prompt matter most?" (answer revealed: The expected result and the actual result)
- **Narration:** Breather. You have found and fixed three kinds of bugs. Now, the whole report.
  **On screen:** Breather card
    - Read a traceback from the bottom up.
    - The cause can be on an earlier line.
    - Print values to find a hidden bug.
- **Breather:** 4 quiet seconds.

## Scene 10: See the outcome: the day report (7:06 to 8:11)

**Section:** See the outcome

**Direction:** Return to the mission. Connect each line to a fix from the steps, ask for the average line, reveal. Hand over to the zero-sales test.

- **Narration:** Back to the mission. Line 2 prints the heading, and every bracket is closed. Line 3 converts the number of sales with int, the fix from step 2.
  **On screen:** Code `examples/ex07_day_report.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 starts the total at 0. Lines 5 to 7 add up each price: the fix from step 4. Range goes up to sales plus 1, so it asks once for each sale.
  **On screen:** Code `examples/ex07_day_report.py`, line 4, 5, 6, 7 highlighted, output hidden
- **Narration:** Line 8 divides the total by the number of sales, and lines 9 to 11 print the report, with two decimal places.
  **On screen:** Code `examples/ex07_day_report.py`, line 8, 9, 10, 11 highlighted, output hidden
- **Interaction:** "The total is 14.00 and there are 3 sales. What does line 11 print?" stays on screen with a 10-second timer.
- **Narration:** Average, 4.67. 14 divided by 3 is 4.666 and more, and two decimal places round it to 4.67.
  **On screen:** Code `examples/ex07_day_report.py`, line 8, 11 highlighted, output `examples/ex07_day_report.expected`
- **Narration:** And the total is 14.00, the money Asha took. Mission complete! But Asha has one more test in mind. What happens on a day with no sales at all? She will find out, with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex07_day_report.py`, line 10 highlighted, output `examples/ex07_day_report.expected`

## Scene 11: Work with AI: six stages, one day with no sales (8:11 to 13:15)

**Section:** Work with AI

**Direction:** Teach the structured prompt skill. One conversation per stage, all about 0 sales. Stage 3 plants the >= mistake, stage 4 catches it with a case list, stage 5 fixes it and re-runs every case, stage 6 catches an ignored instruction.

- **Narration:** This chapter's AI skill is the debugging prompt: the code, the exact error, the expected result, and the actual result.
  **On screen:** This chapter's AI skill: the debugging prompt
    - Give the code, the exact error, the expected result and the actual result.
- **Narration:** Ask for the cause first. Then test every fix yourself. And the safety habits from Chapter 1 still apply.
  **On screen:** This chapter's AI skill: the debugging prompt
    - Give the code, the exact error, the expected result and the actual result.
    - Ask for the cause before the fix.
    - Test every fix yourself. Never paste private data.
- **Narration:** Stage 1: plan. Asha types 0 sales, and the report crashes. Before any fix, she asks for a plan to find the cause. No code yet.
  **On screen:** AI chat, stage 1: Plan: a bug hunt, not a fix
    - You: I am a beginner. My day report crashes when I type 0 sales. Do not fix anything yet and do not write code. Give me a short plan to find the cause.
- **Narration:** The AI gives five steps. Copy the traceback, and read its last line. Find the line and its values. Decide what 0 sales should print. Then test 0, and the cases that worked.
  **On screen:** AI chat, stage 1: Plan: a bug hunt, not a fix
    - You: I am a beginner. My day report crashes when I type 0 sales. Do not fix anything yet and do not write code. Give me a short plan to find the cause.
    - AI (example answer): 1. Run it with 0 and copy the full traceback. 2. Read the last line: the kind of error. 3. Find the line number and the values used on that line. 4. Decide what the report should print for 0 sales. 5. Change one thing, then test 0 and the cases that already worked.
- **Narration:** Stage 2: write. Asha follows the plan. She runs the report with 0, and reads the traceback herself.
  **On screen:** AI chat, stage 2: Write: read it yourself first
    - You: Here is the error for 0 sales. My reading: the kind of error is ZeroDivisionError, it happened on line 8, and the cause is that sales is 0. Do not fix the code. Is my reading right? [code `examples/ai_zero_crash.py`]
- **Narration:** She writes down her reading: a Zero Division Error, on line 8, because sales is 0. Then she asks the AI to check her reading, without fixing anything.
  **On screen:** AI chat, stage 2: Write: read it yourself first
    - You: Here is the error for 0 sales. My reading: the kind of error is ZeroDivisionError, it happened on line 8, and the cause is that sales is 0. Do not fix the code. Is my reading right? [code `examples/ai_zero_crash.py`]
- **Narration:** The AI agrees with all three points. Dividing by zero has no answer, so Python stops.
  **On screen:** AI chat, stage 2: Write: read it yourself first
    - You: Here is the error for 0 sales. My reading: the kind of error is ZeroDivisionError, it happened on line 8, and the cause is that sales is 0. Do not fix the code. Is my reading right? [code `examples/ai_zero_crash.py`]
    - AI (example answer): Yes, all three points are right. The markers point at `total / sales`. Dividing by zero has no answer, so Python stops.
- **Narration:** Stage 3: generate. Asha asks for a check, so that 0 sales prints, No sales today. She asks what it prints for 0.
  **On screen:** AI chat, stage 3: Generate: a check for 0 sales
    - You: Add a check so that 0 sales prints No sales today. instead of crashing. Change only what is needed. Tell me exactly what it prints for 0 sales.
- **Narration:** The AI adds an if before the average, and promises: no sales today. It sounds completely sure.
  **On screen:** AI chat, stage 3: Generate: a check for 0 sales
    - You: Add a check so that 0 sales prints No sales today. instead of crashing. Change only what is needed. Tell me exactly what it prints for 0 sales.
    - AI (example answer): Here is the check. For 0 sales, the report prints `No sales today.` [code `examples/ai_check_flawed.py`]
- **Narration:** Look at line 8, and remember the boundary values from Chapter 6.
  **On screen:** AI chat, stage 3: Generate: a check for 0 sales
    - You: Add a check so that 0 sales prints No sales today. instead of crashing. Change only what is needed. Tell me exactly what it prints for 0 sales.
    - AI (example answer): Here is the check. For 0 sales, the report prints `No sales today.` [code `examples/ai_check_flawed.py`]
- **Interaction:** "The AI says 0 sales prints `No sales today.` Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Greater than or equal to 0 is true when sales is 0. So the program still reaches the division.
  **On screen:** AI chat, stage 3: Generate: a check for 0 sales
    - You: Add a check so that 0 sales prints No sales today. instead of crashing. Change only what is needed. Tell me exactly what it prints for 0 sales.
    - AI (example answer): Here is the check. For 0 sales, the report prints `No sales today.` [code `examples/ai_check_flawed.py`]
- **Narration:** Asha runs it with 0. The same crash, now on line 9. The AI's fix crashed on the same division.
  **On screen:** Code `examples/ai_check_flawed.py`, line 8, 9 highlighted, error `examples/ai_check_flawed.expected_error`
- **Narration:** Stage 4: test. Asha asks for test cases, each with the exact input and the expected result: 0 sales, 1 sale and 3 sales.
  **On screen:** AI chat, stage 4: Test: a list of cases
    - You: List test cases for my report, with the exact input and the expected last lines for each. Include 0 sales, 1 sale and 3 sales.
- **Narration:** The AI lists three cases. 1 sale and 0 sales are edge cases: unusual answers that often break code.
  **On screen:** AI chat, stage 4: Test: a list of cases
    - You: List test cases for my report, with the exact input and the expected last lines for each. Include 0 sales, 1 sale and 3 sales.
    - AI (example answer): 1. 0 sales: `No sales today.` 2. 1 sale of 5.00: Total 5.00, Average 5.00. 3. 3 sales of 4.50, 6.00 and 3.50: Total 14.00, Average 4.67.
- **Narration:** She runs every case on the AI's code. Three sales give 14.00 and 4.67, a pass. One sale of 5.00 passes too.
  **On screen:** Code `examples/ai_test_three.py`, line 8 highlighted, output `examples/ai_test_three.expected`
- **Narration:** So two cases pass. But the case that matters, 0 sales, fails.
  **On screen:** Table: Three cases on the AI's code (row 1 in focus)
- **Narration:** The AI's code only works when there was nothing to fix.
  **On screen:** Table: Three cases on the AI's code
- **Narration:** Stage 5: debug. Now Asha writes the full debugging prompt: the code, the exact error, the expected result, no sales today, and the actual result, a crash.
  **On screen:** AI chat, stage 5: Debug: the structured prompt
    - You: Code: my report with your check. Exact error: below. Expected result for 0 sales: No sales today. Actual result: it printed the heading, then the error report below. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_check_flawed.py`]
- **Narration:** She asks for the cause first. The AI names line 8: greater than or equal lets 0 through. The smallest fix is greater than 0.
  **On screen:** AI chat, stage 5: Debug: the structured prompt
    - You: Code: my report with your check. Exact error: below. Expected result for 0 sales: No sales today. Actual result: it printed the heading, then the error report below. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_check_flawed.py`]
    - AI (example answer): The cause is line 8. `sales >= 0` is true when sales is 0, so line 9 still divides by 0. The smallest fix: `if sales > 0:`
- **Narration:** Asha changes line 8 and runs it with 0. No sales today. No crash.
  **On screen:** Code `examples/ai_check_fixed.py`, line 8 highlighted, output `examples/ai_check_fixed.expected`
- **Narration:** A fix can break a case that worked before. So she runs every case again. Three sales: still 14.00 and 4.67, and one sale still gives 5.00.
  **On screen:** Code `examples/ai_fixed_three.py`, line 8 highlighted, output `examples/ai_fixed_three.expected`
- **Narration:** All three cases pass on the fixed code.
  **On screen:** Table: Every case again, on the fixed code (row 1 in focus)
- **Narration:** Stage 6: improve. The report works. Asha asks for at most two changes that make future bugs easier to find. And she adds: do not change what it prints.
  **On screen:** AI chat, stage 6: Improve: easier to debug next time
    - You: My report works. Suggest at most two changes that make future bugs easier to find, each with one reason. Do not change what it prints.
- **Narration:** Suggestion 1: rename sale to sale number, so nobody adds it instead of price. That would have made the bug from step 4 easier to spot!
  **On screen:** AI chat, stage 6: Improve: easier to debug next time
    - You: My report works. Suggest at most two changes that make future bugs easier to find, each with one reason. Do not change what it prints.
    - AI (example answer): 1. Rename `sale` to `sale_number`, so nobody adds it by mistake instead of `price`. 2. Keep a debug line inside the loop, so you can always see the total.
- **Narration:** Suggestion 2: keep a debug line inside the loop, so the total is always visible.
  **On screen:** AI chat, stage 6: Improve: easier to debug next time
    - You: My report works. Suggest at most two changes that make future bugs easier to find, each with one reason. Do not change what it prints.
    - AI (example answer): 1. Rename `sale` to `sale_number`, so nobody adds it by mistake instead of `price`. 2. Keep a debug line inside the loop, so you can always see the total.
- **Narration:** Asha tries both suggestions. Line 5 uses the new name.
  **On screen:** Code `examples/ai_improve_debug.py`, line 5 highlighted, output hidden
- **Narration:** And line 8 is the debug line the AI wants to keep.
  **On screen:** Code `examples/ai_improve_debug.py`, line 8 highlighted, output hidden
- **Interaction:** "Asha said: do not change what it prints. Does suggestion 2 keep that promise?" stays on screen with a 10-second timer.
- **Narration:** No. Three extra debug lines appear in the report. The AI ignored her instruction.
  **On screen:** Code `examples/ai_improve_debug.py`, line 8 highlighted, output `examples/ai_improve_debug.expected`
- **Narration:** Debug lines are for finding a bug, not for the finished report. So Asha keeps suggestion 1 only.
  **On screen:** Code `examples/ai_improve_debug.py`, line 8 highlighted, output `examples/ai_improve_debug.expected`
- **Narration:** Here is the result: a clear name on line 5, the check on line 8, and the same report as before. Every stage helped, and Asha checked every answer herself.
  **On screen:** Code `examples/ai_report_final.py`, line 5, 8 highlighted, output `examples/ai_report_final.expected`
- **Narration:** Quick check. An AI fixes your code, and says it works now. What do you do next?
  **On screen:** Quick check: "An AI fixes your code and says it works now. What do you do next?" (options shown)
- **Interaction:** "An AI fixes your code and says it works now. What do you do next?" stays on screen with a 10-second timer.
- **Narration:** D. Run the case that failed, and the cases that worked. A fix can break something else.
  **On screen:** Quick check: "An AI fixes your code and says it works now. What do you do next?" (answer revealed: Run the case that failed and the cases that worked)
- **Narration:** Breather. Asha caught two AI mistakes: a check that let 0 through, and a change she did not ask for.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Code, exact error, expected, actual.
    - After a fix, run every case again.
- **Narration:** Next, mistakes beginners make while debugging.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Code, exact error, expected, actual.
    - After a fix, run every case again.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes (13:15 to 14:41)

**Section:** Common mistakes

**Direction:** Mistake 1 is a spot-it with Python's own suggestion. Mistake 3 is a spot-it on indentation. Mistake 4 is the decimal comma.

- **Narration:** Now you try. Line 3 should print the word Total and the value of total.
  **On screen:** Code `examples/err01_comma.py`, line 3 highlighted, output hidden
- **Interaction:** "What is missing on line 3?" stays on screen with a 10-second timer.
- **Narration:** A comma between the two values. And look at the last line: Python even suggests it.
  **On screen:** Code `examples/err01_comma.py`, line 3 highlighted, error `examples/err01_comma.expected_error`
- **Narration:** Python's suggestions are often right, so always read them.
  **On screen:** Code `examples/err01_comma.py`, line 3 highlighted, error `examples/err01_comma.expected_error`
- **Narration:** One more. Asha adds a debug line on line 5. Compare its start with line 4.
  **On screen:** Code `examples/err03_indent.py`, line 5 highlighted, output hidden
- **Interaction:** "Why will Python refuse line 5?" stays on screen with a 10-second timer.
- **Narration:** Line 5 has six spaces at the start, but the block uses four. Python reports an Indentation Error.
  **On screen:** Code `examples/err03_indent.py`, line 5 highlighted, error `examples/err03_indent.expected_error`
- **Narration:** The fix: indent a debug line exactly like the line above it.
  **On screen:** Code `examples/err03_indent.py`, line 4, 5 highlighted, error `examples/err03_indent.expected_error`
- **Narration:** Mistake 3. In many countries, people write four and a half as 4 comma 50. Python accepts only a decimal point, so float stops with a Value Error.
  **On screen:** Code `examples/err04_decimal_comma.py`, line 2 highlighted, error `examples/err04_decimal_comma.expected_error`
- **Narration:** The message even shows the exact text that failed. The fix: type 4 point 50.
  **On screen:** Code `examples/err04_decimal_comma.py`, line 2 highlighted, error `examples/err04_decimal_comma.expected_error`
- **Narration:** Last breather. Now you know three mistakes that slow down a bug hunt.
  **On screen:** Breather card
    - Read Python's suggestions.
    - Create a variable before you use it.
    - Indent a debug line like its neighbours.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - Read Python's suggestions.
    - Create a variable before you use it.
    - Indent a debug line like its neighbours.
- **Breather:** 4 quiet seconds.

## Scene 13: Think beyond (14:41 to 15:28)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. A program gives the right total for 1 sale, but a wrong total for 3 sales. What kind of bug is it, and what would you print inside the loop?
  **On screen:** Question card: "A program gives the right total for 1 sale, but a wrong total for 3 sales. What kind of bug is it, and what would you print inside the loop?"
- **Interaction:** "A program gives the right total for 1 sale, but a wrong total for 3 sales. What kind of bug is it, and what would you print inside the loop?" stays on screen with a 10-second timer.
- **Narration:** Think about which values change on every pass.
  **On screen:** Question card: "A program gives the right total for 1 sale, but a wrong total for 3 sales. What kind of bug is it, and what would you print inside the loop?"
- **Narration:** Second. What happens if someone types a negative number of sales into Asha's report? Predict first, then run it.
  **On screen:** Question card: "What happens if someone types a negative number of sales into Asha's report?"
- **Interaction:** "What happens if someone types a negative number of sales into Asha's report?" stays on screen with a 10-second timer.
- **Narration:** Then decide what the report should print in that case.
  **On screen:** Question card: "What happens if someone types a negative number of sales into Asha's report?"

## Scene 14: Recap (15:28 to 16:27)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap. A syntax error stops everything. A runtime error stops partway. A logic error gives a wrong result, with no message.
  **On screen:** Recap
    - Syntax error: nothing runs. Runtime error: a traceback partway. Logic error: a wrong result, no message.
- **Narration:** Read a traceback from the bottom up. The line Python names is where it noticed, and the cause can be earlier.
  **On screen:** Recap
    - Syntax error: nothing runs. Runtime error: a traceback partway. Logic error: a wrong result, no message.
    - Read a traceback from the bottom up.
    - The line Python names is where it noticed. The cause can be earlier.
- **Narration:** Print debugging shows values while the program runs. And a debugging prompt has the code, the exact error, the expected result and the actual result.
  **On screen:** Recap
    - Syntax error: nothing runs. Runtime error: a traceback partway. Logic error: a wrong result, no message.
    - Read a traceback from the bottom up.
    - The line Python names is where it noticed. The cause can be earlier.
    - Print debugging shows values while the program runs. Remove it afterwards.
    - A debugging prompt: code, exact error, expected result, actual result. Cause first.
- **Narration:** And after a fix, test the case that failed, and the cases that worked.
  **On screen:** Recap
    - Syntax error: nothing runs. Runtime error: a traceback partway. Logic error: a wrong result, no message.
    - Read a traceback from the bottom up.
    - The line Python names is where it noticed. The cause can be earlier.
    - Print debugging shows values while the program runs. Remove it afterwards.
    - A debugging prompt: code, exact error, expected result, actual result. Cause first.
    - After a fix, test the case that failed and the cases that worked.
- **Narration:** One last check. A program stops on line 12 with a Type Error. Where can the cause be?
  **On screen:** Quick check: "A program stops on line 12 with a `TypeError`. Where can the cause be?" (options shown)
- **Interaction:** "A program stops on line 12 with a `TypeError`. Where can the cause be?" stays on screen with a 10-second timer.
- **Narration:** C. On line 12, or on an earlier line, like the cups from step 2.
  **On screen:** Quick check: "A program stops on line 12 with a `TypeError`. Where can the cause be?" (answer revealed: On line 12 or on an earlier line)
- **Narration:** Mission complete! You earned 100 XP and the Bug Hunter badge.
  **On screen:** Bug Hunter You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice (16:27 to 16:55)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. The practice file has eight tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each, including reading a traceback.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each. In one, a wrong total looks right by luck.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each: a report with three bugs, and an AI's member price to fix.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Work out the expected result before you run anything. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 16: What's next (16:55 to 17:22)

**Section:** What's next

**Direction:** End card. Tease the guessing game: decisions, loops and input checks together. Hold quietly at the end.

- **Narration:** Today Asha's report learned to handle 0 sales. But it still trusts every answer. Type a word instead of a number, and it crashes.
  **On screen:** Boss Level 2: The Number Guessing Game Decisions, loops and input checks, together.
- **Narration:** In Chapter 10, the second boss level, you will build a number guessing game. A secret number, hints, a limit on tries, and answers that are checked first.
  **On screen:** Boss Level 2: The Number Guessing Game Decisions, loops and input checks, together.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Boss Level 2: The Number Guessing Game Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 10.
  **On screen:** Boss Level 2: The Number Guessing Game Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
