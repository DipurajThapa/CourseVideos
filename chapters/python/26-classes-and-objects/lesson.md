# Chapter 26: Classes and Objects: Modelling Real Things

> Quest: build the Corner Cafe's own types, a menu item and an order that carry their data and their rules. Then review an AI's class design before you trust it. Reward: 100 XP and the **Modeller** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Write a class with `__init__`, attributes and methods, and create several objects from it.
- Explain what `self` is, and why each object keeps its own data.
- Give an object a readable print form with `__str__`.
- Write a data class with `@dataclass`, and use `field(default_factory=list)` for a list.
- Ask an AI assistant to design a class, then test whether its design fits the problem.

## Why this matters

At the end of Chapter 25, Asha's report kept each sale as a pair of an item and an amount, and each day as a dictionary. The data lived in one place and the rules, such as the total, lived in separate functions. Nothing stopped her from typing `row["Amount"]` when the key was `"amount"`; the mistake appeared only when the program ran.

A **class** is a new type that you define yourself. It bundles data and the functions that work on that data. A menu item can carry its name and price, and know how to add tax to its own price. An order can keep its own list of items and know its own total.

Every large program is built from types like these. A shop has products and baskets, a game has players and levels, and an app has users and messages. AI assistants also design code in classes, so you need to read a class design and judge it.

## The idea

A class is the plan. An **object** is one thing made from that plan. Each object made from a class is also called an **instance** of the class.

```text
  class MenuItem          the plan: every menu item has a name and a price
     |
     +--> tea   = MenuItem("Tea", 3.5)     one object
     +--> cake  = MenuItem("Cake", 4.25)   another object, with its own data
```

| Word | Meaning | Example |
|---|---|---|
| class | The plan for a new type | `class MenuItem:` |
| object, instance | One thing made from the class | `tea = MenuItem("Tea", 3.5)` |
| attribute | A value stored in an object | `tea.price` |
| method | A function that belongs to the class | `tea.with_tax()` |
| `self` | The object a method is working on | `self.price` inside a method |

Think of the cafe's printed order slip. The blank slip is the class: it says that every order has a customer and a list of items. Each filled-in slip is an object with its own customer and items. The comparison stops working at one point: a paper slip cannot add up its own total, but an object can, with a method.

## Build it step by step

**Step 1: Your first class.** `__init__` is a special method that Python runs when you create an object. It stores the starting values as attributes on `self`.

```python
# file: examples/ex01_menu_item.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


tea = MenuItem("Tea", 3.5)
cake = MenuItem("Cake", 4.25)
print(tea.name, tea.price)
print(cake.name, cake.price)
```

<!-- output: examples/ex01_menu_item.expected -->
```output
Tea 3.5
Cake 4.25
```

`MenuItem("Tea", 3.5)` creates an object and runs `__init__` with `name` set to `"Tea"` and `price` set to `3.5`. Python passes the new object as `self` automatically, so you never write it in the call. `tea.name` reads the attribute with a dot.

**Step 2: Add methods.** A method is a function written inside the class. Its first parameter is always `self`, so it can use the object's own attributes.

```python
# file: examples/ex02_methods.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def with_tax(self):
        return round(self.price * 1.1, 2)

    def label(self):
        return f"{self.name}: {self.with_tax():.2f}"


tea = MenuItem("Tea", 3.5)
print(tea.with_tax())
print(tea.label())
```

<!-- output: examples/ex02_methods.expected -->
```output
3.85
Tea: 3.85
```

`tea.with_tax()` runs `with_tax` with `self` set to `tea`, so `self.price` is 3.5. A method can call another method through `self`, as `label()` does on line 11.

**Step 3: Each object keeps its own data.** Attributes set on `self` in `__init__` belong to one object only. In Chapter 17, each function call had its own local names; in the same way, each object has its own attributes.

```python
# file: examples/ex03_own_data.py
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add(self, item):
        self.items.append(item)


lina = Order("Lina")
omar = Order("Omar")
lina.add("Tea")
lina.add("Cake")
omar.add("Juice")
print(lina.customer, lina.items)
print(omar.customer, omar.items)
```

<!-- output: examples/ex03_own_data.expected -->
```output
Lina ['Tea', 'Cake']
Omar ['Juice']
```

Line 5 runs once for each new object, so Lina and Omar each get a new empty list. Adding a tea to Lina's order does not change Omar's order.

**Step 4: Objects that work together.** An order can hold menu item objects. Its total is worked out by a method each time you ask, so it is always up to date.

```python
# file: examples/ex04_order_total.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return round(sum([item.price for item in self.items]), 2)


order = Order("Lina")
order.add(MenuItem("Tea", 3.5))
print(order.total())
order.add(MenuItem("Cake", 4.25))
print(order.total())
```

<!-- output: examples/ex04_order_total.expected -->
```output
3.5
7.75
```

Line 17 is a list comprehension from Chapter 14: it collects the price of every item, and `sum()` adds them. The order does not store its total. If it did, the stored number would be wrong after the next `add()`.

**Step 5: A readable print form.** Printing an object of your own class shows its type and a memory address, which changes from run to run.

```python
# illustrative
print(tea)   # <__main__.MenuItem object at 0x7f3a2c1b9d30>
```

The special method `__str__` returns the text that `print()` and f-strings show for the object.

```python
# file: examples/ex05_str.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price:.2f})"


tea = MenuItem("Tea", 3.5)
print(tea)
print(f"Today: {tea}")
```

<!-- output: examples/ex05_str.expected -->
```output
Tea (3.50)
Today: Tea (3.50)
```

Special methods such as `__init__` and `__str__` have two underscores on each side. You write them, and Python calls them for you at the right moment.

**Step 6: Data classes.** Many classes only store a few values. The `dataclasses` module writes `__init__`, a print form and `==` for you. You list the attributes with a type after each name.

```python
# file: examples/ex06_dataclass.py
from dataclasses import dataclass


@dataclass
class MenuItem:
    name: str
    price: float


tea = MenuItem("Tea", 3.5)
print(tea)
print(tea == MenuItem("Tea", 3.5))
print(tea == MenuItem("Tea", 3.0))
```

<!-- output: examples/ex06_dataclass.expected -->
```output
MenuItem(name='Tea', price=3.5)
True
False
```

`==` on two data class objects compares their values, attribute by attribute. A list attribute needs `field(default_factory=list)`, which makes a new empty list for each object. Chapter 17 showed why a list as a default value is a trap, and a data class refuses it.

```python
# file: examples/ex07_list_error.py
from dataclasses import dataclass


@dataclass
class Order:
    customer: str
    items: list = []
```

<!-- error: examples/ex07_list_error.expected_error -->
```output
Traceback (most recent call last):
  File "ex07_list_error.py", line 5, in <module>
    @dataclass
     ^^^^^^^^^
  ...
ValueError: mutable default <class 'list'> for field items is not allowed: use default_factory
```

With `field(default_factory=list)`, each order gets its own list.

```python
# file: examples/ex07_list_field.py
from dataclasses import dataclass, field


@dataclass
class Order:
    customer: str
    items: list = field(default_factory=list)


lina = Order("Lina")
omar = Order("Omar")
lina.items.append("Tea")
print(lina)
print(omar)
```

<!-- output: examples/ex07_list_field.expected -->
```output
Order(customer='Lina', items=['Tea'])
Order(customer='Omar', items=[])
```

## See the outcome

Here is Asha's order receipt, built from two data classes. The order holds menu items, and its total is a method.

```python
# file: examples/ex08_order_receipt.py
from dataclasses import dataclass, field


@dataclass
class MenuItem:
    name: str
    price: float


@dataclass
class Order:
    customer: str
    items: list = field(default_factory=list)

    def add(self, item):
        self.items.append(item)

    def total(self):
        return round(sum([item.price for item in self.items]), 2)


order = Order("Lina")
order.add(MenuItem("Tea", 3.5))
order.add(MenuItem("Cake", 4.25))
order.add(MenuItem("Tea", 3.5))
print(f"Order for {order.customer}")
for item in order.items:
    print(f"{item.name:<8}{item.price:>6.2f}")
print(f"{'Total':<8}{order.total():>6.2f}")
```

<!-- output: examples/ex08_order_receipt.expected -->
```output
Order for Lina
Tea       3.50
Cake      4.25
Tea       3.50
Total    11.25
```

Lines 5 to 8 describe a menu item. Lines 11 to 20 describe an order: a customer, its own list of items, a method that adds an item and a method that works out the total. Lines 23 to 30 create one order, add three items and print the receipt. The format codes `<8` and `>6.2f` from Chapter 3 line up the columns.

## Work with AI

The AI skill for this chapter is asking an AI assistant to design a class, then reviewing whether the design fits the problem. A class design is a set of choices: which data each object stores, and which jobs its methods do. Test each choice with real cases before you accept it.

Never paste private data into an AI tool. A real list of customers and their visits is private, so use made-up names.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Describe the thing to model and ask for attributes and methods only, with no code. Check that each method has one job. |
| Write | Write your own small class first, then ask the AI to predict what it prints. |
| Generate | Ask for one new method with an exact example result. Check whether it stores a value that could go stale. |
| Test | Write cases with expected results, including an object created with data already in it, and run every case. |
| Debug | Paste the code and the full error report. Ask for the cause before the fix. |
| Improve | Ask for one improvement, then test it with two objects and run every case again. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha wanted a loyalty card: one stamp for each drink, and one free tea for every 10 stamps. She wrote the start of the class herself.

```python
# file: examples/ai_mine.py
class LoyaltyCard:
    def __init__(self, customer, stamps=0):
        self.customer = customer
        self.stamps = stamps

    def add_stamp(self):
        self.stamps += 1


card = LoyaltyCard("Lina")
card.add_stamp()
card.add_stamp()
print(card.customer, card.stamps)
```

<!-- output: examples/ai_mine.expected -->
```output
Lina 2
```

Then she asked: "Add free teas to my LoyaltyCard class. A customer gets one free tea for every 10 stamps. Tell me what a card shows after 25 stamps." The AI answered with this class and said that after 25 stamps the card has 2 free teas.

```python
# file: examples/card_ai.py
class LoyaltyCard:
    def __init__(self, customer, stamps=0):
        self.customer = customer
        self.stamps = stamps
        self.free_teas = 0

    def add_stamp(self):
        self.stamps += 1
        if self.stamps == 10:
            self.free_teas += 1
```

Asha ran it with 25 stamps.

```python
# file: examples/ai_generate_run.py
from card_ai import LoyaltyCard

card = LoyaltyCard("Lina")
for cup in range(25):
    card.add_stamp()
print(card.stamps, card.free_teas)
```

<!-- output: examples/ai_generate_run.expected -->
```output
25 1
```

The AI was wrong, and it sounded sure. Lines 10 and 11 add a free tea only when the stamps are exactly 10, so stamp 20 never counts. Line 6 stores the free teas as a number, so a card that starts with old stamps begins with 0 free teas. Asha's test cases show both problems.

```python
# file: examples/ai_cases_flawed.py
from card_ai import LoyaltyCard

cases = [("No stamps", 0, 0, 0), ("Nine stamps", 0, 9, 0),
         ("Ten stamps", 0, 10, 1), ("25 stamps", 0, 25, 2),
         ("Old card, 12", 12, 0, 1)]
for name, start, cups, expected in cases:
    card = LoyaltyCard("Test", start)
    for cup in range(cups):
        card.add_stamp()
    got = card.free_teas
    result = "pass" if got == expected else "FAIL"
    print(f"{name}: expected {expected}, got {got} {result}")
```

<!-- output: examples/ai_cases_flawed.expected -->
```output
No stamps: expected 0, got 0 pass
Nine stamps: expected 0, got 0 pass
Ten stamps: expected 1, got 1 pass
25 stamps: expected 2, got 1 FAIL
Old card, 12: expected 1, got 0 FAIL
```

The fix is a design change, not a bigger `if`. The number of free teas can always be worked out from the stamps, so a method computes it instead of storing it.

```python
# file: examples/card_fixed.py
class LoyaltyCard:
    def __init__(self, customer, stamps=0):
        self.customer = customer
        self.stamps = stamps

    def add_stamp(self):
        self.stamps += 1

    def free_teas(self):
        return self.stamps // 10
```

Her cases, run again on the fixed class (with `card.free_teas()` called as a method), all pass.

<!-- output: examples/ai_cases_fixed.expected -->
```output
No stamps: expected 0, got 0 pass
Nine stamps: expected 0, got 0 pass
Ten stamps: expected 1, got 1 pass
25 stamps: expected 2, got 2 pass
Old card, 12: expected 1, got 1 pass
```

A quick review question catches this kind of design flaw. If a value can be worked out from other attributes, store those attributes and compute the value in a method.

Later, the AI suggested a list of every drink stamped, written as `history = []` directly in the class instead of in `__init__`. Asha tested it with two cards.

```python
# file: examples/ai_history_shared.py
from card_shared import LoyaltyCard

lina = LoyaltyCard("Lina")
omar = LoyaltyCard("Omar")
lina.add_stamp("Latte")
print(lina.customer, lina.history)
print(omar.customer, omar.history)
```

<!-- output: examples/ai_history_shared.expected -->
```output
Lina ['Latte']
Omar ['Latte']
```

A list written directly in the class body belongs to the class, so every card shares it. Asha moved `self.history = []` into `__init__` (see `card_final.py`) and ran her tests again.

```python
# file: examples/test_loyalty.py
from card_final import LoyaltyCard


def stamped(cups, start=0):
    card = LoyaltyCard("Test", start)
    for cup in range(cups):
        card.add_stamp()
    return card


def test_nine_stamps():
    assert stamped(9).free_teas() == 0


def test_ten_stamps():
    assert stamped(10).free_teas() == 1


def test_25_stamps():
    assert stamped(25).free_teas() == 2


def test_old_card():
    assert stamped(0, start=12).free_teas() == 1


def test_each_card_has_its_own_history():
    lina = LoyaltyCard("Lina")
    omar = LoyaltyCard("Omar")
    lina.add_stamp("Latte")
    assert omar.history == []
```

<!-- output: examples/test_loyalty.expected -->
```output
.....                                            [100%]
5 passed in 0.01s
```

## Common mistakes

**Mistake 1: forgetting `self` in a method.** Python passes the object as the first argument, so a method needs a parameter to receive it.

```python
# file: examples/err01_no_self.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def with_tax():
        return round(self.price * 1.1, 2)


tea = MenuItem("Tea", 3.5)
print(tea.with_tax())
```

<!-- error: examples/err01_no_self.expected_error -->
```output
Traceback (most recent call last):
  File "err01_no_self.py", line 12, in <module>
    print(tea.with_tax())
          ~~~~~~~~~~~~^^
TypeError: MenuItem.with_tax() takes 0 positional arguments but 1 was given
```

Fix: write `def with_tax(self):`. "Takes 0 positional arguments but 1 was given" means the method has no parameter for the object that Python passed.

**Mistake 2: forgetting the brackets when you create an object.**

```python
# file: examples/err02_no_brackets.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


tea = MenuItem
print(tea.price)
```

<!-- error: examples/err02_no_brackets.expected_error -->
```output
Traceback (most recent call last):
  File "err02_no_brackets.py", line 9, in <module>
    print(tea.price)
          ^^^^^^^^^
AttributeError: type object 'MenuItem' has no attribute 'price'
```

Fix: `tea = MenuItem("Tea", 3.5)`. Without brackets, `tea` is the class itself, the plan, which has no price of its own. "Type object" in the message is the clue.

**Mistake 3: a spelling mistake in an attribute name.**

```python
# file: examples/err03_attribute_typo.py
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


tea = MenuItem("Tea", 3.5)
print(tea.prcie)
```

<!-- error: examples/err03_attribute_typo.expected_error -->
```output
Traceback (most recent call last):
  File "err03_attribute_typo.py", line 9, in <module>
    print(tea.prcie)
          ^^^^^^^^^
AttributeError: 'MenuItem' object has no attribute 'prcie'. Did you mean '.price' instead of '.prcie'?
```

Fix: spell the attribute as `__init__` created it, `price`. Newer versions of Python also suggest the closest name, and the exact wording of the suggestion differs between versions.

**Mistake 4: a list in the class body.** This mistake gives no error, which makes it worse.

```python
# file: examples/err04_shared_list.py
class Order:
    items = []

    def __init__(self, customer):
        self.customer = customer

    def add(self, item):
        self.items.append(item)


lina = Order("Lina")
omar = Order("Omar")
lina.add("Tea")
print(omar.customer, omar.items)
```

<!-- output: examples/err04_shared_list.expected -->
```output
Omar ['Tea']
```

Omar never ordered a tea, but his list shows one. Line 3 creates one list for the whole class, shared by every object. Fix: create the list in `__init__` with `self.items = []`, or use `field(default_factory=list)` in a data class.

## Think beyond

1. Asha's cafe has tables, and each table has several orders. Design a `Table` class: which attributes does it store, and which methods does it need? Which value should be a method instead of a stored number?
2. Two data class objects with the same values are equal with `==`. Are two objects of a normal class, such as `MenuItem("Tea", 3.5)` from Step 1, equal when their values are the same? Predict, then test it.

## Recap

- A class is the plan for a new type; an object is one thing made from it.
- `__init__` stores the starting values as attributes on `self`. Methods are functions inside the class, and `self` is the object they work on.
- Attributes set in `__init__` belong to one object. A list in the class body is shared by every object.
- `__str__` gives an object a readable print form.
- `@dataclass` writes `__init__`, a print form and `==` for you. A list attribute needs `field(default_factory=list)`.
- Compute a value that depends on other attributes in a method, so it never goes stale. Test every AI class design with real cases.

You earned **100 XP** and the **Modeller** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 27, you will read code that someone else wrote, such as an AI assistant, and improve it safely with tests.
