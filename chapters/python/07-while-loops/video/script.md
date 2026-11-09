# Video Script: Chapter 7: Repeat Until Done: while Loops

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:05.

## Scene 1: Introduction (0:00 to 0:45)

**Section:** Introduction

**Direction:** Open on the program that gave up after one bad answer. Show the finished order loop as the mission, then the AI tease. No question yet.

- **Narration:** One wrong answer. The program prints a message, and then it ends. The customer has to start again.
  **On screen:** One wrong answer, and it gives up
- **Narration:** Welcome back to Code Quest. This is Chapter 7.
  **On screen:** Repeat Until Done: while Loops
- **Narration:** Today your programs learn to repeat. They keep going until the job is done.
  **On screen:** Repeat Until Done: while Loops Keep going until the job is done.
- **Narration:** And an AI assistant will promise three tries. Its loop will ask a fourth time.
  **On screen:** Repeat Until Done: while Loops Keep going until the job is done.
- **Narration:** And a real cafe takes items until the customer says: that is all. So here is today's mission. Asha's order loop asks for an item, again and again.
  **On screen:** Code `examples/ex06_order_loop.py`, line 4, 5 highlighted, output `examples/ex06_order_loop.expected`
- **Narration:** Coffee is not on the menu, so it says sorry, and asks again.
  **On screen:** Code `examples/ex06_order_loop.py`, line 14, 15 highlighted, output `examples/ex06_order_loop.expected`
- **Narration:** When the customer types done, the loop stops, and the program prints the items and the total.
  **On screen:** Code `examples/ex06_order_loop.py`, line 6, 7, 16, 17 highlighted, output `examples/ex06_order_loop.expected`
- **Narration:** One loop, any number of items. Let's build it.
  **On screen:** Code `examples/ex06_order_loop.py`, output `examples/ex06_order_loop.expected`

## Scene 2: Learning goals (0:45 to 1:02)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Write a while loop that repeats while a condition is True.
  **On screen:** By the end, you will be able to:
    - Write a `while` loop that repeats while its condition is `True`.
- **Narration:** Use a counter and a running total.
  **On screen:** By the end, you will be able to:
    - Write a `while` loop that repeats while its condition is `True`.
    - Use a counter and a running total that change on every pass.
- **Narration:** Ask a question again until the answer is valid.
  **On screen:** By the end, you will be able to:
    - Write a `while` loop that repeats while its condition is `True`.
    - Use a counter and a running total that change on every pass.
    - Ask a question again until the answer is valid.
- **Narration:** Stop a loop with a stop value, or with break.
  **On screen:** By the end, you will be able to:
    - Write a `while` loop that repeats while its condition is `True`.
    - Use a counter and a running total that change on every pass.
    - Ask a question again until the answer is valid.
    - Stop a loop with a stop value or with `break`.
- **Narration:** And trace a loop in a table, to see why it ends, or why it never does.
  **On screen:** By the end, you will be able to:
    - Write a `while` loop that repeats while its condition is `True`.
    - Use a counter and a running total that change on every pass.
    - Ask a question again until the answer is valid.
    - Stop a loop with a stop value or with `break`.
    - Trace a loop in a table and explain why it never ends.

## Scene 3: Why this matters (1:02 to 1:21)

**Section:** Why this matters

**Direction:** Connect loops to machines the learner uses.

- **Narration:** Real programs repeat. A cash machine asks for your PIN again. A shop's till scans items until the cashier presses Total. A game runs until you quit.
  **On screen:** Why this matters
    - A cash machine asks for your PIN again after a wrong try.
    - A shop's till scans items until the cashier presses Total.
    - A game keeps running until you quit.
- **Narration:** Each of these is a loop: a block of code that runs again and again, until a condition says stop.
  **On screen:** Why this matters
    - A cash machine asks for your PIN again after a wrong try.
    - A shop's till scans items until the cashier presses Total.
    - A game keeps running until you quit.

## Scene 4: The idea: check, run, go back (1:21 to 2:38)

**Section:** The idea

**Direction:** Teach the loop diagram, then the rule that something must change, then the waiter analogy. Then a quiz and a breather.

- **Narration:** A while loop checks a condition, the same way as if. If it is True, Python runs the indented block.
  **On screen:** while: check, run, go back
- **Narration:** But then, unlike if, Python goes back to the top and checks the condition again. One run of the block is called a pass.
  **On screen:** while: check, run, go back
- **Narration:** When the condition is False, Python skips the block, and continues after the loop.
  **On screen:** while: check, run, go back
- **Narration:** Here is the one rule of every loop. Something inside the block must change the value that the condition checks.
  **On screen:** The one rule of every loop
    - Something inside the block must change the value that the condition checks.
- **Narration:** If nothing changes, the condition stays True forever, and the loop never ends.
  **On screen:** The one rule of every loop
    - Something inside the block must change the value that the condition checks.
    - If nothing changes, the condition stays `True`, and the loop never ends.
- **Narration:** Think of a waiter who asks every table: anything else? Unlike a real waiter, Python never gets tired, and never notices that something is wrong.
  **On screen:** The one rule of every loop
    - Something inside the block must change the value that the condition checks.
    - If nothing changes, the condition stays `True`, and the loop never ends.
    - Like a waiter who asks every table "Anything else?", but never notices when to stop.
- **Narration:** Quick check. What must a line inside a while loop do, so that the loop can end?
  **On screen:** Quick check: "What must a line inside a `while` loop do, so that the loop can end?" (options shown)
- **Interaction:** "What must a line inside a `while` loop do, so that the loop can end?" stays on screen with a 10-second timer.
- **Narration:** C. Change a value that the condition checks. That is the only way the condition can become False.
  **On screen:** Quick check: "What must a line inside a `while` loop do, so that the loop can end?" (answer revealed: Change a value the condition checks)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - `while` checks, runs the block, and goes back.
    - One run of the block is a pass.
    - Something inside must change, or the loop never ends.
- **Narration:** Next, Asha serves her first tables, one pass at a time.
  **On screen:** Breather card
    - `while` checks, runs the block, and goes back.
    - One run of the block is a pass.
    - Something inside must change, or the loop never ends.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: A counter (2:38 to 3:28)

**Section:** Build it step by step

**Direction:** The file types in. Name the counter and the line that changes it, then ask how many tables are served.

- **Narration:** Step 1. Asha serves tables 1 to 3. Line 2 creates a counter, table, and sets it to 1. A counter is a variable that counts the passes.
  **On screen:** Code `examples/ex01_count.py`, lines 1 to 3 typed in, line 2 highlighted, output hidden
- **Narration:** Line 3 is the loop: while table is less than or equal to 3.
  **On screen:** Code `examples/ex01_count.py`, lines 1 to 3 typed in, line 3 highlighted, output hidden
- **Narration:** Line 4 prints the table number. Line 5 adds 1 to the counter. That is the line that changes the value the condition checks.
  **On screen:** Code `examples/ex01_count.py`, lines 1 to 5 typed in, line 4, 5 highlighted, output hidden
- **Narration:** Line 6 is not indented, so it is outside the loop.
  **On screen:** Code `examples/ex01_count.py`, lines 1 to 6 typed in, line 6 highlighted, output hidden
- **Interaction:** "How many times does line 4 print, and which line prints last?" stays on screen with a 10-second timer.
- **Narration:** Three times: tables 1, 2 and 3.
  **On screen:** Code `examples/ex01_count.py`, lines 1 to 6 typed in, line 4 highlighted, output `examples/ex01_count.expected`
- **Narration:** After the third pass, table is 4. 4 is not less than or equal to 3, so the loop ends, and line 6 prints once.
  **On screen:** Code `examples/ex01_count.py`, lines 1 to 6 typed in, line 3, 6 highlighted, output `examples/ex01_count.expected`

## Scene 6: Step 2: Ask again until valid (3:28 to 4:11)

**Section:** Build it step by step

**Direction:** This fixes the Chapter 6 problem. Teach the two input lines, ask how many messages, reveal.

- **Narration:** Step 2. This fixes the problem from Chapter 6. Line 2 asks once, before the loop, so people has a value when line 3 checks it.
  **On screen:** Code `examples/ex02_ask_again.py`, line 2 highlighted, output hidden
- **Narration:** Line 3: while people is less than 1. Line 4 explains the rule.
  **On screen:** Code `examples/ex02_ask_again.py`, line 3, 4 highlighted, output hidden
- **Narration:** And line 5 asks again, inside the loop. That new answer is the change that can end the loop.
  **On screen:** Code `examples/ex02_ask_again.py`, line 5 highlighted, output hidden
- **Interaction:** "The user types `0`, then `-2`, then `4`. How many times does `Please type 1 or more.` print?" stays on screen with a 10-second timer.
- **Narration:** Twice. Once for 0, and once for minus 2. Both are less than 1.
  **On screen:** Code `examples/ex02_ask_again.py`, line 4 highlighted, output `examples/ex02_ask_again.expected`
- **Narration:** Then 4 makes the condition False. The loop ends, and line 6 shows the table.
  **On screen:** Code `examples/ex02_ask_again.py`, line 6 highlighted, output `examples/ex02_ask_again.expected`

## Scene 7: Step 3: A running total (4:11 to 5:13)

**Section:** Build it step by step

**Direction:** Teach the running total, the stop value and plus equals. Ask whether the stop value is added, then reveal.

- **Narration:** Step 3. Asha adds up prices. Line 2 starts a running total at 0: a variable that grows on every pass. Line 3 starts a counter.
  **On screen:** Code `examples/ex03_running_total.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 asks for the first price, before the loop. The user types 0 to finish. A value that means stop is called a stop value. Line 5 loops while the price is not 0.
  **On screen:** Code `examples/ex03_running_total.py`, line 4, 5 highlighted, output hidden
- **Narration:** Line 6 says total plus equals price. That is short for: total equals total plus price. Line 7 adds 1 to the count, the same way. And minus equals takes away, in the same way.
  **On screen:** Code `examples/ex03_running_total.py`, line 6, 7 highlighted, output hidden
- **Narration:** And line 8 asks for the next price, as the last line of the pass.
  **On screen:** Code `examples/ex03_running_total.py`, line 8 highlighted, output hidden
- **Interaction:** "The user types `3.5`, `4`, `2.25`, then `0`. What are the items and the total?" stays on screen with a 10-second timer.
- **Narration:** Three items, and a total of 9.75.
  **On screen:** Code `examples/ex03_running_total.py`, line 9, 10 highlighted, output `examples/ex03_running_total.expected`
- **Narration:** The stop value is not added. Line 5 checks the 0 first, so line 6 never adds it.
  **On screen:** Code `examples/ex03_running_total.py`, line 5, 6 highlighted, output `examples/ex03_running_total.expected`

## Scene 8: Step 4: while True and break (5:13 to 6:31)

**Section:** Build it step by step

**Direction:** Teach while True and break, ask what Done does, reveal.

- **Narration:** Step 4. Line 2 says while True. That condition never becomes False on its own.
  **On screen:** Code `examples/ex04_break.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 asks for an item, and cleans it with strip and lower, as in Chapter 6.
  **On screen:** Code `examples/ex04_break.py`, line 3 highlighted, output hidden
- **Narration:** Lines 4 and 5: if the item is done, break. Break ends the loop immediately, and Python continues after it.
  **On screen:** Code `examples/ex04_break.py`, line 4, 5 highlighted, output hidden
- **Interaction:** "The user types `Done` with a capital D. Does line 6 run for that answer?" stays on screen with a 10-second timer.
- **Narration:** No. Strip and lower turn Done into done, so break runs first, and line 6 is skipped.
  **On screen:** Code `examples/ex04_break.py`, line 4, 5 highlighted, output `examples/ex04_break.expected`
- **Narration:** Then line 7 runs after the loop: order closed.
  **On screen:** Code `examples/ex04_break.py`, line 7 highlighted, output `examples/ex04_break.expected`
- **Narration:** Quick check. Cups starts at 1. While cups is less than 5, cups goes up by 2. What is cups after the loop?
  **On screen:** Quick check: "`cups = 1`, then `while cups < 5:` with `cups = cups + 2` inside. What is `cups` after the loop?" (options shown)
- **Interaction:** "`cups = 1`, then `while cups < 5:` with `cups = cups + 2` inside. What is `cups` after the loop?" stays on screen with a 10-second timer.
- **Narration:** A. 5. 1 becomes 3, then 5. 5 is not less than 5, so the loop ends.
  **On screen:** Quick check: "`cups = 1`, then `while cups < 5:` with `cups = cups + 2` inside. What is `cups` after the loop?" (answer revealed: `5`)
- **Narration:** Breather. Sit back, and take a slow breath.
  **On screen:** Breather card
    - Ask before the loop, and again inside it.
    - `total += price` adds to a running total.
    - `break` ends a loop immediately.
- **Narration:** Next, a tool that shows exactly what a loop does: the trace table.
  **On screen:** Breather card
    - Ask before the loop, and again inside it.
    - `total += price` adds to a running total.
    - `break` ends a loop immediately.
- **Breather:** 4 quiet seconds.

## Scene 9: Step 5: A trace table (6:31 to 7:35)

**Section:** Build it step by step

**Direction:** Teach the trace table on the doubling loop, row by row, then ask for the last number, then reveal.

- **Narration:** Step 5. Cups starts at 1. While cups is less than 20, line 4 doubles it, and line 5 prints it.
  **On screen:** Code `examples/ex05_trace.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** A trace table writes down the value of each variable on every pass. Let's fill one in.
  **On screen:** Code `examples/ex05_trace.py`, line 3 highlighted, output hidden
- **Narration:** Pass 1. Cups is 1. 1 is less than 20, so it doubles to 2.
  **On screen:** Table: Trace table: cups doubles (row 1 in focus)
- **Narration:** Pass 2: 2 becomes 4. Pass 3: 4 becomes 8.
  **On screen:** Table: Trace table: cups doubles (row 3 in focus)
- **Narration:** Pass 4: 8 becomes 16.
  **On screen:** Table: Trace table: cups doubles (row 4 in focus)
- **Narration:** Now cups is 16 at the check. Fill in the next row in your head.
  **On screen:** Table: Trace table: cups doubles (row 5 in focus)
- **Interaction:** "What is the last number that line 5 prints: 16 or 32?" stays on screen with a 10-second timer.
- **Narration:** 32. 16 is still less than 20, so pass 5 runs completely, and doubles it to 32.
  **On screen:** Table: Trace table: cups doubles (row 5 in focus)
- **Narration:** Only then does the check find False. Python checks the condition only at the top of each pass.
  **On screen:** Table: Trace table: cups doubles (row 6 in focus)
- **Narration:** And the real run agrees with the table: 2, 4, 8, 16, 32, then stopped at 32.
  **On screen:** Code `examples/ex05_trace.py`, line 4, 5 highlighted, output `examples/ex05_trace.expected`

## Scene 10: See the outcome: the order loop (7:35 to 8:33)

**Section:** See the outcome

**Direction:** Return to the mission. Explain every group of lines, ask for the items and total, reveal. Hand over to the AI story.

- **Narration:** Back to the mission. Lines 2 and 3 start a running total and a counter at 0.
  **On screen:** Code `examples/ex06_order_loop.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 starts the loop with while True. Lines 5 to 7 ask for an item, clean it, and break on done.
  **On screen:** Code `examples/ex06_order_loop.py`, line 4, 5, 6, 7 highlighted, output hidden
- **Narration:** Lines 8 to 13 are the decisions from Chapter 6. Tea adds 3.5, cake adds 4, and each adds 1 to the count.
  **On screen:** Code `examples/ex06_order_loop.py`, line 8, 9, 10, 11, 12, 13 highlighted, output hidden
- **Narration:** Lines 14 and 15 catch anything else. And lines 16 and 17 run once, after the loop.
  **On screen:** Code `examples/ex06_order_loop.py`, line 14, 15, 16, 17 highlighted, output hidden
- **Interaction:** "The user types tea, Cake, coffee, tea, done. What are the items and the total?" stays on screen with a 10-second timer.
- **Narration:** Coffee gets a sorry, and changes nothing.
  **On screen:** Code `examples/ex06_order_loop.py`, line 14, 15 highlighted, output `examples/ex06_order_loop.expected`
- **Narration:** Two teas and a cake: 3 items, and 3.5 plus 4 plus 3.5 is 11.00.
  **On screen:** Code `examples/ex06_order_loop.py`, line 16, 17 highlighted, output `examples/ex06_order_loop.expected`
- **Narration:** Mission complete! Next, Asha protects the How many teas question. She uses an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex06_order_loop.py`, output `examples/ex06_order_loop.expected`

## Scene 11: Work with AI: six stages, one limit (8:33 to 13:34)

**Section:** Work with AI

**Direction:** Teach the tracing skill. Then one conversation per stage, all about the teas question and a limit of 3 tries. Stage 3 plants the mistake, stages 4 and 5 catch it, stage 6 catches a second.

- **Narration:** This chapter's AI skill is tracing. You ask the AI to trace a loop for one set of answers, one line per pass.
  **On screen:** This chapter's AI skill: tracing
    - Ask AI to trace a loop for one set of answers, one line per pass.
    - A trace shows which value changes on each pass, and which never does.
- **Narration:** Then you run the same answers yourself. And the safety habits from Chapter 1 still apply.
  **On screen:** This chapter's AI skill: tracing
    - Ask AI to trace a loop for one set of answers, one line per pass.
    - A trace shows which value changes on each pass, and which never does.
    - Run the same answers yourself. Never paste private data.
- **Narration:** Stage 1: plan. The number of teas must be from 1 to 10. Asha asks for the loop condition, the value that must change, and test answers. No code yet.
  **On screen:** AI chat, stage 1: Plan: the condition and the test answers
    - You: I am a beginner learning while loops. The number of teas must be from 1 to 10. If it is not, my program asks again. Do not write code yet. Tell me the loop condition, which value must change inside the loop, and some test answers.
- **Narration:** The AI names the condition, says the new answer is what ends the loop, and lists test answers, including 1 and 10, the points where the result changes. These are called boundary values.
  **On screen:** AI chat, stage 1: Plan: the condition and the test answers
    - You: I am a beginner learning while loops. The number of teas must be from 1 to 10. If it is not, my program asks again. Do not write code yet. Tell me the loop condition, which value must change inside the loop, and some test answers.
    - AI (example answer): 1. Repeat while teas is less than 1 or more than 10. 2. Inside the loop, ask again and store the new answer in `teas`. That is the value that can end the loop. 3. Test answers: 3. Then 0, then 3. Then 12, then 3. And the boundary values 1 and 10.
- **Narration:** Stage 2: write. Asha writes the loop herself, and asks the AI to trace it for 0, 12 and 3. The AI traces two passes, then a check that is False.
  **On screen:** AI chat, stage 2: Write it yourself, then ask for a trace
    - You: I wrote the loop myself. Do not change it. Trace it for the answers 0, then 12, then 3: one line per pass. [code `examples/ai_teas_mine.py`]
    - AI (example answer): Pass 1: `teas` is 0. The condition is True: message, then the answer 12. Pass 2: `teas` is 12. True: message, then the answer 3. Check: `teas` is 3. False, so the loop ends and line 6 prints `Teas: 3`.
- **Narration:** Asha traced it too, and she runs it. All three agree.
  **On screen:** AI chat, stage 2: Write it yourself, then ask for a trace
    - You: I wrote the loop myself. Do not change it. Trace it for the answers 0, then 12, then 3: one line per pass. [code `examples/ai_teas_mine.py`]
    - AI (example answer): Pass 1: `teas` is 0. The condition is True: message, then the answer 12. Pass 2: `teas` is 12. True: message, then the answer 3. Check: `teas` is 3. False, so the loop ends and line 6 prints `Teas: 3`.
    - You: My trace said the same. I ran it:
- **Narration:** Stage 3: generate. Asha wants a limit: at most 3 tries, and then use 1 tea. She asks what 0, 0 and 0 print.
  **On screen:** AI chat, stage 3: Generate: add a limit of 3 tries
    - You: Add a limit to my loop: at most 3 tries. After 3 wrong answers, print 'Too many tries. Using 1 tea.' and use 1. If the answers are 0, 0 and 0, tell me exactly what it prints.
- **Narration:** The AI says: three questions, then too many tries. It gives no warning at all.
  **On screen:** AI chat, stage 3: Generate: add a limit of 3 tries
    - You: Add a limit to my loop: at most 3 tries. After 3 wrong answers, print 'Too many tries. Using 1 tea.' and use 1. If the answers are 0, 0 and 0, tell me exactly what it prints.
    - AI (example answer): Here is the code. With 0, 0 and 0 it asks 3 times, then prints `Too many tries. Using 1 tea.` and `Teas: 1`. [code `examples/ai_tries_flawed.py`]
- **Narration:** Look at the condition on line 4, and remember the one rule of every loop.
  **On screen:** AI chat, stage 3: Generate: add a limit of 3 tries
    - You: Add a limit to my loop: at most 3 tries. After 3 wrong answers, print 'Too many tries. Using 1 tea.' and use 1. If the answers are 0, 0 and 0, tell me exactly what it prints.
    - AI (example answer): Here is the code. With 0, 0 and 0 it asks 3 times, then prints `Too many tries. Using 1 tea.` and `Teas: 1`. [code `examples/ai_tries_flawed.py`]
- **Interaction:** "Line 4 checks `tries < 3`. Which line inside the loop changes `tries`?" stays on screen with a 10-second timer.
- **Narration:** None of them. Lines 5 and 6 print and ask, but tries stays 1. Asha suspects a bug. Now she proves it with tests.
  **On screen:** AI chat, stage 3: Generate: add a limit of 3 tries
    - You: Add a limit to my loop: at most 3 tries. After 3 wrong answers, print 'Too many tries. Using 1 tea.' and use 1. If the answers are 0, 0 and 0, tell me exactly what it prints.
    - AI (example answer): Here is the code. With 0, 0 and 0 it asks 3 times, then prints `Too many tries. Using 1 tea.` and `Teas: 1`. [code `examples/ai_tries_flawed.py`]
- **Narration:** Stage 4: test. Asha asks for edge cases: unusual answers that can break a rule. And the exact output each one should give.
  **On screen:** AI chat, stage 4: Test: run every edge case
    - You: Before I trust it, list the edge cases, with the exact output each one should give.
- **Narration:** The AI lists five. 1 and 10 are boundary values, the points where the result changes. The last case is three wrong answers: three questions, then 1 tea.
  **On screen:** AI chat, stage 4: Test: run every edge case
    - You: Before I trust it, list the edge cases, with the exact output each one should give.
    - AI (example answer): 1. `1`: Teas: 1. 2. `10`: Teas: 10. These are the boundary values. 3. `11`, then `5`: two questions, then Teas: 5. 4. `0`, `0`, then `5`: three questions, then Teas: 5. 5. `0`, `0`, `0`: three questions, then Too many tries. Using 1 tea.
- **Narration:** She runs every case on the AI's code. Here is case 4: three questions, then 5. It passes.
  **On screen:** AI chat, stage 4: Test: run every edge case
    - You: Before I trust it, list the edge cases, with the exact output each one should give.
    - AI (example answer): 1. `1`: Teas: 1. 2. `10`: Teas: 10. These are the boundary values. 3. `11`, then `5`: two questions, then Teas: 5. 4. `0`, `0`, then `5`: three questions, then Teas: 5. 5. `0`, `0`, `0`: three questions, then Too many tries. Using 1 tea.
    - You: I ran case 4 on your code. It passes:
- **Narration:** Cases 1 to 4 pass. 1 and 10 are accepted, and wrong answers are asked again.
  **On screen:** Table: Asha runs every case on the AI's code (row 3 in focus)
- **Narration:** But case 5 fails. Three wrong answers should end in too many tries. The program asks a fourth time.
  **On screen:** Table: Asha runs every case on the AI's code (row 5 in focus)
- **Narration:** Here is case 5. She types 0 three times. The program does not stop. It asks a fourth time.
  **On screen:** Code `examples/ai_tries_flawed.py`, line 4 highlighted, output `examples/ai_tries_flawed.expected`
- **Narration:** She types 5, and it takes it. The limit never worked. With more zeros, it would ask forever.
  **On screen:** Code `examples/ai_tries_flawed.py`, line 4 highlighted, output `examples/ai_tries_flawed.expected`
- **Narration:** Stage 5: debug. Asha pastes the loop and the failed run. She asks for a trace table first, then the value that never changes, then the fix.
  **On screen:** AI chat, stage 5: Debug: a trace before a fix
    - You: Case 5 failed: it asked a fourth time, and took my 5. First trace the loop for 0, 0, 0 in a table, one line per pass. Then tell me which value never changes, and the smallest fix. [code `examples/ai_tries_flawed.py`]
- **Narration:** The trace shows it clearly. Tries is 1 on every pass. Nothing inside the loop changes it, so tries less than 3 is always True. The fix: tries plus equals 1, inside the loop.
  **On screen:** AI chat, stage 5: Debug: a trace before a fix
    - You: Case 5 failed: it asked a fourth time, and took my 5. First trace the loop for 0, 0, 0 in a table, one line per pass. Then tell me which value never changes, and the smallest fix. [code `examples/ai_tries_flawed.py`]
    - AI (example answer): Pass 1: `teas` 0, `tries` 1. True. Pass 2: `teas` 0, `tries` 1. True. Pass 3: `teas` 0, `tries` 1. True. `tries` is 1 on every pass. No line inside the loop changes it, so `tries < 3` is always True. Fix: add `tries += 1` as the last line inside the loop.
- **Narration:** Asha writes the trace as a table, like step 5. Three passes, and tries is 1 every time.
  **On screen:** Table: Asha checks the AI's trace (row 3 in focus)
- **Narration:** That matches her run: one first question, plus three passes, is four questions. The trace and the run agree.
  **On screen:** Table: Asha checks the AI's trace (row 4 in focus)
- **Narration:** Here is the fix on line 7. Now tries goes 1, 2, 3, and the third wrong answer ends the loop.
  **On screen:** Code `examples/ai_tries_fixed.py`, line 7 highlighted, output `examples/ai_tries_fixed.expected`
- **Narration:** Too many tries, using 1 tea. Exactly what the AI promised in the first place.
  **On screen:** Code `examples/ai_tries_fixed.py`, line 7 highlighted, output `examples/ai_tries_fixed.expected`
- **Narration:** A fix can break something else. So Asha runs every case again, on the fixed code.
  **On screen:** Table: All cases again, on the fixed code
- **Narration:** All five pass. Now she trusts it.
  **On screen:** Table: All cases again, on the fixed code (row 5 in focus)
- **Narration:** Stage 6: improve. Asha asks for at most two readability improvements that do not change how many times it asks.
  **On screen:** AI chat, stage 6: Improve: count the questions
    - You: Suggest at most two readability improvements, each with one reason. Do not change how many times it asks. [code `examples/ai_tries_fixed.py`]
- **Narration:** Suggestion 1, a comment, helps a reader. Suggestion 2 says: change less than 3 to less than or equal to 3, for three full tries.
  **On screen:** AI chat, stage 6: Improve: count the questions
    - You: Suggest at most two readability improvements, each with one reason. Do not change how many times it asks. [code `examples/ai_tries_fixed.py`]
    - AI (example answer): 1. Add a comment above the loop: `# Ask at most 3 times`. 2. Change `tries < 3` to `tries <= 3`, so the customer gets three full tries.
- **Narration:** Asha does not accept it yet. She will count the questions.
  **On screen:** AI chat, stage 6: Improve: count the questions
    - You: Suggest at most two readability improvements, each with one reason. Do not change how many times it asks. [code `examples/ai_tries_fixed.py`]
    - AI (example answer): 1. Add a comment above the loop: `# Ask at most 3 times`. 2. Change `tries < 3` to `tries <= 3`, so the customer gets three full tries.
    - You: Suggestion 2 changes a condition. Before I accept it, I will count the questions it asks.
- **Narration:** Here is the suggested condition on line 4: tries less than or equal to 3. Trace it in your head. Tries is 1, then 2, then 3.
  **On screen:** Code `examples/ai_tries_improve.py`, line 4, 7 highlighted, output hidden
- **Interaction:** "With `tries <= 3`, how many times does it ask before `Too many tries`?" stays on screen with a 10-second timer.
- **Narration:** Four times. When tries is 3, the condition is still True, so there is one more pass.
  **On screen:** Code `examples/ai_tries_improve.py`, line 4, 7 highlighted, output `examples/ai_tries_improve.expected`
- **Narration:** And Asha had said: do not change how many times it asks. The AI ignored that. She keeps less than 3, and adds only the comment.
  **On screen:** Code `examples/ai_tries_improve.py`, line 4, 7 highlighted, output `examples/ai_tries_improve.expected`
- **Narration:** Quick check. A loop never ends. What do you ask the AI for first?
  **On screen:** Quick check: "A loop never ends. What do you ask the AI for first?" (options shown)
- **Interaction:** "A loop never ends. What do you ask the AI for first?" stays on screen with a 10-second timer.
- **Narration:** B. A trace table of each pass. It shows which value never changes.
  **On screen:** Quick check: "A loop never ends. What do you ask the AI for first?" (answer revealed: A trace table of each pass)
- **Narration:** Breather. Asha caught two AI mistakes, with a trace, and by counting.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Every value in the condition needs a line that changes it.
    - Count the questions: `<` and `<=` differ by one pass.
- **Narration:** Next, the four mistakes beginners make most with loops. You have already seen one of them.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Every value in the condition needs a line that changes it.
    - Count the questions: `<` and `<=` differ by one pass.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes (13:34 to 15:26)

**Section:** Common mistakes

**Direction:** Mistake 1 is a real error. Mistake 2 is a spot-it question about the counter. Mistake 3 shows the never-ending loop as a fragment and how to stop it. Mistake 4 is a spot-it on capital letters.

- **Narration:** Mistake 1. The condition on line 2 is checked before the first pass. But answer does not exist yet.
  **On screen:** Code `examples/err01_not_created.py`, line 2 highlighted, error `examples/err01_not_created.expected_error`
- **Narration:** Python stops with a Name Error. The fix: ask once before the loop, as in step 2, or use while True with break, as in step 4.
  **On screen:** Code `examples/err01_not_created.py`, line 2 highlighted, error `examples/err01_not_created.expected_error`
- **Narration:** Now you try. Asha wants to serve tables 1 to 3. Compare line 3 with step 1.
  **On screen:** Code `examples/ex07_off_by_one.py`, line 3 highlighted, output hidden
- **Interaction:** "Asha wants tables 1 to 3. Which table is never served, and why?" stays on screen with a 10-second timer.
- **Narration:** Table 3. Less than 3 is False when table is 3, so the loop stops one pass too early.
  **On screen:** Code `examples/ex07_off_by_one.py`, line 3 highlighted, output `examples/ex07_off_by_one.expected`
- **Narration:** No error, only a missing table. This is called an off-by-one error. The fix: less than or equal to 3.
  **On screen:** Code `examples/ex07_off_by_one.py`, line 3 highlighted, output `examples/ex07_off_by_one.expected`
- **Narration:** Mistake 3 is the one the AI made. Nothing inside this loop changes table, so it prints table 1 again and again, forever.
  **On screen:** Mistake 3: a loop that never ends
- **Narration:** If a program never stops, click in the terminal and press Control and C together. Python stops with a Keyboard Interrupt message.
  **On screen:** Mistake 3: a loop that never ends
- **Narration:** The fix: add the line that changes the counter, inside the loop.
  **On screen:** Mistake 3: a loop that never ends
- **Narration:** One more. The loop stops on done, in small letters. The user types Done, with a capital D.
  **On screen:** Code `examples/ex08_done_case.py`, line 3 highlighted, output hidden
- **Interaction:** "The user types `Done` with a capital D. What happens?" stays on screen with a 10-second timer.
- **Narration:** Done is added to the order as if it were an item. The loop keeps going until done in small letters.
  **On screen:** Code `examples/ex08_done_case.py`, line 3 highlighted, output `examples/ex08_done_case.expected`
- **Narration:** The fix is the one from step 4: compare the answer after strip and lower.
  **On screen:** Code `examples/ex08_done_case.py`, line 3 highlighted, output `examples/ex08_done_case.expected`
- **Narration:** Last breather. Now you know the four most common loop mistakes.
  **On screen:** Breather card
    - Give every name a value before the loop.
    - Check the last pass: `<` or `<=`?
    - Ctrl+C stops a loop that never ends.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - Give every name a value before the loop.
    - Check the last pass: `<` or `<=`?
    - Ctrl+C stops a loop that never ends.
- **Breather:** 4 quiet seconds.

## Scene 13: Think beyond (15:26 to 16:13)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. The cafe kettle needs 5 minutes. How would you count down from 5 to 1, and then print: tea is ready?
  **On screen:** Question card: "The kettle needs 5 minutes. How do you count down from 5 to 1, then print `Tea is ready!`?"
- **Interaction:** "The kettle needs 5 minutes. How do you count down from 5 to 1, then print `Tea is ready!`?" stays on screen with a 10-second timer.
- **Narration:** Think about the value that changes on each pass, and its direction. Minus equals takes away.
  **On screen:** Question card: "The kettle needs 5 minutes. How do you count down from 5 to 1, then print `Tea is ready!`?"
- **Narration:** Second. How could Asha's order loop stop after 10 items, even if the customer never types done?
  **On screen:** Question card: "How could the order loop stop after 10 items, even if nobody types `done`?"
- **Interaction:** "How could the order loop stop after 10 items, even if nobody types `done`?" stays on screen with a 10-second timer.
- **Narration:** Trace your loop with 10 items before you run it.
  **On screen:** Question card: "How could the order loop stop after 10 items, even if nobody types `done`?"

## Scene 14: Recap (16:13 to 17:13)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check on something new, then the badge.

- **Narration:** Let's recap.
  **On screen:** Recap
- **Narration:** A while loop repeats its block while the condition is True.
  **On screen:** Recap
    - A `while` loop repeats its block while the condition is `True`.
- **Narration:** A line inside the loop must change the value that the condition checks.
  **On screen:** Recap
    - A `while` loop repeats its block while the condition is `True`.
    - A line inside the loop must change the value the condition checks.
- **Narration:** A counter counts passes, and a running total grows. Plus equals and minus equals are short forms.
  **On screen:** Recap
    - A `while` loop repeats its block while the condition is `True`.
    - A line inside the loop must change the value the condition checks.
    - A counter counts passes; a running total grows. `+=` and `-=` are short forms.
- **Narration:** A stop value or break ends the loop. And a trace table shows every value on every pass.
  **On screen:** Recap
    - A `while` loop repeats its block while the condition is `True`.
    - A line inside the loop must change the value the condition checks.
    - A counter counts passes; a running total grows. `+=` and `-=` are short forms.
    - A stop value or `break` ends the loop when the user is finished.
    - A trace table shows every value on every pass.
- **Narration:** And with AI: ask for a trace, then run the same answers yourself.
  **On screen:** Recap
    - A `while` loop repeats its block while the condition is `True`.
    - A line inside the loop must change the value the condition checks.
    - A counter counts passes; a running total grows. `+=` and `-=` are short forms.
    - A stop value or `break` ends the loop when the user is finished.
    - A trace table shows every value on every pass.
    - Ask AI to trace a loop, then run the same answers yourself.
- **Narration:** One last check. N starts at 10. While n is greater than 0, the loop prints n, then takes away 3. How many numbers print?
  **On screen:** Quick check: "`n = 10`, then `while n > 0:` with `print(n)` and `n -= 3` inside. How many numbers print?" (options shown)
- **Interaction:** "`n = 10`, then `while n > 0:` with `print(n)` and `n -= 3` inside. How many numbers print?" stays on screen with a 10-second timer.
- **Narration:** D. Four: 10, 7, 4 and 1. Then n is minus 2, and the loop ends.
  **On screen:** Quick check: "`n = 10`, then `while n > 0:` with `print(n)` and `n -= 3` inside. How many numbers print?" (answer revealed: 4)
- **Narration:** Mission complete! You earned 100 XP and the Loop Tamer badge.
  **On screen:** Loop Tamer You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice (17:13 to 17:38)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. The practice file has eight tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including a savings goal.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, an AI's kettle timer never ends. Trace it, and fix it.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Trace each loop before you run it. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 16: What's next (17:38 to 18:05)

**Section:** What's next

**Direction:** End card. Tease for and range as the fix for counter mistakes. Hold quietly at the end.

- **Narration:** To serve tables 1 to 3, Asha needed a counter, a condition and a line that changes it. Three places to make a mistake, as you saw today.
  **On screen:** Repeat a Set Number of Times: for Loops and range() Repeat a known number of times, in one line.
- **Narration:** In Chapter 8, for loops and range repeat a block a set number of times, with no counter of your own. And a for loop can go through every letter of a word.
  **On screen:** Repeat a Set Number of Times: for Loops and range() Repeat a known number of times, in one line.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Repeat a Set Number of Times: for Loops and range() Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 8.
  **On screen:** Repeat a Set Number of Times: for Loops and range() Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
