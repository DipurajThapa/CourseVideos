# Video Script: Chapter 26: Classes and Objects: Modelling Real Things

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:43 (estimate, not rendered yet).

## Scene 1: Introduction

**Section:** Introduction

**Direction:** Open on the Chapter 25 limit: data and rules live apart. Then the title, the AI tease and the mission code with no output.

- **Narration:** At the Corner Cafe, Asha's report from Chapter 25 keeps each sale as a pair, and each day as a dictionary.
  **On screen:** Data here, rules somewhere else
- **Narration:** The rules, like the total, live in separate functions. And a wrong key, like Amount with a capital A, shows up only when the program runs.
  **On screen:** Data here, rules somewhere else
- **Narration:** This is Code Quest, Chapter 26. Today, you build your own types.
  **On screen:** Classes and Objects: Modelling Real Things
- **Narration:** And an AI assistant will design a loyalty card for Asha. It will sound sure about the free teas. Your test cases will decide.
  **On screen:** Classes and Objects: Modelling Real Things Data and rules, together.
- **Narration:** Here is today's mission: an order that keeps its own items, and works out its own total.
  **On screen:** Code `examples/ex08_order_receipt.py`, line 12, 13, 14 highlighted, output hidden
- **Narration:** By the end, you will know every line. Let's build it, piece by piece.
  **On screen:** Code `examples/ex08_order_receipt.py`, line 19, 20 highlighted, output hidden

## Scene 2: Learning goals

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Write a class, and explain self.
  **On screen:** By the end, you will be able to:
    - Write a class with `__init__`, attributes and methods.
    - Explain `self`, and why each object keeps its own data.
- **Narration:** Give an object a readable print form, and write a data class.
  **On screen:** By the end, you will be able to:
    - Write a class with `__init__`, attributes and methods.
    - Explain `self`, and why each object keeps its own data.
    - Give an object a readable print form with `__str__`.
    - Write a data class with `@dataclass`.
- **Narration:** And ask an AI to design a class, then test the design.
  **On screen:** By the end, you will be able to:
    - Write a class with `__init__`, attributes and methods.
    - Explain `self`, and why each object keeps its own data.
    - Give an object a readable print form with `__str__`.
    - Write a data class with `@dataclass`.
    - Ask an AI to design a class, then test the design.

## Scene 3: Why this matters

**Section:** Why this matters

**Direction:** Define a class through Asha's problem, then real uses.

- **Narration:** A class is a new type that you define yourself. It bundles data and the functions that work on it, like a menu item that knows how to add tax to its own price.
  **On screen:** Why this matters
    - A **class** is a new type that you define yourself.
    - It bundles data and the functions that work on that data.
- **Narration:** A shop has products and baskets. A game has players and levels. And AI assistants design code in classes, so you need to judge their designs.
  **On screen:** Why this matters
    - A **class** is a new type that you define yourself.
    - It bundles data and the functions that work on that data.
    - Shops, games and apps are built from types like these. AI assistants design code this way too.

## Scene 4: The idea: a plan and its objects

**Section:** The idea

**Direction:** Teach class and object with the diagram, the five words with the table, then the order slip analogy. Breather.

- **Narration:** A class is the plan. An object is one thing made from that plan. Each object is also called an instance of the class.
  **On screen:** One plan, many objects
- **Narration:** Tea and cake are two objects from the same plan. Each one has its own name, and its own price.
  **On screen:** One plan, many objects
- **Narration:** Class, the plan. Object, or instance, one thing made from it.
  **On screen:** Table: Five words you need (row 2 in focus)
- **Narration:** Attribute: a value stored in an object, read with a dot.
  **On screen:** Table: Five words you need (row 3 in focus)
- **Narration:** Method: a function that belongs to the class.
  **On screen:** Table: Five words you need (row 4 in focus)
- **Narration:** And self: the object a method is working on.
  **On screen:** Table: Five words you need (row 5 in focus)
- **Narration:** Think of the cafe's printed order slip. The blank slip is the class. Each filled-in slip is an object, with its own customer and items.
  **On screen:** Like a printed order slip
    - The blank slip is the class. Each filled-in slip is an object.
- **Narration:** The comparison stops at one point. A paper slip cannot add up its own total. An object can, with a method.
  **On screen:** Like a printed order slip
    - The blank slip is the class. Each filled-in slip is an object.
    - Unlike a paper slip, an object can add up its own total, with a method.
- **Narration:** Breather. One picture: a plan, and the things made from it.
  **On screen:** Breather card
    - A class is the plan for a new type.
    - An object is one thing made from it.
    - Attributes store data; methods do the work.
- **Narration:** Next, Asha writes her first class.
  **On screen:** Breather card
    - A class is the plan for a new type.
    - An object is one thing made from it.
    - Attributes store data; methods do the work.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Your first class

**Section:** Build it step by step

**Direction:** Teach __init__ and self before the ask. Ask what line 10 prints. Reveal.

- **Narration:** Step 1. Line 2 starts the class. Class names use capital letters, like Menu Item.
  **On screen:** Code `examples/ex01_menu_item.py`, line 2 highlighted, output hidden
- **Narration:** The special method init, written with two underscores on each side, runs when you create an object. It stores the starting values on self.
  **On screen:** Code `examples/ex01_menu_item.py`, line 3, 4, 5 highlighted, output hidden
- **Narration:** Line 8 creates an object. Python runs init with name set to Tea and price set to 3.5. It passes the new object as self, so you never write it in the call.
  **On screen:** Code `examples/ex01_menu_item.py`, line 8 highlighted, output hidden
- **Narration:** Line 9 creates a second object. Lines 10 and 11 read attributes with a dot.
  **On screen:** Code `examples/ex01_menu_item.py`, line 9, 10, 11 highlighted, output hidden
- **Interaction:** "What does line 10 print?" stays on screen with a 10-second timer.
- **Narration:** Tea 3.5. Tea dot name, and tea dot price.
  **On screen:** Code `examples/ex01_menu_item.py`, line 10 highlighted, output `examples/ex01_menu_item.expected`
- **Narration:** And line 11 reads cake's own values: Cake 4.25.
  **On screen:** Code `examples/ex01_menu_item.py`, line 11 highlighted, output `examples/ex01_menu_item.expected`

## Scene 6: Step 2: Methods

**Section:** Build it step by step

**Direction:** Teach a method and self.price, and a method calling a method. Ask lines 15 and 16. Quiz on self.

- **Narration:** Step 2. A method is a function written inside the class. Its first parameter is always self.
  **On screen:** Code `examples/ex02_methods.py`, line 7, 8 highlighted, output hidden
- **Narration:** Line 8 uses self dot price, the price of whichever object called the method. It adds 10 percent tax, and rounds to two places.
  **On screen:** Code `examples/ex02_methods.py`, line 8 highlighted, output hidden
- **Narration:** Line 11 calls another method through self, and shows it with two decimal places.
  **On screen:** Code `examples/ex02_methods.py`, line 10, 11 highlighted, output hidden
- **Narration:** Lines 15 and 16 call both methods on tea.
  **On screen:** Code `examples/ex02_methods.py`, line 14, 15, 16 highlighted, output hidden
- **Interaction:** "What do lines 15 and 16 print?" stays on screen with a 10-second timer.
- **Narration:** 3.85, then Tea: 3.85. In tea dot with tax, self is tea, so self dot price is 3.5.
  **On screen:** Code `examples/ex02_methods.py`, line 8, 15 highlighted, output `examples/ex02_methods.expected`
- **Narration:** And label adds the name in front.
  **On screen:** Code `examples/ex02_methods.py`, line 11, 16 highlighted, output `examples/ex02_methods.expected`
- **Narration:** Quick check. In cake dot with tax, what is self?
  **On screen:** Quick check: "In `cake.with_tax()`, what is `self`?" (options shown)
- **Interaction:** "In `cake.with_tax()`, what is `self`?" stays on screen with a 10-second timer.
- **Narration:** C. The object cake. Python passes the object before the dot as self.
  **On screen:** Quick check: "In `cake.with_tax()`, what is `self`?" (answer revealed: The object `cake`)

## Scene 7: Step 3: Each object keeps its own data

**Section:** Build it step by step

**Direction:** Callback to Chapter 17 scope. Teach line 5, and the class-body rule. Ask about Omar. Breather.

- **Narration:** Step 3. In Chapter 17, each function call had its own local names. In the same way, each object has its own attributes.
  **On screen:** Code `examples/ex03_own_data.py`, line 5 highlighted, output hidden
- **Narration:** Line 5 runs once for each new object, so every order gets a new empty list.
  **On screen:** Code `examples/ex03_own_data.py`, line 3, 4, 5 highlighted, output hidden
- **Narration:** Lines 11 and 12 create two orders. Lina gets a tea and a cake, and Omar gets a juice.
  **On screen:** Code `examples/ex03_own_data.py`, line 11, 12, 13, 14, 15 highlighted, output hidden
- **Interaction:** "What does line 17 print for Omar?" stays on screen with a 10-second timer.
- **Narration:** Omar, and a list with only juice. Lina's tea and cake are in her own list.
  **On screen:** Code `examples/ex03_own_data.py`, line 17 highlighted, output `examples/ex03_own_data.expected`
- **Narration:** One more rule. A value written directly in the class body, outside any method, is different. It belongs to the class, and every object shares it. Remember that one.
  **On screen:** Code `examples/ex03_own_data.py`, line 5 highlighted, output `examples/ex03_own_data.expected`
- **Narration:** Breather. You can write a class, create objects, and call their methods.
  **On screen:** Breather card
    - `__init__` stores the starting values on `self`.
    - A method's first parameter is `self`.
    - Each object keeps its own attributes.
- **Narration:** Next, objects start working together.
  **On screen:** Breather card
    - `__init__` stores the starting values on `self`.
    - A method's first parameter is `self`.
    - Each object keeps its own attributes.
- **Breather:** 4 quiet seconds.

## Scene 8: Step 4: Objects that work together

**Section:** Build it step by step

**Direction:** An order holds menu items. The total is computed, not stored. Ask lines 22 and 24.

- **Narration:** Step 4. An order can hold menu item objects. Add, on lines 13 and 14, puts one in the list.
  **On screen:** Code `examples/ex04_order_total.py`, line 13, 14 highlighted, output hidden
- **Narration:** Line 17 is a list comprehension from Chapter 14. It collects the price of every item, and sum adds them up.
  **On screen:** Code `examples/ex04_order_total.py`, line 16, 17 highlighted, output hidden
- **Narration:** The order does not store its total. It works it out each time you ask.
  **On screen:** Code `examples/ex04_order_total.py`, line 17 highlighted, output hidden
- **Narration:** Lines 21 to 24 add a tea, print the total, add a cake, and print it again.
  **On screen:** Code `examples/ex04_order_total.py`, line 21, 22, 23, 24 highlighted, output hidden
- **Interaction:** "What do lines 22 and 24 print?" stays on screen with a 10-second timer.
- **Narration:** 3.5, then 7.75. The total follows every new item.
  **On screen:** Code `examples/ex04_order_total.py`, line 22, 24 highlighted, output `examples/ex04_order_total.expected`
- **Narration:** If the order stored its total as a number, that number would be wrong after the next add. Keep that rule in mind for the AI section.
  **On screen:** Code `examples/ex04_order_total.py`, line 17 highlighted, output `examples/ex04_order_total.expected`

## Scene 9: Step 5: A readable print form

**Section:** Build it step by step

**Direction:** Teach __str__. Show the run. No ask.

- **Narration:** Step 5. Printing your own object shows its type and a memory address, a code that changes every run.
  **On screen:** Code `examples/ex05_str.py`, line 7, 8 highlighted, output hidden
- **Narration:** The special method s t r, also written with two underscores on each side, returns the text that print and f strings show.
  **On screen:** Code `examples/ex05_str.py`, line 7, 8 highlighted, output hidden
- **Narration:** Asha runs it. Print shows Tea, with the price in brackets, and the f string on line 13 uses the same text.
  **On screen:** Code `examples/ex05_str.py`, line 12, 13 highlighted, output `examples/ex05_str.expected`

## Scene 10: Step 6: Data classes

**Section:** Build it step by step

**Direction:** Teach @dataclass and ==. Ask lines 13 and 14. Then the list default error and the field fix. Quiz. Breather.

- **Narration:** Step 6. Many classes only store a few values. The data classes module writes init, a print form and the double equals check for you.
  **On screen:** Code `examples/ex06_dataclass.py`, line 2, 5 highlighted, output hidden
- **Narration:** Line 5 puts at data class above the class. Lines 7 and 8 list the attributes, each with a type after a colon.
  **On screen:** Code `examples/ex06_dataclass.py`, line 5, 6, 7, 8 highlighted, output hidden
- **Narration:** Double equals on two data class objects compares their values, attribute by attribute.
  **On screen:** Code `examples/ex06_dataclass.py`, line 13, 14 highlighted, output hidden
- **Interaction:** "What do lines 13 and 14 print?" stays on screen with a 10-second timer.
- **Narration:** True, then False. Same name and price, then a different price.
  **On screen:** Code `examples/ex06_dataclass.py`, line 13, 14 highlighted, output `examples/ex06_dataclass.expected`
- **Narration:** And line 12 shows the print form the data class wrote: the type, then each attribute and its value.
  **On screen:** Code `examples/ex06_dataclass.py`, line 12 highlighted, output `examples/ex06_dataclass.expected`
- **Narration:** Chapter 17 showed that a list as a default value is a trap: every call shares one list. A data class refuses it.
  **On screen:** Code `examples/ex07_list_error.py`, line 8 highlighted, error `examples/ex07_list_error.expected_error`
- **Narration:** Read the last line: mutable default, not allowed, use default factory. Mutable means it can change.
  **On screen:** Code `examples/ex07_list_error.py`, line 8 highlighted, error `examples/ex07_list_error.expected_error`
- **Narration:** Field, with default factory list, makes a new empty list for each object.
  **On screen:** Code `examples/ex07_list_field.py`, line 8 highlighted, output `examples/ex07_list_field.expected`
- **Narration:** Lina's list has a tea. Omar's list is still empty.
  **On screen:** Code `examples/ex07_list_field.py`, line 13, 14, 15 highlighted, output `examples/ex07_list_field.expected`
- **Narration:** Breather. You have every piece of the mission now. Let's build Asha's receipt.
  **On screen:** Breather card
    - Compute a total in a method; never store it.
    - `__str__` gives a readable print form.
    - `@dataclass` writes `__init__`, the print form and `==`.
- **Breather:** 4 quiet seconds.

## Scene 11: See the outcome: the order receipt

**Section:** See the outcome

**Direction:** Walk the two data classes, then the main lines. Ask what line 30 prints. Hand over to the AI.

- **Narration:** Back to the mission. Lines 5 to 8 describe a menu item: a name and a price.
  **On screen:** Code `examples/ex08_order_receipt.py`, line 5, 6, 7, 8 highlighted, output hidden
- **Narration:** Lines 11 to 14 describe an order: a customer, and its own list of items.
  **On screen:** Code `examples/ex08_order_receipt.py`, line 11, 12, 13, 14 highlighted, output hidden
- **Narration:** Add puts an item in the list. Total works it out, every time.
  **On screen:** Code `examples/ex08_order_receipt.py`, line 16, 17, 19, 20 highlighted, output hidden
- **Narration:** Line 23 creates Lina's order. Lines 24 to 26 add a tea, a cake, and another tea.
  **On screen:** Code `examples/ex08_order_receipt.py`, line 23, 24, 25, 26 highlighted, output hidden
- **Narration:** Line 27 prints the customer. Lines 28 and 29 print each item, lined up with the format codes from Chapter 3.
  **On screen:** Code `examples/ex08_order_receipt.py`, line 27, 28, 29 highlighted, output hidden
- **Narration:** Line 30 prints the total.
  **On screen:** Code `examples/ex08_order_receipt.py`, line 30 highlighted, output hidden
- **Interaction:** "What does line 30 print?" stays on screen with a 10-second timer.
- **Narration:** Total, 11.25. 3.5, plus 4.25, plus 3.5.
  **On screen:** Code `examples/ex08_order_receipt.py`, line 30 highlighted, output `examples/ex08_order_receipt.expected`
- **Narration:** Mission complete! Next, Asha wants a loyalty card for her regulars. She designs it with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex08_order_receipt.py`, output `examples/ex08_order_receipt.expected`

## Scene 12: Work with AI: a loyalty card

**Section:** Work with AI

**Direction:** Safety first. Six stages on LoyaltyCard. Plan drops print and save jobs; Write is Asha's own; Generate stores free_teas; Test catches it; Debug a missing self; Improve a class-body list.

- **Narration:** This chapter's AI skill: ask an AI to design a class, then review whether the design fits.
  **On screen:** This chapter's AI skill: review a class design
    - A design is a set of choices: what each object stores, what each method does.
- **Narration:** Test every choice with real cases. And never paste private data: use made-up names.
  **On screen:** This chapter's AI skill: review a class design
    - A design is a set of choices: what each object stores, what each method does.
    - Test every choice with real cases before you accept it.
    - A real customer list is private: use made-up names.
- **Narration:** Stage 1: plan. Asha describes the loyalty card: one stamp per drink, and a free tea for every 10 stamps. No code yet.
  **On screen:** AI chat, stage 1: Plan: a design, not code
    - You: I want to model a cafe loyalty card: one stamp per drink, and a free tea for every 10 stamps. Do not write code. List the attributes and methods, with one job for each method.
- **Narration:** The AI lists two attributes and four methods. Print card and save card are separate jobs, so Asha drops them. Her main program can print. One job for each method, as in Chapter 17.
  **On screen:** AI chat, stage 1: Plan: a design, not code
    - You: I want to model a cafe loyalty card: one stamp per drink, and a free tea for every 10 stamps. Do not write code. List the attributes and methods, with one job for each method.
    - AI (example answer): Attributes: customer, stamps. Methods: add_stamp() adds one stamp. free_teas() gives the free teas. print_card() prints the card. save_card() saves it to a file.
- **Narration:** Stage 2: write. Asha writes the start of the class herself, and asks the AI to predict the last line.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote this myself. Do not change it. Predict exactly what the last line prints. [code `examples/ai_mine.py`]
- **Narration:** The AI says Lina 2. Asha predicted the same, and the run agrees.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote this myself. Do not change it. Predict exactly what the last line prints. [code `examples/ai_mine.py`]
    - AI (example answer): It prints Lina 2. add_stamp ran twice, and each call added 1 to self.stamps.
    - You: I predicted the same. I ran it:
- **Narration:** Stage 3: generate. Now the free teas. Asha asks the AI to add them, and to say what a card shows after 25 stamps.
  **On screen:** AI chat, stage 3: Generate: one new feature
    - You: Add free teas to my LoyaltyCard class: one free tea for every 10 stamps. Tell me what a card shows after 25 stamps.
- **Narration:** The AI is sure: after 25 stamps, 2 free teas.
  **On screen:** AI chat, stage 3: Generate: one new feature
    - You: Add free teas to my LoyaltyCard class: one free tea for every 10 stamps. Tell me what a card shows after 25 stamps.
    - AI (example answer): Here is the class. After 25 stamps, free_teas is 2. [code `examples/card_ai.py`]
- **Narration:** Look at the AI's class. Line 6 stores free teas as a number. Line 10 adds one when the stamps are exactly 10.
  **On screen:** Code `examples/card_ai.py`, line 6, 10, 11 highlighted, output hidden
- **Narration:** Asha runs it: 25 stamps, then she prints the stamps and the free teas.
  **On screen:** Code `examples/ai_generate_run.py`, line 5, 6, 7 highlighted, output hidden
- **Interaction:** "The AI says the card shows 2 free teas. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. 25 stamps, but only 1 free tea. Line 10 counts only stamp number 10, so stamp 20 never counts. And the AI sounded sure.
  **On screen:** Code `examples/ai_generate_run.py`, line 7 highlighted, output `examples/ai_generate_run.expected`
- **Narration:** Stage 4: test. Asha asks for test cases, each with an expected result.
  **On screen:** AI chat, stage 4: Test: cases with expected results
    - You: Suggest test cases for free teas, each with an expected result.
- **Narration:** The AI suggests 0, 9, 10 and 25 stamps. Asha adds one more: an old card that starts with 12 stamps.
  **On screen:** AI chat, stage 4: Test: cases with expected results
    - You: Suggest test cases for free teas, each with an expected result.
    - AI (example answer): Test 0, 9, 10 and 25 stamps. Expect 0, 0, 1 and 2 free teas.
    - You: I am adding one more case: an old card that starts with 12 stamps. It should have 1 free tea.
- **Narration:** She runs all five cases on the AI's class. Two fail: 25 stamps gives 1, and the old card gives 0.
  **On screen:** Code `examples/ai_cases_flawed.py`, line 7, 8, 9, 10, 11 highlighted, output `examples/ai_cases_flawed.expected`
- **Narration:** Asha shows the failing cases, and asks for the cause first.
  **On screen:** AI chat, stage 4: Test: the cause before the fix
    - You: Two cases fail. Explain the cause before you change any code.
- **Narration:** The AI explains: free teas is a stored number, and an old card starts at 0. The fix works it out from the stamps, with a method. The same rule as the total in step 4.
  **On screen:** AI chat, stage 4: Test: the cause before the fix
    - You: Two cases fail. Explain the cause before you change any code.
    - AI (example answer): free_teas is a stored number. Line 10 adds one only at exactly 10 stamps, and an old card starts at 0. Fix: work it out from the stamps, with a method that returns self.stamps // 10.
- **Narration:** Lines 10 and 11 return the stamps, floor divided by 10. Nothing is stored, so nothing goes stale.
  **On screen:** Code `examples/card_fixed.py`, line 10, 11 highlighted, output hidden
- **Narration:** She runs all five cases again. Line 11 now calls free teas as a method. All five pass.
  **On screen:** Code `examples/ai_cases_fixed.py`, line 11 highlighted, output `examples/ai_cases_fixed.expected`
- **Narration:** Stage 5: debug. Asha adds a method, card line, and calls it on line 5. Type error!
  **On screen:** Code `examples/ai_line_crash.py`, line 5 highlighted, error `examples/ai_line_crash.expected_error`
- **Narration:** Read the last line: card line takes 0 positional arguments, but 1 was given.
  **On screen:** Code `examples/ai_line_crash.py`, line 5 highlighted, error `examples/ai_line_crash.expected_error`
- **Narration:** She pastes the code and the full error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I added card_line and got this error. First explain what it means and which line causes it. Then show the smallest fix. [code `examples/card_debug.py`]
- **Narration:** The AI explains: line 13 has no parameter. Python passes the card as the first argument, so the method needs self.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I added card_line and got this error. First explain what it means and which line causes it. Then show the smallest fix. [code `examples/card_debug.py`]
    - AI (example answer): Line 13 defines card_line with no parameter. Python passes the card as the first argument, so the method has nowhere to put it. Fix: def card_line(self):
- **Narration:** With self added, she runs all five cases again. All pass, and line 14 prints Omar's card line.
  **On screen:** Code `examples/ai_cases_lines.py`, line 14 highlighted, output `examples/ai_cases_lines.expected`
- **Narration:** Stage 6: improve. Asha asks for one improvement.
  **On screen:** AI chat, stage 6: Improve: one suggestion, then test it
    - You: Review my class. Suggest one improvement, with one reason. Do not change what my methods return.
- **Narration:** The AI suggests a history of every drink stamped, with a list at the top of the class.
  **On screen:** AI chat, stage 6: Improve: one suggestion, then test it
    - You: Review my class. Suggest one improvement, with one reason. Do not change what my methods return.
    - AI (example answer): Keep a history of every drink stamped. Write history = [] at the top of the class, and append the drink in add_stamp.
- **Narration:** Asha tests the idea with two cards. Only Lina gets a stamp, for a latte. Omar gets nothing.
  **On screen:** Code `examples/ai_history_shared.py`, line 4, 5, 6 highlighted, output hidden
- **Narration:** Remember the rule from step 3, about a value in the class body.
  **On screen:** Code `examples/ai_history_shared.py`, line 8 highlighted, output hidden
- **Interaction:** "What does line 8 print for Omar?" stays on screen with a 10-second timer.
- **Narration:** Omar, with a latte! The list in the class body belongs to the class, so every card shares it. The AI was wrong again.
  **On screen:** Code `examples/ai_history_shared.py`, line 8 highlighted, output `examples/ai_history_shared.expected`
- **Narration:** So Asha keeps the idea, but moves the list into init, on line 6. Now each card makes its own list.
  **On screen:** Code `examples/card_final.py`, line 6 highlighted, output hidden
- **Narration:** She writes her cases as pytest tests, from Chapter 19, and adds one for the history. Five dots: five passed.
  **On screen:** Code `examples/test_loyalty.py`, line 28, 29, 30, 31, 32 highlighted, output `examples/test_loyalty.expected`
- **Narration:** Quick check. A card stores its stamps. What is the best design for its free teas?
  **On screen:** Quick check: "A card stores its stamps. What is the best design for its free teas?" (options shown)
- **Interaction:** "A card stores its stamps. What is the best design for its free teas?" stays on screen with a 10-second timer.
- **Narration:** B. A method that works them out from the stamps. Then they can never go stale.
  **On screen:** Quick check: "A card stores its stamps. What is the best design for its free teas?" (answer revealed: A method that returns `self.stamps // 10`)
- **Narration:** Breather. The AI made two confident design mistakes, and Asha's cases caught both. Next, four classic mistakes.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Compute a value from other attributes in a method.
    - Test a design with two objects.
- **Breather:** 4 quiet seconds.

## Scene 13: Common mistakes

**Section:** Common mistakes

**Direction:** Mistake 1 calls back to the debug stage. Mistakes 2 and 4 are spot-it asks. Mistake 3 is explained.

- **Narration:** Mistake 1 is the one Asha debugged. Line 7 has no self, so Python has nowhere to put the object.
  **On screen:** Code `examples/err01_no_self.py`, line 7 highlighted, error `examples/err01_no_self.expected_error`
- **Narration:** Takes 0 positional arguments, but 1 was given. That 1 is the object. The fix: def with tax, self.
  **On screen:** Code `examples/err01_no_self.py`, line 7 highlighted, error `examples/err01_no_self.expected_error`
- **Narration:** Mistake 2. You try. Line 8 is meant to create a menu item. Look closely, and remember step 1.
  **On screen:** Code `examples/err02_no_brackets.py`, line 8 highlighted, output hidden
- **Interaction:** "What is missing on line 8?" stays on screen with a 10-second timer.
- **Narration:** The brackets, and the values. Without them, tea is the class itself, the plan, which has no price of its own.
  **On screen:** Code `examples/err02_no_brackets.py`, line 8 highlighted, error `examples/err02_no_brackets.expected_error`
- **Narration:** Type object, in the message, is the clue: tea is a class, not an object.
  **On screen:** Code `examples/err02_no_brackets.py`, line 8 highlighted, error `examples/err02_no_brackets.expected_error`
- **Narration:** Mistake 3. Line 9 spells price wrongly, so the object has no attribute with that name. Newer versions of Python even suggest the closest one.
  **On screen:** Code `examples/err03_attribute_typo.py`, line 9 highlighted, error `examples/err03_attribute_typo.expected_error`
- **Narration:** Mistake 4. Line 3 creates the list in the class body. Line 14 adds a tea for Lina only.
  **On screen:** Code `examples/err04_shared_list.py`, line 3, 14 highlighted, output hidden
- **Interaction:** "What does line 15 print for Omar?" stays on screen with a 10-second timer.
- **Narration:** Omar, with a tea. No error at all, which makes it worse. One list, shared by every order.
  **On screen:** Code `examples/err04_shared_list.py`, line 3, 15 highlighted, output `examples/err04_shared_list.expected`
- **Narration:** The fix: create the list in init, with self dot items, or use field in a data class.
  **On screen:** Code `examples/err04_shared_list.py`, line 3, 15 highlighted, output `examples/err04_shared_list.expected`
- **Narration:** Last breather. Two questions to think about on your own come next.
  **On screen:** Breather card
    - Every method needs `self`.
    - Create an object with brackets and values.
    - Lists belong in `__init__`, not the class body.
- **Breather:** 4 quiet seconds.

## Scene 14: Think beyond

**Section:** Think beyond

**Direction:** Two open questions. No answers are given.

- **Narration:** First. Asha's cafe has tables, and each table has several orders. Design a table class. Which attributes does it store, and which value should be a method?
  **On screen:** Question card: "Design a `Table` class that holds several orders. Which attributes does it store, and which value should be a method?"
- **Interaction:** "Design a `Table` class that holds several orders. Which attributes does it store, and which value should be a method?" stays on screen with a 10-second timer.
- **Narration:** Sketch it after the video, then try it in the practice tasks.
  **On screen:** Question card: "Design a `Table` class that holds several orders. Which attributes does it store, and which value should be a method?"
- **Narration:** Second. Two data class objects with the same values are equal. Are two objects of a normal class, like the menu item from step 1, equal too?
  **On screen:** Question card: "Are two objects of a normal class, such as `MenuItem("Tea", 3.5)` from Step 1, equal with `==`?"
- **Interaction:** "Are two objects of a normal class, such as `MenuItem("Tea", 3.5)` from Step 1, equal with `==`?" stays on screen with a 10-second timer.
- **Narration:** Predict, then test it.
  **On screen:** Question card: "Are two objects of a normal class, such as `MenuItem("Tea", 3.5)` from Step 1, equal with `==`?"

## Scene 15: Recap

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a quiz, then the badge.

- **Narration:** Let's recap. A class is the plan. An object is one thing made from it.
  **On screen:** Recap
    - A class is the plan; an object is one thing made from it.
- **Narration:** Init stores the starting values on self, and methods work on self.
  **On screen:** Recap
    - A class is the plan; an object is one thing made from it.
    - `__init__` stores attributes on `self`. Methods work on `self`.
- **Narration:** Attributes set in init belong to one object.
  **On screen:** Recap
    - A class is the plan; an object is one thing made from it.
    - `__init__` stores attributes on `self`. Methods work on `self`.
    - Attributes set in `__init__` belong to one object.
- **Narration:** S t r gives a readable print form.
  **On screen:** Recap
    - A class is the plan; an object is one thing made from it.
    - `__init__` stores attributes on `self`. Methods work on `self`.
    - Attributes set in `__init__` belong to one object.
    - `__str__` gives a readable print form.
- **Narration:** A data class writes init, the print form and double equals for you.
  **On screen:** Recap
    - A class is the plan; an object is one thing made from it.
    - `__init__` stores attributes on `self`. Methods work on `self`.
    - Attributes set in `__init__` belong to one object.
    - `__str__` gives a readable print form.
    - `@dataclass` writes `__init__`, a print form and `==`.
- **Narration:** And a value that depends on other attributes belongs in a method.
  **On screen:** Recap
    - A class is the plan; an object is one thing made from it.
    - `__init__` stores attributes on `self`. Methods work on `self`.
    - Attributes set in `__init__` belong to one object.
    - `__str__` gives a readable print form.
    - `@dataclass` writes `__init__`, a print form and `==`.
    - Compute a value from other attributes in a method.
- **Narration:** One last check. Menu item is a data class. What does printing a cake show?
  **On screen:** Quick check: "`MenuItem` is a data class. What does `print(MenuItem("Cake", 4.25))` show?" (options shown)
- **Interaction:** "`MenuItem` is a data class. What does `print(MenuItem("Cake", 4.25))` show?" stays on screen with a 10-second timer.
- **Narration:** A. The type, then each attribute and its value, like line 12 in step 6.
  **On screen:** Quick check: "`MenuItem` is a data class. What does `print(MenuItem("Cake", 4.25))` show?" (answer revealed: `MenuItem(name='Cake', price=4.25)`)
- **Narration:** Quest complete! You earned 100 XP and the Modeller badge.
  **On screen:** Modeller You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 16: Practice

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. Three warm-up tasks at 10 XP, and three apply tasks at 20.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's order class whose total goes stale.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 17: What's next

**Section:** What's next

**Direction:** End card. Tease Chapter 27: reading and improving code you did not write. Hold quietly.

- **Narration:** Today, Asha reviewed an AI's design before she trusted it. But soon she will meet a whole program written by someone else.
  **On screen:** Reading and Improving Code with AI Read code you did not write, and improve it safely.
- **Narration:** In Chapter 27, you will read unfamiliar code, and improve it safely, with tests and an AI assistant.
  **On screen:** Reading and Improving Code with AI Read code you did not write, and improve it safely.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Reading and Improving Code with AI Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 27.
  **On screen:** Reading and Improving Code with AI Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
