# Chapter 17: Scope and Good Function Design

> Quest: decide where each variable lives, pass values in and return results out, and split a function that does too much into small functions with one job each. Reward: 100 XP and the **Architect** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Explain the difference between a local variable and a global variable, and predict which one a line uses.
- Fix a `NameError` and an `UnboundLocalError` caused by scope.
- Write functions with default arguments and call them with keyword arguments.
- Split a function that does several jobs into small functions that each do one job.
- Ask an AI assistant which functions do too much, and check its split with the same tests before and after.

## Why this matters

In Chapter 16, Asha's `day_total()` function had a variable called `total` inside it. Can the rest of her program read it? And her old "close the day" function calculates, prints and changes a week total, all at once. When one part goes wrong, she has to read the whole function to find it.

Real programs have hundreds of functions. They stay manageable only when each function is small, gets everything it needs through its parameters, and gives its result back with `return`. A function like that can be tested on its own and reused anywhere, and an AI assistant can change it without breaking the rest of the program.

## The idea

The **scope** of a variable is the part of the program where its name can be used. Python has two scopes you need now:

| Scope | Where the variable is created | Where you can use it |
|---|---|---|
| Local | Inside a function, by assigning to it or as a parameter | Only inside that function, while it runs |
| Global | At the top level of the file, outside every function | Everywhere in the file, including inside functions (for reading) |

```text
  file (global scope)
  +--------------------------------------+
  | tax_rate = 1.1                        |
  |                                       |
  |   def day_total(prices):             |
  |   +--------------------------------+ |
  |   | local: prices, total, price    | |
  |   | can read tax_rate              | |
  |   +--------------------------------+ |
  |                                       |
  | print(total)   <- NameError           |
  +--------------------------------------+
```

Think of a function as a kitchen with its own small whiteboard. Notes written on the kitchen whiteboard are local: they are wiped when the cook finishes, and nobody in the cafe can read them. The big menu board on the wall is global: the cook can read it from the kitchen. The comparison stops working at one point. Suppose the cook writes a note with the same name as something on the menu board. Python then treats that name as a kitchen note for the whole function, even on the lines before the note was written.

Good function design follows one rule: **pass values in, return results out.** A function that reads only its parameters and returns its result, without printing or changing anything outside, is called a **pure function**. A pure function gives the same result for the same arguments every time, so you can test it with one line.

## Build it step by step

**Step 1: A local variable lives inside its function.** `total` is created inside `day_total()`.

```python
# file: examples/ex01_local.py
def day_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

print(day_total([3.5, 4.0]))
print(total)
```

<!-- error: examples/ex01_local.expected_error -->
```output
7.5
Traceback (most recent call last):
  File "ex01_local.py", line 9, in <module>
    print(total)
          ^^^^^
NameError: name 'total' is not defined
```

Line 8 works: the function returns the value of `total`. Line 9 fails, because `total` existed only while the function ran. To use a result outside, return it and store it in a variable.

**Step 2: A function can read a global variable.** `tax_rate` is created at the top level.

```python
# file: examples/ex02_global_read.py
tax_rate = 1.1

def with_tax(price):
    return round(price * tax_rate, 2)

print(with_tax(3.5))
tax_rate = 1.2
print(with_tax(3.5))
```

<!-- output: examples/ex02_global_read.expected -->
```output
3.85
4.2
```

The same call gives two different results, because the function reads `tax_rate` at the moment it runs. Nothing in the call `with_tax(3.5)` shows that the result depends on another line of the program. That hidden link is why good functions take what they need as parameters.

**Step 3: Assigning to a global name inside a function.** Asha tries to count sales with a global variable.

```python
# file: examples/ex03_unbound.py
sales_count = 0

def add_sale():
    sales_count = sales_count + 1

add_sale()
print(sales_count)
```

<!-- error: examples/ex03_unbound.expected_error -->
```output
Traceback (most recent call last):
  File "ex03_unbound.py", line 7, in <module>
    add_sale()
    ~~~~~~~~^^
  File "ex03_unbound.py", line 5, in add_sale
    sales_count = sales_count + 1
                  ^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'sales_count' where it is not associated with a value
```

Line 5 assigns to `sales_count`, so Python decides that `sales_count` is a local variable for the whole function. The right side then tries to read that local variable before it has a value. Python has a keyword, `global`, that lets a function change a global variable, but it brings back the hidden link from step 2. The better fix is to pass the value in and return the new value:

```python
# file: examples/ex04_pass_in.py
def add_sale(count):
    return count + 1

sales_count = 0
sales_count = add_sale(sales_count)
sales_count = add_sale(sales_count)
print(sales_count)
```

<!-- output: examples/ex04_pass_in.expected -->
```output
2
```

**Step 4: Default arguments.** A **default argument** is a value a parameter gets when the call leaves it out.

```python
# file: examples/ex05_defaults.py
def with_tax(price, rate=1.1):
    return round(price * rate, 2)

print(with_tax(3.5))
print(with_tax(3.5, 1.2))
print(with_tax(4.0))
```

<!-- output: examples/ex05_defaults.expected -->
```output
3.85
4.2
4.4
```

The rate is now a parameter, so nothing is hidden, and most calls stay short. Parameters with a default must come after the parameters without one.

**Step 5: Keyword arguments.** A **keyword argument** names the parameter in the call: `qty=2`. Keyword arguments can come in any order, after any positional ones.

```python
# file: examples/ex06_keywords.py
def order_line(item, price, qty=1):
    return f"{qty} x {item:<6} {price * qty:>5.2f}"

print(order_line("Tea", 3.5))
print(order_line("Cake", 4.0, qty=2))
print(order_line(price=2.75, item="Scone"))
```

<!-- output: examples/ex06_keywords.expected -->
```output
1 x Tea     3.50
2 x Cake    8.00
1 x Scone   2.75
```

Line 6 names `qty`, so a reader sees at once what the 2 means. Line 7 gives both arguments by name, in a different order from the definition.

**Step 6: One job per function.** A function that calculates and prints is hard to test, because its result goes to the screen, not back to you. Here the jobs are split: one function calculates, one builds the text, and the main code prints.

```python
# file: examples/ex07_one_job.py
def day_total(prices):
    total = 0
    for price in prices:
        total += price
    return round(total, 2)

def total_line(day, total):
    return f"{day}: {total:.2f}"

monday = day_total([3.85, 4.4, 3.03])
print(total_line("Monday", monday))
print(monday == 11.28)
```

<!-- output: examples/ex07_one_job.expected -->
```output
Monday: 11.28
True
```

Both functions are pure. Line 13 tests `day_total()` with one comparison, which is impossible for a function that only prints.

## See the outcome

Here is Asha's day report from Chapter 16, redesigned. The tax rate is a default argument instead of a fixed number, every function returns its result, and only the last three lines print.

```python
# file: examples/ex08_day_report.py
def with_tax(price, rate=1.1):
    """Return the price with tax, rounded to cents."""
    return round(price * rate, 2)

def day_total(prices, rate=1.1):
    """Return the day's total with tax."""
    total = 0
    for price in prices:
        total += with_tax(price, rate)
    return round(total, 2)

def report_line(day, prices, rate=1.1):
    """Return one report line as text."""
    return f"{day:<8} {len(prices)} sales {day_total(prices, rate):>6.2f}"

print(report_line("Monday", [3.5, 4.0, 2.75]))
print(report_line("Friday", [4.25, 3.5], rate=1.2))
print(day_total([3.5, 4.0, 2.75]) == 11.28)
```

<!-- output: examples/ex08_day_report.expected -->
```output
Monday   3 sales  11.28
Friday   2 sales   9.30
True
```

Line 18 uses the keyword argument `rate=1.2` for a day with a higher tax, and every function passes the rate on. Line 19 tests a total in one line. Each variable lives exactly where it is needed: `total` and `price` only inside `day_total()`.

## Work with AI

The AI skill for this chapter is asking an AI assistant to find functions that do too much and to suggest a split. A split must not change what the program prints, so record the output before the change and compare it after every change.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Paste a long function and ask AI to list each job it does. No code yet. |
| Write | Run the original program and save its exact output. That output is your target. |
| Generate | Ask AI to split the function into small functions with no global variables and the same output. |
| Test | Ask AI for test cases with expected lines. Run them on the split, before and after each fix. |
| Debug | Paste the code and the full error. Ask for the cause and a fix that keeps your design rules. |
| Improve | Ask for one improvement. Test it with two separate days before you accept it. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha's old `close_day()` function adds tax, prints a line and changes a global week total. She saved its output first:

```python
# file: examples/ai_close_day_original.py
week_total = 0

def close_day(day, prices):
    global week_total
    total = 0
    for price in prices:
        total += round(price * 1.1, 2)
    total = round(total, 2)
    print(f"{day:<8} {len(prices)} sales {total:>6.2f}")
    week_total = round(week_total + total, 2)

close_day("Monday", [3.5, 4.0, 2.75])
close_day("Tuesday", [4.25, 3.5])
print(f"Week {week_total:>17.2f}")
```

<!-- output: examples/ai_close_day_original.expected -->
```output
Monday   3 sales  11.28
Tuesday  2 sales   8.53
Week             19.81
```

She asked an AI assistant: "Split this function into small functions with one job each. Use no global variables. The output must stay exactly the same." The AI answered with this code and said the output was the same:

```python
# file: examples/ai_split_flawed.py
def day_total(prices):
    total = 0
    for price in prices:
        total += round(price * 1.1, 2)
    return round(total, 2)

def report_line(day, prices):
    print(f"{day:<8} {len(prices)} sales {day_total(prices):>6.2f}")

monday = [3.5, 4.0, 2.75]
tuesday = [4.25, 3.5]
print(report_line("Monday", monday))
print(report_line("Tuesday", tuesday))
week_total = round(day_total(monday) + day_total(tuesday), 2)
print(f"Week {week_total:>17.2f}")
```

<!-- output: examples/ai_split_flawed.expected -->
```output
Monday   3 sales  11.28
None
Tuesday  2 sales   8.53
None
Week             19.81
```

Two extra lines say `None`. `report_line()` prints instead of returning, so it returns `None`, and lines 13 and 14 print that too. Comparing with the saved output catches it at once. The fix is one word: `return` instead of `print(` on line 9.

```python
# file: examples/ai_split_fixed.py
def day_total(prices):
    total = 0
    for price in prices:
        total += round(price * 1.1, 2)
    return round(total, 2)

def report_line(day, prices):
    return f"{day:<8} {len(prices)} sales {day_total(prices):>6.2f}"

monday = [3.5, 4.0, 2.75]
tuesday = [4.25, 3.5]
print(report_line("Monday", monday))
print(report_line("Tuesday", tuesday))
week_total = round(day_total(monday) + day_total(tuesday), 2)
print(f"Week {week_total:>17.2f}")
```

<!-- output: examples/ai_split_fixed.expected -->
```output
Monday   3 sales  11.28
Tuesday  2 sales   8.53
Week             19.81
```

The output now matches the original exactly. Later, the AI suggested a default empty list, `sales=[]`, so that she could record sales without making a list first. Asha tested it with two separate days:

```python
# file: examples/ai_record_flawed.py
def record_sale(price, sales=[]):
    sales.append(price)
    return sales

monday = record_sale(3.5)
monday = record_sale(4.0, monday)
tuesday = record_sale(4.25)
print("Monday:", monday)
print("Tuesday:", tuesday)
```

<!-- output: examples/ai_record_flawed.expected -->
```output
Monday: [3.5, 4.0, 4.25]
Tuesday: [3.5, 4.0, 4.25]
```

Python creates a default value once, when the `def` line runs, not at each call. Every call that leaves out `sales` shares the same list, so Tuesday's sale lands in Monday's list too. Asha rejected the suggestion and passes a new empty list for each day.

## Common mistakes

**Mistake 1: using a local variable outside its function.** The variable disappears when the function ends.

```python
# file: examples/err01_local_outside.py
def thank_you(name):
    message = f"Thank you, {name}!"

thank_you("Omar")
print(message)
```

<!-- error: examples/err01_local_outside.expected_error -->
```output
Traceback (most recent call last):
  File "err01_local_outside.py", line 6, in <module>
    print(message)
          ^^^^^^^
NameError: name 'message' is not defined
```

Fix: end the function with `return message`, then write `message = thank_you("Omar")`.

**Mistake 2: a positional argument after a keyword argument.** Once you name one argument in a call, every argument after it needs a name too.

```python
# file: examples/err02_keyword_order.py
def order_line(item, price, qty=1):
    return f"{qty} x {item:<6} {price * qty:>5.2f}"

print(order_line(item="Cake", 4.0))
```

<!-- error: examples/err02_keyword_order.expected_error -->
```output
  File "err02_keyword_order.py", line 5
    print(order_line(item="Cake", 4.0))
                                     ^
SyntaxError: positional argument follows keyword argument
```

Fix: write `order_line("Cake", 4.0)` or `order_line(item="Cake", price=4.0)`.

**Mistake 3: a default before a parameter without one.** In the `def` line, parameters with a default go last.

```python
# file: examples/err03_default_order.py
def with_tax(rate=1.1, price):
    return round(price * rate, 2)

print(with_tax(price=3.5))
```

<!-- error: examples/err03_default_order.expected_error -->
```output
  File "err03_default_order.py", line 2
    def with_tax(rate=1.1, price):
                           ^^^^^
SyntaxError: parameter without a default follows parameter with a default
```

Fix: write `def with_tax(price, rate=1.1):`.

**Mistake 4: a list as a default value.** This mistake gives no error, which makes it worse.

```python
# file: examples/err04_shared_list.py
def new_order(item, order=[]):
    order.append(item)
    return order

lina = new_order("Tea")
omar = new_order("Cake")
print("Lina:", lina)
print("Omar:", omar)
```

<!-- output: examples/err04_shared_list.expected -->
```output
Lina: ['Tea', 'Cake']
Omar: ['Tea', 'Cake']
```

Lina and Omar share one list, because the default list is created only once. Fix: remove the default and pass a new list in each call, `new_order("Tea", [])`.

## Think beyond

1. Asha's `report_line()` builds text but does not print it. Why does that make it easier to send the same line to a printer, a file or a chat message later?
2. You have a function `close_day()` with 30 lines that reads input, calculates, prints and saves. Which three or four smaller functions would you split it into, and which of them could be pure?

## Recap

- A local variable is created inside a function and exists only while the function runs. A global variable is created at the top level.
- A function can read a global variable, but its result then depends on a line you cannot see in the call.
- Assigning to a name inside a function makes that name local for the whole function, which causes an `UnboundLocalError` if you read it first.
- Pass values in and return results out. A pure function uses only its parameters and returns its result.
- Default arguments make a parameter optional; keyword arguments name the parameter in the call. Never use a list as a default.
- Before you accept an AI split, save the old output and compare every line after each change.

You earned **100 XP** and the **Architect** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 18, you will move your functions into their own file, import them, and use ready-made modules from Python's standard library.
