# Practice: Chapter 6

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed. Test every program with more than one answer, including the boundary value.

## Warm-up (10 XP each)

### Task 1: Even or odd

**Goal:** Ask for a whole number. Print whether it is even or odd.

**Expected output:**
```text
Type a whole number: 7
7 is odd
```

**Hint:** A number is even when the remainder after dividing by 2 is 0. Use the remainder operator, `%`, and `==`.

**AI variant:** Ask an AI assistant for three edge cases for this program, including 0 and a negative number. Run each one. Is 0 even?

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Adult or child ticket

**Goal:** Ask for the user's age. Print `Ticket: adult` for 18 or older, and `Ticket: child` otherwise.

**Expected output:**
```text
How old are you? 18
Ticket: adult
```

**Hint:** "18 or older" includes 18, so choose the operator that includes the boundary value.

**AI variant:** Ask an AI assistant to name the boundary value for this rule. Test the program with that value and with one less.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Predict the conditions

**Goal:** Create the variables `cups = 4`, `price = 2.5` and `item = "Cake"`. Then print these five conditions: `cups >= 4`, `price * cups == 10`, `item != "cake"`, `cups < 4 or price > 2` and `not cups == 4`. Write your prediction for each one (`True` or `False`) before you run the program.

**Expected output:**
```text
True
True
True
True
False
```

**Hint:** Work out each side of a comparison first. In the fourth condition, Python checks `cups < 4` and `price > 2` separately, then joins them with `or`.

**AI variant:** Ask an AI assistant to predict the five lines. Compare its predictions, yours and the real output. Where they differ, find out why.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Opening hours

**Goal:** The Corner Cafe opens at 8 and closes at 18. Ask for the hour (0 to 23) and print whether the cafe is open.

**Expected output:**
```text
Hour (0 to 23): 18
Sorry, the Corner Cafe is closed.
```

**Hint:** The cafe is open when the hour is 8 or more and less than 18. Join the two comparisons with `and`.

**AI variant:** Ask an AI assistant for the edge cases of this rule. Check that its list includes 7, 8, 17 and 18, then run each one.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Quiz grade

**Goal:** Ask for a quiz score from 0 to 100. Print grade A for 90 or more, B for 75 or more, C for 50 or more, and `Try again` for anything lower.

**Expected output:**
```text
Quiz score (0 to 100): 75
Grade: B
```

**Hint:** Use `if`, two `elif` blocks and `else`. Check the highest score first, because Python runs only the first block whose condition is `True`.

**AI variant:** Ask an AI assistant to write this program with the conditions in the opposite order, lowest first. Test it with 95. Explain the result.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: A safe yes

**Goal:** Ask whether the customer wants a receipt. Accept `yes` or `y`, with any capital letters and spaces.

**Expected output:**
```text
Do you want a receipt? (yes/no)  Y
Printing your receipt.
```

**Hint:** Clean the answer once with `.strip().lower()`. Then use `or` with a full comparison on each side.

**AI variant:** Ask an AI assistant for five different ways a user might type yes. Run your program with each one. Which ones does it accept?

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: A bill splitter that checks

**Goal:** Rebuild the core of the Chapter 5 bill splitter. Ask for the bill total and the number of people. If the number of people is 0 or less, print a clear message. Otherwise, share the total in whole cents and print each share and the extra cents.

**Expected output:**
```text
Bill total: 43.07
Number of people: 4
Each pays: 10.76
Extra cents: 3
```

**Hint:** Put every line that divides by `people` inside the `else` block, so Python never reaches a division by zero.

**AI variant:** Ask an AI assistant for edge cases that could still break your program. Run each one. Which of them would need a tool from a later chapter?

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's delivery fee

**Goal:** The cafe delivers for free when the order total is 30 or more; otherwise delivery costs 2.50. An AI assistant wrote the condition `if order > 30:` and said an order of 30 gets free delivery. Write the program with the correct condition, and print the fee and the amount to pay.

**Expected output:**
```text
Order total: 30
Delivery fee: 0.00
To pay: 30.00
```

**Hint:** Test the AI's condition with exactly 30 first. "30 or more" includes 30.

**AI variant:** Show the AI its own condition and the result for 30. Ask it to explain the cause before the fix. Did it name the operator?

**Solution:** [solutions/task8.py](solutions/task8.py)
