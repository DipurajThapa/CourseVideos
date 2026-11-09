# Chapter 2: Values and Variables: Giving Data a Name

> Quest: store data in well-named variables, calculate with them and predict each result before you run the code. Reward: 100 XP and the **Name Keeper** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write variables with clear names and give them values with `=`.
- Explain the four basic types `int`, `float`, `str` and `bool`, and check a type with `type()`.
- Calculate with the operators `+`, `-`, `*`, `/`, `//`, `%` and `**`.
- Predict the output of a short program before you run it, then check your prediction.
- Fix the errors that beginners meet most often with variables.

## Why this matters

In Chapter 1, the cafe receipt typed each price twice: once in the item line and once in the total. If the price of tea changes, you must find and change every copy. If you miss one, the receipt is wrong.

A **variable** solves this problem. A variable is a name that refers to a value. You store the price once, under a name such as `tea_price`, and use that name everywhere. Change the value in one place, and every calculation uses the new value.

Every real program works this way. A shopping app keeps the items in your basket. A game keeps your score. A banking app keeps your balance. Each of these values has a name inside the program.

## The idea

A **value** is a single piece of data, such as `3`, `3.5` or `"Tea"`. Every value has a **type**. The type tells Python what kind of data it is and what you can do with it. Here are the four basic types:

| Type | Name | Example values | Use it for |
|---|---|---|---|
| `int` | integer | `3`, `0`, `-12` | Whole numbers: counts, ages, scores |
| `float` | floating-point number | `3.5`, `0.1`, `-2.0` | Numbers with a decimal point: prices, distances |
| `str` | string | `"Tea"`, `"Asha"`, `"3"` | Text, always inside quotation marks |
| `bool` | Boolean | `True`, `False` | Yes or no facts: is a member, is paid |

**Assignment** is the action that connects a name to a value. You write the name, then `=`, then the value:

```text
   name         value
 tea_price  =    3
     ^           |
     +-----------+
  Python works out the right side first,
  then connects the name on the left to it.
```

Read `=` as "now refers to", not as "is equal to". The line `tea_price = 3` means "the name `tea_price` now refers to the value `3`".

Think of a variable as a name label that you stick on a value. You can move the label to a new value at any time. The comparison stops working at one point: two labels can point to the same value, and moving one label does not move the other.

## Build it step by step

**Step 1: Create your first variables.** Make a file called `ex01_first_variables.py`:

```python
# file: examples/ex01_first_variables.py
customer = "Asha"
tea_price = 3
print(customer)
print("Tea costs", tea_price)
print("Two teas cost", tea_price * 2)
```

<!-- output: examples/ex01_first_variables.expected -->
```output
Asha
Tea costs 3
Two teas cost 6
```

The name `customer` has no quotation marks in `print()`, so Python prints its value, `Asha`, and not the word "customer".

Good names make code easy to read. Follow these rules from the Python style guide, called PEP 8:

- Use lowercase letters, and join words with an underscore: `tea_price`, not `TeaPrice` or `tp`.
- A name can contain letters, digits and underscores, but it cannot start with a digit.
- Capital letters matter: `price` and `Price` are two different names.
- Do not use the words Python reserves for itself, such as `True`, `None` or `class`.

**Step 2: Check the type of a value.** The `type()` function tells you the type of any value.

```python
# file: examples/ex02_types.py
cups = 2
price = 3.5
item = "Tea"
is_member = True
print(cups, type(cups))
print(price, type(price))
print(item, type(item))
print(is_member, type(is_member))
```

<!-- output: examples/ex02_types.expected -->
```output
2 <class 'int'>
3.5 <class 'float'>
Tea <class 'str'>
True <class 'bool'>
```

Python chose each type from the way you wrote the value. A decimal point makes a `float`, and quotation marks make a `str`. `True` and `False` need a capital first letter.

**Step 3: Calculate with operators.** An **operator** is a symbol that does a calculation. Seventeen biscuits are shared between five friends. Predict each line before you run it.

```python
# file: examples/ex03_arithmetic.py
biscuits = 17
friends = 5
print("Add:", biscuits + friends)
print("Subtract:", biscuits - friends)
print("Multiply:", biscuits * friends)
print("Divide:", biscuits / friends)
print("Floor divide:", biscuits // friends)
print("Remainder:", biscuits % friends)
print("Power:", friends ** 2)
```

<!-- output: examples/ex03_arithmetic.expected -->
```output
Add: 22
Subtract: 12
Multiply: 85
Divide: 3.4
Floor divide: 3
Remainder: 2
Power: 25
```

Three operators often surprise beginners:

| Operator | Name | Result for 17 and 5 | Meaning |
|---|---|---|---|
| `/` | division | `3.4` | The exact answer. It is always a `float`. |
| `//` | floor division | `3` | Each friend gets 3 whole biscuits. |
| `%` | remainder | `2` | 2 biscuits are left over. |

`**` raises a number to a power, so `5 ** 2` is 5 times 5.

**Step 4: Change a variable.** A variable can get a new value. Python works out the right side first, using the current value, then moves the name to the result.

```python
# file: examples/ex04_reassign.py
points = 10
print("Start:", points)
points = points + 5
print("After a quiz:", points)
points = points * 2
print("After the bonus:", points)
```

<!-- output: examples/ex04_reassign.expected -->
```output
Start: 10
After a quiz: 15
After the bonus: 30
```

In mathematics, `points = points + 5` would be impossible. In Python, it means "take the current value of `points`, add 5, and give `points` the new value".

**Step 5: Know the order of operations.** Python follows the same order as mathematics. It calculates `**` first, then `*`, `/`, `//` and `%`, and then `+` and `-`. Brackets change the order.

```python
# file: examples/ex05_order.py
print(2 + 3 * 4)
print((2 + 3) * 4)
print(10 - 4 / 2)
print(0.1 + 0.1 + 0.1)
print(round(0.1 + 0.1 + 0.1, 2))
```

<!-- output: examples/ex05_order.expected -->
```output
14
20
8.0
0.30000000000000004
0.3
```

Line 2 multiplies first, so the result is 14. Line 3 adds first because of the brackets. Line 5 shows that a `float` is not always exact. Computers store decimal numbers in binary, so some values, such as 0.1, are stored with a tiny error. The `round()` function rounds a number to the number of decimal places you give it.

## See the outcome

Here is the cafe receipt from Chapter 1, rebuilt with variables. Members get a 10 percent discount. Every price appears only once.

```python
# file: examples/ex06_cafe_bill.py
customer = "Asha"
tea_price = 3.5
sandwich_price = 6
tea_count = 2
is_member = True
member_discount = 0.1

tea_total = tea_price * tea_count
bill = tea_total + sandwich_price
discount = bill * member_discount
to_pay = bill - discount

print("Customer:", customer)
print("Teas:", tea_count, "x", tea_price, "=", tea_total)
print("Sandwich:", sandwich_price)
print("Bill:", bill)
print("Member:", is_member)
print("Discount:", discount)
print("To pay:", to_pay)
```

<!-- output: examples/ex06_cafe_bill.expected -->
```output
Customer: Asha
Teas: 2 x 3.5 = 7.0
Sandwich: 6
Bill: 13.0
Member: True
Discount: 1.3
To pay: 11.7
```

Change `tea_price` to `4` and run it again. Every line that depends on the tea price updates by itself. Notice that `tea_total` is `7.0`, a `float`, because one of its parts was a `float`. For now, the program applies the discount every time. In Chapter 6, you will use `is_member` to decide whether to apply it.

## Work with AI

The AI skill for this chapter is prediction. Before you run a program, ask an AI assistant such as ChatGPT or Claude to predict its output. Write down your own prediction too. Then run the code. The real output is the only answer that counts.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe a calculation in words and ask AI to list the variables it needs, with a name and type for each. |
| Write | Write the program yourself. Then ask AI to predict its output line by line, and compare with a real run. |
| Generate | Ask for a short program with fixed variable names and an exact expected output. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Test | Ask for three sets of values to try, including zero and a decimal. Predict, then run each one. |
| Improve | Ask AI to suggest clearer variable names, then decide which suggestions help a reader. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** A learner asked an AI assistant: "Write Python code that finds the average of the scores 80, 90 and 100. Tell me what it prints." The AI answered with this code and said it would print `Average: 90.0`.

```python
# file: examples/ai_average_flawed.py
score_1 = 80
score_2 = 90
score_3 = 100
average = score_1 + score_2 + score_3 / 3
print("Average:", average)
```

The learner ran it. The real output did not match the prediction:

<!-- output: examples/ai_average_flawed.expected -->
```output
Average: 203.33333333333334
```

The AI forgot the order of operations. Python divided only `score_3` by 3, then added the other two scores. Both the code and the prediction were wrong, and the AI sounded sure about both. Brackets fix the order:

```python
# file: examples/ai_average_fixed.py
score_1 = 80
score_2 = 90
score_3 = 100
average = (score_1 + score_2 + score_3) / 3
print("Average:", average)
```

<!-- output: examples/ai_average_fixed.expected -->
```output
Average: 90.0
```

A quick check would also catch this flaw. The average of three scores must be between the lowest and the highest score. A result of 203 is impossible.

## Common mistakes

**Mistake 1: a typing error in a variable name.** Python only knows the names you created.

```python
# file: examples/err01_name_typo.py
tea_price = 3
print("Price:", tea_price)
print("Price:", tea_prise)
```

<!-- error: examples/err01_name_typo.expected_error -->
```output
Price: 3
Traceback (most recent call last):
  File "err01_name_typo.py", line 4, in <module>
    print("Price:", tea_prise)
                    ^^^^^^^^^
NameError: name 'tea_prise' is not defined. Did you mean: 'tea_price'?
```

Fix: spell the name exactly as you created it, `tea_price`. You also get this error if you use a name on a line above the line that creates it.

**Mistake 2: a number stored as text.** `"3"` with quotation marks is a `str`, not an `int`. Python will not add text and a number.

```python
# file: examples/err02_text_number.py
price = "3"
total = price + 4
print(total)
```

<!-- error: examples/err02_text_number.expected_error -->
```output
TypeError: can only concatenate str (not "int") to str
```

Fix: remove the quotation marks, `price = 3`. Sometimes this mistake gives no error at all, which is worse:

```python
# file: examples/ex07_text_times.py
price = "3"
print(price * 2)
price = 3
print(price * 2)
```

<!-- output: examples/ex07_text_times.expected -->
```output
33
6
```

Multiplying a string by 2 repeats the text, so you get `33` instead of `6`. If a calculation looks strange, check the type with `type()`.

**Mistake 3: a name that starts with a digit.**

```python
# file: examples/err03_digit_first.py
2nd_place = "Omar"
print(2nd_place)
```

<!-- error: examples/err03_digit_first.expected_error -->
```output
SyntaxError: invalid decimal literal
```

Fix: start the name with a letter, such as `second_place`. Python reads `2` as the start of a number and does not understand the letters after it.

**Mistake 4: the name and value on the wrong sides.**

```python
# file: examples/err04_reversed.py
10 = points
print(points)
```

<!-- error: examples/err04_reversed.expected_error -->
```output
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```

Fix: the name always goes on the left, `points = 10`. A **literal** is a value written directly in the code, such as `10`. A literal cannot be given a new value.

## Think beyond

1. Four friends share a bill of 50. How could you use `//` and `%` to find how much each person pays in whole units, and how much is left over? Write it and run it.
2. You have `a = 5` and `b = 8`, and you want to swap them, so `a` is 8 and `b` is 5. Why does `a = b` followed by `b = a` not work? Predict the result, test it, and then find a fix that uses a third variable.

## Recap

- A value is a piece of data, and every value has a type: `int`, `float`, `str` or `bool`.
- A variable is a name that refers to a value. `=` connects the name on the left to the value on the right.
- Python works out the right side of `=` first, so `points = points + 5` is valid.
- `/` always gives a `float`. `//` gives the whole part of a division, and `%` gives the remainder.
- Brackets control the order of operations. A `float` result can be slightly inexact, and `round()` helps.
- Ask AI to predict output, make your own prediction, and let the real run decide.

You earned **100 XP** and the **Name Keeper** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 3, you will work with text: you will join strings and build clear messages from your variables with f-strings.
