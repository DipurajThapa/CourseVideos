# Practice: Chapter 7

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed. If a program never stops, click in the terminal and press Ctrl+C.

## Warm-up (10 XP each)

### Task 1: Count to five

**Goal:** Use a `while` loop and a counter to print the numbers 1 to 5, one per line. Then print `Done counting.`

**Expected output:**
```text
1
2
3
4
5
Done counting.
```

**Hint:** Start the counter at 1. Which operator makes the loop include 5?

**AI variant:** Ask an AI assistant to trace your loop in a table, one row per pass. Check that the last row shows the condition is `False`.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Countdown

**Goal:** Count down from 3 to 1, printing `3...`, `2...` and `1...`, then print `Go!`.

**Expected output:**
```text
3...
2...
1...
Go!
```

**Hint:** The counter starts at 3 and goes down by 1 on every pass. `seconds -= 1` is short for `seconds = seconds - 1`.

**AI variant:** Ask an AI assistant what happens if you write `seconds += 1` by mistake. Predict the answer first, then check it with a trace table, not by running it.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Predict the passes

**Goal:** A jar holds 100 coins. Every day, half of the coins are spent: `coins = coins // 2`. Count the days until 10 coins or fewer are left. Print the number of days and the coins left. Write a trace table before you run the program.

**Expected output:**
```text
After 4 days: 6 coins
```

**Hint:** Your trace table needs a column for `coins` and one for `days`. The loop continues while `coins > 10`.

**AI variant:** Ask an AI assistant to trace the loop in a table. Compare its table with yours, row by row.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: A valid age

**Goal:** Ask for the user's age. While the age is below 0 or above 120, print a message and ask again. Then print the age.

**Expected output:**
```text
Your age (0 to 120): 150
Please type an age from 0 to 120.
Your age (0 to 120): -1
Please type an age from 0 to 120.
Your age (0 to 120): 34
Age saved: 34
```

**Hint:** Ask once before the loop, and ask again as the last line inside the loop.

**AI variant:** Ask an AI assistant for edge cases with the expected output for each, including the boundary values 0 and 120. Run every one.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Savings goal

**Goal:** Asha saves 15 each week and wants at least 100. Use a loop to count the weeks she needs. Print the weeks and the amount saved.

**Expected output:**
```text
Weeks: 7
Saved: 105
```

**Hint:** You need a running total, `saved`, and a counter, `weeks`. Stop when `saved` is 100 or more.

**AI variant:** Ask an AI assistant to solve the same problem with one calculation and no loop. Does its answer match yours? Which version is easier to change if the weekly amount changes every week?

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Average score

**Goal:** Ask for quiz scores until the user types -1. Print how many scores there were and their average, with one decimal place. If the first answer is -1, print `No scores entered.`

**Expected output:**
```text
Score (-1 to finish): 70
Score (-1 to finish): 85
Score (-1 to finish): 90
Score (-1 to finish): -1
Scores: 3
Average: 81.7
```

**Hint:** -1 is the stop value. Divide only after the loop, and only when the count is more than 0.

**AI variant:** Ask an AI assistant what your program does when the first answer is -1. Then run it with that answer.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Menu with help

**Goal:** Extend Asha's order loop with juice at 2.75 and a `help` command that prints the menu. Unknown items print a message. Stop on `done`, then print the number of items and the total.

**Expected output:**
```text
Item (tea, cake, juice, help or done): help
Menu: tea 3.50, cake 4.00, juice 2.75
Item (tea, cake, juice, help or done): juice
Item (tea, cake, juice, help or done): Tea
Item (tea, cake, juice, help or done): soup
Sorry, that is not on the menu. Type help.
Item (tea, cake, juice, help or done): done
Items: 2
Total: 6.25
```

**Hint:** `help` must not change the total or the count. Check `done` first, then `help`, then the items.

**AI variant:** Ask an AI assistant for five test answers that cover every branch of your loop. Run them and check the total by hand.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's kettle timer

**Goal:** An AI assistant wrote this countdown for the kettle and said it prints 5 down to 1 and then `Tea is ready!`:

```python
# illustrative: the AI's countdown, do not run it as it is
minutes = 5
while minutes > 0:
    print(f"Minutes left: {minutes}")
print("Tea is ready!")
```

Trace it for two passes without running it, explain why it never ends, and write the correct program.

**Expected output:**
```text
Minutes left: 5
Minutes left: 4
Minutes left: 3
Minutes left: 2
Minutes left: 1
Tea is ready!
```

**Hint:** Which value does the condition check? Which line changes it?

**AI variant:** Show the AI its own code and ask it to trace the first three passes in a table before it suggests a fix. Did the trace show that `minutes` never changes?

**Solution:** [solutions/task8.py](solutions/task8.py)
