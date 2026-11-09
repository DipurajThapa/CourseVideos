# Chapter 9: Debugging with AI: Reading Errors and Tracebacks

> Quest: tell the three kinds of bugs apart, read a traceback and find a silent bug. Then give an AI assistant everything it needs to help. Reward: 100 XP and the **Bug Hunter** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Explain the difference between a syntax error, a runtime error and a logic error.
- Read a traceback from the bottom up and find the line that Python names.
- Find a logic error by printing the values of variables inside a loop.
- Write a debugging prompt with the code, the exact error, the expected result and the actual result.
- Test a fix with several cases, including the case that failed.

## Why this matters

A **bug** is a mistake in a program that makes it stop or give a wrong result. Every programmer writes bugs, every day. The difference between a beginner and an experienced programmer is not the number of bugs. It is how fast they find them.

Asha's end-of-day report adds up the cafe's sales. One evening it says the total is 6.00, but the cafe took 14.00. There is no error message. Nothing looks broken. Bugs like this one are the most dangerous, because a wrong number can look like a right one.

AI assistants can help you find bugs, but only when you give them the right information. A vague question such as "my code is wrong, fix it" often gets a confident fix for the wrong problem.

## The idea

Bugs come in three kinds. Each kind shows itself in a different way.

| Kind | When it happens | What you see | Example |
|---|---|---|---|
| Syntax error | Before the program starts | An error report; no line of the program runs | A missing bracket |
| Runtime error | While the program runs | Some output, then a traceback | Multiplying text by a decimal number |
| Logic error | The program finishes | A wrong result and no error at all | Adding the wrong variable |

A **syntax error** means Python cannot read the file, so it runs nothing. A **runtime error** happens when Python reaches a line it cannot carry out. A **logic error** means the code does exactly what you wrote, but what you wrote is not what you meant.

Think of a recipe. A syntax error is a recipe with a smudged word that nobody can read, so cooking never starts. A runtime error is a step that asks for an ingredient you do not have, so cooking stops halfway. A logic error is a recipe that says salt where it should say sugar: the cake comes out, and it tastes wrong. Unlike a cook, Python never guesses what you meant.

## Build it step by step

**Step 1: A syntax error stops everything.** Asha's report starts with three lines. The last line is missing its closing bracket.

```python
# file: examples/ex01_syntax.py
print("Corner Cafe: end of day")
price = 4.5
print(f"Tea: {price:.2f}"
```

<!-- error: examples/ex01_syntax.expected_error -->
```output
  File "ex01_syntax.py", line 4
    print(f"Tea: {price:.2f}"
         ^
SyntaxError: '(' was never closed
```

Line 2 is correct, but it never ran: the output does not show `Corner Cafe: end of day`. Python reads the whole file before it runs any line. The report names the file, line 4 and the kind of error. The `^` marker points at the bracket that was never closed. Fix: add `)` at the end of line 4.

**Step 2: Read a traceback from the bottom up.** A **traceback** is the report Python prints when a runtime error stops a program. Here, the user types `12`.

```python
# file: examples/ex02_runtime.py
print("Corner Cafe: end of day")
cups = input("Cups of tea sold: ")
print(f"Cups: {cups}")
total = cups * 3.5
print(f"Tea total: {total:.2f}")
```

<!-- error: examples/ex02_runtime.expected_error -->
```output
Corner Cafe: end of day
Cups of tea sold: 12
Cups: 12
Traceback (most recent call last):
  File "ex02_runtime.py", line 5, in <module>
    total = cups * 3.5
            ~~~~~^~~~~
TypeError: can't multiply sequence by non-int of type 'float'
```

Lines 2 to 4 ran, so their output appears. Then Python stopped at line 5. Read the traceback from the bottom up:

1. The last line names the kind of error, `TypeError`, and describes it. A **sequence** is a value made of parts in order, and a string is one.
2. The line above shows the code, and the `~` and `^` markers point at the part that failed: `cups * 3.5`.
3. The line above that names the file and line 5.
4. The first line, `most recent call last`, means the newest step is at the bottom. In programs of this size there is only one step. In Chapter 16, tracebacks will grow longer.

The line that Python names is where it noticed the problem. The cause can be on an earlier line. Here, line 3 stored the answer as text, because `input()` always returns a string. Fix line 3 with `int()`:

```python
# file: examples/ex03_runtime_fixed.py
print("Corner Cafe: end of day")
cups = int(input("Cups of tea sold: "))
print(f"Cups: {cups}")
total = cups * 3.5
print(f"Tea total: {total:.2f}")
```

<!-- output: examples/ex03_runtime_fixed.expected -->
```output
Corner Cafe: end of day
Cups of tea sold: 12
Cups: 12
Tea total: 42.00
```

**Step 3: Spot a logic error.** This loop adds up three sales. The user types `4.50`, `6.00` and `3.50`, so the total should be 14.00.

```python
# file: examples/ex04_logic.py
total = 0
for sale in range(1, 4):
    price = float(input(f"Price of sale {sale}: "))
    total = total + sale
print(f"Total: {total:.2f}")
```

<!-- output: examples/ex04_logic.expected -->
```output
Price of sale 1: 4.50
Price of sale 2: 6.00
Price of sale 3: 3.50
Total: 6.00
```

The program finishes with no error, but 6.00 is wrong. You only notice because you know the expected result. Always work out the expected result before you run a program.

**Step 4: Find the bug with print debugging.** **Print debugging** means adding a temporary `print()` that shows the values of variables while the program runs. Asha adds line 6 inside the loop.

```python
# file: examples/ex05_print_debug.py
total = 0
for sale in range(1, 4):
    price = float(input(f"Price of sale {sale}: "))
    total = total + sale
    print(f"DEBUG sale={sale} price={price} total={total}")
print(f"Total: {total:.2f}")
```

<!-- output: examples/ex05_print_debug.expected -->
```output
Price of sale 1: 4.50
DEBUG sale=1 price=4.5 total=1
Price of sale 2: 6.00
DEBUG sale=2 price=6.0 total=3
Price of sale 3: 3.50
DEBUG sale=3 price=3.5 total=6
Total: 6.00
```

After the first sale, `total` is 1, not 4.5. The total grows by the sale number, not by the price. Line 5 adds `sale` where it should add `price`. Fix line 5, and remove the debug line:

```python
# file: examples/ex06_logic_fixed.py
total = 0
for sale in range(1, 4):
    price = float(input(f"Price of sale {sale}: "))
    total = total + price
print(f"Total: {total:.2f}")
```

<!-- output: examples/ex06_logic_fixed.expected -->
```output
Price of sale 1: 4.50
Price of sale 2: 6.00
Price of sale 3: 3.50
Total: 14.00
```

Start each debug line with a word such as `DEBUG`, so you can find it and remove it later.

**Step 5: Write a debugging prompt that works.** An AI assistant cannot see your screen or read your mind. Give it four things:

| Part | What to paste | Why it helps |
|---|---|---|
| Code | The whole program, or the lines around the problem | The AI needs the real code, not a description |
| Exact error | The full traceback, or "no error message" | The last line names the kind of error |
| Expected result | What you wanted, worked out by hand | Without it, a logic error is invisible |
| Actual result | What the program really printed | The difference points at the bug |

Then ask for the cause before the fix. A cause you understand teaches you something. A fix you do not understand can hide a second bug.

## See the outcome

Here is Asha's end-of-day report, with all three bugs fixed. The user types `3`, then the prices `4.50`, `6.00` and `3.50`.

```python
# file: examples/ex07_day_report.py
print("Corner Cafe: end of day")
sales = int(input("How many sales today? "))
total = 0
for sale in range(1, sales + 1):
    price = float(input(f"Price of sale {sale}: "))
    total = total + price
average = total / sales
print(f"Sales:   {sales}")
print(f"Total:   {total:.2f}")
print(f"Average: {average:.2f}")
```

<!-- output: examples/ex07_day_report.expected -->
```output
Corner Cafe: end of day
How many sales today? 3
Price of sale 1: 4.50
Price of sale 2: 6.00
Price of sale 3: 3.50
Sales:   3
Total:   14.00
Average: 4.67
```

The total matches the expected 14.00, and 14.00 divided by 3 is about 4.67. Line 3 converts the number of sales with `int()`, line 6 adds the price, and every bracket is closed.

## Work with AI

The AI skill for this chapter is the structured debugging prompt: the code, the exact error, the expected result and the actual result. Then ask for the cause before the fix, and test every fix yourself.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe the problem and ask for a plan to find the bug, with no code yet. |
| Write | Read the traceback yourself, write down the kind of error, the line and the cause, then ask AI to check your reading. |
| Generate | Ask for a fix with an exact expected output, then run it. |
| Test | Ask for test cases with the expected result for each, including the case that failed. Run every case. |
| Debug | Paste the code, the exact error, the expected result and the actual result. Ask for the cause first. |
| Improve | Ask how to make future bugs easier to find, without changing the output. Check each suggestion. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha tested her report with a day with no sales. She typed `0`, and the report crashed with `ZeroDivisionError: division by zero` on the average line. She asked an AI assistant: "Add a check so that 0 sales prints No sales today. instead of crashing. Tell me exactly what it prints for 0 sales." The AI said it would print `No sales today.` and gave this code.

```python
# file: examples/ai_check_flawed.py
print("Corner Cafe: end of day")
sales = int(input("How many sales today? "))
total = 0
for sale in range(1, sales + 1):
    price = float(input(f"Price of sale {sale}: "))
    total = total + price
if sales >= 0:
    average = total / sales
    print(f"Sales:   {sales}")
    print(f"Total:   {total:.2f}")
    print(f"Average: {average:.2f}")
else:
    print("No sales today.")
```

Asha typed `0` and ran it:

<!-- error: examples/ai_check_flawed.expected_error -->
```output
Corner Cafe: end of day
How many sales today? 0
Traceback (most recent call last):
  File "ai_check_flawed.py", line 9, in <module>
    average = total / sales
              ~~~~~~^~~~~~~
ZeroDivisionError: division by zero
```

The program still crashed. `sales >= 0` is true when `sales` is 0, so the program divides by zero anyway. This is the boundary mistake from Chapter 6. The condition must be `sales > 0`:

```python
# file: examples/ai_check_fixed.py
print("Corner Cafe: end of day")
sales = int(input("How many sales today? "))
total = 0
for sale in range(1, sales + 1):
    price = float(input(f"Price of sale {sale}: "))
    total = total + price
if sales > 0:
    average = total / sales
    print(f"Sales:   {sales}")
    print(f"Total:   {total:.2f}")
    print(f"Average: {average:.2f}")
else:
    print("No sales today.")
```

<!-- output: examples/ai_check_fixed.expected -->
```output
Corner Cafe: end of day
How many sales today? 0
No sales today.
```

Asha then ran the fixed report again with 1 sale and with 3 sales, and both gave the same results as before. Always test the case that failed, and test the cases that worked, after every fix.

## Common mistakes

**Mistake 1: a missing comma between values.**

```python
# file: examples/err01_comma.py
total = 14.0
print("Total:" total)
```

<!-- error: examples/err01_comma.expected_error -->
```output
  File "err01_comma.py", line 3
    print("Total:" total)
          ^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

Fix: separate the values with a comma, `print("Total:", total)`. Python's suggestion at the end of the message is often right, so read it.

**Mistake 2: using a variable before the line that creates it.**

```python
# file: examples/err02_before.py
for sale in range(1, 4):
    total = total + 5
total = 0
print(total)
```

<!-- error: examples/err02_before.expected_error -->
```output
Traceback (most recent call last):
  File "err02_before.py", line 3, in <module>
    total = total + 5
            ^^^^^
NameError: name 'total' is not defined
```

Python runs from top to bottom, so `total` does not exist yet on line 3. Fix: move `total = 0` above the loop.

**Mistake 3: a debug line with the wrong indentation.**

```python
# file: examples/err03_indent.py
total = 0
for sale in range(1, 4):
    total = total + 5
      print(total)
print(f"Total: {total}")
```

<!-- error: examples/err03_indent.expected_error -->
```output
  File "err03_indent.py", line 5
    print(total)
IndentationError: unexpected indent
```

Line 5 has six spaces, but the block uses four. Fix: indent a debug line exactly like the line above it.

**Mistake 4: a decimal comma in a number.** In many countries, people write 4,50 for four and a half. Python accepts only a decimal point.

```python
# file: examples/err04_decimal_comma.py
price = float(input("Price of the cake: "))
print(f"Cake: {price:.2f}")
```

<!-- error: examples/err04_decimal_comma.expected_error -->
```output
Price of the cake: 4,50
Traceback (most recent call last):
  File "err04_decimal_comma.py", line 2, in <module>
    price = float(input("Price of the cake: "))
ValueError: could not convert string to float: '4,50'
```

Fix: type `4.50`. The message even shows the exact text that failed, `'4,50'`.

## Think beyond

1. A program gives the right total for 1 sale but a wrong total for 3 sales. What kind of error is it, and which values would you print inside the loop to find it?
2. Asha's report divides by the number of sales. What other inputs could still crash it or give a strange result? Try a negative number of sales, and predict what happens before you run it.

## Recap

- A syntax error stops the program before any line runs. A runtime error stops it partway with a traceback. A logic error gives a wrong result and no message.
- Read a traceback from the bottom up: the kind of error, the code and markers, then the line number.
- The line Python names is where it noticed the problem; the cause can be earlier.
- Print debugging shows the values of variables while the program runs. Remove the debug lines afterwards.
- A good debugging prompt has the code, the exact error, the expected result and the actual result. Ask for the cause first.
- After a fix, test the case that failed and the cases that already worked.

You earned **100 XP** and the **Bug Hunter** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 10, the second boss level, you will combine decisions, loops and input checks to build a number guessing game.
