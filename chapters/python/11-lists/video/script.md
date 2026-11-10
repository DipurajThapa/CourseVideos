# Video Script: Chapter 11: Lists: Keeping Many Values in Order

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:54.

## Scene 1: Introduction (0:00 to 0:55)

**Section:** Introduction

**Direction:** Open on the forgetful game from Chapter 10. Then the title and the AI tease, then the day report as the mission, with no output yet.

- **Narration:** Remember Asha's biscuit jar game at the Corner Cafe? A player guesses 7, then 12, then 15.
  **On screen:** A game that forgets
    - At the Corner Cafe, a player guesses 7, then 12, then 15.
- **Narration:** Each guess lives in one variable, so each new guess replaces the one before.
  **On screen:** A game that forgets
    - At the Corner Cafe, a player guesses 7, then 12, then 15.
    - Each new guess replaces the one before.
- **Narration:** At the end, the game cannot show a single guess. Asha's day report from Chapter 9 had the same problem: it added up the sales, but could not show them again.
  **On screen:** A game that forgets
    - At the Corner Cafe, a player guesses 7, then 12, then 15.
    - Each new guess replaces the one before.
    - At the end, the game cannot show a single guess.
- **Narration:** This is Code Quest, Chapter 11. Today you learn lists: one variable that keeps many values, in order.
  **On screen:** Lists: Keeping Many Values in Order
- **Narration:** And an AI assistant will promise the three biggest sales of the day. Will its code deliver them? You will check.
  **On screen:** Lists: Keeping Many Values in Order Keep every value. Find any one.
- **Narration:** So here is today's mission. Asha's day report keeps every sale in one list, on line 2.
  **On screen:** Code `examples/ex06_day_report.py`, line 2 highlighted, output hidden
- **Narration:** Then it reports the total, the average, the biggest and the smallest sale, and the best two.
  **On screen:** Code `examples/ex06_day_report.py`, line 6, 7, 8, 9, 12 highlighted, output hidden
- **Narration:** And it still shows the sales in the order they happened. Let's build it.
  **On screen:** Code `examples/ex06_day_report.py`, line 13 highlighted, output hidden

## Scene 2: Learning goals (0:55 to 1:05)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Read any item of a list, and add or remove items.
  **On screen:** By the end, you will be able to:
    - Write a list and read any item by its index, from the start or the end.
    - Change a list with `append()`, `insert()`, `remove()` and `pop()`.
- **Narration:** Take a part with a slice, and build a list in a loop.
  **On screen:** By the end, you will be able to:
    - Write a list and read any item by its index, from the start or the end.
    - Change a list with `append()`, `insert()`, `remove()` and `pop()`.
    - Take a part of a list with a slice, and predict which items it gives.
    - Build a list in a loop, go through it with `for`, and check for an item with `in`.
- **Narration:** And sort a list, and add it up.
  **On screen:** By the end, you will be able to:
    - Write a list and read any item by its index, from the start or the end.
    - Change a list with `append()`, `insert()`, `remove()` and `pop()`.
    - Take a part of a list with a slice, and predict which items it gives.
    - Build a list in a loop, go through it with `for`, and check for an item with `in`.
    - Sort a list, and use `sum()`, `min()` and `max()` to report on it.

## Scene 3: Why this matters (1:05 to 1:20)

**Section:** Why this matters

**Direction:** Define a list through the forgetful game, then connect it to apps the learner uses.

- **Narration:** A list keeps many values in one variable, in a fixed order. And a list of 3 sales needs the same code as a list of 3,000.
  **On screen:** Why this matters
    - A **list** keeps many values in one variable, in a fixed order.
    - A list of 3 sales and a list of 3,000 sales need the same code.
- **Narration:** Your music playlist is a list. So is your shopping basket, and the messages in a chat.
  **On screen:** Why this matters
    - A **list** keeps many values in one variable, in a fixed order.
    - A list of 3 sales and a list of 3,000 sales need the same code.
    - A playlist, a shopping basket, the messages in a chat: each one is a list.

## Scene 4: The idea: items with an index (1:20 to 2:30)

**Section:** The idea

**Direction:** Teach brackets, indexes from 0 and negative indexes with the diagram. Then mutable versus strings, a quiz and a breather.

- **Narration:** A list is written with square brackets, and commas between the items. This list has four items.
  **On screen:** Every item has an index
- **Narration:** Each item has an index: its position. Counting starts at 0. So tea is at index 0, and scone is at index 3.
  **On screen:** Every item has an index
- **Narration:** Negative indexes count from the end. Minus 1 is always the last item, whatever the length of the list.
  **On screen:** Every item has an index
- **Narration:** In Chapter 3, you learned that a string cannot be changed after it is made.
  **On screen:** A list can change
    - Chapter 3: a string cannot be changed after it is made.
- **Narration:** A list can. You can replace an item, add one or remove one, and the list itself changes.
  **On screen:** A list can change
    - Chapter 3: a string cannot be changed after it is made.
    - A list can: replace an item, add one or remove one.
- **Narration:** We say a list is mutable. It can change after it is made.
  **On screen:** A list can change
    - Chapter 3: a string cannot be changed after it is made.
    - A list can: replace an item, add one or remove one.
    - A list is **mutable**: it can change after it is made.
- **Narration:** Quick check. Which one can you change after it is made?
  **On screen:** Quick check: "Which one can you change after it is made?" (options shown)
- **Interaction:** "Which one can you change after it is made?" stays on screen with a 10-second timer.
- **Narration:** C. A list. A string cannot be changed. Its methods give you a new string instead.
  **On screen:** Quick check: "Which one can you change after it is made?" (answer revealed: A list)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - A list keeps many values in order.
    - Indexes start at 0; minus 1 is the last item.
    - A list can change after it is made.
- **Narration:** Next, Asha writes her first list.
  **On screen:** Breather card
    - A list keeps many values in order.
    - Indexes start at 0; minus 1 is the last item.
    - A list can change after it is made.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Make a list and read its items (2:30 to 3:13)

**Section:** Build it step by step

**Direction:** The file types itself in. Teach len() on lists, then ask about lines 5 and 6, then reveal.

- **Narration:** Step 1. Asha writes today's first order as a list: tea, cake, sandwich, and tea again. A list can hold the same value twice.
  **On screen:** Code `examples/ex01_order_list.py`, lines 1 to 2 typed in, line 2 highlighted, output hidden
- **Narration:** Line 3 prints the whole list. Line 4 prints the item at index 0.
  **On screen:** Code `examples/ex01_order_list.py`, lines 1 to 4 typed in, line 3, 4 highlighted, output hidden
- **Narration:** Lines 5 and 6 print the items at index 2 and minus 1.
  **On screen:** Code `examples/ex01_order_list.py`, lines 1 to 6 typed in, line 5, 6 highlighted, output hidden
- **Narration:** And line 7 uses len, from Chapter 3. For a list, it counts the items.
  **On screen:** Code `examples/ex01_order_list.py`, lines 1 to 7 typed in, line 7 highlighted, output hidden
- **Interaction:** "What do lines 5 and 6 print?" stays on screen with a 10-second timer.
- **Narration:** Line 5 prints sandwich, the third item, because counting starts at 0.
  **On screen:** Code `examples/ex01_order_list.py`, lines 1 to 7 typed in, line 5 highlighted, output `examples/ex01_order_list.expected`
- **Narration:** Line 6 prints tea, the last item.
  **On screen:** Code `examples/ex01_order_list.py`, lines 1 to 7 typed in, line 6 highlighted, output `examples/ex01_order_list.expected`

## Scene 6: Step 2: Change a list (3:13 to 4:23)

**Section:** Build it step by step

**Direction:** Teach the five ways to change a list with the table, then the code. Ask which item line 7 replaces, then reveal.

- **Narration:** Step 2. A method is a function that belongs to a value, like upper for strings. Lists have methods that change the list itself.
  **On screen:** Table: Step 2: Five ways to change a list
- **Narration:** Append adds an item at the end.
  **On screen:** Table: Step 2: Five ways to change a list (row 1 in focus)
- **Narration:** Insert puts an item at an index, and moves the rest along.
  **On screen:** Table: Step 2: Five ways to change a list (row 2 in focus)
- **Narration:** An index with an equals sign replaces one item.
  **On screen:** Table: Step 2: Five ways to change a list (row 3 in focus)
- **Narration:** Remove deletes the first item that matches.
  **On screen:** Table: Step 2: Five ways to change a list (row 4 in focus)
- **Narration:** And pop removes the last item, and gives it back to you.
  **On screen:** Table: Step 2: Five ways to change a list (row 5 in focus)
- **Narration:** Asha's order starts with tea and cake. Line 3 appends a sandwich at the end.
  **On screen:** Code `examples/ex02_change_order.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 5 inserts juice at index 0, at the front. Everything else moves along by one.
  **On screen:** Code `examples/ex02_change_order.py`, line 5 highlighted, output hidden
- **Narration:** Line 7 replaces the item at index 1 with green tea.
  **On screen:** Code `examples/ex02_change_order.py`, line 7 highlighted, output hidden
- **Interaction:** "Which item does line 7 replace: juice, tea or cake?" stays on screen with a 10-second timer.
- **Narration:** Tea. After line 5, juice is at index 0, so tea moved to index 1.
  **On screen:** Code `examples/ex02_change_order.py`, line 5, 7 highlighted, output `examples/ex02_change_order.expected`
- **Narration:** Line 9 removes cake.
  **On screen:** Code `examples/ex02_change_order.py`, line 9 highlighted, output `examples/ex02_change_order.expected`
- **Narration:** And line 11 pops the last item, sandwich, and keeps it in the variable last. Line 12 prints it, then the shorter list.
  **On screen:** Code `examples/ex02_change_order.py`, line 11, 12 highlighted, output `examples/ex02_change_order.expected`

## Scene 7: Step 3: Slices (4:23 to 5:30)

**Section:** Build it step by step

**Direction:** Teach the slice rules first, with the range callback. Ask what line 3 prints, then reveal every line, ending with the slice past the end.

- **Narration:** Step 3. A slice takes a part of a list, and gives you a new list. You write a start and a stop, with a colon between them.
  **On screen:** Step 3: A slice takes a part
    - `sales[start:stop]` gives a new list.
- **Narration:** It starts at the start index, and stops before the stop index. Exactly like range in Chapter 8.
  **On screen:** Step 3: A slice takes a part
    - `sales[start:stop]` gives a new list.
    - It starts at `start` and stops **before** `stop`, like `range()`.
- **Narration:** Leave out the start, and it starts at 0. Leave out the stop, and it goes to the end.
  **On screen:** Step 3: A slice takes a part
    - `sales[start:stop]` gives a new list.
    - It starts at `start` and stops **before** `stop`, like `range()`.
    - No start: from index 0. No stop: to the end.
- **Narration:** And a slice never goes past the end of the list. It stops there, with no error.
  **On screen:** Step 3: A slice takes a part
    - `sales[start:stop]` gives a new list.
    - It starts at `start` and stops **before** `stop`, like `range()`.
    - No start: from index 0. No stop: to the end.
    - A slice never goes past the end. It gives no error.
- **Narration:** Here are five sales. Line 3 slices from 1 to 3.
  **On screen:** Code `examples/ex03_slices.py`, line 2, 3 highlighted, output hidden
- **Interaction:** "What does line 3 print?" stays on screen with a 10-second timer.
- **Narration:** 8.0 and 15.75: the items at index 1 and 2. Index 3 is the stop, so it is left out.
  **On screen:** Code `examples/ex03_slices.py`, line 3 highlighted, output `examples/ex03_slices.expected`
- **Narration:** Line 4 has no start, so it gives the first two. Line 5 has no stop, so it goes from index 2 to the end.
  **On screen:** Code `examples/ex03_slices.py`, line 4, 5 highlighted, output `examples/ex03_slices.expected`
- **Narration:** Line 6 starts at minus 2, so it gives the last two sales.
  **On screen:** Code `examples/ex03_slices.py`, line 6 highlighted, output `examples/ex03_slices.expected`
- **Narration:** And line 7 asks for items up to index 10. The list has only five, so the slice stops at the end. No error.
  **On screen:** Code `examples/ex03_slices.py`, line 7 highlighted, output `examples/ex03_slices.expected`

## Scene 8: Step 4: Build a list in a loop (5:30 to 6:19)

**Section:** Build it step by step

**Direction:** The fix for the forgetful game. Teach append in a loop, for over a list and in, then ask what line 11 prints.

- **Narration:** Step 4. Here is the fix for the game that forgot. Line 2 makes an empty list: two brackets with nothing between them.
  **On screen:** Code `examples/ex04_guesses.py`, line 2 highlighted, output hidden
- **Narration:** The loop asks three times. Line 5 appends each guess, so the list grows by one item on every pass.
  **On screen:** Code `examples/ex04_guesses.py`, line 3, 4, 5 highlighted, output hidden
- **Narration:** Line 7 goes through the list with for, one item at a time, as it went through a string in Chapter 8.
  **On screen:** Code `examples/ex04_guesses.py`, line 7, 8 highlighted, output hidden
- **Narration:** And the word in checks whether a value is in the list. It gives True or False.
  **On screen:** Code `examples/ex04_guesses.py`, line 9, 11 highlighted, output hidden
- **Interaction:** "The user types 7, 12 and 15. What does line 11 print?" stays on screen with a 10-second timer.
- **Narration:** False. 20 is not one of the guesses.
  **On screen:** Code `examples/ex04_guesses.py`, line 11 highlighted, output `examples/ex04_guesses.expected`
- **Narration:** And the game remembers every guess. Line 6 shows all three.
  **On screen:** Code `examples/ex04_guesses.py`, line 6 highlighted, output `examples/ex04_guesses.expected`
- **Narration:** 12 is in the list, so line 10 prints, You tried 12.
  **On screen:** Code `examples/ex04_guesses.py`, line 9, 10 highlighted, output `examples/ex04_guesses.expected`

## Scene 9: Step 5: Sort and add up (6:19 to 7:25)

**Section:** Build it step by step

**Direction:** Teach sorted() against sort() with the table first. Ask what line 4 prints, reveal, then sum, min and max. Then a breather.

- **Narration:** Step 5. There are two ways to sort a list, and the difference matters.
  **On screen:** Table: Step 5: Two ways to sort
- **Narration:** The function sorted makes a new sorted list. The original list stays the same.
  **On screen:** Table: Step 5: Two ways to sort (row 1 in focus)
- **Narration:** The method sort changes the list itself. And it gives back None, a special value that means no value.
  **On screen:** Table: Step 5: Two ways to sort (row 2 in focus)
- **Narration:** Line 3 prints sorted sales. Line 4 prints sales itself.
  **On screen:** Code `examples/ex05_sorting.py`, line 3, 4 highlighted, output hidden
- **Interaction:** "What does line 4 print?" stays on screen with a 10-second timer.
- **Narration:** The original order: 12.5, 8.0, 15.75, 9.25. Sorted made a new list, and left sales alone.
  **On screen:** Code `examples/ex05_sorting.py`, line 4 highlighted, output `examples/ex05_sorting.expected`
- **Narration:** Line 5 uses sort, so now the list itself is sorted, smallest first.
  **On screen:** Code `examples/ex05_sorting.py`, line 5, 6 highlighted, output `examples/ex05_sorting.expected`
- **Narration:** Reverse equals True sorts from the biggest to the smallest.
  **On screen:** Code `examples/ex05_sorting.py`, line 7 highlighted, output `examples/ex05_sorting.expected`
- **Narration:** And sum, min and max give the total, the smallest and the biggest number.
  **On screen:** Code `examples/ex05_sorting.py`, line 8 highlighted, output `examples/ex05_sorting.expected`
- **Narration:** Breather. You now have every piece of the mission. Let's put them together.
  **On screen:** Breather card
    - `append()`, `insert()`, `remove()`, `pop()` change a list.
    - A slice stops before its stop index.
    - `sorted()` makes a new list; `sort()` gives `None`.
- **Breather:** 4 quiet seconds.

## Scene 10: See the outcome: the day report (7:25 to 8:26)

**Section:** See the outcome

**Direction:** Return to the mission. Walk every line, ask about the best two, reveal. Hand over to the top three feature.

- **Narration:** Back to the mission. Line 2 keeps five sales. Line 3 appends a sixth, 6.5.
  **On screen:** Code `examples/ex06_day_report.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 adds them up with sum. Line 5 counts them with len.
  **On screen:** Code `examples/ex06_day_report.py`, line 4, 5 highlighted, output hidden
- **Narration:** Line 7 divides the total by len, so the average stays right when more sales arrive.
  **On screen:** Code `examples/ex06_day_report.py`, line 6, 7 highlighted, output hidden
- **Narration:** Lines 8 and 9 use max and min, and line 10 slices the last three. Line 11 makes a sorted copy, biggest first, and line 12 slices its first two.
  **On screen:** Code `examples/ex06_day_report.py`, line 8, 9, 10, 11, 12 highlighted, output hidden
- **Narration:** And line 13 prints the list in the order of the day.
  **On screen:** Code `examples/ex06_day_report.py`, line 13 highlighted, output hidden
- **Interaction:** "What does line 12 print?" stays on screen with a 10-second timer.
- **Narration:** 21.0 and 15.75, the two biggest sales.
  **On screen:** Code `examples/ex06_day_report.py`, line 11, 12 highlighted, output `examples/ex06_day_report.expected`
- **Narration:** And because line 11 used sorted, not sort, the last line still shows the day in order.
  **On screen:** Code `examples/ex06_day_report.py`, line 13 highlighted, output `examples/ex06_day_report.expected`
- **Narration:** Mission complete! Next, Asha wants a top three sales line. She builds it with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex06_day_report.py`, output `examples/ex06_day_report.expected`

## Scene 11: Work with AI: six stages, one top three line (8:26 to 13:31)

**Section:** Work with AI

**Direction:** Teach the worked example skill. One conversation per stage, all about the top three line. Stage 3 gives the three smallest, stage 4 predicts a wrong IndexError, stage 5 is Asha's sort() error, stage 6 reverses the order.

- **Narration:** This chapter's AI skill is the worked example. When AI explains a slice or a method, ask for a small list, the code and the exact result.
  **On screen:** This chapter's AI skill: a worked example
    - Ask AI to explain a slice or a method with a small list and the exact result.
- **Narration:** Then run the example yourself. And the safety habits from Chapter 1 still apply.
  **On screen:** This chapter's AI skill: a worked example
    - Ask AI to explain a slice or a method with a small list and the exact result.
    - Run the example yourself. The run decides.
    - Never paste private data. You are responsible for the code you use.
- **Narration:** Stage 1: plan. Asha wants the three biggest sales, biggest first, and the day order must stay the same. She asks for steps, with no code.
  **On screen:** AI chat, stage 1: Plan: the steps before the code
    - You: I am a beginner. My list `sales` holds today's sales in the order they happened. I want a line that shows the three biggest sales, biggest first, and the day order must stay the same. Do not write code yet. List the steps and name the method or function for each.
- **Narration:** The AI's plan: a sorted copy, biggest first. A slice of its first three. Print them. Then print sales, to check the day order.
  **On screen:** AI chat, stage 1: Plan: the steps before the code
    - You: I am a beginner. My list `sales` holds today's sales in the order they happened. I want a line that shows the three biggest sales, biggest first, and the day order must stay the same. Do not write code yet. List the steps and name the method or function for each.
    - AI (example answer): 1. Make a sorted copy, biggest first: `sorted(sales, reverse=True)`. 2. Take its first three items with a slice: `[:3]`. 3. Print them. 4. Print `sales` to check that the day order did not change.
- **Narration:** Stage 2: write. Asha writes a slice herself, and asks the AI to explain it with her own list as a worked example.
  **On screen:** AI chat, stage 2: Write: a worked example of a slice
    - You: I wrote these lines myself. Explain what `sales[:3]` gives, with my list as a worked example. Do not change my code. [code `examples/ai_slice_check.py`]
- **Narration:** The AI says: the first three items, in the order of the list. Not the biggest.
  **On screen:** AI chat, stage 2: Write: a worked example of a slice
    - You: I wrote these lines myself. Explain what `sales[:3]` gives, with my list as a worked example. Do not change my code. [code `examples/ai_slice_check.py`]
    - AI (example answer): `sales[:3]` takes the items at index 0, 1 and 2, in the order of the list: `[12.5, 8.0, 15.75]`. It does not pick the biggest. It picks the first three.
- **Narration:** She runs it. The example matches the run.
  **On screen:** AI chat, stage 2: Write: a worked example of a slice
    - You: I wrote these lines myself. Explain what `sales[:3]` gives, with my list as a worked example. Do not change my code. [code `examples/ai_slice_check.py`]
    - AI (example answer): `sales[:3]` takes the items at index 0, 1 and 2, in the order of the list: `[12.5, 8.0, 15.75]`. It does not pick the biggest. It picks the first three.
    - You: I ran it. Your example was right:
- **Narration:** Stage 3: generate. Asha asks for the code, and the exact output.
  **On screen:** AI chat, stage 3: Generate: the three biggest sales
    - You: Write code that prints the three biggest sales from my list. Show the exact output.
- **Narration:** The AI promises 21.0, 15.75 and 12.5. It sounds completely sure.
  **On screen:** AI chat, stage 3: Generate: the three biggest sales
    - You: Write code that prints the three biggest sales from my list. Show the exact output.
    - AI (example answer): Here it is. It prints `Top three: [21.0, 15.75, 12.5]`. [code `examples/ai_top_flawed.py`]
- **Narration:** Look at line 3. Remember which way sort puts the numbers.
  **On screen:** AI chat, stage 3: Generate: the three biggest sales
    - You: Write code that prints the three biggest sales from my list. Show the exact output.
    - AI (example answer): Here it is. It prints `Top three: [21.0, 15.75, 12.5]`. [code `examples/ai_top_flawed.py`]
- **Interaction:** "The AI says this prints the three biggest sales. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Sort puts the smallest first, so the first three items are the three smallest.
  **On screen:** AI chat, stage 3: Generate: the three biggest sales
    - You: Write code that prints the three biggest sales from my list. Show the exact output.
    - AI (example answer): Here it is. It prints `Top three: [21.0, 15.75, 12.5]`. [code `examples/ai_top_flawed.py`]
- **Narration:** Asha runs it. 6.5, 8.0 and 9.25: the three smallest sales of the day.
  **On screen:** Code `examples/ai_top_flawed.py`, line 3, 4 highlighted, output `examples/ai_top_flawed.expected`
- **Narration:** Stage 4: test. Asha shows the AI a failed check: the first of the top three must equal max, 21.0. She asks for a fix, and three test lists with expected outputs.
  **On screen:** AI chat, stage 4: Test: three lists with expected results
    - You: It printed `[6.5, 8.0, 9.25]`. My check: the first item must equal `max(sales)`, 21.0, so it fails. Fix it. Then give me three test lists with the expected output: a normal day, a day where the top three sales are equal, and a day with two sales.
- **Narration:** The fix: reverse equals True. And three expected results. For a day with only two sales, the AI predicts an Index Error.
  **On screen:** AI chat, stage 4: Test: three lists with expected results
    - You: It printed `[6.5, 8.0, 9.25]`. My check: the first item must equal `max(sales)`, 21.0, so it fails. Fix it. Then give me three test lists with the expected output: a normal day, a day where the top three sales are equal, and a day with two sales.
    - AI (example answer): Sort with `reverse=True`, so the biggest comes first. 1. Normal day: `[21.0, 15.75, 12.5]` 2. Top three equal: `[5.0, 5.0, 5.0]` 3. Two sales: an `IndexError`, because the list has fewer than three items. [code `examples/ai_top_fixed.py`]
- **Interaction:** "The AI says a day with two sales gives an `IndexError`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Remember step 3: a slice never goes past the end of the list. It stops there, with no error.
  **On screen:** AI chat, stage 4: Test: three lists with expected results
    - You: It printed `[6.5, 8.0, 9.25]`. My check: the first item must equal `max(sales)`, 21.0, so it fails. Fix it. Then give me three test lists with the expected output: a normal day, a day where the top three sales are equal, and a day with two sales.
    - AI (example answer): Sort with `reverse=True`, so the biggest comes first. 1. Normal day: `[21.0, 15.75, 12.5]` 2. Top three equal: `[5.0, 5.0, 5.0]` 3. Two sales: an `IndexError`, because the list has fewer than three items. [code `examples/ai_top_fixed.py`]
- **Narration:** Asha runs all three lists. A normal day: 21.0 first, and it equals max. Pass.
  **On screen:** Code `examples/ai_top_tests.py`, line 2, 3, 4 highlighted, output `examples/ai_top_tests.expected`
- **Narration:** The top three all equal: three fives. Pass.
  **On screen:** Code `examples/ai_top_tests.py`, line 5, 6, 7 highlighted, output `examples/ai_top_tests.expected`
- **Narration:** And only two sales: 9.0 and 4.0, with no error.
  **On screen:** Code `examples/ai_top_tests.py`, line 8, 9, 10 highlighted, output `examples/ai_top_tests.expected`
- **Narration:** But remember the plan: the day order must stay the same. Asha prints sales after the fix.
  **On screen:** Code `examples/ai_fix_order.py`, line 3, 5 highlighted, output `examples/ai_fix_order.expected`
- **Narration:** The top three are right. But sort changed the list itself, so the day order is gone.
  **On screen:** Code `examples/ai_fix_order.py`, line 3 highlighted, output `examples/ai_fix_order.expected`
- **Narration:** Three test lists pass. For two sales, the AI predicted an error, but the run gave none. A prediction is not a test. The run is.
  **On screen:** Table: Four checks on the AI's fix (row 3 in focus)
- **Narration:** And the day order check fails. Asha must fix that next.
  **On screen:** Table: Four checks on the AI's fix (row 4 in focus)
- **Narration:** Stage 5: debug. To keep the day order, Asha stores the result of sort in a new variable, top. Python stops with a Type Error.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I want to keep the day order, so I tried this. I got the error below. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_top_none.py`]
- **Narration:** She pastes the code and the full error, and asks for the cause first. The AI names line 3: sort gives back None. Not subscriptable means you cannot use square brackets on it. The fix is sorted.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I want to keep the day order, so I tried this. I got the error below. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_top_none.py`]
    - AI (example answer): Line 3 is the cause. `sort()` sorts the list and gives back `None`, so `top` is `None`. Line 4 cannot slice `None`. The smallest fix: `top = sorted(sales, reverse=True)`.
- **Narration:** Asha uses sorted on line 3. The top three are right.
  **On screen:** Code `examples/ai_top_sorted.py`, line 3 highlighted, output `examples/ai_top_sorted.expected`
- **Narration:** And the day order is still there, on the last line.
  **On screen:** Code `examples/ai_top_sorted.py`, line 5 highlighted, output `examples/ai_top_sorted.expected`
- **Narration:** A fix can break a case that worked before. So Asha runs all three test lists again, with sorted, and prints each list after it.
  **On screen:** Code `examples/ai_top_regression.py`, line 2, 3, 4 highlighted, output `examples/ai_top_regression.expected`
- **Narration:** Every top three is right, and every list keeps its order. All four checks pass.
  **On screen:** Code `examples/ai_top_regression.py`, output `examples/ai_top_regression.expected`
- **Narration:** Stage 6: improve. Asha asks for one change that makes the line shorter or clearer. And she adds: do not change what it prints.
  **On screen:** AI chat, stage 6: Improve: shorter, but the same?
    - You: My top three line works. Suggest one change that makes it shorter or clearer, with one reason. Do not change what it prints.
- **Narration:** The AI suggests: sort normally, and take the last three items with a negative slice. It says the output is the same.
  **On screen:** AI chat, stage 6: Improve: shorter, but the same?
    - You: My top three line works. Suggest one change that makes it shorter or clearer, with one reason. Do not change what it prints.
    - AI (example answer): Drop `reverse=True`: sort normally and take the last three items with `top[-3:]`. It is shorter and shows the same three sales.
- **Narration:** Asha tests it. Line 3 sorts smallest first. Line 4 takes the last three.
  **On screen:** Code `examples/ai_top_suggest.py`, line 3, 4 highlighted, output hidden
- **Interaction:** "Asha said: do not change what it prints. Does the suggestion keep that promise?" stays on screen with a 10-second timer.
- **Narration:** No. The same three sales, but in the opposite order: the biggest is now last. The AI ignored her instruction.
  **On screen:** Code `examples/ai_top_suggest.py`, line 3, 4 highlighted, output `examples/ai_top_suggest.expected`
- **Narration:** A different order is a different output. Asha keeps her sorted version.
  **On screen:** Code `examples/ai_top_suggest.py`, line 3, 4 highlighted, output `examples/ai_top_suggest.expected`
- **Narration:** Quick check. An AI explains what a slice does. What do you do next?
  **On screen:** Quick check: "An AI explains what a slice does. What do you do next?" (options shown)
- **Interaction:** "An AI explains what a slice does. What do you do next?" stays on screen with a 10-second timer.
- **Narration:** D. Run its worked example, and compare the result.
  **On screen:** Quick check: "An AI explains what a slice does. What do you do next?" (answer revealed: Run its worked example and compare)
- **Narration:** Breather. Asha caught three AI mistakes: the three smallest sales, an error that never happens, and a change of order. Next, the mistakes beginners make with lists.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - A prediction is not a test. The run is.
    - A different order is a different output.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes (13:31 to 15:24)

**Section:** Common mistakes

**Direction:** Mistake 1 shows the IndexError. Mistake 2 is a spot-it on sort(). Mistake 3 shows remove(). Mistake 4 is the missing comma, then a quiz.

- **Narration:** Mistake 1. This list has four items, so its indexes are 0 to 3. Line 3 prints tea.
  **On screen:** Code `examples/err01_index.py`, line 3 highlighted, error `examples/err01_index.expected_error`
- **Narration:** Line 4 asks for index 4, which does not exist. Python stops with an Index Error: list index out of range.
  **On screen:** Code `examples/err01_index.py`, line 4 highlighted, error `examples/err01_index.expected_error`
- **Narration:** The fix: the last index is the length minus 1. Or use minus 1.
  **On screen:** Code `examples/err01_index.py`, line 4 highlighted, error `examples/err01_index.expected_error`
- **Narration:** Now you try. Line 3 sorts the sales, and stores the result back in sales.
  **On screen:** Code `examples/ex07_sort_none.py`, line 3 highlighted, output hidden
- **Interaction:** "What does line 4 print?" stays on screen with a 10-second timer.
- **Narration:** None. Sort gives back None, so line 3 replaced the whole list with None.
  **On screen:** Code `examples/ex07_sort_none.py`, line 3 highlighted, output `examples/ex07_sort_none.expected`
- **Narration:** The fix: write sales dot sort on its own line, or use sorted.
  **On screen:** Code `examples/ex07_sort_none.py`, line 3 highlighted, output `examples/ex07_sort_none.expected`
- **Narration:** Mistake 3. The list has tea twice. Line 3 removes only the first tea.
  **On screen:** Code `examples/err02_remove_missing.py`, line 3 highlighted, error `examples/err02_remove_missing.expected_error`
- **Narration:** Line 5 removes juice, which is not in the list. Python stops with a Value Error.
  **On screen:** Code `examples/err02_remove_missing.py`, line 5 highlighted, error `examples/err02_remove_missing.expected_error`
- **Narration:** The fix: check with in first, and remove only when it is there.
  **On screen:** Code `examples/err02_remove_missing.py`, line 5 highlighted, error `examples/err02_remove_missing.expected_error`
- **Narration:** Mistake 4. Line 2 has no comma between tea and cake. Python joins two strings that stand next to each other, so you get one item: teacake.
  **On screen:** Code `examples/ex08_missing_comma.py`, line 2 highlighted, output `examples/ex08_missing_comma.expected`
- **Narration:** There is no error, but the list has 2 items, not 3. Check the count with len.
  **On screen:** Code `examples/ex08_missing_comma.py`, line 2 highlighted, output `examples/ex08_missing_comma.expected`
- **Narration:** Quick check. A list has 5 items. What is the index of the last item, counting from the start?
  **On screen:** Quick check: "A list has 5 items. What is the index of the last item, counting from the start?" (options shown)
- **Interaction:** "A list has 5 items. What is the index of the last item, counting from the start?" stays on screen with a 10-second timer.
- **Narration:** A. 4. Counting starts at 0, so the indexes are 0 to 4.
  **On screen:** Quick check: "A list has 5 items. What is the index of the last item, counting from the start?" (answer revealed: 4)
- **Narration:** Last breather. Now you know the four list mistakes that catch most beginners.
  **On screen:** Breather card
    - The last index is the length minus 1.
    - Never keep the result of `sort()`.
    - Check with `in` before you remove.
- **Breather:** 4 quiet seconds.

## Scene 13: Think beyond (15:24 to 16:10)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. A player types 7 twice. How could the word in let the game say, you already guessed 7, and not count the second try?
  **On screen:** Question card: "A player types 7 twice. How could `in` let the game say "You already guessed 7" and not count the try?"
- **Interaction:** "A player types 7 twice. How could `in` let the game say "You already guessed 7" and not count the try?" stays on screen with a 10-second timer.
- **Narration:** Try it in your editor after the video.
  **On screen:** Question card: "A player types 7 twice. How could `in` let the game say "You already guessed 7" and not count the try?"
- **Narration:** Second. Range has a step. A slice can have one too: two colons, then 2. Which sales does it give? Predict first, then run it.
  **On screen:** Question card: "`range()` has a step. A slice can have one too: `sales[::2]`. Which sales does it give?"
- **Interaction:** "`range()` has a step. A slice can have one too: `sales[::2]`. Which sales does it give?" stays on screen with a 10-second timer.
- **Narration:** Compare your prediction with the real run.
  **On screen:** Question card: "`range()` has a step. A slice can have one too: `sales[::2]`. Which sales does it give?"

## Scene 14: Recap (16:10 to 17:09)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap. A list keeps many values in order. Indexes start at 0, and minus 1 is the last item.
  **On screen:** Recap
    - A list keeps many values in order. Indexes start at 0; `-1` is the last item.
- **Narration:** A list can change: append, insert, remove and pop.
  **On screen:** Recap
    - A list keeps many values in order. Indexes start at 0; `-1` is the last item.
    - A list is mutable: `append()`, `insert()`, `remove()` and `pop()` change it.
- **Narration:** A slice stops before its stop index, and never goes past the end.
  **On screen:** Recap
    - A list keeps many values in order. Indexes start at 0; `-1` is the last item.
    - A list is mutable: `append()`, `insert()`, `remove()` and `pop()` change it.
    - A slice `[start:stop]` stops before `stop` and never goes past the end.
- **Narration:** For goes through a list, and in checks whether a value is in it.
  **On screen:** Recap
    - A list keeps many values in order. Indexes start at 0; `-1` is the last item.
    - A list is mutable: `append()`, `insert()`, `remove()` and `pop()` change it.
    - A slice `[start:stop]` stops before `stop` and never goes past the end.
    - `for` goes through a list; `in` checks whether a value is in it.
- **Narration:** Sorted gives a new list. Sort changes the list, and gives None.
  **On screen:** Recap
    - A list keeps many values in order. Indexes start at 0; `-1` is the last item.
    - A list is mutable: `append()`, `insert()`, `remove()` and `pop()` change it.
    - A slice `[start:stop]` stops before `stop` and never goes past the end.
    - `for` goes through a list; `in` checks whether a value is in it.
    - `sorted()` gives a new list; `sort()` changes the list and gives `None`.
- **Narration:** And with AI: ask for a worked example, then run it yourself.
  **On screen:** Recap
    - A list keeps many values in order. Indexes start at 0; `-1` is the last item.
    - A list is mutable: `append()`, `insert()`, `remove()` and `pop()` change it.
    - A slice `[start:stop]` stops before `stop` and never goes past the end.
    - `for` goes through a list; `in` checks whether a value is in it.
    - `sorted()` gives a new list; `sort()` changes the list and gives `None`.
    - Ask AI for a worked example, then run it yourself.
- **Narration:** One last check. Sales holds 3, 9 and 1. What does sorted sales, index minus 1, give?
  **On screen:** Quick check: "`sales = [3, 9, 1]`. What does `sorted(sales)[-1]` give?" (options shown)
- **Interaction:** "`sales = [3, 9, 1]`. What does `sorted(sales)[-1]` give?" stays on screen with a 10-second timer.
- **Narration:** B. 9. Sorted gives 1, 3, 9, and minus 1 is the last item.
  **On screen:** Quick check: "`sales = [3, 9, 1]`. What does `sorted(sales)[-1]` give?" (answer revealed: 9)
- **Narration:** Mission complete! You earned 100 XP and the List Builder badge.
  **On screen:** List Builder You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice (17:09 to 17:33)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. The practice file has eight tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including a shopping list.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each: a game that remembers, and an AI's top scores to fix.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Predict first, then run. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 16: What's next (17:33 to 17:54)

**Section:** What's next

**Direction:** End card. Tease dictionaries: find a price by its name, not its position. Hold quietly at the end.

- **Narration:** Lists find a value by its position. But what is the price of tea? A list cannot answer by name.
  **On screen:** Dictionaries: Looking Things Up by Name Find a value by its name, not its position.
- **Narration:** In Chapter 12, you will learn dictionaries. They find a value by its name, like the price of tea.
  **On screen:** Dictionaries: Looking Things Up by Name Find a value by its name, not its position.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Dictionaries: Looking Things Up by Name Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 12.
  **On screen:** Dictionaries: Looking Things Up by Name Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
