# Practice: Chapter 5

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, questions and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed.

## Warm-up (10 XP each)

### Task 1: The tip alone

**Goal:** Ask for a bill total and a tip percent. Print only the tip, with two decimal places.

**Expected output:**
```text
Bill total: 30
Tip percent: 10
Tip: 3.00
```

**Hint:** A percent is divided by 100. Use `float()` for the bill and `int()` for the percent.

**AI variant:** Ask an AI assistant for the tip on a bill of 30 at 10 percent. Work it out by hand first, then compare.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Money to cents and back

**Goal:** Ask for an amount of money. Print it as a whole number of cents, then turn the cents back into money with two decimal places.

**Expected output:**
```text
Amount: 12.34
In cents: 1234
Back to money: 12.34
```

**Hint:** Multiply by 100 and use `round()`, because `amount * 100` is a `float`.

**AI variant:** Ask an AI assistant why `round()` is needed in this task. Then print `12.34 * 100` without `round()` and see if the AI was right.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Share the sweets

**Goal:** Ask how many sweets there are and how many children share them. Print how many sweets each child gets and how many are left over.

**Expected output:**
```text
How many sweets? 17
How many children? 5
Each child gets 3 sweets.
2 sweets are left over.
```

**Hint:** `//` gives the whole share, and `%` gives what is left.

**AI variant:** Ask an AI assistant to predict the output for 17 sweets and 5 children. Run your program to check the prediction.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Split without a tip

**Goal:** Ask for a bill total and the number of people. Print a receipt with the bill, what each person pays and the extra cents.

**Expected output:**
```text
Bill total: 50
Number of people: 3
------------------------
Bill               50.00
Each pays          16.66
Extra cents            2
```

**Hint:** Work in whole cents, as in Step 3 of the project. Check: 3 times 16.66, plus 2 cents, is 50.00.

**AI variant:** Ask an AI assistant to split 50 between 3 people. Does its answer add up to exactly 50.00?

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: A fixed service charge

**Goal:** A cafe adds a 5 percent service charge to every bill. Store the 5 in a variable, ask for the bill, and print the bill, the service charge and the total in a 24-character column.

**Expected output:**
```text
Bill total: 64
Bill               64.00
Service 5%          3.20
Total              67.20
```

**Hint:** Build the label with an f-string, as the project builds `Tip 10%`.

**AI variant:** Ask an AI assistant to suggest three bill totals to test this program. Work out each total by hand, then run each test.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: What tip did we give?

**Goal:** Ask for the bill total and the amount the table really paid. Print the tip in money and as a percent with one decimal place.

**Expected output:**
```text
Bill total: 40
Amount paid with tip: 46
Tip: 6.00
That is a 15.0% tip.
```

**Hint:** The tip is the difference. To get a percent, divide the tip by the bill and multiply by 100.

**AI variant:** Ask an AI assistant to write the percent line. Check its order of operations against Chapter 2 before you run it.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Food and tip, shown apart

**Goal:** Ask the same three questions as the bill splitter. Print what each person pays for the food and for the tip separately, and the extra cents from both.

**Expected output:**
```text
Bill total: 37.45
Tip percent: 15
Number of people: 4
Food each           9.36
Tip each            1.40
Extra cents            3
```

**Hint:** Turn the bill into cents first, then calculate the tip in cents and round it. Share each one with `//`, and add the two remainders.

**AI variant:** Ask an AI assistant whether 9.36 plus 1.40 matches the 10.76 from the project. Check the arithmetic yourself.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's splitter

**Goal:** An AI assistant wrote this splitter and said that a bill of 60 with a 10 percent tip, shared by 4, costs 16.50 each:

```text
tip = bill * tip_percent / 100
share = bill + tip / people
```

Work out the correct share by hand, run the AI's lines to see what they really give, and write a fixed program.

**Expected output:**
```text
Bill total: 60
Tip percent: 10
Number of people: 4
Each pays: 16.50
```

**Hint:** Python divides before it adds. Which part should be divided by the number of people?

**AI variant:** Show the AI its own lines and the result they really give. Ask it to explain the cause before the fix. Did it name the order of operations?

**Solution:** [solutions/task8.py](solutions/task8.py)
