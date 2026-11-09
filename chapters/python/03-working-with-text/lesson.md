# Chapter 3: Working with Text: Strings and f-strings

> Quest: build clear, neatly lined-up messages from your variables, and clean up text before you show it. Reward: 100 XP and the **Wordsmith** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Join strings with `+` and build messages from variables with f-strings.
- Show a number with exactly two decimal places, such as `11.70`.
- Line up text and numbers in columns with a width and an alignment.
- Clean and change text with the string methods `strip()`, `title()`, `upper()`, `lower()` and `replace()`.
- Read one character of a string with an index, and fix the errors beginners meet with text.

## Why this matters

In Chapter 2, Asha's cafe bill worked, but it looked untidy. It printed `Teas: 2 x 3.5 = 7.0` and `To pay: 11.7`. A real receipt shows `11.70`, and its prices sit in one straight column.

Almost every program shows text to people: a receipt, a message, a menu or a report. The data inside can be correct, but if the text is messy, people do not trust it. Good text handling makes your output clear and professional.

## The idea

A **string** is a sequence of characters, such as letters, digits, spaces and symbols. Each character has a position, called its **index**. The first index is 0, not 1.

```text
 text:     C   A   F   E   -   1   0   2   4
 index:    0   1   2   3   4   5   6   7   8
 from end: -9  -8  -7  -6  -5  -4  -3  -2  -1
```

You build a message in one of two ways:

| Way | Example | Good for |
|---|---|---|
| Join with `+` | `"Hello, " + name` | Joining two or three strings |
| f-string | `f"Hello, {name}"` | Mixing text with numbers and formatting them |

An **f-string** is a string with the letter `f` in front of its opening quotation mark. Inside it, anything in curly brackets `{ }` is worked out, and its value goes into the text. Think of an f-string as a form with blank boxes. Python fills each box with a value. The comparison stops at one point: a box can also say how to show the value, for example with two decimal places.

A string cannot be changed after it is made. Methods such as `upper()` do not change a string. They give you a new string, and the original stays the same.

## Build it step by step

**Step 1: Join strings with `+`.** The `+` operator joins two strings into one. This is called **concatenation**.

```python
# file: examples/ex01_join.py
first = "Corner"
second = "Cafe"
print(first + " " + second)
print("Welcome to the " + first + " " + second + "!")
```

<!-- output: examples/ex01_join.expected -->
```output
Corner Cafe
Welcome to the Corner Cafe!
```

The `+` adds no space by itself, so you add a space string, `" "`, wherever you want one.

**Step 2: Build a message with an f-string.** Put `f` before the opening quotation mark, and put names or calculations inside curly brackets.

```python
# file: examples/ex02_fstring.py
customer = "Asha"
tea_count = 2
tea_price = 3.5
print(f"Hello, {customer}!")
print(f"{tea_count} teas cost {tea_count * tea_price}")
```

<!-- output: examples/ex02_fstring.expected -->
```output
Hello, Asha!
2 teas cost 7.0
```

The f-string mixes text and numbers without `+`. Python works out `tea_count * tea_price` inside the brackets, so the line shows `7.0`.

**Step 3: Show exactly two decimal places.** After the value inside the brackets, add a colon and a **format specification**: a short code that says how to show the value. `.2f` means "a decimal number with exactly two digits after the point".

```python
# file: examples/ex03_decimals.py
to_pay = 11.7
discount = 1.3
print(f"To pay: {to_pay}")
print(f"To pay: {to_pay:.2f}")
print(f"Discount: {discount:.2f}")
print(f"One third: {10 / 3:.2f}")
```

<!-- output: examples/ex03_decimals.expected -->
```output
To pay: 11.7
To pay: 11.70
Discount: 1.30
One third: 3.33
```

`.2f` adds a zero when it is missing and rounds when there are more digits. The value in the variable does not change; only the way it is shown changes.

**Step 4: Line up columns.** A number in the format specification sets the **width**: the smallest number of characters the value takes. An arrow sets the **alignment**: `<` for left, `>` for right and `^` for centre. Inside the brackets you can also write text in single quotation marks.

```python
# file: examples/ex04_columns.py
tea_price = 3.5
sandwich_price = 6
print(f"{'Item':<10}{'Price':>8}")
print(f"{'Tea':<10}{tea_price:>8.2f}")
print(f"{'Sandwich':<10}{sandwich_price:>8.2f}")
print(f"{' MENU ':*^18}")
```

<!-- output: examples/ex04_columns.expected -->
```output
Item         Price
Tea           3.50
Sandwich      6.00
****** MENU ******
```

Every name takes 10 characters and every price takes 8, so the prices line up on the right. On the last line, the `*` before `^` is a **fill character**: it fills the empty space instead of spaces.

**Step 5: Clean and change text with methods.** A **method** is a function that belongs to a value. You call it with a dot after the value: `name.upper()`.

```python
# file: examples/ex05_methods.py
typed_name = "  asha khan  "
name = typed_name.strip()
print(name)
print(name.title())
print(name.upper())
print(name.replace("khan", "K."))
print(len(typed_name), len(name))
```

<!-- output: examples/ex05_methods.expected -->
```output
asha khan
Asha Khan
ASHA KHAN
asha K.
13 9
```

| Method | What it gives you |
|---|---|
| `strip()` | The text without spaces at the start and the end |
| `title()` | Each word with a capital first letter |
| `upper()` and `lower()` | All capital letters, or all small letters |
| `replace(old, new)` | The text with every `old` part changed to `new` |

The function `len()` counts the characters in a string, spaces included. `typed_name` still has 13 characters, because `strip()` made a new string and did not change the old one.

**Step 6: Read one character with an index.** Write the index in square brackets after the string. A negative index counts from the end, so `-1` is the last character.

```python
# file: examples/ex06_index.py
order_code = "CAFE-1024-T4"
print(order_code[0])
print(order_code[5])
print(order_code[-1])
print(order_code[-2])
print(len(order_code))
```

<!-- output: examples/ex06_index.expected -->
```output
C
1
4
T
12
```

The code has 12 characters, so its indexes go from 0 to 11. Index 5 is the sixth character, the `1` after the hyphen.

## See the outcome

Here is Asha's receipt from Chapter 2, rebuilt with f-strings. It cleans the customer's name, shows every amount with two decimal places and lines up the prices in one column.

```python
# file: examples/ex07_receipt.py
customer = "  asha  "
tea_price = 3.5
tea_count = 2
sandwich_price = 6
member_discount = 0.1

tea_total = tea_price * tea_count
bill = tea_total + sandwich_price
discount = bill * member_discount
to_pay = bill - discount
name = customer.strip().title()
tea_label = f"Tea x {tea_count}"
line = "-" * 24

print(f"{' CORNER CAFE ':=^24}")
print(f"Customer: {name}")
print(line)
print(f"{tea_label:<16}{tea_total:>8.2f}")
print(f"{'Sandwich':<16}{sandwich_price:>8.2f}")
print(f"{'Member discount':<16}{-discount:>8.2f}")
print(line)
print(f"{'TO PAY':<16}{to_pay:>8.2f}")
```

<!-- output: examples/ex07_receipt.expected -->
```output
===== CORNER CAFE ======
Customer: Asha
------------------------
Tea x 2             7.00
Sandwich            6.00
Member discount    -1.30
------------------------
TO PAY             11.70
```

Every line is 24 characters wide: 16 for the label and 8 for the amount. Line 12 calls two methods in a row: `strip()` first, then `title()` on the result. Line 14 repeats the string `"-"` 24 times, as you saw with text in Chapter 2.

## Work with AI

The AI skill for this chapter is a precise prompt. When you want text in an exact shape, show the AI the exact output you want, character by character. Then compare the AI's result with your target.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Show the exact line you want and ask which widths, alignments and format codes it needs. |
| Write | Write the f-string yourself, then ask AI to predict its exact output, including spaces. |
| Generate | Ask for code with fixed names and paste the exact target output into the prompt. |
| Test | Ask for values that could break the layout, such as a long name or a large price, and run them. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask AI for a shorter or clearer version, then test it with new values before you accept it. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha wanted one receipt line: the item name in 16 characters on the left and the price in 8 characters on the right. She asked an AI assistant: "Write Python code that prints the item Sandwich and the price 6 as one receipt line. The name takes 16 characters on the left, and the price takes 8 characters on the right with two decimal places. Tell me exactly what it prints." The AI said the code would print `Sandwich            6.00`.

```python
# file: examples/ai_line_flawed.py
item = "Sandwich"
price = 6
print("{item:<16}{price:>8.2f}")
```

Asha ran it. The real output did not match the prediction:

<!-- output: examples/ai_line_flawed.expected -->
```output
{item:<16}{price:>8.2f}
```

The AI forgot the `f` before the opening quotation mark. Without it, the curly brackets are ordinary characters, so Python printed them as text. There was no error message, so only a comparison with the target output catches this flaw. One letter fixes it:

```python
# file: examples/ai_line_fixed.py
item = "Sandwich"
price = 6
print(f"{item:<16}{price:>8.2f}")
```

<!-- output: examples/ai_line_fixed.expected -->
```output
Sandwich            6.00
```

Later, Asha asked the AI to make her code shorter. It suggested `:.2` instead of `:.2f`, "because both mean two decimal places". She tested the idea with two prices before she changed anything:

```python
# file: examples/ai_short_spec.py
tea_price = 3.5
cake_price = 12.5
print(f"With .2f: {tea_price:.2f} and {cake_price:.2f}")
print(f"With .2: {tea_price:.2} and {cake_price:.2}")
```

<!-- output: examples/ai_short_spec.expected -->
```output
With .2f: 3.50 and 12.50
With .2: 3.5 and 1.2e+01
```

Without the `f`, `.2` means two significant digits in total, not two decimal places. It looked right for 3.5 but turned 12.5 into `1.2e+01`. Asha kept `.2f`. A suggestion that works for one value can fail for another, so test with more than one.

## Common mistakes

**Mistake 1: joining a string and a number with `+`.** `+` only joins strings to strings.

```python
# file: examples/err01_join_number.py
tea_count = 2
print("Teas: " + tea_count)
```

<!-- error: examples/err01_join_number.expected_error -->
```output
Traceback (most recent call last):
  File "err01_join_number.py", line 3, in <module>
    print("Teas: " + tea_count)
          ~~~~~~~~~^~~~~~~~~~~
TypeError: can only concatenate str (not "int") to str
```

Fix: use an f-string, `print(f"Teas: {tea_count}")`. It turns the number into text for you.

**Mistake 2: an index that is too large.** A string with 2 characters has the indexes 0 and 1 only.

```python
# file: examples/err02_index_range.py
table = "T4"
print(table[0])
print(table[2])
```

<!-- error: examples/err02_index_range.expected_error -->
```output
T
Traceback (most recent call last):
  File "err02_index_range.py", line 4, in <module>
    print(table[2])
          ~~~~~^^^
IndexError: string index out of range
```

Fix: the last index is always one less than `len()`. Use `table[1]`, or `table[-1]` for the last character.

**Mistake 3: trying to change one character.** A string cannot be changed after it is made.

```python
# file: examples/err03_change_letter.py
name = "asha"
name[0] = "A"
print(name)
```

<!-- error: examples/err03_change_letter.expected_error -->
```output
Traceback (most recent call last):
  File "err03_change_letter.py", line 3, in <module>
    name[0] = "A"
    ~~~~^^^
TypeError: 'str' object does not support item assignment
```

Fix: make a new string and give it the name, for example `name = name.title()`.

**Mistake 4: a decimal format for text.** `"6"` with quotation marks is a string, and `.2f` only works for numbers.

```python
# file: examples/err04_format_text.py
price = "6"
print(f"Price: {price:.2f}")
```

<!-- error: examples/err04_format_text.expected_error -->
```output
Traceback (most recent call last):
  File "err04_format_text.py", line 3, in <module>
    print(f"Price: {price:.2f}")
                   ^^^^^^^^^^^
ValueError: Unknown format code 'f' for object of type 'str'
```

Fix: store the price as a number, `price = 6`. In Chapter 4, you will learn to turn text into a number with `float()`.

## Think beyond

1. Asha wants to show only the first letter of a customer's name, as a capital, on a table card. Which index and which method would you combine? Write it and test it with `"omar"`.
2. A new receipt printer is 32 characters wide. Which numbers in `ex07_receipt.py` would you change so that the columns still line up? Predict the new output, then test it.

## Recap

- A string is a sequence of characters. Indexes start at 0, and `-1` is the last character.
- `+` joins strings. An f-string puts values into text with curly brackets.
- After a colon, `.2f` shows two decimal places, a number sets the width, and `<`, `>` and `^` set the alignment.
- Methods such as `strip()`, `title()`, `upper()` and `replace()` give you a new string. The original never changes.
- Show AI the exact output you want, and test its code with more than one value.

You earned **100 XP** and the **Wordsmith** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 4, your programs will ask the user questions with `input()`, so the receipt can use the customer's own order instead of fixed values.
