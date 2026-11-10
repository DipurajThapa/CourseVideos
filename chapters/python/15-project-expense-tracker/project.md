# Chapter 15: Boss Level 3: The Expense Tracker

> Quest: build a tracker that records the cafe's expenses by category, checks every answer, and prints the total for each category, the total for the day and the biggest category. Reward: 300 XP and the **Money Mapper** badge.

## The mission

Every day, the Corner Cafe spends money: milk, coffee beans, paper cups and sometimes a repair. Asha writes each expense on a scrap of paper. When the cafe closes, nobody knows where the money went.

Asha wants a program for it. She types each expense, the category and the amount, and types `done` when the cafe closes. The program then answers three questions: how much did each category cost, how much did the day cost, and which category cost the most?

This boss level uses everything from Chapters 11 to 14, plus the loops and decisions from Module 2:

| Chapter | What you use from it |
|---|---|
| 7 | A `while True` loop that stops with `break` |
| 11 | A list that grows with `append()`, and `sorted()` |
| 12 | A dictionary of totals, `get()` with a default, `values()` and `sum()` |
| 13 | A set of allowed categories, `in` and `not in`, and tuples that you unpack |
| 14 | The habit of running the old and the new version on the same test cases |
| New | `replace()` with a third value, to check an amount such as `12.50` |

## What you will build

A program called `expense_tracker.py`. Here is one day. The text after each question is what Asha typed.

<!-- output: project/expense_tracker.expected -->
```output
Category (or done): milk
Amount: 12.50
Category (or done): beans
Amount: 30
Category (or done): Milk
Amount: 8
Category (or done): cups
Amount: 6.25
Category (or done): done
beans     30.00
cups       6.25
milk      20.50
Expenses: 4  Total: 56.75
Biggest: beans
```

Milk appears twice, 12.50 and 8, so its total is 20.50.

## Acceptance criteria

Your tracker is finished when all of these are true:

1. It asks for a category and an amount until the user types `done`, in capital or small letters.
2. It accepts only the categories milk, beans, cups and repairs, and it gives a clear message for any other answer.
3. It accepts an amount such as `30` or `12.50`, and it gives a clear message for `12,50`, a word or a minus sign, without crashing.
4. It prints one line for each category, in alphabetical order, with its total to two decimal places.
5. It prints the number of expenses, the total for the day and the biggest category. A day with no expenses prints `Biggest: none` and does not crash.
6. You tested it with at least five days whose results you knew in advance.

## Plan it with AI

Before any code, Asha asked an AI assistant to plan how to keep the data. This is the AI skill of this chapter: let AI suggest a data model, then check it against your real data.

> "I am a beginner. I know lists, dictionaries, tuples and sets. I want a program that records the cafe's expenses: a category and an amount for each one. At the end it prints a total for each category and the biggest category. Do not write the program. Suggest how to store the expenses, and give one reason."

An example answer looked like this:

> Store the expenses in a dictionary: the category is the key and the amount is the value, for example `expenses["milk"] = 12.50`. Then the totals are already there.

The suggestion sounds tidy. Asha remembered a rule from Chapter 12: keys in a dictionary are unique. The cafe buys milk twice on a busy day. She tested the idea.

```python
# file: examples/ai_plan_overwrite.py
expenses = {}
expenses["milk"] = 12.50
expenses["beans"] = 30.00
expenses["milk"] = 8.00
print(expenses)
```

<!-- output: examples/ai_plan_overwrite.expected -->
```output
{'milk': 8.0, 'beans': 30.0}
```

The second milk replaced the first one, and 12.50 disappeared. Asha chose a different model: a **list of tuples**, one tuple for each expense, such as `("milk", 12.5)`. Nothing is ever lost. The program then builds a dictionary of totals from the list.

## Build it step by step

**Step 1: Keep each expense as a tuple in a list.**

```python
# file: examples/ex01_record.py
expenses = []
expenses.append(("milk", 12.5))
expenses.append(("beans", 30.0))
print(expenses)
print(len(expenses), "expenses")
category, amount = expenses[0]
print(category, amount)
```

<!-- output: examples/ex01_record.expected -->
```output
[('milk', 12.5), ('beans', 30.0)]
2 expenses
milk 12.5
```

`append()` needs one value, so each tuple has its own brackets inside the brackets of `append()`. Line 7 unpacks the first tuple into two variables, as in Chapter 13.

**Step 2: Ask until done, and check the category.** A set holds the allowed categories, and `not in` finds any other answer.

```python
# file: examples/ex02_categories.py
allowed = {"milk", "beans", "cups", "repairs"}
count = 0
while True:
    category = input("Category (or done): ").strip().lower()
    if category == "done":
        break
    elif category not in allowed:
        print("Use milk, beans, cups or repairs.")
    else:
        count += 1
        print("OK:", category)
print("Categories entered:", count)
```

<!-- output: examples/ex02_categories.expected -->
```output
Category (or done):  Milk
OK: milk
Category (or done): tea
Use milk, beans, cups or repairs.
Category (or done): done
Categories entered: 1
```

Line 5 calls two methods one after the other. `strip()` removes the space before `Milk`, and `lower()` turns it into `milk`, so the set finds it. Asha asked an AI assistant to say which message each of her three answers would get, before she ran the code. Its answer matched the real run.

**Step 3: Check an amount before you convert it.** In Chapter 10, `isdigit()` checked a whole number. An amount such as `12.50` has a decimal point, and `isdigit()` says `False` for it. The fix is to remove one decimal point and then check. `replace()` takes an optional third value: the number of changes to make.

```python
# file: examples/ex03_amount_check.py
print("12.50".replace(".", "", 1))
print("1.2.3".replace(".", "", 1))
for text in ["12.50", "30", "12,50", "twelve", "1.2.3", "-5"]:
    print(f"{text:>7}", text.replace(".", "", 1).isdigit())
```

<!-- output: examples/ex03_amount_check.expected -->
```output
1250
12.3
  12.50 True
     30 True
  12,50 False
 twelve False
  1.2.3 False
     -5 False
```

`"12.50"` becomes `"1250"`, which is all digits. `"1.2.3"` loses only its first point and becomes `"12.3"`, which still has a point, so it fails. Only text with at most one point and nothing but digits passes. Then `float()` is safe.

**Step 4: Add up each category.** A dictionary keeps one total for each category. `get(category, 0)` gives the total so far, or 0 for a category that has no total yet.

```python
# file: examples/ex04_totals.py
expenses = [("milk", 12.5), ("beans", 30.0), ("milk", 8.0), ("cups", 6.25)]
totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount
print(totals)
```

<!-- output: examples/ex04_totals.expected -->
```output
{'milk': 20.5, 'beans': 30.0, 'cups': 6.25}
```

Milk appears twice in the list. The first time, `get()` gives 0, and the total becomes 12.5. The second time, it gives 12.5, and the total becomes 20.5.

**Step 5: Print the table.**

```python
# file: examples/ex05_table.py
expenses = [("milk", 12.5), ("beans", 30.0), ("milk", 8.0), ("cups", 6.25)]
totals = {"milk": 20.5, "beans": 30.0, "cups": 6.25}
for category in sorted(totals):
    print(f"{category:<8}{totals[category]:>7.2f}")
print(f"Expenses: {len(expenses)}  Total: {sum(totals.values()):.2f}")
```

<!-- output: examples/ex05_table.expected -->
```output
beans     30.00
cups       6.25
milk      20.50
Expenses: 4  Total: 56.75
```

`sorted(totals)` gives the keys in alphabetical order. `<8` fills the name to 8 characters, and `>7.2f` puts the amount on the right with two decimal places, as in Chapter 3.

**Step 6: Find the biggest category.** Asha asked an AI assistant for this part. Its answer and her tests are in [Test it](#test-it). The final version keeps a variable `biggest`, which starts as `"none"`, and checks every category in a loop.

**Step 7: Put it together.**

```python
# file: project/expense_tracker.py
allowed = {"milk", "beans", "cups", "repairs"}
expenses = []
while True:
    category = input("Category (or done): ").strip().lower()
    if category == "done":
        break
    elif category not in allowed:
        print("Use milk, beans, cups or repairs.")
    else:
        amount_text = input("Amount: ").strip()
        if amount_text.replace(".", "", 1).isdigit():
            expenses.append((category, float(amount_text)))
        else:
            print("Type an amount like 12.50.")
totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount
biggest = "none"
for category in sorted(totals):
    print(f"{category:<8}{totals[category]:>7.2f}")
    if biggest == "none" or totals[category] > totals[biggest]:
        biggest = category
print(f"Expenses: {len(expenses)}  Total: {sum(totals.values()):.2f}")
print("Biggest:", biggest)
```

Lines 4 to 15 collect the expenses. A category is checked before the program asks for an amount, and an amount is checked before `float()` converts it. Lines 16 to 18 build the totals. The loop on lines 20 to 23 does two jobs: it prints each row, and it keeps the biggest category so far. Lines 24 and 25 print the summary.

## Test it

**AI pair moment.** For Step 6, Asha asked an AI assistant for one line that finds the category with the biggest total in `totals`. It answered `biggest = max(totals)`. It said this gives the category that cost the most. In Chapter 11, `max()` found the largest number in a list, so it looked right. Asha tested it.

```python
# file: examples/ai_biggest_flawed.py
totals = {"milk": 20.5, "beans": 30.0, "cups": 6.25}
biggest = max(totals)
print("Biggest:", biggest)
```

<!-- output: examples/ai_biggest_flawed.expected -->
```output
Biggest: milk
```

Beans cost 30.00, so the answer should be beans. Chapter 12 explains the result: a loop over a dictionary goes through its keys, and `max()` does the same. It compares the names, not the amounts, and `milk` comes last in alphabetical order.

Asha asked the AI for test days, each with the category it expected. It listed three days: three categories, one category, and a day where repairs cost the most. It forgot a day with no expenses, which criterion 5 asks for, so Asha added it as Day 4. Then she ran the AI's line on the first three days.

```python
# file: examples/ai_max_tests.py
day_1 = {"milk": 20.5, "beans": 30.0, "cups": 6.25}
day_2 = {"cups": 9.0}
day_3 = {"beans": 5.0, "repairs": 45.0}
print("Day 1:", max(day_1))
print("Day 2:", max(day_2))
print("Day 3:", max(day_3))
```

<!-- output: examples/ai_max_tests.expected -->
```output
Day 1: milk
Day 2: cups
Day 3: repairs
```

| Test day | Expected | Real | Result |
|---|---|---|---|
| Day 1: three categories | beans | milk | Fail |
| Day 2: one category | cups | cups | Pass |
| Day 3: repairs cost the most | repairs | repairs | Pass, by luck |
| Day 4: no expenses | none | error | Fail |

Day 3 passed only because `repairs` also comes last in alphabetical order. One passing test proves little; several tests with different data catch the mistake. The empty day stopped the program.

<!-- error: examples/ai_max_empty.expected_error -->
```output
Summary
Traceback (most recent call last):
  File "ai_max_empty.py", line 4, in <module>
    biggest = max(totals)
ValueError: max() iterable argument is empty
```

Asha pasted the code and the full error into the chat and asked for the cause before the fix. The AI explained that an empty dictionary has no keys, so `max()` has nothing to choose from. It also agreed that `max()` compares the keys. Its fix keeps the biggest category so far in a loop.

```python
# file: examples/ai_biggest_fixed.py
totals = {"milk": 20.5, "beans": 30.0, "cups": 6.25}
biggest = "none"
for category in totals:
    if biggest == "none" or totals[category] > totals[biggest]:
        biggest = category
print("Biggest:", biggest)
```

<!-- output: examples/ai_biggest_fixed.expected -->
```output
Biggest: beans
```

Asha then ran the fixed loop on all four test days again.

```python
# file: examples/ai_biggest_regression.py
days = [{"milk": 20.5, "beans": 30.0, "cups": 6.25},
        {"cups": 9.0},
        {"beans": 5.0, "repairs": 45.0},
        {}]
for totals in days:
    biggest = "none"
    for category in totals:
        if biggest == "none" or totals[category] > totals[biggest]:
            biggest = category
    print("Biggest:", biggest)
```

<!-- output: examples/ai_biggest_regression.expected -->
```output
Biggest: beans
Biggest: cups
Biggest: repairs
Biggest: none
```

All four days pass. When the complete program was ready, Asha tested whole days. Each test is a copy of `expense_tracker.py` with its own typed answers.

| Test | Answers typed | Expected last lines | Result |
|---|---|---|---|
| A normal day | milk 12.50, beans 30, Milk 8, cups 6.25 | `Total: 56.75`, `Biggest: beans` | Pass |
| An empty day | done | `Total: 0.00`, `Biggest: none` | Pass |
| Bad amounts | milk 12,50, milk twelve, milk 12.50 | two messages, then `Total: 12.50` | Pass |
| Unknown categories | tea, cake, then " repairs " 45 | two messages, then `Biggest: repairs` | Pass |
| One expense | cups 9 | `Total: 9.00`, `Biggest: cups` | Pass |

Here are two of the runs.

<!-- output: examples/test_empty.expected -->
```output
Category (or done): done
Expenses: 0  Total: 0.00
Biggest: none
```

<!-- output: examples/test_bad_amount.expected -->
```output
Category (or done): milk
Amount: 12,50
Type an amount like 12.50.
Category (or done): milk
Amount: twelve
Type an amount like 12.50.
Category (or done): milk
Amount: 12.50
Category (or done): done
milk      12.50
Expenses: 1  Total: 12.50
Biggest: milk
```

## Improve it with AI

With every test passing, Asha asked an AI assistant: "Suggest one way to make lines 16 to 18 shorter. Do not change what the program prints." The AI suggested `totals[category] += amount`, "because `+=` adds to the total". Asha remembered the reason for `get()` in Chapter 12. She tested the suggestion on three expenses.

```python
# file: examples/ai_totals_keyerror.py
expenses = [("milk", 12.5), ("beans", 30.0), ("milk", 8.0)]
totals = {}
for category, amount in expenses:
    totals[category] += amount
print(totals)
```

<!-- error: examples/ai_totals_keyerror.expected_error -->
```output
Traceback (most recent call last):
  File "ai_totals_keyerror.py", line 5, in <module>
    totals[category] += amount
    ~~~~~~^^^^^^^^^^
KeyError: 'milk'
```

`+=` reads the old total first, and the first milk has no total yet, so Python stops with a `KeyError`. The shorter line breaks the program. Asha kept `get(category, 0)`.

These are the six ways AI helped with this project. The full prompts are in [ai-prompts.md](ai-prompts.md).

| Stage | How AI helped |
|---|---|
| Plan | Suggested a data model, which Asha tested and replaced: a dictionary would lose the second milk. |
| Write | Said which message each answer gets in Asha's own category loop, before she ran it. |
| Generate | Wrote the biggest-category line, with a confident mistake: `max(totals)` compares names. |
| Test | Listed three test days with expected results, but forgot the empty day; one day passed only by luck. |
| Debug | Explained the `ValueError` on an empty day, then gave a loop that works for every day. |
| Improve | Suggested `+=`, which a test showed would stop the program with a `KeyError`. |

## Recap

- Keep each record as a tuple in a list, so nothing is lost. Build a dictionary of totals from the list with `get(key, 0)`.
- A set of allowed values and `not in` reject any other answer. `strip()` and `lower()` clean an answer first.
- `replace(".", "", 1)` removes one decimal point, so `isdigit()` can check an amount before `float()` converts it.
- `max()` on a dictionary compares the keys, not the values. To find the biggest value, keep the best key so far in a loop.
- Test with several cases, including an empty one. One passing test can pass by luck.

You earned **300 XP** and the **Money Mapper** badge. Module 3 is complete.

The practice tasks for this chapter are in [practice/practice.md](practice/practice.md).

## What's next

In Chapter 16, you will learn functions: named blocks of code that you write once and use many times. Then one line can print the tracker's summary for any day.
