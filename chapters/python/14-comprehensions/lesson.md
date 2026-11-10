# Chapter 14: Comprehensions: Transforming Data in One Line

> Quest: turn loops that build a new list or dictionary into one short line, filter items as you go, and decide when a normal loop is clearer. Reward: 100 XP and the **Transformer** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write a list comprehension that makes a new list from an old one.
- Add an `if` at the end of a comprehension to keep only some items.
- Write a dictionary comprehension that makes a new dictionary.
- Explain when a normal loop is clearer than a comprehension.
- Ask AI to rewrite a loop as a comprehension, then prove the output stayed the same.

## Why this matters

At the end of Chapter 13, Asha wanted a list of every price with tax added. She needed four lines: an empty list, a loop, the new price, and `append()`. She writes this pattern again and again: new prices, names in capital letters, only the vegan items.

A **comprehension** is a short way to build a new list or dictionary from another collection, in one line. It says what you want, not how to collect it step by step. Data tools, reports and websites use comprehensions all the time to clean and reshape data.

A comprehension does not replace every loop. When each item needs several steps or a `print()`, a normal loop is easier to read. Part of this chapter is learning to choose.

## The idea

A list comprehension has three parts inside square brackets. Read the middle part first, then the left part.

```text
   [ round(price * 1.1, 2)   for price in prices    if price < 4 ]
     |                       |                      |
     the new value           the loop               an optional filter
     (made for each item)    (same as a for loop)   (keep the item only if True)
```

It does the same job as this loop. It needs no empty list and no `append()`.

```text
   result = []
   for price in prices:
       if price < 4:
           result.append(round(price * 1.1, 2))
```

Think of a comprehension as a recipe card for a new list: "for each price, if it is under 4, write down the price with tax". Unlike a recipe card, it cannot do other jobs on the way, such as printing or adding to a total.

## Build it step by step

**Step 1: The loop you already know.** Here is Asha's loop from the end of Chapter 13. It adds 10 percent tax to every price.

```python
# file: examples/ex01_tax_loop.py
prices = [3.5, 4.0, 4.25, 2.75]
with_tax = []
for price in prices:
    with_tax.append(round(price * 1.1, 2))
print(with_tax)
```

<!-- output: examples/ex01_tax_loop.expected -->
```output
[3.85, 4.4, 4.68, 3.03]
```

Multiplying by 1.1 adds 10 percent. `round(..., 2)` keeps two decimal places, as in Chapter 2.

**Step 2: The same list in one line.** The comprehension puts the new value first, then the loop.

```python
# file: examples/ex02_tax_comp.py
prices = [3.5, 4.0, 4.25, 2.75]
with_tax = [round(price * 1.1, 2) for price in prices]
print(with_tax)
print(len(with_tax), len(prices))
```

<!-- output: examples/ex02_tax_comp.expected -->
```output
[3.85, 4.4, 4.68, 3.03]
4 4
```

The output is exactly the same as in Step 1. Without a filter, the new list has one item for each old item, so both lists have 4 items.

**Step 3: Transform text.** The new value can be any expression, such as a string method or `len()`.

```python
# file: examples/ex03_names.py
items = ["tea", "coffee", "carrot cake", "scone"]
titles = [item.title() for item in items]
lengths = [len(item) for item in items]
print(titles)
print(lengths)
print(items)
```

<!-- output: examples/ex03_names.expected -->
```output
['Tea', 'Coffee', 'Carrot Cake', 'Scone']
[3, 6, 11, 5]
['tea', 'coffee', 'carrot cake', 'scone']
```

A comprehension makes a new list. The old list, `items`, does not change.

**Step 4: Keep only some items.** An `if` at the end is a **filter**: an item goes into the new list only when the condition is `True`. You can also unpack tuples in the loop part, as in Chapter 13.

```python
# file: examples/ex04_filter.py
menu = [("Tea", 3.5, True),
        ("Coffee", 4.0, True),
        ("Carrot cake", 4.25, False),
        ("Scone", 2.75, False)]
vegan = [name for name, price, is_vegan in menu if is_vegan]
cheap = [name for name, price, is_vegan in menu if price < 4]
print(vegan)
print(cheap)
```

<!-- output: examples/ex04_filter.expected -->
```output
['Tea', 'Coffee']
['Tea', 'Scone']
```

Each tuple holds a name, a price and whether the item is vegan. Line 6 keeps the names of vegan items. Line 7 keeps the names of items under 4.

**Step 5: Filter or choose.** An `if` at the end filters, so the list can get shorter. An `if` with an `else` at the start chooses a value for every item, so the list keeps its length.

```python
# file: examples/ex05_if_else.py
prices = [3.5, 4.0, 4.25, 2.75]
under_4 = [price for price in prices if price < 4]
labels = ["snack" if price < 4 else "treat" for price in prices]
print(under_4)
print(labels)
```

<!-- output: examples/ex05_if_else.expected -->
```output
[3.5, 2.75]
['snack', 'treat', 'treat', 'snack']
```

`"snack" if price < 4 else "treat"` is one value that depends on a condition. It must have an `else`, because every item needs a value.

**Step 6: Build a dictionary.** Curly brackets with `key: value` make a **dictionary comprehension**.

```python
# file: examples/ex06_dict_comp.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25, "scone": 2.75}
with_tax = {name: round(price * 1.1, 2) for name, price in menu.items()}
print(with_tax)
print(with_tax["cake"])
print(menu["cake"])
```

<!-- output: examples/ex06_dict_comp.expected -->
```output
{'tea': 3.85, 'coffee': 4.4, 'cake': 4.68, 'scone': 3.03}
4.68
4.25
```

`menu.items()` gives each name and price, as in Chapter 12. The new dictionary keeps the same keys with new values, and `menu` does not change.

**Step 7: Know when a loop is clearer.** Today, items of 4 or more cost 0.50 less, get a label, are printed and are added to a total. That is four jobs for each item.

```python
# file: examples/ex07_loop_clearer.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25, "scone": 2.75}
total = 0
for name, price in menu.items():
    if price >= 4:
        price = price - 0.5
        name = name + " (offer)"
    print(f"{name:<16}{price:>6.2f}")
    total += price
print(f"{'Total':<16}{total:>6.2f}")
```

<!-- output: examples/ex07_loop_clearer.expected -->
```output
tea               3.50
coffee (offer)    3.50
cake (offer)      3.75
scone             2.75
Total            13.50
```

Use a comprehension when you build one new list or dictionary and nothing else. Use a normal loop when each item needs several steps, a `print()` or a running total.

## See the outcome

Asha's menu board shows every price with tax, the vegan items, and the items under 4.00 after tax. Three comprehensions do the work.

```python
# file: examples/ex08_menu_board.py
menu = [("Tea", 3.5, True),
        ("Coffee", 4.0, True),
        ("Carrot cake", 4.25, False),
        ("Scone", 2.75, False)]
board = {name: round(price * 1.1, 2) for name, price, is_vegan in menu}
vegan = [name for name, price, is_vegan in menu if is_vegan]
under_4 = [name for name, price in board.items() if price < 4]
for name, price in board.items():
    print(f"{name:<12}{price:>6.2f}")
print("Vegan:", vegan)
print("Under 4.00 with tax:", under_4)
```

<!-- output: examples/ex08_menu_board.expected -->
```output
Tea           3.85
Coffee        4.40
Carrot cake   4.68
Scone         3.03
Vegan: ['Tea', 'Coffee']
Under 4.00 with tax: ['Tea', 'Scone']
```

Line 6 builds a dictionary of prices with tax. Line 7 filters the vegan names. Line 8 filters the board, so it compares the prices with tax. The printing stays in a normal loop, because printing is not building a list.

## Work with AI

The AI skill for this chapter is safe refactoring. To **refactor** means to change how code is written without changing what it does. Ask AI to rewrite a loop as a comprehension, then prove that the output stayed the same: run both versions on the same data and compare every line.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Before any rewrite, ask AI to list what must stay exactly the same. |
| Write | Write the loop yourself. Ask AI to predict its output, then run it. |
| Generate | Ask AI to rewrite your loop as a comprehension and to say what it prints. |
| Test | Ask for test cases with expected results. Run your loop and the AI's line on each case. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask for a better version that prints the same. Run every case again before you accept it. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha wrote a loop that adds tax to the vegan items only. It prints `[3.85, 4.4]`. She asked an AI assistant: "Rewrite this loop as a list comprehension. Keep the output exactly the same, and tell me what it prints." The AI said the new line prints `[3.85, 4.4]`. Here is its code.

```python
# file: examples/ai_vegan_flawed.py
menu = [("Tea", 3.5, True),
        ("Coffee", 4.0, True),
        ("Carrot cake", 4.25, False),
        ("Scone", 2.75, False)]
taxed = [round(price * 1.1, 2) for name, price, vegan in menu]
print(taxed)
```

Asha ran it:

<!-- output: examples/ai_vegan_flawed.expected -->
```output
[3.85, 4.4, 4.68, 3.03]
```

The AI dropped the filter. Its line adds tax to every item, so the list has four prices instead of two. The AI sounded sure, and its prediction was wrong. Adding the filter at the end fixes it:

```python
# file: examples/ai_vegan_fixed.py
menu = [("Tea", 3.5, True),
        ("Coffee", 4.0, True),
        ("Carrot cake", 4.25, False),
        ("Scone", 2.75, False)]
taxed = [round(price * 1.1, 2) for name, price, vegan in menu if vegan]
print(taxed)
```

<!-- output: examples/ai_vegan_fixed.expected -->
```output
[3.85, 4.4]
```

Asha then ran her loop and the AI's line on three test cases. The fixed line passed all three. Later, the AI suggested curly brackets, "because a set is faster to search". She ran the cases again before she accepted it. Every case failed: the output became a set, and a set keeps a repeated price only once.

## Common mistakes

**Mistake 1: curly brackets instead of square brackets.** Curly brackets without a colon make a **set comprehension**. You get a set, which has no fixed order and keeps each value once.

```python
# file: examples/err01_braces.py
prices = [3.5, 3.5, 4.0, 2.75]
with_tax = {round(price * 1.1, 2) for price in prices}
print(with_tax)
print(type(with_tax))
print(len(with_tax), len(prices))
```

<!-- output: examples/err01_braces.expected -->
```output
{3.03, 3.85, 4.4}
<class 'set'>
3 4
```

There is no error, but one 3.85 is gone. Fix: use square brackets for a list, and curly brackets with `key: value` for a dictionary.

**Mistake 2: `else` after a filter.** A filter at the end cannot have an `else`.

```python
# file: examples/err02_else_at_end.py
prices = [3.5, 4.0, 4.25, 2.75]
labels = [price for price in prices if price < 4 else 0]
print(labels)
```

<!-- error: examples/err02_else_at_end.expected_error -->
```output
  File "err02_else_at_end.py", line 3
    labels = [price for price in prices if price < 4 else 0]
                                                     ^^^^
SyntaxError: invalid syntax
```

Fix: to choose a value for every item, move the condition to the start: `[price if price < 4 else 0 for price in prices]`. To keep only some items, remove the `else`.

**Mistake 3: a comprehension only to print.** A comprehension builds a list. If you only want to print, the list is useless.

```python
# file: examples/err03_print_comp.py
items = ["Tea", "Coffee", "Scone"]
result = [print(item) for item in items]
print(result)
```

<!-- output: examples/err03_print_comp.expected -->
```output
Tea
Coffee
Scone
[None, None, None]
```

`print()` gives back `None`, so the list holds three `None` values. Fix: use a normal `for` loop when the job is printing.

**Mistake 4: forgetting to round.** Prices with tax are `float` values, and some are stored with a tiny error, as you saw in Chapter 2.

```python
# file: examples/ex09_no_round.py
prices = [3.5, 4.0, 4.25, 2.75]
with_tax = [price * 1.1 for price in prices]
print(with_tax)
print([round(price, 2) for price in with_tax])
```

<!-- output: examples/ex09_no_round.expected -->
```output
[3.8500000000000005, 4.4, 4.675000000000001, 3.0250000000000004]
[3.85, 4.4, 4.68, 3.03]
```

Fix: round inside the comprehension, or format the price with `:.2f` when you print it.

## Think beyond

1. Asha has `orders = ["tea", "cake", "tea", "scone", "tea"]`. Write a comprehension that keeps only the teas, then use `len()` to count them. Could you count them without making a new list?
2. A comprehension can have two `for` parts, such as `[size + " " + drink for drink in drinks for size in sizes]`. Predict the order of the items for `drinks = ["tea", "coffee"]` and `sizes = ["small", "large"]`, then run it.

## Recap

- A list comprehension builds a new list in one line: the new value, then `for`, then an optional `if`.
- An `if` at the end filters items. A value with `if` and `else` at the start chooses a value for every item.
- `{key: value for ...}` builds a dictionary. Curly brackets without a colon build a set.
- A comprehension makes a new collection and leaves the old one unchanged.
- Use a normal loop when each item needs several steps, a `print()` or a running total.
- Ask AI to refactor, then run both versions on the same test cases and compare every line.

You earned **100 XP** and the **Transformer** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 15, Boss Level 3, you will combine lists, dictionaries, loops and decisions to build an expense tracker.
