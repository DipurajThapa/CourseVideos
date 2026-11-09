# Video Script: Chapter 1: Your First Program and Your AI Study Partner

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 11:32.

## Scene 1: Introduction (0:00 to 0:51)

**Section:** Introduction

**Direction:** Title card, then the AI's date code with its output hidden. Pause, then reveal the spaces.

- **Narration:** Welcome to Code Quest, Chapter 1: Your First Program and Your AI Study Partner. Today you will write and run your first Python program, and you will learn to use an AI assistant as a tutor.
  **On screen:** Your First Program and Your AI Study Partner Write it, run it, read the errors, and check the AI.
- **Narration:** First, a puzzle. A learner asked an AI assistant to print today's date as 2026, hyphen, 11, hyphen, 09, using three separate values. The AI wrote this line of code.
  **On screen:** Code `examples/ai_date_flawed.py`, lines 2 highlighted, output hidden (predict first)
- **Narration:** The code runs without an error. But does it do what the learner asked?
  **On screen:** Pause card: "Will this print 2026-11-09 exactly?" with a 4-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** Here is the real output. There are spaces where the hyphens should be. Code that runs is not always code that is correct. By the end of this chapter, you will know why, and how to fix it.
  **On screen:** Code `examples/ai_date_flawed.py`, lines 2 highlighted, output `examples/ai_date_flawed.expected`

## Scene 2: Learning goals (0:51 to 1:21)

**Section:** Learning goals

**Direction:** Reveal the five goals in three steps.

- **Narration:** By the end of this chapter, you will be able to run a Python file from the terminal and see its output. You will also be able to explain how Python runs a program: one line at a time, from top to bottom.
  **On screen:** By the end of this chapter, you will be able to:
    - Run a Python file from the terminal and see its output.
    - Explain how Python runs a program: one line at a time, from top to bottom.
- **Narration:** You will use print to show text and numbers, and control the spacing with two settings called sep and end. You will read an error message and find the line that caused it.
  **On screen:** By the end of this chapter, you will be able to:
    - Run a Python file from the terminal and see its output.
    - Explain how Python runs a program: one line at a time, from top to bottom.
    - Use `print()` to show text and numbers, and control spacing with `sep` and `end`.
    - Read an error message and find the line that caused it.
- **Narration:** And you will ask an AI assistant to explain code in a safe and useful way.
  **On screen:** By the end of this chapter, you will be able to:
    - Run a Python file from the terminal and see its output.
    - Explain how Python runs a program: one line at a time, from top to bottom.
    - Use `print()` to show text and numbers, and control spacing with `sep` and `end`.
    - Read an error message and find the line that caused it.
    - Ask an AI assistant to explain code in a safe and useful way.

## Scene 3: Why this matters (1:21 to 2:10)

**Section:** Why this matters

**Direction:** Three short ideas: programs are instructions, output shows what a program does, and you remain the checker.

- **Narration:** Every app you use is a program. A program is a list of instructions that a computer follows exactly. Your phone's calculator, a shop's checkout screen and a train timetable all start as instructions like the ones you will write today.
  **On screen:** Every app is a program
    - A **program** is a list of instructions that a computer follows exactly.
    - A calculator, a checkout screen and a train timetable all start as instructions.
- **Narration:** Output is the first skill you need. When a program shows a message, you can see what it is doing. Professional developers often use print to check that their code works.
  **On screen:** Output shows what a program is doing
    - When a program shows a message, you can see what it is doing.
    - Developers often use `print()` to check that their code works.
- **Narration:** AI assistants such as ChatGPT and Claude can now write code. You still need to understand that code. AI tools are often right, but they can also be wrong while sounding confident. A study of AI tutors in Harvard's CS50 course found exactly this. You are the person who runs the code and decides if it is correct.
  **On screen:** AI writes code. You check it.
    - AI assistants such as ChatGPT and Claude can write code.
    - They are often right, and sometimes wrong while sounding confident.
    - You run the code, check the result and decide if it is correct.

## Scene 4: The idea: Python reads from top to bottom (2:10 to 3:02)

**Section:** The idea

**Direction:** The diagram, then the definitions of function and string, then the recipe analogy with its limit.

- **Narration:** A Python program is a text file that ends in dot p y. Each line is an instruction. Python, the program called the interpreter, reads your file and carries out each instruction in order: top to bottom, one line at a time.
  **On screen:** How Python runs a program ['The **interpreter** reads your `.py` file and carries out each line in order.']
- **Narration:** Print is a function: a named action that Python already knows. You call it by writing its name, then brackets. The value inside the brackets is what it shows. Text must be inside quotation marks, and text in quotation marks is called a string.
  **On screen:** Two words you need
    - A **function** is a named action Python already knows. Call it with its name and brackets: `print(...)`.
    - A **string** is text inside quotation marks: `"Hello"`.
- **Narration:** Think of a program like a recipe. The cook follows each step in order and does exactly what it says. The comparison stops at one point. A cook can guess what you meant, but Python cannot. If a step has a typing mistake, Python stops and reports an error.
  **On screen:** A program is like a recipe
    - The cook follows each step in order, exactly as written.
    - Where it stops working: a cook can guess what you meant. Python cannot.
    - A typing mistake makes Python stop and report an error.

## Scene 5: Step 1: Install Python (3:02 to 3:37)

**Section:** Build it step by step

**Direction:** Text slides only: installation cannot be filmed here. Point learners to python.org.

- **Narration:** Step 1: install Python. Check the official guide for your system on python dot org. The current version is Python 3.15, and any version from 3.12 works for this course. On Windows, install the Python install manager from python dot org or the Microsoft Store.
  **On screen:** Table: Step 1: Install Python (3.12 or newer) (3 rows)
- **Narration:** On macOS, download the installer package from python dot org and open it. On Linux, Python is usually installed already. Then open a terminal and check the version. You should see a line that starts with Python 3.
  **On screen:** Table: Check the version in a terminal (2 rows)

## Scene 6: Steps 2 and 3: Write and run your first file (3:37 to 4:22)

**Section:** Build it step by step

**Direction:** Show the file, explain the comment, then the run command and the output.

- **Narration:** Step 2: create your first file. Open a code editor, such as Visual Studio Code, or IDLE. Create a file called ex 0 1 hello, and type these lines. Line 1 starts with a hash sign, so it is a comment. Python ignores comments. They are notes for people.
  **On screen:** Code `examples/ex01_hello.py`, lines 1 highlighted, output hidden (predict first)
- **Narration:** Step 3: run the file. In the terminal, go to the folder that holds your file. Type python, then the file name, on Windows. Type python3, then the file name, on macOS and Linux.
  **On screen:** Table: Step 3: Run the file (2 rows)
- **Narration:** You will see two lines. Each print produces one line of output. The quotation marks do not appear, because they only mark where the text starts and ends.
  **On screen:** Code `examples/ex01_hello.py`, lines 2, 3 highlighted, output `examples/ex01_hello.expected`

## Scene 7: Step 4: Check the order (4:22 to 4:50)

**Section:** Build it step by step

**Direction:** Predict before the reveal. Then challenge the learner to swap two lines.

- **Narration:** Step 4: check the order. This program prints three steps for making tea. Predict the output before you run it.
  **On screen:** Code `examples/ex02_order.py`, lines 2, 3, 4 highlighted, output hidden (predict first)
- **Narration:** In which order will the lines appear?
  **On screen:** Pause card: "In which order will the three steps appear?" with a 4-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** The lines appear in the same order as the code. Now swap two lines in your file and run it again. The output changes, because Python always runs from top to bottom.
  **On screen:** Code `examples/ex02_order.py`, lines 2, 3, 4 highlighted, output `examples/ex02_order.expected`

## Scene 8: Step 5: Several values, sep and end (4:50 to 5:51)

**Section:** Build it step by step

**Direction:** Explain the two settings with a table, show the code, pause on lines 4 and 5, then reveal.

- **Narration:** Step 5: print several values at once. Print can take more than one value, separated by commas. It also has two settings. Sep sets what goes between the values, and its default is one space. End sets what goes after the last value, and its default is a new line.
  **On screen:** Table: Step 5: Two settings of `print()` (2 rows)
- **Narration:** Look at this program. Line 2 adds 3 and 4 without quotation marks. Line 3 sets sep to a hyphen. Line 4 sets end to three dots.
  **On screen:** Code `examples/ex03_many_values.py`, lines 2, 3, 4 highlighted, output hidden (predict first)
- **Narration:** Predict the output, especially lines 4 and 5.
  **On screen:** Pause card: "What do lines 4 and 5 print together?" with a 5-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** Line 2 has no quotation marks around 3 plus 4, so Python calculates it and prints 7. Line 3 joins the values with a hyphen instead of a space. Line 4 ends with three dots instead of a new line, so line 5 continues on the same line: Loading, dot dot dot, done.
  **On screen:** Code `examples/ex03_many_values.py`, lines 4, 5 highlighted, output `examples/ex03_many_values.expected`

## Scene 9: See the outcome: a cafe receipt (5:51 to 6:27)

**Section:** See the outcome

**Direction:** Code first, then the receipt output. Point at the calculated lines.

- **Narration:** Here is a complete program that prints a receipt for the Corner Cafe. It uses everything from this chapter: print, text, sep for the dotted lines, and calculations.
  **On screen:** Code `examples/ex04_receipt.py`, lines 5, 6, 7, 8 highlighted, output hidden (predict first)
- **Narration:** Run it, and you get the receipt. The dots line up because each sep value has a different length. Python calculates the item count, 2, and the total, 10, for you.
  **On screen:** Code `examples/ex04_receipt.py`, lines 7, 8 highlighted, output `examples/ex04_receipt.expected`
- **Narration:** Notice one problem: each price is typed twice, once in its line and once in the total. In Chapter 2, you will store prices in named values instead.
  **On screen:** One problem to solve next
    - Each price is typed twice: in its own line and in the total.
    - In Chapter 2, you will store each price once, in a named value.

## Scene 10: Work with AI: a tutor, not a machine (6:27 to 8:20)

**Section:** Work with AI

**Direction:** Safety habits, the six stages, two prompt cards, then the AI pair moment from the opening.

- **Narration:** Use an AI assistant as a tutor that explains, not as a machine that does your work. Follow three safety habits from today. One: never paste passwords, keys or private information into an AI tool. Two: run every piece of AI code yourself, and compare the output with what you asked for. Three: you are responsible for the code you use, even if an AI wrote it.
  **On screen:** Three safety habits
    - Never paste passwords, keys or private information into an AI tool.
    - Run every piece of AI code yourself and compare the output with what you asked for.
    - You are responsible for the code you use, even if an AI wrote it.
- **Narration:** AI helps at every stage. Plan the steps in plain English. Write the program yourself first, then ask for an explanation. Generate code from an exact output. Debug with the full error message. Test by comparing outputs. And improve with at most two suggestions.
  **On screen:** Table: AI at every stage (6 rows)
- **Narration:** Here is the Write card. Paste your code, and ask the AI not to rewrite it. Ask it to explain each line in one simple sentence, and to say whether it prints exactly the output you want. Then run your program. If the AI said yes but the output differs, trust the real output.
  **On screen:** Prompt card (Write): "Here is my Python code: <paste your code>. Do not rewrite it. Explain what each line does in one simple sentence, and tell me if it prints exactly this: <paste the output you want>."
- **Narration:** And here is the Generate card. Paste the exact output you want, and ask for code that uses only print. Then compare every character, including spaces. This is how the date flaw was caught.
  **On screen:** Prompt card (Generate): "Write Python code that uses only the print() function. It must output exactly these lines, with the same spaces and symbols: <paste the exact output>. Show the code, then show the output it produces."
- **Narration:** Now the AI pair moment. Back to the opening puzzle. The request asked for hyphens, but the output has spaces. Which setting did the AI forget?
  **On screen:** Code `examples/ai_date_flawed.py`, lines 2 highlighted, output `examples/ai_date_flawed.expected`
- **Narration:** Think about step 5.
  **On screen:** Pause card: "Which setting puts a space between the values? How do you change it?" with a 6-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** The AI forgot that sep is a space by default. The fix sets sep to a hyphen, and the date prints correctly. Always check AI output against what you asked for, character by character.
  **On screen:** Code `examples/ai_date_fixed.py`, lines 2 highlighted, output `examples/ai_date_fixed.expected`

## Scene 11: Common mistakes (8:20 to 9:35)

**Section:** Common mistakes

**Direction:** One beat per mistake with the real error, then the reading habit.

- **Narration:** Now, four common mistakes. Mistake 1 is a missing closing quotation mark. Python cannot see where the text ends, so it reports a Syntax Error. A syntax error means Python could not read the file, so no line runs. The fix is to add the closing quotation mark before the bracket.
  **On screen:** Code `examples/err01_missing_quote.py`, lines 2 highlighted, error `examples/err01_missing_quote.expected_error`
- **Narration:** Mistake 2 is a capital letter in print. Python treats capital P Print and small p print as different names. Notice that Start was printed first. This error happened while the program was running, so the lines before it had already run. The message names line 3, and even suggests the fix.
  **On screen:** Code `examples/err02_capital_p.py`, lines 3 highlighted, error `examples/err02_capital_p.expected_error`
- **Narration:** Mistake 3 is curly quotation marks. Word processors and some chat apps change straight quotation marks into curly ones. Python only accepts straight ones. Type the quotation marks again in your code editor, and copy code from a code block, never from a formatted document.
  **On screen:** Code `examples/err03_curly_quotes.py`, lines 2 highlighted, error `examples/err03_curly_quotes.expected_error`
- **Narration:** Mistake 4 is a missing closing bracket. Every opening bracket needs a closing bracket.
  **On screen:** Code `examples/err04_missing_bracket.py`, lines 2 highlighted, error `examples/err04_missing_bracket.expected_error`
- **Narration:** The habit to build: read the last line of an error first. It names the kind of error. Then look at the line number to find where it happened.
  **On screen:** Table: Read the last line first (4 rows)

## Scene 12: Think beyond (9:35 to 10:09)

**Section:** Think beyond

**Direction:** Two open questions with pauses. Do not answer them.

- **Narration:** Two questions to think beyond this chapter. First: you want to print a shopping list with each item on its own line, using only one print. Which setting from this chapter could help? Test your idea.
  **On screen:** Pause card: "One print(), several lines: which setting could help?" with a 6-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** Second: an AI gives you code that runs with no error. What two things should you check before you trust it?
  **On screen:** Pause card: "AI code runs with no error. What two things do you check before you trust it?" with a 6-second countdown
  **Interaction:** the learner pauses and answers before the reveal.

## Scene 13: Recap (10:09 to 10:47)

**Section:** Recap

**Direction:** Reveal the recap, then the badge.

- **Narration:** Let's recap. A program is a list of instructions, and Python runs them one at a time, from top to bottom. Print shows values. Text goes inside quotation marks, and calculations without quotation marks are worked out first.
  **On screen:** Recap
    - A program is a list of instructions. Python runs them from top to bottom.
    - `print()` shows values. Text goes in quotation marks; calculations are worked out first.
- **Narration:** Sep controls what goes between values, and end controls what goes after them. An error message names the kind of error and the line, so read the last line first. And AI is a tutor: ask it to explain, then run and check everything yourself.
  **On screen:** Recap
    - A program is a list of instructions. Python runs them from top to bottom.
    - `print()` shows values. Text goes in quotation marks; calculations are worked out first.
    - `sep` controls what goes between values, and `end` what goes after them.
    - An error names the kind of error and the line. Read the last line first.
    - AI is a tutor. Ask it to explain, then run and check everything yourself.
- **Narration:** You earned 100 XP and the First Run badge.
  **On screen:** First Run You earned 100 XP.

## Scene 14: Practice (10:47 to 11:15)

**Section:** Practice

**Direction:** The eight tasks by tier.

- **Narration:** Now practise. The practice file has eight tasks. The warm-up tasks are worth 10 XP each: introduce yourself, fix a broken greeting, and predict, then run.
  **On screen:** Table: Practice: 8 tasks, 160 XP (3 rows)
- **Narration:** The apply tasks are worth 20 XP each, and the two stretch tasks are worth 40 each. In the last task, you check an AI's work and fix every difference yourself. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 160 XP (3 rows)

## Scene 15: What's next (11:15 to 11:32)

**Section:** What's next

**Direction:** End card. Hold for two seconds after the narration.

- **Narration:** In Chapter 2, you will give your data names with variables, so a program can store a value once and use it many times. Do the warm-up tasks now. They take about ten minutes. See you in Chapter 2.
  **On screen:** Values and Variables: Giving Data a Name Do the warm-up tasks now. They take about ten minutes.
