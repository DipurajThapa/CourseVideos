# Chapter 11: Lists: Keeping Many Values in Order

> Quest: keep many values in one list, read and change them by position, and let Python sort and add them up. Reward: 100 XP and the **List Builder** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write a list and read any item with its index, counting from the start or from the end.
- Change a list with `append()`, `insert()`, `remove()` and `pop()`.
- Take a part of a list with a slice and predict which items it gives.
- Build a list in a loop, go through it with `for`, and check for an item with `in`.
- Sort a list and use `sum()`, `min()` and `max()` to report on it.

## Why this matters

In Chapter 10, the guessing game forgot every guess as soon as the next one arrived. Each guess lived in one variable, and each new answer replaced the old one. Asha's day report in Chapter 9 had the same limit: it added up the sales as they were typed, but it could not show them again.

A **list** keeps many values in one variable, in a fixed order. You can add values, remove them, sort them and go through them one by one. A list of 3 sales and a list of 3,000 sales need the same code.

Lists are everywhere in real programs. A music app keeps your playlist in a list. A shop keeps the items in your basket. A chat app keeps the messages in order.

## The idea

A list is written with square brackets, with commas between the items. Each item has an **index**: its position, counting from 0. Negative indexes count from the end, so `-1` is always the last item.

```text
menu = ["tea", "cake", "juice", "scone"]

  index:      0       1        2        3
  item:    "tea"  "cake"  "juice"  "scone"
  from end:  -4      -3       -2       -1
```

A list can hold any type: strings, numbers or a mix. It can also hold the same value twice.

In Chapter 3, you learned that a string cannot be changed after it is made. A list can. You can replace an item, add one or remove one, and the list itself changes. A list is **mutable**, which means it can change after it is made.

Think of a numbered queue of order tickets on the kitchen wall. You can add a ticket at the end, push one in at the front or take one away. Unlike paper tickets, the numbers move: when you take ticket 0 away, the next ticket becomes ticket 0.

## Build it step by step

**Step 1: Make a list and read its items.** Asha writes today's first order as a list.

```python
# file: examples/ex01_order_list.py
order = ["tea", "cake", "sandwich", "tea"]
print(order)
print(order[0])
print(order[2])
print(order[-1])
print(len(order))
```

<!-- output: examples/ex01_order_list.expected -->
```output
['tea', 'cake', 'sandwich', 'tea']
tea
sandwich
tea
4
```

Printing the whole list shows the brackets and the quotation marks. `order[2]` is the third item, because counting starts at 0. `len()` from Chapter 3 counts the items in a list, as it counts the characters in a string.

**Step 2: Change a list.** A **method** is a function that belongs to a value, like `upper()` for strings. Lists have methods that change the list itself.

```python
# file: examples/ex02_change_order.py
order = ["tea", "cake"]
order.append("sandwich")
print(order)
order.insert(0, "juice")
print(order)
order[1] = "green tea"
print(order)
order.remove("cake")
print(order)
last = order.pop()
print(last, order)
```

<!-- output: examples/ex02_change_order.expected -->
```output
['tea', 'cake', 'sandwich']
['juice', 'tea', 'cake', 'sandwich']
['juice', 'green tea', 'cake', 'sandwich']
['juice', 'green tea', 'sandwich']
sandwich ['juice', 'green tea']
```

| Code | What it does |
|---|---|
| `order.append(x)` | Adds `x` at the end. |
| `order.insert(i, x)` | Puts `x` at index `i` and moves the rest along. |
| `order[i] = x` | Replaces the item at index `i`. |
| `order.remove(x)` | Removes the first item equal to `x`. |
| `order.pop()` | Removes the last item and gives it back. |

After line 5, `"tea"` moved from index 0 to index 1, so line 7 replaces `"tea"`, not `"juice"`. Line 11 keeps the removed item in the variable `last`.

**Step 3: Take a part of a list with a slice.** A **slice** gives a new list with some of the items: `sales[start:stop]`. Like `range()` in Chapter 8, it stops before `stop`.

```python
# file: examples/ex03_slices.py
sales = [12.5, 8.0, 15.75, 9.25, 21.0]
print(sales[1:3])
print(sales[:2])
print(sales[2:])
print(sales[-2:])
print(sales[1:10])
```

<!-- output: examples/ex03_slices.expected -->
```output
[8.0, 15.75]
[12.5, 8.0]
[15.75, 9.25, 21.0]
[9.25, 21.0]
[8.0, 15.75, 9.25, 21.0]
```

Line 3 gives the items at index 1 and 2. With no start, a slice starts at 0. With no stop, it goes to the end. `[-2:]` gives the last two items. Line 7 asks for more items than the list has, and a slice stops at the end, with no error.

**Step 4: Build a list in a loop.** Here is the fix for the game that forgot its guesses. An empty list, `[]`, grows by one item on each pass.

```python
# file: examples/ex04_guesses.py
guesses = []
for turn in range(1, 4):
    guess = int(input(f"Guess {turn}: "))
    guesses.append(guess)
print(f"Your guesses: {guesses}")
for guess in guesses:
    print(f"- {guess}")
if 12 in guesses:
    print("You tried 12.")
print(20 in guesses)
```

<!-- output: examples/ex04_guesses.expected -->
```output
Guess 1: 7
Guess 2: 12
Guess 3: 15
Your guesses: [7, 12, 15]
- 7
- 12
- 15
You tried 12.
False
```

A `for` loop goes through a list item by item, as it goes through the characters of a string. The `in` operator checks whether a value is in the list and gives `True` or `False`.

**Step 5: Sort and add up.** Python has functions that work on a whole list of numbers.

```python
# file: examples/ex05_sorting.py
sales = [12.5, 8.0, 15.75, 9.25]
print(sorted(sales))
print(sales)
sales.sort()
print(sales)
print(sorted(sales, reverse=True))
print(sum(sales), min(sales), max(sales))
```

<!-- output: examples/ex05_sorting.expected -->
```output
[8.0, 9.25, 12.5, 15.75]
[12.5, 8.0, 15.75, 9.25]
[8.0, 9.25, 12.5, 15.75]
[15.75, 12.5, 9.25, 8.0]
45.5 8.0 15.75
```

There are two ways to sort, and the difference matters:

| Code | The original list | What it gives back |
|---|---|---|
| `sorted(sales)` | stays the same | a new sorted list |
| `sales.sort()` | is sorted | `None`, which means "no value" |

`reverse=True` sorts from the biggest to the smallest. `sum()`, `min()` and `max()` give the total, the smallest and the biggest number.

## See the outcome

Here is Asha's day report. Every sale is kept, so the report can show the total, the average, the best sales and the order of the day.

```python
# file: examples/ex06_day_report.py
sales = [12.5, 8.0, 15.75, 9.25, 21.0]
sales.append(6.5)
total = sum(sales)
print(f"Sales today: {len(sales)}")
print(f"Total: {total:.2f}")
print(f"Average: {total / len(sales):.2f}")
print(f"Biggest: {max(sales):.2f}")
print(f"Smallest: {min(sales):.2f}")
print(f"Last three: {sales[-3:]}")
best = sorted(sales, reverse=True)
print(f"Best two: {best[:2]}")
print(f"In order of the day: {sales}")
```

<!-- output: examples/ex06_day_report.expected -->
```output
Sales today: 6
Total: 73.00
Average: 12.17
Biggest: 21.00
Smallest: 6.50
Last three: [9.25, 21.0, 6.5]
Best two: [21.0, 15.75]
In order of the day: [12.5, 8.0, 15.75, 9.25, 21.0, 6.5]
```

Line 3 adds the sixth sale. Line 7 divides the total by `len(sales)`, so the average stays right when more sales are added. Line 11 uses `sorted()`, so the last line still shows the sales in the order they happened.

## Work with AI

The AI skill for this chapter is asking for a worked example. When AI explains a slice or a list method, ask it to show a small list, the code and the exact result. Then run the example yourself. An explanation is only as good as the result it predicts.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe what the list must do and ask AI for the steps, before any code. |
| Write | Write the code yourself, then ask AI to explain one slice or method with a worked example. |
| Generate | Ask for code with your list and the exact output it prints. |
| Test | Ask for test lists with the expected result for each, such as a short list or equal values, then run them. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask for a clearer version that prints exactly the same. Run both and compare every line. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha wanted the three best sales of the day for a "Top sales" line. She asked an AI assistant: "Here is my list: sales = [12.5, 8.0, 15.75, 9.25, 21.0, 6.5]. Write code that prints the three biggest sales. Show the exact output." The AI said the output would be `Top three: [21.0, 15.75, 12.5]`, and gave this code.

```python
# file: examples/ai_top_flawed.py
sales = [12.5, 8.0, 15.75, 9.25, 21.0, 6.5]
sales.sort()
top_three = sales[:3]
print(f"Top three: {top_three}")
```

Asha ran it:

<!-- output: examples/ai_top_flawed.expected -->
```output
Top three: [6.5, 8.0, 9.25]
```

These are the three smallest sales. `sort()` puts the smallest first, so the first three items are the smallest. A quick check catches this: the first of the top three must equal `max(sales)`, which is 21.0. Sorting with `reverse=True` puts the biggest first:

```python
# file: examples/ai_top_fixed.py
sales = [12.5, 8.0, 15.75, 9.25, 21.0, 6.5]
sales.sort(reverse=True)
top_three = sales[:3]
print(f"Top three: {top_three}")
```

<!-- output: examples/ai_top_fixed.expected -->
```output
Top three: [21.0, 15.75, 12.5]
```

Asha then tested a day with three equal sales and a day with only two sales. A slice never goes past the end of a list, so a short day gives two items and no error.

## Common mistakes

**Mistake 1: an index past the end.** A list of 4 items has the indexes 0 to 3.

```python
# file: examples/err01_index.py
order = ["tea", "cake", "sandwich", "tea"]
print(order[0])
print(order[4])
```

<!-- error: examples/err01_index.expected_error -->
```output
tea
Traceback (most recent call last):
  File "err01_index.py", line 4, in <module>
    print(order[4])
          ~~~~~^^^
IndexError: list index out of range
```

Fix: the last index is `len(order) - 1`, or `-1`.

**Mistake 2: keeping the result of `sort()`.** `sort()` sorts the list and gives back `None`.

```python
# file: examples/ex07_sort_none.py
sales = [12.5, 8.0, 15.75]
sales = sales.sort()
print(sales)
```

<!-- output: examples/ex07_sort_none.expected -->
```output
None
```

There is no error on line 3, but the sales are gone: `sales` now refers to `None`. Fix: write `sales.sort()` on its own line, or use `sorted_sales = sorted(sales)`.

**Mistake 3: removing an item that is not there.** `remove()` deletes only the first match, and it stops the program if there is no match.

```python
# file: examples/err02_remove_missing.py
order = ["tea", "cake", "tea"]
order.remove("tea")
print(order)
order.remove("juice")
```

<!-- error: examples/err02_remove_missing.expected_error -->
```output
['cake', 'tea']
Traceback (most recent call last):
  File "err02_remove_missing.py", line 5, in <module>
    order.remove("juice")
    ~~~~~~~~~~~~^^^^^^^^^
ValueError: list.remove(x): x not in list
```

Line 3 removed only the first `"tea"`. Fix: check first with `if "juice" in order:`, then remove it.

**Mistake 4: a missing comma.** Two strings with no comma between them become one string.

```python
# file: examples/ex08_missing_comma.py
order = ["tea" "cake", "sandwich"]
print(order)
print(len(order))
```

<!-- output: examples/ex08_missing_comma.expected -->
```output
['teacake', 'sandwich']
2
```

There is no error, but the list has 2 items instead of 3. Fix: put a comma between every two items, and check the count with `len()`.

## Think beyond

1. In the guessing game, a player types 7 twice. How could `in` let the game say "You already guessed 7" and not count the second try?
2. `range()` has a step, such as `range(0, 10, 2)`. A slice can have a step too: `sales[::2]`. Predict which sales it gives, then run it.

## Recap

- A list keeps many values in one variable, in order. Each item has an index that starts at 0, and `-1` is the last item.
- A list is mutable: `append()`, `insert()`, `remove()`, `pop()` and `list[i] = x` change it.
- A slice `[start:stop]` gives a new list and stops before `stop`. It never goes past the end.
- `for` goes through a list item by item, and `in` checks whether a value is in it.
- `sorted()` gives a new list; `sort()` changes the list and gives back `None`.
- Ask AI for a worked example of a slice or a method, then run the example yourself.

You earned **100 XP** and the **List Builder** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 12, you will learn dictionaries, which find a value by a name instead of a position, such as the price of `"tea"`.
