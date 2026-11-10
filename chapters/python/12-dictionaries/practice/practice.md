# Practice: Chapter 12

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed.

## Warm-up (10 XP each)

### Task 1: The drinks board

**Goal:** Make a dictionary of three drinks and their prices: tea 3.5, coffee 4.0 and juice 3.0. Print the price of tea, the price of juice and the number of drinks.

**Expected output:**
```text
Tea: 3.50
Juice: 3.00
Drinks: 3
```

**Hint:** Read a value with `drinks["tea"]`. Inside an f-string with double quotation marks, write the key with single ones. `len()` counts the items.

**AI variant:** Ask an AI assistant what `len()` gives for a dictionary: the keys, the values or the items. Check its answer with your run.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Change the menu

**Goal:** Start with `{"tea": 3.5, "cake": 4.25, "scone": 2.75}`. Add a muffin at 3.25, change the price of cake to 4.5 and remove the scone. Print the dictionary.

**Expected output:**
```text
{'tea': 3.5, 'cake': 4.5, 'muffin': 3.25}
```

**Hint:** `menu[key] = value` adds or changes an item. `del menu[key]` removes one.

**AI variant:** Before you run your code, ask an AI assistant to predict the final dictionary. Compare its prediction with your run.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: The price board

**Goal:** Print a menu of three items with their prices lined up, under the heading `MENU`, then the number of items.

**Expected output:**
```text
MENU
tea         3.50
cake        4.25
sandwich    6.00
Items: 3
```

**Hint:** Use `for name, price in menu.items():` and the alignment codes from Chapter 3, such as `<10` and `>6.2f`.

**AI variant:** Ask an AI assistant to explain `menu.items()` with a worked example. Run the example and check that it matches.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Price lookup

**Goal:** Ask the customer which item they want. Print its price, or a polite message if it is not on the menu. Capital letters and extra spaces must not matter.

**Expected output:**
```text
Which item? Coffee
coffee costs 4.00
```

**Hint:** Use `strip()` and `lower()` on the answer, then check it with `in` before you read the price.

**AI variant:** Ask an AI assistant for four answers to test, including one with a capital letter and one that is not on the menu. Predict the output for each, then run them.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Count the votes

**Goal:** Customers voted for a new cake: `["cake", "scone", "cake", "muffin", "cake", "scone"]`. Count the votes for each item with a dictionary and print the counts.

**Expected output:**
```text
cake: 3
scone: 2
muffin: 1
```

**Hint:** Start with `{}`. For each vote, use `counts.get(vote, 0) + 1`.

**AI variant:** Ask an AI assistant to explain the counting line with a worked example for the first three votes. Check each step with `print()`.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Vegan choices

**Goal:** Each menu item has a price and a vegan flag in an inner dictionary. Print only the vegan items with their prices.

**Expected output:**
```text
Vegan choices:
- tea (3.50)
- salad (7.00)
```

**Hint:** Use `items()` to get each name and its inner dictionary, then check `info["vegan"]`.

**AI variant:** Ask an AI assistant to design a structure for menu items with a price and a vegan flag. Challenge its choice: how would you find the price of one item by its name?

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Order with quantities

**Goal:** Take an order until the customer types `done`. For each item on the menu, ask how many. Keep the order in a dictionary, add up the same item if it is ordered twice, and print each item, its count and the total.

**Expected output:**
```text
Item (or done): tea
How many? 2
Item (or done): pizza
Not on the menu.
Item (or done): Cake
How many? 1
Item (or done): done
tea: 2
cake: 1
Total: 11.25
```

**Hint:** Use `while True` and `break` from Chapter 7. Use `order.get(item, 0) + count` to add to an item that is already in the order.

**AI variant:** Ask an AI assistant for test cases, such as the same item twice or an item that is not on the menu. Run each one and write pass or fail.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's order total

**Goal:** An AI assistant wrote this code to add up an order. It said the total would be `11.25`. Instead, the program stops with a `KeyError`. Find the cause and fix it, so that items that are not in `prices` are skipped with a message.

```python
# illustrative: the AI's version
prices = {"tea": 3.5, "cake": 4.25}
order = ["tea", "cake", "juice", "tea"]
total = 0
for item in order:
    total += prices[item]
print(f"Total: {total:.2f}")
```

**Expected output:**
```text
Skipped: juice
Total: 11.25
```

**Hint:** Which item is not a key in `prices`? Check with `in` before you read the price.

**AI variant:** Paste the code and the full error into an AI assistant. Ask for the cause before the fix. Did it name the missing key?

**Solution:** [solutions/task8.py](solutions/task8.py)
