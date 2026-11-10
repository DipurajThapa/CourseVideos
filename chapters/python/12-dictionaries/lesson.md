# Chapter 12: Dictionaries: Looking Things Up by Name

> Quest: store values under names, find any value by its name, and count and report with a dictionary. Reward: 100 XP and the **Key Master** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write a dictionary and read a value with its key.
- Add, change and remove items in a dictionary.
- Check for a key with `in`, and use `get()` with a default value for keys that may be missing.
- Go through a dictionary with `items()` and count things with a dictionary.
- Choose between a list and a dictionary for a task, and challenge an AI's choice.

## Why this matters

In Chapter 11, a list kept many values in order, and you found each value by its position. But at the Corner Cafe, nobody asks for "item number 2". A customer asks for "cake". To find the price of cake in a list, you must first know where cake is.

A **dictionary** stores each value under a name, called a **key**. You ask for the key, and Python gives you the value. The price of cake is `menu["cake"]`, wherever cake is in the menu.

Real programs use this all the time. A phone keeps each contact's number under a name. A shop finds a product by its code. A game keeps each player's score under the player's name.

## The idea

A dictionary is written with curly brackets. Each item is a **key**, a colon and a **value**, and commas separate the items.

```text
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}

   key         value
  "tea"   -->   3.5
  "coffee" -->  4.0
  "cake"   -->  4.25

menu["cake"]  gives  4.25
```

Each key appears only once, and the keys are often strings. A value can be any type, even a list or another dictionary. Python keeps the items in the order you added them.

Think of the price board behind the counter. You look up a name and read the price next to it. Unlike a price board, a dictionary cannot show the same name twice: if you add a key that already exists, the new value replaces the old one.

## Build it step by step

**Step 1: Make a dictionary and read values.** Asha writes part of the Corner Cafe menu.

```python
# file: examples/ex01_menu.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
print(menu)
print(menu["tea"])
print(menu["cake"])
print(len(menu))
```

<!-- output: examples/ex01_menu.expected -->
```output
{'tea': 3.5, 'coffee': 4.0, 'cake': 4.25}
3.5
4.25
3
```

`menu["tea"]` uses square brackets with a key, not an index. `len()` counts the items: three key and value pairs.

**Step 2: Add, change and remove items.** A dictionary is mutable, like a list.

```python
# file: examples/ex02_change_menu.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
menu["scone"] = 2.75
print(menu)
menu["tea"] = 3.75
print(menu)
del menu["coffee"]
print(menu)
price = menu.pop("cake")
print(price, menu)
```

<!-- output: examples/ex02_change_menu.expected -->
```output
{'tea': 3.5, 'coffee': 4.0, 'cake': 4.25, 'scone': 2.75}
{'tea': 3.75, 'coffee': 4.0, 'cake': 4.25, 'scone': 2.75}
{'tea': 3.75, 'cake': 4.25, 'scone': 2.75}
4.25 {'tea': 3.75, 'scone': 2.75}
```

| Code | What it does |
|---|---|
| `menu["scone"] = 2.75` | Adds the key, because `"scone"` is new. |
| `menu["tea"] = 3.75` | Replaces the value, because `"tea"` already exists. |
| `del menu["coffee"]` | Removes the key and its value. |
| `menu.pop("cake")` | Removes the key and gives back its value. |

The same line, `menu[key] = value`, adds or changes an item. It adds when the key is new and changes the value when the key exists.

**Step 3: Check before you look up.** Asking for a key that is not there stops the program, so Python gives you two safe ways to check.

```python
# file: examples/ex03_lookups.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
print("tea" in menu)
print("juice" in menu)
print(3.5 in menu)
print(menu.get("cake"))
print(menu.get("juice"))
print(menu.get("juice", 0))
```

<!-- output: examples/ex03_lookups.expected -->
```output
True
False
False
4.25
None
0
```

`in` checks the keys only. Line 5 gives `False` because 3.5 is a value, not a key. `get()` gives the value if the key exists. If it does not, `get()` gives `None`, or the **default value** you put second, here `0`.

**Step 4: Go through a dictionary.** A `for` loop over a dictionary gives its keys. `items()` gives each key together with its value.

```python
# file: examples/ex04_loop_menu.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
for name in menu:
    print(name)
for name, price in menu.items():
    print(f"{name:<8}{price:>6.2f}")
print(list(menu.keys()))
print(list(menu.values()))
print(sum(menu.values()))
```

<!-- output: examples/ex04_loop_menu.expected -->
```output
tea
coffee
cake
tea       3.50
coffee    4.00
cake      4.25
['tea', 'coffee', 'cake']
[3.5, 4.0, 4.25]
11.75
```

Line 5 takes two loop variables, `name` and `price`, from each item. `keys()` and `values()` give the keys and the values on their own. `list()` turns them into lists so they print clearly, and `sum()` adds the values.

**Step 5: Count with a dictionary.** Asha wants to know how many of each item she sold today. She starts with an empty dictionary, `{}`.

```python
# file: examples/ex05_count_sales.py
sold = ["tea", "cake", "tea", "scone", "tea", "cake"]
counts = {}
for item in sold:
    counts[item] = counts.get(item, 0) + 1
print(counts)
print(counts["tea"])
```

<!-- output: examples/ex05_count_sales.expected -->
```output
{'tea': 3, 'cake': 2, 'scone': 1}
3
```

Line 5 does the counting. `counts.get(item, 0)` gives the count so far, or 0 the first time an item appears. Python works out the right side first, adds 1, and stores the new count under the item's name.

**Step 6: Put a dictionary inside a dictionary.** A value can be another dictionary. This is called **nested data**.

```python
# file: examples/ex06_nested_menu.py
menu = {
    "tea": {"price": 3.5, "vegan": True},
    "cake": {"price": 4.25, "vegan": False},
    "scone": {"price": 2.75, "vegan": True},
}
print(menu["cake"]["price"])
for name, info in menu.items():
    if info["vegan"]:
        print(f"{name} is vegan, {info['price']:.2f}")
```

<!-- output: examples/ex06_nested_menu.expected -->
```output
4.25
tea is vegan, 3.50
scone is vegan, 2.75
```

`menu["cake"]` gives the inner dictionary, and `["price"]` reads one value from it. Inside the f-string on line 9, the key uses single quotation marks, because the f-string itself uses double ones.

## See the outcome

Here is Asha's order taker. The customer types each item by name, the program counts the items in a dictionary, and it prints a receipt. In the expected output, the text after each question is what the customer typed.

```python
# file: examples/ex07_order_by_name.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25, "sandwich": 6.0}
order = {}
while True:
    item = input("Item (or done): ").strip().lower()
    if item == "done":
        break
    if item in menu:
        order[item] = order.get(item, 0) + 1
    else:
        print(f"Sorry, no {item} today.")
total = 0
for item, count in order.items():
    cost = count * menu[item]
    total += cost
    print(f"{count} x {item:<10}{cost:>6.2f}")
print(f"{'Total':<14}{total:>6.2f}")
```

<!-- output: examples/ex07_order_by_name.expected -->
```output
Item (or done): Tea
Item (or done): cake
Item (or done): juice
Sorry, no juice today.
Item (or done):  tea
Item (or done): done
2 x tea         7.00
1 x cake        4.25
Total          11.25
```

Line 5 removes spaces and capital letters, so `Tea` and ` tea` both find `"tea"`. Line 8 checks the menu before the program uses `menu[item]`, so `juice` gets a polite message and no error. Lines 13 to 16 go through the order with `items()` and add up the total.

## Work with AI

The AI skill for this chapter is challenging a design. When you ask AI how to store your data, it gives you one structure. Ask why, and compare it with the job the data must do. If you will look values up by name, a dictionary usually fits better than a list.

The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe your data and how you will use it. Ask AI to design a structure, then challenge its choice. |
| Write | Write the code yourself, then ask AI to explain one line with a worked example. |
| Generate | Ask for code with your dictionary and the exact output it prints. |
| Test | Ask for test cases with the expected result for each, including a key that is missing. Run them all. |
| Debug | Paste the code and the full error. Ask for the cause before the fix. |
| Improve | Ask for a clearer version that prints exactly the same. Run both and compare every line. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha keeps the cafe's stock of cakes, scones and sandwiches in a dictionary. She asked an AI assistant: "Here is my stock and today's sales. Write code that takes the sales away from the stock and prints how many of each item are left. Show the exact output." The AI said the output would start with `Left: 4`, and gave this code.

```python
# file: examples/ai_stock_flawed.py
stock = {"cake": 6, "scone": 4, "sandwich": 5}
sold = ["cake", "scone", "cake"]
for item in sold:
    stock[item] = stock[item] - 1
for count in stock:
    print(f"Left: {count}")
```

Asha ran it:

<!-- output: examples/ai_stock_flawed.expected -->
```output
Left: cake
Left: scone
Left: sandwich
```

The program printed the names, not the numbers. A `for` loop over a dictionary gives its keys, so `count` held `"cake"`, `"scone"` and `"sandwich"`. The variable name `count` does not change what Python puts in it. `items()` gives each name with its number:

```python
# file: examples/ai_stock_fixed.py
stock = {"cake": 6, "scone": 4, "sandwich": 5}
sold = ["cake", "scone", "cake"]
for item in sold:
    stock[item] = stock[item] - 1
for item, count in stock.items():
    print(f"{item}: {count} left")
```

<!-- output: examples/ai_stock_fixed.expected -->
```output
cake: 4 left
scone: 3 left
sandwich: 5 left
```

Asha then tested three cases: no sales, selling the last cake, and a sale of a muffin, which is not in the stock. The muffin stopped the program with `KeyError: 'muffin'`. She added an `if item in stock:` check and ran all three cases again. Later, the AI suggested `stock.get(item, 0) - 1` to make the code shorter. It added a new line to the output, `muffin: -1 left`, so Asha kept her check.

## Common mistakes

**Mistake 1: a key that is not there.** Python only knows the keys you created.

```python
# file: examples/err01_missing_key.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
print(menu["tea"])
print(menu["juice"])
```

<!-- error: examples/err01_missing_key.expected_error -->
```output
3.5
Traceback (most recent call last):
  File "err01_missing_key.py", line 4, in <module>
    print(menu["juice"])
          ~~~~^^^^^^^^^
KeyError: 'juice'
```

Fix: check first with `if "juice" in menu:`, or use `menu.get("juice", 0)` when a default value makes sense.

**Mistake 2: a capital letter, and `get()` gives `None`.** Keys are case-sensitive, so `"Tea"` and `"tea"` are different keys.

```python
# file: examples/err02_get_none.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
price = menu.get("Tea")
print(price)
total = price * 2
```

<!-- error: examples/err02_get_none.expected_error -->
```output
None
Traceback (most recent call last):
  File "err02_get_none.py", line 5, in <module>
    total = price * 2
            ~~~~~~^~~
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

`get()` did not stop the program on line 3. It gave `None`, line 4 printed it, and the program stopped on line 5, when it tried to multiply `None`. Fix: use `.lower()` on names before you look them up, and check the result of `get()` before you calculate with it.

**Mistake 3: the same key twice.** A dictionary keeps one value per key, so a repeated key replaces the earlier value without any error.

```python
# file: examples/ex08_duplicate_key.py
menu = {"tea": 3.5, "cake": 4.25, "tea": 3.0}
print(menu)
print(len(menu))
```

<!-- output: examples/ex08_duplicate_key.expected -->
```output
{'tea': 3.0, 'cake': 4.25}
2
```

The first price of tea, 3.5, is gone, and the dictionary has 2 items, not 3. Fix: check that every key in a dictionary is different.

**Mistake 4: looping over a dictionary and expecting values.** This is the AI's mistake from the pair moment, in a new place.

```python
# file: examples/err03_loop_keys.py
menu = {"tea": 3.5, "coffee": 4.0, "cake": 4.25}
total = 0
for price in menu:
    total += price
print(total)
```

<!-- error: examples/err03_loop_keys.expected_error -->
```output
Traceback (most recent call last):
  File "err03_loop_keys.py", line 5, in <module>
    total += price
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

`price` holds the key `"tea"`, a string, and Python cannot add a string to a number. Fix: write `for price in menu.values():`, or use `items()` when you need both.

## Think beyond

1. Two customers order at the same table. How could a dictionary with table numbers as keys and lists of items as values keep each table's order? Write one and print the order for table 4.
2. In the order taker, a customer types `cakes`. The program says "Sorry, no cakes today." How could you also accept the plural, and is it worth it?

## Recap

- A dictionary stores values under keys: `menu["tea"]` gives the value for the key `"tea"`.
- `menu[key] = value` adds a new key or changes an existing one. `del` and `pop()` remove a key.
- `in` checks the keys. `get()` gives the value, or `None`, or the default you give it.
- A `for` loop over a dictionary gives its keys. `items()` gives each key with its value.
- `counts[item] = counts.get(item, 0) + 1` counts things by name.
- Ask AI to design your data, then challenge its choice against how you will use the data.

You earned **100 XP** and the **Key Master** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 13, you will meet tuples, fixed groups of values, and sets, which keep each item only once, such as every different customer of the day.
