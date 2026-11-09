# Video Script: Chapter 1: Your First Program and Your AI Study Partner

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 15:54.

## Scene 1: Introduction (0:00 to 0:46)

**Section:** Introduction

**Direction:** Warm welcome, then the AI date puzzle. The request and the code stay on screen with the question and timer; the real output is revealed after the timer.

- **Narration:** Welcome to Code Quest, Chapter 1.
  **On screen:** Your First Program and Your AI Study Partner
- **Narration:** Today you will write and run your first Python program.
  **On screen:** Your First Program and Your AI Study Partner Write it. Run it.
- **Narration:** You will also learn to use an AI assistant as a tutor, and to check its work.
  **On screen:** Your First Program and Your AI Study Partner Write it. Run it. Read the errors. Check the AI.
- **Narration:** Let's start with a puzzle.
  **On screen:** Code `examples/ai_date_flawed.py`, output hidden
- **Narration:** A learner asked an AI assistant to print today's date with hyphens between the numbers.
  **On screen:** Code `examples/ai_date_flawed.py`, output hidden
- **Narration:** The AI wrote this single line of code.
  **On screen:** Code `examples/ai_date_flawed.py`, line 2 highlighted, output hidden
- **Interaction:** "Will this print `2026-11-09` exactly? Yes or no?" stays on screen with a 10-second timer.
- **Narration:** Here is the real output. There are spaces where the hyphens should be.
  **On screen:** Code `examples/ai_date_flawed.py`, line 2 highlighted, output `examples/ai_date_flawed.expected`
- **Narration:** The code runs without an error, but it does not do what was asked.
  **On screen:** Code `examples/ai_date_flawed.py`, line 2 highlighted, output `examples/ai_date_flawed.expected`
- **Narration:** By the end of this video, you will know why, and how to fix it.
  **On screen:** Code `examples/ai_date_flawed.py`, line 2 highlighted, output `examples/ai_date_flawed.expected`

## Scene 2: Learning goals (0:46 to 1:15)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken and stays highlighted while it is discussed.

- **Narration:** Here are your five goals for this chapter.
  **On screen:** By the end of this chapter, you will be able to:
- **Narration:** One. Run a Python file and see its output.
  **On screen:** By the end of this chapter, you will be able to:
    - Run a Python file from the terminal and see its output.
- **Narration:** Two. Explain how Python runs a program: one line at a time, from top to bottom.
  **On screen:** By the end of this chapter, you will be able to:
    - Run a Python file from the terminal and see its output.
    - Explain how Python runs a program: one line at a time, from top to bottom.
- **Narration:** Three. Use print to show text and numbers, and control the spacing.
  **On screen:** By the end of this chapter, you will be able to:
    - Run a Python file from the terminal and see its output.
    - Explain how Python runs a program: one line at a time, from top to bottom.
    - Use `print()` to show text and numbers, and control spacing with `sep` and `end`.
- **Narration:** Four. Read an error message and find the line that caused it.
  **On screen:** By the end of this chapter, you will be able to:
    - Run a Python file from the terminal and see its output.
    - Explain how Python runs a program: one line at a time, from top to bottom.
    - Use `print()` to show text and numbers, and control spacing with `sep` and `end`.
    - Read an error message and find the line that caused it.
- **Narration:** And five. Ask an AI assistant to explain code in a safe way.
  **On screen:** By the end of this chapter, you will be able to:
    - Run a Python file from the terminal and see its output.
    - Explain how Python runs a program: one line at a time, from top to bottom.
    - Use `print()` to show text and numbers, and control spacing with `sep` and `end`.
    - Read an error message and find the line that caused it.
    - Ask an AI assistant to explain code in a safe and useful way.

## Scene 3: Why this matters (1:15 to 2:04)

**Section:** Why this matters

**Direction:** Three short ideas, each highlighted while spoken.

- **Narration:** Every app you use is a program. A program is a list of instructions that a computer follows exactly.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
- **Narration:** When a program shows a message, you can see what it is doing. Professional developers often use print to check their code.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
    - Output shows what a program is doing. Developers use `print()` to check their code.
- **Narration:** AI assistants such as ChatGPT and Claude can write code.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
    - Output shows what a program is doing. Developers use `print()` to check their code.
    - AI can write code.
- **Narration:** They are often right. But sometimes they are wrong, and still sound sure.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
    - Output shows what a program is doing. Developers use `print()` to check their code.
    - AI can write code.
    - It is often right, and sometimes wrong while sounding sure.
- **Narration:** Researchers who built AI tutors for Harvard's CS50 course saw exactly this.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
    - Output shows what a program is doing. Developers use `print()` to check their code.
    - AI can write code.
    - It is often right, and sometimes wrong while sounding sure.
    - Researchers who built AI tutors for Harvard's CS50 course saw this too.
- **Narration:** So who checks the code?
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
    - Output shows what a program is doing. Developers use `print()` to check their code.
    - AI can write code.
    - It is often right, and sometimes wrong while sounding sure.
    - Researchers who built AI tutors for Harvard's CS50 course saw this too.
- **Interaction:** "An AI wrote your code. Who decides if it is correct?" stays on screen with a 10-second timer.
- **Narration:** You do. You are the person who runs the code, and decides if it is correct.
  **On screen:** Why this matters
    - A **program** is a list of instructions that a computer follows exactly.
    - Output shows what a program is doing. Developers use `print()` to check their code.
    - AI can write code.
    - It is often right, and sometimes wrong while sounding sure.
    - Researchers who built AI tutors for Harvard's CS50 course saw this too.
    - **You** run the code. **You** decide if it is correct.

## Scene 4: The idea: Python reads from top to bottom (2:04 to 3:30)

**Section:** The idea

**Direction:** Diagram, two key words, the recipe analogy, then a quick check.

- **Narration:** A Python program is a text file that ends in dot p y. Each line is an instruction.
  **On screen:** How Python runs a program
- **Narration:** Python, the program called the interpreter, reads your file.
  **On screen:** How Python runs a program
- **Narration:** It carries out each line in order: top to bottom, one line at a time.
  **On screen:** How Python runs a program
- **Narration:** Print is a function: a named action that Python already knows. You call it with its name, then brackets.
  **On screen:** Two words you need
    - A **function** is a named action Python already knows. Call it with its name and brackets: `print(...)`.
- **Narration:** Text must be inside quotation marks. Text in quotation marks is called a string.
  **On screen:** Two words you need
    - A **function** is a named action Python already knows. Call it with its name and brackets: `print(...)`.
    - A **string** is text inside quotation marks: `"Hello"`.
- **Narration:** Think of a program like a recipe. The cook follows each step in order.
  **On screen:** A program is like a recipe
    - The cook follows each step in order, exactly as written.
- **Narration:** But the comparison stops at one point. A cook can guess what you meant. Python cannot.
  **On screen:** A program is like a recipe
    - The cook follows each step in order, exactly as written.
    - Where it stops working: a cook can guess what you meant. Python cannot.
- **Narration:** If a step has a typing mistake, Python stops and reports an error.
  **On screen:** A program is like a recipe
    - The cook follows each step in order, exactly as written.
    - Where it stops working: a cook can guess what you meant. Python cannot.
    - A typing mistake makes Python stop and report an error.
- **Narration:** Quick check. A file has three print lines. In which order does Python run them? Choose A, B, C or D.
  **On screen:** Quick check: "A file has three `print()` lines. In which order does Python run them?" (options shown)
- **Interaction:** "A file has three `print()` lines. In which order does Python run them?" stays on screen with a 10-second timer.
- **Narration:** The answer is B. Python runs your file from top to bottom, one line at a time.
  **On screen:** Quick check: "A file has three `print()` lines. In which order does Python run them?" (answer revealed: From top to bottom, one line at a time)
- **Narration:** Time for a short breather. Sit back for a moment. Here is what you know so far.
  **On screen:** Breather card
    - A program is a list of instructions.
    - Python runs them from top to bottom.
    - Text inside quotation marks is a string.
- **Narration:** Next, you will install Python and write your first file.
  **On screen:** Breather card
    - A program is a list of instructions.
    - Python runs them from top to bottom.
    - Text inside quotation marks is a string.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Install Python (3:30 to 4:12)

**Section:** Build it step by step

**Direction:** Each system's row is highlighted as it is spoken.

- **Narration:** Step 1: install Python.
  **On screen:** Table: Step 1: Install Python
- **Narration:** The current version is Python 3.15, and any version from 3.12 works for this course.
  **On screen:** Table: Step 1: Install Python (3.12 or newer)
- **Narration:** On Windows, use the Python install manager from python dot org or the Microsoft Store.
  **On screen:** Table: Step 1: Install Python (3.12 or newer) (row 1 in focus)
- **Narration:** On macOS, download the installer package from python dot org and open it.
  **On screen:** Table: Step 1: Install Python (3.12 or newer) (row 2 in focus)
- **Narration:** On Linux, Python is usually installed already.
  **On screen:** Table: Step 1: Install Python (3.12 or newer) (row 3 in focus)
- **Narration:** Then open a terminal and check the version.
  **On screen:** Table: Check the version in a terminal
- **Narration:** On Windows, type python, space, dash dash version.
  **On screen:** Table: Check the version in a terminal (row 1 in focus)
- **Narration:** On macOS and Linux, type python3, space, dash dash version. You should see a line that starts with Python 3.
  **On screen:** Table: Check the version in a terminal (row 2 in focus)

## Scene 6: Steps 2 and 3: Write and run your first file (4:12 to 4:58)

**Section:** Build it step by step

**Direction:** The file types itself in line by line as it is explained. The output appears only after the run command.

- **Narration:** Step 2. Open a code editor, such as Visual Studio Code or IDLE, and create a file called ex 0 1 hello.
  **On screen:** Code `examples/ex01_hello.py`, lines 1 to 1 typed in, output hidden
- **Narration:** Line 1 starts with a hash sign, so it is a comment. Python ignores comments. They are notes for people.
  **On screen:** Code `examples/ex01_hello.py`, lines 1 to 1 typed in, line 1 highlighted, output hidden
- **Narration:** Line 2 prints a greeting.
  **On screen:** Code `examples/ex01_hello.py`, lines 1 to 2 typed in, line 2 highlighted, output hidden
- **Narration:** Line 3 prints a second line.
  **On screen:** Code `examples/ex01_hello.py`, lines 1 to 3 typed in, line 3 highlighted, output hidden
- **Narration:** Step 3: run the file. In the terminal, go to the folder that holds your file.
  **On screen:** Table: Step 3: Run the file
- **Narration:** On Windows, type python, then the file name.
  **On screen:** Table: Step 3: Run the file (row 1 in focus)
- **Narration:** On macOS and Linux, type python3, then the file name.
  **On screen:** Table: Step 3: Run the file (row 2 in focus)
- **Narration:** You will see two lines. Each print produces one line of output.
  **On screen:** Code `examples/ex01_hello.py`, line 2, 3 highlighted, output `examples/ex01_hello.expected`
- **Narration:** The quotation marks do not appear, because they only mark where the text starts and ends.
  **On screen:** Code `examples/ex01_hello.py`, line 2, 3 highlighted, output `examples/ex01_hello.expected`

## Scene 7: Step 4: Check the order (4:58 to 5:36)

**Section:** Build it step by step

**Direction:** Type the three steps in, keep them on screen with the question and timer, then reveal.

- **Narration:** Step 4. This program prints three steps for making tea. Step 1, boil the water.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 2 typed in, line 2 highlighted, output hidden
- **Narration:** Step 2, add the tea leaves.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 3 typed in, line 3 highlighted, output hidden
- **Narration:** Step 3, pour the tea into a cup.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 4 typed in, line 4 highlighted, output hidden
- **Narration:** Before you run it, predict the output.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 4 typed in, line 2, 3, 4 highlighted, output hidden
- **Interaction:** "In which order will the three steps appear in the output?" stays on screen with a 10-second timer.
- **Narration:** The lines appear in the same order as the code.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 4 typed in, line 2, 3, 4 highlighted, output `examples/ex02_order.expected`
- **Narration:** Try this: swap two lines in your file and run it again.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 4 typed in, line 2, 3 highlighted, output `examples/ex02_order.expected`
- **Narration:** The output changes, because Python always runs from top to bottom.
  **On screen:** Code `examples/ex02_order.py`, lines 1 to 4 typed in, output `examples/ex02_order.expected`

## Scene 8: Step 5: Several values, sep and end (5:36 to 7:18)

**Section:** Build it step by step

**Direction:** Settings table with each row in focus, then the code line by line, the question with the code still visible, and the reveal with the matching output line lit.

- **Narration:** Step 5. Print can show several values at once, separated by commas. It also has two settings.
  **On screen:** Table: Step 5: Two settings of `print()`
- **Narration:** Sep sets what goes between the values. Its default is one space.
  **On screen:** Table: Step 5: Two settings of `print()` (row 1 in focus)
- **Narration:** End sets what goes after the last value. Its default is a new line.
  **On screen:** Table: Step 5: Two settings of `print()` (row 2 in focus)
- **Narration:** Look at line 2. The calculation 3 plus 4 has no quotation marks.
  **On screen:** Code `examples/ex03_many_values.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 sets sep to a colon.
  **On screen:** Code `examples/ex03_many_values.py`, line 3 highlighted, output hidden
- **Narration:** Line 4 sets end to three dots, and line 5 prints the word done.
  **On screen:** Code `examples/ex03_many_values.py`, line 4, 5 highlighted, output hidden
- **Interaction:** "What do lines 4 and 5 print together?" stays on screen with a 10-second timer.
- **Narration:** Here is the output. Line 2 has no quotation marks, so Python calculates 3 plus 4 and prints 7.
  **On screen:** Code `examples/ex03_many_values.py`, line 2 highlighted, output `examples/ex03_many_values.expected`
- **Narration:** Line 3 joins the values with colons instead of spaces, so they look like a time.
  **On screen:** Code `examples/ex03_many_values.py`, line 3 highlighted, output `examples/ex03_many_values.expected`
- **Narration:** Line 4 ends with three dots instead of a new line.
  **On screen:** Code `examples/ex03_many_values.py`, line 4 highlighted, output `examples/ex03_many_values.expected`
- **Narration:** So line 5 continues on the same line: Loading, dot dot dot, done.
  **On screen:** Code `examples/ex03_many_values.py`, line 5 highlighted, output `examples/ex03_many_values.expected`
- **Narration:** Quick check. Which setting changes what goes between the values in print?
  **On screen:** Quick check: "Which setting changes what goes **between** the values in `print()`?" (options shown)
- **Interaction:** "Which setting changes what goes **between** the values in `print()`?" stays on screen with a 10-second timer.
- **Narration:** The answer is B, sep. Sep goes between values. End goes after the last value.
  **On screen:** Quick check: "Which setting changes what goes **between** the values in `print()`?" (answer revealed: `sep`)
- **Narration:** Another breather. Relax your shoulders, and look at what you can already do.
  **On screen:** Breather card
    - You can run a Python file from the terminal.
    - Each `print()` makes one line of output.
    - `sep` goes between values; `end` goes after them.
- **Narration:** Next, you will put it all together in one complete program.
  **On screen:** Breather card
    - You can run a Python file from the terminal.
    - Each `print()` makes one line of output.
    - `sep` goes between values; `end` goes after them.
- **Breather:** 4 quiet seconds.

## Scene 9: See the outcome: a cafe receipt (7:18 to 8:04)

**Section:** See the outcome

**Direction:** Walk the receipt code in three groups, reveal the output, then ask which lines Python calculated.

- **Narration:** Here is a complete program that prints a receipt for the Corner Cafe. Lines 2 to 4 print the header.
  **On screen:** Code `examples/ex04_receipt.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Lines 5 and 6 use sep to draw the dotted lines between each item and its price.
  **On screen:** Code `examples/ex04_receipt.py`, line 5, 6 highlighted, output hidden
- **Narration:** Lines 7 and 8 have calculations without quotation marks.
  **On screen:** Code `examples/ex04_receipt.py`, line 7, 8 highlighted, output hidden
- **Narration:** Run it, and you get the receipt.
  **On screen:** Code `examples/ex04_receipt.py`, output `examples/ex04_receipt.expected`
- **Interaction:** "Which two output lines did Python calculate by itself?" stays on screen with a 10-second timer.
- **Narration:** Items 2, and Total U S D 10. Python worked out 1 plus 1, and 3 plus 7.
  **On screen:** Code `examples/ex04_receipt.py`, line 7, 8 highlighted, output `examples/ex04_receipt.expected`
- **Narration:** Notice one problem: each price is typed twice.
  **On screen:** Code `examples/ex04_receipt.py`, line 5, 6, 8 highlighted, output `examples/ex04_receipt.expected`
- **Narration:** In Chapter 2, you will store prices in named values instead.
  **On screen:** Code `examples/ex04_receipt.py`, output `examples/ex04_receipt.expected`

## Scene 10: Work with AI: a tutor, not a machine (8:04 to 10:32)

**Section:** Work with AI

**Direction:** Safety habits one at a time, then the six stages and two prompt cards. The opening puzzle returns: the question stays beside the code, and the fix replaces the flawed line.

- **Narration:** Use an AI assistant as a tutor that explains, not as a machine that does your work. Follow three safety habits.
  **On screen:** Three safety habits
- **Narration:** One. Never paste passwords, keys or private information into an AI tool.
  **On screen:** Three safety habits
    - Never paste passwords, keys or private information into an AI tool.
- **Narration:** Two. Run every piece of AI code yourself, and compare the output with what you asked for.
  **On screen:** Three safety habits
    - Never paste passwords, keys or private information into an AI tool.
    - Run every piece of AI code yourself and compare the output with what you asked for.
- **Narration:** Three. You are responsible for the code you use, even if an AI wrote it.
  **On screen:** Three safety habits
    - Never paste passwords, keys or private information into an AI tool.
    - Run every piece of AI code yourself and compare the output with what you asked for.
    - You are responsible for the code you use, even if an AI wrote it.
- **Narration:** AI helps at every stage. Plan the steps in plain English first.
  **On screen:** Table: AI at every stage (row 1 in focus)
- **Narration:** Write the program yourself, then ask for an explanation.
  **On screen:** Table: AI at every stage (row 2 in focus)
- **Narration:** Generate code from an exact output.
  **On screen:** Table: AI at every stage (row 3 in focus)
- **Narration:** Debug with the full error message.
  **On screen:** Table: AI at every stage (row 4 in focus)
- **Narration:** Test by comparing outputs, space by space.
  **On screen:** Table: AI at every stage (row 5 in focus)
- **Narration:** And improve with at most two suggestions.
  **On screen:** Table: AI at every stage (row 6 in focus)
- **Narration:** Try this one.
  **On screen:** Table: AI at every stage
- **Interaction:** "Your program stops with an error. Which stage do you use, and what do you paste?" stays on screen with a 10-second timer.
- **Narration:** Debug. Paste the code and the full error message, and ask for the cause before the fix.
  **On screen:** Table: AI at every stage (row 4 in focus)
- **Narration:** Here is the Write card. Paste your code, and ask the AI not to rewrite it.
  **On screen:** Prompt card (Write)
- **Narration:** Ask it to explain each line in one simple sentence, and to say whether it prints exactly the output you want.
  **On screen:** Prompt card (Write)
- **Narration:** Then run your program. If the AI said yes but the output differs, trust the real output.
  **On screen:** Prompt card (Write)
- **Narration:** And here is the Generate card. Ask for code that uses only print.
  **On screen:** Prompt card (Generate)
- **Narration:** Paste the exact output you want, with the same spaces and symbols.
  **On screen:** Prompt card (Generate)
- **Narration:** Then run it and compare every character, including spaces. This is how the date flaw was caught.
  **On screen:** Prompt card (Generate)
- **Narration:** Now, back to the opening puzzle. The request asked for hyphens, but the output has spaces.
  **On screen:** Code `examples/ai_date_flawed.py`, line 2 highlighted, output `examples/ai_date_flawed.expected`
- **Interaction:** "Which `print()` setting puts a space between the values? How would you change it?" stays on screen with a 10-second timer.
- **Narration:** The AI forgot that sep is a space by default.
  **On screen:** Code `examples/ai_date_flawed.py`, line 2 highlighted, output `examples/ai_date_flawed.expected`
- **Narration:** The fix sets sep to a hyphen, and now the date prints correctly.
  **On screen:** Code `examples/ai_date_fixed.py`, line 2 highlighted, output `examples/ai_date_fixed.expected`
- **Narration:** Always check AI output against what you asked for, character by character.
  **On screen:** Code `examples/ai_date_fixed.py`, line 2 highlighted, output `examples/ai_date_fixed.expected`
- **Narration:** Take a breath. You have caught a real AI mistake. That is the most important skill in this course.
  **On screen:** Breather card
    - Use AI as a tutor that explains.
    - Never paste private information.
    - Run AI code and compare it with your request.
- **Narration:** Next, the four mistakes that beginners make most often.
  **On screen:** Breather card
    - Use AI as a tutor that explains.
    - Never paste private information.
    - Run AI code and compare it with your request.
- **Breather:** 4 quiet seconds.

## Scene 11: Common mistakes (10:32 to 13:27)

**Section:** Common mistakes

**Direction:** For the first two mistakes, the learner hunts the bug while the code and question stay on screen; then the real error appears.

- **Narration:** Mistake 1. This line should print Good morning. Something is missing.
  **On screen:** Code `examples/err01_missing_quote.py`, line 2 highlighted, output hidden
- **Interaction:** "What is missing on line 2?" stays on screen with a 10-second timer.
- **Narration:** The closing quotation mark is missing. Python cannot see where the text ends, so it reports a syntax error.
  **On screen:** Code `examples/err01_missing_quote.py`, line 2 highlighted, error `examples/err01_missing_quote.expected_error`
- **Narration:** A syntax error means Python could not read the file, so no line runs.
  **On screen:** Code `examples/err01_missing_quote.py`, line 2 highlighted, error `examples/err01_missing_quote.expected_error`
- **Narration:** Add the closing quotation mark before the bracket.
  **On screen:** Code `examples/err01_missing_quote.py`, line 2 highlighted, error `examples/err01_missing_quote.expected_error`
- **Narration:** Mistake 2. Line 2 is fine. Look closely at line 3.
  **On screen:** Code `examples/err02_capital_p.py`, line 3 highlighted, output hidden
- **Interaction:** "What is wrong on line 3?" stays on screen with a 10-second timer.
- **Narration:** Print starts with a capital P. Python treats capital P Print and small p print as different names.
  **On screen:** Code `examples/err02_capital_p.py`, line 3 highlighted, error `examples/err02_capital_p.expected_error`
- **Narration:** Notice that Start was printed first. This error happened while the program was running, so the lines before it had already run.
  **On screen:** Code `examples/err02_capital_p.py`, line 3 highlighted, error `examples/err02_capital_p.expected_error`
- **Narration:** The report names line 3, and the last line even suggests the fix.
  **On screen:** Code `examples/err02_capital_p.py`, line 3 highlighted, error `examples/err02_capital_p.expected_error`
- **Narration:** Mistake 3 is curly quotation marks. Word processors and some chat apps change straight quotation marks into curly ones.
  **On screen:** Code `examples/err03_curly_quotes.py`, line 2 highlighted, error `examples/err03_curly_quotes.expected_error`
- **Narration:** Python only accepts straight ones.
  **On screen:** Code `examples/err03_curly_quotes.py`, line 2 highlighted, error `examples/err03_curly_quotes.expected_error`
- **Narration:** Type the quotation marks again in your code editor.
  **On screen:** Code `examples/err03_curly_quotes.py`, line 2 highlighted, error `examples/err03_curly_quotes.expected_error`
- **Narration:** And copy code from a code block, never from a formatted document.
  **On screen:** Code `examples/err03_curly_quotes.py`, error `examples/err03_curly_quotes.expected_error`
- **Narration:** Mistake 4. One more line that will not run.
  **On screen:** Code `examples/err04_missing_bracket.py`, line 2 highlighted, output hidden
- **Interaction:** "What is missing on line 2?" stays on screen with a 10-second timer.
- **Narration:** The closing bracket is missing. Every opening bracket needs a closing bracket.
  **On screen:** Code `examples/err04_missing_bracket.py`, line 2 highlighted, error `examples/err04_missing_bracket.expected_error`
- **Narration:** Here are all four, side by side. Each one is the last line of its error report.
  **On screen:** Table: Read the last line first
- **Narration:** Unterminated string literal: a quotation mark is missing.
  **On screen:** Table: Read the last line first (row 1 in focus)
- **Narration:** Name is not defined: check the spelling, such as a capital P.
  **On screen:** Table: Read the last line first (row 2 in focus)
- **Narration:** Invalid character: retype the quotation marks.
  **On screen:** Table: Read the last line first (row 3 in focus)
- **Narration:** Was never closed: add the closing bracket.
  **On screen:** Table: Read the last line first (row 4 in focus)
- **Narration:** The habit to build: read the last line first. It names the kind of error. Then look at the line number.
  **On screen:** Table: Read the last line first
- **Narration:** Quick check. An error message has several lines. Which line do you read first?
  **On screen:** Quick check: "An error message has several lines. Which line do you read first?" (options shown)
- **Interaction:** "An error message has several lines. Which line do you read first?" stays on screen with a 10-second timer.
- **Narration:** The answer is B, the last line. It names the kind of error.
  **On screen:** Quick check: "An error message has several lines. Which line do you read first?" (answer revealed: The last line)
- **Narration:** One more breather. Errors are normal, and every developer sees them every day.
  **On screen:** Breather card
    - Errors are messages, not failures.
    - Read the last line first: it names the error.
    - Then find the line number.
- **Narration:** Next, two questions to think about on your own.
  **On screen:** Breather card
    - Errors are messages, not failures.
    - Read the last line first: it names the error.
    - Then find the line number.
- **Breather:** 4 quiet seconds.

## Scene 12: Think beyond (13:27 to 14:15)

**Section:** Think beyond

**Direction:** Two open questions. Each question stays on screen above its timer. No answers are given.

- **Narration:** Two questions to think beyond this chapter. First. You want to print a shopping list with each item on its own line, using only one print. Which setting could help?
  **On screen:** Question card: "One `print()`, several lines. Which setting could help?"
- **Interaction:** "One `print()`, several lines. Which setting could help?" stays on screen with a 10-second timer.
- **Narration:** Test your idea in your editor after the video.
  **On screen:** Question card: "One `print()`, several lines. Which setting could help?"
- **Narration:** Second. An AI gives you code that runs with no error. What two things should you check before you trust it?
  **On screen:** Question card: "AI code runs with no error. What two things do you check before you trust it?"
- **Interaction:** "AI code runs with no error. What two things do you check before you trust it?" stays on screen with a 10-second timer.
- **Narration:** Keep your answer. You will use it in every chapter.
  **On screen:** Question card: "AI code runs with no error. What two things do you check before you trust it?"

## Scene 13: Recap (14:15 to 15:16)

**Section:** Recap

**Direction:** Each recap point appears and is highlighted as it is spoken, then the badge.

- **Narration:** Let's recap.
  **On screen:** Recap
- **Narration:** A program is a list of instructions, and Python runs them from top to bottom.
  **On screen:** Recap
    - A program is a list of instructions. Python runs them from top to bottom.
- **Narration:** Print shows values. Text goes in quotation marks, and calculations are worked out first.
  **On screen:** Recap
    - A program is a list of instructions. Python runs them from top to bottom.
    - `print()` shows values. Text goes in quotation marks; calculations are worked out first.
- **Narration:** Sep controls what goes between values, and end controls what goes after them.
  **On screen:** Recap
    - A program is a list of instructions. Python runs them from top to bottom.
    - `print()` shows values. Text goes in quotation marks; calculations are worked out first.
    - `sep` controls what goes between values, and `end` what goes after them.
- **Narration:** An error names the kind of error and the line, so read the last line first.
  **On screen:** Recap
    - A program is a list of instructions. Python runs them from top to bottom.
    - `print()` shows values. Text goes in quotation marks; calculations are worked out first.
    - `sep` controls what goes between values, and `end` what goes after them.
    - An error names the kind of error and the line. Read the last line first.
- **Narration:** And AI is a tutor. Ask it to explain, then run and check everything yourself.
  **On screen:** Recap
    - A program is a list of instructions. Python runs them from top to bottom.
    - `print()` shows values. Text goes in quotation marks; calculations are worked out first.
    - `sep` controls what goes between values, and `end` what goes after them.
    - An error names the kind of error and the line. Read the last line first.
    - AI is a tutor. Ask it to explain, then run and check everything yourself.
- **Narration:** One last quick check. An AI gives you code that runs with no error. What should you do next?
  **On screen:** Quick check: "An AI gives you code that runs with no error. What should you do next?" (options shown)
- **Interaction:** "An AI gives you code that runs with no error. What should you do next?" stays on screen with a 10-second timer.
- **Narration:** The answer is B. Run it, and compare the output with what you asked for.
  **On screen:** Quick check: "An AI gives you code that runs with no error. What should you do next?" (answer revealed: Run it and compare the output with what you asked for)
- **Narration:** You earned 100 XP and the First Run badge. Well done.
  **On screen:** First Run You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 14: Practice (15:16 to 15:38)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now practise. The practice file has eight tasks.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** The three warm-up tasks are worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** The three apply tasks are worth 20 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** The two stretch tasks are worth 40 each. In the last one, you check an AI's work and fix every difference yourself.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 15: What's next (15:38 to 15:54)

**Section:** What's next

**Direction:** End card. Hold quietly for two seconds after the narration.

- **Narration:** In Chapter 2, you will give your data names with variables, so a program can store a value once and use it many times.
  **On screen:** Values and Variables: Giving Data a Name Store a value once. Use it many times.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Values and Variables: Giving Data a Name Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 2.
  **On screen:** Values and Variables: Giving Data a Name Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
