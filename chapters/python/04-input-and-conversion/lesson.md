# Chapter 4: Talking Back: Input and Type Conversion

> Quest: write programs that ask questions, turn the answers into numbers and calculate with them. Reward: 100 XP and the **Listener** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Ask the user a question with `input()` and store the answer in a variable.
- Explain why every answer from `input()` is a string, and check its type with `type()`.
- Convert text to numbers with `int()` and `float()`, and numbers to text with `str()`.
- Write a program that asks questions, converts the answers and calculates a result.
- Read the `TypeError` and `ValueError` messages that conversion causes, and fix them.

## Why this matters

In Chapter 3, Asha's receipt looked professional. But every customer got the same order: two teas and a sandwich. The values were fixed in the code, so a new order meant editing the program.

Real programs react to the person who uses them. A cash machine asks for an amount. A booking site asks for a date and the number of guests. A game asks for your name. In each case, the program asks a question, waits for the answer and then uses it.

## The idea

The function `input()` shows a question, waits for the user to type an answer and press Enter, and gives back what they typed. The answer is always a string, even when the user types digits.

```text
  input("How many teas? ")
        |
        v
  The terminal shows:  How many teas? _
  The user types 3 and presses Enter
        |
        v
  input() gives back the string "3", not the number 3
```

To calculate with an answer, you **convert** it: you make a new value of another type from it. Python has one conversion function for each type you know:

| Function | Gives you | Example | Result |
|---|---|---|---|
| `int()` | a whole number | `int("3")` | `3` |
| `float()` | a decimal number | `float("4.25")` | `4.25` |
| `str()` | a string | `str(3)` | `"3"` |

Think of `input()` as a waiter who writes every order on a paper slip. The kitchen cannot add up slips; it needs numbers. Conversion reads the slip and writes the number. Unlike a person, a conversion function cannot guess: if the slip says "two" instead of "2", it stops with an error.

## Build it step by step

**Step 1: Ask a question.** The text inside `input()` is the **prompt**: the question the user sees. End it with a space, so the answer does not touch the question.

```python
# file: examples/ex01_input.py
name = input("What is your name? ")
print(f"Hello, {name}!")
print(f"Welcome to the Corner Cafe, {name}.")
```

<!-- output: examples/ex01_input.expected -->
```output
What is your name? Asha
Hello, Asha!
Welcome to the Corner Cafe, Asha.
```

In this chapter, the output shows the user's answer after each question, as it appears in the terminal. Here the user typed `Asha`. The program waits at line 2 until the user presses Enter.

**Step 2: See that every answer is text.** The user types `3`, and the program checks the type of the answer.

```python
# file: examples/ex02_text_answer.py
answer = input("How many teas? ")
print(answer, type(answer))
print(answer * 2)
```

<!-- output: examples/ex02_text_answer.expected -->
```output
How many teas? 3
3 <class 'str'>
33
```

The answer is the string `"3"`. Multiplying a string by 2 repeats it, so line 4 prints `33`, the same silent problem you met in Chapter 2.

**Step 3: Convert an answer to a whole number.** Put `input()` inside `int()`. Python works from the inside out: first `input()` gives back the string, then `int()` turns it into a whole number.

```python
# file: examples/ex03_int.py
tea_count = int(input("How many teas? "))
tea_price = 3.5
print(tea_count, type(tea_count))
print(f"{tea_count} teas cost {tea_count * tea_price:.2f}")
```

<!-- output: examples/ex03_int.expected -->
```output
How many teas? 3
3 <class 'int'>
3 teas cost 10.50
```

Now `tea_count` is the number 3, so the multiplication calculates instead of repeating text.

**Step 4: Convert an answer to a decimal number.** Use `float()` when the answer can have a decimal point, such as a price.

```python
# file: examples/ex04_float.py
cake_price = float(input("Price of one cake? "))
cake_count = int(input("How many cakes? "))
total = cake_price * cake_count
print(f"{cake_count} cakes cost {total:.2f}")
```

<!-- output: examples/ex04_float.expected -->
```output
Price of one cake? 4.25
How many cakes? 2
2 cakes cost 8.50
```

The program asks two questions, one after the other. Use `int()` for counts and `float()` for amounts of money.

**Step 5: Know what each conversion accepts.** The conversion functions also work on values you write in the code.

```python
# file: examples/ex05_conversions.py
print(int("12") + 1)
print(float("2.5") * 2)
print(float("3"))
print(int(3.9))
print(int(" 5 "))
print(str(4) + " teas")
```

<!-- output: examples/ex05_conversions.expected -->
```output
13
5.0
3.0
3
5
4 teas
```

| Line | What happened |
|---|---|
| 2 | `int("12")` made the number 12, so adding 1 gives 13. |
| 4 | `float()` accepts text without a decimal point and adds `.0`. |
| 5 | `int()` on a decimal number cuts off the part after the point. It does not round, so 3.9 becomes 3. |
| 6 | `int()` ignores spaces at the start and the end of the text. |
| 7 | `str()` turns a number into text, so `+` can join it to another string. |

Be careful with one difference. `int()` accepts the number 3.9, but not the text `"3.9"`. Run this example to see it.

```python
# file: examples/ex05_int_text.py
print(int(3.9))
print(int("3.9"))
```

<!-- error: examples/ex05_int_text.expected_error -->
```output
3
Traceback (most recent call last):
  File "ex05_int_text.py", line 3, in <module>
    print(int("3.9"))
          ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '3.9'
```

Text with a decimal point is not a whole number, so `int()` stops with a `ValueError` instead of cutting off the decimals. Use `float()` for that text.

## See the outcome

Here is Asha's receipt from Chapter 3. Now it asks the customer for the order. This time, the user typed `  omar ` with extra spaces, then `3` teas and `2` sandwiches.

```python
# file: examples/ex06_order.py
customer = input("Your name: ")
tea_count = int(input("How many teas? "))
sandwich_count = int(input("How many sandwiches? "))
tea_price = 3.5
sandwich_price = 6

name = customer.strip().title()
tea_total = tea_price * tea_count
sandwich_total = sandwich_price * sandwich_count
to_pay = tea_total + sandwich_total
tea_label = f"Tea x {tea_count}"
sandwich_label = f"Sandwich x {sandwich_count}"
line = "-" * 24

print(f"{' CORNER CAFE ':=^24}")
print(f"Customer: {name}")
print(line)
print(f"{tea_label:<16}{tea_total:>8.2f}")
print(f"{sandwich_label:<16}{sandwich_total:>8.2f}")
print(line)
print(f"{'TO PAY':<16}{to_pay:>8.2f}")
```

<!-- output: examples/ex06_order.expected -->
```output
Your name:   omar
How many teas? 3
How many sandwiches? 2
===== CORNER CAFE ======
Customer: Omar
------------------------
Tea x 3            10.50
Sandwich x 2       12.00
------------------------
TO PAY             22.50
```

To keep the program short, the member discount from Chapter 3 is left out. Lines 2 to 4 ask the three questions. The name stays text, and the two counts become whole numbers. Line 8 cleans the name with `strip()` and `title()` from Chapter 3. Lines 9 to 14 calculate and build the labels, and lines 16 to 22 print the receipt. Run it again with a different order, and the receipt changes without any change to the code.

## Work with AI

The AI skill for this chapter is debugging with the exact error. When a program stops, copy the full error message and the code into your prompt. Ask the AI to explain the cause first, and only then to show the smallest fix.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe the questions your program asks and ask which type each answer needs. |
| Write | Write a line with `input()` inside a conversion, then ask AI to explain the order in which Python works it out. |
| Generate | Ask for code with fixed names, the exact prompt text and the exact output for one typed answer. |
| Test | Ask for answers to try, such as a whole number, a decimal and a word, with the result each one should give. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask for a simpler version, then test it with the same answers before you accept it. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha wanted her program to ask how much the customer paid and print the change. She asked an AI assistant: "The bill is 22.5. Write Python code that asks 'Amount paid? ' and prints the change with two decimal places. If I type 30, tell me exactly what it prints." The AI said the code would print `Change: 7.50`.

```python
# file: examples/ai_change_flawed.py
to_pay = 22.5
paid = input("Amount paid? ")
change = paid - to_pay
print(f"Change: {change:.2f}")
```

Asha typed `30`. The program stopped with an error:

<!-- error: examples/ai_change_flawed.expected_error -->
```output
Amount paid? 30
Traceback (most recent call last):
  File "ai_change_flawed.py", line 4, in <module>
    change = paid - to_pay
             ~~~~~^~~~~~~~
TypeError: unsupported operand type(s) for -: 'str' and 'float'
```

She pasted the code and the full error into a new prompt, and asked for the cause before the fix. The cause: `input()` gives back a string, and Python cannot subtract a decimal number from text. The AI had forgotten the conversion, and it sounded sure. The fix is `float()` around `input()`:

```python
# file: examples/ai_change_fixed.py
to_pay = 22.5
paid = float(input("Amount paid? "))
change = paid - to_pay
print(f"Change: {change:.2f}")
```

<!-- output: examples/ai_change_fixed.expected -->
```output
Amount paid? 30
Change: 7.50
```

Later, Asha asked the AI to simplify her program. It suggested `int()` instead of `float()`, "because customers usually pay with whole notes". She tested the idea with an amount that has a decimal point before she changed anything:

```python
# file: examples/ai_change_int.py
to_pay = 22.5
paid = int(input("Amount paid? "))
change = paid - to_pay
print(f"Change: {change:.2f}")
```

<!-- error: examples/ai_change_int.expected_error -->
```output
Amount paid? 25.50
Traceback (most recent call last):
  File "ai_change_int.py", line 3, in <module>
    paid = int(input("Amount paid? "))
ValueError: invalid literal for int() with base 10: '25.50'
```

`int()` only accepts text that looks like a whole number. Asha kept `float()`. Test a suggestion with more than one kind of answer before you accept it.

## Common mistakes

**Mistake 1: calculating with an answer you did not convert.** The answer from `input()` is a string.

```python
# file: examples/err01_add_text.py
tea_count = input("How many teas? ")
total = tea_count + 1
print(total)
```

<!-- error: examples/err01_add_text.expected_error -->
```output
How many teas? 3
Traceback (most recent call last):
  File "err01_add_text.py", line 3, in <module>
    total = tea_count + 1
            ~~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

Fix: convert the answer when you read it, `tea_count = int(input("How many teas? "))`.

**Mistake 2: `int()` for an answer with a decimal point.**

```python
# file: examples/err02_int_decimal.py
price = int(input("Price of a cake? "))
print(price * 2)
```

<!-- error: examples/err02_int_decimal.expected_error -->
```output
Price of a cake? 4.25
Traceback (most recent call last):
  File "err02_int_decimal.py", line 2, in <module>
    price = int(input("Price of a cake? "))
ValueError: invalid literal for int() with base 10: '4.25'
```

Fix: use `float()` for prices and other amounts that can have a decimal point. A **literal** here means the text Python tried to read as a number.

**Mistake 3: an answer that is not a number at all.** The user typed a word.

```python
# file: examples/err03_word.py
tea_count = int(input("How many teas? "))
print(tea_count * 3.5)
```

<!-- error: examples/err03_word.expected_error -->
```output
How many teas? two
Traceback (most recent call last):
  File "err03_word.py", line 2, in <module>
    tea_count = int(input("How many teas? "))
ValueError: invalid literal for int() with base 10: 'two'
```

Fix: for now, tell the user what to type in the prompt, such as `"How many teas? (a number) "`. In later chapters, you will learn to check an answer before you convert it.

**Mistake 4: a missing closing bracket.** A line with `input()` inside `int()` needs two closing brackets.

```python
# file: examples/err04_bracket.py
tea_count = int(input("How many teas? ")
print(tea_count * 3.5)
```

<!-- error: examples/err04_bracket.expected_error -->
```output
  File "err04_bracket.py", line 2
    tea_count = int(input("How many teas? ")
                   ^
SyntaxError: '(' was never closed
```

Fix: count the brackets. Every opening bracket needs its own closing bracket: `int(input("How many teas? "))`.

## Think beyond

1. A customer types `2.0` when the program asks how many teas. What happens with `int()`? How could you combine `float()` and `int()` to accept it? Predict, then test.
2. Asha wants the program to ask for the price of tea too, instead of fixing it at 3.5. Which line would you change, and which conversion would you use?

## Recap

- `input()` shows a prompt, waits for the user and gives back the answer as a string.
- `int()` makes a whole number, `float()` makes a decimal number and `str()` makes text.
- Python works out `int(input(...))` from the inside out.
- `int()` cuts off decimals instead of rounding, and it cannot read text such as `"4.25"` or `"two"`.
- Give AI the code and the full error, and ask for the cause before the fix.

You earned **100 XP** and the **Listener** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 5, the first boss level, you will combine everything from Chapters 1 to 4 to build a bill splitter that shares a cafe bill between friends.
