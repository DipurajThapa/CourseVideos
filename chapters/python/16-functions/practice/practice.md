# Practice: Chapter 16

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: A thank-you card

**Goal:** Write a function `card(name)` that prints two lines: `Dear <name>,` and `Thank you for visiting the Corner Cafe.` Call it for Omar and for Lina.

**Expected output:**
```text
Dear Omar,
Thank you for visiting the Corner Cafe.
Dear Lina,
Thank you for visiting the Corner Cafe.
```

**Hint:** Put `name` inside the brackets after `def card`. Indent both `print()` lines under the `def` line.

**AI variant:** Ask an AI assistant to explain the difference between the parameter `name` and the argument `"Omar"` in your code. Check that it names the right line for each.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Double it

**Goal:** Write a function `double(number)` that returns the number times 2. Print `double(4)`, `double(2.5)` and `double(4) + double(1)`.

**Expected output:**
```text
8
5.0
10
```

**Hint:** Use `return`, not `print()`, inside the function. Only a returned value can be added to another one.

**AI variant:** Ask an AI assistant to predict all three lines before you run the code. Check its answer for `5.0`: is it a `float`?

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Fix the None

**Goal:** This function prints the bill with a 15 percent tip, so `bill + 5` fails:

```python
# illustrative
def with_tip(total):
    print(round(total * 1.15, 2))
```

Rewrite it so that it returns the value. Then store `with_tip(20.0)` in `bill`, and print `bill` and `bill + 5`.

**Expected output:**
```text
23.0
28.0
```

**Hint:** Replace `print(` with `return ` and remove the extra closing bracket.

**AI variant:** Show an AI assistant the old function and the error `unsupported operand type(s) for +: 'NoneType' and 'int'`. Ask for the cause before the fix. Did it say "the function returns None"?

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Change for a note

**Goal:** Write `change(paid, cost)` with a docstring. It returns the change, rounded to cents. Print the change for 10.0 and 7.25, for 20.0 and 11.28, and for 5.0 and 5.0.

**Expected output:**
```text
2.75
8.72
0.0
```

**Hint:** `round(paid - cost, 2)`. Keep the parameters in the order `paid, cost`, and pass the arguments in the same order.

**AI variant:** Ask an AI assistant for two more test cases, one with a zero result. Predict each result, then run them.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Minutes to hours

**Goal:** Write `hours_text(minutes)` that returns text such as `2 h 15 min`. Print the result for 135, 60 and 45 minutes.

**Expected output:**
```text
2 h 15 min
1 h 0 min
0 h 45 min
```

**Hint:** Use `//` for the hours and the remainder operator `%` for the minutes, inside an f-string.

**AI variant:** Ask an AI assistant to write this function from your specification: the name, the parameter, the return value and the three examples. Run your three examples on its code.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Menu lines

**Goal:** Write `menu_line(name, price)` that returns one line with the name on the left in 12 characters and the price on the right in 6 characters, with 2 decimal places. Use it in a loop over a list of tuples.

**Expected output:**
```text
Tea           3.50
Coffee        4.00
Carrot cake   4.25
```

**Hint:** `f"{name:<12}{price:>6.2f}"`. Unpack each tuple in the `for` line: `for name, price in menu:`.

**AI variant:** Ask an AI assistant whether `menu_line` should print or return. Check its reason against what you need: the loop prints, the function only builds the text.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Average with an empty day

**Goal:** Write `average(values)` that returns the average rounded to cents, or `0.0` for an empty list. Then write `report(day, sales)` that calls `average()` and prints one line. Report Monday with three sales and Sunday with none.

**Expected output:**
```text
Monday: average sale 3.42
Sunday: average sale 0.00
```

**Hint:** Check `len(values) == 0` first and return `0.0` straight away. A function stops at the first `return` it reaches.

**AI variant:** Ask an AI assistant to write `average()` from your specification. Test it with the empty list. Does it crash with a `ZeroDivisionError`?

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's member price

**Goal:** An AI assistant wrote this function for a 10 percent member discount and said it returns the new price:

```python
# illustrative
def member_price(is_member, price):
    if is_member:
        print(price * 0.9)
    return price
```

It has two problems: it prints instead of returning the discount, and its parameters are in a different order from the calls Asha writes, `member_price(4.0, True)`. Fix both, round to cents, and print three checks.

**Expected output:**
```text
3.6 True
4.0 True
2.48 True
```

**Hint:** Put `price` first in the `def` line. Return `round(price * 0.9, 2)` for a member and `price` for everyone else.

**AI variant:** Show the AI its function and your three checks. Ask it to explain the cause of each failure before the fix. Did it find both problems?

**Solution:** [solutions/task8.py](solutions/task8.py)
