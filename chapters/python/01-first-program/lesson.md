# Chapter 1: Your First Program and Your AI Study Partner

> Quest: write and run your first Python program, read your first error message, and set up an AI assistant as a tutor. Reward: 100 XP and the **First Run** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Run a Python file from the terminal and see its output.
- Explain how Python runs a program: one line at a time, from top to bottom.
- Use `print()` to show text and numbers, and control spacing with `sep` and `end`.
- Read an error message and find the line that caused it.
- Ask an AI assistant to explain code in a safe and useful way.

## Why this matters

Every app you use is a program. A program is a list of instructions that a computer follows exactly. Your phone's calculator, a shop's checkout screen and a train timetable all start as instructions like the ones you will write today.

Output is the first skill you need. When a program shows a message, you can see what it is doing. Professional developers often use `print()` to check that their code works. It is the simplest tool for finding out what a program is really doing.

AI assistants such as ChatGPT and Claude can now write code. You still need to understand that code. AI tools are often right, but they can also be wrong while sounding confident. A study of AI tutors in Harvard's CS50 course found exactly this. You are the person who runs the code, checks the result and decides if it is correct.

## The idea

A Python program is a text file that ends in `.py`. Each line is an instruction. Python, the program called the **interpreter**, reads your file and carries out each instruction in order.

```text
  You write          Python reads          The computer acts
 +-----------+      +--------------+      +-------------------+
 | hello.py  | ---> |  line 1      | ---> | shows line 1      |
 | (text)    |      |  line 2      |      | shows line 2      |
 +-----------+      +--------------+      +-------------------+
                     top to bottom,
                     one line at a time
```

`print()` is a **function**: a named action that Python already knows. You call it by writing its name, then brackets. The value inside the brackets is what it shows. Text must be inside quotation marks. Text in quotation marks is called a **string**.

Think of a program like a recipe. The cook follows each step in order and does exactly what it says. The comparison stops at one point: a cook can guess what you meant, but Python cannot. If a step has a typing mistake, Python stops and reports an error.

## Build it step by step

**Step 1: Install Python.** Check the official guide for your system on python.org. The current version is Python 3.15. Any version from 3.12 works for this course.

- **Windows:** install the Python install manager from python.org/downloads or from the Microsoft Store. Since Python 3.14, this is the recommended way, and the older installer is being phased out.
- **macOS:** download the installer package from python.org/downloads/macos and open it.
- **Linux:** Python is usually installed already. If it is not, install it with your system's package manager.

Open a terminal and check the version. On Windows, type `python --version`. On macOS and Linux, type `python3 --version`. You should see a line that starts with `Python 3`.

**Step 2: Create your first file.** Open a code editor, such as Visual Studio Code, or IDLE, which comes with many Python installations. Create a file called `ex01_hello.py` and type these lines:

```python
# file: examples/ex01_hello.py
print("Hello! My name is Asha.")
print("I am learning Python today.")
```

The first line starts with `#`, so it is a **comment**. Python ignores comments. They are notes for people.

**Step 3: Run the file.** In the terminal, go to the folder that holds your file. Then type `python ex01_hello.py` on Windows, or `python3 ex01_hello.py` on macOS and Linux. You will see:

<!-- output: examples/ex01_hello.expected -->
```output
Hello! My name is Asha.
I am learning Python today.
```

Each `print()` produces one line of output. The quotation marks do not appear, because they only mark where the text starts and ends.

**Step 4: Check the order.** Predict the output of this program before you run it.

```python
# file: examples/ex02_order.py
print("Step 1: Boil the water.")
print("Step 2: Add the tea leaves.")
print("Step 3: Pour the tea into a cup.")
```

<!-- output: examples/ex02_order.expected -->
```output
Step 1: Boil the water.
Step 2: Add the tea leaves.
Step 3: Pour the tea into a cup.
```

The lines appear in the same order as the code. Swap two lines in your file and run it again. The output changes, because Python always runs from top to bottom.

**Step 5: Print several values at once.** `print()` can take more than one value, separated by commas. It also has two settings. `sep` sets what goes between the values, and its default is one space. `end` sets what goes after the last value, and its default is a new line.

```python
# file: examples/ex03_many_values.py
print("Total items:", 3 + 4)
print("10", "30", "45", sep=":")
print("Loading", end="...")
print("done")
```

<!-- output: examples/ex03_many_values.expected -->
```output
Total items: 7
10:30:45
Loading...done
```

Line 2 shows that `3 + 4` has no quotation marks, so Python calculates it and prints `7`. Line 3 joins the values with a colon instead of a space, so they look like a time. Line 4 ends with `...` instead of a new line, so line 5 continues on the same line.

## See the outcome

Here is a complete program that prints a receipt. It uses everything from this chapter.

```python
# file: examples/ex04_receipt.py
print("=========================")
print("   CORNER CAFE RECEIPT")
print("=========================")
print("Tea", "USD 3", sep=" ............. ")
print("Sandwich", "USD 7", sep=" ........ ")
print("Items:", 1 + 1)
print("Total: USD", 3 + 7)
print("=========================")
print("Thank you. See you soon!")
```

<!-- output: examples/ex04_receipt.expected -->
```output
=========================
   CORNER CAFE RECEIPT
=========================
Tea ............. USD 3
Sandwich ........ USD 7
Items: 2
Total: USD 10
=========================
Thank you. See you soon!
```

The dots line up because each `sep` value has a different length. Python calculates the item count and the total for you. In Chapter 2, you will store prices in named values instead of typing them twice.

## Work with AI

Use an AI assistant as a tutor that explains, not as a machine that does your work. Follow three safety habits from today:

1. Never paste passwords, keys or private information into an AI tool.
2. Run every piece of AI code yourself and compare the output with what you asked for.
3. You are responsible for the code you use, even if an AI wrote it.

Here is how AI helps at each stage of this chapter. The full prompts are in [ai-prompts.md](ai-prompts.md).

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Ask for the steps of a printed welcome card in plain English, with no code yet. |
| Write | Write the program yourself first. Then ask AI to explain each of your lines. |
| Generate | Paste the exact output you want and ask for code that uses only `print()`. |
| Debug | Paste your code and the full error message. Ask for the cause before the fix. |
| Test | Ask AI to compare your expected output and your real output, space by space. |
| Improve | Ask for at most two readability suggestions, each with a reason. |

**AI pair moment.** A learner gave an AI assistant this request: "Print today's date as 2026-11-09 using three separate values." The AI answered with this code:

```python
# file: examples/ai_date_flawed.py
print("2026", "11", "09")
```

The code runs without an error. Now compare its output with the request:

<!-- output: examples/ai_date_flawed.expected -->
```output
2026 11 09
```

The request asked for hyphens. The AI forgot that `sep` is a space by default. Code that runs is not always code that is correct. The fix sets `sep` to a hyphen:

```python
# file: examples/ai_date_fixed.py
print("2026", "11", "09", sep="-")
```

<!-- output: examples/ai_date_fixed.expected -->
```output
2026-11-09
```

Always check AI output against what you asked for, character by character.

## Common mistakes

**Mistake 1: a missing closing quotation mark.** Python cannot see where the text ends.

```python
# file: examples/err01_missing_quote.py
print("Good morning)
```

<!-- error: examples/err01_missing_quote.expected_error -->
```output
SyntaxError: unterminated string literal (detected at line 2)
```

Fix: add the closing quotation mark before the bracket: `print("Good morning")`. A **syntax error** means Python could not read the file, so no line runs.

**Mistake 2: a capital letter in `print`.** Python treats `Print` and `print` as different names.

```python
# file: examples/err02_capital_p.py
print("Start")
Print("Hello")
```

<!-- error: examples/err02_capital_p.expected_error -->
```output
Start
Traceback (most recent call last):
  File "err02_capital_p.py", line 3, in <module>
    Print("Hello")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

Fix: use a lowercase `p`. Notice that `Start` was printed first. This error happened while the program was running, so the lines before it had already run. The message names the line, line 3, and even suggests the fix.

**Mistake 3: curly quotation marks.** Word processors and some chat apps change straight quotation marks (`"`) into curly ones (`“` and `”`). Python only accepts straight ones.

```python
# file: examples/err03_curly_quotes.py
print(“Hello”)
```

<!-- error: examples/err03_curly_quotes.expected_error -->
```output
SyntaxError: invalid character '“' (U+201C)
```

Fix: type the quotation marks again in your code editor. Copy code from a code block, never from a formatted document.

**Mistake 4: a missing closing bracket.**

```python
# file: examples/err04_missing_bracket.py
print("Hello"
```

<!-- error: examples/err04_missing_bracket.expected_error -->
```output
SyntaxError: '(' was never closed
```

Fix: every opening bracket needs a closing bracket: `print("Hello")`.

The habit to build: read the last line of an error first. It names the kind of error. Then look at the line number to find where it happened.

## Think beyond

1. You want to print a shopping list with each item on its own line, using only one `print()`. Which setting from this chapter could help? Test your idea.
2. An AI gives you code that runs with no error. What two things should you check before you trust it?

## Recap

- A program is a list of instructions. Python runs them one at a time, from top to bottom.
- `print()` shows values. Text goes inside quotation marks. Calculations without quotation marks are worked out first.
- `sep` controls what goes between values, and `end` controls what goes after them.
- An error message names the kind of error and the line. Read the last line first.
- AI is a tutor. Ask it to explain, then run and check everything yourself.

You earned **100 XP** and the **First Run** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 2, you will give your data names with variables, so a program can store a value once and use it many times.
