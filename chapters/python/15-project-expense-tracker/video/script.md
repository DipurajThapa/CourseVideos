# Video Script: Chapter 15: Boss Level 3: The Expense Tracker

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:14.

## Scene 1: Introduction (0:00 to 0:52)

**Section:** Introduction

**Direction:** Open on Asha's scraps of paper and one question a learner can work out. Then the boss level title and the AI tease.

- **Narration:** It is closing time at the Corner Cafe. Today, Asha wrote every expense on a scrap of paper. Milk, coffee beans, paper cups.
  **On screen:** Where did the money go?
- **Narration:** Look closely. Milk appears twice.
  **On screen:** Where did the money go?
- **Interaction:** "Which category cost the most today?" stays on screen with a 10-second timer.
- **Narration:** Beans, 30. Milk was bought twice, 12.50 and 8, so 20.50. Easy on four scraps of paper. Not on forty!
  **On screen:** Where did the money go?
- **Narration:** Welcome to Chapter 15, the third boss level!
  **On screen:** The Expense Tracker
- **Narration:** You will combine lists, dictionaries, sets and tuples into one tool that answers that question for any day.
  **On screen:** The Expense Tracker Record. Total. Find the biggest.
- **Narration:** And an AI assistant will sound completely sure at every stage. Your tests will decide who is right.
  **On screen:** The Expense Tracker Record. Total. Find the biggest.

## Scene 2: The mission (0:52 to 1:34)

**Section:** The mission

**Direction:** The tracker's job, then the table of what each chapter contributes, row by row.

- **Narration:** Here is the mission. Asha types each expense: a category, then an amount.
  **On screen:** The expense tracker
    - Asha types each expense: a category and an amount.
- **Narration:** When the cafe closes, she types done.
  **On screen:** The expense tracker
    - Asha types each expense: a category and an amount.
    - She types `done` when the cafe closes.
- **Narration:** The tracker then prints a total for each category, the total for the day, and the biggest category.
  **On screen:** The expense tracker
    - Asha types each expense: a category and an amount.
    - She types `done` when the cafe closes.
    - The tracker prints a total for each category, the day's total and the biggest category.
- **Narration:** And, like the biscuit jar game, no answer may crash it.
  **On screen:** The expense tracker
    - Asha types each expense: a category and an amount.
    - She types `done` when the cafe closes.
    - The tracker prints a total for each category, the day's total and the biggest category.
    - No answer may crash it.
- **Narration:** You know almost every piece. A while loop from Chapter 7.
  **On screen:** Table: Everything you need (row 1 in focus)
- **Narration:** A list from Chapter 11.
  **On screen:** Table: Everything you need (row 2 in focus)
- **Narration:** A dictionary from Chapter 12.
  **On screen:** Table: Everything you need (row 3 in focus)
- **Narration:** Sets and tuples from Chapter 13.
  **On screen:** Table: Everything you need (row 4 in focus)
- **Narration:** And a habit from Chapter 14: run the old and the new version on the same test cases.
  **On screen:** Table: Everything you need (row 5 in focus)
- **Narration:** Plus one small new tool: the replace method with a third value, to check an amount such as 12.50.
  **On screen:** Table: Everything you need (row 6 in focus)

## Scene 3: What you will build (1:34 to 1:58)

**Section:** What you will build

**Direction:** Show one finished day as the destination, line by line in the output.

- **Narration:** Here is where we are going. On the right, Asha types four expenses, the same four as on her scraps of paper.
  **On screen:** Code `project/expense_tracker.py`, output `project/expense_tracker.expected`
- **Narration:** She types done. The tracker prints one row for each category, in alphabetical order.
  **On screen:** Code `project/expense_tracker.py`, output `project/expense_tracker.expected`
- **Narration:** Then the number of expenses, the total for the day, and the biggest category: beans.
  **On screen:** Code `project/expense_tracker.py`, output `project/expense_tracker.expected`
- **Narration:** About twenty-five lines of code. By the end of this video, you will understand every one.
  **On screen:** Code `project/expense_tracker.py`, output `project/expense_tracker.expected`

## Scene 4: Acceptance criteria (1:58 to 3:06)

**Section:** Acceptance criteria

**Direction:** Six criteria, revealed in groups. A quiz on criterion five, then a breather.

- **Narration:** Asha writes down what done means first.
  **On screen:** Done means all six are true
- **Narration:** One and two. It asks until done, and it accepts only four categories: milk, beans, cups and repairs.
  **On screen:** Done means all six are true
    - Asks for a category and an amount until `done`.
    - Accepts only milk, beans, cups and repairs.
- **Narration:** Three. It accepts amounts such as 30 or 12.50. A comma, a word or a minus sign gets a message, not a crash.
  **On screen:** Done means all six are true
    - Asks for a category and an amount until `done`.
    - Accepts only milk, beans, cups and repairs.
    - Accepts `30` or `12.50`, and gives a message for `12,50`, a word or a minus sign.
- **Narration:** Four and five. A total for each category, the day's total, and the biggest category. An empty day prints: Biggest, none.
  **On screen:** Done means all six are true
    - Asks for a category and an amount until `done`.
    - Accepts only milk, beans, cups and repairs.
    - Accepts `30` or `12.50`, and gives a message for `12,50`, a word or a minus sign.
    - Prints a total for each category, in alphabetical order.
    - Prints the count, the day's total and the biggest category. An empty day prints `Biggest: none`.
- **Narration:** And six. It passes at least five test days with known results.
  **On screen:** Done means all six are true
    - Asks for a category and an amount until `done`.
    - Accepts only milk, beans, cups and repairs.
    - Accepts `30` or `12.50`, and gives a message for `12,50`, a word or a minus sign.
    - Prints a total for each category, in alphabetical order.
    - Prints the count, the day's total and the biggest category. An empty day prints `Biggest: none`.
    - Passes at least five test days with known results.
- **Narration:** Quick check, using criterion five. Which test day must print: Biggest, none?
  **On screen:** Quick check: "Which test day must print `Biggest: none`?" (options shown)
- **Interaction:** "Which test day must print `Biggest: none`?" stays on screen with a 10-second timer.
- **Narration:** A. A day with no expenses. There is no biggest category, and the tracker must not crash. Remember this day. It will matter.
  **On screen:** Quick check: "Which test day must print `Biggest: none`?" (answer revealed: A day with no expenses)
- **Narration:** Take a breather. You know the tool, and what done means.
  **On screen:** Breather card
    - One tool: record, total, find the biggest.
    - Four categories, checked amounts.
    - Six criteria say when it is done.
- **Narration:** Next, Asha asks an AI assistant how to store the data.
  **On screen:** Breather card
    - One tool: record, total, find the biggest.
    - Four categories, checked amounts.
    - Six criteria say when it is done.
- **Breather:** 4 quiet seconds.

## Scene 5: Plan it with AI (3:06 to 4:20)

**Section:** Plan it with AI

**Direction:** Stage 1: the AI suggests a dictionary model. Ask whether it keeps both milks, then the test, then Asha's model.

- **Narration:** In this project, all six AI stages help build one tracker, piece by piece. Stage 1: plan. Asha asks the AI how to store the expenses. No code yet.
  **On screen:** AI chat, stage 1: Plan: review the data model
    - You: I am a beginner. I know lists, dictionaries, tuples and sets. I want to record the cafe's expenses: a category and an amount for each one. Do not write the program. Suggest how to store the expenses, and give one reason.
- **Narration:** The AI suggests a dictionary: the category is the key, and the amount is the value. It sounds tidy.
  **On screen:** AI chat, stage 1: Plan: review the data model
    - You: I am a beginner. I know lists, dictionaries, tuples and sets. I want to record the cafe's expenses: a category and an amount for each one. Do not write the program. Suggest how to store the expenses, and give one reason.
    - AI (example answer): Store them in a dictionary. The category is the key and the amount is the value, for example `expenses["milk"] = 12.50`. Then the totals are already there.
- **Narration:** Now remember Asha's scraps of paper. Milk appears twice. And remember a rule from Chapter 12 about keys.
  **On screen:** AI chat, stage 1: Plan: review the data model
    - You: I am a beginner. I know lists, dictionaries, tuples and sets. I want to record the cafe's expenses: a category and an amount for each one. Do not write the program. Suggest how to store the expenses, and give one reason.
    - AI (example answer): Store them in a dictionary. The category is the key and the amount is the value, for example `expenses["milk"] = 12.50`. Then the totals are already there.
- **Interaction:** "Will this model keep both milk expenses, 12.50 and 8?" stays on screen with a 10-second timer.
- **Narration:** No. Keys in a dictionary are unique. Asha tests it anyway.
  **On screen:** AI chat, stage 1: Plan: review the data model
    - You: I am a beginner. I know lists, dictionaries, tuples and sets. I want to record the cafe's expenses: a category and an amount for each one. Do not write the program. Suggest how to store the expenses, and give one reason.
    - AI (example answer): Store them in a dictionary. The category is the key and the amount is the value, for example `expenses["milk"] = 12.50`. Then the totals are already there.
- **Narration:** Lines 3 to 5 store milk, then beans, then milk again.
  **On screen:** Code `examples/ai_plan_overwrite.py`, line 3, 4, 5 highlighted, output `examples/ai_plan_overwrite.expected`
- **Narration:** The second milk replaced the first one. 12.50 has disappeared!
  **On screen:** Code `examples/ai_plan_overwrite.py`, line 5 highlighted, output `examples/ai_plan_overwrite.expected`
- **Narration:** This is the AI skill of this chapter: let AI suggest a data model, then test it against your real data.
  **On screen:** Code `examples/ai_plan_overwrite.py`, output `examples/ai_plan_overwrite.expected`
- **Narration:** So Asha chooses a different model. A list of tuples: one tuple for each expense.
  **On screen:** Asha's data model
    - A **list of tuples**: one tuple for each expense, such as `("milk", 12.5)`.
- **Narration:** Nothing is ever lost. Two milks are two tuples.
  **On screen:** Asha's data model
    - A **list of tuples**: one tuple for each expense, such as `("milk", 12.5)`.
    - Nothing is ever lost: two milks are two tuples.
- **Narration:** And at the end, the program builds a dictionary of totals from the list.
  **On screen:** Asha's data model
    - A **list of tuples**: one tuple for each expense, such as `("milk", 12.5)`.
    - Nothing is ever lost: two milks are two tuples.
    - A **dictionary of totals** is built from the list at the end.

## Scene 6: Step 1: A list of tuples (4:20 to 5:04)

**Section:** Build it step by step

**Direction:** Teach append with a tuple and unpacking, then ask about line 8.

- **Narration:** Time to build. Step 1. Line 2 starts an empty list.
  **On screen:** Code `examples/ex01_record.py`, line 2 highlighted, output hidden
- **Narration:** Lines 3 and 4 append one tuple each. Append takes one value, so each tuple has its own brackets.
  **On screen:** Code `examples/ex01_record.py`, line 3, 4 highlighted, output hidden
- **Narration:** Line 5 prints the list, and line 6 counts the expenses.
  **On screen:** Code `examples/ex01_record.py`, line 5, 6 highlighted, output hidden
- **Narration:** Line 7 unpacks the first tuple into two variables, as in Chapter 13. Index 0 is the first expense.
  **On screen:** Code `examples/ex01_record.py`, line 7 highlighted, output hidden
- **Interaction:** "What does line 8 print?" stays on screen with a 10-second timer.
- **Narration:** Milk, 12.5. The first tuple gives category milk and amount 12.5.
  **On screen:** Code `examples/ex01_record.py`, line 7, 8 highlighted, output `examples/ex01_record.expected`
- **Narration:** And line 6 says 2 expenses.
  **On screen:** Code `examples/ex01_record.py`, line 6 highlighted, output `examples/ex01_record.expected`

## Scene 7: Step 2: Ask until done (5:04 to 6:01)

**Section:** Build it step by step

**Direction:** Teach the loop and the set check, then stage 2: the AI predicts the messages, and the run confirms.

- **Narration:** Step 2. Line 2 keeps the four allowed categories in a set.
  **On screen:** Code `examples/ex02_categories.py`, line 2 highlighted, output hidden
- **Narration:** Line 4 starts a loop that runs until break. Line 5 asks for a category, and calls two methods in a row. Strip removes the spaces, and lower makes small letters.
  **On screen:** Code `examples/ex02_categories.py`, line 4, 5 highlighted, output hidden
- **Narration:** Lines 6 and 7: done stops the loop.
  **On screen:** Code `examples/ex02_categories.py`, line 6, 7 highlighted, output hidden
- **Narration:** Lines 8 and 9: any answer that is not in the set gets a message.
  **On screen:** Code `examples/ex02_categories.py`, line 8, 9 highlighted, output hidden
- **Narration:** Otherwise, lines 11 and 12 count it and confirm it.
  **On screen:** Code `examples/ex02_categories.py`, line 10, 11, 12 highlighted, output hidden
- **Narration:** Stage 2: write. Asha wrote this loop herself. Before she runs it, she asks the AI what it prints for three answers. Make your own prediction too.
  **On screen:** AI chat, stage 2: Write it yourself, then check the messages
    - You: I wrote this loop myself. Do not change it. What does it print for these answers: Milk with a space before it, then tea, then done? [code `examples/ex02_categories.py`]
- **Interaction:** "Asha types Milk with a space before it. Does the set accept it?" stays on screen with a 10-second timer.
- **Narration:** Yes. The AI agrees: strip and lower turn it into milk, which is in the set. Tea gets the message, and done stops the loop.
  **On screen:** AI chat, stage 2: Write it yourself, then check the messages
    - You: I wrote this loop myself. Do not change it. What does it print for these answers: Milk with a space before it, then tea, then done? [code `examples/ex02_categories.py`]
    - AI (example answer): `strip()` and `lower()` turn it into milk, which is in the set, so it prints `OK: milk`. Tea is not in the set, so it prints the message. Done stops the loop, and the count is 1.

## Scene 8: Step 2: The real run (6:01 to 6:14)

**Section:** Build it step by step

**Direction:** The real run confirms the AI's prediction, line by line.

- **Narration:** Asha runs it. Milk with a space is accepted: OK, milk.
  **On screen:** Code `examples/ex02_categories.py`, line 12 highlighted, output `examples/ex02_categories.expected`
- **Narration:** Tea gets the message.
  **On screen:** Code `examples/ex02_categories.py`, line 9 highlighted, output `examples/ex02_categories.expected`
- **Narration:** And done stops the loop, with one category entered. The AI's prediction matches the real run.
  **On screen:** Code `examples/ex02_categories.py`, line 13 highlighted, output `examples/ex02_categories.expected`

## Scene 9: Step 3: Check an amount (6:14 to 7:57)

**Section:** Build it step by step

**Direction:** Teach why isdigit fails for 12.50, the third value of replace, then ask which texts pass. A quiz, then a breather.

- **Narration:** Step 3: the amount. In Chapter 10, is digit checked a whole number. But 12.50 has a decimal point, and is digit says False for it.
  **On screen:** Code `examples/ex03_amount_check.py`, line 2 highlighted, output hidden
- **Narration:** The fix: remove one decimal point first, then check. Replace takes an optional third value: how many changes to make. Line 2 removes one point, so 12.50 becomes 1250.
  **On screen:** Code `examples/ex03_amount_check.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 removes only the first point of 1.2.3, so it becomes 12.3. That still has a point.
  **On screen:** Code `examples/ex03_amount_check.py`, line 3 highlighted, output hidden
- **Narration:** Line 4 loops over six texts, and line 5 prints each one with the result of the check.
  **On screen:** Code `examples/ex03_amount_check.py`, line 4, 5 highlighted, output hidden
- **Interaction:** "Which of the six texts on line 4 print `True`?" stays on screen with a 10-second timer.
- **Narration:** Only two: 12.50 and 30. A comma, a word, a second point and a minus sign all fail.
  **On screen:** Code `examples/ex03_amount_check.py`, line 4, 5 highlighted, output `examples/ex03_amount_check.expected`
- **Narration:** Only text with at most one point and nothing but digits passes. Then float is safe.
  **On screen:** Code `examples/ex03_amount_check.py`, line 4, 5 highlighted, output `examples/ex03_amount_check.expected`
- **Narration:** Quick check, with four new answers. Which one passes the amount check?
  **On screen:** Quick check: "Which answer passes the amount check?" (options shown)
- **Interaction:** "Which answer passes the amount check?" stays on screen with a 10-second timer.
- **Narration:** C, 0.75. Without its one point, it is 0 7 5: all digits. And 1, dot, dot, 5 keeps a second point, so it fails.
  **On screen:** Quick check: "Which answer passes the amount check?" (answer revealed: `0.75`)
- **Narration:** Breather. Relax your hands. The tracker can now collect clean expenses.
  **On screen:** Breather card
    - Each expense is a tuple in a list.
    - A set rejects unknown categories.
    - Check an amount, then convert it.
- **Narration:** Next, the totals.
  **On screen:** Breather card
    - Each expense is a tuple in a list.
    - A set rejects unknown categories.
    - Check an amount, then convert it.
- **Breather:** 4 quiet seconds.

## Scene 10: Step 4: Add up each category (7:57 to 8:40)

**Section:** Build it step by step

**Direction:** Teach get with a default, walk the milk twice, ask the milk total, reveal.

- **Narration:** Step 4. Line 2 is the list of tuples, with milk twice. Line 3 starts an empty dictionary of totals.
  **On screen:** Code `examples/ex04_totals.py`, line 2 highlighted, output hidden
- **Narration:** Line 4 unpacks each tuple into category and amount.
  **On screen:** Code `examples/ex04_totals.py`, line 4 highlighted, output hidden
- **Narration:** Line 5 is the key line. Get gives the total so far, or 0 for a category with no total yet. Then it adds the amount.
  **On screen:** Code `examples/ex04_totals.py`, line 5 highlighted, output hidden
- **Interaction:** "What total does line 6 show for milk?" stays on screen with a 10-second timer.
- **Narration:** 20.5. The first milk found no total, so get gave 0, and the total became 12.5. The second milk added 8.
  **On screen:** Code `examples/ex04_totals.py`, line 5, 6 highlighted, output `examples/ex04_totals.expected`

## Scene 11: Step 5: Print the table (8:40 to 9:05)

**Section:** Build it step by step

**Direction:** Teach sorted keys and the format codes, then show the table.

- **Narration:** Step 5 prints the table. Line 4 loops over sorted totals: the keys in alphabetical order.
  **On screen:** Code `examples/ex05_table.py`, line 4 highlighted, output `examples/ex05_table.expected`
- **Narration:** Line 5 is Chapter 3 formatting. Less than 8 fills the name to 8 characters. Greater than 7 point 2 f puts the amount on the right, with two decimal places.
  **On screen:** Code `examples/ex05_table.py`, line 5 highlighted, output `examples/ex05_table.expected`
- **Narration:** Line 6 prints the count of expenses, and the sum of the values: 56.75.
  **On screen:** Code `examples/ex05_table.py`, line 6 highlighted, output `examples/ex05_table.expected`

## Scene 12: Step 6: The biggest category (9:05 to 12:33)

**Section:** Build it step by step

**Direction:** Stage 3 plants the AI mistake. The learner judges it, the test reveals milk. Stage 4: the AI lists test days but forgets the empty day. The runs, the empty-day error, the table, stage 5 debug, a re-run of every day. Quiz, breather.

- **Narration:** Step 6: the biggest category. Stage 3: generate. Asha asks the AI for one line, and asks what it gives.
  **On screen:** AI chat, stage 3: Generate: one line for the biggest
    - You: My dictionary totals holds a total for each category. Write one line that finds the category with the biggest total. Tell me what it gives.
- **Narration:** The AI writes biggest equals max of totals. It says this gives the category that cost the most. In Chapter 11, max found the largest number in a list, so it looks right.
  **On screen:** AI chat, stage 3: Generate: one line for the biggest
    - You: My dictionary totals holds a total for each category. Write one line that finds the category with the biggest total. Tell me what it gives.
    - AI (example answer): Here is the line: `biggest = max(totals)` It gives the category that cost the most.
- **Narration:** But remember what a loop over a dictionary gives you, from Chapter 12.
  **On screen:** AI chat, stage 3: Generate: one line for the biggest
    - You: My dictionary totals holds a total for each category. Write one line that finds the category with the biggest total. Tell me what it gives.
    - AI (example answer): Here is the line: `biggest = max(totals)` It gives the category that cost the most.
- **Interaction:** "The AI says `max(totals)` gives the category that cost the most. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Max goes through a dictionary like a loop does, so it compares the keys, not the totals. Asha tests it.
  **On screen:** AI chat, stage 3: Generate: one line for the biggest
    - You: My dictionary totals holds a total for each category. Write one line that finds the category with the biggest total. Tell me what it gives.
    - AI (example answer): Here is the line: `biggest = max(totals)` It gives the category that cost the most.
- **Narration:** Beans cost 30, the most. But the line prints milk!
  **On screen:** Code `examples/ai_biggest_flawed.py`, line 3 highlighted, output `examples/ai_biggest_flawed.expected`
- **Narration:** Max compared the names. In alphabetical order, milk comes last.
  **On screen:** Code `examples/ai_biggest_flawed.py`, line 3 highlighted, output `examples/ai_biggest_flawed.expected`
- **Narration:** Stage 4: test. Asha asks the AI for test days, each with the answer it expects.
  **On screen:** AI chat, stage 4: Test: days with known results
    - You: List test days for my biggest-category line. For each day, give the totals and the category you expect.
- **Narration:** The AI lists three days: three categories, one category, and a day where repairs cost the most.
  **On screen:** AI chat, stage 4: Test: days with known results
    - You: List test days for my biggest-category line. For each day, give the totals and the category you expect.
    - AI (example answer): Day 1: milk 20.5, beans 30, cups 6.25. Expect beans. Day 2: cups 9. Expect cups. Day 3: beans 5, repairs 45. Expect repairs.
- **Narration:** But it forgot a day. Asha remembers criterion five, and adds a day with no expenses.
  **On screen:** AI chat, stage 4: Test: days with known results
    - You: List test days for my biggest-category line. For each day, give the totals and the category you expect.
    - AI (example answer): Day 1: milk 20.5, beans 30, cups 6.25. Expect beans. Day 2: cups 9. Expect cups. Day 3: beans 5, repairs 45. Expect repairs.
    - You: You forgot one day. My criteria say a day with no expenses prints Biggest: none. I am adding Day 4 with no expenses.
- **Narration:** Lines 2 to 4 hold the AI's three test days. Lines 5 to 7 run the AI's line on each one.
  **On screen:** Code `examples/ai_max_tests.py`, line 5, 6, 7 highlighted, output hidden
- **Interaction:** "Which of the three days give the right answer?" stays on screen with a 10-second timer.
- **Narration:** Days 2 and 3. Day 1 fails with milk.
  **On screen:** Code `examples/ai_max_tests.py`, line 5, 6, 7 highlighted, output `examples/ai_max_tests.expected`
- **Narration:** But Day 3 passed only by luck: repairs is also last in alphabetical order. One passing test proves little.
  **On screen:** Code `examples/ai_max_tests.py`, line 4 highlighted, output `examples/ai_max_tests.expected`
- **Narration:** Now Asha's own day 4: no expenses. Line 2 is an empty dictionary, and line 4 calls max.
  **On screen:** Code `examples/ai_max_empty.py`, line 2, 4 highlighted, error `examples/ai_max_empty.expected_error`
- **Narration:** The program prints Summary, then stops with a Value Error on line 4.
  **On screen:** Code `examples/ai_max_empty.py`, line 2, 4 highlighted, error `examples/ai_max_empty.expected_error`
- **Narration:** Here are Asha's results. Day 1 fails.
  **On screen:** Table: Test days for the AI's line (row 1 in focus)
- **Narration:** Day 2 passes.
  **On screen:** Table: Test days for the AI's line (row 2 in focus)
- **Narration:** Day 3 passes, but only by luck.
  **On screen:** Table: Test days for the AI's line (row 3 in focus)
- **Narration:** And Day 4, the day the AI forgot, stops the program with an error.
  **On screen:** Table: Test days for the AI's line (row 4 in focus)
- **Narration:** Stage 5: debug. Asha pastes her lines and the full error report. She asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: On a day with no expenses, my program stopped. Here are my lines and the full error. Explain the cause first. Then show a fix that works for every day. [code `examples/ai_max_empty.py`]
- **Narration:** The AI explains: an empty dictionary has no keys, so max has nothing to choose from. And it agrees that max compares the keys.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: On a day with no expenses, my program stopped. Here are my lines and the full error. Explain the cause first. Then show a fix that works for every day. [code `examples/ai_max_empty.py`]
    - AI (example answer): An empty dictionary has no keys, so `max()` has nothing to choose from. And `max()` compares the keys, not the totals. The fix: start `biggest` at "none" and keep the biggest category so far in a loop.
- **Narration:** Its fix: start biggest at the text none, and keep the biggest category so far in a loop.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: On a day with no expenses, my program stopped. Here are my lines and the full error. Explain the cause first. Then show a fix that works for every day. [code `examples/ai_max_empty.py`]
    - AI (example answer): An empty dictionary has no keys, so `max()` has nothing to choose from. And `max()` compares the keys, not the totals. The fix: start `biggest` at "none" and keep the biggest category so far in a loop.
- **Narration:** Asha does not trust the fix yet. She runs all four test days again. Lines 2 to 5 hold the four days, and the last one is empty.
  **On screen:** Code `examples/ai_biggest_regression.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** Line 7 starts biggest at none. Lines 8 to 10 check every category. A category wins if nothing is chosen yet, or if its total is bigger than the best so far.
  **On screen:** Code `examples/ai_biggest_regression.py`, line 7, 8, 9, 10 highlighted, output hidden
- **Narration:** Here are the results: beans, cups, repairs, and none for the empty day. All four days pass!
  **On screen:** Code `examples/ai_biggest_regression.py`, line 11 highlighted, output `examples/ai_biggest_regression.expected`
- **Narration:** Quick check. What does max compare when you give it a dictionary?
  **On screen:** Quick check: "What does `max()` compare when you give it a dictionary?" (options shown)
- **Interaction:** "What does `max()` compare when you give it a dictionary?" stays on screen with a 10-second timer.
- **Narration:** B. The keys. A dictionary gives its keys, like a loop over it does.
  **On screen:** Quick check: "What does `max()` compare when you give it a dictionary?" (answer revealed: The keys)
- **Narration:** Breather. The AI was wrong, and sounded sure. Different test days caught it.
  **On screen:** Breather card
    - `max()` on a dictionary compares names.
    - One test passed by luck, and the AI forgot a day.
    - After the fix, every day ran again.
- **Narration:** Now, the complete tracker.
  **On screen:** Breather card
    - `max()` on a dictionary compares names.
    - One test passed by luck, and the AI forgot a day.
    - After the fix, every day ran again.
- **Breather:** 4 quiet seconds.

## Scene 13: Step 7: Put it together (12:33 to 13:37)

**Section:** Build it step by step

**Direction:** Walk the complete tracker in two halves, each beside the real output, then a new prediction with a test copy.

- **Narration:** Step 7: the complete tracker, in two halves. Lines 2 and 3: the set of categories, and an empty list.
  **On screen:** Code `project/expense_tracker.py`, line 2, 3 highlighted, output `project/expense_tracker.expected`
- **Narration:** Lines 4 to 9 are the loop from step 2. On the right, Asha's four categories.
  **On screen:** Code `project/expense_tracker.py`, line 4, 5, 6, 7, 8, 9 highlighted, output `project/expense_tracker.expected`
- **Narration:** Lines 11 to 15 ask for the amount and check it, as in step 3. A good amount becomes a tuple in the list.
  **On screen:** Code `project/expense_tracker.py`, line 10, 11, 12, 13, 14, 15 highlighted, output `project/expense_tracker.expected`
- **Narration:** The second half. Lines 16 to 18 build the totals, as in step 4.
  **On screen:** Code `project/expense_tracker.py`, line 16, 17, 18 highlighted, output `project/expense_tracker.expected`
- **Narration:** The loop on lines 20 to 23 does two jobs. It prints each row, and it keeps the biggest category so far.
  **On screen:** Code `project/expense_tracker.py`, line 19, 20, 21, 22, 23 highlighted, output `project/expense_tracker.expected`
- **Narration:** And lines 24 and 25 print the summary.
  **On screen:** Code `project/expense_tracker.py`, line 24, 25 highlighted, output `project/expense_tracker.expected`
- **Narration:** Your turn. Asha buys paper cups twice: 2, then 3.5. Then she types done.
  **On screen:** Code `examples/test_two_cups.py`, line 24 highlighted, output hidden
- **Interaction:** "What does line 24 print?" stays on screen with a 10-second timer.
- **Narration:** Expenses, 2. Total, 5.50. Both cups went into the list, and the totals added them into one row.
  **On screen:** Code `examples/test_two_cups.py`, line 24 highlighted, output `examples/test_two_cups.expected`

## Scene 14: Test it (13:37 to 14:55)

**Section:** Test it

**Direction:** The five whole-day tests with expected results, a prediction on bad amounts, the other runs as proof, then the results table.

- **Narration:** Criterion six says: test it. Each test is a copy of the tracker, with its own typed answers and an expected result.
  **On screen:** Table: Five test days
- **Narration:** A normal day, the day you saw at the start.
  **On screen:** Table: Five test days (row 1 in focus)
- **Narration:** An empty day.
  **On screen:** Table: Five test days (row 2 in focus)
- **Narration:** Bad amounts, with a comma and a word.
  **On screen:** Table: Five test days (row 3 in focus)
- **Narration:** Unknown categories.
  **On screen:** Table: Five test days (row 4 in focus)
- **Narration:** And one expense.
  **On screen:** Table: Five test days (row 5 in focus)
- **Narration:** The bad amounts test. Asha types milk with 12 comma 50, then milk with the word twelve, then milk with 12.50. Line 12 checks each amount.
  **On screen:** Code `examples/test_bad_amount.py`, line 12 highlighted, output hidden
- **Interaction:** "How many expenses does the summary count?" stays on screen with a 10-second timer.
- **Narration:** One. Each bad amount got a message and was never added. Only 12.50 counted. Pass!
  **On screen:** Code `examples/test_bad_amount.py`, line 12 highlighted, output `examples/test_bad_amount.expected`
- **Narration:** The empty day: Total, 0.00, and Biggest, none. No crash. Pass!
  **On screen:** Code `examples/test_empty.py`, line 19, 25 highlighted, output `examples/test_empty.expected`
- **Narration:** Unknown categories. Tea and cake each get the message. Repairs, with spaces around it, is cleaned and accepted. Pass!
  **On screen:** Code `examples/test_unknown.py`, line 5, 8, 9 highlighted, output `examples/test_unknown.expected`
- **Narration:** One expense: cups, 9.00, and Biggest, cups. Pass!
  **On screen:** Code `examples/test_one.py`, line 20, 21 highlighted, output `examples/test_one.expected`
- **Narration:** The normal day matched at the start of this video.
  **On screen:** Table: Five test days: results (row 1 in focus)
- **Narration:** And the other four runs you saw match too. All five test days pass.
  **On screen:** Table: Five test days: results

## Scene 15: Improve it with AI (14:55 to 16:16)

**Section:** Improve it with AI

**Direction:** Stage 6: the AI suggests plus equals. Ask what happens to the first milk, then the error on its own screen. Then the six stages table, and a breather.

- **Narration:** Stage 6: improve. Every test passes. Asha asks for one way to make lines 16 to 18 shorter, and says: do not change what it prints.
  **On screen:** AI chat, stage 6: Improve: a shorter line?
    - You: Every test passes. Suggest one way to make lines 16 to 18 shorter. Do not change what the program prints. [code `project/expense_tracker.py`]
- **Narration:** The AI suggests plus equals on line 18, without get. It sounds shorter and sensible.
  **On screen:** AI chat, stage 6: Improve: a shorter line?
    - You: Every test passes. Suggest one way to make lines 16 to 18 shorter. Do not change what the program prints. [code `project/expense_tracker.py`]
    - AI (example answer): Use `totals[category] += amount` on line 18. Plus equals adds the amount to the total, so you do not need `get()`.
- **Narration:** Remember why line 18 uses get. Plus equals must read the old total first.
  **On screen:** AI chat, stage 6: Improve: a shorter line?
    - You: Every test passes. Suggest one way to make lines 16 to 18 shorter. Do not change what the program prints. [code `project/expense_tracker.py`]
    - AI (example answer): Use `totals[category] += amount` on line 18. Plus equals adds the amount to the total, so you do not need `get()`.
- **Interaction:** "With `+=`, what happens when the first milk arrives?" stays on screen with a 10-second timer.
- **Narration:** There is no milk total yet, so Python cannot read it. Asha tests it on three expenses.
  **On screen:** AI chat, stage 6: Improve: a shorter line?
    - You: Every test passes. Suggest one way to make lines 16 to 18 shorter. Do not change what the program prints. [code `project/expense_tracker.py`]
    - AI (example answer): Use `totals[category] += amount` on line 18. Plus equals adds the amount to the total, so you do not need `get()`.
- **Narration:** Line 5 uses plus equals. The first milk has no total, and Python stops with a Key Error.
  **On screen:** Code `examples/ai_totals_keyerror.py`, line 5 highlighted, error `examples/ai_totals_keyerror.expected_error`
- **Narration:** The shorter line breaks the program, so Asha keeps get, with its default of 0.
  **On screen:** Code `examples/ai_totals_keyerror.py`, line 5 highlighted, error `examples/ai_totals_keyerror.expected_error`
- **Narration:** Here are all six stages on one tracker.
  **On screen:** Table: Six stages while building one tracker
- **Narration:** The AI helped at every stage, from the data model to the review.
  **On screen:** Table: Six stages while building one tracker (row 1 in focus)
- **Narration:** And it was confidently wrong three times: the model, the biggest category, and the shorter line.
  **On screen:** Table: Six stages while building one tracker (row 3 in focus)
- **Narration:** Every time, a test with a known result caught it.
  **On screen:** Table: Six stages while building one tracker (row 6 in focus)
- **Narration:** Last breather. You built a real data tool, and you made the decisions.
  **On screen:** Breather card
    - AI helped at all six stages.
    - It was wrong three times, and sounded sure.
    - Tests with known results caught every mistake.
- **Narration:** Let's recap.
  **On screen:** Breather card
    - AI helped at all six stages.
    - It was wrong three times, and sounded sure.
    - Tests with known results caught every mistake.
- **Breather:** 4 quiet seconds.

## Scene 16: Recap (16:16 to 17:50)

**Section:** Recap

**Direction:** Recap points one by one, a final quiz, the badge and the practice table.

- **Narration:** Here is what you used in this boss level.
  **On screen:** Recap
- **Narration:** Keep each record as a tuple in a list, so nothing is lost.
  **On screen:** Recap
    - Keep each record as a tuple in a list, so nothing is lost.
- **Narration:** Build totals with get and a default of 0. A set of allowed values rejects anything else.
  **On screen:** Recap
    - Keep each record as a tuple in a list, so nothing is lost.
    - Build totals with `get(key, 0)`. A set of allowed values rejects anything else.
- **Narration:** Replace with a third value, and is digit, check an amount before float converts it.
  **On screen:** Recap
    - Keep each record as a tuple in a list, so nothing is lost.
    - Build totals with `get(key, 0)`. A set of allowed values rejects anything else.
    - `replace(".", "", 1)` and `isdigit()` check an amount before `float()`.
- **Narration:** Max on a dictionary compares the keys. To find the biggest total, keep the biggest so far in a loop.
  **On screen:** Recap
    - Keep each record as a tuple in a list, so nothing is lost.
    - Build totals with `get(key, 0)`. A set of allowed values rejects anything else.
    - `replace(".", "", 1)` and `isdigit()` check an amount before `float()`.
    - `max()` on a dictionary compares the keys. Keep the biggest so far in a loop.
- **Narration:** And test several days, including an empty one. One test can pass by luck.
  **On screen:** Recap
    - Keep each record as a tuple in a list, so nothing is lost.
    - Build totals with `get(key, 0)`. A set of allowed values rejects anything else.
    - `replace(".", "", 1)` and `isdigit()` check an amount before `float()`.
    - `max()` on a dictionary compares the keys. Keep the biggest so far in a loop.
    - Test several days, including an empty one. One test can pass by luck.
- **Narration:** One last check. Asha types Beans with a capital B, then the amount 12.5.0. What does the tracker print next?
  **On screen:** Quick check: "Asha types `Beans` and then `12.5.0`. What does the tracker print next?" (options shown)
- **Interaction:** "Asha types `Beans` and then `12.5.0`. What does the tracker print next?" stays on screen with a 10-second timer.
- **Narration:** D. Lower makes beans, which is allowed. But 12.5.0 keeps a second point after one is removed, so the amount check fails, with a message, not a crash.
  **On screen:** Quick check: "Asha types `Beans` and then `12.5.0`. What does the tracker print next?" (answer revealed: Type an amount like 12.50.)
- **Narration:** Boss level complete! You earned 300 XP and the Money Mapper badge. And Module 3 is done.
  **On screen:** Money Mapper You earned 300 XP. Module 3 is complete.
- **Breather:** 2 quiet seconds.
- **Narration:** The practice file has eight more tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-ups, worth 10 XP each, such as checking an amount.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including the smallest category.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's tracker that forgets its totals.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Write down the expected result before you run each one.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 17: What's next (17:50 to 18:14)

**Section:** What's next

**Direction:** End card. Tease functions as the way to reuse the summary. Hold quietly at the end.

- **Narration:** Asha's tracker works. But the biggest-category loop appears in her tests, her fix and her tracker. Three copies of the same code.
  **On screen:** Functions: Reusable Blocks of Logic Write it once. Use it everywhere.
- **Narration:** In Chapter 16, you will learn functions: named blocks of code that you write once and use many times.
  **On screen:** Functions: Reusable Blocks of Logic Write it once. Use it everywhere.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Functions: Reusable Blocks of Logic Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 16.
  **On screen:** Functions: Reusable Blocks of Logic Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
