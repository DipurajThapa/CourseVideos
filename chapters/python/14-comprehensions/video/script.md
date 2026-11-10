# Video Script: Chapter 14: Comprehensions: Transforming Data in One Line

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:54 (estimate, not rendered yet).

## Scene 1: Introduction

**Section:** Introduction

**Direction:** Open on the three-line loop pattern that builds a new list, in Asha's words. Then the title with the AI tease, then the menu board as the mission, with no output yet.

- **Narration:** At the Corner Cafe, Asha adds tax to every price. She needs three lines: an empty list, a loop, and append with the new price.
  **On screen:** Code `examples/ex01_tax_loop.py`, line 3, 4, 5 highlighted, output hidden
- **Narration:** Then names in capitals. Then only the vegan items. Asha sighs: another empty list, another loop, another append. Is there a shorter way?
  **On screen:** Code `examples/ex01_tax_loop.py`, line 3, 4, 5 highlighted, output hidden
- **Narration:** This is Code Quest, Chapter 14: comprehensions. One line that builds a new list.
  **On screen:** Comprehensions: Transforming Data in One Line
- **Narration:** And an AI assistant will rewrite Asha's loop in one line, and promise the same output. Will it keep its promise? You will check.
  **On screen:** Comprehensions: Transforming Data in One Line One line. The same result. Prove it.
- **Narration:** So here is today's mission: the menu board for the Corner Cafe. Lines 2 to 5 hold each item, its price, and whether it is vegan.
  **On screen:** Code `examples/ex08_menu_board.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** Lines 6, 7 and 8 are three comprehensions. Each one builds something new in one line.
  **On screen:** Code `examples/ex08_menu_board.py`, line 6, 7, 8 highlighted, output hidden
- **Narration:** And the printing stays in a normal loop. You will see why. Let's build it.
  **On screen:** Code `examples/ex08_menu_board.py`, line 9, 10 highlighted, output hidden

## Scene 2: Learning goals

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Write list comprehensions, filter them, build dictionaries the same way, and know when a loop is clearer.
  **On screen:** By the end, you will be able to:
    - Write a list comprehension that makes a new list from an old one.
    - Add an `if` at the end to keep only some items.
    - Write a dictionary comprehension that makes a new dictionary.
    - Explain when a normal loop is clearer than a comprehension.
- **Narration:** And ask an AI to rewrite a loop, then prove that the output stayed the same.
  **On screen:** By the end, you will be able to:
    - Write a list comprehension that makes a new list from an old one.
    - Add an `if` at the end to keep only some items.
    - Write a dictionary comprehension that makes a new dictionary.
    - Explain when a normal loop is clearer than a comprehension.
    - Ask AI to rewrite a loop as one line, then prove the output stayed the same.

## Scene 3: Why this matters

**Section:** Why this matters

**Direction:** Define a comprehension through Asha's repeated pattern, then connect it to real tools and to choosing.

- **Narration:** A comprehension builds a new list or dictionary from another collection, in one line. It says what you want, not how to collect it.
  **On screen:** Why this matters
    - A **comprehension** builds a new list or dictionary from another collection, in one line.
    - It says what you want, not how to collect it step by step.
- **Narration:** Data tools and reports use comprehensions all the time. But they do not replace every loop. Part of this chapter is learning to choose.
  **On screen:** Why this matters
    - A **comprehension** builds a new list or dictionary from another collection, in one line.
    - It says what you want, not how to collect it step by step.
    - Data tools and reports use them to clean and reshape data.
    - It does not replace every loop. Part of the skill is choosing.

## Scene 4: The idea: three parts in square brackets

**Section:** The idea

**Direction:** Teach the three parts with the diagram, then the recipe-card comparison and where it stops working. Then a quiz and a breather.

- **Narration:** A list comprehension has three parts inside square brackets. Start in the middle: the loop. For price in prices, exactly like a for loop.
  **On screen:** Three parts in square brackets
- **Narration:** On the left is the new value, made for each item. Here, the price with tax, rounded to two places.
  **On screen:** Three parts in square brackets
- **Narration:** And on the right, an optional filter. Keep the item only if the condition is True. No empty list. No append.
  **On screen:** Three parts in square brackets
- **Narration:** Think of a comprehension as a recipe card for a new list. For each price, if it is under 4, write down the price with tax.
  **On screen:** A recipe card for a new list
    - "For each price, if it is under 4, write down the price with tax."
- **Narration:** Unlike a real recipe card, it cannot do other jobs on the way. No printing, and no running total. It only builds the new list.
  **On screen:** A recipe card for a new list
    - "For each price, if it is under 4, write down the price with tax."
    - Unlike a real recipe card, it cannot do other jobs on the way.
    - No printing, and no running total. Only one new list.
- **Narration:** Quick check. In this comprehension, which part is the new value?
  **On screen:** Quick check: "In `[name.upper() for name in items]`, which part is the new value?" (options shown)
- **Interaction:** "In `[name.upper() for name in items]`, which part is the new value?" stays on screen with a 10-second timer.
- **Narration:** C. Name dot upper. The new value comes first, on the left, and it is made for each item.
  **On screen:** Quick check: "In `[name.upper() for name in items]`, which part is the new value?" (answer revealed: `name.upper()`)
- **Narration:** Take a breather. Here is what you know so far. Next, Asha rewrites her tax loop in one line.
  **On screen:** Breather card
    - The new value comes first.
    - Then the loop.
    - Then an optional filter.
- **Breather:** 4 quiet seconds.

## Scene 5: Steps 1 and 2: The same list in one line

**Section:** Build it step by step

**Direction:** Recall the loop from the opening as the known starting point, then the comprehension. Ask what lines 4 and 5 print, then compare.

- **Narration:** Step 1 is the loop you saw at the start: an empty list, a loop, and append, with round to two places, from Chapter 2.
  **On screen:** Code `examples/ex02_tax_comp.py`, output hidden
- **Narration:** Step 2. Line 3 builds the same list in one line. The new value first, then for price in prices.
  **On screen:** Code `examples/ex02_tax_comp.py`, line 3 highlighted, output hidden
- **Narration:** Line 4 prints the new list. Line 5 prints the length of the new list, and the length of the old one.
  **On screen:** Code `examples/ex02_tax_comp.py`, line 4, 5 highlighted, output hidden
- **Interaction:** "What do lines 4 and 5 print?" stays on screen with a 10-second timer.
- **Narration:** Line 4 prints exactly the same list as the loop: 3.85, 4.4, 4.68, and 3.03.
  **On screen:** Code `examples/ex02_tax_comp.py`, line 4 highlighted, output `examples/ex02_tax_comp.expected`
- **Narration:** And line 5 prints 4 and 4. Without a filter, the new list has one item for each old item.
  **On screen:** Code `examples/ex02_tax_comp.py`, line 5 highlighted, output `examples/ex02_tax_comp.expected`

## Scene 6: Step 3: Transform text

**Section:** Build it step by step

**Direction:** Teach that the new value can be any expression. Ask what lines 5 and 6 print. Reveal that the old list did not change.

- **Narration:** Step 3. The new value can be any expression. Line 2 holds the menu names, all in small letters.
  **On screen:** Code `examples/ex03_names.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 uses title, the string method from Chapter 3. Line 4 uses len, so each new item is a number.
  **On screen:** Code `examples/ex03_names.py`, line 3, 4 highlighted, output hidden
- **Interaction:** "What do lines 5 and 6 print?" stays on screen with a 10-second timer.
- **Narration:** Line 5 prints the names with capital letters: Tea, Coffee, Carrot Cake, Scone.
  **On screen:** Code `examples/ex03_names.py`, line 5 highlighted, output `examples/ex03_names.expected`
- **Narration:** Line 6 prints the lengths: 3, 6, 11 and 5. The space in carrot cake counts too.
  **On screen:** Code `examples/ex03_names.py`, line 6 highlighted, output `examples/ex03_names.expected`
- **Narration:** And line 7 shows the old list, unchanged. A comprehension always makes a new list.
  **On screen:** Code `examples/ex03_names.py`, line 7 highlighted, output `examples/ex03_names.expected`

## Scene 7: Step 4: Keep only some items

**Section:** Build it step by step

**Direction:** Teach the filter and unpacking tuples in the loop part, with line 6. Ask what line 9 prints.

- **Narration:** Step 4. Each tuple holds a name, a price, and whether the item is vegan. The loop part unpacks all three, as in Chapter 13.
  **On screen:** Code `examples/ex04_filter.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** An if at the end is a filter. An item goes into the new list only when the condition is True. Line 6 keeps the vegan names.
  **On screen:** Code `examples/ex04_filter.py`, line 6 highlighted, output hidden
- **Narration:** Line 7 keeps the names of the items that cost less than 4.
  **On screen:** Code `examples/ex04_filter.py`, line 7 highlighted, output hidden
- **Interaction:** "What does line 9 print?" stays on screen with a 10-second timer.
- **Narration:** Tea and Scone. Coffee costs exactly 4, and 4 is not less than 4.
  **On screen:** Code `examples/ex04_filter.py`, line 7, 9 highlighted, output `examples/ex04_filter.expected`
- **Narration:** And line 8 prints the vegan names: Tea and Coffee. With a filter, the new list can be shorter.
  **On screen:** Code `examples/ex04_filter.py`, line 6, 8 highlighted, output `examples/ex04_filter.expected`

## Scene 8: Step 5: Filter or choose

**Section:** Build it step by step

**Direction:** Contrast the filter at the end with if-else at the start. Ask how many items line 6 prints. Then a quiz and a breather.

- **Narration:** Step 5. Line 3 has an if at the end, so it filters. Only prices under 4 stay.
  **On screen:** Code `examples/ex05_if_else.py`, line 3 highlighted, output hidden
- **Narration:** Line 4 is different. The if and else come first, before the for. That chooses a value for every item: snack under 4, otherwise treat.
  **On screen:** Code `examples/ex05_if_else.py`, line 4 highlighted, output hidden
- **Narration:** This form must have an else, because every item needs a value.
  **On screen:** Code `examples/ex05_if_else.py`, line 4 highlighted, output hidden
- **Interaction:** "How many labels does line 6 print?" stays on screen with a 10-second timer.
- **Narration:** Four. One label for each price: snack, treat, treat, snack.
  **On screen:** Code `examples/ex05_if_else.py`, line 4, 6 highlighted, output `examples/ex05_if_else.expected`
- **Narration:** But line 5 prints only two prices. The filter made that list shorter.
  **On screen:** Code `examples/ex05_if_else.py`, line 3, 5 highlighted, output `examples/ex05_if_else.expected`
- **Narration:** Quick check. Which comprehension keeps only the prices under 4?
  **On screen:** Quick check: "Which comprehension keeps only the prices under 4?" (options shown)
- **Interaction:** "Which comprehension keeps only the prices under 4?" stays on screen with a 10-second timer.
- **Narration:** B. The filter goes at the end. Option A keeps every item, and puts 0 in place of the others.
  **On screen:** Quick check: "Which comprehension keeps only the prices under 4?" (answer revealed: `[p for p in prices if p < 4]`)
- **Narration:** Breather. Relax for a moment. Next, the same idea builds a whole dictionary.
  **On screen:** Breather card
    - The new value can be any expression.
    - An `if` at the end filters.
    - `if ... else` at the start chooses.
- **Breather:** 4 quiet seconds.

## Scene 9: Step 6: Build a dictionary

**Section:** Build it step by step

**Direction:** Teach key: value in curly brackets with items() from Chapter 12. Ask what lines 5 and 6 print.

- **Narration:** Step 6. Line 2 is the menu dictionary from Chapter 12.
  **On screen:** Code `examples/ex06_dict_comp.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 uses curly brackets with a key, a colon, and a value. That makes a dictionary comprehension. Items gives each name and price.
  **On screen:** Code `examples/ex06_dict_comp.py`, line 3 highlighted, output hidden
- **Narration:** Line 5 reads cake from the new dictionary. Line 6 reads cake from the old menu.
  **On screen:** Code `examples/ex06_dict_comp.py`, line 5, 6 highlighted, output hidden
- **Interaction:** "What do lines 5 and 6 print?" stays on screen with a 10-second timer.
- **Narration:** 4.68, the cake with tax, and then 4.25. The old menu did not change.
  **On screen:** Code `examples/ex06_dict_comp.py`, line 5, 6 highlighted, output `examples/ex06_dict_comp.expected`
- **Narration:** Line 4 shows the whole new dictionary: the same keys, with new values.
  **On screen:** Code `examples/ex06_dict_comp.py`, line 4 highlighted, output `examples/ex06_dict_comp.expected`

## Scene 10: Step 7: When a loop is clearer

**Section:** Build it step by step

**Direction:** Show a loop with four jobs per item. Explain why a comprehension would be harder to read here.

- **Narration:** Step 7. Today, items of 4 or more cost 0.50 less, and they get a label. Lines 5 to 7 do that.
  **On screen:** Code `examples/ex07_loop_clearer.py`, line 5, 6, 7 highlighted, output hidden
- **Narration:** Line 8 prints each item, and line 9 adds it to a total. That is four jobs for each item.
  **On screen:** Code `examples/ex07_loop_clearer.py`, line 8, 9 highlighted, output hidden
- **Narration:** A comprehension builds one new list and nothing else. Here, a normal loop is much easier to read.
  **On screen:** Code `examples/ex07_loop_clearer.py`, output `examples/ex07_loop_clearer.expected`
- **Narration:** So the rule is simple. One new list or dictionary: use a comprehension. Several steps, a print, or a running total: use a loop.
  **On screen:** Code `examples/ex07_loop_clearer.py`, output `examples/ex07_loop_clearer.expected`

## Scene 11: See the outcome: the menu board

**Section:** See the outcome

**Direction:** Return to the mission. Walk every line, ask what line 12 prints, then reveal. Hand over to the AI feature.

- **Narration:** Back to the mission. Line 6 builds a dictionary: each name, with its price plus tax.
  **On screen:** Code `examples/ex08_menu_board.py`, line 6 highlighted, output hidden
- **Narration:** Line 7 filters the vegan names. Line 8 filters the board, so it compares the prices with tax.
  **On screen:** Code `examples/ex08_menu_board.py`, line 7, 8 highlighted, output hidden
- **Narration:** Lines 9 and 10 print the board with a normal loop, because printing is not building a list.
  **On screen:** Code `examples/ex08_menu_board.py`, line 9, 10 highlighted, output hidden
- **Narration:** Line 12 prints the names whose price with tax is under 4.
  **On screen:** Code `examples/ex08_menu_board.py`, line 8, 12 highlighted, output hidden
- **Interaction:** "What does line 12 print?" stays on screen with a 10-second timer.
- **Narration:** Tea and Scone. With tax, Tea is 3.85 and Scone is 3.03. Coffee becomes 4.40, so it is out.
  **On screen:** Code `examples/ex08_menu_board.py`, line 8, 12 highlighted, output `examples/ex08_menu_board.expected`
- **Narration:** Line 11 prints the vegan items, Tea and Coffee. Three comprehensions, one loop. Mission complete!
  **On screen:** Code `examples/ex08_menu_board.py`, line 7, 11 highlighted, output `examples/ex08_menu_board.expected`
- **Narration:** Next, Asha wants a loop of her own in one line. She asks an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex08_menu_board.py`, output `examples/ex08_menu_board.expected`

## Scene 12: Work with AI: six stages, one rewrite

**Section:** Work with AI

**Direction:** Teach the refactoring skill. One conversation per stage, all about rewriting the vegan-tax loop. Generate: the AI drops the filter. Test: two cases fail. Debug: if before for, then every case again. Improve: curly brackets fail every case.

- **Narration:** This chapter's AI skill is safe refactoring. To refactor means to change how code is written, without changing what it does.
  **On screen:** This chapter's AI skill: safe refactoring
    - To **refactor** is to change how code is written, not what it does.
- **Narration:** And you prove it: run both versions on the same data, and compare every line.
  **On screen:** This chapter's AI skill: safe refactoring
    - To **refactor** is to change how code is written, not what it does.
    - Prove it: run both versions on the same data and compare every line.
    - Never paste private data. You are responsible for the code you use.
- **Narration:** Stage 1: plan. Asha's loop adds tax to the vegan items only. Before any rewrite, she asks the AI what the new line must keep exactly the same.
  **On screen:** AI chat, stage 1: Plan: what must stay the same?
    - You: I want to rewrite this loop as one line. Do not write code yet. List what the new line must keep exactly the same. [code `examples/ai_vegan_loop.py`]
- **Narration:** The AI gives a checklist: only vegan items, the same order, the same rounding, and a list. Asha keeps this checklist.
  **On screen:** AI chat, stage 1: Plan: what must stay the same?
    - You: I want to rewrite this loop as one line. Do not write code yet. List what the new line must keep exactly the same. [code `examples/ai_vegan_loop.py`]
    - AI (example answer): 1. Only vegan items: the `if` on line 8. 2. The same order as the menu. 3. Rounding to two decimal places. 4. The result is a list.
- **Narration:** Stage 2: write. Asha wrote the loop herself. She asks the AI to predict its exact output, without running it.
  **On screen:** AI chat, stage 2: Write: predict, then run
    - You: I wrote this loop myself. Do not change it and do not run it. Predict its exact output. [code `examples/ai_vegan_loop.py`]
- **Narration:** The AI predicts 3.85 and 4.4, only Tea and Coffee. Asha predicted the same, and the run agrees.
  **On screen:** AI chat, stage 2: Write: predict, then run
    - You: I wrote this loop myself. Do not change it and do not run it. Predict its exact output. [code `examples/ai_vegan_loop.py`]
    - AI (example answer): It prints `[3.85, 4.4]`. Line 8 keeps only Tea and Coffee, and line 9 adds tax and rounds each price.
    - You: My prediction was the same. I ran it:
- **Narration:** Stage 3: generate. Asha asks the AI to rewrite her loop as a list comprehension, keep the output the same, and say what it prints.
  **On screen:** AI chat, stage 3: Generate: the loop in one line
    - You: Rewrite my loop as a list comprehension. Keep the output exactly the same, and tell me what it prints.
- **Narration:** The AI gives one line, and promises 3.85 and 4.4, the same as the loop.
  **On screen:** AI chat, stage 3: Generate: the loop in one line
    - You: Rewrite my loop as a list comprehension. Keep the output exactly the same, and tell me what it prints.
    - AI (example answer): Here is the one line. It prints `[3.85, 4.4]`, the same as your loop. [code `examples/ai_vegan_flawed.py`]
- **Narration:** Here is the AI's line, on line 6. Compare it with the checklist from stage 1.
  **On screen:** Code `examples/ai_vegan_flawed.py`, line 6 highlighted, output hidden
- **Interaction:** "The AI promises `[3.85, 4.4]`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Point 1 on the checklist was the filter. Line 6 has no if at the end, so it keeps every item.
  **On screen:** Code `examples/ai_vegan_flawed.py`, line 6 highlighted, output `examples/ai_vegan_flawed.expected`
- **Narration:** Asha runs it: four prices instead of two. The cake and the scone got tax too. The AI sounded sure, and it dropped part of her loop.
  **On screen:** Code `examples/ai_vegan_flawed.py`, line 6 highlighted, output `examples/ai_vegan_flawed.expected`
- **Narration:** Stage 4: test. Asha asks for three test cases, with the expected result for each.
  **On screen:** AI chat, stage 4: Test: three cases with expected results
    - You: Give me three test cases with the expected result for each. Use a normal menu and a menu with no vegan items. In the third, two vegan items have the same price.
- **Narration:** A normal menu, a menu with no vegan items, and two vegan items with the same price.
  **On screen:** AI chat, stage 4: Test: three cases with expected results
    - You: Give me three test cases with the expected result for each. Use a normal menu and a menu with no vegan items. In the third, two vegan items have the same price.
    - AI (example answer): 1. Normal: Tea and Scone. Expected `[3.85]`. 2. No vegan: only Scone. Expected `[]`. 3. Same price: Tea and Mint, both 3.5. Expected `[3.85, 3.85]`.
- **Narration:** Lines 2 to 6 keep the three cases in a dictionary: a name, and a small menu for each.
  **On screen:** Code `examples/ai_vegan_cases.py`, line 2, 3, 4, 5, 6 highlighted, output hidden
- **Narration:** For each case, lines 8 to 11 run Asha's loop.
  **On screen:** Code `examples/ai_vegan_cases.py`, line 8, 9, 10, 11 highlighted, output hidden
- **Narration:** Line 12 runs the AI's line. Line 13 uses the same if and else from step 5: it prints pass when both lists are the same, otherwise FAIL.
  **On screen:** Code `examples/ai_vegan_cases.py`, line 12, 13 highlighted, output hidden
- **Interaction:** "Which cases will the AI's line fail?" stays on screen with a 10-second timer.
- **Narration:** The normal menu and the menu with no vegan items. Both get a scone price they should not have.
  **On screen:** Code `examples/ai_vegan_cases.py`, line 12, 13 highlighted, output `examples/ai_vegan_cases.expected`
- **Narration:** The same-price case passes, because both items are vegan. One passing case proves nothing. Run them all.
  **On screen:** Code `examples/ai_vegan_cases.py`, line 12, 13 highlighted, output `examples/ai_vegan_cases.expected`
- **Narration:** Stage 5: debug. Asha tries to add the filter herself, and puts the if before the for. Python stops with a syntax error. She pastes the line and the full error report.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I added the filter myself, but the program stops with this error. First explain the cause. Then show the smallest fix. [code `examples/ai_vegan_typo.py`]
- **Narration:** The AI explains: an if before the for chooses a value for every item, so it needs an else. Remember step 5. To filter, move if vegan to the end.
  **On screen:** AI chat, stage 5: Debug: the AI's answer
    - You: I added the filter myself, but the program stops with this error. First explain the cause. Then show the smallest fix. [code `examples/ai_vegan_typo.py`]
    - AI (example answer): An `if` before the `for` chooses a value for every item, so it needs an `else`. To keep only some items, move `if vegan` to the end, after `in menu`.
- **Narration:** Asha moves the if to the end, on line 12. Then she runs every case again, because a fix can break a case that worked before.
  **On screen:** Code `examples/ai_vegan_cases_fixed.py`, line 12 highlighted, output `examples/ai_vegan_cases_fixed.expected`
- **Narration:** Normal: 3.85, pass. No vegan: an empty list, pass. Same price: pass. All three cases pass.
  **On screen:** Code `examples/ai_vegan_cases_fixed.py`, line 12 highlighted, output `examples/ai_vegan_cases_fixed.expected`
- **Narration:** Stage 6: improve. Asha asks for one change that makes her line better. And she adds: the output must stay exactly the same.
  **On screen:** AI chat, stage 6: Improve: better, but the same?
    - You: My line passes every case. Suggest one change that makes it better, with one reason. The output must stay exactly the same.
- **Narration:** The AI suggests curly brackets, because a set is faster to search. It promises the same output.
  **On screen:** AI chat, stage 6: Improve: better, but the same?
    - You: My line passes every case. Suggest one change that makes it better, with one reason. The output must stay exactly the same.
    - AI (example answer): Use curly brackets instead of square brackets. A set is faster to search, and the output stays the same.
- **Narration:** Asha does not trust it yet. Line 12 now has curly brackets, with no colon. She runs every case.
  **On screen:** Code `examples/ai_vegan_cases_set.py`, line 12 highlighted, output hidden
- **Interaction:** "Will every case still pass?" stays on screen with a 10-second timer.
- **Narration:** No. Every case fails. Curly brackets made a set, and a set is never equal to a list. Set, with empty round brackets, is an empty set.
  **On screen:** Code `examples/ai_vegan_cases_set.py`, line 12 highlighted, output `examples/ai_vegan_cases_set.expected`
- **Narration:** And look at the same-price case: the two equal prices merged into one. A set keeps each value once.
  **On screen:** Code `examples/ai_vegan_cases_set.py`, line 12 highlighted, output `examples/ai_vegan_cases_set.expected`
- **Narration:** The AI broke her rule: the output did not stay the same. Asha keeps her square brackets.
  **On screen:** Code `examples/ai_vegan_cases_set.py`, line 12 highlighted, output `examples/ai_vegan_cases_set.expected`
- **Narration:** Quick check. An AI rewrote your loop as one line. How do you prove the output stayed the same?
  **On screen:** Quick check: "An AI rewrote your loop as one line. How do you prove the output stayed the same?" (options shown)
- **Interaction:** "An AI rewrote your loop as one line. How do you prove the output stayed the same?" stays on screen with a 10-second timer.
- **Narration:** A. Run both versions on the same test cases, and compare every line. A promise is not proof.
  **On screen:** Quick check: "An AI rewrote your loop as one line. How do you prove the output stayed the same?" (answer revealed: Run both on the same test cases.)
- **Narration:** Breather. Asha kept a checklist, ran three cases, and caught two AI mistakes: a missing filter, and curly brackets. Next, the comprehension mistakes beginners make.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Run every case again after a fix.
    - A promise is not proof. A run is.
- **Breather:** 4 quiet seconds.

## Scene 13: Common mistakes

**Section:** Common mistakes

**Direction:** Mistake 1 calls back to the AI's curly brackets. Mistake 2 is a spot-it question on step 5. Mistake 3 teaches that print gives back None, then asks. Mistake 4 calls back to Chapter 2's float error.

- **Narration:** Mistake 1 is the AI's improvement. Curly brackets with no colon make a set comprehension. Line 4 shows the type: set.
  **On screen:** Code `examples/err01_braces.py`, line 3, 4 highlighted, output `examples/err01_braces.expected`
- **Narration:** A set has no fixed order, so line 5 prints it sorted. There is no error. But the list had 3.5 twice, and the set kept 3.85 only once: 3 items instead of 4.
  **On screen:** Code `examples/err01_braces.py`, line 5, 6 highlighted, output `examples/err01_braces.expected`
- **Narration:** The fix: square brackets for a list. Curly brackets with key, colon, value for a dictionary.
  **On screen:** Code `examples/err01_braces.py`, line 5, 6 highlighted, output `examples/err01_braces.expected`
- **Narration:** Now you try. Look closely at line 3, and remember step 5.
  **On screen:** Code `examples/err02_else_at_end.py`, line 3 highlighted, output hidden
- **Interaction:** "What is wrong with line 3?" stays on screen with a 10-second timer.
- **Narration:** A filter at the end cannot have an else. Python stops with a syntax error on line 3.
  **On screen:** Code `examples/err02_else_at_end.py`, line 3 highlighted, error `examples/err02_else_at_end.expected_error`
- **Narration:** The fix: to choose a value for every item, move the if and else to the start. To filter, remove the else.
  **On screen:** Code `examples/err02_else_at_end.py`, line 3 highlighted, error `examples/err02_else_at_end.expected_error`
- **Narration:** Mistake 3. Print shows text on the screen, but it gives back nothing. Python calls that nothing None.
  **On screen:** Code `examples/err03_print_comp.py`, line 3 highlighted, output hidden
- **Narration:** Line 3 builds a list from three calls to print. Line 4 prints that list.
  **On screen:** Code `examples/err03_print_comp.py`, line 3, 4 highlighted, output hidden
- **Interaction:** "What does line 4 print?" stays on screen with a 10-second timer.
- **Narration:** None, None, None. The names were printed, but the list is useless.
  **On screen:** Code `examples/err03_print_comp.py`, line 4 highlighted, output `examples/err03_print_comp.expected`
- **Narration:** The fix: when the job is printing, use a normal for loop.
  **On screen:** Code `examples/err03_print_comp.py`, line 4 highlighted, output `examples/err03_print_comp.expected`
- **Narration:** Mistake 4. Line 3 adds tax with no round. Remember Chapter 2: some floats are stored with a tiny error.
  **On screen:** Code `examples/ex09_no_round.py`, line 3 highlighted, output `examples/ex09_no_round.expected`
- **Narration:** The fix: round inside the comprehension, as line 5 does. Or format the price with two decimal places when you print it.
  **On screen:** Code `examples/ex09_no_round.py`, line 5 highlighted, output `examples/ex09_no_round.expected`
- **Narration:** Last breather. Now you know the four comprehension mistakes that catch most beginners.
  **On screen:** Breather card
    - Square brackets for a list.
    - No `else` after a filter.
    - Use a loop to print.
- **Breather:** 4 quiet seconds.

## Scene 14: Think beyond

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Asha has five orders. Write a comprehension that keeps only the teas, then count them. Could you count them without making a new list?
  **On screen:** Question card: "`orders = ["tea", "cake", "tea", "scone", "tea"]`. Keep only the teas, then count them. Could you count without a new list?"
- **Interaction:** "`orders = ["tea", "cake", "tea", "scone", "tea"]`. Keep only the teas, then count them. Could you count without a new list?" stays on screen with a 10-second timer.
- **Narration:** Write it after the video, and run it.
  **On screen:** Question card: "`orders = ["tea", "cake", "tea", "scone", "tea"]`. Keep only the teas, then count them. Could you count without a new list?"
- **Narration:** Second. A comprehension can have two for parts, such as every size of every drink. Predict the order of the items, then run it.
  **On screen:** Question card: "`[size + " " + drink for drink in drinks for size in sizes]` with drinks tea and coffee, and sizes small and large. In what order do the items come?"
- **Interaction:** "`[size + " " + drink for drink in drinks for size in sizes]` with drinks tea and coffee, and sizes small and large. In what order do the items come?" stays on screen with a 10-second timer.
- **Narration:** Compare your prediction with the real output.
  **On screen:** Question card: "`[size + " " + drink for drink in drinks for size in sizes]` with drinks tea and coffee, and sizes small and large. In what order do the items come?"

## Scene 15: Recap

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap. A list comprehension: the new value, then for, then an optional if.
  **On screen:** Recap
    - A list comprehension: the new value, then `for`, then an optional `if`.
- **Narration:** An if at the end filters. An if and else at the start chooses a value for every item.
  **On screen:** Recap
    - A list comprehension: the new value, then `for`, then an optional `if`.
    - An `if` at the end filters. `if ... else` at the start chooses a value for every item.
- **Narration:** Curly brackets with a colon build a dictionary. And the old collection never changes.
  **On screen:** Recap
    - A list comprehension: the new value, then `for`, then an optional `if`.
    - An `if` at the end filters. `if ... else` at the start chooses a value for every item.
    - `{key: value for ...}` builds a dictionary. Curly brackets without a colon build a set.
    - A comprehension makes a new collection. The old one does not change.
- **Narration:** Use a loop for several steps, and with AI, run both versions on the same cases.
  **On screen:** Recap
    - A list comprehension: the new value, then `for`, then an optional `if`.
    - An `if` at the end filters. `if ... else` at the start chooses a value for every item.
    - `{key: value for ...}` builds a dictionary. Curly brackets without a colon build a set.
    - A comprehension makes a new collection. The old one does not change.
    - Use a normal loop for several steps, a `print()` or a running total.
    - Refactor with AI, then run both versions on the same cases.
- **Narration:** One last check. What does this comprehension give?
  **On screen:** Quick check: "What does `[n * 2 for n in [1, 2, 3] if n > 1]` give?" (options shown)
- **Interaction:** "What does `[n * 2 for n in [1, 2, 3] if n > 1]` give?" stays on screen with a 10-second timer.
- **Narration:** D. 4 and 6. The filter keeps 2 and 3, and the new value doubles each one.
  **On screen:** Quick check: "What does `[n * 2 for n in [1, 2, 3] if n > 1]` give?" (answer revealed: `[4, 6]`)
- **Narration:** Mission complete! You earned 100 XP and the Transformer badge.
  **On screen:** Transformer You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 16: Practice

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn: eight tasks, worth 170 XP. Three warm-up tasks at 10 XP, and three apply tasks at 20, including a stock check.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each: a vegan menu board, and an AI's refactor to check. Try each one before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 17: What's next

**Section:** What's next

**Direction:** End card. Tease Boss Level 3: the expense tracker that combines everything in Module 3. Hold quietly at the end.

- **Narration:** Asha now knows lists, dictionaries, tuples, sets and comprehensions. But every day, she still adds up the Corner Cafe's costs on paper: milk, cups, tea leaves.
  **On screen:** Boss Level 3: The Expense Tracker Lists, dictionaries, loops and decisions, together.
- **Narration:** In Chapter 15, Boss Level 3, you will build an expense tracker that does it for her.
  **On screen:** Boss Level 3: The Expense Tracker Lists, dictionaries, loops and decisions, together.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Boss Level 3: The Expense Tracker Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 15.
  **On screen:** Boss Level 3: The Expense Tracker Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
