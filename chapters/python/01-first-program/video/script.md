# Video Script: Chapter 1: Your First Program and Your AI Study Partner

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:09.

## Scene 1: Introduction (0:00 to 0:37)

**Section:** Introduction

**Direction:** Open on the mission. Show the finished receipt as the destination, with no question yet. Introduce Asha and the AI assistant that will make one mistake.

- **Narration:** Welcome to Code Quest, Chapter 1.
  **On screen:** Your First Program and Your AI Study Partner
- **Narration:** Today you will write your first Python program, and you will learn to work with an AI assistant.
  **On screen:** Your First Program and Your AI Study Partner Write it. Run it. Check the AI.
- **Narration:** Meet Asha. She helps at her family's cafe, the Corner Cafe.
  **On screen:** Code `examples/ex04_receipt.py`, output `examples/ex04_receipt.expected`
- **Narration:** Her mission today is to make the computer print this receipt.
  **On screen:** Code `examples/ex04_receipt.py`, output `examples/ex04_receipt.expected`
- **Narration:** By the end of this video, you will understand every line of this program, and you will be able to build it yourself.
  **On screen:** Code `examples/ex04_receipt.py`, line 5, 6, 7, 8 highlighted, output `examples/ex04_receipt.expected`
- **Narration:** Along the way, an AI assistant will be confidently wrong. Your job is to catch it.
  **On screen:** Code `examples/ex04_receipt.py`, output `examples/ex04_receipt.expected`

## Scene 2: Learning goals (0:37 to 1:05)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Here is the plan. Each goal is one piece of the mission.
  **On screen:** By the end, you will be able to:
- **Narration:** Run a Python file and see its output.
  **On screen:** By the end, you will be able to:
    - Run a Python file and see its output.
- **Narration:** Explain how Python runs a program, from top to bottom.
  **On screen:** By the end, you will be able to:
    - Run a Python file and see its output.
    - Explain how Python runs a program: top to bottom, one line at a time.
- **Narration:** Control spacing with print, sep and end.
  **On screen:** By the end, you will be able to:
    - Run a Python file and see its output.
    - Explain how Python runs a program: top to bottom, one line at a time.
    - Use `print()` with `sep` and `end` to control spacing.
- **Narration:** Read an error message and find the line that caused it.
  **On screen:** By the end, you will be able to:
    - Run a Python file and see its output.
    - Explain how Python runs a program: top to bottom, one line at a time.
    - Use `print()` with `sep` and `end` to control spacing.
    - Read an error message and find the line that caused it.
- **Narration:** And use an AI assistant at every stage, safely, while you check its answers.
  **On screen:** By the end, you will be able to:
    - Run a Python file and see its output.
    - Explain how Python runs a program: top to bottom, one line at a time.
    - Use `print()` with `sep` and `end` to control spacing.
    - Read an error message and find the line that caused it.
    - Use an AI assistant at every stage, safely, and check its answers.

## Scene 3: Why this matters (1:05 to 1:35)

**Section:** Why this matters

**Direction:** Tie the idea of a program to the cafe, then to AI.

- **Narration:** A program is a list of instructions that a computer follows exactly.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
- **Narration:** The till at Asha's cafe runs one. So do train timetables and calculators.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
    - The cafe's till, a train timetable and a calculator all run programs.
- **Narration:** AI assistants such as ChatGPT and Claude can write code. They are often right. Sometimes they are wrong, and still sound sure.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
    - The cafe's till, a train timetable and a calculator all run programs.
    - AI can write code. It is often right, and sometimes wrong while sounding sure.
- **Narration:** So you are the one who runs the code, and decides if it is correct.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
    - The cafe's till, a train timetable and a calculator all run programs.
    - AI can write code. It is often right, and sometimes wrong while sounding sure.
    - **You** run the code. **You** decide if it is correct.

## Scene 4: The idea: Python reads from top to bottom (1:35 to 3:00)

**Section:** The idea

**Direction:** Teach the model with the diagram, the two key words and the recipe, then check it with a quiz, then a breather.

- **Narration:** Here is the big idea. A Python program is a text file that ends in dot p y.
  **On screen:** How Python runs a program
- **Narration:** Python, the program called the interpreter, reads it and carries out each line in order: top to bottom, one line at a time.
  **On screen:** How Python runs a program
- **Narration:** Print is a function: a named action that Python already knows. You call it with its name, then brackets.
  **On screen:** Two words you need
    - A **function** is a named action Python already knows. Call it with its name and brackets: `print(...)`.
- **Narration:** And text inside quotation marks is called a string.
  **On screen:** Two words you need
    - A **function** is a named action Python already knows. Call it with its name and brackets: `print(...)`.
    - A **string** is text inside quotation marks: `"Hello"`.
- **Narration:** Think of a recipe card in Asha's kitchen. The cook follows each step in order.
  **On screen:** A program is like a cafe recipe
    - The cook follows each step in order, exactly as written.
- **Narration:** The comparison stops at one point. A cook can guess what you meant. Python cannot.
  **On screen:** A program is like a cafe recipe
    - The cook follows each step in order, exactly as written.
    - Where it stops working: a cook can guess what you meant. Python cannot.
- **Narration:** One typing mistake, and Python stops with an error.
  **On screen:** A program is like a cafe recipe
    - The cook follows each step in order, exactly as written.
    - Where it stops working: a cook can guess what you meant. Python cannot.
    - A typing mistake makes Python stop and report an error.
- **Narration:** Let's check that idea. A file has three print lines. In which order does Python run them?
  **On screen:** Quick check: "A file has three `print()` lines. In which order does Python run them?" (options shown)
- **Interaction:** "A file has three `print()` lines. In which order does Python run them?" stays on screen with a 10-second timer.
- **Narration:** B. From top to bottom, one line at a time.
  **On screen:** Quick check: "A file has three `print()` lines. In which order does Python run them?" (answer revealed: From top to bottom, one line at a time)
- **Narration:** Take a short breather. Here is what you know so far.
  **On screen:** Breather card
    - A program is a list of instructions.
    - Python runs it from top to bottom.
    - Text in quotation marks is a string.
- **Narration:** Next, Asha installs Python and writes her very first line.
  **On screen:** Breather card
    - A program is a list of instructions.
    - Python runs it from top to bottom.
    - Text in quotation marks is a string.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Install Python (3:00 to 3:46)

**Section:** Build it step by step

**Direction:** Each system's row is highlighted as it is spoken.

- **Narration:** Step 1: install Python. Get the latest version. Any version from 3.12 works for this course.
  **On screen:** Table: Step 1: Install Python
- **Narration:** On Windows, use the Python install manager from python dot org or the Microsoft Store.
  **On screen:** Table: Step 1: Install Python (row 1 in focus)
- **Narration:** On macOS, download the installer package from python dot org.
  **On screen:** Table: Step 1: Install Python (row 2 in focus)
- **Narration:** On Linux, Python is usually installed already.
  **On screen:** Table: Step 1: Install Python (row 3 in focus)
- **Narration:** Then open a terminal and check the version.
  **On screen:** Table: Check the version
- **Narration:** On Windows, type python, space, dash dash version.
  **On screen:** Table: Check the version (row 1 in focus)
- **Narration:** On macOS and Linux, type python3 instead. You should see a line that starts with Python 3.
  **On screen:** Table: Check the version (row 2 in focus)

## Scene 6: Steps 2 and 3: Asha's first program (3:46 to 4:42)

**Section:** Build it step by step

**Direction:** The file types itself in, line by line. Then the run command, then the output.

- **Narration:** Step 2. Asha opens a code editor, such as Visual Studio Code or IDLE, and creates a file called ex 0 1 hello.
  **On screen:** Code `examples/ex01_hello.py`, lines 1 to 1 typed in, output hidden
- **Narration:** Line 1 starts with a hash sign, so it is a comment. Python ignores it. Comments are notes for people.
  **On screen:** Code `examples/ex01_hello.py`, lines 1 to 1 typed in, line 1 highlighted, output hidden
- **Narration:** Line 2 prints a greeting with her name.
  **On screen:** Code `examples/ex01_hello.py`, lines 1 to 2 typed in, line 2 highlighted, output hidden
- **Narration:** Line 3 prints a second line.
  **On screen:** Code `examples/ex01_hello.py`, lines 1 to 3 typed in, line 3 highlighted, output hidden
- **Narration:** Step 3: run it. In the terminal, go to the folder that holds the file.
  **On screen:** Table: Step 3: Run the file
- **Narration:** On Windows, type python, then the file name.
  **On screen:** Table: Step 3: Run the file (row 1 in focus)
- **Narration:** On macOS and Linux, type python3, then the file name.
  **On screen:** Table: Step 3: Run the file (row 2 in focus)
- **Narration:** And there it is: two lines. Each print makes one line of output.
  **On screen:** Code `examples/ex01_hello.py`, line 2, 3 highlighted, output `examples/ex01_hello.expected`
- **Narration:** The quotation marks do not appear. They only mark where the text starts and ends.
  **On screen:** Code `examples/ex01_hello.py`, line 2, 3 highlighted, output `examples/ex01_hello.expected`

## Scene 7: Step 4: Order matters (4:42 to 5:27)

**Section:** Build it step by step

**Direction:** Use the cafe's tea recipe. The steps type in, then the learner predicts the order, then the reveal.

- **Narration:** Step 4. Asha writes the cafe's tea recipe as a program. Step 1, boil the water.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 2 typed in, line 2 highlighted, output hidden
- **Narration:** Step 2, add the tea leaves.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 3 typed in, line 3 highlighted, output hidden
- **Narration:** Step 3, pour the tea into a cup.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 4 typed in, line 4 highlighted, output hidden
- **Narration:** You know how Python reads a file. Use that now.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 4 typed in, line 2, 3, 4 highlighted, output hidden
- **Interaction:** "In which order will the three steps appear in the output?" stays on screen with a 10-second timer.
- **Narration:** The same order as the code. Step 1, step 2, step 3.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 4 typed in, line 2, 3, 4 highlighted, output `examples/ex02_order.expected`
- **Narration:** Swap two lines in your file and run it again. The output changes, because Python always runs from top to bottom.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 4 typed in, output `examples/ex02_order.expected`

## Scene 8: Step 5: Spacing with sep and end (5:27 to 7:19)

**Section:** Build it step by step

**Direction:** Teach the two settings first, then the code, then the prediction, then a quick check, then a breather.

- **Narration:** Step 5. The receipt needs neat spacing, so Asha learns two settings. Print can show several values, separated by commas.
  **On screen:** Table: Step 5: Two settings of `print()`
- **Narration:** Sep sets what goes between the values. By default, it is one space.
  **On screen:** Table: Step 5: Two settings of `print()` (row 1 in focus)
- **Narration:** End sets what goes after the last value. By default, it is a new line.
  **On screen:** Table: Step 5: Two settings of `print()` (row 2 in focus)
- **Narration:** Line 2 has a calculation, 3 plus 4, with no quotation marks.
  **On screen:** Code `examples/ex03_many_values.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 prints the cafe's opening time, and sets sep to a colon.
  **On screen:** Code `examples/ex03_many_values.py`, line 3 highlighted, output hidden
- **Narration:** Line 4 sets end to three dots, and line 5 prints the word done.
  **On screen:** Code `examples/ex03_many_values.py`, line 4, 5 highlighted, output hidden
- **Interaction:** "What do lines 4 and 5 print together?" stays on screen with a 10-second timer.
- **Narration:** Line 2 prints 7, because Python calculates anything without quotation marks.
  **On screen:** Code `examples/ex03_many_values.py`, line 2 highlighted, output `examples/ex03_many_values.expected`
- **Narration:** Line 3 joins the values with colons, so they look like a time.
  **On screen:** Code `examples/ex03_many_values.py`, line 3 highlighted, output `examples/ex03_many_values.expected`
- **Narration:** And line 4 ends with three dots instead of a new line, so line 5 continues on the same line: Loading, dot dot dot, done.
  **On screen:** Code `examples/ex03_many_values.py`, line 4, 5 highlighted, output `examples/ex03_many_values.expected`
- **Narration:** Quick check. Which setting changes what goes between the values?
  **On screen:** Quick check: "Which setting changes what goes **between** the values in `print()`?" (options shown)
- **Interaction:** "Which setting changes what goes **between** the values in `print()`?" stays on screen with a 10-second timer.
- **Narration:** B, sep. Sep goes between. End goes after.
  **On screen:** Quick check: "Which setting changes what goes **between** the values in `print()`?" (answer revealed: `sep`)
- **Narration:** Breather. Relax your shoulders. Look at how much you can already do.
  **On screen:** Breather card
    - You can run a Python file.
    - Each `print()` makes one line.
    - `sep` goes between values; `end` goes after them.
- **Narration:** Now Asha has every piece she needs for the receipt.
  **On screen:** Breather card
    - You can run a Python file.
    - Each `print()` makes one line.
    - `sep` goes between values; `end` goes after them.
- **Breather:** 4 quiet seconds.

## Scene 9: See the outcome: the cafe receipt (7:19 to 8:10)

**Section:** See the outcome

**Direction:** Return to the mission from the opening. Walk the code in groups, connect each group to what was taught, reveal, then ask. End by handing over to the AI story.

- **Narration:** Remember the receipt from the start? Now you can read every line. Lines 2 to 4 print the header, top to bottom.
  **On screen:** Code `examples/ex04_receipt.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Lines 5 and 6 use sep to draw the dots between each item and its price.
  **On screen:** Code `examples/ex04_receipt.py`, line 5, 6 highlighted, output hidden
- **Narration:** Lines 7 and 8 print the item count and the total.
  **On screen:** Code `examples/ex04_receipt.py`, line 7, 8 highlighted, output hidden
- **Narration:** Asha runs it.
  **On screen:** Code `examples/ex04_receipt.py`, output `examples/ex04_receipt.expected`
- **Interaction:** "Which two output lines did Python calculate by itself?" stays on screen with a 10-second timer.
- **Narration:** Items 2, and Total U S D 10. Python worked out 1 plus 1, and 3 plus 7.
  **On screen:** Code `examples/ex04_receipt.py`, line 7, 8 highlighted, output `examples/ex04_receipt.expected`
- **Narration:** The receipt works. But it has no order code. Asha wants to add one, and she will use an AI assistant to help, one stage at a time.
  **On screen:** Code `examples/ex04_receipt.py`, line 3 highlighted, output `examples/ex04_receipt.expected`

## Scene 10: Work with AI: six stages, one receipt (8:10 to 12:41)

**Section:** Work with AI

**Direction:** Safety habits first. Then one real conversation per stage, all about adding an order code to the same receipt. Stage 3 plants the AI mistake; stage 4 catches it with a test; stage 6 catches a second one by counting.

- **Narration:** Before Asha opens an AI assistant, she follows three safety habits.
  **On screen:** Three safety habits
- **Narration:** One. Never paste passwords, keys or private information.
  **On screen:** Three safety habits
    - Never paste passwords, keys or private information into an AI tool.
- **Narration:** Two. Run every piece of AI code yourself, and compare it with what you asked for.
  **On screen:** Three safety habits
    - Never paste passwords, keys or private information into an AI tool.
    - Run every piece of AI code yourself, and compare it with what you asked for.
- **Narration:** Three. You are responsible for the code you use, even if an AI wrote it.
  **On screen:** Three safety habits
    - Never paste passwords, keys or private information into an AI tool.
    - Run every piece of AI code yourself, and compare it with what you asked for.
    - You are responsible for the code you use, even if an AI wrote it.
- **Narration:** Stage 1: plan. Before any code, Asha asks how to add the order code. She says what she wants, and says: no code yet.
  **On screen:** AI chat, stage 1: Plan before you code
    - You: I am a beginner. My Python receipt prints a cafe name, items and a total. I want to add an order code, CAFE-1024-T4, under the cafe name. List the steps in plain English. No code yet.
- **Narration:** The AI answers with four clear steps. Each one is something she can check. A plan you understand is easier to check than code you do not.
  **On screen:** AI chat, stage 1: Plan before you code
    - You: I am a beginner. My Python receipt prints a cafe name, items and a total. I want to add an order code, CAFE-1024-T4, under the cafe name. List the steps in plain English. No code yet.
    - AI (example answer): 1. Find the line that prints the cafe name. 2. Add one new print line after it. 3. Print the three parts of the code as three values, with hyphens between them. 4. Run the receipt and check the code, character by character.
- **Narration:** Stage 2: write. Before she changes her receipt, Asha makes sure she understands every line. She asks the AI to explain her code, not to rewrite it.
  **On screen:** AI chat, stage 2: Write it, then ask for an explanation
    - You: Before I change my receipt, explain it to me. Do not rewrite it. One simple sentence for each group of lines. [code `examples/ex04_receipt.py`]
- **Narration:** The AI explains each group, and shows where the order code belongs: after line 3. Asha checks each sentence against what she learned.
  **On screen:** AI chat, stage 2: Write it, then ask for an explanation
    - You: Before I change my receipt, explain it to me. Do not rewrite it. One simple sentence for each group of lines. [code `examples/ex04_receipt.py`]
    - AI (example answer): Lines 2 to 4 print the header between two borders, so the order code goes after line 3. Lines 5 and 6 use `sep` to put dots between each item and its price. Lines 7 and 8 calculate `1 + 1` and `3 + 7`, so Python prints 2 and 10. Lines 9 and 10 close the receipt.
- **Narration:** Stage 3: generate. Now Asha asks for the code line itself: one line that prints the order code with hyphens.
  **On screen:** AI chat, stage 3: Generate code with a precise request
    - You: Write one line of Python that prints the order code `CAFE-1024-T4`, using three separate values. Show the output too.
- **Narration:** The AI gives a line of code, and says it prints the order code with hyphens. It sounds sure.
  **On screen:** AI chat, stage 3: Generate code with a precise request
    - You: Write one line of Python that prints the order code `CAFE-1024-T4`, using three separate values. Show the output too.
    - AI (example answer): Here is the code. It prints `CAFE-1024-T4`. [code `examples/ai_code_flawed.py`]
- **Narration:** Look at its code. You learned exactly what this line does in step 5.
  **On screen:** AI chat, stage 3: Generate code with a precise request
    - You: Write one line of Python that prints the order code `CAFE-1024-T4`, using three separate values. Show the output too.
    - AI (example answer): Here is the code. It prints `CAFE-1024-T4`. [code `examples/ai_code_flawed.py`]
- **Interaction:** "The AI says this prints `CAFE-1024-T4`. Is it right? Why?" stays on screen with a 10-second timer.
- **Narration:** Asha runs it. It prints spaces, not hyphens. The AI was wrong, and it sounded sure. Can she find out why? That is what testing is for.
  **On screen:** AI chat, stage 3: Generate code with a precise request
    - You: Write one line of Python that prints the order code `CAFE-1024-T4`, using three separate values. Show the output too.
    - AI (example answer): Here is the code. It prints `CAFE-1024-T4`. [code `examples/ai_code_flawed.py`]
    - You: I ran the AI's line. This is what it printed:
- **Narration:** Stage 4: test. Asha gives the AI what she expected, and what the line really printed.
  **On screen:** AI chat, stage 4: Test: compare expected and real output
    - You: I expected `CAFE-1024-T4`. The line printed `CAFE 1024 T4`. List every difference, character by character.
- **Narration:** This time the AI finds both differences, and names the cause: sep is a space by default. It adds sep equals hyphen.
  **On screen:** AI chat, stage 4: Test: compare expected and real output
    - You: I expected `CAFE-1024-T4`. The line printed `CAFE 1024 T4`. List every difference, character by character.
    - AI (example answer): There are two differences. Characters 5 and 10 are spaces, but you expected hyphens. The cause: `sep` is a space by default. Add `sep="-"`. [code `examples/ai_code_fixed.py`]
- **Narration:** Asha does not trust it yet. She runs it. Now the order code is correct, so she adds it to her receipt.
  **On screen:** AI chat, stage 4: Test: compare expected and real output
    - You: I expected `CAFE-1024-T4`. The line printed `CAFE 1024 T4`. List every difference, character by character.
    - AI (example answer): There are two differences. Characters 5 and 10 are spaces, but you expected hyphens. The cause: `sep` is a space by default. Add `sep="-"`. [code `examples/ai_code_fixed.py`]
    - You: I ran the fixed line:
- **Narration:** Stage 5: debug. While adding the order code, Asha types Print with a capital P on the last line. Python stops with an error. She pastes her code and the full error.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I added the order code to my receipt and got this error. Here are the last two lines of my code. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_receipt_typo.py`]
- **Narration:** She asks for the cause first, then the smallest fix. The AI names line 11, explains that names are case-sensitive, and changes one letter.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I added the order code to my receipt and got this error. Here are the last two lines of my code. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_receipt_typo.py`]
    - AI (example answer): The cause is on line 11: `Print` starts with a capital P. Python names are case-sensitive, so `Print` is not the `print()` function. The fix: change `Print` to `print`.
- **Narration:** Stage 6: improve. The receipt now works. Asha asks for at most two readability suggestions, each with a reason.
  **On screen:** AI chat, stage 6: Improve: a short, reasoned review
    - You: Review my receipt for readability. Here are the order code and price lines. Suggest at most two improvements, each with a one-sentence reason. Do not change what it prints. [code `examples/ai_receipt_typo.py`]
- **Narration:** Suggestion 1 helps. Suggestion 2 says the dots do not line up.
  **On screen:** AI chat, stage 6: Improve: a short, reasoned review
    - You: Review my receipt for readability. Here are the order code and price lines. Suggest at most two improvements, each with a one-sentence reason. Do not change what it prints. [code `examples/ai_receipt_typo.py`]
    - AI (example answer): 1. Add a comment that says what the program does, such as a cafe receipt with its order code. A reader then knows its purpose at once. 2. The dots do not line up. Make both `sep` values the same length.
- **Narration:** Asha checks it herself. She counts: both price rows are 23 characters, so they already line up. The AI was wrong again. She keeps suggestion 1 only, and runs the receipt.
  **On screen:** AI chat, stage 6: Improve: a short, reasoned review
    - You: Review my receipt for readability. Here are the order code and price lines. Suggest at most two improvements, each with a one-sentence reason. Do not change what it prints. [code `examples/ai_receipt_typo.py`]
    - AI (example answer): 1. Add a comment that says what the program does, such as a cafe receipt with its order code. A reader then knows its purpose at once. 2. The dots do not line up. Make both `sep` values the same length.
    - You: I counted: both price rows are already 23 characters, so they do line up. Suggestion 2 is wrong. I added the comment and ran the receipt:
- **Narration:** Here is the result. A comment that says what the program does, on line 2. And the order code, on line 5.
  **On screen:** Code `examples/ai_receipt_final.py`, line 2, 5 highlighted, output `examples/ai_receipt_final.expected`
- **Narration:** Every stage helped, and at every stage Asha checked the answer herself. That is how you work with AI.
  **On screen:** Code `examples/ai_receipt_final.py`, line 2, 5 highlighted, output `examples/ai_receipt_final.expected`
- **Narration:** Quick check on what you watched. Your program stops with an error. Which stage do you use?
  **On screen:** Quick check: "Your program stops with an error. Which stage do you use, and what do you paste?" (options shown)
- **Interaction:** "Your program stops with an error. Which stage do you use, and what do you paste?" stays on screen with a 10-second timer.
- **Narration:** C. Debug. Paste the code and the full error, and ask for the cause first.
  **On screen:** Quick check: "Your program stops with an error. Which stage do you use, and what do you paste?" (answer revealed: Debug: paste the code and the full error)
- **Narration:** Breather. You watched Asha use AI at every stage, and she caught two AI mistakes by checking.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - AI can be wrong and sound sure.
    - Run it, compare it, then trust it.
- **Narration:** Next, the four errors every beginner meets, including the one Asha debugged.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - AI can be wrong and sound sure.
    - Run it, compare it, then trust it.
- **Breather:** 4 quiet seconds.

## Scene 11: Common mistakes (12:41 to 15:30)

**Section:** Common mistakes

**Direction:** Teach three mistakes with their real error reports, then let the learner spot the fourth, then a summary table and a quick check.

- **Narration:** Mistake 1. The closing quotation mark is missing, so Python cannot see where the text ends.
  **On screen:** Code `examples/err01_missing_quote.py`, line 2 highlighted, error `examples/err01_missing_quote.expected_error`
- **Narration:** It reports a syntax error. That means Python could not read the file, so no line runs at all.
  **On screen:** Code `examples/err01_missing_quote.py`, line 2 highlighted, error `examples/err01_missing_quote.expected_error`
- **Narration:** The fix: add the closing quotation mark. Remember this rule: every opening mark needs its closing partner, for quotation marks and for brackets.
  **On screen:** Code `examples/err01_missing_quote.py`, line 2 highlighted, error `examples/err01_missing_quote.expected_error`
- **Narration:** Mistake 2 is the one Asha debugged with the AI. Print with a capital P is a different name. Here it is in a short test file.
  **On screen:** Code `examples/err02_capital_p.py`, line 3 highlighted, error `examples/err02_capital_p.expected_error`
- **Narration:** Notice that Start printed first. This error happened while the program was running, so the lines above it had already run.
  **On screen:** Code `examples/err02_capital_p.py`, line 3 highlighted, error `examples/err02_capital_p.expected_error`
- **Narration:** The report names line 3, and the last line even suggests the fix.
  **On screen:** Code `examples/err02_capital_p.py`, line 3 highlighted, error `examples/err02_capital_p.expected_error`
- **Narration:** Mistake 3. Word processors and some chat apps turn straight quotation marks into curly ones. Python accepts only straight ones.
  **On screen:** Code `examples/err03_curly_quotes.py`, line 2 highlighted, error `examples/err03_curly_quotes.expected_error`
- **Narration:** So when you copy code from a chat, copy it from the code block, never from formatted text.
  **On screen:** Code `examples/err03_curly_quotes.py`, line 2 highlighted, error `examples/err03_curly_quotes.expected_error`
- **Narration:** Now you know three errors, and the rule about closing partners. Try the fourth yourself.
  **On screen:** Code `examples/err04_missing_bracket.py`, line 2 highlighted, output hidden
- **Interaction:** "What is missing on line 2?" stays on screen with a 10-second timer.
- **Narration:** The closing bracket. Every opening bracket needs a closing bracket.
  **On screen:** Code `examples/err04_missing_bracket.py`, line 2 highlighted, error `examples/err04_missing_bracket.expected_error`
- **Narration:** Here are all four. Each row starts with the last line of its error report.
  **On screen:** Table: Read the last line first
- **Narration:** Unterminated string literal: a quotation mark is missing.
  **On screen:** Table: Read the last line first (row 1 in focus)
- **Narration:** Name is not defined: check the spelling, such as a capital P.
  **On screen:** Table: Read the last line first (row 2 in focus)
- **Narration:** Invalid character: retype the quotation marks.
  **On screen:** Table: Read the last line first (row 3 in focus)
- **Narration:** Was never closed: add the closing bracket.
  **On screen:** Table: Read the last line first (row 4 in focus)
- **Narration:** So the habit is simple. Read the last line first, then find the line number.
  **On screen:** Table: Read the last line first
- **Narration:** Quick check. An error report has several lines. Which one do you read first?
  **On screen:** Quick check: "An error report has several lines. Which line do you read first?" (options shown)
- **Interaction:** "An error report has several lines. Which line do you read first?" stays on screen with a 10-second timer.
- **Narration:** B. The last line. It names the kind of error.
  **On screen:** Quick check: "An error report has several lines. Which line do you read first?" (answer revealed: The last line)
- **Narration:** One more breather. Every developer sees errors every day. Now you can read them.
  **On screen:** Breather card
    - Errors are messages, not failures.
    - Read the last line first.
    - Then find the line number.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - Errors are messages, not failures.
    - Read the last line first.
    - Then find the line number.
- **Breather:** 4 quiet seconds.

## Scene 12: Think beyond (15:30 to 16:22)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. The question stays above its timer. No answers are given.

- **Narration:** First. The cafe wants the order code written backwards, with slashes. What would you change in Asha's code line?
  **On screen:** Question card: "The cafe wants the order code as `T4/1024/CAFE`. What would you change?"
- **Interaction:** "The cafe wants the order code as `T4/1024/CAFE`. What would you change?" stays on screen with a 10-second timer.
- **Narration:** Try it in your editor after the video, and compare the output with the target, character by character.
  **On screen:** Question card: "The cafe wants the order code as `T4/1024/CAFE`. What would you change?"
- **Narration:** Second. An AI gives you code that runs with no error. What two things do you check before you trust it?
  **On screen:** Question card: "AI code runs with no error. What two things do you check before you trust it?"
- **Interaction:** "AI code runs with no error. What two things do you check before you trust it?" stays on screen with a 10-second timer.
- **Narration:** Keep your answer. You will use it in every chapter.
  **On screen:** Question card: "AI code runs with no error. What two things do you check before you trust it?"

## Scene 13: Recap (16:22 to 17:22)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap the mission.
  **On screen:** Recap
- **Narration:** Python runs a program from top to bottom, one line at a time.
  **On screen:** Recap
    - Python runs a program from top to bottom, one line at a time.
- **Narration:** Print shows text and numbers, and calculations without quotation marks are worked out first.
  **On screen:** Recap
    - Python runs a program from top to bottom, one line at a time.
    - `print()` shows text and numbers. Calculations without quotation marks are worked out first.
- **Narration:** Sep goes between values, and end goes after them.
  **On screen:** Recap
    - Python runs a program from top to bottom, one line at a time.
    - `print()` shows text and numbers. Calculations without quotation marks are worked out first.
    - `sep` goes between values; `end` goes after the last one.
- **Narration:** Read the last line of an error first.
  **On screen:** Recap
    - Python runs a program from top to bottom, one line at a time.
    - `print()` shows text and numbers. Calculations without quotation marks are worked out first.
    - `sep` goes between values; `end` goes after the last one.
    - Read the last line of an error first, then find the line number.
- **Narration:** And use AI at every stage, then run and check everything yourself.
  **On screen:** Recap
    - Python runs a program from top to bottom, one line at a time.
    - `print()` shows text and numbers. Calculations without quotation marks are worked out first.
    - `sep` goes between values; `end` goes after the last one.
    - Read the last line of an error first, then find the line number.
    - Use AI at every stage, then run and check everything yourself.
- **Narration:** One last check. Asha wants a new line: Tea, dash, U S D 3. Which code prints it?
  **On screen:** Quick check: "Asha wants a new line on the receipt: `Tea - USD 3`. Which code prints it?" (options shown)
- **Interaction:** "Asha wants a new line on the receipt: `Tea - USD 3`. Which code prints it?" stays on screen with a 10-second timer.
- **Narration:** A. The separator goes between the two values.
  **On screen:** Quick check: "Asha wants a new line on the receipt: `Tea - USD 3`. Which code prints it?" (answer revealed: `print("Tea", "USD 3", sep=" - ")`)
- **Narration:** Mission complete. You earned 100 XP and the First Run badge.
  **On screen:** First Run You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 14: Practice (17:22 to 17:48)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn to build. The practice file has eight tasks.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you check an AI's work, like Asha did.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 15: What's next (17:48 to 18:09)

**Section:** What's next

**Direction:** End card. Hold quietly for two seconds after the narration.

- **Narration:** Asha typed every price twice on her receipt. In Chapter 2, you will fix that with variables: store a value once, and use it many times.
  **On screen:** Values and Variables: Giving Data a Name Store a value once. Use it many times.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Values and Variables: Giving Data a Name Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 2.
  **On screen:** Values and Variables: Giving Data a Name Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
