# Practice: Chapter 2

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: Store and print

**Goal:** Create three variables: a name, an age and a city. Print each one on its own line with a label.

**Expected output:**
```text
Name: Omar
Age: 16
City: Nairobi
```

**Hint:** The name and the city are strings, so they need quotation marks. The age is an `int`, so it does not.

**AI variant:** Ask an AI assistant which type each of your three variables has. Check its answer with `type()`.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Name the type

**Goal:** Print the type of the values `42`, `42.0`, `"42"` and `False`.

**Expected output:**
```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

**Hint:** Put each value inside `type()`, and put that inside `print()`.

**AI variant:** Before you run it, ask an AI assistant to predict the four lines. Was its prediction correct?

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Predict the operators

**Goal:** Write down what you think each line prints. Then print `20 / 4`, `20 // 6`, `20 % 6` and `2 ** 5`, and compare.

**Expected output:**
```text
5.0
3
2
32
```

**Hint:** `/` always gives a `float`, even when the division has no remainder.

**AI variant:** Ask an AI assistant to explain why `20 / 4` gives `5.0` and not `5`. Check the explanation against Step 3 of the lesson.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Stationery shop total

**Goal:** A notebook costs 2.5 and a pen costs 1.25. Store the prices and the counts (3 notebooks, 4 pens) in variables. Calculate and print each subtotal and the total.

**Expected output:**
```text
Notebooks: 7.5
Pens: 5.0
Total: 12.5
```

**Hint:** Use four variables for the prices and counts, then three more for the results.

**AI variant:** Use the Plan card in `ai-prompts.md` to ask an AI assistant which variables you need. Compare its list with yours.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Minutes to hours

**Goal:** Store `135` in a variable called `total_minutes`. Use `//` and `%` to print it as hours and minutes.

**Expected output:**
```text
135 minutes is 2 hours and 15 minutes
```

**Hint:** There are 60 minutes in an hour. `//` gives the whole hours and `%` gives the minutes that are left.

**AI variant:** Ask an AI assistant for three more values of `total_minutes` to test, including `0` and `60`. Predict each output, then run them.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Savings tracker

**Goal:** Start with `savings = 0`. Add 15 each week for three weeks, printing the total after each week. Then spend 20 on a book and print what is left.

**Expected output:**
```text
Week 1: 15
Week 2: 30
Week 3: 45
After buying a book: 25
```

**Hint:** Store the weekly amount in a variable. Reuse the same line, `savings = savings + weekly_saving`, for each week.

**AI variant:** Ask an AI assistant to predict the output if the weekly amount changes to 12. Change the value in your code and check.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Split the bill with a tip

**Goal:** Three friends share a bill of 60 and add a 10 percent tip. Store the bill, the tip rate and the number of people in variables. Print the bill, the tip, the total and what each person pays.

**Expected output:**
```text
Bill: 60
Tip: 6.0
Total: 66.0
Each person pays: 22.0
```

**Hint:** 10 percent is `0.1`. Calculate the tip first, then the total, then divide by the number of people.

**AI variant:** Ask an AI assistant to test your program with a bill of 0 and with 4 people. Run both cases. Does each result make sense?

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's temperature converter

**Goal:** An AI assistant wrote this converter and said it prints `25 C is 77.0 F`. Run it, find the flaw and fix it.

```text
celsius = 25
fahrenheit = celsius + 32 * 9 / 5
print(celsius, "C is", fahrenheit, "F")
```

**Expected output:**
```text
25 C is 77.0 F
```

**Hint:** The formula is: multiply the Celsius value by 9, divide by 5, then add 32. Check which operation Python does first.

**AI variant:** Show the AI its own code and the real output, `25 C is 82.6 F`. Ask it to explain the cause before the fix. Did it name the order of operations?

**Solution:** [solutions/task8.py](solutions/task8.py)
