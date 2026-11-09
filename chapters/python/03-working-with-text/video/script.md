# Video Script: Chapter 3: Working with Text: Strings and f-strings

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:19.

## Scene 1: Introduction (0:00 to 0:50)

**Section:** Introduction

**Direction:** Open on the untidy bill from Chapter 2, then show the neat receipt as the mission. Tease the AI mistake. No question yet.

- **Narration:** Welcome back to Code Quest. This is Chapter 3.
  **On screen:** Working with Text: Strings and f-strings
- **Narration:** Today you will turn plain values into clear, tidy text that people trust.
  **On screen:** Working with Text: Strings and f-strings Clear text. Straight columns. Two decimals.
- **Narration:** And an AI assistant will make a mistake that gives no error at all. You will spot it anyway.
  **On screen:** Working with Text: Strings and f-strings Clear text. Straight columns. Two decimals.
- **Narration:** In Chapter 2, Asha's bill updated itself. The maths was right. But look at the text.
  **On screen:** Asha's bill is correct, but messy
    - It printed `Teas: 2 x 3.5 = 7.0`.
- **Narration:** The amount to pay was 11.7, not 11.70, and the prices were all over the place. Customers notice that.
  **On screen:** Asha's bill is correct, but messy
    - It printed `Teas: 2 x 3.5 = 7.0`.
    - It printed `To pay: 11.7`, not `11.70`.
    - The prices did not sit in one column.
- **Narration:** So here is today's mission. A receipt with a clean customer name and a title in the middle.
  **On screen:** Code `examples/ex07_receipt.py`, line 16, 17 highlighted, output `examples/ex07_receipt.expected`
- **Narration:** Every amount has two decimal places, and every price sits in one straight column.
  **On screen:** Code `examples/ex07_receipt.py`, line 19, 20, 21, 23 highlighted, output `examples/ex07_receipt.expected`
- **Narration:** By the end of this video, you will understand every line of it. Let's build it, piece by piece.
  **On screen:** Code `examples/ex07_receipt.py`, output `examples/ex07_receipt.expected`

## Scene 2: Learning goals (0:50 to 1:09)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Here is the plan. Join strings, and build messages with f strings.
  **On screen:** By the end, you will be able to:
    - Join strings with `+` and build messages with f-strings.
- **Narration:** Show any number with exactly two decimal places.
  **On screen:** By the end, you will be able to:
    - Join strings with `+` and build messages with f-strings.
    - Show a number with exactly two decimal places.
- **Narration:** Line up text and numbers in neat columns.
  **On screen:** By the end, you will be able to:
    - Join strings with `+` and build messages with f-strings.
    - Show a number with exactly two decimal places.
    - Line up text and numbers in columns.
- **Narration:** Clean up text with a few handy methods.
  **On screen:** By the end, you will be able to:
    - Join strings with `+` and build messages with f-strings.
    - Show a number with exactly two decimal places.
    - Line up text and numbers in columns.
    - Clean text with `strip()`, `title()`, `upper()` and `replace()`.
- **Narration:** And read single characters, and fix the errors beginners meet with text.
  **On screen:** By the end, you will be able to:
    - Join strings with `+` and build messages with f-strings.
    - Show a number with exactly two decimal places.
    - Line up text and numbers in columns.
    - Clean text with `strip()`, `title()`, `upper()` and `replace()`.
    - Read one character with an index, and fix common text errors.

## Scene 3: Why this matters (1:09 to 1:27)

**Section:** Why this matters

**Direction:** Connect tidy text to trust, with everyday examples.

- **Narration:** Almost every program shows text to people: a receipt, a menu, a message on your phone, or a report at work.
  **On screen:** Why this matters
    - Almost every program shows text to people.
    - Receipts, menus, messages and reports all need clear text.
- **Narration:** The data inside can be perfect. But if the text is messy, people do not trust it. So today, Asha makes her output look as good as her maths.
  **On screen:** Why this matters
    - Almost every program shows text to people.
    - Receipts, menus, messages and reports all need clear text.
    - Correct data in messy text looks wrong.
    - Clear text makes your output look professional.

## Scene 4: The idea: strings, indexes and f-strings (1:27 to 3:04)

**Section:** The idea

**Direction:** Teach the index diagram, then the two ways to build text, then the form analogy and immutability. Quiz on indexes, then a breather.

- **Narration:** First, the idea. A string is a sequence of characters: letters, digits, spaces and symbols, in a row.
  **On screen:** A string is a row of characters
- **Narration:** Each character has a position, called its index. And here is the surprise. The first index is 0, not 1.
  **On screen:** A string is a row of characters
- **Narration:** You can also count from the end. Minus 1 is always the last character.
  **On screen:** A string is a row of characters
- **Narration:** There are two ways to build a message from your variables.
  **On screen:** Table: Two ways to build a message
- **Narration:** You can join strings with a plus sign. That works well for a few pieces of text.
  **On screen:** Table: Two ways to build a message (row 1 in focus)
- **Narration:** Or you can use an f string. It mixes text and numbers, and it can format them too.
  **On screen:** Table: Two ways to build a message (row 2 in focus)
- **Narration:** An f string starts with the letter f, right before the opening quotation mark.
  **On screen:** An f-string is like a form
    - An `f` before the quotation mark makes an f-string.
- **Narration:** Think of it as a form with blank boxes. Each pair of curly brackets is a box, and Python fills it with a value.
  **On screen:** An f-string is like a form
    - An `f` before the quotation mark makes an f-string.
    - Each `{ }` is a box that Python fills with a value.
- **Narration:** Unlike a paper form, a box can also say how to show the value, for example with two decimal places.
  **On screen:** An f-string is like a form
    - An `f` before the quotation mark makes an f-string.
    - Each `{ }` is a box that Python fills with a value.
    - Unlike a paper form, a box can also say **how** to show the value.
- **Narration:** One more rule. A string can never be changed after it is made. You always make a new one.
  **On screen:** An f-string is like a form
    - An `f` before the quotation mark makes an f-string.
    - Each `{ }` is a box that Python fills with a value.
    - Unlike a paper form, a box can also say **how** to show the value.
    - A string never changes. Methods give you a **new** string.
- **Narration:** Quick check. In the word cafe, in capitals, what is the index of the letter F?
  **On screen:** Quick check: "In the string `"CAFE"`, what is the index of the letter `F`?" (options shown)
- **Interaction:** "In the string `"CAFE"`, what is the index of the letter `F`?" stays on screen with a 10-second timer.
- **Narration:** B, 2. C is 0, A is 1, and F is 2. Counting from 0 takes practice, so keep this one in mind.
  **On screen:** Quick check: "In the string `"CAFE"`, what is the index of the letter `F`?" (answer revealed: 2)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - A string is a row of characters.
    - Indexes start at 0; minus 1 is the last.
    - An f-string fills `{ }` boxes with values.
- **Narration:** Next, Asha starts building her text, one piece at a time.
  **On screen:** Breather card
    - A string is a row of characters.
    - Indexes start at 0; minus 1 is the last.
    - An f-string fills `{ }` boxes with values.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Join strings (3:04 to 3:40)

**Section:** Build it step by step

**Direction:** Teach that plus adds no space, then ask about the output, then reveal.

- **Narration:** Step 1. Joining strings with a plus sign is called concatenation. Asha stores two words.
  **On screen:** Code `examples/ex01_join.py`, lines 1 to 3 typed in, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 joins them. The plus sign adds no space by itself, so Asha adds a space string in the middle.
  **On screen:** Code `examples/ex01_join.py`, lines 1 to 4 typed in, line 4 highlighted, output hidden
- **Narration:** Line 5 joins five pieces into a welcome message.
  **On screen:** Code `examples/ex01_join.py`, lines 1 to 5 typed in, line 5 highlighted, output hidden
- **Interaction:** "What does line 5 print? Look closely at the spaces." stays on screen with a 10-second timer.
- **Narration:** Welcome to the Corner Cafe, with an exclamation mark. Every space is there because Asha typed it.
  **On screen:** Code `examples/ex01_join.py`, lines 1 to 5 typed in, line 5 highlighted, output `examples/ex01_join.expected`

## Scene 6: Step 2: f-strings (3:40 to 4:22)

**Section:** Build it step by step

**Direction:** Teach the f prefix and braces, then predict the calculation line.

- **Narration:** Step 2. Asha stores her customer, a count and a price, as in Chapter 2.
  **On screen:** Code `examples/ex02_fstring.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Line 5 is an f string. The name inside the curly brackets is replaced with its value.
  **On screen:** Code `examples/ex02_fstring.py`, line 5 highlighted, output hidden
- **Narration:** Inside the brackets you can also put a calculation. Python works it out first.
  **On screen:** Code `examples/ex02_fstring.py`, line 6 highlighted, output hidden
- **Interaction:** "What does line 6 print?" stays on screen with a 10-second timer.
- **Narration:** Line 5 says hello to Asha.
  **On screen:** Code `examples/ex02_fstring.py`, line 5 highlighted, output `examples/ex02_fstring.expected`
- **Narration:** And line 6 says 2 teas cost 7.0. No plus signs needed. But 7.0 still looks untidy, so let's fix that next.
  **On screen:** Code `examples/ex02_fstring.py`, line 6 highlighted, output `examples/ex02_fstring.expected`

## Scene 7: Step 3: Two decimal places (4:22 to 5:15)

**Section:** Build it step by step

**Direction:** Teach dot 2 f, then predict two lines, then reveal including rounding.

- **Narration:** Step 3. Line 4 prints the amount the plain way.
  **On screen:** Code `examples/ex03_decimals.py`, line 4 highlighted, output hidden
- **Narration:** On line 5, after the name, there is a colon and a short code: dot 2 f. That is a format specification.
  **On screen:** Code `examples/ex03_decimals.py`, line 5 highlighted, output hidden
- **Narration:** Dot 2 f means: a decimal number, with exactly two digits after the point. With more digits, Python rounds, like round in Chapter 2.
  **On screen:** Code `examples/ex03_decimals.py`, line 5, 6, 7 highlighted, output hidden
- **Interaction:** "What do lines 5 and 7 print?" stays on screen with a 10-second timer.
- **Narration:** Line 4 still shows 11.7. Line 5 shows 11.70. The format added the missing zero.
  **On screen:** Code `examples/ex03_decimals.py`, line 4, 5 highlighted, output `examples/ex03_decimals.expected`
- **Narration:** Line 6 shows the discount as 1.30.
  **On screen:** Code `examples/ex03_decimals.py`, line 6 highlighted, output `examples/ex03_decimals.expected`
- **Narration:** And line 7 rounds ten divided by three to 3.33. The value itself never changes. Only the way it is shown.
  **On screen:** Code `examples/ex03_decimals.py`, line 7 highlighted, output `examples/ex03_decimals.expected`

## Scene 8: Step 4: Columns (5:15 to 7:06)

**Section:** Build it step by step

**Direction:** Teach width, alignment and fill with a table, then the code, then the ask, then a quiz and a breather.

- **Narration:** Step 4. To line up columns, the format can also set a width and an alignment.
  **On screen:** Table: Step 4: Width and alignment
- **Narration:** A less than arrow and a number: the value takes at least that many characters, aligned left.
  **On screen:** Table: Step 4: Width and alignment (row 1 in focus)
- **Narration:** A greater than arrow aligns it right. That is perfect for prices.
  **On screen:** Table: Step 4: Width and alignment (row 2 in focus)
- **Narration:** A caret centres the value.
  **On screen:** Table: Step 4: Width and alignment (row 3 in focus)
- **Narration:** And a character before the arrow fills the empty space instead of spaces.
  **On screen:** Table: Step 4: Width and alignment (row 4 in focus)
- **Narration:** Line 4 prints a header. Inside the brackets, Asha writes text in single quotation marks, because the f string itself uses double ones. Mixing them tells Python where each string ends.
  **On screen:** Code `examples/ex04_columns.py`, line 4 highlighted, output hidden
- **Narration:** Lines 5 and 6 use the same widths: 10 on the left for the name, and 8 on the right for the price, with dot 2 f.
  **On screen:** Code `examples/ex04_columns.py`, line 5, 6 highlighted, output hidden
- **Narration:** Line 7 centres the word menu in 18 characters, and fills the space with stars.
  **On screen:** Code `examples/ex04_columns.py`, line 7 highlighted, output hidden
- **Interaction:** "Lines 5 and 6: do the two prices line up? Why?" stays on screen with a 10-second timer.
- **Narration:** Yes. Every name takes 10 characters and every price takes 8, so both prices end in the same column.
  **On screen:** Code `examples/ex04_columns.py`, line 5, 6 highlighted, output `examples/ex04_columns.expected`
- **Narration:** And line 7 gives six stars, the word menu with a space on each side, and six more stars.
  **On screen:** Code `examples/ex04_columns.py`, line 7 highlighted, output `examples/ex04_columns.expected`
- **Narration:** Quick check. Which code shows the price 6 as 6.00, right aligned in 8 characters?
  **On screen:** Quick check: "Which code shows the price `6` as `6.00`, right-aligned in 8 characters?" (options shown)
- **Interaction:** "Which code shows the price `6` as `6.00`, right-aligned in 8 characters?" stays on screen with a 10-second timer.
- **Narration:** D. The arrow points right, 8 is the width, and dot 2 f gives two decimals.
  **On screen:** Quick check: "Which code shows the price `6` as `6.00`, right-aligned in 8 characters?" (answer revealed: `{price:>8.2f}`)
- **Narration:** Breather. Relax your shoulders. You can already format numbers like a professional.
  **On screen:** Breather card
    - An f-string mixes text and values.
    - `.2f` shows two decimal places.
    - Width and `<`, `>`, `^` line up columns.
- **Narration:** Next, Asha cleans up the text itself.
  **On screen:** Breather card
    - An f-string mixes text and values.
    - `.2f` shows two decimal places.
    - Width and `<`, `>`, `^` line up columns.
- **Breather:** 4 quiet seconds.

## Scene 9: Step 5: String methods (7:06 to 8:11)

**Section:** Build it step by step

**Direction:** Teach the methods with a table, then the code, then the ask on len, then the immutability point.

- **Narration:** Step 5. A method is a function that belongs to a value. You call it with a dot after the value.
  **On screen:** Table: Step 5: Methods that clean text
- **Narration:** Strip removes spaces at the start and the end.
  **On screen:** Table: Step 5: Methods that clean text (row 1 in focus)
- **Narration:** Title gives each word a capital first letter.
  **On screen:** Table: Step 5: Methods that clean text (row 2 in focus)
- **Narration:** Upper and lower change every letter to capitals, or to small letters.
  **On screen:** Table: Step 5: Methods that clean text (row 3 in focus)
- **Narration:** And replace swaps one part of the text for another.
  **On screen:** Table: Step 5: Methods that clean text (row 4 in focus)
- **Narration:** A customer typed a name with extra spaces, and no capitals. Asha strips it on line 3.
  **On screen:** Code `examples/ex05_methods.py`, line 2, 3 highlighted, output hidden
- **Narration:** Lines 5 to 7 try title, upper and replace.
  **On screen:** Code `examples/ex05_methods.py`, line 5, 6, 7 highlighted, output hidden
- **Narration:** Line 8 uses len. The len function counts every character in a string, spaces included.
  **On screen:** Code `examples/ex05_methods.py`, line 8 highlighted, output hidden
- **Interaction:** "Line 8 prints two numbers. What are they?" stays on screen with a 10-second timer.
- **Narration:** Strip removed the spaces. Title, upper and replace each gave a new version.
  **On screen:** Code `examples/ex05_methods.py`, line 3, 4, 5, 6, 7 highlighted, output `examples/ex05_methods.expected`
- **Narration:** And line 8 prints 13 and 9. The typed name still has 13 characters. Strip made a new string, and the old one never changed.
  **On screen:** Code `examples/ex05_methods.py`, line 8 highlighted, output `examples/ex05_methods.expected`

## Scene 10: Step 6: Indexes (8:11 to 8:55)

**Section:** Build it step by step

**Direction:** Use the order code from Chapter 1. Predict four characters, then reveal.

- **Narration:** Step 6. Remember the order code from Chapter 1? Asha stores it as a string.
  **On screen:** Code `examples/ex06_index.py`, line 2 highlighted, output hidden
- **Narration:** To read one character, write its index in square brackets after the string. Use the rules from the idea section.
  **On screen:** Code `examples/ex06_index.py`, line 3, 4, 5, 6 highlighted, output hidden
- **Interaction:** "Predict lines 3 to 6. Which characters do they print?" stays on screen with a 10-second timer.
- **Narration:** Index 0 is C, the first character.
  **On screen:** Code `examples/ex06_index.py`, line 3 highlighted, output `examples/ex06_index.expected`
- **Narration:** Index 5 is the 1 right after the hyphen. Count from 0: C, A, F, E, hyphen, then 1.
  **On screen:** Code `examples/ex06_index.py`, line 4 highlighted, output `examples/ex06_index.expected`
- **Narration:** Minus 1 is the last character, 4. And minus 2 is the T before it.
  **On screen:** Code `examples/ex06_index.py`, line 5, 6 highlighted, output `examples/ex06_index.expected`
- **Narration:** The code has 12 characters, so its indexes go from 0 to 11.
  **On screen:** Code `examples/ex06_index.py`, line 7 highlighted, output `examples/ex06_index.expected`

## Scene 11: See the outcome: the neat receipt (8:55 to 10:05)

**Section:** See the outcome

**Direction:** Return to the mission. Walk the groups of lines, reveal, then ask. Hand over to the AI story.

- **Narration:** Back to the mission. Lines 2 to 6 store the values, and lines 8 to 11 do the maths, exactly as in Chapter 2.
  **On screen:** Code `examples/ex07_receipt.py`, line 2, 3, 4, 5, 6 highlighted, output hidden
- **Narration:** Line 12 cleans the name with two methods in a row: strip first, then title.
  **On screen:** Code `examples/ex07_receipt.py`, line 12 highlighted, output hidden
- **Narration:** Line 13 builds the tea label with an f string. Line 14 repeats a hyphen 24 times, the way text times a number worked in Chapter 2.
  **On screen:** Code `examples/ex07_receipt.py`, line 13, 14 highlighted, output hidden
- **Narration:** Line 16 centres the cafe name, filled with equals signs. Then every amount line uses 16 characters for the label and 8 for the amount.
  **On screen:** Code `examples/ex07_receipt.py`, line 16, 19, 20, 21, 23 highlighted, output hidden
- **Narration:** Asha runs it.
  **On screen:** Code `examples/ex07_receipt.py`, output `examples/ex07_receipt.expected`
- **Interaction:** "Asha changes `tea_price` to 4.25. What does the Tea line show?" stays on screen with a 10-second timer.
- **Narration:** Tea x 2, and 8.50. Two teas at 4.25 is 8.5, and dot 2 f adds the zero. It stays in the same column.
  **On screen:** Code `examples/ex07_receipt.py`, line 3, 19 highlighted, output `examples/ex07_receipt.expected`
- **Narration:** The receipt looks professional now. Next, Asha wants a tool that prints one tidy line for any item. She builds it with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex07_receipt.py`, output `examples/ex07_receipt.expected`

## Scene 12: Work with AI: six stages, one receipt line (10:05 to 13:39)

**Section:** Work with AI

**Direction:** The AI skill is a precise prompt. Then one conversation per stage on one receipt line. Stage 3 plants the missing f, stage 4 catches it, stage 6 catches .2.

- **Narration:** This chapter's AI skill is a precise prompt.
  **On screen:** This chapter's AI skill: a precise prompt
- **Narration:** When you want text in an exact shape, show the AI the exact output you want.
  **On screen:** This chapter's AI skill: a precise prompt
    - Show the AI the **exact** output you want, character by character.
- **Narration:** Then compare its result with your target, character by character.
  **On screen:** This chapter's AI skill: a precise prompt
    - Show the AI the **exact** output you want, character by character.
    - Compare the AI's result with your target, character by character.
- **Narration:** And the safety habits still apply. No private data, and you run every piece of code yourself.
  **On screen:** This chapter's AI skill: a precise prompt
    - Show the AI the **exact** output you want, character by character.
    - Compare the AI's result with your target, character by character.
    - No passwords or private data. Run every piece of AI code yourself.
- **Narration:** Stage 1: plan. Asha describes the exact line she wants, and asks for the widths and codes. No code yet.
  **On screen:** AI chat, stage 1: Plan the line first
    - You: I am a beginner learning f-strings. I want one receipt line: the name Sandwich on the left and the price 6.00 on the right, 24 characters in total. Do not write code yet. Which widths, alignments and format code do I need?
- **Narration:** The AI plans 16 characters on the left, 8 on the right, and dot 2 f. And 16 plus 8 is 24. That matches her target.
  **On screen:** AI chat, stage 1: Plan the line first
    - You: I am a beginner learning f-strings. I want one receipt line: the name Sandwich on the left and the price 6.00 on the right, 24 characters in total. Do not write code yet. Which widths, alignments and format code do I need?
    - AI (example answer): 1. The name: width 16, aligned left with `<`. 2. The price: width 8, aligned right with `>`. 3. `.2f` shows the price with two decimal places. 16 + 8 = 24 characters in total.
- **Narration:** Stage 2: write. Asha writes the header row herself. She asks the AI to predict it, with a dot for every space, so she can count.
  **On screen:** AI chat, stage 2: Write it yourself, then predict
    - You: I wrote the header row myself. Do not change it and do not run it. Predict the exact output, with a dot for every space. [code `examples/ai_header.py`]
- **Narration:** The AI predicts the word item, 15 dots, then the word price.
  **On screen:** AI chat, stage 2: Write it yourself, then predict
    - You: I wrote the header row myself. Do not change it and do not run it. Predict the exact output, with a dot for every space. [code `examples/ai_header.py`]
    - AI (example answer): Item...............Price That is Item, 15 dots, then Price: 24 characters.
- **Narration:** Asha counts 24 characters too. She runs it, and it matches.
  **On screen:** AI chat, stage 2: Write it yourself, then predict
    - You: I wrote the header row myself. Do not change it and do not run it. Predict the exact output, with a dot for every space. [code `examples/ai_header.py`]
    - AI (example answer): Item...............Price That is Item, 15 dots, then Price: 24 characters.
    - You: I counted 24 too. Then I ran it:
- **Narration:** Stage 3: generate. Now the item line itself. Asha asks for the code, and asks exactly what it prints.
  **On screen:** AI chat, stage 3: Generate the item line
    - You: Now write the line for one item: the name Sandwich and the price 6. Use the names item and price. Tell me exactly what it prints.
- **Narration:** The AI gives a line, and promises Sandwich, spaces, then 6.00. It sounds sure.
  **On screen:** AI chat, stage 3: Generate the item line
    - You: Now write the line for one item: the name Sandwich and the price 6. Use the names item and price. Tell me exactly what it prints.
    - AI (example answer): Here is the code. It prints `Sandwich            6.00`. [code `examples/ai_line_flawed.py`]
- **Narration:** Look at line 4 carefully.
  **On screen:** AI chat, stage 3: Generate the item line
    - You: Now write the line for one item: the name Sandwich and the price 6. Use the names item and price. Tell me exactly what it prints.
    - AI (example answer): Here is the code. It prints `Sandwich            6.00`. [code `examples/ai_line_flawed.py`]
- **Interaction:** "The AI says this prints `Sandwich            6.00`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** Asha runs it. It prints the curly brackets and the codes, as plain text! And there is no error message to warn her.
  **On screen:** AI chat, stage 3: Generate the item line
    - You: Now write the line for one item: the name Sandwich and the price 6. Use the names item and price. Tell me exactly what it prints.
    - AI (example answer): Here is the code. It prints `Sandwich            6.00`. [code `examples/ai_line_flawed.py`]
    - You: I ran it. This is what it printed:
- **Narration:** Stage 4: test. Asha compares the real output with her target, and gives the AI both.
  **On screen:** AI chat, stage 4: Test: compare with the target
    - You: I expected `Sandwich            6.00`, but it printed the curly brackets as text. Compare the two and tell me the cause.
- **Narration:** Now the AI names the cause. The f is missing, so the brackets are plain text. One letter fixes it.
  **On screen:** AI chat, stage 4: Test: compare with the target
    - You: I expected `Sandwich            6.00`, but it printed the curly brackets as text. Compare the two and tell me the cause.
    - AI (example answer): The `f` is missing before the opening quotation mark. Without it, the curly brackets are plain text. Add the `f`: [code `examples/ai_line_fixed.py`]
- **Narration:** Asha runs the fixed line. Sandwich, twelve spaces, 6.00. Exactly her target.
  **On screen:** AI chat, stage 4: Test: compare with the target
    - You: I expected `Sandwich            6.00`, but it printed the curly brackets as text. Compare the two and tell me the cause.
    - AI (example answer): The `f` is missing before the opening quotation mark. Without it, the curly brackets are plain text. Add the `f`: [code `examples/ai_line_fixed.py`]
    - You: I ran the fixed line:
- **Narration:** Stage 5: debug. Later, Asha copies a price from the menu sheet, with quotation marks around it. Python stops with a Value Error. She pastes the code and the full error.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I copied my price from the menu sheet, so I stored it with quotation marks. Now I get this error. First explain the cause and the line, then the smallest fix. [code `examples/ai_line_text_price.py`]
- **Narration:** She asks for the cause first. The AI explains that the f code only works for numbers, and the price is a string. The fix: remove the quotation marks.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I copied my price from the menu sheet, so I stored it with quotation marks. Now I get this error. First explain the cause and the line, then the smallest fix. [code `examples/ai_line_text_price.py`]
    - AI (example answer): It is a `ValueError` on line 4. The format code `f` only works for numbers, but `price` is the string `"6"`. The fix: store a number, `price = 6`, without quotation marks.
- **Narration:** Stage 6: improve. The line works. Asha asks for at most two improvements.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Review my receipt line. Suggest at most two improvements, each with one reason. Do not change what it prints. [code `examples/ai_line_fixed.py`]
- **Narration:** Suggestion 1 is good: test with a larger price. Suggestion 2 says dot 2 is the same as dot 2 f, only shorter.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Review my receipt line. Suggest at most two improvements, each with one reason. Do not change what it prints. [code `examples/ai_line_fixed.py`]
    - AI (example answer): 1. Test it with a second item and a larger price, such as 12.5, to check that the columns line up. 2. Use `.2` instead of `.2f`. Both mean two decimal places, and `.2` is shorter.
- **Narration:** Asha does not accept it yet. She tests both codes with two prices.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Review my receipt line. Suggest at most two improvements, each with one reason. Do not change what it prints. [code `examples/ai_line_fixed.py`]
    - AI (example answer): 1. Test it with a second item and a larger price, such as 12.5, to check that the columns line up. 2. Use `.2` instead of `.2f`. Both mean two decimal places, and `.2` is shorter.
    - You: Suggestion 2 would change the output. I tested it with two prices: [code `examples/ai_short_spec.py`]
- **Narration:** With dot 2 f, both prices show two decimal places: 3.50 and 12.50.
  **On screen:** Code `examples/ai_short_spec.py`, line 4 highlighted, output `examples/ai_short_spec.expected`
- **Narration:** With dot 2, the price 3.5 loses its zero. And 12.5 becomes one point two, e plus zero one. That is 12, in scientific notation!
  **On screen:** Code `examples/ai_short_spec.py`, line 5 highlighted, output `examples/ai_short_spec.expected`
- **Narration:** Dot 2 keeps two significant digits, not two decimal places. The AI was wrong again.
  **On screen:** Code `examples/ai_short_spec.py`, line 4, 5 highlighted, output `examples/ai_short_spec.expected`
- **Narration:** So Asha keeps suggestion 1 only. She tests a second item with a larger price, and keeps dot 2 f.
  **On screen:** Code `examples/ai_line_final.py`, line 6, 7 highlighted, output `examples/ai_line_final.expected`
- **Narration:** Both prices line up, with two decimals. Two AI mistakes caught, both by comparing the real output with the target.
  **On screen:** Code `examples/ai_line_final.py`, line 6, 7 highlighted, output `examples/ai_line_final.expected`
- **Narration:** Breather. You watched Asha use AI at all six stages, and catch two mistakes by comparing output with her target.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Paste the exact target output into your prompt.
    - Test a suggestion with more than one value.
- **Narration:** Next, the four errors beginners meet most often with text. You have met one already.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Paste the exact target output into your prompt.
    - Test a suggestion with more than one value.
- **Breather:** 4 quiet seconds.

## Scene 13: Common mistakes (13:39 to 15:47)

**Section:** Common mistakes

**Direction:** Mistake 1 calls back to Chapter 2. Mistakes 2 and 3 are spot-it questions on rules taught earlier. Mistake 4 calls back to the debug stage.

- **Narration:** Mistake 1. Asha joins text and a number with a plus sign. The plus sign only joins strings to strings.
  **On screen:** Code `examples/err01_join_number.py`, line 3 highlighted, error `examples/err01_join_number.expected_error`
- **Narration:** So Python stops with a Type Error, the same message you met in Chapter 2.
  **On screen:** Code `examples/err01_join_number.py`, line 3 highlighted, error `examples/err01_join_number.expected_error`
- **Narration:** The fix is an f string. It turns the number into text for you.
  **On screen:** Code `examples/err01_join_number.py`, line 3 highlighted, error `examples/err01_join_number.expected_error`
- **Narration:** Now you try. The table code has two characters. Remember where indexes start.
  **On screen:** Code `examples/err02_index_range.py`, line 2, 3, 4 highlighted, output hidden
- **Interaction:** "Line 3 works. What is wrong with line 4?" stays on screen with a 10-second timer.
- **Narration:** Index 2 does not exist. Two characters have the indexes 0 and 1 only, so Python reports an Index Error.
  **On screen:** Code `examples/err02_index_range.py`, line 4 highlighted, error `examples/err02_index_range.expected_error`
- **Narration:** The last index is always one less than the length. Or use minus 1 for the last character.
  **On screen:** Code `examples/err02_index_range.py`, line 4 highlighted, error `examples/err02_index_range.expected_error`
- **Narration:** One more. Asha wants a capital A at the start of the name. Think about the rule for changing strings.
  **On screen:** Code `examples/err03_change_letter.py`, line 2, 3 highlighted, output hidden
- **Interaction:** "What is wrong with line 3?" stays on screen with a 10-second timer.
- **Narration:** A string cannot be changed after it is made, not even one letter. Python says a string does not support item assignment.
  **On screen:** Code `examples/err03_change_letter.py`, line 3 highlighted, error `examples/err03_change_letter.expected_error`
- **Narration:** The fix: make a new string, for example with the title method, and give it the name.
  **On screen:** Code `examples/err03_change_letter.py`, line 3 highlighted, error `examples/err03_change_letter.expected_error`
- **Narration:** Mistake 4 is the Value Error Asha debugged with the AI: dot 2 f on a price in quotation marks. Store a number instead, and in Chapter 4 you will learn to turn text into a number.
  **On screen:** Code `examples/err04_format_text.py`, line 2, 3 highlighted, error `examples/err04_format_text.expected_error`
- **Narration:** Quick check. A string has 5 characters. What is its last index?
  **On screen:** Quick check: "A string has 5 characters. What is its last index?" (options shown)
- **Interaction:** "A string has 5 characters. What is its last index?" stays on screen with a 10-second timer.
- **Narration:** C, 4. Five characters have the indexes 0, 1, 2, 3 and 4.
  **On screen:** Quick check: "A string has 5 characters. What is its last index?" (answer revealed: 4)
- **Narration:** Last breather. These errors will not surprise you any more.
  **On screen:** Breather card
    - Use an f-string to mix text and numbers.
    - The last index is one less than the length.
    - Strings never change; make a new one.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - Use an f-string to mix text and numbers.
    - The last index is one less than the length.
    - Strings never change; make a new one.
- **Breather:** 4 quiet seconds.

## Scene 14: Think beyond (15:47 to 16:36)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Asha wants only the first letter of a customer's name, as a capital, for a table card. Which index and which method would you combine?
  **On screen:** Question card: "Asha wants only the first letter of a name, as a capital, on a table card. Which index and which method would you combine?"
- **Interaction:** "Asha wants only the first letter of a name, as a capital, on a table card. Which index and which method would you combine?" stays on screen with a 10-second timer.
- **Narration:** Write it and test it with the name omar, after the video.
  **On screen:** Question card: "Asha wants only the first letter of a name, as a capital, on a table card. Which index and which method would you combine?"
- **Narration:** Second. A new receipt printer is 32 characters wide. Which numbers in Asha's receipt would you change, so the columns still line up?
  **On screen:** Question card: "A new receipt printer is 32 characters wide. Which numbers in the receipt would you change?"
- **Interaction:** "A new receipt printer is 32 characters wide. Which numbers in the receipt would you change?" stays on screen with a 10-second timer.
- **Narration:** Predict the new output first, then test it.
  **On screen:** Question card: "A new receipt printer is 32 characters wide. Which numbers in the receipt would you change?"

## Scene 15: Recap (16:36 to 17:34)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap.
  **On screen:** Recap
- **Narration:** A string is a row of characters. Indexes start at 0, and minus 1 is the last.
  **On screen:** Recap
    - A string is a sequence of characters. Indexes start at 0; `-1` is the last.
- **Narration:** A plus sign joins strings. An f string puts values into text with curly brackets.
  **On screen:** Recap
    - A string is a sequence of characters. Indexes start at 0; `-1` is the last.
    - `+` joins strings. An f-string puts values into text with `{ }`.
- **Narration:** Dot 2 f shows two decimal places, and a number sets the width.
  **On screen:** Recap
    - A string is a sequence of characters. Indexes start at 0; `-1` is the last.
    - `+` joins strings. An f-string puts values into text with `{ }`.
    - `.2f` shows two decimal places. A number sets the width.
- **Narration:** The arrows align left and right, and the caret centres.
  **On screen:** Recap
    - A string is a sequence of characters. Indexes start at 0; `-1` is the last.
    - `+` joins strings. An f-string puts values into text with `{ }`.
    - `.2f` shows two decimal places. A number sets the width.
    - `<`, `>` and `^` align left, right and centre.
- **Narration:** Methods give you a new string. The original never changes.
  **On screen:** Recap
    - A string is a sequence of characters. Indexes start at 0; `-1` is the last.
    - `+` joins strings. An f-string puts values into text with `{ }`.
    - `.2f` shows two decimal places. A number sets the width.
    - `<`, `>` and `^` align left, right and centre.
    - Methods give you a new string. The original never changes.
- **Narration:** And with AI: show the exact output you want, and test with more than one value.
  **On screen:** Recap
    - A string is a sequence of characters. Indexes start at 0; `-1` is the last.
    - `+` joins strings. An f-string puts values into text with `{ }`.
    - `.2f` shows two decimal places. A number sets the width.
    - `<`, `>` and `^` align left, right and centre.
    - Methods give you a new string. The original never changes.
    - Show AI the exact output you want, and test with more than one value.
- **Narration:** One last check. Which line prints 7.00?
  **On screen:** Quick check: "Which line prints `7.00`?" (options shown)
- **Interaction:** "Which line prints `7.00`?" stays on screen with a 10-second timer.
- **Narration:** A. It needs both the f before the quotation mark, and dot 2 f inside the brackets.
  **On screen:** Quick check: "Which line prints `7.00`?" (answer revealed: `print(f"{7:.2f}")`)
- **Narration:** Mission complete! You earned 100 XP and the Wordsmith badge.
  **On screen:** Wordsmith You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 16: Practice (17:34 to 17:57)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. The practice file has eight tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's receipt line with two flaws.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Predict first, then run. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 17: What's next (17:57 to 18:19)

**Section:** What's next

**Direction:** End card. Tease input() as the fix for fixed values. Hold quietly at the end.

- **Narration:** Asha's receipt looks great. But every value is still typed into the code. Every customer gets two teas and a sandwich!
  **On screen:** Talking Back: Input and Type Conversion Let the customer type the order.
- **Narration:** In Chapter 4, your programs will ask questions, and use the answers the customer types.
  **On screen:** Talking Back: Input and Type Conversion Let the customer type the order.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Talking Back: Input and Type Conversion Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 4.
  **On screen:** Talking Back: Input and Type Conversion Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
