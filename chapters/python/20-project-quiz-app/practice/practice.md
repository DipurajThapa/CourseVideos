# Practice: Chapter 20

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, questions and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: One more question

**Goal:** Start with a list of two question dictionaries. Append a third question about fresh bread. Print how many questions there are and the last question.

**Expected output:**
```text
3 questions
Last: Is the bread fresh today?
```

**Hint:** `append()` takes one dictionary. `[-1]` gives the last item of a list, as in Chapter 11.

**AI variant:** Ask an AI assistant why a list of dictionaries fits quiz questions better than two separate lists. Check its reason against Step 1 of the project.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Prices as numbers

**Goal:** Write `same_price(given, correct)` that returns True when two prices are the same number, so `3.5` and `3.50` match.

**Expected output:**
```text
True
False
```

**Hint:** Convert both answers with `float()` before you compare them.

**AI variant:** Ask an AI assistant what `same_price()` does with the answer `three`. Predict the result, then run it. Which chapter will teach you to handle it?

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Checks before you trust it

**Goal:** Copy `percentage()` from the project. Add three `assert` lines for 1 out of 4, 4 out of 4 and 0 out of 4, then print a message.

**Expected output:**
```text
All checks passed
```

**Hint:** An `assert` stays silent when it is true, so the message prints only if all three pass.

**AI variant:** Ask an AI assistant for two more edge cases for `percentage()`. Add them, predict each result and run the file.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: An Expert grade

**Goal:** Add a new grade, Expert, for a score of exactly 100. Keep the other grades. Print the grade for 100, 80, 50 and 40.

**Expected output:**
```text
100 Expert
80 Ready
50 Almost
40 Practise again
```

**Hint:** Put the Expert check first. In an `if` and `elif` chain, the first true condition wins.

**AI variant:** Ask an AI assistant to write the tests for the new grade first. Check that one test uses exactly 100 and one uses 99.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Stars for the score

**Goal:** Write `stars(points, total)` that returns one star for each right answer and one dash for each wrong one.

**Expected output:**
```text
***-
----
****
```

**Hint:** In Chapter 3, `"*" * 3` gave three stars. Join the stars and the dashes with `+`.

**AI variant:** Ask an AI assistant to predict `stars(0, 0)`. Run it and compare.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Tests first for change

**Goal:** Write three `assert` lines for `change_due(paid, price)` first: 5 paid for 3.5, 10 paid for 2.75, and the exact price paid. Then write the function so they pass.

**Expected output:**
```text
3 checks passed
```

**Hint:** Round the result to two places, as Chapter 19 did for decimals.

**AI variant:** Show an AI assistant only your three checks and ask for the function. Run your checks on its answer.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Points by topic

**Goal:** Each question has a topic: prices or allergens. Given a list of answers, count the right answers for each topic in a dictionary and print one line per topic, in alphabetical order.

**Expected output:**
```text
allergens: 1/2
prices: 2/2
```

**Hint:** Use `get(topic, 0)` from Chapter 12 to add to each total.

**AI variant:** Ask an AI assistant how to store the topic in `quiz_data.py`. Check that every question still has a question and an answer.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's counter

**Goal:** An AI assistant wrote `count_correct(given, answers)` with `for i in range(1, len(answers)):`, and it said the function counts every answer. Write three checks, including one where only the first answer is right, find the mistake and fix it.

**Expected output:**
```text
All checks passed
```

**Hint:** `range(1, ...)` starts at the second item. Which answer does it skip?

**AI variant:** Show the AI its own function and the failing check. Ask for the cause before the fix, and check that it names the start of the `range()`.

**Solution:** [solutions/task8.py](solutions/task8.py)
