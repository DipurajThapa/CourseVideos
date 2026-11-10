# Practice: Chapter 15

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, questions and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed.

## Warm-up (10 XP each)

### Task 1: Two expenses in a list

**Goal:** Start with an empty list. Append two expenses as tuples: cups for 6.25 and repairs for 45. Print the list, then unpack the second expense and print it with two decimal places.

**Expected output:**
```text
[('cups', 6.25), ('repairs', 45.0)]
Second expense: repairs 45.00
```

**Hint:** `append()` takes one value, so put the tuple in its own brackets: `append(("cups", 6.25))`. The second item has index 1.

**AI variant:** Ask an AI assistant why a tuple is a good fit for one expense. Check its answer against what Chapter 13 says about tuples.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Is it an amount?

**Goal:** Ask for an amount. Remove the spaces, then print whether it is a valid amount: digits with at most one decimal point.

**Expected output:**
```text
Amount: 7.5.0
Valid amount: False
```

**Hint:** `replace(".", "", 1)` removes only the first point. Then `isdigit()` checks the rest.

**AI variant:** Ask an AI assistant to list five answers this check rejects. Predict each result yourself, then run them all.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Allowed or not

**Goal:** Keep the allowed categories in a set. Ask for a category, clean it with `strip()` and `lower()`, and say whether it is allowed.

**Expected output:**
```text
Category:  BEANS 
beans is allowed.
```

**Hint:** Clean the answer before you use `in`. The set holds only small letters.

**AI variant:** Ask an AI assistant what happens if you leave out `lower()`. Test its answer with `BEANS`.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Totals by category

**Goal:** Start with the list `[("cups", 6.25), ("milk", 9.0), ("cups", 4.5), ("repairs", 45.0)]`. Build a dictionary of totals and print one row for each category, in alphabetical order.

**Expected output:**
```text
cups      10.75
milk       9.00
repairs   45.00
```

**Hint:** Use `totals.get(category, 0) + amount`, as in Step 4 of the project, then `sorted(totals)`.

**AI variant:** Ask an AI assistant to predict the total for cups before you run the code. Check its arithmetic: 6.25 plus 4.5.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Ask until the amount is valid

**Goal:** Keep asking for an amount until the answer is valid. Then convert it with `float()` and print it with two decimal places.

**Expected output:**
```text
Amount: ten
Type an amount like 12.50.
Amount: -3
Type an amount like 12.50.
Amount: 7.5
Saved: 7.50
```

**Hint:** Use `while True` and `break` when the check passes. Convert only after the loop.

**AI variant:** Ask an AI assistant for three answers that should be rejected and two that should pass. Run all five.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: The smallest category

**Goal:** For each day in the list `[{"milk": 20.5, "beans": 30.0, "cups": 6.25}, {}]`, print the category with the smallest total. An empty day prints `none`.

**Expected output:**
```text
Smallest: cups
Smallest: none
```

**Hint:** Use the loop from the project's biggest category, with `<` instead of `>`. Remember that `min()` on a dictionary compares the keys, not the totals.

**AI variant:** Ask an AI assistant whether `min(totals)` gives the smallest total. Test its answer on the first day.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Over budget

**Goal:** The cafe has a budget for each category: milk 15, beans 40 and cups 5. Use the totals `{"milk": 20.5, "beans": 30.0, "cups": 6.25}`. Print each category with its total and budget, then a list of the categories over budget, made with a comprehension, and how many there are.

**Expected output:**
```text
beans     30.00 of 40.00
cups       6.25 of 5.00
milk      20.50 of 15.00
Over budget: ['cups', 'milk']
Categories over budget: 2
```

**Hint:** Use `sorted(totals)` in the comprehension, with an `if` at the end that compares `totals[category]` with `budget[category]`.

**AI variant:** Ask an AI assistant to write the comprehension. Run it, and check that the list is in alphabetical order.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's tracker

**Goal:** An AI assistant wrote this loop and said it adds up each category. It prints `{'milk': 8.0}`. Find the bug, explain it in one sentence, and fix it so it prints both categories with the right totals.

```python
# illustrative
expenses = [("milk", 12.5), ("beans", 30.0), ("milk", 8.0)]
for category, amount in expenses:
    totals = {}
    totals[category] = totals.get(category, 0) + amount
print(totals)
```

**Expected output:**
```text
{'milk': 20.5, 'beans': 30.0}
```

**Hint:** Count how many times the line `totals = {}` runs. It should run once, before the loop.

**AI variant:** Show the AI its own code and the real output. Ask it to explain the cause before it gives a fix. Did it point at the line inside the loop?

**Solution:** [solutions/task8.py](solutions/task8.py)
