# Practice: Chapter 11

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed.

## Warm-up (10 XP each)

### Task 1: The drinks menu

**Goal:** Make a list of four drinks: `tea`, `coffee`, `juice` and `water`. Print the first drink, the last drink and the number of drinks.

**Expected output:**
```text
First: tea
Last: water
Drinks on the menu: 4
```

**Hint:** The first item has index 0. Index -1 gives the last item, and `len()` counts the items.

**AI variant:** Ask an AI assistant what index the last item of a 4-item list has, counting from the start. Check its answer by printing that index.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Change the order

**Goal:** Start with the order `["tea", "cake"]`. Add `juice` at the end, add `scone` at the start, then remove `cake`. Print the list and the number of items.

**Expected output:**
```text
['scone', 'tea', 'juice']
Items: 3
```

**Hint:** Use `append()`, `insert()` with index 0, and `remove()`.

**AI variant:** Before you run your code, ask an AI assistant to predict the final list. Compare its prediction with your run.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: A week of visitors

**Goal:** The cafe counts its visitors for 7 days: 34, 41, 29, 50, 62, 75 and 58. Print the first three days, the last two days and the middle day.

**Expected output:**
```text
First three days: [34, 41, 29]
Last two days: [75, 58]
Middle day: 50
```

**Hint:** A slice stops before its end index, like `range()`. The middle of 7 items has index 3.

**AI variant:** Ask an AI assistant to explain `visitors[-2:]` with a worked example. Run the example and check that it gives the same result.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: The shopping list

**Goal:** Ask for three items to buy and keep them in a list. Remove extra spaces from each answer. Then print the list with numbers, and the number of items.

**Expected output:**
```text
Item 1: milk
Item 2:   sugar
Item 3: tea bags
Your list:
1. milk
2. sugar
3. tea bags
3 items
```

**Hint:** Start with an empty list, `[]`. Use `append()` inside a `for` loop, then a second loop with a counter to print.

**AI variant:** Ask an AI assistant for three test answers that could cause trouble, such as an empty answer. Run your program with each one.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Sales numbers

**Goal:** Five sales are 18.5, 22.0, 9.75, 31.25 and 14.0. Print the total, the average with two decimal places, the biggest and the smallest sale, and the list sorted from biggest to smallest.

**Expected output:**
```text
Total: 95.50
Average: 19.10
Biggest: 31.25
Smallest: 9.75
Biggest first: [31.25, 22.0, 18.5, 14.0, 9.75]
```

**Hint:** `sum()`, `len()`, `max()` and `min()` work on a list of numbers. `sorted()` with `reverse=True` puts the biggest first.

**AI variant:** Ask an AI assistant to predict the average. Check its arithmetic against your run.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Is it on the menu?

**Goal:** The menu is `tea`, `coffee`, `cake` and `sandwich`. Ask the customer what they would like, and say whether it is on the menu. Capital letters and extra spaces must not matter.

**Expected output:**
```text
What would you like? Cake
Yes, we have cake.
```

**Hint:** `in` checks whether a value is in a list. Use `strip()` and `lower()` on the answer first.

**AI variant:** Ask an AI assistant for four answers to test, including one that is not on the menu. Predict the output for each, then run them.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: The game remembers

**Goal:** The secret number is 9, and the player has 4 guesses. Keep every guess in a list. A number the player already guessed does not use a guess. At the end, print all the guesses.

**Expected output:**
```text
Your guess: 5
Not this one.
Your guess: 5
You already guessed 5.
Your guess: 12
Not this one.
Your guess: 9
Correct!
Your guesses: [5, 12, 9]
```

**Hint:** Use `while len(guesses) < 4`. Check `guess in guesses` before you add the guess.

**AI variant:** Ask an AI assistant to list test cases, such as winning on the last guess or repeating a number. Run each one and write pass or fail.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's top scores

**Goal:** An AI assistant wrote this code to show the best score and the top three. It said the output would be `Best score: 95`. Instead, the program stops with a `TypeError`. Find the cause and fix it. The original order of the scores must not change.

```python
# illustrative: the AI's version
scores = [72, 95, 64, 88, 91]
ranked = scores.sort(reverse=True)
print(f"Best score: {ranked[0]}")
print(f"Top three: {ranked[:3]}")
print(f"In the order they were played: {scores}")
```

**Expected output:**
```text
Best score: 95
Top three: [95, 91, 88]
In the order they were played: [72, 95, 64, 88, 91]
```

**Hint:** What does `sort()` give back? Which function gives a new sorted list and leaves the original alone?

**AI variant:** Paste the code and the full error into an AI assistant. Ask for the cause before the fix. Did it explain that `sort()` gives `None`?

**Solution:** [solutions/task8.py](solutions/task8.py)
