# Practice: Chapter 14

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: Double portions

**Goal:** Start with `prices = [3.5, 4.0, 2.75]`. Use a list comprehension to make a new list where every price is doubled, and print it.

**Expected output:**
```text
[7.0, 8.0, 5.5]
```

**Hint:** Put the new value first: `price * 2`, then `for price in prices`.

**AI variant:** Ask an AI assistant to explain your comprehension word by word. Check that its explanation matches the order: new value, then the loop.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Shout the menu

**Goal:** Start with `items = ["tea", "coffee", "scone"]`. Make a list of the names in capital letters. Print the new list, then the old list to show that it did not change.

**Expected output:**
```text
['TEA', 'COFFEE', 'SCONE']
['tea', 'coffee', 'scone']
```

**Hint:** Use the string method `upper()` from Chapter 3 as the new value.

**AI variant:** Ask an AI assistant whether a comprehension changes the old list. Check its answer with your second `print()`.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Short names

**Goal:** Start with `items = ["Tea", "Coffee", "Scone", "Carrot cake"]`. Keep only the names with 5 letters or fewer. Print them, then how many you kept out of how many.

**Expected output:**
```text
['Tea', 'Scone']
2 of 4
```

**Hint:** Put `if len(item) <= 5` at the end of the comprehension.

**AI variant:** Ask an AI assistant for one more name that would test the limit of 5 letters exactly. Add it and predict the result before you run it.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Sale labels

**Goal:** Start with `prices = [3.5, 4.0, 4.25, 2.75]`. Items of 4 or more are on sale. Make a list with the label `sale` or `full price` for every price.

**Expected output:**
```text
['full price', 'sale', 'sale', 'full price']
```

**Hint:** Every item needs a label, so the condition goes at the start, with an `else`.

**AI variant:** Ask an AI assistant for test prices around the limit, such as 3.99 and 4.0. Predict each label, then run them.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Stock check

**Goal:** Start with `stock = {"tea": 40, "cake": 3, "scone": 0, "coffee": 25}`. Make a dictionary of only the items in stock, and a list of the names with fewer than 5 left. Print both.

**Expected output:**
```text
{'tea': 40, 'cake': 3, 'coffee': 25}
Order more: ['cake', 'scone']
```

**Hint:** Use `stock.items()` in both comprehensions, and a filter at the end of each.

**AI variant:** Ask an AI assistant to write the dictionary comprehension for you. Run both versions and compare every line of the output.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: From loop to one line

**Goal:** Start with `tips = [2.0, 0, 1.5, 0, 3.0]`. First write a loop that keeps the tips above 0. Then write the same list as a comprehension. Print both, check that they are equal with `==`, and print the total with `sum()`.

**Expected output:**
```text
[2.0, 1.5, 3.0]
[2.0, 1.5, 3.0]
Same: True
Total tips: 6.5
```

**Hint:** `print("Same:", real_tips == short_way)` prints `True` when both lists hold the same items in the same order.

**AI variant:** Ask an AI assistant to refactor your loop. Run its line next to your loop and check `Same: True`.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Vegan menu board

**Goal:** Start with the menu from the lesson's outcome. Build a dictionary where each name maps to its price with tax as text with two decimal places, plus ` V` for vegan items. Print one line per item, then the number of items.

**Expected output:**
```text
Tea         3.85 V
Coffee      4.40 V
Carrot cake 4.68
Scone       3.03
Items: 4
```

**Hint:** An f-string with `:.2f` makes the price text. `(" V" if is_vegan else "")` adds the mark or nothing.

**AI variant:** Ask an AI assistant for a shorter version. Run it, and check that every line of the output stays exactly the same.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Check the AI's refactor

**Goal:** Orders over 10 get 10 percent off. Asha's loop keeps those orders and rounds the new price. An AI rewrote it as `{round(order * 0.9, 2) for order in orders}`. Start with `orders = [12.5, 8.0, 15.25, 10.0, 22.0]`. Print the loop's list, the AI's result as a sorted list with whether it matches, and your fixed comprehension with whether it matches.

**Expected output:**
```text
Loop: [11.25, 13.72, 19.8]
AI: [7.2, 9.0, 11.25, 13.72, 19.8] same: False
Fixed: [11.25, 13.72, 19.8] same: True
```

**Hint:** The AI's line has two problems: the brackets, and a missing part at the end. Compare with `==`.

**AI variant:** Show the AI its own line and the real output. Ask it to explain the cause before the fix. Did it name both problems?

**Solution:** [solutions/task8.py](solutions/task8.py)
