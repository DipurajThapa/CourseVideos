# Chapter 6: Making Decisions: if, elif and else

> Quest: make your programs check a fact and choose what to do, with `if`, `elif` and `else`. Reward: 100 XP and the **Decision Maker** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write comparisons with `==`, `!=`, `<`, `>`, `<=` and `>=`, and explain why each one gives `True` or `False`.
- Write `if`, `elif` and `else` blocks with correct colons and indentation.
- Combine conditions with `and`, `or` and `not`.
- Compare text answers safely with `.strip()` and `.lower()`.
- Fix the `SyntaxError` and `IndentationError` messages that beginners meet with `if`.

## Why this matters

In Chapter 5, the bill splitter stopped with a `ZeroDivisionError` when someone typed 0 people. It also could not give the member discount only to members. A program that runs every line, every time, cannot react to the answers it gets.

Real programs decide all the time. A cash machine checks that your balance is high enough before it pays out. A shop gives free delivery when the order is over a set amount. A login page lets you in only when the password matches. Each of these is a decision: check a fact, then choose what to do.

## The idea

A **condition** is an expression that Python works out to `True` or `False`. You met `True` and `False` in Chapter 2: they are the two values of the type `bool`. A **comparison operator** compares two values and gives a `bool`:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | is equal to | `3.5 == 3.5` | `True` |
| `!=` | is not equal to | `3.5 != 3.5` | `False` |
| `<` | is less than | `12 < 15` | `True` |
| `>` | is greater than | `15 > 15` | `False` |
| `<=` | is less than or equal to | `15 <= 15` | `True` |
| `>=` | is greater than or equal to | `15 >= 15` | `True` |

`=` and `==` are different. One `=` gives a name a value. Two `==` ask whether two values are equal.

An `if` statement runs a block of lines only when its condition is `True`. The **block** is the group of indented lines under the line that ends with a colon.

```text
  if people == 0:                  <- condition, then a colon
      print("Please type 1 or more.")   <- the block: 4 spaces in
  print("Thank you!")              <- not indented: always runs

          people == 0 ?
           /        \
        True        False
          |           |
     run the block   skip it
           \        /
       continue with the next line
```

Think of a condition as a gate at the cafe door that checks one fact, such as "Is this person a member?". Unlike a person at a door, the gate cannot guess. It checks exactly what you wrote, so `"Yes"` and `"yes"` are two different answers.

## Build it step by step

**Step 1: Compare values.** Each comparison gives a `bool`. Predict each line before you run it.

```python
# file: examples/ex01_compare.py
tea_price = 3.5
print(tea_price > 3)
print(tea_price == 3.5)
print(tea_price != 3.5)
print(tea_price <= 3)
print("Tea" == "tea")
print(type(tea_price > 3))
```

<!-- output: examples/ex01_compare.expected -->
```output
True
True
False
False
False
<class 'bool'>
```

Line 7 gives `False` because capital letters matter in text. Line 8 shows that a comparison is a value of type `bool`.

**Step 2: Run lines only when a condition is true.** Write `if`, the condition and a colon. Indent the block by 4 spaces. In this chapter, the output shows the user's answer after each question, as it appears in the terminal.

```python
# file: examples/ex02_if.py
people = int(input("Number of people: "))
if people == 0:
    print("Please type 1 or more.")
    print("A bill needs 1 person or more.")
print("Thank you!")
```

<!-- output: examples/ex02_if.expected -->
```output
Number of people: 0
Please type 1 or more.
A bill needs 1 person or more.
Thank you!
```

The user typed 0, so the condition is `True` and both indented lines run. If the user types 4, Python skips the block and prints only `Thank you!`. Line 6 is not indented, so it always runs.

**Step 3: Choose between two paths with `else`.** The `else` block runs when the condition is `False`. Exactly one of the two blocks runs. This is the fix for the bill splitter's crash.

```python
# file: examples/ex03_else.py
bill = float(input("Bill total: "))
people = int(input("Number of people: "))
if people > 0:
    share = bill / people
    print(f"Each pays: {share:.2f}")
else:
    print("People must be 1 or more.")
print("Done.")
```

<!-- output: examples/ex03_else.expected -->
```output
Bill total: 20
Number of people: 0
People must be 1 or more.
Done.
```

With 0 people, line 4 is `False`, so Python never reaches the division on line 5. The program no longer crashes.

**Step 4: Choose between more paths with `elif`.** `elif` means "else, if". Python checks the conditions from top to bottom and runs only the first block whose condition is `True`. The cafe gives a free cake for 50 or more, and a free biscuit for 15 or more.

```python
# file: examples/ex04_elif.py
to_pay = float(input("Amount to pay: "))
if to_pay >= 50:
    print("Reward: a free cake")
elif to_pay >= 15:
    print("Reward: a free biscuit")
else:
    print("Reward: none this time")
```

<!-- output: examples/ex04_elif.expected -->
```output
Amount to pay: 15
Reward: a free biscuit
```

An amount of exactly 15 is a **boundary value**: the point where the result changes. `>=` includes 15, so the customer gets a biscuit. Because Python stops at the first `True` condition, the order matters: put the biggest amount first.

**Step 5: Combine conditions with `and`, `or` and `not`.** `and` is `True` only when both sides are `True`. `or` is `True` when at least one side is `True`. `not` turns `True` into `False` and `False` into `True`.

```python
# file: examples/ex05_and_or.py
is_member = True
to_pay = 12.0
day = "Friday"
print(is_member and to_pay >= 15)
print(is_member or to_pay >= 15)
print(not is_member)
print(day == "Friday" or day == "Saturday")
```

<!-- output: examples/ex05_and_or.expected -->
```output
False
True
False
True
```

Line 5 is `False` because 12 is less than 15. Line 8 needs a full comparison on each side of `or`.

**Step 6: Compare text answers safely.** A user may type `Yes`, `yes` or `YES `, with a space at the end. `.strip()` removes spaces at both ends and `.lower()` makes every letter small, so all three become `yes`.

```python
# file: examples/ex06_lower.py
answer = input("Are you a member? (yes/no) ")
if answer.strip().lower() == "yes":
    print("Member discount: 10%")
else:
    print("No discount")
```

<!-- output: examples/ex06_lower.expected -->
```output
Are you a member? (yes/no) Yes 
Member discount: 10%
```

The user typed `Yes` with a space after it. After `.strip().lower()`, the answer is exactly `yes`, so the condition is `True`.

## See the outcome

Here is Asha's cafe checkout. It gives the 10 percent discount only to members and a free biscuit when the amount to pay is 15 or more.

```python
# file: examples/ex07_checkout.py
name = input("Name: ")
teas = int(input("How many teas? "))
member = input("Member? ").strip().lower()

bill = teas * 3.5
if member == "yes":
    discount = bill * 0.1
else:
    discount = 0
to_pay = bill - discount

print(f"Bill for {name}: {bill:.2f}")
print(f"Discount: {discount:.2f}")
print(f"To pay: {to_pay:.2f}")
if to_pay >= 15:
    print("Reward: a free biscuit")
else:
    print("Thank you, see you soon!")
```

<!-- output: examples/ex07_checkout.expected -->
```output
Name: Asha
How many teas? 6
Member? Yes
Bill for Asha: 21.00
Discount: 2.10
To pay: 18.90
Reward: a free biscuit
```

Six teas cost 21.00. The answer `Yes` becomes `yes` on line 4, so the member discount of 2.10 applies. The amount to pay, 18.90, is 15 or more, so the customer gets a biscuit. Run it again and answer `no`: the discount is 0.00.

## Work with AI

The AI skill for this chapter is asking for edge cases. An **edge case** is an unusual input that can break a condition, such as a boundary value, zero, or an answer with capital letters. Before you trust a condition, ask an AI assistant to list the edge cases, then run each one.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe a rule in words and ask AI to list the conditions and the boundary values to test. |
| Write | Write the condition yourself, then ask AI what happens at the boundary value. |
| Generate | Ask for an `if` block with the exact rule, and the exact output for one boundary value. |
| Test | Ask for edge cases with the result each one should give, then run every one. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask for a clearer version, then test it with the same edge cases before you accept it. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha asked an AI assistant: "Write Python code that prints 'Reward: a free biscuit' when to_pay is 15 or more, and 'No biscuit this time' otherwise. If to_pay is exactly 15.0, tell me exactly what it prints." The AI said it would print `Reward: a free biscuit`.

```python
# file: examples/ai_biscuit_flawed.py
to_pay = 15.0
if to_pay > 15:
    print("Reward: a free biscuit")
else:
    print("No biscuit this time")
```

Asha ran it with the boundary value, 15.0:

<!-- output: examples/ai_biscuit_flawed.expected -->
```output
No biscuit this time
```

The AI used `>`, which means "more than", but the rule says "15 or more". The prediction and the code did not agree, and the AI sounded sure. `>=` fixes it:

```python
# file: examples/ai_biscuit_fixed.py
to_pay = 15.0
if to_pay >= 15:
    print("Reward: a free biscuit")
else:
    print("No biscuit this time")
```

<!-- output: examples/ai_biscuit_fixed.expected -->
```output
Reward: a free biscuit
```

Later, Asha asked the AI to make her reward rules easier to read. It suggested checking the biscuit rule first, "because it is the most common reward". She tested the idea with a large amount, 60.0, before she changed anything:

```python
# file: examples/ai_reward_order.py
to_pay = 60.0
if to_pay >= 15:
    print("Reward: a free biscuit")
elif to_pay >= 50:
    print("Reward: a free cake")
else:
    print("Reward: none this time")
```

<!-- output: examples/ai_reward_order.expected -->
```output
Reward: a free biscuit
```

A customer who pays 60 should get a cake. But 60 is also 15 or more, so line 3 is `True` first and Python never checks line 5. Asha kept her order, with the biggest amount first. Test every suggestion with the same edge cases you used before.

## Common mistakes

**Mistake 1: one `=` in a condition.** One `=` gives a name a value. A condition needs `==`.

```python
# file: examples/err01_single_equals.py
member = "yes"
if member = "yes":
    print("Member discount: 10%")
```

<!-- error: examples/err01_single_equals.expected_error -->
```output
  File "err01_single_equals.py", line 3
    if member = "yes":
       ^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Fix: write `if member == "yes":`. The error message suggests `==`. (`:=` is a feature this course does not use.)

**Mistake 2: a missing colon.** Every `if`, `elif` and `else` line ends with a colon.

```python
# file: examples/err02_colon.py
to_pay = 18.9
if to_pay >= 15
    print("Reward: a free biscuit")
```

<!-- error: examples/err02_colon.expected_error -->
```output
  File "err02_colon.py", line 3
    if to_pay >= 15
                   ^
SyntaxError: expected ':'
```

Fix: add the colon at the end of line 3.

**Mistake 3: a block that is not indented.** Python uses indentation to see which lines belong to the block.

```python
# file: examples/err03_indent.py
to_pay = 18.9
if to_pay >= 15:
print("Reward: a free biscuit")
```

<!-- error: examples/err03_indent.expected_error -->
```output
  File "err03_indent.py", line 4
    print("Reward: a free biscuit")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 3
```

Fix: indent line 4 by 4 spaces. Most code editors do this for you when you press Enter after the colon.

**Mistake 4: comparing text with different capital letters.** This mistake gives no error at all.

```python
# file: examples/ex08_case.py
answer = "Yes"
if answer == "yes":
    print("Member discount: 10%")
else:
    print("No discount")
```

<!-- output: examples/ex08_case.expected -->
```output
No discount
```

`"Yes"` and `"yes"` are different strings, so a member gets no discount. Fix: compare `answer.strip().lower() == "yes"`, as in Step 6.

## Think beyond

1. Asha wants the free biscuit only for members whose amount to pay is 15 or more. Which operator joins the two conditions? Write the condition, then test it with a member who pays 12 and a non-member who pays 20.
2. Some customers type `y` instead of `yes`. How could one condition accept both answers? Predict which edge cases still fail, then test them.

## Recap

- A condition works out to `True` or `False`, the two values of the type `bool`.
- `==` asks whether two values are equal; one `=` gives a name a value.
- `if` runs its indented block only when its condition is `True`. `else` runs when it is `False`.
- Python runs only the first `elif` block whose condition is `True`, so the order of the conditions matters.
- `and`, `or` and `not` combine conditions. Compare text after `.strip().lower()`.
- Ask AI for edge cases, such as boundary values, and run every one.

You earned **100 XP** and the **Decision Maker** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 7, you will use `while` loops to ask a question again and again until the answer is valid.
