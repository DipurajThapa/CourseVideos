# Video Script: Chapter 4: Talking Back: Input and Type Conversion

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:21.

## Scene 1: Introduction (0:00 to 0:55)

**Section:** Introduction

**Direction:** Open on the limit from Chapter 3: one fixed order. Show the finished program asking questions as the mission, then the AI tease. No question yet.

- **Narration:** Welcome back to Code Quest. This is Chapter 4.
  **On screen:** Talking Back: Input and Type Conversion
- **Narration:** Today your programs start a conversation. They ask a question, listen to the answer, and calculate with it.
  **On screen:** Talking Back: Input and Type Conversion Ask. Listen. Convert. Calculate.
- **Narration:** And an AI assistant will promise you 7.50 of change. Instead, its program will crash.
  **On screen:** Talking Back: Input and Type Conversion Ask. Listen. Convert. Calculate.
- **Narration:** Remember Asha's receipt from Chapter 3? Neat columns, two decimal places. Very professional.
  **On screen:** One receipt for everybody
    - Asha's receipt from Chapter 3 is neat and lined up.
- **Narration:** But there is a problem. Every customer gets the same order, two teas and a sandwich.
  **On screen:** One receipt for everybody
    - Asha's receipt from Chapter 3 is neat and lined up.
    - But every customer gets the same order: two teas and a sandwich.
- **Narration:** Omar wants three teas? Asha has to open the code and change it. That is not how a real cafe program works.
  **On screen:** One receipt for everybody
    - Asha's receipt from Chapter 3 is neat and lined up.
    - But every customer gets the same order: two teas and a sandwich.
    - A new order means editing the code.
- **Narration:** So here is today's mission. The program asks the customer three questions.
  **On screen:** Code `examples/ex06_order.py`, line 2, 3, 4 highlighted, output `examples/ex06_order.expected`
- **Narration:** Then it prints the receipt for that order, and only that order.
  **On screen:** Code `examples/ex06_order.py`, line 16, 17, 18, 19, 20, 21, 22 highlighted, output `examples/ex06_order.expected`
- **Narration:** Different answers, different receipt, and not one line of code changes. Let's build it, piece by piece.
  **On screen:** Code `examples/ex06_order.py`, output `examples/ex06_order.expected`

## Scene 2: Learning goals (0:55 to 1:14)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Ask a question with input, and store the answer.
  **On screen:** By the end, you will be able to:
    - Ask a question with `input()` and store the answer.
- **Narration:** Explain why every answer is text, even when it looks like a number.
  **On screen:** By the end, you will be able to:
    - Ask a question with `input()` and store the answer.
    - Explain why every answer from `input()` is a string.
- **Narration:** Convert text into numbers, and numbers into text.
  **On screen:** By the end, you will be able to:
    - Ask a question with `input()` and store the answer.
    - Explain why every answer from `input()` is a string.
    - Convert text with `int()` and `float()`, and numbers with `str()`.
- **Narration:** Write a program that asks, converts and calculates.
  **On screen:** By the end, you will be able to:
    - Ask a question with `input()` and store the answer.
    - Explain why every answer from `input()` is a string.
    - Convert text with `int()` and `float()`, and numbers with `str()`.
    - Write a program that asks, converts and calculates.
- **Narration:** And fix the two errors that conversion causes most often.
  **On screen:** By the end, you will be able to:
    - Ask a question with `input()` and store the answer.
    - Explain why every answer from `input()` is a string.
    - Convert text with `int()` and `float()`, and numbers with `str()`.
    - Write a program that asks, converts and calculates.
    - Read and fix `TypeError` and `ValueError` from conversion.

## Scene 3: Why this matters (1:14 to 1:30)

**Section:** Why this matters

**Direction:** Connect asking questions to apps the learner uses every day.

- **Narration:** Real programs react to the person who uses them.
  **On screen:** Why this matters
    - Real programs react to the person who uses them.
- **Narration:** A cash machine asks how much money you want. A booking site asks how many guests are coming.
  **On screen:** Why this matters
    - Real programs react to the person who uses them.
    - A cash machine asks for an amount. A booking site asks for the number of guests.
- **Narration:** Each one asks a question, waits for your answer, and then uses it. Today, so will yours.
  **On screen:** Why this matters
    - Real programs react to the person who uses them.
    - A cash machine asks for an amount. A booking site asks for the number of guests.
    - Each one asks, waits for the answer, then uses it.

## Scene 4: The idea: every answer is text (1:30 to 3:04)

**Section:** The idea

**Direction:** Teach input() with the diagram, then the conversion table, then the waiter analogy. Then a quiz, then a breather.

- **Narration:** Here is the big idea. The function input shows a question, and then it waits.
  **On screen:** input() gives back text
- **Narration:** The user types an answer and presses Enter. Then input gives back exactly what they typed.
  **On screen:** input() gives back text
- **Narration:** And here is the important part. The answer is always a string. Even when the user types the digit 3, you get the text 3, not the number.
  **On screen:** input() gives back text
- **Narration:** To calculate with an answer, you convert it. Converting means making a new value of another type.
  **On screen:** Table: One conversion for each type
- **Narration:** Int makes a whole number. The text 3 becomes the number 3.
  **On screen:** Table: One conversion for each type (row 1 in focus)
- **Narration:** Float makes a decimal number, for prices like 4.25.
  **On screen:** Table: One conversion for each type (row 2 in focus)
- **Narration:** And str goes the other way. It turns a number into text.
  **On screen:** Table: One conversion for each type (row 3 in focus)
- **Narration:** Think of a waiter. Every order goes onto a paper slip. That is input: everything arrives as writing.
  **On screen:** Like a waiter's order slip
    - The waiter writes every order on a paper slip: that is `input()`.
- **Narration:** The kitchen cannot add up slips. It needs numbers. Conversion reads the slip and writes the number.
  **On screen:** Like a waiter's order slip
    - The waiter writes every order on a paper slip: that is `input()`.
    - The kitchen needs numbers to add up: conversion reads the slip.
- **Narration:** But unlike a person, a conversion cannot guess. If the slip says the word two, instead of the digit, it stops with an error.
  **On screen:** Like a waiter's order slip
    - The waiter writes every order on a paper slip: that is `input()`.
    - The kitchen needs numbers to add up: conversion reads the slip.
    - Unlike a person, a conversion cannot guess. "two" instead of "2" stops it with an error.
- **Narration:** Quick check. The user types 3 and presses Enter. What does input give back?
  **On screen:** Quick check: "The user types `3` and presses Enter. What does `input()` give back?" (options shown)
- **Interaction:** "The user types `3` and presses Enter. What does `input()` give back?" stays on screen with a 10-second timer.
- **Narration:** B. The string 3. Input always gives back text.
  **On screen:** Quick check: "The user types `3` and presses Enter. What does `input()` give back?" (answer revealed: The string `"3"`)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - `input()` asks and waits.
    - Every answer is a string.
    - `int()` and `float()` turn text into numbers.
- **Narration:** Next, Asha asks her first question.
  **On screen:** Breather card
    - `input()` asks and waits.
    - Every answer is a string.
    - `int()` and `float()` turn text into numbers.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Ask a question (3:04 to 3:52)

**Section:** Build it step by step

**Direction:** The file types itself in. Explain the prompt and the waiting, then ask what appears first, then reveal.

- **Narration:** Step 1. Line 2 asks the customer's name. The text inside input is the prompt, the question the user sees.
  **On screen:** Code `examples/ex01_input.py`, lines 1 to 2 typed in, line 2 highlighted, output hidden
- **Narration:** Notice the space after the question mark. It keeps the answer from touching the question.
  **On screen:** Code `examples/ex01_input.py`, lines 1 to 2 typed in, line 2 highlighted, output hidden
- **Narration:** Lines 3 and 4 greet the customer by name, with f strings from Chapter 3.
  **On screen:** Code `examples/ex01_input.py`, lines 1 to 4 typed in, line 3, 4 highlighted, output hidden
- **Interaction:** "The program starts. What appears on the screen first, before anyone types?" stays on screen with a 10-second timer.
- **Narration:** The prompt: What is your name? Then the program waits on line 2 until the user presses Enter.
  **On screen:** Code `examples/ex01_input.py`, lines 1 to 4 typed in, line 2 highlighted, output `examples/ex01_input.expected`
- **Narration:** In this course, the output shows the typed answer after each question, the way your terminal does. Here, the user typed Asha.
  **On screen:** Code `examples/ex01_input.py`, lines 1 to 4 typed in, line 2 highlighted, output `examples/ex01_input.expected`
- **Narration:** Then lines 3 and 4 use her answer.
  **On screen:** Code `examples/ex01_input.py`, lines 1 to 4 typed in, line 3, 4 highlighted, output `examples/ex01_input.expected`

## Scene 6: Step 2: Every answer is text (3:52 to 4:33)

**Section:** Build it step by step

**Direction:** Use type() to prove the answer is a string, then let the learner predict the repeat.

- **Narration:** Step 2. Asha asks how many teas, and the user types 3.
  **On screen:** Code `examples/ex02_text_answer.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 prints the answer and its type, with the type function from Chapter 2.
  **On screen:** Code `examples/ex02_text_answer.py`, line 3 highlighted, output hidden
- **Narration:** Line 4 multiplies the answer by 2. Remember the big idea about answers.
  **On screen:** Code `examples/ex02_text_answer.py`, line 4 highlighted, output hidden
- **Interaction:** "What do lines 3 and 4 print?" stays on screen with a 10-second timer.
- **Narration:** Line 3 shows class str. The answer is a string.
  **On screen:** Code `examples/ex02_text_answer.py`, line 3 highlighted, output `examples/ex02_text_answer.expected`
- **Narration:** So line 4 repeats the text, and prints 33. That is the same silent bug you met in Chapter 2: no error message, only a wrong answer!
  **On screen:** Code `examples/ex02_text_answer.py`, line 4 highlighted, output `examples/ex02_text_answer.expected`

## Scene 7: Step 3: Convert with int() (4:33 to 5:12)

**Section:** Build it step by step

**Direction:** Teach the inside-out order of int(input()), then the prediction.

- **Narration:** Step 3. The fix is to put input inside int.
  **On screen:** Code `examples/ex03_int.py`, line 2 highlighted, output hidden
- **Narration:** Python works from the inside out. First, input gives back the string 3. Then int turns it into the number 3.
  **On screen:** Code `examples/ex03_int.py`, line 2 highlighted, output hidden
- **Narration:** Line 4 checks the type again. Line 5 calculates the cost, with two decimal places.
  **On screen:** Code `examples/ex03_int.py`, line 4, 5 highlighted, output hidden
- **Interaction:** "The user types 3. What does line 5 print now?" stays on screen with a 10-second timer.
- **Narration:** Line 4 shows class int: a whole number.
  **On screen:** Code `examples/ex03_int.py`, line 4 highlighted, output `examples/ex03_int.expected`
- **Narration:** So line 5 really calculates. 3 teas cost 10.50.
  **On screen:** Code `examples/ex03_int.py`, line 5 highlighted, output `examples/ex03_int.expected`

## Scene 8: Step 4: Convert with float() (5:12 to 5:54)

**Section:** Build it step by step

**Direction:** Two questions, two conversions. Teach the rule for choosing, then predict the last line.

- **Narration:** Step 4. Remember the price stored as text in Chapter 3? You were promised a way to turn text into a number. Here it is: float. A price can have a decimal point, like 4.25, so line 2 uses float.
  **On screen:** Code `examples/ex04_float.py`, line 2 highlighted, output hidden
- **Narration:** A count is always whole, so line 3 uses int.
  **On screen:** Code `examples/ex04_float.py`, line 3 highlighted, output hidden
- **Narration:** Here is the rule. Use int for counts, and float for amounts of money.
  **On screen:** Code `examples/ex04_float.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 multiplies, and line 5 prints the total.
  **On screen:** Code `examples/ex04_float.py`, line 4, 5 highlighted, output hidden
- **Interaction:** "The user types 4.25, then 2. What does line 5 print?" stays on screen with a 10-second timer.
- **Narration:** Two questions, one after the other.
  **On screen:** Code `examples/ex04_float.py`, line 2, 3 highlighted, output `examples/ex04_float.expected`
- **Narration:** Then: 2 cakes cost 8.50.
  **On screen:** Code `examples/ex04_float.py`, line 5 highlighted, output `examples/ex04_float.expected`

## Scene 9: Step 5: What each conversion accepts (5:54 to 7:46)

**Section:** Build it step by step

**Direction:** Teach the general rules, ask about two lines, then reveal the surprises. Quiz, then a breather.

- **Narration:** Step 5. Conversions also work on values you write in the code. No questions this time.
  **On screen:** Code `examples/ex05_conversions.py`, line 2 highlighted, output hidden
- **Narration:** Remember the table: int makes a whole number from text, and str turns a number into text.
  **On screen:** Code `examples/ex05_conversions.py`, line 2, 7 highlighted, output hidden
- **Interaction:** "What do lines 2 and 7 print?" stays on screen with a 10-second timer.
- **Narration:** Line 2: the text 12 becomes the number 12, plus 1 is 13.
  **On screen:** Code `examples/ex05_conversions.py`, line 2 highlighted, output `examples/ex05_conversions.expected`
- **Narration:** Line 7: str turns 4 into text, so plus can join it to the word teas.
  **On screen:** Code `examples/ex05_conversions.py`, line 7 highlighted, output `examples/ex05_conversions.expected`
- **Narration:** Line 3: float turns the text 2.5 into a number, so times 2 gives 5.0.
  **On screen:** Code `examples/ex05_conversions.py`, line 3 highlighted, output `examples/ex05_conversions.expected`
- **Narration:** Now the surprises. Line 4: float accepts text without a decimal point, and adds point 0.
  **On screen:** Code `examples/ex05_conversions.py`, line 4 highlighted, output `examples/ex05_conversions.expected`
- **Narration:** Line 5: int on 3.9 gives 3. It cuts off the part after the point. It does not round!
  **On screen:** Code `examples/ex05_conversions.py`, line 5 highlighted, output `examples/ex05_conversions.expected`
- **Narration:** And line 6: int ignores spaces at the start and the end of the text.
  **On screen:** Code `examples/ex05_conversions.py`, line 6 highlighted, output `examples/ex05_conversions.expected`
- **Narration:** Careful with one difference. Int accepts the number 3.9, and cuts it down to 3.
  **On screen:** Code `examples/ex05_int_text.py`, line 2 highlighted, output `examples/ex05_int_text.expected`
- **Narration:** But the text 3.9, in quotation marks, is not a whole number. Int stops with a Value Error, instead of cutting off the decimals.
  **On screen:** Code `examples/ex05_int_text.py`, line 3 highlighted, output `examples/ex05_int_text.expected`, error `examples/ex05_int_text.expected_error`
- **Narration:** So for answers with a decimal point, use float.
  **On screen:** Code `examples/ex05_int_text.py`, line 3 highlighted, output `examples/ex05_int_text.expected`, error `examples/ex05_int_text.expected_error`
- **Narration:** Quick check. What does int of 7.8 give?
  **On screen:** Quick check: "What does `int(7.8)` give?" (options shown)
- **Interaction:** "What does `int(7.8)` give?" stays on screen with a 10-second timer.
- **Narration:** A, 7. Int cuts off the decimals. It does not round.
  **On screen:** Quick check: "What does `int(7.8)` give?" (answer revealed: `7`)
- **Narration:** Breather. Stretch your arms. You now have every piece of the mission.
  **On screen:** Breather card
    - `int()` for counts, `float()` for money.
    - Python works out `int(input(...))` from the inside out.
    - `int()` cuts off decimals.
- **Narration:** Let's put them together in Asha's receipt.
  **On screen:** Breather card
    - `int()` for counts, `float()` for money.
    - Python works out `int(input(...))` from the inside out.
    - `int()` cuts off decimals.
- **Breather:** 4 quiet seconds.

## Scene 10: See the outcome: a receipt that asks (7:46 to 9:01)

**Section:** See the outcome

**Direction:** Return to the mission. Walk every group of lines, reveal, ask which answer stays text, then hand over to the AI story.

- **Narration:** Back to the mission. Lines 2 to 4 ask the three questions. The two counts are converted with int.
  **On screen:** Code `examples/ex06_order.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Lines 5 and 6 store the prices, as before. To keep the program short, the member discount from Chapter 3 is left out this time.
  **On screen:** Code `examples/ex06_order.py`, line 5, 6 highlighted, output hidden
- **Narration:** Line 8 cleans the name with strip and title, from Chapter 3. Lines 9 to 11 calculate the totals.
  **On screen:** Code `examples/ex06_order.py`, line 8, 9, 10, 11 highlighted, output hidden
- **Narration:** Lines 12 to 14 build the two labels and the line, and lines 16 to 22 print the receipt.
  **On screen:** Code `examples/ex06_order.py`, line 12, 13, 14, 16, 17, 18, 19, 20, 21, 22 highlighted, output hidden
- **Narration:** Look at lines 2 to 4 once more. Which answer is different?
  **On screen:** Code `examples/ex06_order.py`, line 2, 3, 4 highlighted, output hidden
- **Interaction:** "Only one of the three answers is never converted. Which one, and why?" stays on screen with a 10-second timer.
- **Narration:** The name, on line 2. It is only cleaned and printed, never used in a calculation, so it can stay a string.
  **On screen:** Code `examples/ex06_order.py`, line 2, 8 highlighted, output hidden
- **Narration:** Now Asha runs it. The customer types omar with extra spaces, then 3 teas and 2 sandwiches.
  **On screen:** Code `examples/ex06_order.py`, output `examples/ex06_order.expected`
- **Narration:** And there is Omar's own receipt, with his name cleaned up. 22.50 to pay.
  **On screen:** Code `examples/ex06_order.py`, output `examples/ex06_order.expected`
- **Narration:** Mission complete! But Asha's cafe needs one more thing: how much change does the customer get? She builds it with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex06_order.py`, output `examples/ex06_order.expected`

## Scene 11: Work with AI: six stages, one change line (9:01 to 12:28)

**Section:** Work with AI

**Direction:** Safety and the skill first. Then one conversation per stage, all about the change. Stage 3 plants the mistake, stage 4 finds it, stage 5 fixes it with the exact error, stage 6 catches a second one.

- **Narration:** This chapter's AI skill is debugging with the exact error.
  **On screen:** This chapter's AI skill: the exact error
- **Narration:** When a program stops, copy the full error message and the code into your prompt.
  **On screen:** This chapter's AI skill: the exact error
    - When a program stops, copy the full error and the code.
- **Narration:** Ask for the cause first. Only then ask for the smallest fix. A fix you do not understand will break again.
  **On screen:** This chapter's AI skill: the exact error
    - When a program stops, copy the full error and the code.
    - Ask for the cause first, and only then for the smallest fix.
- **Narration:** And the safety habits from Chapter 1 still apply.
  **On screen:** This chapter's AI skill: the exact error
    - When a program stops, copy the full error and the code.
    - Ask for the cause first, and only then for the smallest fix.
    - Never paste passwords or private data. You are responsible for the code you use.
- **Narration:** Stage 1: plan. Asha describes the change feature, and asks which type the answer needs. No code yet.
  **On screen:** AI chat, stage 1: Plan: the questions and their types
    - You: I am a beginner learning input(). After the receipt, I want to ask how much the customer paid and print the change. Do not write code yet. List the steps, and say which type the answer needs.
- **Narration:** The AI lists four steps. Step 2 converts with float, because money can have decimals. That matches the rule from step 4.
  **On screen:** AI chat, stage 1: Plan: the questions and their types
    - You: I am a beginner learning input(). After the receipt, I want to ask how much the customer paid and print the change. Do not write code yet. List the steps, and say which type the answer needs.
    - AI (example answer): 1. Ask `Amount paid? ` with `input()`. 2. Convert the answer with `float()`, because money can have decimals. 3. Subtract the bill from the amount paid. 4. Print the change with `.2f`.
- **Narration:** Stage 2: write. Asha writes the question line herself, and asks the AI to explain it from the inside out.
  **On screen:** AI chat, stage 2: Write it yourself, then explain it
    - You: I wrote the question line myself. Do not change it. Explain the order in which Python works it out, and the type after each step. [code `examples/ai_change_fixed.py`]
- **Narration:** Input first, then float, then the name. Exactly the order you learned in step 3.
  **On screen:** AI chat, stage 2: Write it yourself, then explain it
    - You: I wrote the question line myself. Do not change it. Explain the order in which Python works it out, and the type after each step. [code `examples/ai_change_fixed.py`]
    - AI (example answer): 1. `input()` shows `Amount paid? ` and gives back the text the customer types, such as `"30"`. 2. `float()` turns that text into the number 30.0. 3. The name `paid` now refers to 30.0, a `float`.
- **Narration:** Stage 3: generate. Asha asks the AI for the whole program, to compare it with hers.
  **On screen:** AI chat, stage 3: Generate: compare with an AI version
    - You: Now write the whole change program, so I can compare it with mine. The bill is 22.5. Use the names to_pay, paid and change. If I type 30, tell me exactly what it prints.
- **Narration:** The AI promises: type 30, and it prints change 7.50. It sounds sure.
  **On screen:** AI chat, stage 3: Generate: compare with an AI version
    - You: Now write the whole change program, so I can compare it with mine. The bill is 22.5. Use the names to_pay, paid and change. If I type 30, tell me exactly what it prints.
    - AI (example answer): Here is the program. If you type 30, it prints `Change: 7.50`. [code `examples/ai_change_flawed.py`]
- **Narration:** Check every line before you trust it.
  **On screen:** AI chat, stage 3: Generate: compare with an AI version
    - You: Now write the whole change program, so I can compare it with mine. The bill is 22.5. Use the names to_pay, paid and change. If I type 30, tell me exactly what it prints.
    - AI (example answer): Here is the program. If you type 30, it prints `Change: 7.50`. [code `examples/ai_change_flawed.py`]
- **Interaction:** "The AI says that typing 30 prints `Change: 7.50`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No! Its line 3 has input, but no float. The answer stays text. Let's see what happens when Asha tests it.
  **On screen:** AI chat, stage 3: Generate: compare with an AI version
    - You: Now write the whole change program, so I can compare it with mine. The bill is 22.5. Use the names to_pay, paid and change. If I type 30, tell me exactly what it prints.
    - AI (example answer): Here is the program. If you type 30, it prints `Change: 7.50`. [code `examples/ai_change_flawed.py`]
- **Narration:** Stage 4: test. Asha asks for three test answers, with the result each one should give.
  **On screen:** AI chat, stage 4: Test: try the AI's own answers
    - You: Before I trust it, give me three answers to test it with, and what each one should print.
- **Narration:** The AI suggests 30, 22.5, and 25.50.
  **On screen:** AI chat, stage 4: Test: try the AI's own answers
    - You: Before I trust it, give me three answers to test it with, and what each one should print.
    - AI (example answer): 1. `30` prints `Change: 7.50`. 2. `22.5` prints `Change: 0.00`. 3. `25.50` prints `Change: 3.00`.
- **Narration:** She tries the first one. The program shows the question, and then it stops with an error.
  **On screen:** AI chat, stage 4: Test: try the AI's own answers
    - You: Before I trust it, give me three answers to test it with, and what each one should print.
    - AI (example answer): 1. `30` prints `Change: 7.50`. 2. `22.5` prints `Change: 0.00`. 3. `25.50` prints `Change: 3.00`.
    - You: I tried your first answer, 30. It did not print the change. It showed the question, then stopped with an error.
- **Narration:** Stage 5: debug. This is today's skill. Asha pastes the code, her answer and the full error. A Type Error on line 4.
  **On screen:** AI chat, stage 5: Debug: the exact error, the cause first
    - You: Here is the code and the full error. I typed 30. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_change_flawed.py`]
- **Narration:** She asks for the cause first. The AI explains: input gives back a string, and you cannot subtract a number from text. The fix is float.
  **On screen:** AI chat, stage 5: Debug: the exact error, the cause first
    - You: Here is the code and the full error. I typed 30. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_change_flawed.py`]
    - AI (example answer): Line 4 subtracts a number from text. `input()` on line 3 gives back a string, and the code never converts it. Put `float()` around `input()`: [code `examples/ai_change_fixed.py`]
- **Narration:** She runs the fix and types 30. Change: 7.50. Now the promise is true.
  **On screen:** AI chat, stage 5: Debug: the exact error, the cause first
    - You: Here is the code and the full error. I typed 30. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_change_flawed.py`]
    - AI (example answer): Line 4 subtracts a number from text. `input()` on line 3 gives back a string, and the code never converts it. Put `float()` around `input()`: [code `examples/ai_change_fixed.py`]
    - You: I ran the fix and typed 30:
- **Narration:** Stage 6: improve. Asha asks for at most two improvements that do not change the output.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Review my program. Suggest at most two improvements, each with one reason. Do not change what it prints for any answer.
- **Narration:** Suggestion 1, a clearer name, helps. Suggestion 2 says: use int, because customers pay with whole notes.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Review my program. Suggest at most two improvements, each with one reason. Do not change what it prints for any answer.
    - AI (example answer): 1. Rename `paid` to `amount_paid`, so a reader knows what the number is. 2. Use `int()` instead of `float()`. Customers usually pay with whole notes, and whole numbers are simpler.
- **Narration:** Asha uses the AI's own test answer, 25.50. Int cannot read text with a decimal point. Value Error! The AI was wrong again.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Review my program. Suggest at most two improvements, each with one reason. Do not change what it prints for any answer.
    - AI (example answer): 1. Rename `paid` to `amount_paid`, so a reader knows what the number is. 2. Use `int()` instead of `float()`. Customers usually pay with whole notes, and whole numbers are simpler.
    - You: Suggestion 2 fails your own test answer, 25.50. I tried it: [pasted error from `examples/ai_change_int.py`]
- **Narration:** So Asha keeps suggestion 1 only: the clearer name, amount paid, with float.
  **On screen:** Code `examples/ai_change_final.py`, line 3 highlighted, output `examples/ai_change_final.expected`
- **Narration:** She tests it with 25.50. Change: 3.00. The AI helped at every stage, and Asha checked every answer.
  **On screen:** Code `examples/ai_change_final.py`, line 3 highlighted, output `examples/ai_change_final.expected`
- **Narration:** Quick check. Your program stops after you type an answer. What do you paste into the AI prompt?
  **On screen:** Quick check: "Your program stops with an error after you type an answer. What do you paste into the AI prompt?" (options shown)
- **Interaction:** "Your program stops with an error after you type an answer. What do you paste into the AI prompt?" stays on screen with a 10-second timer.
- **Narration:** D. The code, your answer and the full error. Then ask for the cause first.
  **On screen:** Quick check: "Your program stops with an error after you type an answer. What do you paste into the AI prompt?" (answer revealed: The code, the answer you typed and the full error)
- **Narration:** Breather. You watched Asha catch two AI mistakes, with what you learned today.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Paste the exact error. Ask for the cause first.
    - Test each suggestion with more than one answer.
- **Narration:** Next, the four mistakes beginners make most with input. You have already seen two of them.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Paste the exact error. Ask for the cause first.
    - Test each suggestion with more than one answer.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes (12:28 to 14:45)

**Section:** Common mistakes

**Direction:** Mistakes 1 and 2 call back to the AI stages. Mistakes 3 and 4 are spot-it questions on rules taught earlier.

- **Narration:** Mistake 1 is the same kind of mistake as the AI's first one. Line 2 reads the answer, but never converts it.
  **On screen:** Code `examples/err01_add_text.py`, line 2 highlighted, error `examples/err01_add_text.expected_error`
- **Narration:** So line 3 tries to add 1 to the text 3, and Python stops with a Type Error. With plus, the message says can only concatenate. With minus, it said unsupported operand. The cause is the same.
  **On screen:** Code `examples/err01_add_text.py`, line 3 highlighted, error `examples/err01_add_text.expected_error`
- **Narration:** The fix: convert the answer where you read it, with int around input.
  **On screen:** Code `examples/err01_add_text.py`, line 2 highlighted, error `examples/err01_add_text.expected_error`
- **Narration:** Mistake 2 is the AI's second mistake. Int for a price. The user types 4.25, and int cannot read it.
  **On screen:** Code `examples/err02_int_decimal.py`, line 2 highlighted, error `examples/err02_int_decimal.expected_error`
- **Narration:** The message says invalid literal with base 10. A literal is the text Python tried to read, and base 10 means normal digits. The fix: use float for money.
  **On screen:** Code `examples/err02_int_decimal.py`, line 2 highlighted, error `examples/err02_int_decimal.expected_error`
- **Narration:** Now you try. The user answers with a word. Remember the waiter's slip from the idea section.
  **On screen:** Code `examples/err03_word.py`, line 2 highlighted, output hidden
- **Interaction:** "The user types `two`. What happens on line 2?" stays on screen with a 10-second timer.
- **Narration:** A Value Error. Int cannot guess that the word two means 2.
  **On screen:** Code `examples/err03_word.py`, line 2 highlighted, error `examples/err03_word.expected_error`
- **Narration:** For now, make the prompt say what to type. In later chapters, you will learn to check an answer before you convert it.
  **On screen:** Code `examples/err03_word.py`, line 2 highlighted, error `examples/err03_word.expected_error`
- **Narration:** One more. Count the brackets on line 2, like Asha learned in Chapter 1.
  **On screen:** Code `examples/err04_bracket.py`, line 2 highlighted, output hidden
- **Interaction:** "What is missing on line 2?" stays on screen with a 10-second timer.
- **Narration:** A closing bracket. Int and input each open one, so the line needs two closing brackets.
  **On screen:** Code `examples/err04_bracket.py`, line 2 highlighted, error `examples/err04_bracket.expected_error`
- **Narration:** This is a syntax error, so the program never even asks the question.
  **On screen:** Code `examples/err04_bracket.py`, line 2 highlighted, error `examples/err04_bracket.expected_error`
- **Narration:** Quick check. Which line reads a price that can have decimals?
  **On screen:** Quick check: "Which line reads a price that can have decimals?" (options shown)
- **Interaction:** "Which line reads a price that can have decimals?" stays on screen with a 10-second timer.
- **Narration:** C. Float around input. Option A keeps text, and option B fails for 4.25.
  **On screen:** Quick check: "Which line reads a price that can have decimals?" (answer revealed: `price = float(input("Price? "))`)
- **Narration:** Last breather. These errors will not surprise you any more.
  **On screen:** Breather card
    - Convert an answer where you read it.
    - `float()` for money, `int()` for counts.
    - Count your brackets.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - Convert an answer where you read it.
    - `float()` for money, `int()` for counts.
    - Count your brackets.
- **Breather:** 4 quiet seconds.

## Scene 13: Think beyond (14:45 to 15:33)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. A customer types 2.0 for the number of teas. What happens with int? And how could float and int together accept it?
  **On screen:** Question card: "A customer types `2.0` teas. What does `int()` do? How could `float()` and `int()` together accept it?"
- **Interaction:** "A customer types `2.0` teas. What does `int()` do? How could `float()` and `int()` together accept it?" stays on screen with a 10-second timer.
- **Narration:** Predict it, then test it after the video.
  **On screen:** Question card: "A customer types `2.0` teas. What does `int()` do? How could `float()` and `int()` together accept it?"
- **Narration:** Second. Asha wants the program to ask for the price of tea, instead of fixing it at 3.5. Which line changes, and which conversion fits?
  **On screen:** Question card: "Asha wants to ask for the price of tea too. Which line changes, and which conversion fits?"
- **Interaction:** "Asha wants to ask for the price of tea too. Which line changes, and which conversion fits?" stays on screen with a 10-second timer.
- **Narration:** Write it, and test it with a price that has decimals.
  **On screen:** Question card: "Asha wants to ask for the price of tea too. Which line changes, and which conversion fits?"

## Scene 14: Recap (15:33 to 16:30)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap.
  **On screen:** Recap
- **Narration:** Input shows a prompt, and gives back the answer as a string.
  **On screen:** Recap
    - `input()` shows a prompt and gives back the answer as a string.
- **Narration:** Int makes a whole number, float a decimal number, and str makes text.
  **On screen:** Recap
    - `input()` shows a prompt and gives back the answer as a string.
    - `int()` makes a whole number, `float()` a decimal number, `str()` text.
- **Narration:** Python works out int of input from the inside out.
  **On screen:** Recap
    - `input()` shows a prompt and gives back the answer as a string.
    - `int()` makes a whole number, `float()` a decimal number, `str()` text.
    - Python works out `int(input(...))` from the inside out.
- **Narration:** Int cuts off decimals, and it cannot read 4.25 or the word two.
  **On screen:** Recap
    - `input()` shows a prompt and gives back the answer as a string.
    - `int()` makes a whole number, `float()` a decimal number, `str()` text.
    - Python works out `int(input(...))` from the inside out.
    - `int()` cuts off decimals. It cannot read `"4.25"` or `"two"`.
- **Narration:** And with AI: paste the code, your answer and the full error, and ask for the cause first.
  **On screen:** Recap
    - `input()` shows a prompt and gives back the answer as a string.
    - `int()` makes a whole number, `float()` a decimal number, `str()` text.
    - Python works out `int(input(...))` from the inside out.
    - `int()` cuts off decimals. It cannot read `"4.25"` or `"two"`.
    - Give AI the code, your answer and the full error. Ask for the cause first.
- **Narration:** One last check. The answer is not converted, and the user types 2. What does tea count times 3 show?
  **On screen:** Quick check: "`tea_count = input("How many teas? ")` and the user types `2`. What does `print(tea_count * 3)` show?" (options shown)
- **Interaction:** "`tea_count = input("How many teas? ")` and the user types `2`. What does `print(tea_count * 3)` show?" stays on screen with a 10-second timer.
- **Narration:** B. 222. The answer is text, so times 3 repeats it. Convert first!
  **On screen:** Quick check: "`tea_count = input("How many teas? ")` and the user types `2`. What does `print(tea_count * 3)` show?" (answer revealed: `222`)
- **Narration:** Mission complete! You earned 100 XP and the Listener badge.
  **On screen:** Listener You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice (16:30 to 16:57)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. The practice file has eight tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including one receipt line that asks for its item.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, an AI's ticket program has two flaws. Fix them one error at a time.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Predict first, then run. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 16: What's next (16:57 to 17:21)

**Section:** What's next

**Direction:** End card. Tease the first boss level. Hold quietly at the end.

- **Narration:** Four friends finish their meal at the Corner Cafe. They want to add a tip and share the bill. Who pays how much?
  **On screen:** Boss Level 1: The Bill Splitter Share a cafe bill fairly between friends.
- **Narration:** In Chapter 5, the first boss level, you will build a bill splitter. It asks for the total, the tip and the number of people, then prints each share.
  **On screen:** Boss Level 1: The Bill Splitter Share a cafe bill fairly between friends.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Boss Level 1: The Bill Splitter Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you at the boss level.
  **On screen:** Boss Level 1: The Bill Splitter Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
