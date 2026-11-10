# Video Script: Chapter 13: Tuples and Sets: Fixed Groups and Unique Items

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:18.

## Scene 1: Introduction (0:00 to 0:48)

**Section:** Introduction

**Direction:** Open on the problem from Chapter 12: Omar is in the customer list four times. Then the title with the AI tease, then the loyalty report as the mission, with no output yet.

- **Narration:** At the Corner Cafe, Asha keeps a list of today's customers. Omar loves the cafe. He is in the list four times.
  **On screen:** Omar, four times
    - Asha's list of today's customers has Omar in it four times.
- **Narration:** So len counts visits, not people. How many different customers came in today? A list cannot tell her.
  **On screen:** Omar, four times
    - Asha's list of today's customers has Omar in it four times.
    - `len()` counts visits, not people.
    - How many different customers came in today?
- **Narration:** This is Code Quest, Chapter 13: tuples, for fixed groups, and sets, which keep each item only once.
  **On screen:** Tuples and Sets: Fixed Groups and Unique Items
- **Narration:** And an AI assistant will sound completely sure about empty brackets, and be wrong. You will catch it.
  **On screen:** Tuples and Sets: Fixed Groups and Unique Items Each item once. Fixed groups stay fixed.
- **Narration:** So here is today's mission. Line 2 is the list of today's visits, with every repeat.
  **On screen:** Code `examples/ex07_loyalty.py`, line 2 highlighted, output hidden
- **Narration:** Line 5 makes a set from it, so each customer counts once. Line 4 keeps the opening hours as a fixed pair.
  **On screen:** Code `examples/ex07_loyalty.py`, line 4, 5 highlighted, output hidden
- **Narration:** And lines 9 to 11 compare today with yesterday. Let's build it.
  **On screen:** Code `examples/ex07_loyalty.py`, line 9, 10, 11 highlighted, output hidden

## Scene 2: Learning goals (0:48 to 0:58)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Write and unpack tuples, remove repeats with a set, compare two sets, and choose the right collection with an AI that compares the options.
  **On screen:** By the end, you will be able to:
    - Write a tuple, read its values and unpack them into variables.
    - Make a set from a list to remove repeats, and check items with `in`.
    - Compare two sets with `|`, `&`, `-` and `^`.
    - Choose between a list, a tuple, a set and a dictionary for a task.
    - Ask AI to compare options with trade-offs, then test its advice.

## Scene 3: Why this matters (0:58 to 1:11)

**Section:** Why this matters

**Direction:** Define a set and a tuple through the cafe, then connect them to apps the learner uses.

- **Narration:** A set keeps each item once, so it counts people. A tuple keeps a fixed group, such as the opening hours. Booking sites and maps use both, and the right choice makes code shorter and safer.
  **On screen:** Why this matters
    - A **set** keeps each item only once. It counts people, not visits.
    - A **tuple** keeps a fixed group, such as the opening hours.
    - A booking site keeps each seat once. A map stores each place as a fixed pair of numbers.

## Scene 4: The idea: four collections (1:11 to 2:21)

**Section:** The idea

**Direction:** Teach the four collections with the table, row by row, then the bag of name cards. Then a quiz and a breather.

- **Narration:** You now know four collections. A list, in square brackets, keeps order, allows repeats, and can change.
  **On screen:** Table: Four collections, four jobs (row 1 in focus)
- **Narration:** A tuple, in round brackets, is like a list that cannot change.
  **On screen:** Table: Four collections, four jobs (row 2 in focus)
- **Narration:** A set uses curly brackets with values inside. It keeps no order, and each item appears only once.
  **On screen:** Table: Four collections, four jobs (row 3 in focus)
- **Narration:** And a dictionary also uses curly brackets, but with keys and values. Each key appears once.
  **On screen:** Table: Four collections, four jobs (row 4 in focus)
- **Narration:** Think of a set as a bag of name cards, in no fixed order. Unlike a real bag, a set ignores a card that is already inside. Add Omar four times, and it still holds one Omar.
  **On screen:** A set is like a bag of name cards
    - Each name card is in the bag once. The cards are in no fixed order.
    - Unlike a bag: a set ignores a card that is already inside.
    - Add Omar four times, and the set still holds one Omar.
- **Narration:** Quick check. Which collection keeps each item only once, in no fixed order?
  **On screen:** Quick check: "Which collection keeps each item only once, in no fixed order?" (options shown)
- **Interaction:** "Which collection keeps each item only once, in no fixed order?" stays on screen with a 10-second timer.
- **Narration:** D. A set. Each item once, and no fixed order.
  **On screen:** Quick check: "Which collection keeps each item only once, in no fixed order?" (answer revealed: A set)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - A list keeps every repeat.
    - A tuple is a fixed group.
    - A set keeps each item once.
- **Narration:** Next, Asha stores the opening hours as a tuple.
  **On screen:** Breather card
    - A list keeps every repeat.
    - A tuple is a fixed group.
    - A set keeps each item once.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Make a tuple (2:21 to 3:16)

**Section:** Build it step by step

**Direction:** The file types itself in. Teach round brackets, the comma and indexing, then ask what lines 5 and 6 print.

- **Narration:** Step 1. Asha's cafe opens at 8 and closes at 18. Line 2 keeps both numbers in a tuple, with round brackets and a comma. The comma is what makes a tuple.
  **On screen:** Code `examples/ex01_tuples.py`, lines 1 to 3 typed in, line 2 highlighted, output hidden
- **Narration:** Line 3 keeps one special: a scone and its price. A tuple can hold different types.
  **On screen:** Code `examples/ex01_tuples.py`, lines 1 to 3 typed in, line 3 highlighted, output hidden
- **Narration:** You read a tuple with an index, exactly like a list. Index 0 is the first value.
  **On screen:** Code `examples/ex01_tuples.py`, lines 1 to 8 typed in, line 5, 6 highlighted, output hidden
- **Interaction:** "What do lines 5 and 6 print?" stays on screen with a 10-second timer.
- **Narration:** Line 4 prints the whole tuple, 8 and 18, in round brackets.
  **On screen:** Code `examples/ex01_tuples.py`, lines 1 to 8 typed in, line 4 highlighted, output `examples/ex01_tuples.expected`
- **Narration:** Then lines 5 and 6 print 8 and 18, and Scone. Index 0 of hours is 8, index 1 is 18, and index 0 of special is the name.
  **On screen:** Code `examples/ex01_tuples.py`, lines 1 to 8 typed in, line 5, 6 highlighted, output `examples/ex01_tuples.expected`
- **Narration:** Line 7 counts 2 values, and line 8 shows the type: tuple.
  **On screen:** Code `examples/ex01_tuples.py`, lines 1 to 8 typed in, line 7, 8 highlighted, output `examples/ex01_tuples.expected`

## Scene 6: Step 2: Unpack a tuple (3:16 to 4:08)

**Section:** Build it step by step

**Direction:** Teach unpacking on line 3, then the swap on line 9. Ask what line 10 prints, then call back to the Chapter 2 swap question.

- **Narration:** Step 2. Unpacking puts each value of a tuple into its own variable, in one line. Line 3 gives opens the first value, and closes the second.
  **On screen:** Code `examples/ex02_unpacking.py`, line 2, 3 highlighted, output hidden
- **Narration:** The number of names on the left must match the number of values. Line 5 unpacks the scone and its price the same way.
  **On screen:** Code `examples/ex02_unpacking.py`, line 5, 6 highlighted, output hidden
- **Narration:** Now lines 7 to 9. First is Omar, second is Lina. Line 9 builds a tuple on the right from the old values, second then first, and then unpacks it.
  **On screen:** Code `examples/ex02_unpacking.py`, line 7, 8, 9 highlighted, output hidden
- **Interaction:** "What does line 10 print?" stays on screen with a 10-second timer.
- **Narration:** Lina, then Omar. The two names swapped places, with no third variable.
  **On screen:** Code `examples/ex02_unpacking.py`, line 9, 10 highlighted, output `examples/ex02_unpacking.expected`
- **Narration:** Remember the swap question from Chapter 2? This is the short answer. And lines 4 and 6 print the hours and the scone.
  **On screen:** Code `examples/ex02_unpacking.py`, line 4, 6 highlighted, output `examples/ex02_unpacking.expected`

## Scene 7: Step 3: A list of tuples (4:08 to 5:09)

**Section:** Build it step by step

**Direction:** Teach unpacking in a loop, like items() in Chapter 12, and reading in two steps. Ask what line 10 prints. Then a breather.

- **Narration:** Step 3. A list of tuples is a common way to keep records. Each special is a name and a price.
  **On screen:** Code `examples/ex03_specials.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Line 6 unpacks each tuple into name and price, the same way items did with a dictionary in Chapter 12. Lines 7 and 8 print the line and add the price.
  **On screen:** Code `examples/ex03_specials.py`, line 6, 7, 8 highlighted, output hidden
- **Narration:** Line 10 reads in two steps, like the nested menu in Chapter 12. Specials, index 1, gives one tuple. Then index 0 reads from that tuple.
  **On screen:** Code `examples/ex03_specials.py`, line 10 highlighted, output hidden
- **Interaction:** "What does line 10 print?" stays on screen with a 10-second timer.
- **Narration:** Scone. Index 1 is the second tuple, scone and 2.75, and index 0 is its name.
  **On screen:** Code `examples/ex03_specials.py`, line 10 highlighted, output `examples/ex03_specials.expected`
- **Narration:** And the loop printed each special, lined up, with a total of 10.50.
  **On screen:** Code `examples/ex03_specials.py`, line 6, 7, 8, 9 highlighted, output `examples/ex03_specials.expected`
- **Narration:** Breather. Tuples are done. Next, the hero of this chapter: the set.
  **On screen:** Breather card
    - Round brackets and a comma make a tuple.
    - Unpacking: one name for each value.
    - A list of tuples keeps records.
- **Breather:** 4 quiet seconds.

## Scene 8: Step 4: Remove repeats with a set (5:09 to 6:01)

**Section:** Build it step by step

**Direction:** Teach set(), no order and no positions, sorted() and in. Ask what lines 4 and 5 print, then reveal.

- **Narration:** Step 4. Line 2 lists five visits, with Omar three times. Line 3 turns the list into a set, and every repeat disappears.
  **On screen:** Code `examples/ex04_unique.py`, line 2, 3 highlighted, output hidden
- **Narration:** A set has no order, so it has no positions, and printed directly, its names can change order between runs. So line 6 prints sorted, a list in a fixed order.
  **On screen:** Code `examples/ex04_unique.py`, line 6 highlighted, output hidden
- **Narration:** A set compares the exact text, so Omar and omar would be two different items. And in checks a set quickly, even when it holds thousands of names.
  **On screen:** Code `examples/ex04_unique.py`, line 7, 8 highlighted, output hidden
- **Interaction:** "What do lines 4 and 5 print?" stays on screen with a 10-second timer.
- **Narration:** 5, then 3. The list has five visits, but the set has three different customers.
  **On screen:** Code `examples/ex04_unique.py`, line 4, 5 highlighted, output `examples/ex04_unique.expected`
- **Narration:** Line 6 shows them in order: Lina, Omar, Sam. Lina is in the set, and Ravi is not.
  **On screen:** Code `examples/ex04_unique.py`, line 6, 7, 8 highlighted, output `examples/ex04_unique.expected`

## Scene 9: Step 5: Add and remove items (6:01 to 7:10)

**Section:** Build it step by step

**Direction:** Teach add() and discard(), ask what line 6 prints, then the empty-set rule on line 10, then a quiz on it.

- **Narration:** Step 5. Line 2 makes an empty set. Add puts an item into it. Lines 3 to 5 add Omar, Lina, and Omar again. Remember the bag of name cards.
  **On screen:** Code `examples/ex05_change_set.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** Line 6 prints the sorted names and the number of items.
  **On screen:** Code `examples/ex05_change_set.py`, line 6 highlighted, output hidden
- **Interaction:** "What does line 6 print?" stays on screen with a 10-second timer.
- **Narration:** Lina and Omar, and 2. The second Omar changed nothing: he was already inside.
  **On screen:** Code `examples/ex05_change_set.py`, line 5, 6 highlighted, output `examples/ex05_change_set.expected`
- **Narration:** Discard takes an item out. Line 8 discards Zoe, who is not in the set, and there is no error.
  **On screen:** Code `examples/ex05_change_set.py`, line 7, 8, 9 highlighted, output `examples/ex05_change_set.expected`
- **Narration:** And line 10 shows an important rule. Empty curly brackets make an empty dictionary. To make an empty set, write set, with round brackets.
  **On screen:** Code `examples/ex05_change_set.py`, line 10 highlighted, output `examples/ex05_change_set.expected`
- **Narration:** Quick check. How do you make an empty set?
  **On screen:** Quick check: "How do you make an empty set?" (options shown)
- **Interaction:** "How do you make an empty set?" stays on screen with a 10-second timer.
- **Narration:** B. Set, with round brackets. Empty curly brackets make a dictionary. Keep this one in mind.
  **On screen:** Quick check: "How do you make an empty set?" (answer revealed: `set()`)

## Scene 10: Step 6: Compare two sets (7:10 to 8:09)

**Section:** Build it step by step

**Direction:** Teach the four operators with the table, then the code. Ask what line 6 prints, then reveal all four.

- **Narration:** Step 6. Four operators compare two sets. The vertical bar is union: items in either set.
  **On screen:** Table: Step 6: Four ways to compare two sets (row 1 in focus)
- **Narration:** The and sign is intersection: items in both.
  **On screen:** Table: Step 6: Four ways to compare two sets (row 2 in focus)
- **Narration:** Minus is difference: items in the first set only.
  **On screen:** Table: Step 6: Four ways to compare two sets (row 3 in focus)
- **Narration:** And the hat sign, called a caret, is symmetric difference: items in one set, but not both.
  **On screen:** Table: Step 6: Four ways to compare two sets (row 4 in focus)
- **Narration:** Today, Omar, Lina and Sam came in. Yesterday, Lina, Ravi and Sam.
  **On screen:** Code `examples/ex06_set_ops.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 6 takes yesterday away from today.
  **On screen:** Code `examples/ex06_set_ops.py`, line 6 highlighted, output hidden
- **Interaction:** "What does line 6 print?" stays on screen with a 10-second timer.
- **Narration:** Omar, only. He came today, but not yesterday.
  **On screen:** Code `examples/ex06_set_ops.py`, line 6 highlighted, output `examples/ex06_set_ops.expected`
- **Narration:** Union gives all four names, and intersection gives Lina and Sam, who came both days.
  **On screen:** Code `examples/ex06_set_ops.py`, line 4, 5 highlighted, output `examples/ex06_set_ops.expected`
- **Narration:** The caret gives Omar and Ravi: each came on one day only. And for minus, order matters: yesterday minus today gives Ravi.
  **On screen:** Code `examples/ex06_set_ops.py`, line 7 highlighted, output `examples/ex06_set_ops.expected`

## Scene 11: See the outcome: the loyalty report (8:09 to 9:10)

**Section:** See the outcome

**Direction:** Return to the mission. Walk every line, ask about lines 7 and 8, reveal the rest. Hand over to the welcome feature.

- **Narration:** Back to the mission. Line 2 lists today's visits, with every repeat. Line 3 is yesterday's set of customers.
  **On screen:** Code `examples/ex07_loyalty.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 unpacks the opening hours, line 5 makes the set of today's customers, and line 6 prints the hours.
  **On screen:** Code `examples/ex07_loyalty.py`, line 4, 5, 6 highlighted, output hidden
- **Narration:** Lines 9 to 11 compare the two days, and line 12 checks for Omar with in.
  **On screen:** Code `examples/ex07_loyalty.py`, line 9, 10, 11, 12 highlighted, output hidden
- **Narration:** And line 7 counts the list, while line 8 counts the set.
  **On screen:** Code `examples/ex07_loyalty.py`, line 7, 8 highlighted, output hidden
- **Interaction:** "What numbers do lines 7 and 8 print?" stays on screen with a 10-second timer.
- **Narration:** Visits today, 7. Different customers, 3. The list counts visits, and the set counts people.
  **On screen:** Code `examples/ex07_loyalty.py`, line 7, 8 highlighted, output `examples/ex07_loyalty.expected`
- **Narration:** Lina and Sam came both days. Omar is new today, and Ravi missed today.
  **On screen:** Code `examples/ex07_loyalty.py`, line 9, 10, 11 highlighted, output `examples/ex07_loyalty.expected`
- **Narration:** And line 12 checks the set with in: Omar came today, True.
  **On screen:** Code `examples/ex07_loyalty.py`, line 12 highlighted, output `examples/ex07_loyalty.expected`
- **Narration:** Each collection does one job. Mission complete! Next, Asha welcomes each new customer, with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex07_loyalty.py`, output `examples/ex07_loyalty.expected`

## Scene 12: Work with AI: six stages, one welcome (9:10 to 14:14)

**Section:** Work with AI

**Direction:** Teach the trade-offs skill. One conversation per stage, all about the welcome. Generate: the AI's empty curly brackets. Test: the AI predicts one welcome for omar with a space. Debug: square brackets after add, then every case again. Improve: a suggestion that removes every welcome.

- **Narration:** This chapter's AI skill is asking for trade-offs: what you gain and what you lose with each choice. Ask for a strength and a weakness for each option, and you get an answer you can check.
  **On screen:** This chapter's AI skill: ask for trade-offs
    - "Which is best?" gets one answer you cannot judge.
    - "Compare the options, with a strength and a weakness each" gets an answer you can check.
    - Never paste private data. You are responsible for the code you use.
- **Narration:** Stage 1: plan. Asha wants to welcome each customer the first time they come in, in the order they arrive. She asks the AI to compare all four collections, and not to choose for her.
  **On screen:** AI chat, stage 1: Plan: compare, then choose
    - You: I want to welcome each customer the first time they come in today, in the order they arrive. Compare a list, a tuple, a set and a dictionary for remembering who I have welcomed. One strength and one weakness each. Do not choose for me.
- **Narration:** The AI gives a strength and a weakness for each. Asha chooses: the visit list keeps the order, and a set remembers who she has already welcomed.
  **On screen:** AI chat, stage 1: Plan: compare, then choose
    - You: I want to welcome each customer the first time they come in today, in the order they arrive. Compare a list, a tuple, a set and a dictionary for remembering who I have welcomed. One strength and one weakness each. Do not choose for me.
    - AI (example answer): List: keeps order. Weakness: `in` checks every item, one by one. Tuple: fixed. Weakness: you cannot add a name. Set: each name once, and `in` is fast. Weakness: no order. Dictionary: can count visits per name. Weakness: more than you need.
- **Narration:** Stage 2: write. Asha writes the first lines herself, and asks the AI to explain line 3 with her own list.
  **On screen:** AI chat, stage 2: Write: a worked example of one line
    - You: I wrote these lines myself. Explain line 3 step by step, with my list as a worked example. Do not change my code. [code `examples/ai_seen_write.py`]
- **Narration:** The AI explains: set of today keeps each name once, so the length is 3, and Sam is in it. She runs it, and the worked example matches.
  **On screen:** AI chat, stage 2: Write: a worked example of one line
    - You: I wrote these lines myself. Explain line 3 step by step, with my list as a worked example. Do not change my code. [code `examples/ai_seen_write.py`]
    - AI (example answer): `set(today)` goes through the list and keeps each name once: Omar, Lina and Sam. Omar's second visit adds nothing new, so `len(seen)` is 3, and `"Sam" in seen` is `True`.
    - You: I ran it. Your worked example was right:
- **Narration:** Stage 3: generate. Asha asks for the welcome code, with an empty set called seen, and the exact output.
  **On screen:** AI chat, stage 3: Generate: welcome each customer once
    - You: Write code that prints Welcome and the name the first time each customer in my list appears, then the number of new customers. Use an empty set called seen. Show the exact output.
- **Narration:** The AI promises three welcomes, then New today, 3. Look at line 3.
  **On screen:** AI chat, stage 3: Generate: welcome each customer once
    - You: Write code that prints Welcome and the name the first time each customer in my list appears, then the number of new customers. Use an empty set called seen. Show the exact output.
    - AI (example answer): Here it is. It prints three welcomes, then `New today: 3`. [code `examples/ai_welcome_flawed.py`]
- **Interaction:** "The AI promises three welcomes and `New today: 3`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Remember step 5: empty curly brackets make a dictionary, not a set.
  **On screen:** AI chat, stage 3: Generate: welcome each customer once
    - You: Write code that prints Welcome and the name the first time each customer in my list appears, then the number of new customers. Use an empty set called seen. Show the exact output.
    - AI (example answer): Here it is. It prints three welcomes, then `New today: 3`. [code `examples/ai_welcome_flawed.py`]
- **Narration:** Asha runs it. One welcome for Omar, then the program stops on line 7.
  **On screen:** Code `examples/ai_welcome_flawed.py`, line 3, 7 highlighted, error `examples/ai_welcome_flawed.expected_error`
- **Narration:** No attribute add means a dictionary has no add method. The AI sounded sure, and it was wrong. Set, with round brackets, fixes line 3.
  **On screen:** Code `examples/ai_welcome_flawed.py`, line 3, 7 highlighted, error `examples/ai_welcome_flawed.expected_error`
- **Narration:** Stage 4: test. Asha fixes line 3, and asks for three test cases with the exact expected output. Her rule: one welcome per person.
  **On screen:** AI chat, stage 4: Test: three cases, with expected output
    - You: I fixed line 3 with set(). My rule: one welcome per person. Give me three test cases with the exact expected output. Use a normal day and an empty day. In the third, Omar is also typed as "omar ", with a small letter and a space.
- **Narration:** The AI predicts each case. For case 3, Omar and omar with a space, it predicts one welcome for Omar.
  **On screen:** AI chat, stage 4: Test: three cases, with expected output
    - You: I fixed line 3 with set(). My rule: one welcome per person. Give me three test cases with the exact expected output. Use a normal day and an empty day. In the third, Omar is also typed as "omar ", with a small letter and a space.
    - AI (example answer): 1. A normal day: Omar, Lina and Sam are welcomed. New today: 3. 2. An empty day: no welcomes. New today: 0. 3. Omar and "omar ": one welcome for Omar, then Lina. New today: 2.
- **Interaction:** "Will the code really print one welcome for Omar in case 3?" stays on screen with a 10-second timer.
- **Narration:** No. A set compares the exact text. Omar with a capital O, and omar with a space, are two different names.
  **On screen:** AI chat, stage 4: Test: three cases, with expected output
    - You: I fixed line 3 with set(). My rule: one welcome per person. Give me three test cases with the exact expected output. Use a normal day and an empty day. In the third, Omar is also typed as "omar ", with a small letter and a space.
    - AI (example answer): 1. A normal day: Omar, Lina and Sam are welcomed. New today: 3. 2. An empty day: no welcomes. New today: 0. 3. Omar and "omar ": one welcome for Omar, then Lina. New today: 2.
- **Narration:** Asha runs every case. The normal day and the empty day print what the AI predicted. But case 3 welcomes Omar twice: once as Omar, and once as omar with a space.
  **On screen:** Code `examples/ai_case_spelling.py`, line 2 highlighted, output `examples/ai_case_spelling.expected`
- **Narration:** Case 3 fails her rule: one welcome per person. And the AI's prediction did not match the run. Only running it showed both.
  **On screen:** Table: Three cases on the fixed code (row 3 in focus)
- **Narration:** Stage 5: debug. Asha cleans each name on line 5, with strip and title from Chapter 3. But she types line 8 too fast, and the program stops. She pastes the code and the full error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I clean each name with line 5 now. But the program stopped with this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_welcome_typo.py`]
- **Narration:** The AI names line 8: square brackets after add. Add is a method, so it needs round brackets. Not subscriptable means you cannot use square brackets on it.
  **On screen:** AI chat, stage 5: Debug: the AI's answer
    - You: What is the cause, and the smallest fix?
    - AI (example answer): Line 8 uses square brackets after `add`. `add` is a method, so you call it with round brackets: `seen.add(name)`. "Not subscriptable" means you cannot use square brackets on it.
- **Narration:** A fix can break a case that worked before, so Asha runs all three cases again. Lines 2 to 4 keep each case name with its list of visits.
  **On screen:** Code `examples/ai_welcome_regression.py`, line 2, 3, 4 highlighted, output `examples/ai_welcome_regression.expected`
- **Narration:** Line 9 cleans each name, and line 12 now uses round brackets.
  **On screen:** Code `examples/ai_welcome_regression.py`, line 9, 12 highlighted, output `examples/ai_welcome_regression.expected`
- **Narration:** The normal day: three welcomes, New today 3. Pass.
  **On screen:** Code `examples/ai_welcome_regression.py`, output `examples/ai_welcome_regression.expected`
- **Narration:** Omar typed two ways: one welcome for Omar, then Lina. New today, 2. Pass.
  **On screen:** Code `examples/ai_welcome_regression.py`, output `examples/ai_welcome_regression.expected`
- **Narration:** And the empty day: New today, 0. Pass. All three cases pass.
  **On screen:** Code `examples/ai_welcome_regression.py`, output `examples/ai_welcome_regression.expected`
- **Narration:** Stage 6: improve. Asha asks for one change that makes the code shorter. And she adds: the output must stay exactly the same.
  **On screen:** AI chat, stage 6: Improve: shorter, but the same?
    - You: My program passes every case. Suggest one change that makes it shorter, with one reason. The output must stay exactly the same.
- **Narration:** The AI suggests making the set from the whole list on line 3. Then the add line is not needed, it says.
  **On screen:** AI chat, stage 6: Improve: shorter, but the same?
    - You: My program passes every case. Suggest one change that makes it shorter, with one reason. The output must stay exactly the same.
    - AI (example answer): Make the set from the list on line 3: `seen = set(today)`. The set then holds every name already, so you can delete the `add` line. The output stays the same.
- **Narration:** Asha tests it on the normal day. Line 3 now fills the set with every name before the loop starts. Line 6 checks if the name is not in seen.
  **On screen:** Code `examples/ai_welcome_suggest.py`, line 3, 6 highlighted, output hidden
- **Interaction:** "Does the AI's version still welcome Omar, Lina and Sam?" stays on screen with a 10-second timer.
- **Narration:** No. Every name is already in seen, so the check on line 6 is never true. No welcomes at all, only New today, 3.
  **On screen:** Code `examples/ai_welcome_suggest.py`, line 3, 6 highlighted, output `examples/ai_welcome_suggest.expected`
- **Narration:** The AI broke her rule: the output did not stay the same. Asha keeps her version.
  **On screen:** Code `examples/ai_welcome_suggest.py`, line 3, 6 highlighted, output `examples/ai_welcome_suggest.expected`
- **Narration:** Quick check. Which prompt gets an answer you can check against your job?
  **On screen:** Quick check: "Which prompt gets an AI answer you can check?" (options shown)
- **Interaction:** "Which prompt gets an AI answer you can check?" stays on screen with a 10-second timer.
- **Narration:** A. Ask for a comparison, with a strength and a weakness each. Then you choose.
  **On screen:** Quick check: "Which prompt gets an AI answer you can check?" (answer revealed: Compare the four collections, with a strength and weakness each.)
- **Narration:** Breather. Asha compared four options and chose one. Then she caught three AI mistakes: empty curly brackets, a wrong prediction, and a change that broke her rule. Next, the mistakes beginners make with tuples and sets.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - A set compares the exact text.
    - Run every case again after a fix.
- **Breather:** 4 quiet seconds.

## Scene 13: Common mistakes (14:14 to 15:51)

**Section:** Common mistakes

**Direction:** Mistake 1 shows changing a tuple. Mistakes 2 and 3 are spot-it questions on rules taught in steps 1 and 4. The video leaves the unpacking mistake to the lesson.

- **Narration:** Mistake 1. Line 3 prints the hours. Line 4 tries to change the opening hour to 9.
  **On screen:** Code `examples/err01_change_tuple.py`, line 3, 4 highlighted, error `examples/err01_change_tuple.expected_error`
- **Narration:** A tuple cannot change, so Python stops with a Type Error. Does not support item assignment means you cannot give one position a new value.
  **On screen:** Code `examples/err01_change_tuple.py`, line 4 highlighted, error `examples/err01_change_tuple.expected_error`
- **Narration:** The fix: make a new tuple, nine and eighteen. Or use a list if the values change often.
  **On screen:** Code `examples/err01_change_tuple.py`, line 4 highlighted, error `examples/err01_change_tuple.expected_error`
- **Narration:** Now you try. Line 2 puts round brackets around one word, tea. Remember step 1: what makes a tuple?
  **On screen:** Code `examples/ex08_one_item.py`, line 2 highlighted, output hidden
- **Interaction:** "What type is `special` on line 2?" stays on screen with a 10-second timer.
- **Narration:** A string, not a tuple. There is no comma, so the brackets do nothing. Len counts 3 letters.
  **On screen:** Code `examples/ex08_one_item.py`, line 2, 3 highlighted, output `examples/ex08_one_item.expected`
- **Narration:** There is no error, which makes this mistake hard to see. The fix: a comma after the value, as on line 4.
  **On screen:** Code `examples/ex08_one_item.py`, line 4, 5 highlighted, output `examples/ex08_one_item.expected`
- **Narration:** One more. Line 4 asks the set of customers for index 0. Remember step 4.
  **On screen:** Code `examples/err02_set_index.py`, line 4 highlighted, output hidden
- **Interaction:** "What happens on line 4?" stays on screen with a 10-second timer.
- **Narration:** The program stops with a Type Error. A set has no order, so it has no positions. Not subscriptable means no square brackets.
  **On screen:** Code `examples/err02_set_index.py`, line 4 highlighted, error `examples/err02_set_index.expected_error`
- **Narration:** The fix: check a name with in, or use sorted to get a list you can index.
  **On screen:** Code `examples/err02_set_index.py`, line 4 highlighted, error `examples/err02_set_index.expected_error`
- **Narration:** Last breather. Now you know the tuple and set mistakes that catch most beginners.
  **On screen:** Breather card
    - A tuple cannot change.
    - The comma makes a tuple.
    - A set has no positions.
- **Breather:** 4 quiet seconds.

## Scene 14: Think beyond (15:51 to 16:40)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Asha has a set of customers who ordered tea, and a set who ordered cake. Which operator gives the customers who ordered both? And which gives tea, but not cake?
  **On screen:** Question card: "One set holds the tea drinkers, one holds the cake eaters. Which operator gives both? Which gives tea but not cake?"
- **Interaction:** "One set holds the tea drinkers, one holds the cake eaters. Which operator gives both? Which gives tea but not cake?" stays on screen with a 10-second timer.
- **Narration:** Write both after the video, and run them.
  **On screen:** Question card: "One set holds the tea drinkers, one holds the cake eaters. Which operator gives both? Which gives tea but not cake?"
- **Narration:** Second. A dictionary key must never change. Could a tuple, such as table 4 by the window, be a key for a booking? Could a list?
  **On screen:** Question card: "A dictionary key must never change. Could the tuple `(4, "window")` be a key for a table booking? Could a list?"
- **Interaction:** "A dictionary key must never change. Could the tuple `(4, "window")` be a key for a table booking? Could a list?" stays on screen with a 10-second timer.
- **Narration:** Try both, and read the error message if you get one.
  **On screen:** Question card: "A dictionary key must never change. Could the tuple `(4, "window")` be a key for a table booking? Could a list?"

## Scene 15: Recap (16:40 to 17:34)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap. A tuple is a fixed group you cannot change, and unpacking puts each value into its own variable.
  **On screen:** Recap
    - A tuple is a fixed group in round brackets. Read it like a list; you cannot change it.
    - Unpacking puts each value into its own variable: `opens, closes = hours`.
- **Narration:** A set keeps each item once, with no order. An empty set is set, with round brackets.
  **On screen:** Recap
    - A tuple is a fixed group in round brackets. Read it like a list; you cannot change it.
    - Unpacking puts each value into its own variable: `opens, closes = hours`.
    - A set keeps each item once and has no order. `set(visits)` removes repeats.
    - `{}` is an empty dictionary. An empty set is `set()`.
- **Narration:** Four operators compare two sets, and sorted gives a fixed order.
  **On screen:** Recap
    - A tuple is a fixed group in round brackets. Read it like a list; you cannot change it.
    - Unpacking puts each value into its own variable: `opens, closes = hours`.
    - A set keeps each item once and has no order. `set(visits)` removes repeats.
    - `{}` is an empty dictionary. An empty set is `set()`.
    - `|`, `&`, `-` and `^` compare two sets. Print `sorted(...)` for a fixed order.
- **Narration:** And with AI: ask for trade-offs, then choose and test yourself.
  **On screen:** Recap
    - A tuple is a fixed group in round brackets. Read it like a list; you cannot change it.
    - Unpacking puts each value into its own variable: `opens, closes = hours`.
    - A set keeps each item once and has no order. `set(visits)` removes repeats.
    - `{}` is an empty dictionary. An empty set is `set()`.
    - `|`, `&`, `-` and `^` compare two sets. Print `sorted(...)` for a fixed order.
    - Ask AI to compare options with trade-offs, then choose and test.
- **Narration:** One last check. Set a holds tea and cake. Set b holds cake and scone. What does sorted of a and b give, with the and sign?
  **On screen:** Quick check: "`a = {"tea", "cake"}` and `b = {"cake", "scone"}`. What does `sorted(a & b)` give?" (options shown)
- **Interaction:** "`a = {"tea", "cake"}` and `b = {"cake", "scone"}`. What does `sorted(a & b)` give?" stays on screen with a 10-second timer.
- **Narration:** C. Cake, only. The and sign gives the items in both sets.
  **On screen:** Quick check: "`a = {"tea", "cake"}` and `b = {"cake", "scone"}`. What does `sorted(a & b)` give?" (answer revealed: `['cake']`)
- **Narration:** Mission complete! You earned 100 XP and the Collector badge.
  **On screen:** Collector You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 16: Practice (17:34 to 17:56)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn: eight tasks, worth 170 XP. Three warm-up tasks at 10 XP, and three apply tasks at 20, including an allergy check.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each: a welcome with a reward, and an AI's set code to fix. Try each one before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 17: What's next (17:56 to 18:18)

**Section:** What's next

**Direction:** End card. Tease comprehensions: a loop that builds a new list in four lines, written in one. Hold quietly at the end.

- **Narration:** To make a list of every price with tax added, Asha writes four lines: an empty list, a loop, the new price, and append.
  **On screen:** Comprehensions: Transforming Data in One Line Build a new list in one line.
- **Narration:** In Chapter 14, you will write that in one line, with a comprehension, and learn when a normal loop is clearer.
  **On screen:** Comprehensions: Transforming Data in One Line Build a new list in one line.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Comprehensions: Transforming Data in One Line Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 14.
  **On screen:** Comprehensions: Transforming Data in One Line Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
