# Chapter 5: Boss Level 1: The Bill Splitter

> Quest: build a program that splits a cafe bill fairly between friends, with a tip, to the exact cent. Reward: 300 XP and the **Fair Share** badge.

## The mission

Four friends finish lunch at the Corner Cafe. The bill is 37.45, and they want to add a 15 percent tip. One friend types the numbers into a phone calculator and gets 10.7675 each. Nobody can pay 10.7675. Somebody rounds it to 10.77, and now the four payments add up to 43.08, one cent more than the real total.

Asha wants a tool that the cafe can give to every table. Your mission is to build it. It asks three questions, shows a neat receipt and tells each person exactly what to pay. If the total does not share out evenly, it also says how many cents are left over, so the table can decide who pays them.

This boss level uses everything from Chapters 1 to 4:

| Chapter | What you use from it |
|---|---|
| 1 | `print()` and running a program from top to bottom |
| 2 | Variables, `int` and `float`, the operators `/`, `//` and `%`, and `round()` |
| 3 | f-strings with `:.2f`, alignment with `<` and `>`, and centring with `^` |
| 4 | `input()`, and converting answers with `int()` and `float()` |

## What you will build

A program called `bill_splitter.py`. Here is a run for three friends who share a bill of 48 with a 10 percent tip. The text after each question is what the user typed.

<!-- output: project/bill_splitter.expected -->
```output
==== BILL SPLITTER =====
Bill total: 48
Tip percent: 10
Number of people: 3
------------------------
Bill               48.00
Tip 10%             4.80
Total              52.80
------------------------
Each pays          17.60
Extra cents            0
```

Every receipt line is 24 characters wide: 16 for the label and 8 for the amount, as on the receipt from Chapter 3.

## Acceptance criteria

Your program is finished when all of these are true:

1. It asks for the bill total, the tip percent and the number of people, in that order.
2. The bill can have decimals, such as `37.45`. The tip percent and the number of people are whole numbers.
3. It prints the bill, the tip and the total, each with exactly two decimal places, lined up in one column.
4. It prints what each person pays, rounded down to a whole cent.
5. It prints the extra cents that are left over. Each share times the number of people, plus the extra cents, equals the total exactly.
6. You tested it with at least four different sets of answers and compared each output with a result you worked out by hand.

## Plan it with AI

Plan before you write any code. Asha described the tool to an AI assistant and asked for a plan, not code:

> "I am a beginner. I know print, variables, int and float, the operators including // and %, f-strings and input. I want a program that splits a cafe bill between friends with a tip. Do not write code. List the inputs, the calculations in order and the outputs."

An example answer looked like this:

> Inputs: the bill total (float), the tip percent (int) and the number of people (int).
> Calculations: the tip is the bill times the tip percent, divided by 100. The total is the bill plus the tip. Each share is the total divided by the number of people.
> Outputs: the bill, the tip, the total and each share, with two decimal places.

The plan is a good start, but the last calculation hides the problem from the mission. Dividing 43.07 by 4 gives 10.7675, which is not a real amount of money. Asha added one step to the plan: **work in whole cents**. A whole number of cents can be shared with `//`, and `%` gives the cents that are left over.

## Build it step by step

**Step 1: Ask the three questions.** Each answer is converted as soon as it is read: `float()` for the bill, because it can have decimals, and `int()` for the two whole numbers.

```python
# file: examples/ex01_questions.py
print(f"{' BILL SPLITTER ':=^24}")
bill = float(input("Bill total: "))
tip_percent = int(input("Tip percent: "))
people = int(input("Number of people: "))
print(type(bill), type(tip_percent), type(people))
```

<!-- output: examples/ex01_questions.expected -->
```output
==== BILL SPLITTER =====
Bill total: 48
Tip percent: 10
Number of people: 3
<class 'float'> <class 'int'> <class 'int'>
```

Line 6 is only a check that each answer has the right type. The finished program does not need it.

**Step 2: Calculate the tip and the total.** A percent is a number out of 100, so 10 percent of 48 is 48 times 10, divided by 100.

```python
# file: examples/ex02_tip.py
bill = 48.0
tip_percent = 10
tip = bill * tip_percent / 100
total = bill + tip
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
```

<!-- output: examples/ex02_tip.expected -->
```output
Tip: 4.80
Total: 52.80
```

The values are written into the code here, so you can check the calculation without typing answers each time.

**Step 3: Share the total in whole cents.** Multiply by 100 and round, to get the total as a whole number of cents. Then `//` gives each person's share, and `%` gives the cents that are left over.

```python
# file: examples/ex03_cents.py
total = 43.07
people = 4
total_cents = round(total * 100)
share_cents = total_cents // people
extra_cents = total_cents % people
print("Total in cents:", total_cents)
print("Each pays (cents):", share_cents)
print("Extra cents:", extra_cents)
print("Check:", share_cents * people + extra_cents)
```

<!-- output: examples/ex03_cents.expected -->
```output
Total in cents: 4307
Each pays (cents): 1076
Extra cents: 3
Check: 4307
```

Line 4 uses `round()` because `total * 100` is a `float`, and a `float` can be a tiny amount below the whole number you expect. The check on line 10 proves that no cent is lost: 4 times 1076, plus 3, is 4307.

**Step 4: Turn cents back into money.** Divide by 100 to get the share as a `float`. Then format it with two decimal places, inside a 24-character receipt line.

```python
# file: examples/ex04_share.py
share_cents = 1760
share = share_cents / 100
print(share)
print(f"{share:.2f}")
print(f"{'Each pays':<16}{share:>8.2f}")
```

<!-- output: examples/ex04_share.expected -->
```output
17.6
17.60
Each pays          17.60
```

Line 4 prints `17.6`, because Python drops the last zero of a `float`. Line 5 uses `:.2f`, so the amount looks like money: `17.60`.

**Step 5: Put it together.** Here is the complete program. Lines 3 to 5 ask the questions, lines 7 to 12 calculate and lines 14 to 22 print the receipt.

```python
# file: project/bill_splitter.py
print(f"{' BILL SPLITTER ':=^24}")
bill = float(input("Bill total: "))
tip_percent = int(input("Tip percent: "))
people = int(input("Number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
total_cents = round(total * 100)
share_cents = total_cents // people
extra_cents = total_cents % people
share = share_cents / 100

tip_label = f"Tip {tip_percent}%"
line = "-" * 24
print(line)
print(f"{'Bill':<16}{bill:>8.2f}")
print(f"{tip_label:<16}{tip:>8.2f}")
print(f"{'Total':<16}{total:>8.2f}")
print(line)
print(f"{'Each pays':<16}{share:>8.2f}")
print(f"{'Extra cents':<16}{extra_cents:>8}")
```

Line 14 builds the tip label with the percent inside it, so the receipt shows `Tip 10%`. The last line prints `extra_cents` without `.2f`, because it is a whole number of cents.

## Test it

A test is a run with answers whose correct result you already know. Work out each result by hand first, then run the program and compare every line.

| Test | Answers typed | Result worked out by hand |
|---|---|---|
| Normal | 48, 10, 3 | Total 52.80, each pays 17.60, 0 extra cents |
| Decimal bill | 37.45, 15, 4 | Total 43.07, each pays 10.76, 3 extra cents |
| No tip | 20, 0, 2 | Total 20.00, each pays 10.00 |
| One person | 12.5, 10, 1 | Total 13.75, the one person pays all of it |

The normal test is shown in "What you will build". Here is the decimal bill, the case from the mission:

<!-- output: examples/test_decimal.expected -->
```output
==== BILL SPLITTER =====
Bill total: 37.45
Tip percent: 15
Number of people: 4
------------------------
Bill               37.45
Tip 15%             5.62
Total              43.07
------------------------
Each pays          10.76
Extra cents            3
```

Four people pay 10.76 each, which is 43.04. With the 3 extra cents, that is exactly 43.07. The tip, 5.6175, is shown rounded to 5.62. The no-tip and one-person tests also match the table:

<!-- output: examples/test_no_tip.expected -->
```output
==== BILL SPLITTER =====
Bill total: 20
Tip percent: 0
Number of people: 2
------------------------
Bill               20.00
Tip 0%              0.00
Total              20.00
------------------------
Each pays          10.00
Extra cents            0
```

<!-- output: examples/test_one_person.expected -->
```output
==== BILL SPLITTER =====
Bill total: 12.5
Tip percent: 10
Number of people: 1
------------------------
Bill               12.50
Tip 10%             1.25
Total              13.75
------------------------
Each pays          13.75
Extra cents            0
```

**AI pair moment.** While she built Step 2, Asha asked an AI assistant for help. "Write the two lines that calculate the tip and the total for a bill of 48 with a 10 percent tip. Tell me what they print." The AI said the code would print a tip of 4.80:

```python
# file: examples/ai_tip_flawed.py
bill = 48.0
tip_percent = 10
tip = bill * tip_percent
total = bill + tip
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
```

<!-- output: examples/ai_tip_flawed.expected -->
```output
Tip: 480.00
Total: 528.00
```

Her test caught it at once: she had worked out 4.80 by hand. The AI multiplied by 10 instead of by 10 percent. A percent must be divided by 100:

```python
# file: examples/ai_tip_fixed.py
bill = 48.0
tip_percent = 10
tip = bill * tip_percent / 100
total = bill + tip
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
```

<!-- output: examples/ai_tip_fixed.expected -->
```output
Tip: 4.80
Total: 52.80
```

**A test that breaks the program.** A friend typed 0 for the number of people. The program stopped on line 10, because nothing can be shared between zero people:

<!-- error: examples/test_zero_people.expected_error -->
```output
==== BILL SPLITTER =====
Bill total: 20
Tip percent: 10
Number of people: 0
Traceback (most recent call last):
  File "test_zero_people.py", line 10, in <module>
    share_cents = total_cents // people
                  ~~~~~~~~~~~~^^~~~~~~~
ZeroDivisionError: division by zero
```

A `ZeroDivisionError` happens when a program divides by zero. Older versions of Python word the last line as `integer division or modulo by zero`, with the same meaning. With what you know so far, the program cannot refuse a bad answer. For now, make the question clear, for example `Number of people (1 or more): `. In Chapter 6, you will learn to check an answer before you use it.

## Improve it with AI

When the program worked, Asha asked an AI assistant to review it: "Suggest one way to make this program simpler. Do not change what it prints." The AI suggested replacing the three cent lines with one line, `share = round(total / people, 2)`. It sounded reasonable, so she tested it with the mission's numbers before she changed anything:

```python
# file: examples/ai_round_share.py
total = 43.07
people = 4
share = round(total / people, 2)
print(f"Each pays: {share:.2f}")
print(f"Shares added up: {share * people:.2f}")
```

<!-- output: examples/ai_round_share.expected -->
```output
Each pays: 10.77
Shares added up: 43.08
```

The shares add up to 43.08, one cent more than the total. This is the problem from the mission, and the cent lines exist to prevent it. Asha kept her version. A suggestion that changes the result is not a simplification. Test every suggestion with the same answers you used before.

These are the six ways AI helped with this project. The full prompts are in [ai-prompts.md](ai-prompts.md).

| Stage | How AI helped |
|---|---|
| Plan | Listed the inputs, calculations and outputs, before any code. |
| Write | Checked that Asha's three questions use the right conversions. |
| Generate | Wrote the tip and total lines, with a confident mistake. |
| Test | Compared the output with a result worked out by hand. |
| Debug | Explained the `ZeroDivisionError` before suggesting a fix. |
| Improve | Suggested a "simpler" line that a test showed was wrong. |

## Recap

- A program is planned before it is written: inputs, calculations in order, then outputs.
- Convert each answer as soon as you read it: `float()` for amounts with decimals, `int()` for counts.
- A percent is divided by 100.
- Money is shared fairly in whole cents: `//` gives each share and `%` gives what is left over.
- A test is an answer whose correct result you worked out first. Test every AI suggestion the same way.

You earned **300 XP** and the **Fair Share** badge. Module 1 is complete.

The practice tasks for this chapter are in [practice/practice.md](practice/practice.md).

## What's next

In Chapter 6, you will make your programs decide: with `if`, the bill splitter can refuse zero people and say who pays the extra cents.
