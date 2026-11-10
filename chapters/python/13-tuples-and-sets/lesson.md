# Chapter 13: Tuples and Sets: Fixed Groups and Unique Items

> Quest: keep fixed groups of values in tuples, keep each item only once in a set, compare two days of customers, and choose the right collection for a job. Reward: 100 XP and the **Collector** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write a tuple, read its values and unpack them into variables.
- Make a set from a list to remove repeats, and check items with `in`.
- Compare two sets with `|`, `&`, `-` and `^`.
- Choose between a list, a tuple, a set and a dictionary for a task, and explain the choice.
- Ask AI to compare options with their trade-offs, then test its advice.

## Why this matters

At the end of Chapter 12, Asha's list of today's customers had Omar in it four times. A list keeps every repeat, so `len()` counts visits, not people. To count different customers, Asha needs a collection that keeps each name only once. That collection is a **set**.

Some data never changes once you write it, such as the cafe's opening hours or one item with its price. A **tuple** keeps a fixed group of values together, and Python stops you if you try to change it by mistake.

Real programs choose their collections with care. A booking site keeps each seat only once. A map app stores each place as a fixed pair of numbers. The right choice makes the code shorter and safer.

## The idea

You now know four collections. Each one fits a different job.

| Collection | Written with | Keeps order | Allows repeats | Can change | Use it for |
|---|---|---|---|---|---|
| list | `[ ]` | yes | yes | yes | Many values in order, such as today's visits |
| tuple | `( )` | yes | yes | no | A fixed group, such as opening hours |
| set | `{ }` with values | no | no | yes | Each item once, such as different customers |
| dictionary | `{ }` with keys | yes | keys: no | yes | Values found by name, such as prices |

A **tuple** is like a list that cannot change. A **set** is like a bag of name cards: each name is in the bag once, and the cards are in no fixed order. Unlike a bag, a set ignores a card that is already inside, so you can add Omar many times and still have one Omar.

## Build it step by step

**Step 1: Make a tuple and read its values.** Round brackets make a tuple. You read a value with its index, as with a list.

```python
# file: examples/ex01_tuples.py
hours = (8, 18)
special = ("Scone", 2.75)
print(hours)
print(hours[0], hours[1])
print(special[0])
print(len(special))
print(type(hours))
```

<!-- output: examples/ex01_tuples.expected -->
```output
(8, 18)
8 18
Scone
2
<class 'tuple'>
```

`hours` holds the opening hour and the closing hour. `special` holds a name and a price of different types. A tuple can hold any types, even a list.

**Step 2: Unpack a tuple.** **Unpacking** puts each value of a tuple into its own variable, in one line.

```python
# file: examples/ex02_unpacking.py
hours = (8, 18)
opens, closes = hours
print(f"Open {opens}:00 to {closes}:00")
name, price = ("Scone", 2.75)
print(f"{name}: {price:.2f}")
first = "Omar"
second = "Lina"
first, second = second, first
print(first, second)
```

<!-- output: examples/ex02_unpacking.expected -->
```output
Open 8:00 to 18:00
Scone: 2.75
Lina Omar
```

Line 3 gives `opens` the first value and `closes` the second. The number of names on the left must match the number of values. Line 9 swaps two variables: Python builds the tuple on the right first, then unpacks it. This answers the swap question from Chapter 2 without a third variable.

**Step 3: Keep tuples in a list.** A list of tuples is a common way to store records, such as menu items with their prices.

```python
# file: examples/ex03_specials.py
specials = [("Tea", 3.5), ("Scone", 2.75), ("Cake", 4.25)]
total = 0
for name, price in specials:
    print(f"{name:<8}{price:>6.2f}")
    total += price
print(f"{'Total':<8}{total:>6.2f}")
print(specials[1][0])
```

<!-- output: examples/ex03_specials.expected -->
```output
Tea       3.50
Scone     2.75
Cake      4.25
Total    10.50
Scone
```

Line 4 unpacks each tuple into `name` and `price`, as `items()` did with a dictionary in Chapter 12. Line 8 reads in two steps: `specials[1]` is the tuple `("Scone", 2.75)`, and `[0]` reads its first value.

**Step 4: Remove repeats with a set.** `set()` turns a list into a set, and every repeat disappears.

```python
# file: examples/ex04_unique.py
visits = ["Omar", "Lina", "Omar", "Sam", "Omar"]
customers = set(visits)
print(len(visits))
print(len(customers))
print(sorted(customers))
print("Lina" in customers)
print("Ravi" in customers)
```

<!-- output: examples/ex04_unique.expected -->
```output
5
3
['Lina', 'Omar', 'Sam']
True
False
```

The list has 5 visits, but the set has 3 different customers. A set has no order, so if you print it directly, the names can appear in a different order on another run. `sorted()` gives a list in a fixed order, which is why every example in this chapter prints `sorted(...)` instead of the set itself. `in` checks a set quickly, even when it holds thousands of names.

**Step 5: Add and remove items.** A set can change. `add()` puts an item in, and `discard()` takes one out.

```python
# file: examples/ex05_change_set.py
regulars = set()
regulars.add("Omar")
regulars.add("Lina")
regulars.add("Omar")
print(sorted(regulars), len(regulars))
regulars.discard("Lina")
regulars.discard("Zoe")
print(sorted(regulars))
print(type({}), type(set()))
```

<!-- output: examples/ex05_change_set.expected -->
```output
['Lina', 'Omar'] 2
['Omar']
<class 'dict'> <class 'set'>
```

Line 5 adds Omar a second time, and nothing changes: the set already holds Omar. Line 8 discards Zoe, who is not in the set, and there is no error. Line 10 shows an important rule: empty curly brackets, `{}`, make an empty dictionary. To make an empty set, write `set()`.

**Step 6: Compare two sets.** Four operators compare two sets and give a new set.

```python
# file: examples/ex06_set_ops.py
today = {"Omar", "Lina", "Sam"}
yesterday = {"Lina", "Ravi", "Sam"}
print(sorted(today | yesterday))
print(sorted(today & yesterday))
print(sorted(today - yesterday))
print(sorted(today ^ yesterday))
```

<!-- output: examples/ex06_set_ops.expected -->
```output
['Lina', 'Omar', 'Ravi', 'Sam']
['Lina', 'Sam']
['Omar']
['Omar', 'Ravi']
```

| Operator | Name | Gives | Here |
|---|---|---|---|
| `\|` | union | items in either set | everyone from both days |
| `&` | intersection | items in both sets | customers who came both days |
| `-` | difference | items in the first set only | new today |
| `^` | symmetric difference | items in one set, but not both | came on only one day |

The order matters for `-`: `today - yesterday` gives Omar, but `yesterday - today` gives Ravi.

## See the outcome

Here is Asha's loyalty report. It counts visits and different customers, and compares today with yesterday.

```python
# file: examples/ex07_loyalty.py
today = ["Omar", "Lina", "Omar", "Sam", "Omar", "Lina", "Omar"]
yesterday = {"Lina", "Ravi", "Sam"}
opens, closes = (8, 18)
customers = set(today)
print(f"Open {opens}:00 to {closes}:00")
print(f"Visits today: {len(today)}")
print(f"Different customers: {len(customers)}")
print("Both days:", sorted(customers & yesterday))
print("New today:", sorted(customers - yesterday))
print("Missed today:", sorted(yesterday - customers))
print("Omar came today:", "Omar" in customers)
```

<!-- output: examples/ex07_loyalty.expected -->
```output
Open 8:00 to 18:00
Visits today: 7
Different customers: 3
Both days: ['Lina', 'Sam']
New today: ['Omar']
Missed today: ['Ravi']
Omar came today: True
```

Each collection does one job. The list `today` keeps every visit, so line 7 counts 7. The set `customers` keeps each name once, so line 8 counts 3. The tuple on line 4 holds the fixed opening hours. Lines 9 to 11 compare the two days with `&` and `-`.

## Work with AI

The AI skill for this chapter is asking for trade-offs. "Which collection is best?" gets one answer, and you cannot judge it. "Compare a list, a tuple, a set and a dictionary for this job, with one strength and one weakness each" gets a comparison you can check against your task.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe the job and ask AI to compare the four collections, with a strength and a weakness for each. Then choose yourself. |
| Write | Write the code yourself, then ask AI to explain one line with a worked example. |
| Generate | Ask for code with your names and the exact output it prints. |
| Test | Ask for test cases with the expected result for each, including an empty list. Run them all. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask for a shorter version that prints exactly the same. Run both and compare every line. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha wants to welcome each customer the first time they come in today, in the order they arrive. She asked an AI assistant: "Write code that prints Welcome and the name the first time each customer in my list appears, then the number of new customers. Use an empty set called seen. Show the exact output." The AI said the program would print three welcomes and `New today: 3`, and gave this code.

```python
# file: examples/ai_welcome_flawed.py
today = ["Omar", "Lina", "Omar", "Sam"]
seen = {}
for name in today:
    if name not in seen:
        print(f"Welcome, {name}!")
        seen.add(name)
print(f"New today: {len(seen)}")
```

Asha ran it:

<!-- error: examples/ai_welcome_flawed.expected_error -->
```output
Welcome, Omar!
Traceback (most recent call last):
  File "ai_welcome_flawed.py", line 7, in <module>
    seen.add(name)
    ^^^^^^^^
AttributeError: 'dict' object has no attribute 'add'
```

Line 3 makes `{}`, an empty dictionary, not an empty set. A dictionary has no `add()`, so the program stops after the first welcome. The AI used the same curly brackets as a set and sounded sure. `set()` fixes it:

```python
# file: examples/ai_welcome_fixed.py
today = ["Omar", "Lina", "Omar", "Sam"]
seen = set()
for name in today:
    if name not in seen:
        print(f"Welcome, {name}!")
        seen.add(name)
print(f"New today: {len(seen)}")
```

<!-- output: examples/ai_welcome_fixed.expected -->
```output
Welcome, Omar!
Welcome, Lina!
Welcome, Sam!
New today: 3
```

Asha then tested three cases: a normal day, an empty day, and a day with a name typed as `omar `, with a small letter and a space. The second case welcomed Omar twice, so she cleaned each name with `strip().title()` and ran all three cases again. Later, the AI suggested `seen = set(today)` to remove the `add()` line. She tested it before she accepted it: the program printed no welcomes at all, because every name was already in `seen`. She kept her version.

## Common mistakes

**Mistake 1: changing a tuple.** A tuple cannot change after you make it.

```python
# file: examples/err01_change_tuple.py
hours = (8, 18)
print(hours)
hours[0] = 9
```

<!-- error: examples/err01_change_tuple.expected_error -->
```output
(8, 18)
Traceback (most recent call last):
  File "err01_change_tuple.py", line 4, in <module>
    hours[0] = 9
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

Fix: make a new tuple, `hours = (9, 18)`, or use a list if the values must change often.

**Mistake 2: a one-item tuple without a comma.** The comma makes a tuple, not the brackets.

```python
# file: examples/ex08_one_item.py
special = ("Tea")
print(type(special), len(special))
special = ("Tea",)
print(type(special), len(special))
```

<!-- output: examples/ex08_one_item.expected -->
```output
<class 'str'> 3
<class 'tuple'> 1
```

Line 2 makes the string `"Tea"`, so `len()` counts 3 letters. There is no error, which makes this mistake hard to see. Fix: put a comma after a single value, `("Tea",)`.

**Mistake 3: asking a set for a position.** A set has no order, so it has no positions.

```python
# file: examples/err02_set_index.py
customers = {"Omar", "Lina", "Sam"}
print(len(customers))
print(customers[0])
```

<!-- error: examples/err02_set_index.expected_error -->
```output
3
Traceback (most recent call last):
  File "err02_set_index.py", line 4, in <module>
    print(customers[0])
          ~~~~~~~~~^^^
TypeError: 'set' object is not subscriptable
```

"Not subscriptable" means you cannot use square brackets on it. Fix: use `in` to check a name, or `sorted(customers)` to get a list you can index.

**Mistake 4: the wrong number of names when you unpack.**

```python
# file: examples/err03_unpack_count.py
hours = (8, 12, 18)
print(len(hours))
opens, closes = hours
```

<!-- error: examples/err03_unpack_count.expected_error -->
```output
3
Traceback (most recent call last):
  File "err03_unpack_count.py", line 4, in <module>
    opens, closes = hours
    ^^^^^^^^^^^^^
ValueError: too many values to unpack (expected 2, got 3)
```

The tuple has 3 values, but line 4 has 2 names. Newer versions of Python also say how many values they got; older ones end after `expected 2`. Fix: write one name for each value, such as `opens, lunch, closes = hours`.

## Think beyond

1. Asha has a set of customers who ordered tea and a set of customers who ordered cake. Which operator gives the customers who ordered both, and which gives the customers who ordered tea but not cake? Write both and run them.
2. A dictionary key must not change. Could a tuple such as `(4, "window")` be a key for a table booking? Could a list? Try both, and read the error message if you get one.

## Recap

- A tuple is a fixed group of values in round brackets. You read it like a list, but you cannot change it.
- Unpacking puts each value into its own variable: `opens, closes = hours`. It also swaps two variables.
- A set keeps each item once and has no order. `set(visits)` removes repeats, and `in` checks it quickly.
- `{}` is an empty dictionary. An empty set is `set()`.
- `|`, `&`, `-` and `^` compare two sets. Print `sorted(...)` to get a fixed order.
- Ask AI to compare options with trade-offs, then choose and test it yourself.

You earned **100 XP** and the **Collector** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 14, you will turn loops that build a new list into one short line, called a comprehension, and learn when a normal loop is clearer.
