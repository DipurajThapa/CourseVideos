# Chapter 16: Functions: Reusable Blocks of Logic

> Quest: turn code you copy again and again into named functions with clear inputs and outputs, and test a function an AI writes for you. Reward: 100 XP and the **Function Forger** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write a function with `def`, call it, and give it inputs with parameters.
- Explain the difference between `return` and `print()`, and recognise `None`.
- Write a docstring that says what a function does.
- Read a traceback that passes through several functions, from the bottom up.
- Write a function specification, ask AI for the code, and test it with your own checks.

## Why this matters

At the end of Chapter 15, Asha's expense tracker printed a summary for one day. To print a summary for three days, she copied the same lines three times. Then she found a mistake in one copy. She had to fix it in three places, and she missed one.

A **function** is a named block of code that you write once and run whenever you need it. You give it a name, such as `day_total`, and call it by that name. Fix a mistake inside the function, and every call gets the fix.

You have used functions since Chapter 1: `print()`, `len()`, `round()` and `input()` are all functions that Python provides. In this chapter, you write your own. Every real program, from a phone app to a website, is built from many small functions.

## The idea

A function is like a recipe card in the cafe kitchen. The card has a name and a list of ingredients. The cook follows the same steps every time, with the ingredients of the day, and hands back one dish.

```text
   def with_tax(price):              <- the name and one parameter
       return round(price * 1.1, 2)  <- the body: indented, runs at each call
                 |
   tea = with_tax(3.5)               <- a call: the argument 3.5 goes in,
                                        the returned value 3.85 comes out
```

The words in this chapter:

| Word | Meaning | Example |
|---|---|---|
| define | Write the function with `def`. Nothing runs yet. | `def with_tax(price):` |
| call | Run the function by its name and brackets. | `with_tax(3.5)` |
| parameter | A name in the `def` line that receives a value. | `price` |
| argument | The value you pass in a call. | `3.5` |
| return value | The value the function hands back to the caller. | `3.85` |

The recipe comparison stops at one point. A cook can taste the dish and adjust it. A function only does exactly what its body says, every time.

## Build it step by step

**Step 1: Define a function and call it.** The `def` line names the function. The indented lines below it are its **body**. Defining a function does not run it. A call runs it.

```python
# file: examples/ex01_welcome.py
def welcome():
    print("Welcome to the Corner Cafe!")
    print("Today's special: carrot cake")

welcome()
welcome()
```

<!-- output: examples/ex01_welcome.expected -->
```output
Welcome to the Corner Cafe!
Today's special: carrot cake
Welcome to the Corner Cafe!
Today's special: carrot cake
```

Each call runs the whole body, so the two lines appear twice. The empty line after the body is not required, but it makes the end of the function easy to see.

**Step 2: Give the function an input.** A **parameter** is a name in the `def` line. When you call the function, the **argument** you pass becomes the value of that parameter.

```python
# file: examples/ex02_greet.py
def greet(name):
    print(f"Hello, {name}! Your tea is ready.")

greet("Omar")
greet("Lina")
```

<!-- output: examples/ex02_greet.expected -->
```output
Hello, Omar! Your tea is ready.
Hello, Lina! Your tea is ready.
```

In the first call, `name` refers to `"Omar"`. In the second call, it refers to `"Lina"`.

**Step 3: Return a value.** The `return` statement ends the function and hands a value back to the line that called it. The caller can store that value, print it or calculate with it.

```python
# file: examples/ex03_with_tax.py
def with_tax(price):
    return round(price * 1.1, 2)

tea = with_tax(3.5)
print(tea)
print(with_tax(4.0))
print(with_tax(2.75) > 3)
```

<!-- output: examples/ex03_with_tax.expected -->
```output
3.85
4.4
True
```

Line 5 stores the returned value in `tea`. Line 7 compares a returned value: `with_tax(2.75)` is 3.03, which is more than 3.

**Step 4: Know the difference between print and return.** `print()` shows a value on the screen. `return` hands a value back to the program. A function without `return` hands back **`None`**, a special value that means "no value".

```python
# file: examples/ex04_print_not_return.py
def tax_print(price):
    print(round(price * 1.1, 2))

result = tax_print(3.5)
print("result is", result)
```

<!-- output: examples/ex04_print_not_return.expected -->
```output
3.85
result is None
```

The function printed 3.85, but it returned nothing, so `result` is `None`. If the caller needs the value, the function must `return` it.

**Step 5: Use several parameters and a docstring.** A function can take several parameters, separated by commas. Arguments fill them in order: the first argument goes to the first parameter. A **docstring** is a string on the first line of the body that says what the function does.

```python
# file: examples/ex05_line_total.py
def line_total(price, count):
    """Return the price of count items, rounded to cents."""
    return round(price * count, 2)

print(line_total(3.5, 2))
print(line_total(2.75, 3))
print(line_total.__doc__)
```

<!-- output: examples/ex05_line_total.expected -->
```output
7.0
8.25
Return the price of count items, rounded to cents.
```

Line 8 prints the docstring. Python keeps it under the name `__doc__`, with two underscores on each side. Code editors and AI assistants read docstrings too.

**Step 6: Call a function from another function, and read a longer traceback.** A function can call another function. `day_total()` calls `with_tax()` for every price.

```python
# file: examples/ex06_calls.py
def with_tax(price):
    return round(price * 1.1, 2)

def day_total(prices):
    total = 0
    for price in prices:
        total += with_tax(price)
    return round(total, 2)

print(day_total([3.5, 4.0, 2.75]))
```

<!-- output: examples/ex06_calls.expected -->
```output
11.28
```

When something goes wrong inside a function, the traceback lists every call on the way, one block per function. Here one price is the text `"4.0"`:

```python
# file: examples/ex07_traceback.py
def with_tax(price):
    return round(price * 1.1, 2)

def day_total(prices):
    total = 0
    for price in prices:
        total += with_tax(price)
    return round(total, 2)

print(day_total([3.5, "4.0"]))
```

<!-- error: examples/ex07_traceback.expected_error -->
```output
Traceback (most recent call last):
  File "ex07_traceback.py", line 11, in <module>
    print(day_total([3.5, "4.0"]))
          ~~~~~~~~~^^^^^^^^^^^^^^
  File "ex07_traceback.py", line 8, in day_total
    total += with_tax(price)
             ~~~~~~~~^^^^^^^
  File "ex07_traceback.py", line 3, in with_tax
    return round(price * 1.1, 2)
                 ~~~~~~~^~~~~
TypeError: can't multiply sequence by non-int of type 'float'
```

Read it from the bottom up, as in Chapter 9. The last line names the error. The block directly above it shows where it happened: line 3, in `with_tax`. Each block above that shows who called it: line 8 in `day_total`, then line 11, the main program. "Most recent call last" means the deepest call is at the bottom. The cause is the text `"4.0"` in the list on line 11.

## See the outcome

Here is the tracker summary from Chapter 15, rebuilt with functions. Each function has one job and a docstring. One line prints the summary for any day.

```python
# file: examples/ex08_day_report.py
def with_tax(price):
    """Return the price with 10 percent tax, rounded to cents."""
    return round(price * 1.1, 2)

def day_total(prices):
    """Return the total of a day's prices, with tax."""
    total = 0
    for price in prices:
        total += with_tax(price)
    return round(total, 2)

def report(day, prices):
    """Print one summary line for one day."""
    print(f"{day:<9} {len(prices)} sales  {day_total(prices):>6.2f}")

report("Monday", [3.5, 4.0, 2.75])
report("Tuesday", [4.25, 3.5])
report("Friday", [])
```

<!-- output: examples/ex08_day_report.expected -->
```output
Monday    3 sales   11.28
Tuesday   2 sales    8.53
Friday    0 sales    0.00
```

`report()` calls `day_total()`, and `day_total()` calls `with_tax()`. An empty day works too: the loop runs zero times, so the total stays 0. To change the tax, Asha now edits one line, line 4.

## Work with AI

The AI skill for this chapter is writing a function from a **specification**. A specification is a short description of a function: its name, its parameters, what it returns and a few examples with exact results. You write the specification and your own checks. The AI writes the code. Your checks decide if the code is right.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Ask AI to turn your idea into a specification with three exact examples. |
| Write | Write your own check lines from the examples. Ask AI to predict what they print. |
| Generate | Ask AI for the function from the specification. It must return, not print. |
| Test | Run your checks on the AI's function. Every check must print `True`. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask for a review that keeps the name, the parameters and the return value. Run every check again. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha wanted a function for her bill splitter from Chapter 5. Her specification: `share(total, people, tip_percent)` returns each person's share with the tip, rounded to cents. For example, `share(40.0, 4, 10)` returns `11.0`. She asked an AI assistant to write it and to say what her f-string line prints. The AI said it prints `Each pays 11.00`.

```python
# file: examples/ai_share_print.py
def share(total, people, tip_percent):
    each = total * (1 + tip_percent / 100) / people
    print(round(each, 2))

print(f"Each pays {share(40.0, 4, 10):.2f}")
```

<!-- error: examples/ai_share_print.expected_error -->
```output
11.0
Traceback (most recent call last):
  File "ai_share_print.py", line 6, in <module>
    print(f"Each pays {share(40.0, 4, 10):.2f}")
                      ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unsupported format string passed to NoneType.__format__
```

The function prints instead of returning, so the call gives back `None`. The f-string cannot format `None` with `.2f`. The AI broke its own specification and sounded sure. Its next version returned the value but forgot the rounding, and Asha's checks caught that too:

```python
# file: examples/ai_share_noround.py
def share(total, people, tip_percent):
    return total * (1 + tip_percent / 100) / people

print(share(40.0, 4, 10), share(40.0, 4, 10) == 11.0)
print(share(43.07, 4, 0), share(43.07, 4, 0) == 10.77)
print(share(10.0, 3, 0), share(10.0, 3, 0) == 3.33)
```

<!-- output: examples/ai_share_noround.expected -->
```output
11.0 True
10.7675 False
3.3333333333333335 False
```

One check passed only by luck: its exact answer has no extra digits. Adding `round(..., 2)` fixes the function, and all three checks print `True`:

```python
# file: examples/ai_share_fixed.py
def share(total, people, tip_percent):
    return round(total * (1 + tip_percent / 100) / people, 2)

print(share(40.0, 4, 10), share(40.0, 4, 10) == 11.0)
print(share(43.07, 4, 0), share(43.07, 4, 0) == 10.77)
print(share(10.0, 3, 0), share(10.0, 3, 0) == 3.33)
```

<!-- output: examples/ai_share_fixed.expected -->
```output
11.0 True
10.77 True
3.33 True
```

Later, the AI suggested swapping the first two parameters, "because people come before money". Asha ran her checks again before she accepted it, and every check printed `False`: the calls still passed the total first. Never change a function's parameters without changing every call, and run every check after each change.

## Common mistakes

**Mistake 1: calling a function before it is defined.** Python runs from top to bottom, so the `def` must come first.

```python
# file: examples/err01_call_before_def.py
welcome()

def welcome():
    print("Welcome to the Corner Cafe!")
```

<!-- error: examples/err01_call_before_def.expected_error -->
```output
Traceback (most recent call last):
  File "err01_call_before_def.py", line 2, in <module>
    welcome()
    ^^^^^^^
NameError: name 'welcome' is not defined
```

Fix: move the call below the function.

**Mistake 2: forgetting the brackets in a call.** Without brackets, the name refers to the function itself, not to the value it returns.

```python
# file: examples/err02_no_brackets.py
def with_tax(price):
    return round(price * 1.1, 2)

tea = with_tax
print(tea + 1)
```

<!-- error: examples/err02_no_brackets.expected_error -->
```output
Traceback (most recent call last):
  File "err02_no_brackets.py", line 6, in <module>
    print(tea + 1)
          ~~~~^~~
TypeError: unsupported operand type(s) for +: 'function' and 'int'
```

Fix: call it with an argument: `tea = with_tax(3.5)`.

**Mistake 3: printing instead of returning.** The function shows a value, but the caller receives `None`.

```python
# file: examples/err03_none_plus.py
def tax_print(price):
    print(round(price * 1.1, 2))

bill = tax_print(3.5) + 1
print(bill)
```

<!-- error: examples/err03_none_plus.expected_error -->
```output
3.85
Traceback (most recent call last):
  File "err03_none_plus.py", line 5, in <module>
    bill = tax_print(3.5) + 1
           ~~~~~~~~~~~~~~~^~~
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

Fix: replace `print(` with `return ` inside the function. `NoneType` is the type of `None`.

**Mistake 4: returning too early.** A `return` inside the loop ends the whole function in the first pass. There is no error, only a wrong answer.

```python
# file: examples/ex09_return_too_early.py
def day_total(prices):
    total = 0
    for price in prices:
        total += price
        return total

print(day_total([3.5, 4.0, 2.75]))
```

<!-- output: examples/ex09_return_too_early.expected -->
```output
3.5
```

Fix: move `return total` four spaces to the left, so it runs after the loop has finished.

## Think beyond

1. Asha wants a function `member_price(price, is_member)` that gives members 10 percent off. Write its specification first: the return value and three examples, one for a non-member. Which `if` from Chapter 6 does the body need?
2. A function can return a tuple, such as `return total, count`. How would you unpack the two values in the caller, as you did in Chapter 13? Write a `day_summary(prices)` that returns both and test it.

## Recap

- A function is a named block of code. `def` defines it; a call with brackets runs it.
- Parameters are the names in the `def` line. Arguments are the values in the call, matched in order.
- `return` hands a value back to the caller. A function without `return` gives back `None`.
- A docstring on the first line of the body says what the function does.
- A traceback through several functions reads from the bottom up: the bottom block is where the error happened.
- Write a specification and your own checks before you ask AI for the code. The checks decide.

You earned **100 XP** and the **Function Forger** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 17, you will learn where a variable lives inside and outside a function, and how to design small functions that each do one job.
