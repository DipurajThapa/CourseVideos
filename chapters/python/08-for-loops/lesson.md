# Chapter 8: Repeat a Set Number of Times: for Loops and range()

> Quest: repeat a block a set number of times with `for` and `range()`, go through the characters of a string, and add up totals. Reward: 100 XP and the **Pattern Runner** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write a `for` loop that repeats a block once for each number in a `range()`.
- Use `range()` with a start, a stop and a step, and predict the numbers it gives.
- Go through every character of a string with a `for` loop.
- Add up a total inside a `for` loop.
- Compare two loops that do the same job and explain which one is clearer.

## Why this matters

In Chapter 7, Asha served tables 1 to 3 with a `while` loop. The loop needed three separate lines to work: the counter's start value, the condition and the line that adds 1. A mistake in any one of them breaks the loop. If the line that adds 1 is missing, the loop never ends.

Often you know in advance how many times something must happen. A receipt has 5 lines. A loyalty card has 10 stamps. An order code has 12 characters. For these jobs, Python has the `for` loop. It counts for you, so there is no counter line to forget.

## The idea

A `for` loop takes the values from a sequence one at a time. A **sequence** is a group of values in a fixed order, such as the numbers that `range()` makes or the characters of a string. On each pass, the loop variable gets the next value. When there are no values left, the loop ends.

```text
for table in range(1, 4):      range(1, 4) gives 1, 2, 3
                                
   pass 1:  table = 1  ->  run the block
   pass 2:  table = 2  ->  run the block
   pass 3:  table = 3  ->  run the block
   no values left       ->  continue after the loop
```

`range(start, stop)` starts at `start` and stops **before** `stop`. The stop value itself is never included. So `range(1, 4)` gives 1, 2 and 3, which is three values.

Think of a stamp card with numbered boxes. You move from box 1 to the last box, one box at a time, and you never skip or repeat a box. Unlike a stamp card, `range()` does not include the number written at the end: the box called `stop` is not on the card.

## Build it step by step

**Step 1: Repeat with `for` and `range()`.** Here is the Chapter 7 loop that served tables 1 to 3, written with `for`.

```python
# file: examples/ex01_tables.py
for table in range(1, 4):
    print(f"Serving table {table}")
print("All tables served.")
```

<!-- output: examples/ex01_tables.expected -->
```output
Serving table 1
Serving table 2
Serving table 3
All tables served.
```

The loop variable `table` gets 1, then 2, then 3. There is no `table = 1` line and no `table = table + 1` line: `range()` does both jobs. Line 4 is not indented, so it runs once, after the loop.

**Step 2: Use the three forms of `range()`.** With one number, `range()` starts at 0. With three numbers, the third one is the **step**: how much to add each time. A negative step counts down.

```python
# file: examples/ex02_range_forms.py
for n in range(4):
    print(n, end=" ")
print()
for n in range(2, 6):
    print(n, end=" ")
print()
for n in range(10, 0, -3):
    print(n, end=" ")
print()
```

<!-- output: examples/ex02_range_forms.expected -->
```output
0 1 2 3
2 3 4 5
10 7 4 1
```

`end=" "` from Chapter 1 keeps each loop's numbers on one line, and the empty `print()` ends the line. `range(4)` gives four values, 0 to 3. `range(10, 0, -3)` counts down by 3 and stops before 0, so the last value is 1.

| Form | Example | Values |
|---|---|---|
| `range(stop)` | `range(4)` | 0, 1, 2, 3 |
| `range(start, stop)` | `range(2, 6)` | 2, 3, 4, 5 |
| `range(start, stop, step)` | `range(10, 0, -3)` | 10, 7, 4, 1 |

**Step 3: Go through the characters of a string.** A `for` loop can take the characters of a string, one at a time. This loop prints Asha's order code from Chapter 1 with spaces and counts its hyphens.

```python
# file: examples/ex03_order_code.py
code = "CAFE-1024-T4"
hyphens = 0
for character in code:
    print(character, end=" ")
    if character == "-":
        hyphens += 1
print()
print(f"{len(code)} characters, {hyphens} hyphens")
```

<!-- output: examples/ex03_order_code.expected -->
```output
C A F E - 1 0 2 4 - T 4
12 characters, 2 hyphens
```

The block runs 12 times, once for each character. The `if` inside the loop adds 1 to `hyphens` only on the two passes where `character` is a hyphen.

**Step 4: Add up a total.** A running total from Chapter 7 works the same way in a `for` loop. Asha types the sales for three days. In this chapter, the output shows the user's answer after each question, as it appears in the terminal.

```python
# file: examples/ex04_week_sales.py
total = 0
for day in range(1, 4):
    sales = float(input(f"Sales on day {day}: "))
    total += sales
print(f"Total: {total:.2f}")
print(f"Average: {total / 3:.2f}")
```

<!-- output: examples/ex04_week_sales.expected -->
```output
Sales on day 1: 120.5
Sales on day 2: 98
Sales on day 3: 143.25
Total: 361.75
Average: 120.58
```

Line 2 sets the total to 0 once, before the loop. Line 5 adds each day's sales on every pass. The average is 361.75 divided by 3, shown with two decimal places.

**Step 5: Count down, and choose between `for` and `while`.** The kettle needs 5 minutes. A step of `-1` counts down.

```python
# file: examples/ex05_kettle.py
for minute in range(5, 0, -1):
    print(f"{minute} min left")
print("Tea is ready!")
```

<!-- output: examples/ex05_kettle.expected -->
```output
5 min left
4 min left
3 min left
2 min left
1 min left
Tea is ready!
```

Use `for` when you know the number of passes before the loop starts: 5 minutes, 10 stamps, 12 characters. Use `while` when you wait for something, such as a valid answer or the word `done`, and you cannot know how many passes it will take.

## See the outcome

Here is Asha's price chart for the cafe counter. Every 5th tea is free, so 5 teas cost the same as 4.

```python
# file: examples/ex06_price_chart.py
tea_price = 3.5
print("Teas   Price")
for teas in range(1, 11):
    free = teas // 5
    cost = (teas - free) * tea_price
    print(f"{teas:>4} {cost:>7.2f}")
print("Every 5th tea is free.")
```

<!-- output: examples/ex06_price_chart.expected -->
```output
Teas   Price
   1    3.50
   2    7.00
   3   10.50
   4   14.00
   5   14.00
   6   17.50
   7   21.00
   8   24.50
   9   28.00
  10   28.00
Every 5th tea is free.
```

`range(1, 11)` gives 1 to 10. `teas // 5` from Chapter 2 counts the free teas: 0 for 1 to 4 teas, 1 for 5 to 9 teas and 2 for 10 teas. The format specifications from Chapter 3 line up the columns.

## Work with AI

The AI skill for this chapter is comparing loops. When an AI assistant writes a loop for a job you already solved, run both with the same values and compare the outputs line by line. Then decide which loop is clearer for a person who reads it later.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe the repeated job and ask AI whether a `for` or a `while` loop fits, and which `range()` to use. |
| Write | Write the loop yourself, then ask AI to list the values the loop variable takes. |
| Generate | Ask for a `for` version of your loop, with the exact output. |
| Test | Ask for checks with the expected result for each, such as the first and last line and the number of lines, then run them. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask which loop is clearer and why. Run both and compare every line before you accept a change. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha's loyalty card has 10 stamps, and every 5th stamp is a free tea. She had written it with a `while` loop. She asked an AI assistant: "Rewrite my loyalty card with a for loop and range(). Keep the same output: 10 stamps, with FREE TEA on stamps 5 and 10. Show the exact output." The AI said the output would be the same 10 lines, and gave this code.

```python
# file: examples/ai_stamps_flawed.py
for stamp in range(1, 10):
    if stamp % 5 == 0:
        print(f"Stamp {stamp}: FREE TEA")
    else:
        print(f"Stamp {stamp}: [ ]")
```

Asha ran it:

<!-- output: examples/ai_stamps_flawed.expected -->
```output
Stamp 1: [ ]
Stamp 2: [ ]
Stamp 3: [ ]
Stamp 4: [ ]
Stamp 5: FREE TEA
Stamp 6: [ ]
Stamp 7: [ ]
Stamp 8: [ ]
Stamp 9: [ ]
```

There are only 9 stamps, and the second free tea is missing. `range(1, 10)` stops before 10. This is an off-by-one error, the same kind as in Chapter 7. The stop value must be one more than the last stamp:

```python
# file: examples/ai_stamps_fixed.py
for stamp in range(1, 11):
    if stamp % 5 == 0:
        print(f"Stamp {stamp}: FREE TEA")
    else:
        print(f"Stamp {stamp}: [ ]")
```

<!-- output: examples/ai_stamps_fixed.expected -->
```output
Stamp 1: [ ]
Stamp 2: [ ]
Stamp 3: [ ]
Stamp 4: [ ]
Stamp 5: FREE TEA
Stamp 6: [ ]
Stamp 7: [ ]
Stamp 8: [ ]
Stamp 9: [ ]
Stamp 10: FREE TEA
```

Asha checked the output against her own `while` version, line by line, and all 10 lines matched. A quick check catches this kind of flaw: count the lines of output, and look at the last line first.

## Common mistakes

**Mistake 1: a stop value that is one too small.** Asha wants tables 1 to 3, but she wrote `range(1, 3)`.

```python
# file: examples/ex07_off_by_one.py
for table in range(1, 3):
    print(f"Serving table {table}")
print("All tables served.")
```

<!-- output: examples/ex07_off_by_one.expected -->
```output
Serving table 1
Serving table 2
All tables served.
```

There is no error, but table 3 is never served. Fix: the stop value is one more than the last value you want, `range(1, 4)`.

**Mistake 2: a decimal number in `range()`.** `range()` works only with whole numbers.

```python
# file: examples/err01_range_float.py
for size in range(0.5, 3):
    print(f"Cup size {size}")
```

<!-- error: examples/err01_range_float.expected_error -->
```output
Traceback (most recent call last):
  File "err01_range_float.py", line 2, in <module>
    for size in range(0.5, 3):
                ~~~~~^^^^^^^^
TypeError: 'float' object cannot be interpreted as an integer
```

Fix: use whole numbers in `range()`. If a number comes from `input()`, convert it with `int()`, not `float()`.

**Mistake 3: setting the total to 0 inside the loop.** The total must start at 0 once, before the loop.

```python
# file: examples/ex08_total_inside.py
for day in range(1, 4):
    total = 0
    sales = float(input(f"Sales on day {day}: "))
    total += sales
print(f"Total: {total:.2f}")
```

<!-- output: examples/ex08_total_inside.expected -->
```output
Sales on day 1: 120.5
Sales on day 2: 98
Sales on day 3: 143.25
Total: 143.25
```

There is no error, but the total is only the last day's sales. Line 3 sets `total` back to 0 on every pass. Fix: move `total = 0` above the loop, as in Step 4.

**Mistake 4: a missing colon.** Every `for` line ends with a colon, like `if` and `while`.

```python
# file: examples/err02_no_colon.py
for table in range(1, 4)
    print(f"Serving table {table}")
```

<!-- error: examples/err02_no_colon.expected_error -->
```output
  File "err02_no_colon.py", line 2
    for table in range(1, 4)
                            ^
SyntaxError: expected ':'
```

Fix: add the colon at the end of line 2: `for table in range(1, 4):`.

## Think beyond

1. The cafe gives a stamp only on even-numbered tables, from 2 to 20. How could one `range()` with a step give exactly those numbers? Predict the values first, then run it.
2. A customer's name is typed with capital and small letters, such as `Anna Abbas`. How could a `for` loop count every letter `a`, capital or small? Think about which string method from Chapter 3 helps.

## Recap

- A `for` loop runs its block once for each value in a sequence, such as a `range()` or a string.
- `range(start, stop, step)` stops before `stop`. `range(4)` starts at 0 and gives four values.
- A negative step counts down, as in `range(5, 0, -1)`.
- A running total starts at 0 before the loop and grows inside it.
- Use `for` when you know the number of passes, and `while` when you wait for something.
- Run an AI loop and your own loop with the same values, compare every line, then choose the clearer one.

You earned **100 XP** and the **Pattern Runner** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 9, you will read error messages and tracebacks in detail, and use AI as a debugging partner for syntax errors, runtime errors and logic errors.
