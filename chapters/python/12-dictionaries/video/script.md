# Video Script: Chapter 12: Dictionaries: Looking Things Up by Name

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:10.

## Scene 1: Introduction (0:00 to 0:52)

**Section:** Introduction

**Direction:** Open on the problem: a customer asks for a price by name, and a list can only answer by position. Then the title with the AI tease, then the order taker as the mission.

- **Narration:** A customer at the Corner Cafe asks Asha: how much is the cake? Her menu is two lists from Chapter 11. One holds the names, and one holds the prices, in the same order.
  **On screen:** "How much is the cake?"
    - Asha's menu is two lists: names, and prices in the same order.
- **Narration:** To find the price, she must first find where cake is, then read the same position in the second list. But customers never ask for item number 2. They ask by name.
  **On screen:** "How much is the cake?"
    - Asha's menu is two lists: names, and prices in the same order.
    - To find the price of cake, she must first find where cake is.
    - Customers never ask for item number 2. They ask by name.
- **Narration:** This is Code Quest, Chapter 12. Today you learn dictionaries. They find a value by its name.
  **On screen:** Dictionaries: Looking Things Up by Name
- **Narration:** And an AI assistant will promise one thing, and print another. You will catch it.
  **On screen:** Dictionaries: Looking Things Up by Name Ask by name. Get the value.
- **Narration:** So here is today's mission. Line 2 holds the whole menu in one dictionary: every price under its name.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 2 highlighted, output hidden
- **Narration:** The customer types each item by name, and the program counts the order in a second dictionary.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 3, 4, 5, 8, 9 highlighted, output hidden
- **Narration:** Then it prints a receipt with the total. Let's build it.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 13, 16, 17 highlighted, output hidden

## Scene 2: Learning goals (0:52 to 1:03)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Read any value by its key, and add, change or remove items.
  **On screen:** By the end, you will be able to:
    - Write a dictionary and read a value with its key.
    - Add, change and remove items in a dictionary.
- **Narration:** And choose between a list and a dictionary, even when an AI chooses differently.
  **On screen:** By the end, you will be able to:
    - Write a dictionary and read a value with its key.
    - Add, change and remove items in a dictionary.
    - Check for a key with `in`, and use `get()` with a default value.
    - Go through a dictionary with `items()`, and count things with one.
    - Choose between a list and a dictionary, and challenge an AI's choice.

## Scene 3: Why this matters (1:03 to 1:19)

**Section:** Why this matters

**Direction:** Define a dictionary and a key through the price question, then connect it to apps the learner uses.

- **Narration:** A dictionary stores each value under a name, called a key. You ask for the key, and Python gives you the value.
  **On screen:** Why this matters
    - A **dictionary** stores each value under a name, called a **key**.
    - You ask for the key, and Python gives you the value: `menu["cake"]`.
- **Narration:** Your phone finds a number by a contact's name. A shop finds a product by its code. A game finds your score by your name.
  **On screen:** Why this matters
    - A **dictionary** stores each value under a name, called a **key**.
    - You ask for the key, and Python gives you the value: `menu["cake"]`.
    - A phone's contacts, a shop's product codes, a game's scores: each one finds a value by name.

## Scene 4: The idea: keys and values (1:19 to 2:27)

**Section:** The idea

**Direction:** Teach curly brackets, key, colon, value and the one-key rule with the diagram. Then a quiz and a breather.

- **Narration:** A dictionary is written with curly brackets. Each item is a key, a colon, and a value. Commas separate the items.
  **On screen:** Each key points to a value
- **Narration:** Here, the key tea points to 3.5, and the key cake points to 4.25. Menu, cake in square brackets, gives 4.25.
  **On screen:** Each key points to a value
- **Narration:** A value can be any type, even another dictionary. Python keeps the items in the order you added them.
  **On screen:** Each key points to a value
- **Narration:** And each key appears only once. Like a name on the price board, but stricter: add a key that already exists, and the new value replaces the old one.
  **On screen:** Each key points to a value
- **Narration:** Quick check. In this dictionary, what is the word cake?
  **On screen:** Quick check: "In `{"tea": 3.5, "cake": 4.25}`, what is `"cake"`?" (options shown)
- **Interaction:** "In `{"tea": 3.5, "cake": 4.25}`, what is `"cake"`?" stays on screen with a 10-second timer.
- **Narration:** C. A key. The part before the colon is the key, and 4.25 is its value.
  **On screen:** Quick check: "In `{"tea": 3.5, "cake": 4.25}`, what is `"cake"`?" (answer revealed: A key)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - A dictionary stores values under keys.
    - Ask for the key, get the value.
    - Each key appears only once.
- **Narration:** Next, Asha writes the menu as a dictionary.
  **On screen:** Breather card
    - A dictionary stores values under keys.
    - Ask for the key, get the value.
    - Each key appears only once.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Make a dictionary and read values (2:27 to 3:08)

**Section:** Build it step by step

**Direction:** The file types itself in. Teach square brackets with a key, then ask what lines 4 and 5 print.

- **Narration:** Step 1. Asha writes part of the menu: tea, coffee and cake, each with its price.
  **On screen:** Code `examples/ex01_menu.py`, lines 1 to 3 typed in, line 2 highlighted, output hidden
- **Narration:** Line 3 prints the whole dictionary.
  **On screen:** Code `examples/ex01_menu.py`, lines 1 to 3 typed in, line 3 highlighted, output hidden
- **Narration:** Lines 4 and 5 read one value each. Square brackets again, but with a key inside, not an index.
  **On screen:** Code `examples/ex01_menu.py`, lines 1 to 5 typed in, line 4, 5 highlighted, output hidden
- **Narration:** And line 6 uses len. For a dictionary, it counts the key and value pairs.
  **On screen:** Code `examples/ex01_menu.py`, lines 1 to 6 typed in, line 6 highlighted, output hidden
- **Interaction:** "What do lines 4 and 5 print?" stays on screen with a 10-second timer.
- **Narration:** 3.5, the price of tea, and 4.25, the price of cake.
  **On screen:** Code `examples/ex01_menu.py`, lines 1 to 6 typed in, line 4, 5 highlighted, output `examples/ex01_menu.expected`
- **Narration:** And len gives 3: three keys, each with its value.
  **On screen:** Code `examples/ex01_menu.py`, lines 1 to 6 typed in, line 6 highlighted, output `examples/ex01_menu.expected`

## Scene 6: Step 2: Add, change and remove (3:08 to 4:09)

**Section:** Build it step by step

**Direction:** Teach the four changes with the table, then the code. Ask what line 5 does to tea, then reveal.

- **Narration:** Step 2. A dictionary can change, like a list. A key in square brackets, with an equals sign and a value, adds a new key.
  **On screen:** Table: Step 2: Four ways to change a dictionary (row 1 in focus)
- **Narration:** The same line changes the value when the key already exists.
  **On screen:** Table: Step 2: Four ways to change a dictionary (row 2 in focus)
- **Narration:** The word del removes a key and its value.
  **On screen:** Table: Step 2: Four ways to change a dictionary (row 3 in focus)
- **Narration:** And pop removes a key, and gives its value back to you.
  **On screen:** Table: Step 2: Four ways to change a dictionary (row 4 in focus)
- **Narration:** Line 3 adds a scone at 2.75. Scone is a new key, so the menu gets a fourth item.
  **On screen:** Code `examples/ex02_change_menu.py`, line 3 highlighted, output hidden
- **Narration:** Line 5 uses the same kind of line, with the key tea and the value 3.75.
  **On screen:** Code `examples/ex02_change_menu.py`, line 5 highlighted, output hidden
- **Interaction:** "Does line 5 add a second tea, or change the price of tea?" stays on screen with a 10-second timer.
- **Narration:** It changes the price. Tea is already a key, and each key appears only once.
  **On screen:** Code `examples/ex02_change_menu.py`, line 5 highlighted, output `examples/ex02_change_menu.expected`
- **Narration:** Line 7 deletes coffee.
  **On screen:** Code `examples/ex02_change_menu.py`, line 7 highlighted, output `examples/ex02_change_menu.expected`
- **Narration:** And line 9 pops cake. The value, 4.25, goes into price, and line 10 prints it before the smaller menu.
  **On screen:** Code `examples/ex02_change_menu.py`, line 9, 10 highlighted, output `examples/ex02_change_menu.expected`

## Scene 7: Step 3: Check before you look up (4:09 to 4:56)

**Section:** Build it step by step

**Direction:** Teach that a missing key stops the program, then in on keys and get() with a default. Ask about line 5, then reveal.

- **Narration:** Step 3. If you ask for a key that is not there, the program stops. So Python gives you two safe ways to check.
  **On screen:** Code `examples/ex03_lookups.py`, line 3, 4 highlighted, output hidden
- **Narration:** The word in checks whether a key is in the dictionary. It checks the keys only, never the values.
  **On screen:** Code `examples/ex03_lookups.py`, line 3, 4, 5 highlighted, output hidden
- **Narration:** And get gives the value if the key exists. If it does not, get gives None, or the default value you put second.
  **On screen:** Code `examples/ex03_lookups.py`, line 6, 7, 8 highlighted, output hidden
- **Interaction:** "What does line 5 print?" stays on screen with a 10-second timer.
- **Narration:** False. 3.5 is a value, not a key, and in checks the keys only.
  **On screen:** Code `examples/ex03_lookups.py`, line 5 highlighted, output `examples/ex03_lookups.expected`
- **Narration:** Line 6 gets the price of cake. Line 7 asks for juice and gets None. Line 8 gives a default, so it gets 0.
  **On screen:** Code `examples/ex03_lookups.py`, line 6, 7, 8 highlighted, output `examples/ex03_lookups.expected`

## Scene 8: Step 4: Go through a dictionary (4:56 to 5:52)

**Section:** Build it step by step

**Direction:** Teach that a for loop gives keys, and items() gives pairs. Ask names or prices for lines 3 and 4, then reveal.

- **Narration:** Step 4. A for loop over a dictionary goes through its keys, one at a time. So lines 3 and 4 print the names.
  **On screen:** Code `examples/ex04_loop_menu.py`, line 3, 4 highlighted, output hidden
- **Narration:** To get each key together with its value, use items. Line 5 takes two loop variables, name and price.
  **On screen:** Code `examples/ex04_loop_menu.py`, line 5, 6 highlighted, output hidden
- **Narration:** Keys and values give the keys or the values on their own. List turns them into lists so they print clearly.
  **On screen:** Code `examples/ex04_loop_menu.py`, line 7, 8 highlighted, output hidden
- **Narration:** And sum adds the values.
  **On screen:** Code `examples/ex04_loop_menu.py`, line 9 highlighted, output hidden
- **Interaction:** "What do lines 5 and 6 print?" stays on screen with a 10-second timer.
- **Narration:** Each name with its price, lined up with the codes from Chapter 3: tea 3.50, coffee 4.00, cake 4.25.
  **On screen:** Code `examples/ex04_loop_menu.py`, line 5, 6 highlighted, output `examples/ex04_loop_menu.expected`
- **Narration:** And lines 3 and 4 printed the names only. A loop over a dictionary gives its keys. Remember this one.
  **On screen:** Code `examples/ex04_loop_menu.py`, line 3, 4 highlighted, output `examples/ex04_loop_menu.expected`
- **Narration:** Then the keys, the values, and their sum: 11.75.
  **On screen:** Code `examples/ex04_loop_menu.py`, line 7, 8, 9 highlighted, output `examples/ex04_loop_menu.expected`

## Scene 9: Steps 5 and 6: Count, then nest (5:52 to 7:11)

**Section:** Build it step by step

**Direction:** Walk the counting line slowly, then ask what line 6 prints. Then nested data and a breather.

- **Narration:** Step 5. Asha wants to know how many of each item she sold today. Line 2 lists the sales. Line 3 starts an empty dictionary: two curly brackets.
  **On screen:** Code `examples/ex05_count_sales.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 5 does the counting. Get gives the count so far, or 0 the first time an item appears.
  **On screen:** Code `examples/ex05_count_sales.py`, line 4, 5 highlighted, output hidden
- **Narration:** Python works out the right side first, adds 1, and stores the new count under the item's name.
  **On screen:** Code `examples/ex05_count_sales.py`, line 5 highlighted, output hidden
- **Interaction:** "What does line 6 print?" stays on screen with a 10-second timer.
- **Narration:** Tea 3, cake 2, scone 1. Each name appears once, with its count.
  **On screen:** Code `examples/ex05_count_sales.py`, line 6 highlighted, output `examples/ex05_count_sales.expected`
- **Narration:** And line 7 reads one count by its name: 3 teas.
  **On screen:** Code `examples/ex05_count_sales.py`, line 7 highlighted, output `examples/ex05_count_sales.expected`
- **Narration:** Step 6. A value can be another dictionary. Here, each item has a price and a vegan flag. This is called nested data.
  **On screen:** Code `examples/ex06_nested_menu.py`, line 2, 3, 4, 5, 6 highlighted, output `examples/ex06_nested_menu.expected`
- **Narration:** Line 7 reads it in two steps: menu cake gives the inner dictionary, and price reads one value from it.
  **On screen:** Code `examples/ex06_nested_menu.py`, line 7 highlighted, output `examples/ex06_nested_menu.expected`
- **Narration:** The loop prints only the vegan items. Inside the f-string on line 10, the key uses single quotation marks, because the f-string uses double ones.
  **On screen:** Code `examples/ex06_nested_menu.py`, line 8, 9, 10 highlighted, output `examples/ex06_nested_menu.expected`
- **Narration:** Breather. You now have every piece of the mission. Let's put them together.
  **On screen:** Breather card
    - `in` and `get()` check before you look up.
    - A loop over a dictionary gives its keys.
    - `get(item, 0) + 1` counts by name.
- **Breather:** 4 quiet seconds.

## Scene 10: See the outcome: the order taker (7:11 to 8:17)

**Section:** See the outcome

**Direction:** Return to the mission. Walk every line, ask about the order dictionary, reveal. Hand over to the stock feature.

- **Narration:** Back to the mission. Line 2 is the menu. Line 3 starts an empty order.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 2, 3 highlighted, output hidden
- **Narration:** The loop asks for items until the customer types done. Line 5 removes spaces and capital letters, so Tea and tea both find tea.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 4, 5, 6, 7 highlighted, output hidden
- **Narration:** Line 8 checks the menu before anything is looked up. A known item is counted on line 9. Anything else gets a polite message on line 11.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 8, 9, 10, 11 highlighted, output hidden
- **Narration:** Then lines 12 to 17 go through the order with items, work out each cost, add up the total and print the receipt.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 12, 13, 14, 15, 16, 17 highlighted, output hidden
- **Interaction:** "The customer types Tea, cake, juice, then " tea" with a space, then done. How many teas does the order hold?" stays on screen with a 10-second timer.
- **Narration:** Two. Capital Tea and tea with a space both become tea, so line 9 counts it twice.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 5, 9 highlighted, output `examples/ex07_order_by_name.expected`
- **Narration:** Juice is not on the menu. Line 11 prints a polite message, and nothing stops.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 10, 11 highlighted, output `examples/ex07_order_by_name.expected`
- **Narration:** The total is 11.25. Mission complete! Next, Asha tracks the cafe's stock with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex07_order_by_name.py`, line 17 highlighted, output `examples/ex07_order_by_name.expected`

## Scene 11: Work with AI: six stages, one stock tracker (8:17 to 13:36)

**Section:** Work with AI

**Direction:** Teach the challenge-the-design skill. One conversation per stage, all about the stock. Plan: two lists, challenged. Generate: names not numbers. Test: the muffin KeyError. Debug, then every case again. Improve: a get() suggestion that adds a line.

- **Narration:** This chapter's AI skill is challenging a design. Ask AI how to store your data, and why. Then compare its answer with the job, and keep the safety habits.
  **On screen:** This chapter's AI skill: challenge the design
    - Ask AI how to store your data, and ask why.
    - Compare its answer with the job: will you look things up by name?
    - Never paste private data. You are responsible for the code you use.
- **Narration:** Stage 1: plan. Asha describes her stock: 6 cakes, 4 scones and 5 sandwiches. She finds items by name, and takes one away when it sells.
  **On screen:** AI chat, stage 1: Plan: ask for a design
    - You: I am a beginner. I need to store how many cakes, scones and sandwiches are left: 6, 4 and 5. When one sells, I find it by its name and take one away. Do not write code yet. Suggest a data structure and say why.
- **Narration:** The AI suggests two lists: one for the names, one for the counts. To sell a cake, find its position first.
  **On screen:** AI chat, stage 1: Plan: ask for a design
    - You: I am a beginner. I need to store how many cakes, scones and sandwiches are left: 6, 4 and 5. When one sells, I find it by its name and take one away. Do not write code yet. Suggest a data structure and say why.
    - AI (example answer): Use two lists: `items = ["cake", "scone", "sandwich"]` and `counts = [6, 4, 5]`. To sell one, find the item's position in `items`, then change `counts` at the same position.
- **Narration:** That is the problem from the start of this video. So Asha challenges it: I always look items up by name. Why not a dictionary?
  **On screen:** AI chat, stage 1: Plan: challenge the design
    - You: You suggested two lists. But I always look items up by name, never by position. Why not a dictionary?
- **Narration:** The AI agrees. A dictionary finds the count directly, by name.
  **On screen:** AI chat, stage 1: Plan: challenge the design
    - You: You suggested two lists. But I always look items up by name, never by position. Why not a dictionary?
    - AI (example answer): You are right. A dictionary fits better: `stock = {"cake": 6, "scone": 4, "sandwich": 5}`. `stock["cake"]` finds the count directly, with no position to search for.
- **Narration:** Stage 2: write. Asha writes the first lines herself, and asks the AI to explain line 3 with her own dictionary.
  **On screen:** AI chat, stage 2: Write: a worked example of one line
    - You: I wrote these lines myself. Explain line 3 step by step, with my dictionary as a worked example. Show the dictionary before and after. Do not change my code. [code `examples/ai_stock_write.py`]
- **Narration:** The AI explains: the right side first, 6 minus 1 is 5, then 5 is stored under cake.
  **On screen:** AI chat, stage 2: Write: a worked example of one line
    - You: I wrote these lines myself. Explain line 3 step by step, with my dictionary as a worked example. Show the dictionary before and after. Do not change my code. [code `examples/ai_stock_write.py`]
    - AI (example answer): Python works out the right side first: `stock["cake"]` is 6, and 6 - 1 is 5. Then it stores 5 under the key `"cake"`. Before: cake 6, scone 4, sandwich 5. After: cake 5, scone 4, sandwich 5.
- **Narration:** She runs it. The worked example matches the run.
  **On screen:** AI chat, stage 2: Write: a worked example of one line
    - You: I wrote these lines myself. Explain line 3 step by step, with my dictionary as a worked example. Show the dictionary before and after. Do not change my code. [code `examples/ai_stock_write.py`]
    - AI (example answer): Python works out the right side first: `stock["cake"]` is 6, and 6 - 1 is 5. Then it stores 5 under the key `"cake"`. Before: cake 6, scone 4, sandwich 5. After: cake 5, scone 4, sandwich 5.
    - You: I ran it. Your worked example was right:
- **Narration:** Stage 3: generate. Asha sold a cake, a scone and another cake. She asks for code that prints how many of each are left, and the exact output.
  **On screen:** AI chat, stage 3: Generate: how many are left?
    - You: Today I sold a cake, a scone and another cake. Write code that takes the sales away from my stock and prints how many of each item are left. Show the exact output.
- **Narration:** The AI promises: Left 4, Left 3, Left 5. Look at line 6.
  **On screen:** AI chat, stage 3: Generate: how many are left?
    - You: Today I sold a cake, a scone and another cake. Write code that takes the sales away from my stock and prints how many of each item are left. Show the exact output.
    - AI (example answer): Here it is. It prints `Left: 4`, `Left: 3` and `Left: 5`. [code `examples/ai_stock_flawed.py`]
- **Interaction:** "The AI promises `Left: 4`, `Left: 3` and `Left: 5`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Remember step 4: a loop over a dictionary gives its keys. The variable is called count, but it holds the names.
  **On screen:** AI chat, stage 3: Generate: how many are left?
    - You: Today I sold a cake, a scone and another cake. Write code that takes the sales away from my stock and prints how many of each item are left. Show the exact output.
    - AI (example answer): Here it is. It prints `Left: 4`, `Left: 3` and `Left: 5`. [code `examples/ai_stock_flawed.py`]
- **Narration:** Asha runs it. Left cake. Left scone. Left sandwich. A name for a variable does not change what Python puts in it.
  **On screen:** Code `examples/ai_stock_flawed.py`, line 6, 7 highlighted, output `examples/ai_stock_flawed.expected`
- **Narration:** Stage 4: test. Asha asks for a fix, and three test cases with expected outputs. Each case starts with 2 cakes, and one sells a muffin, which is not in her stock.
  **On screen:** AI chat, stage 4: Test: the fix, and three cases
    - You: It printed the names, not the numbers. Fix it so each line shows the item and its count. Then give me three test cases, each starting with 2 cakes, with the exact expected output: no sales, selling the last two cakes, and selling a cake and a muffin. Muffins are not in my stock.
- **Narration:** The fix uses items. And for the muffin, the AI predicts: the muffin is ignored.
  **On screen:** AI chat, stage 4: Test: the fix, and three cases
    - You: It printed the names, not the numbers. Fix it so each line shows the item and its count. Then give me three test cases, each starting with 2 cakes, with the exact expected output: no sales, selling the last two cakes, and selling a cake and a muffin. Muffins are not in my stock.
    - AI (example answer): Use `items()` to get each name with its count. 1. No sales: 2, 4 and 5 left. 2. The last two cakes: cake: 0 left. 3. A cake and a muffin: the muffin is ignored, and the counts are printed as normal. [code `examples/ai_stock_fixed.py`]
- **Interaction:** "The AI says a muffin sale is ignored. Is it right?" stays on screen with a 10-second timer.
- **Narration:** The program stops. Remember step 3: asking for a key that is not there stops the program.
  **On screen:** AI chat, stage 4: Test: the fix, and three cases
    - You: It printed the names, not the numbers. Fix it so each line shows the item and its count. Then give me three test cases, each starting with 2 cakes, with the exact expected output: no sales, selling the last two cakes, and selling a cake and a muffin. Muffins are not in my stock.
    - AI (example answer): Use `items()` to get each name with its count. 1. No sales: 2, 4 and 5 left. 2. The last two cakes: cake: 0 left. 3. A cake and a muffin: the muffin is ignored, and the counts are printed as normal. [code `examples/ai_stock_fixed.py`]
- **Narration:** First, Asha runs the AI's fix on today's sales. Cake 4, scone 3, sandwich 5. Now each line shows a name and a number.
  **On screen:** Code `examples/ai_stock_fixed.py`, line 6, 7 highlighted, output `examples/ai_stock_fixed.expected`
- **Narration:** Then the cases. For each one, she sets cake to 2. No sales: 2, 4 and 5 left, as expected. Pass.
  **On screen:** Code `examples/ai_case_none_sold.py`, line 2, 3 highlighted, output `examples/ai_case_none_sold.expected`
- **Narration:** The last two cakes: cake, 0 left. Pass.
  **On screen:** Code `examples/ai_case_last_cake.py`, line 2, 3 highlighted, output `examples/ai_case_last_cake.expected`
- **Narration:** Case 3, a cake and a muffin, stops with a Key Error: muffin. Two cases pass, and one fails. The AI's prediction was wrong, and only the run showed it.
  **On screen:** Table: Three cases on the AI's fix (row 3 in focus)
- **Narration:** Stage 5: debug. Asha pastes the code and the full error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: The muffin case stopped with this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_case_muffin.py`]
- **Narration:** The AI names line 5: the key muffin is not in the dictionary. The smallest fix: check with in first, and print a message for anything else.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: The muffin case stopped with this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_case_muffin.py`]
    - AI (example answer): Line 5 is the cause. `stock["muffin"]` asks for a key that is not in the dictionary, so Python raises a `KeyError`. The smallest fix: check with `if item in stock:` first, and print a message for anything else.
- **Narration:** A fix can break a case that worked before. So Asha runs all three cases again with the check. Lines 2 to 6 keep the cases in a dictionary: each name points to a list of sales.
  **On screen:** Code `examples/ai_stock_regression.py`, line 2, 3, 4, 5, 6 highlighted, output `examples/ai_stock_regression.expected`
- **Narration:** Line 9 resets the stock to 2 cakes at the start of each case. No sales: 2, 4 and 5 left. Pass.
  **On screen:** Code `examples/ai_stock_regression.py`, line 7, 8, 9 highlighted, output `examples/ai_stock_regression.expected`
- **Narration:** The last two cakes: cake, 0 left. Pass.
  **On screen:** Code `examples/ai_stock_regression.py`, line 11, 12 highlighted, output `examples/ai_stock_regression.expected`
- **Narration:** And the muffin: a message, and the other counts are right. Pass. All three cases pass.
  **On screen:** Code `examples/ai_stock_regression.py`, line 13, 14 highlighted, output `examples/ai_stock_regression.expected`
- **Narration:** Stage 6: improve. Asha asks for one change that makes the code shorter. And she adds: the output must stay exactly the same.
  **On screen:** AI chat, stage 6: Improve: shorter, but the same?
    - You: My stock program works for every case. Suggest one change that makes it shorter, with one reason. The output must stay exactly the same.
- **Narration:** The AI suggests one line with get and a default of 0, so the check is not needed. It says the output stays the same.
  **On screen:** AI chat, stage 6: Improve: shorter, but the same?
    - You: My stock program works for every case. Suggest one change that makes it shorter, with one reason. The output must stay exactly the same.
    - AI (example answer): Replace the `if` and `else` with one line: `stock[item] = stock.get(item, 0) - 1`. `get()` never stops the program, so you do not need the check. The output stays the same.
- **Narration:** Asha tests it with the muffin case. Line 5 gets the muffin's count, or 0, and takes one away.
  **On screen:** Code `examples/ai_stock_suggest.py`, line 5 highlighted, output hidden
- **Interaction:** "Asha said: the output must stay the same. Does the suggestion keep that promise?" stays on screen with a 10-second timer.
- **Narration:** No. Get gives 0 for the muffin, minus 1 makes minus 1, and line 5 adds a new key. The output gains a line: muffin, minus 1 left.
  **On screen:** Code `examples/ai_stock_suggest.py`, line 5 highlighted, output `examples/ai_stock_suggest.expected`
- **Narration:** A stock of minus one muffin makes no sense, and the AI ignored her instruction. Asha keeps her check.
  **On screen:** Code `examples/ai_stock_suggest.py`, line 5 highlighted, output `examples/ai_stock_suggest.expected`
- **Narration:** Quick check. An AI designs your data as two lists, but you always look items up by name. What do you do?
  **On screen:** Quick check: "An AI designs your data as two lists, but you always look items up by name. What do you do?" (options shown)
- **Interaction:** "An AI designs your data as two lists, but you always look items up by name. What do you do?" stays on screen with a 10-second timer.
- **Narration:** A. Ask why, and suggest a dictionary. Challenge every design against the job it must do.
  **On screen:** Quick check: "An AI designs your data as two lists, but you always look items up by name. What do you do?" (answer revealed: Ask why, and suggest a dictionary)
- **Narration:** Breather. Asha challenged a design, and caught three AI mistakes: names instead of numbers, a crash it did not predict, and a change that broke her rule. Next, the mistakes beginners make with dictionaries.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - A loop over a dictionary gives its keys.
    - A prediction is not a test. The run is.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes (13:36 to 15:35)

**Section:** Common mistakes

**Direction:** Mistake 1 shows the KeyError. Mistake 2 is a spot-it on get() with a capital letter. Mistake 3 is a spot-it on a repeated key. Mistake 4 calls back to the AI's loop.

- **Narration:** Mistake 1. Line 3 prints the price of tea.
  **On screen:** Code `examples/err01_missing_key.py`, line 3 highlighted, error `examples/err01_missing_key.expected_error`
- **Narration:** Line 4 asks for juice, which is not a key. Python stops with a Key Error, and names the missing key.
  **On screen:** Code `examples/err01_missing_key.py`, line 4 highlighted, error `examples/err01_missing_key.expected_error`
- **Narration:** The fix: check with in first, or use get with a default when a default makes sense.
  **On screen:** Code `examples/err01_missing_key.py`, line 4 highlighted, error `examples/err01_missing_key.expected_error`
- **Narration:** Now you try. Line 3 uses get to find the price of tea, with a capital T. Keys are case-sensitive: capital T and small t make different keys.
  **On screen:** Code `examples/err02_get_none.py`, line 3 highlighted, output hidden
- **Interaction:** "What does line 4 print?" stays on screen with a 10-second timer.
- **Narration:** None. Capital Tea is not a key, so get gives None. Get did not stop the program on line 3.
  **On screen:** Code `examples/err02_get_none.py`, line 3, 4 highlighted, error `examples/err02_get_none.expected_error`
- **Narration:** But line 5 tries to multiply None, and the program stops there with a Type Error.
  **On screen:** Code `examples/err02_get_none.py`, line 5 highlighted, error `examples/err02_get_none.expected_error`
- **Narration:** The fix: use lower on names before you look them up, and check what get gives you.
  **On screen:** Code `examples/err02_get_none.py`, line 5 highlighted, error `examples/err02_get_none.expected_error`
- **Narration:** One more. Line 2 writes tea twice: once at 3.5, and once at 3.0. Remember the one-key rule from the idea section.
  **On screen:** Code `examples/ex08_duplicate_key.py`, line 2 highlighted, output hidden
- **Interaction:** "How many items does line 4 count?" stays on screen with a 10-second timer.
- **Narration:** Two. Each key appears only once, so the second tea replaced the first, with no error.
  **On screen:** Code `examples/ex08_duplicate_key.py`, line 2 highlighted, output `examples/ex08_duplicate_key.expected`
- **Narration:** The fix: check that every key in a dictionary is different.
  **On screen:** Code `examples/ex08_duplicate_key.py`, line 2 highlighted, output `examples/ex08_duplicate_key.expected`
- **Narration:** Mistake 4 is the AI's mistake from stage 3. Line 4 loops over the menu, and expects prices.
  **On screen:** Code `examples/err03_loop_keys.py`, line 4, 5 highlighted, error `examples/err03_loop_keys.expected_error`
- **Narration:** But price holds the key tea, a string. Python cannot add a string to a number, so it stops with a Type Error.
  **On screen:** Code `examples/err03_loop_keys.py`, line 4, 5 highlighted, error `examples/err03_loop_keys.expected_error`
- **Narration:** The fix: loop over menu dot values, or use items when you need both.
  **On screen:** Code `examples/err03_loop_keys.py`, line 4, 5 highlighted, error `examples/err03_loop_keys.expected_error`
- **Narration:** Last breather. Now you know the four dictionary mistakes that catch most beginners.
  **On screen:** Breather card
    - Check with `in`, or use `get()` with a default.
    - Keys are case-sensitive.
    - Use `values()` or `items()` when you need the values.
- **Breather:** 4 quiet seconds.

## Scene 13: Think beyond (15:35 to 16:23)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Two tables order at the same time. How could a dictionary with table numbers as keys, and lists of items as values, keep each table's order?
  **On screen:** Question card: "Two tables order at once. How could a dictionary with table numbers as keys and lists of items as values keep each order?"
- **Interaction:** "Two tables order at once. How could a dictionary with table numbers as keys and lists of items as values keep each order?" stays on screen with a 10-second timer.
- **Narration:** Write one after the video, and print the order for table 4.
  **On screen:** Question card: "Two tables order at once. How could a dictionary with table numbers as keys and lists of items as values keep each order?"
- **Narration:** Second. A customer types cakes, with an s. How could the order taker also accept the plural? And is it worth it?
  **On screen:** Question card: "A customer types `cakes`. How could the order taker also accept the plural, and is it worth it?"
- **Interaction:** "A customer types `cakes`. How could the order taker also accept the plural, and is it worth it?" stays on screen with a 10-second timer.
- **Narration:** Try one idea, and test it with three answers.
  **On screen:** Question card: "A customer types `cakes`. How could the order taker also accept the plural, and is it worth it?"

## Scene 14: Recap (16:23 to 17:22)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap. A dictionary stores values under keys. Ask for the key, and you get the value.
  **On screen:** Recap
    - A dictionary stores values under keys: `menu["tea"]` gives the value for `"tea"`.
- **Narration:** The same line adds a new key or changes an existing one.
  **On screen:** Recap
    - A dictionary stores values under keys: `menu["tea"]` gives the value for `"tea"`.
    - `menu[key] = value` adds a new key or changes an existing one.
- **Narration:** In checks the keys. Get gives the value, or None, or your default.
  **On screen:** Recap
    - A dictionary stores values under keys: `menu["tea"]` gives the value for `"tea"`.
    - `menu[key] = value` adds a new key or changes an existing one.
    - `in` checks the keys. `get()` gives the value, `None` or your default.
- **Narration:** A loop over a dictionary gives its keys. Items gives each key with its value.
  **On screen:** Recap
    - A dictionary stores values under keys: `menu["tea"]` gives the value for `"tea"`.
    - `menu[key] = value` adds a new key or changes an existing one.
    - `in` checks the keys. `get()` gives the value, `None` or your default.
    - A loop over a dictionary gives its keys. `items()` gives each key with its value.
- **Narration:** Get, with 0, plus 1, counts things by name.
  **On screen:** Recap
    - A dictionary stores values under keys: `menu["tea"]` gives the value for `"tea"`.
    - `menu[key] = value` adds a new key or changes an existing one.
    - `in` checks the keys. `get()` gives the value, `None` or your default.
    - A loop over a dictionary gives its keys. `items()` gives each key with its value.
    - `counts[item] = counts.get(item, 0) + 1` counts things by name.
- **Narration:** And with AI: ask for a design, then challenge it against the job.
  **On screen:** Recap
    - A dictionary stores values under keys: `menu["tea"]` gives the value for `"tea"`.
    - `menu[key] = value` adds a new key or changes an existing one.
    - `in` checks the keys. `get()` gives the value, `None` or your default.
    - A loop over a dictionary gives its keys. `items()` gives each key with its value.
    - `counts[item] = counts.get(item, 0) + 1` counts things by name.
    - Ask AI to design your data, then challenge its choice.
- **Narration:** One last check. Counts holds tea 2. Then the counting line runs for cake. What is counts now?
  **On screen:** Quick check: "`counts = {"tea": 2}`. After `counts["cake"] = counts.get("cake", 0) + 1`, what is `counts`?" (options shown)
- **Interaction:** "`counts = {"tea": 2}`. After `counts["cake"] = counts.get("cake", 0) + 1`, what is `counts`?" stays on screen with a 10-second timer.
- **Narration:** B. Tea 2, and cake 1. Get gave 0 for the new key, plus 1 is 1, and the line added cake.
  **On screen:** Quick check: "`counts = {"tea": 2}`. After `counts["cake"] = counts.get("cake", 0) + 1`, what is `counts`?" (answer revealed: `{"tea": 2, "cake": 1}`)
- **Narration:** Mission complete! You earned 100 XP and the Key Master badge.
  **On screen:** Key Master You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice (17:22 to 17:47)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. The practice file has eight tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including counting votes.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each: an order with quantities, and an AI's order total to fix.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Predict first, then run. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 16: What's next (17:47 to 18:10)

**Section:** What's next

**Direction:** End card. Tease tuples and sets: fixed groups, and every different customer of the day once. Hold quietly at the end.

- **Narration:** Asha's list of today's customers has Omar in it four times. How many different customers came in? A list keeps every repeat.
  **On screen:** Tuples and Sets: Fixed Groups and Unique Items Fixed groups, and every item only once.
- **Narration:** In Chapter 13, you will meet tuples, fixed groups of values, and sets, which keep each item only once.
  **On screen:** Tuples and Sets: Fixed Groups and Unique Items Fixed groups, and every item only once.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Tuples and Sets: Fixed Groups and Unique Items Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 13.
  **On screen:** Tuples and Sets: Fixed Groups and Unique Items Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
