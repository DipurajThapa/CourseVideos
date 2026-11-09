# Chapter 7: Repeat Until Done: while Loops

> Quest: make your programs repeat a block of code until a job is done, with `while`, counters and `break`. Reward: 100 XP and the **Loop Tamer** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write a `while` loop that repeats a block while its condition is `True`.
- Use a counter and a running total that change on every pass of a loop.
- Ask a question again until the answer is valid.
- Stop a loop with a stop value or with `break`.
- Trace a loop in a table and explain why a loop never ends.

## Why this matters

In Chapter 6, the bill splitter learned to say "People must be 1 or more." But then it stopped. The customer had to run the whole program again to type a better answer. And Asha's checkout could take only one order, with a number of teas fixed in advance.

Real programs repeat. A cash machine asks for your PIN again after a wrong try. A shop's till keeps scanning items until the cashier presses "Total". A game keeps running until you quit. Each of these is a **loop**: a block of code that runs again and again until a condition says stop.

## The idea

A `while` loop checks a condition. If the condition is `True`, Python runs the indented block, then goes back to the top and checks the condition again. When the condition is `False`, Python skips the block and continues with the next line after it.

```text
        +--------------------------+
        |                          |
        v                          |
   table <= 3 ?                    |
    /        \                     |
 True        False                 |
   |           |                   |
 run the     continue after        |
 block       the loop              |
   |                               |
   +-------------------------------+
     (go back and check again)
```

One run of the block is called a **pass**. Something inside the block must change the value that the condition checks. Otherwise the condition stays `True` forever, and the loop never ends.

Think of a waiter who walks from table to table and asks "Anything else?" until every table is served. Unlike a waiter, Python does not get tired or notice that something is wrong. If nothing changes, it keeps going round forever.

## Build it step by step

**Step 1: Repeat with a counter.** A **counter** is a variable that counts the passes. Asha serves tables 1 to 3.

```python
# file: examples/ex01_count.py
table = 1
while table <= 3:
    print(f"Serving table {table}")
    table = table + 1
print("All tables served.")
```

<!-- output: examples/ex01_count.expected -->
```output
Serving table 1
Serving table 2
Serving table 3
All tables served.
```

Line 5 adds 1 to the counter on every pass. After the third pass, `table` is 4, so `table <= 3` is `False` and the loop ends. Line 6 is not indented, so it runs once, after the loop.

**Step 2: Ask again until the answer is valid.** This loop fixes the problem from Chapter 6: the program asks again instead of stopping. In this chapter, the output shows the user's answer after each question, as it appears in the terminal.

```python
# file: examples/ex02_ask_again.py
people = int(input("Number of people: "))
while people < 1:
    print("Please type 1 or more.")
    people = int(input("Number of people: "))
print(f"Table for {people}, please follow me.")
```

<!-- output: examples/ex02_ask_again.expected -->
```output
Number of people: 0
Please type 1 or more.
Number of people: -2
Please type 1 or more.
Number of people: 4
Table for 4, please follow me.
```

Line 2 asks once before the loop, so `people` has a value when line 3 checks it. Line 5 asks again inside the loop. That new answer is what can make the condition `False`.

**Step 3: Keep a running total.** A **running total** is a variable that grows on every pass. The user types prices, and 0 means "finished". A value like this, which means "stop", is called a **stop value**. `total += price` is short for `total = total + price`, and `-=` takes away in the same way.

```python
# file: examples/ex03_running_total.py
total = 0
count = 0
price = float(input("Price (0 to finish): "))
while price != 0:
    total += price
    count += 1
    price = float(input("Price (0 to finish): "))
print(f"Items: {count}")
print(f"Total: {total:.2f}")
```

<!-- output: examples/ex03_running_total.expected -->
```output
Price (0 to finish): 3.5
Price (0 to finish): 4
Price (0 to finish): 2.25
Price (0 to finish): 0
Items: 3
Total: 9.75
```

The stop value, 0, is not added: the loop checks it on line 5 before line 6 can add it. The total is 3.5 + 4 + 2.25, which is 9.75.

**Step 4: Stop a loop from inside with `break`.** `while True:` starts a loop whose condition is always `True`. `break` ends the loop immediately, and Python continues after it.

```python
# file: examples/ex04_break.py
while True:
    item = input("Item (or done): ").strip().lower()
    if item == "done":
        break
    print(f"Added: {item}")
print("Order closed.")
```

<!-- output: examples/ex04_break.expected -->
```output
Item (or done): tea
Added: tea
Item (or done): Cake
Added: cake
Item (or done): Done
Order closed.
```

When the user types `Done`, `.strip().lower()` turns it into `done`, so `break` runs. Line 6 is skipped for that answer, and line 7 runs.

**Step 5: Trace a loop in a table.** A **trace table** writes down the value of each variable on every pass. It shows exactly why a loop ends.

```python
# file: examples/ex05_trace.py
cups = 1
while cups < 20:
    cups = cups * 2
    print(cups)
print("Stopped at", cups)
```

<!-- output: examples/ex05_trace.expected -->
```output
2
4
8
16
32
Stopped at 32
```

| Pass | `cups` at the check | `cups < 20` | `cups` after line 4 |
|---|---|---|---|
| 1 | 1 | `True` | 2 |
| 2 | 2 | `True` | 4 |
| 3 | 4 | `True` | 8 |
| 4 | 8 | `True` | 16 |
| 5 | 16 | `True` | 32 |
| – | 32 | `False` | loop ends |

The last value is 32, not 16. Python checks the condition only at the top of each pass, so the fifth pass runs completely before the check finds `False`.

## See the outcome

Here is Asha's order loop. It takes items until the customer types `done`, adds the right price for each item and counts them.

```python
# file: examples/ex06_order_loop.py
total = 0
items = 0
while True:
    item = input("Item (tea, cake or done): ").strip().lower()
    if item == "done":
        break
    if item == "tea":
        total += 3.5
        items += 1
    elif item == "cake":
        total += 4.0
        items += 1
    else:
        print("Sorry, we only have tea and cake.")
print(f"Items: {items}")
print(f"Total: {total:.2f}")
```

<!-- output: examples/ex06_order_loop.expected -->
```output
Item (tea, cake or done): tea
Item (tea, cake or done): Cake
Item (tea, cake or done): coffee
Sorry, we only have tea and cake.
Item (tea, cake or done): tea
Item (tea, cake or done): done
Items: 3
Total: 11.00
```

Two teas and one cake cost 3.5 + 4.0 + 3.5, which is 11.00. Coffee is not on the menu, so the `else` block prints a message, and neither the total nor the count changes.

## Work with AI

The AI skill for this chapter is tracing. Before you trust a loop, ask an AI assistant to trace it step by step for one set of answers, in a table. A trace shows which value changes on each pass, and which one never changes.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe the repeat rule in words and ask AI for the loop condition, the stop rule and the test answers. |
| Write | Write the loop yourself, then ask AI to trace it for one set of answers. |
| Generate | Ask for a change to your loop, and the exact output for one set of answers. |
| Test | Ask for edge cases with the expected output for each, then run every one. |
| Debug | Paste the code and the run that went wrong. Ask AI to trace it in a table before it suggests a fix. |
| Improve | Ask for a clearer version, then count the questions it asks with the same test answers. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha's loop asked for the number of teas until the answer was from 1 to 10. She asked an AI assistant: "Add a limit to my loop: at most 3 tries. After 3 wrong answers, print 'Too many tries. Using 1 tea.' and use 1. If the answers are 0, 0 and 0, tell me exactly what it prints." The AI predicted 3 questions and then `Too many tries. Using 1 tea.` It gave this code.

```python
# file: examples/ai_tries_flawed.py
tries = 1
teas = int(input("How many teas? (1 to 10) "))
while (teas < 1 or teas > 10) and tries < 3:
    print("Please type a number from 1 to 10.")
    teas = int(input("How many teas? (1 to 10) "))
if teas < 1 or teas > 10:
    print("Too many tries. Using 1 tea.")
    teas = 1
print(f"Teas: {teas}")
```

Asha ran it with the answers 0, 0, 0 and then 5:

<!-- output: examples/ai_tries_flawed.expected -->
```output
How many teas? (1 to 10) 0
Please type a number from 1 to 10.
How many teas? (1 to 10) 0
Please type a number from 1 to 10.
How many teas? (1 to 10) 0
Please type a number from 1 to 10.
How many teas? (1 to 10) 5
Teas: 5
```

The program asked a fourth time. A trace shows why: `tries` is 1 on every pass, because no line inside the loop changes it. So `tries < 3` is always `True`, and the limit never works. A customer who keeps typing 0 would be asked forever. Adding `tries += 1` inside the loop fixes it:

```python
# file: examples/ai_tries_fixed.py
tries = 1
teas = int(input("How many teas? (1 to 10) "))
while (teas < 1 or teas > 10) and tries < 3:
    print("Please type a number from 1 to 10.")
    teas = int(input("How many teas? (1 to 10) "))
    tries += 1
if teas < 1 or teas > 10:
    print("Too many tries. Using 1 tea.")
    teas = 1
print(f"Teas: {teas}")
```

<!-- output: examples/ai_tries_fixed.expected -->
```output
How many teas? (1 to 10) 0
Please type a number from 1 to 10.
How many teas? (1 to 10) 0
Please type a number from 1 to 10.
How many teas? (1 to 10) 0
Too many tries. Using 1 tea.
Teas: 1
```

Asha ran all her test cases again on the fixed code: 1, 10, 11 then 5, 0 then 0 then 5, and three 0 answers. All five passed. The brackets on line 4 matter: Python checks the whole `or` part first, then the `and`. Every value in a loop condition needs a line inside the loop that can change it.

## Common mistakes

**Mistake 1: using a variable before it has a value.** The condition is checked before the first pass, so every name in it must already exist.

```python
# file: examples/err01_not_created.py
while answer != "done":
    answer = input("Item (or done): ")
print("Order closed.")
```

<!-- error: examples/err01_not_created.expected_error -->
```output
Traceback (most recent call last):
  File "err01_not_created.py", line 2, in <module>
    while answer != "done":
          ^^^^^^
NameError: name 'answer' is not defined
```

Fix: ask once before the loop, as in Step 2, or use `while True:` with `break`, as in Step 4.

**Mistake 2: stopping one pass too early.** Asha wants tables 1 to 3, but she wrote `<` instead of `<=`.

```python
# file: examples/ex07_off_by_one.py
table = 1
while table < 3:
    print(f"Serving table {table}")
    table = table + 1
print("All tables served.")
```

<!-- output: examples/ex07_off_by_one.expected -->
```output
Serving table 1
Serving table 2
All tables served.
```

There is no error, but table 3 is never served. This is called an **off-by-one error**. Fix: use `table <= 3`, and check the last pass with a trace table.

**Mistake 3: a loop that never ends.** If nothing inside the loop changes the value in the condition, the loop runs forever. This fragment is shown only to illustrate; do not run it as it is.

```python
# illustrative: the counter never changes
table = 1
while table <= 3:
    print(f"Serving table {table}")
```

It prints `Serving table 1` again and again. To stop a running program, click in the terminal and press Ctrl+C. Python stops with a `KeyboardInterrupt` message. Fix: add `table = table + 1` inside the loop.

**Mistake 4: a stop value with different capital letters.** This loop checks for `done`, but the user typed `Done`.

```python
# file: examples/ex08_done_case.py
item = input("Item (or done): ")
while item != "done":
    print(f"Added: {item}")
    item = input("Item (or done): ")
print("Order closed.")
```

<!-- output: examples/ex08_done_case.expected -->
```output
Item (or done): tea
Added: tea
Item (or done): Done
Added: Done
Item (or done): done
Order closed.
```

`Done` was added to the order as if it were an item. Fix: compare `item.strip().lower()`, as in Step 4.

## Think beyond

1. The cafe kettle needs 5 minutes. Write a loop that counts down from 5 to 1 and then prints `Tea is ready!`. Which value must change on each pass, and in which direction?
2. Asha's order loop accepts any number of items. How could you stop it after 10 items, even if the customer never types `done`? Trace your loop with 10 items before you run it.

## Recap

- A `while` loop runs its block again and again while its condition is `True`.
- Something inside the loop must change the value that the condition checks.
- A counter counts passes; a running total grows on every pass. `total += price` is short for `total = total + price`.
- A stop value or `break` ends a loop when the user is finished.
- A trace table shows every value on every pass, so you can see why a loop ends or why it never does.
- Ask AI to trace a loop, then run the same answers yourself.

You earned **100 XP** and the **Loop Tamer** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 8, you will use `for` loops and `range()` to repeat a block a set number of times, without a counter of your own.
