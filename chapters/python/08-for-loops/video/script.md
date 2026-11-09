# Video Script: Chapter 8: Repeat a Set Number of Times: for Loops and range()

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:53.

## Scene 1: Introduction (0:00 to 0:44)

**Section:** Introduction

**Direction:** Open on the Chapter 7 counter loop and its three places to make a mistake. Then the title and the AI tease, then the finished price chart as the mission.

- **Narration:** Here is Asha's loop from Chapter 7. To serve three tables, she needed three separate lines: a start, a condition, and an update.
  **On screen:** Three lines to get right
- **Narration:** Three places to make a mistake. Forget the update, and the loop never ends.
  **On screen:** Three lines to get right
- **Narration:** This is Code Quest, Chapter 8. Today you meet a loop that counts for you.
  **On screen:** Repeat a Set Number of Times: for Loops and range()
- **Narration:** And an AI assistant will rewrite Asha's loyalty card, promise the same ten stamps, and quietly lose a free tea.
  **On screen:** Repeat a Set Number of Times: for Loops and range() A loop that counts for you.
- **Narration:** So here is today's mission. A price chart for the cafe counter, from 1 tea to 10 teas.
  **On screen:** Code `examples/ex06_price_chart.py`, line 4 highlighted, output `examples/ex06_price_chart.expected`
- **Narration:** Every 5th tea is free, and the chart works out the free teas by itself.
  **On screen:** Code `examples/ex06_price_chart.py`, line 5, 6 highlighted, output `examples/ex06_price_chart.expected`
- **Narration:** Ten rows, from a loop with no counter of its own. Let's build it.
  **On screen:** Code `examples/ex06_price_chart.py`, output `examples/ex06_price_chart.expected`

## Scene 2: Learning goals (0:44 to 1:00)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Write a for loop that repeats once for each number in a range.
  **On screen:** By the end, you will be able to:
    - Write a `for` loop that repeats once for each number in a `range()`.
- **Narration:** Use range with a start, a stop and a step.
  **On screen:** By the end, you will be able to:
    - Write a `for` loop that repeats once for each number in a `range()`.
    - Use `range()` with a start, a stop and a step.
- **Narration:** Go through every character of a string.
  **On screen:** By the end, you will be able to:
    - Write a `for` loop that repeats once for each number in a `range()`.
    - Use `range()` with a start, a stop and a step.
    - Go through every character of a string.
- **Narration:** Add up a total inside a for loop.
  **On screen:** By the end, you will be able to:
    - Write a `for` loop that repeats once for each number in a `range()`.
    - Use `range()` with a start, a stop and a step.
    - Go through every character of a string.
    - Add up a total inside a `for` loop.
- **Narration:** And compare two loops, and explain which one is clearer.
  **On screen:** By the end, you will be able to:
    - Write a `for` loop that repeats once for each number in a `range()`.
    - Use `range()` with a start, a stop and a step.
    - Go through every character of a string.
    - Add up a total inside a `for` loop.
    - Compare two loops and explain which one is clearer.

## Scene 3: Why this matters (1:00 to 1:11)

**Section:** Why this matters

**Direction:** Known numbers of passes are everywhere.

- **Narration:** Often you know in advance how many times something must happen: 5 receipt lines, 10 stamps, 12 characters. For these jobs, Python has the for loop.
  **On screen:** Why this matters
    - A receipt has 5 lines.
    - A loyalty card has 10 stamps.
    - An order code has 12 characters.

## Scene 4: The idea: one value at a time (1:11 to 2:25)

**Section:** The idea

**Direction:** Teach the sequence, the loop variable and the stop rule with the diagram, then the stamp card analogy. Then a quiz and a breather.

- **Narration:** A for loop takes values from a sequence, one at a time. A sequence is a group of values in a fixed order, like numbers, or the characters of a string.
  **On screen:** for: take the next value
- **Narration:** On each pass, the loop variable gets the next value. Here, table is 1, then 2, then 3. When no values are left, the loop ends.
  **On screen:** for: take the next value
- **Narration:** And here is the most important rule. Range stops before the stop value. Range with 1 and 4 gives 1, 2 and 3. Never 4.
  **On screen:** for: take the next value
- **Narration:** Think of a stamp card. You move from box to box, one at a time, and you never skip a box.
  **On screen:** Like a stamp card
    - You move from box to box, one at a time, and never skip a box.
- **Narration:** But unlike a stamp card, range leaves out the number at the end. Range with 1 and 4 has boxes 1, 2 and 3. There is no box 4.
  **On screen:** Like a stamp card
    - You move from box to box, one at a time, and never skip a box.
    - Unlike a stamp card, `range()` leaves out the number written at the end.
    - `range(1, 4)`: boxes 1, 2 and 3. There is no box 4.
- **Narration:** Quick check. Which numbers does range with 2 and 5 give?
  **On screen:** Quick check: "Which numbers does `range(2, 5)` give?" (options shown)
- **Interaction:** "Which numbers does `range(2, 5)` give?" stays on screen with a 10-second timer.
- **Narration:** D. 2, 3 and 4. It starts at 2, and stops before 5.
  **On screen:** Quick check: "Which numbers does `range(2, 5)` give?" (answer revealed: 2, 3, 4)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - A `for` loop takes one value at a time.
    - The loop variable gets the next value on each pass.
    - `range()` stops before the stop value.
- **Narration:** Next, Asha rewrites her table loop from Chapter 7.
  **On screen:** Breather card
    - A `for` loop takes one value at a time.
    - The loop variable gets the next value on each pass.
    - `range()` stops before the stop value.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: for and range() (2:25 to 3:06)

**Section:** Build it step by step

**Direction:** The file types in. Compare with the Chapter 7 loop, then ask how many lines print.

- **Narration:** Step 1. Here is the Chapter 7 loop, written with for. Line 2 says: for table in range with 1 and 4.
  **On screen:** Code `examples/ex01_tables.py`, lines 1 to 2 typed in, line 2 highlighted, output hidden
- **Narration:** Line 3 prints the table number. It is indented, so it is the block of the loop.
  **On screen:** Code `examples/ex01_tables.py`, lines 1 to 3 typed in, line 3 highlighted, output hidden
- **Narration:** Line 4 is not indented. It runs once, after the loop.
  **On screen:** Code `examples/ex01_tables.py`, lines 1 to 4 typed in, line 4 highlighted, output hidden
- **Interaction:** "How many times does line 3 print, and which table is the last one?" stays on screen with a 10-second timer.
- **Narration:** Three times, and the last table is 3. Range stops before 4.
  **On screen:** Code `examples/ex01_tables.py`, lines 1 to 4 typed in, line 3 highlighted, output `examples/ex01_tables.expected`
- **Narration:** And look: no start line, and no update line. Range does both jobs. One place to get right, not three.
  **On screen:** Code `examples/ex01_tables.py`, lines 1 to 4 typed in, line 2 highlighted, output `examples/ex01_tables.expected`

## Scene 6: Step 2: The three forms of range() (3:06 to 4:00)

**Section:** Build it step by step

**Direction:** Teach the three forms in words first, then ask for the three outputs, then reveal and summarise in a table.

- **Narration:** Step 2. Range has three forms. With one number, it starts at 0. So range with 4 gives four values, starting at 0.
  **On screen:** Code `examples/ex02_range_forms.py`, line 2 highlighted, output hidden
- **Narration:** With two numbers, you give the start and the stop.
  **On screen:** Code `examples/ex02_range_forms.py`, line 5 highlighted, output hidden
- **Narration:** With three numbers, the third is the step: how much to add each time. A negative step counts down.
  **On screen:** Code `examples/ex02_range_forms.py`, line 8 highlighted, output hidden
- **Narration:** End equals a space, from Chapter 1, keeps each loop's numbers on one line. The empty print ends the line.
  **On screen:** Code `examples/ex02_range_forms.py`, line 3, 4 highlighted, output hidden
- **Interaction:** "What do the three loops print? Remember: each stops before its stop value." stays on screen with a 10-second timer.
- **Narration:** Range with 4 gives 0, 1, 2 and 3. Four values, starting at 0.
  **On screen:** Code `examples/ex02_range_forms.py`, line 2 highlighted, output `examples/ex02_range_forms.expected`
- **Narration:** Range with 2 and 6 gives 2 to 5.
  **On screen:** Code `examples/ex02_range_forms.py`, line 5 highlighted, output `examples/ex02_range_forms.expected`
- **Narration:** And 10, counting down by 3: 10, 7, 4, 1. The next value would be minus 2, and that is past the stop value, 0.
  **On screen:** Code `examples/ex02_range_forms.py`, line 8 highlighted, output `examples/ex02_range_forms.expected`

## Scene 7: Step 3: Loop over a string (4:00 to 4:54)

**Section:** Build it step by step

**Direction:** Teach looping over characters with the order code from Chapter 1, ask the count, reveal.

- **Narration:** Step 3. A for loop can also take the characters of a string, one at a time. Here is the order code from Chapter 1. Line 3 starts a hyphen counter at 0.
  **On screen:** Code `examples/ex03_order_code.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 4: for character in code. On each pass, character is the next letter, digit or hyphen.
  **On screen:** Code `examples/ex03_order_code.py`, line 4 highlighted, output hidden
- **Narration:** Line 5 prints it, with a space after it. Lines 6 and 7 add 1 to the counter, but only when the character is a hyphen.
  **On screen:** Code `examples/ex03_order_code.py`, line 5, 6, 7 highlighted, output hidden
- **Narration:** Line 8, an empty print, ends the line of characters. Line 9 prints the length, with len from Chapter 3, and the hyphens.
  **On screen:** Code `examples/ex03_order_code.py`, line 8, 9 highlighted, output hidden
- **Interaction:** "How many times does the block run, and how many hyphens does line 9 report?" stays on screen with a 10-second timer.
- **Narration:** The block runs 12 times, once for each character.
  **On screen:** Code `examples/ex03_order_code.py`, line 4, 5 highlighted, output `examples/ex03_order_code.expected`
- **Narration:** And 2 hyphens. The if adds 1 only on those two passes.
  **On screen:** Code `examples/ex03_order_code.py`, line 6, 7, 9 highlighted, output `examples/ex03_order_code.expected`

## Scene 8: Step 4: A running total (4:54 to 5:50)

**Section:** Build it step by step

**Direction:** Teach the running total in a for loop with input inside. Ask for the total, reveal.

- **Narration:** Step 4. Asha adds up three days of sales. Line 2 sets the total to 0, once, before the loop.
  **On screen:** Code `examples/ex04_week_sales.py`, line 2 highlighted, output hidden
- **Narration:** Line 3: for day in range with 1 and 4. So there are three passes, for days 1, 2 and 3.
  **On screen:** Code `examples/ex04_week_sales.py`, line 3 highlighted, output hidden
- **Narration:** Line 4 asks for the sales of that day. The f string puts the day number in the question. Line 5 adds the answer to the total.
  **On screen:** Code `examples/ex04_week_sales.py`, line 4, 5 highlighted, output hidden
- **Narration:** Lines 6 and 7 run once, after the loop: the total, and the average, which is the total divided by 3.
  **On screen:** Code `examples/ex04_week_sales.py`, line 6, 7 highlighted, output hidden
- **Interaction:** "How many times does line 4 ask a question, and how many times do lines 6 and 7 print?" stays on screen with a 10-second timer.
- **Narration:** Line 4 asks three times, once per pass. Lines 6 and 7 print once each, after the loop.
  **On screen:** Code `examples/ex04_week_sales.py`, line 4 highlighted, output `examples/ex04_week_sales.expected`
- **Narration:** The total is 361.75, and the average is 120.58, with two decimal places.
  **On screen:** Code `examples/ex04_week_sales.py`, line 6, 7 highlighted, output `examples/ex04_week_sales.expected`

## Scene 9: Step 5: Count down, and choose a loop (5:50 to 7:13)

**Section:** Build it step by step

**Direction:** Teach the negative step with the kettle, ask for the last number, reveal. Then for or while, then a quiz and a breather.

- **Narration:** Step 5. The kettle needs 5 minutes. Range with 5, 0 and minus 1 starts at 5, and takes away 1 each time.
  **On screen:** Code `examples/ex05_kettle.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 prints the minutes left. Line 4 runs after the loop.
  **On screen:** Code `examples/ex05_kettle.py`, line 3, 4 highlighted, output hidden
- **Interaction:** "What is the last number that line 3 prints: 1 or 0?" stays on screen with a 10-second timer.
- **Narration:** 1. The stop value is 0, and range stops before it.
  **On screen:** Code `examples/ex05_kettle.py`, line 3 highlighted, output `examples/ex05_kettle.expected`
- **Narration:** Then line 4: tea is ready.
  **On screen:** Code `examples/ex05_kettle.py`, line 4 highlighted, output `examples/ex05_kettle.expected`
- **Narration:** So which loop should you choose? Use for when you know the number of passes before the loop starts. Five minutes, ten stamps, twelve characters.
  **On screen:** for or while?
    - `for`: you know the number of passes before the loop starts. 5 minutes, 10 stamps, 12 characters.
- **Narration:** Use while when you wait for something, like a valid answer, or the word done. Then you cannot know how many passes it will take.
  **On screen:** for or while?
    - `for`: you know the number of passes before the loop starts. 5 minutes, 10 stamps, 12 characters.
    - `while`: you wait for something, such as a valid answer or the word `done`.
- **Narration:** Quick check. A program asks for a PIN until the customer types the right one. Which loop fits best?
  **On screen:** Quick check: "Which loop fits best: ask for a PIN until the customer types the right one?" (options shown)
- **Interaction:** "Which loop fits best: ask for a PIN until the customer types the right one?" stays on screen with a 10-second timer.
- **Narration:** C. A while loop. You wait for the right answer, so you cannot know the number of passes.
  **On screen:** Quick check: "Which loop fits best: ask for a PIN until the customer types the right one?" (answer revealed: `while`)
- **Narration:** Breather. Sit back, and take a slow breath.
  **On screen:** Breather card
    - `range(stop)` starts at 0.
    - A third number is the step. A negative step counts down.
    - `for` when you know the passes, `while` when you wait.
- **Narration:** You now have every piece of the mission.
  **On screen:** Breather card
    - `range(stop)` starts at 0.
    - A third number is the step. A negative step counts down.
    - `for` when you know the passes, `while` when you wait.
- **Breather:** 4 quiet seconds.

## Scene 10: See the outcome: the price chart (7:13 to 8:18)

**Section:** See the outcome

**Direction:** Return to the mission. Explain every line, ask which rows repeat the price above, reveal. Hand over to the AI story.

- **Narration:** Back to the mission. Line 2 stores the tea price. Line 3 prints the column headings.
  **On screen:** Code `examples/ex06_price_chart.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 4: for teas in range with 1 and 11. That gives 1 to 10.
  **On screen:** Code `examples/ex06_price_chart.py`, line 4 highlighted, output hidden
- **Narration:** Line 5 counts the free teas: teas, floor divided by 5, from Chapter 2. 4 teas give 0 free teas. 5 teas give 1.
  **On screen:** Code `examples/ex06_price_chart.py`, line 5 highlighted, output hidden
- **Narration:** Line 6 charges only the teas that are not free. Line 7 lines up the columns with the format codes from Chapter 3. And line 8 runs once, after the loop.
  **On screen:** Code `examples/ex06_price_chart.py`, line 6, 7, 8 highlighted, output hidden
- **Interaction:** "Which two rows show the same price as the row above them?" stays on screen with a 10-second timer.
- **Narration:** 5 teas and 10 teas. At 5 teas, one tea is free, so 5 cost 14.00, the same as 4.
  **On screen:** Code `examples/ex06_price_chart.py`, line 5, 6 highlighted, output `examples/ex06_price_chart.expected`
- **Narration:** At 10 teas, two are free, so 10 cost 28.00, the same as 9.
  **On screen:** Code `examples/ex06_price_chart.py`, line 5, 6 highlighted, output `examples/ex06_price_chart.expected`
- **Narration:** Mission complete! Next, the loyalty card. Asha wrote it with a while loop. Now she will rewrite it with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex06_price_chart.py`, output `examples/ex06_price_chart.expected`

## Scene 11: Work with AI: six stages, one loyalty card (8:18 to 13:30)

**Section:** Work with AI

**Direction:** Teach the comparing skill. One conversation per stage, all about the 10-stamp card. Stage 3 plants the off-by-one, stage 4 catches it with checks and re-runs every check after the fix, stage 6 catches an ignored instruction.

- **Narration:** This chapter's AI skill is comparing loops. When an AI writes a loop for a job you already solved, run both with the same values.
  **On screen:** This chapter's AI skill: comparing loops
    - Run the AI's loop and yours with the same values.
    - Compare the outputs line by line: count the lines, read the last line.
- **Narration:** Compare the outputs line by line. Then decide which loop is clearer for the next person who reads it. And the safety habits from Chapter 1 still apply.
  **On screen:** This chapter's AI skill: comparing loops
    - Run the AI's loop and yours with the same values.
    - Compare the outputs line by line: count the lines, read the last line.
    - Then decide which loop is clearer. Never paste private data.
- **Narration:** Stage 1: plan. Asha's loyalty card has 10 stamps, and every 5th stamp is a free tea. She wrote it with a while loop, and wants to rewrite it with for. She asks: is for a good fit, and which range? No code yet.
  **On screen:** AI chat, stage 1: Plan: for or while?
    - You: I am a beginner. My loyalty card has 10 stamps, and every 5th stamp is a free tea. I wrote it with a while loop, and I want to rewrite it with a for loop. Do not write code yet. Is a for loop a good fit, and which range() gives the stamps 1 to 10?
- **Narration:** The AI says: a for loop, because you know the number of passes. And range with 1 and 11, because the stop value is never included. A good plan.
  **On screen:** AI chat, stage 1: Plan: for or while?
    - You: I am a beginner. My loyalty card has 10 stamps, and every 5th stamp is a free tea. I wrote it with a while loop, and I want to rewrite it with a for loop. Do not write code yet. Is a for loop a good fit, and which range() gives the stamps 1 to 10?
    - AI (example answer): A `for` loop. You know the number of passes before the loop starts: 10. Use `range(1, 11)`. It gives 1 to 10, because the stop value is never included.
- **Narration:** Stage 2: write. Before the rewrite, Asha checks her own while loop. She asks the AI to list every value of stamp, without changing anything.
  **On screen:** AI chat, stage 2: Write: list the values first
    - You: Here is the loop I wrote. Do not change it and do not run it. List every value of stamp, and say how many passes there are. [code `examples/ai_stamps_mine.py`]
- **Narration:** The AI lists 1 to 10: ten passes. Stamps 5 and 10 have no remainder when divided by 5, so they print free tea. Asha's own list says the same.
  **On screen:** AI chat, stage 2: Write: list the values first
    - You: Here is the loop I wrote. Do not change it and do not run it. List every value of stamp, and say how many passes there are. [code `examples/ai_stamps_mine.py`]
    - AI (example answer): `stamp` takes 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10: 10 passes. Stamps 5 and 10 print FREE TEA, because 5 and 10 leave no remainder when divided by 5.
- **Narration:** She runs it. Ten stamps, with free tea on 5 and 10. And notice the three lines from Chapter 7 again: a start, a condition, and an update.
  **On screen:** Code `examples/ai_stamps_mine.py`, line 2, 3, 8 highlighted, output `examples/ai_stamps_mine.expected`
- **Narration:** Stage 3: generate. Asha asks for a for version with the same output: 10 stamps, with free tea on 5 and 10.
  **On screen:** AI chat, stage 3: Generate: a for version
    - You: Rewrite my loyalty card with a for loop and range(). Keep the same output: 10 stamps, with FREE TEA on stamps 5 and 10. Show the exact output.
- **Narration:** The AI gives a short for loop, and promises the same 10 lines. It sounds completely sure.
  **On screen:** AI chat, stage 3: Generate: a for version
    - You: Rewrite my loyalty card with a for loop and range(). Keep the same output: 10 stamps, with FREE TEA on stamps 5 and 10. Show the exact output.
    - AI (example answer): Here is the `for` version. It prints the same 10 lines as yours, with FREE TEA on stamps 5 and 10. [code `examples/ai_stamps_flawed.py`]
- **Narration:** Look at line 2, and remember where range stops.
  **On screen:** AI chat, stage 3: Generate: a for version
    - You: Rewrite my loyalty card with a for loop and range(). Keep the same output: 10 stamps, with FREE TEA on stamps 5 and 10. Show the exact output.
    - AI (example answer): Here is the `for` version. It prints the same 10 lines as yours, with FREE TEA on stamps 5 and 10. [code `examples/ai_stamps_flawed.py`]
- **Interaction:** "The AI promises 10 stamps. How many stamps does `range(1, 10)` give?" stays on screen with a 10-second timer.
- **Narration:** Nine. Range with 1 and 10 stops before 10. Asha suspects a problem. Now she proves it with checks.
  **On screen:** AI chat, stage 3: Generate: a for version
    - You: Rewrite my loyalty card with a for loop and range(). Keep the same output: 10 stamps, with FREE TEA on stamps 5 and 10. Show the exact output.
    - AI (example answer): Here is the `for` version. It prints the same 10 lines as yours, with FREE TEA on stamps 5 and 10. [code `examples/ai_stamps_flawed.py`]
- **Narration:** Stage 4: test. Asha asks for four checks, each with the exact expected result: the first line, stamp 5, the last line, and the number of lines.
  **On screen:** AI chat, stage 4: Test: checks with expected results
    - You: Before I trust it, list 4 checks for the output: the first line, the last line, the number of lines and stamp 5. Give the exact expected result for each.
- **Narration:** The AI lists them. The last line should be stamp 10, free tea. And there should be 10 lines.
  **On screen:** AI chat, stage 4: Test: checks with expected results
    - You: Before I trust it, list 4 checks for the output: the first line, the last line, the number of lines and stamp 5. Give the exact expected result for each.
    - AI (example answer): 1. First line: `Stamp 1: [ ]`. 2. Stamp 5: `Stamp 5: FREE TEA`. 3. Last line: `Stamp 10: FREE TEA`. 4. Number of lines: 10.
- **Narration:** She runs the AI's version, and reads the last line first. Stamp 9, an empty box.
  **On screen:** Code `examples/ai_stamps_flawed.py`, line 2 highlighted, output `examples/ai_stamps_flawed.expected`
- **Narration:** She counts the lines: nine. The second free tea is missing.
  **On screen:** Code `examples/ai_stamps_flawed.py`, line 2 highlighted, output `examples/ai_stamps_flawed.expected`
- **Narration:** The first line and stamp 5 pass.
  **On screen:** Table: The four checks on the AI's code (row 2 in focus)
- **Narration:** But the last line fails, and so does the number of lines. This is an off-by-one error, the same kind as in Chapter 7.
  **On screen:** Table: The four checks on the AI's code (row 4 in focus)
- **Narration:** The fix is on line 2. The stop value must be one more than the last stamp: range with 1 and 11. Now stamp 10 is there, with its free tea.
  **On screen:** Code `examples/ai_stamps_fixed.py`, line 2 highlighted, output `examples/ai_stamps_fixed.expected`
- **Narration:** A fix can break something else. So Asha runs every check again, on the fixed code.
  **On screen:** Table: All four checks again, on the fixed code
- **Narration:** All four pass, and the output matches her while version, line by line.
  **On screen:** Table: All four checks again, on the fixed code (row 4 in focus)
- **Narration:** Stage 5: debug. Now the customer types the size of the card. Python stops with a Type Error. Asha pastes the code and the full error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: Now the customer types the size of the card. I got this error. First explain what it means and which line causes it. Then show the smallest fix. [code `examples/ai_stamps_size.py`]
- **Narration:** She reads the error herself too: line 3, can only concatenate. She met that message in Chapter 4.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: Now the customer types the size of the card. I got this error. First explain what it means and which line causes it. Then show the smallest fix. [code `examples/ai_stamps_size.py`]
- **Narration:** The AI agrees. Input always gives text, so size plus 1 fails. The fix is int, on line 2.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: Now the customer types the size of the card. I got this error. First explain what it means and which line causes it. Then show the smallest fix. [code `examples/ai_stamps_size.py`]
    - AI (example answer): It is a `TypeError` on line 3. `input()` always gives text, so `size` is the text "10". Python cannot add the number 1 to text. The fix: convert the answer on line 2, `size = int(input("Stamps on the card: "))`.
- **Narration:** Asha applies the fix on line 2, and runs it again with 10.
  **On screen:** Code `examples/ai_stamps_size_fixed.py`, line 2 highlighted, output `examples/ai_stamps_size_fixed.expected`
- **Narration:** Then she runs all four checks again. First line, stamp 5, last line, and ten stamps. All pass.
  **On screen:** Code `examples/ai_stamps_size_fixed.py`, line 2 highlighted, output `examples/ai_stamps_size_fixed.expected`
- **Narration:** Stage 6: improve. Asha shows both loops, her while loop and the fixed for loop, and asks which one is clearer. She adds: do not change what it prints.
  **On screen:** AI chat, stage 6: Improve: which loop is clearer?
    - You: Here are my while loop and my fixed for loop. Which one is clearer for a beginner, and why? Suggest at most one change. Do not change what it prints.
- **Narration:** The AI chooses the for loop: there is no counter line to forget. Then it suggests one change: range with 10, and print stamp plus 1. It says the output stays the same.
  **On screen:** AI chat, stage 6: Improve: which loop is clearer?
    - You: Here are my while loop and my fixed for loop. Which one is clearer for a beginner, and why? Suggest at most one change. Do not change what it prints.
    - AI (example answer): The `for` loop is clearer: there is no counter line to forget. One change: use `range(10)` and print `stamp + 1`. The output stays the same.
- **Narration:** Asha runs the suggestion, and compares its output with her card, line by line. Line 2 now counts from 0, so every print adds 1 to stamp.
  **On screen:** Code `examples/ai_stamps_improve.py`, line 2 highlighted, output hidden
- **Interaction:** "Compare with Asha's card: which lines of the output change?" stays on screen with a 10-second timer.
- **Narration:** Stamps 5 and 10. Free tea is now in small letters. Asha had said: do not change what it prints. The AI ignored that.
  **On screen:** Code `examples/ai_stamps_improve.py`, line 4 highlighted, output `examples/ai_stamps_improve.expected`
- **Narration:** And stamp plus 1, written three times, is harder to read than range with 1 and 11, which matches the numbers on the card. Asha keeps her fixed for loop.
  **On screen:** Code `examples/ai_stamps_improve.py`, line 4 highlighted, output `examples/ai_stamps_improve.expected`
- **Narration:** Quick check. An AI says its loop prints the same as yours. What do you check first?
  **On screen:** Quick check: "An AI says its loop prints the same as yours. What do you check first?" (options shown)
- **Interaction:** "An AI says its loop prints the same as yours. What do you check first?" stays on screen with a 10-second timer.
- **Narration:** A. Count the lines, and read the last line. Off-by-one errors hide at the end.
  **On screen:** Quick check: "An AI says its loop prints the same as yours. What do you check first?" (answer revealed: Count the lines and read the last line)
- **Narration:** Breather. Asha caught two AI mistakes: a missing stamp, and a change she did not ask for.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Count the lines and read the last line.
    - After a fix, run every check again.
- **Narration:** Next, the four mistakes beginners make most with for loops.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Count the lines and read the last line.
    - After a fix, run every check again.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes (13:30 to 15:17)

**Section:** Common mistakes

**Direction:** Mistake 1 is a spot-it on the stop value, a callback to the AI. Mistake 2 is a real TypeError. Mistake 3 is a spot-it on the total. Mistake 4 is a real SyntaxError. Then a summary table.

- **Narration:** Now you try. Asha wants to serve tables 1 to 3. Look at line 2.
  **On screen:** Code `examples/ex07_off_by_one.py`, line 2 highlighted, output hidden
- **Interaction:** "Asha wants tables 1 to 3. Which table is never served?" stays on screen with a 10-second timer.
- **Narration:** Table 3. Range with 1 and 3 stops before 3. It is the AI's mistake again.
  **On screen:** Code `examples/ex07_off_by_one.py`, line 2 highlighted, output `examples/ex07_off_by_one.expected`
- **Narration:** No error, only a missing table. The fix: the stop value is one more than the last value you want. Range with 1 and 4.
  **On screen:** Code `examples/ex07_off_by_one.py`, line 2 highlighted, output `examples/ex07_off_by_one.expected`
- **Narration:** Mistake 2. Range works only with whole numbers. Zero point five is a float, so Python stops with a Type Error.
  **On screen:** Code `examples/err01_range_float.py`, line 2 highlighted, error `examples/err01_range_float.expected_error`
- **Narration:** The fix: use whole numbers. If a number comes from input, convert it with int, not float.
  **On screen:** Code `examples/err01_range_float.py`, line 2 highlighted, error `examples/err01_range_float.expected_error`
- **Narration:** One more. This is step 4 again, with one line in a different place. Compare it with step 4, line by line.
  **On screen:** Code `examples/ex08_total_inside.py`, output hidden
- **Interaction:** "The total should be 361.75. What does line 6 print, and why?" stays on screen with a 10-second timer.
- **Narration:** 143.25, only the last day. Line 3 is inside the loop, so the total goes back to 0 on every pass.
  **On screen:** Code `examples/ex08_total_inside.py`, line 3 highlighted, output `examples/ex08_total_inside.expected`
- **Narration:** No error, only a wrong total. The fix: set the total to 0 once, before the loop.
  **On screen:** Code `examples/ex08_total_inside.py`, output `examples/ex08_total_inside.expected`
- **Narration:** Mistake 4. Every for line ends with a colon, like if and while. Without it, Python stops before anything runs.
  **On screen:** Code `examples/err02_no_colon.py`, line 2 highlighted, error `examples/err02_no_colon.expected_error`
- **Narration:** The error even says what it expected: a colon.
  **On screen:** Code `examples/err02_no_colon.py`, line 2 highlighted, error `examples/err02_no_colon.expected_error`
- **Narration:** Last breather. Now you know the four most common for loop mistakes.
  **On screen:** Breather card
    - The stop value is one more than the last value.
    - `range()` needs whole numbers.
    - Set a total to 0 before the loop.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - The stop value is one more than the last value.
    - `range()` needs whole numbers.
    - Set a total to 0 before the loop.
- **Breather:** 4 quiet seconds.

## Scene 13: Think beyond (15:17 to 16:03)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Only even-numbered tables, from 2 to 20, get a stamp. Which one range gives exactly those numbers?
  **On screen:** Question card: "Only even-numbered tables, from 2 to 20, get a stamp. Which one `range()` gives exactly those numbers?"
- **Interaction:** "Only even-numbered tables, from 2 to 20, get a stamp. Which one `range()` gives exactly those numbers?" stays on screen with a 10-second timer.
- **Narration:** Think about the start, the stop and the step. Predict the values first, then run it.
  **On screen:** Question card: "Only even-numbered tables, from 2 to 20, get a stamp. Which one `range()` gives exactly those numbers?"
- **Narration:** Second. How could a for loop count every letter a in the name Anna Abbas, capital or small?
  **On screen:** Question card: "How could a `for` loop count every letter `a` in `Anna Abbas`, capital or small?"
- **Interaction:** "How could a `for` loop count every letter `a` in `Anna Abbas`, capital or small?" stays on screen with a 10-second timer.
- **Narration:** Think about which string method from Chapter 3 can help.
  **On screen:** Question card: "How could a `for` loop count every letter `a` in `Anna Abbas`, capital or small?"

## Scene 14: Recap (16:03 to 16:59)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check on something new, then the badge.

- **Narration:** Let's recap.
  **On screen:** Recap
- **Narration:** A for loop runs once for each value in a range or a string.
  **On screen:** Recap
    - A `for` loop runs once for each value in a `range()` or a string.
- **Narration:** Range stops before the stop value, and range with one number starts at 0.
  **On screen:** Recap
    - A `for` loop runs once for each value in a `range()` or a string.
    - `range(start, stop, step)` stops before `stop`. `range(4)` starts at 0.
- **Narration:** A negative step counts down. And a running total starts at 0 before the loop.
  **On screen:** Recap
    - A `for` loop runs once for each value in a `range()` or a string.
    - `range(start, stop, step)` stops before `stop`. `range(4)` starts at 0.
    - A negative step counts down.
    - A running total starts at 0 before the loop and grows inside it.
- **Narration:** Use for when you know the number of passes, and while when you wait for something.
  **On screen:** Recap
    - A `for` loop runs once for each value in a `range()` or a string.
    - `range(start, stop, step)` stops before `stop`. `range(4)` starts at 0.
    - A negative step counts down.
    - A running total starts at 0 before the loop and grows inside it.
    - Use `for` for a known number of passes, `while` when you wait for something.
- **Narration:** And with AI: run its loop and yours with the same values, and compare every line.
  **On screen:** Recap
    - A `for` loop runs once for each value in a `range()` or a string.
    - `range(start, stop, step)` stops before `stop`. `range(4)` starts at 0.
    - A negative step counts down.
    - A running total starts at 0 before the loop and grows inside it.
    - Use `for` for a known number of passes, `while` when you wait for something.
    - Run an AI loop and yours with the same values. Compare every line.
- **Narration:** One last check. Range with 0, 10 and 4. Which numbers does it give?
  **On screen:** Quick check: "Which numbers does `range(0, 10, 4)` give?" (options shown)
- **Interaction:** "Which numbers does `range(0, 10, 4)` give?" stays on screen with a 10-second timer.
- **Narration:** B. 0, 4 and 8. The next value, 12, is past the stop value, 10.
  **On screen:** Quick check: "Which numbers does `range(0, 10, 4)` give?" (answer revealed: 0, 4, 8)
- **Narration:** Mission complete! You earned 100 XP and the Pattern Runner badge.
  **On screen:** Pattern Runner You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice (16:59 to 17:27)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. The practice file has eight tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including a times table.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, an AI's total is 45 instead of 55. Find the missing number, and fix it.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** List the values of each range before you run it. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 16: What's next (17:27 to 17:53)

**Section:** What's next

**Direction:** End card. Tease debugging with AI: three kinds of problem met today. Hold quietly at the end.

- **Narration:** Today Asha met three kinds of problem. A syntax error, before anything runs. A type error, while the program runs. And a wrong total, with no error at all.
  **On screen:** Debugging with AI: Reading Errors and Tracebacks Three kinds of error, one method.
- **Narration:** In Chapter 9, you will learn to tell them apart, read a full traceback, and debug with AI, step by step.
  **On screen:** Debugging with AI: Reading Errors and Tracebacks Three kinds of error, one method.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Debugging with AI: Reading Errors and Tracebacks Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 9.
  **On screen:** Debugging with AI: Reading Errors and Tracebacks Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
