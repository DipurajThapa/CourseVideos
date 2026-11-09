# Practice: Chapter 9

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed.

## Warm-up (10 XP each)

### Task 1: Fix the syntax error

**Goal:** This program does not run. Type it, read the error, and fix it so it prints three lines.

```text
print("Corner Cafe")
print("Open from 7 to 19)
print("Fresh cake every day")
```

**Expected output:**
```text
Corner Cafe
Open from 7 to 19
Fresh cake every day
```

**Hint:** Read the last line of the error first. Then look for an opening mark without its closing partner.

**AI variant:** Ask an AI assistant which line causes the error and why, before you fix it. Check that its line number matches the error report.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Read the traceback

**Goal:** This program crashes when the user types `8`. Read the traceback from the bottom up, find the cause and fix it.

```text
cakes = input("Cakes sold: ")
total = cakes * 2.75
print(f"Cake total: {total:.2f}")
```

**Expected output:**
```text
Cakes sold: 8
Cake total: 22.00
```

**Hint:** The traceback names the line with the multiplication. The cause is on the line before it.

**AI variant:** Write down the kind of error, the line and the cause yourself. Then ask an AI to check your reading without fixing the code.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Add a debug line

**Goal:** A customer gets 2 stamps for each of 4 cups. Write a loop that adds the stamps, with a debug line inside the loop that shows the cup number and the stamps so far.

**Expected output:**
```text
DEBUG cup=1 stamps=2
DEBUG cup=2 stamps=4
DEBUG cup=3 stamps=6
DEBUG cup=4 stamps=8
Stamps: 8
```

**Hint:** Put the debug line inside the loop, after the line that changes `stamps`, with the same indentation.

**AI variant:** Ask an AI to predict the debug lines before you run the code. Compare its prediction with your run.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Find the logic error

**Goal:** This program should add up the cups in three orders. With the answers 2, 3 and 1 it prints `Cups sold: 6`... but only by luck. Find the logic error with a debug line, and fix it.

```text
cups = 0
for order in range(1, 4):
    in_order = int(input(f"Cups in order {order}: "))
    cups = cups + order
print(f"Cups sold: {cups}")
```

**Expected output:**
```text
Cups in order 1: 2
Cups in order 2: 3
Cups in order 3: 1
Cups sold: 6
```

**Hint:** Try the answers 5, 5 and 5. The expected total is 15. Print `order`, `in_order` and `cups` inside the loop.

**AI variant:** Use the structured debugging prompt: code, "no error message", expected result 15, actual result. Check that the AI names the same line as your debug output.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: The missing table

**Goal:** This loop should list tables 1 to 5, but table 5 is missing. Fix it.

```text
for table in range(1, 5):
    print(f"Clean table {table}")
print("All 5 tables are clean.")
```

**Expected output:**
```text
Clean table 1
Clean table 2
Clean table 3
Clean table 4
Clean table 5
All 5 tables are clean.
```

**Hint:** This is a logic error. Count the lines of output, then look at the stop value of `range()`.

**AI variant:** Ask an AI to list the values of the `range()` in your fix. Check that the list ends with 5.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: No ratings yet

**Goal:** Ask how many cakes were rated, add up the points for each one, and print the average with one decimal place. If the answer is 0, print `No ratings yet.` instead of crashing.

**Expected output:**
```text
How many cakes were rated? 0
No ratings yet.
```

**Hint:** Use `if count > 0:` before the division. Test with 0, with 1 and with 3.

**AI variant:** Ask an AI for four test cases with expected results, including 0 and 1. Run every case and mark each one pass or fail.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Three bugs, one report

**Goal:** This weekly report has a syntax error, a runtime error and a logic error. Fix all three, one at a time, and say which kind each one was.

```text
print("Weekly tea report"
days = input("How many days? ")
cups = 0
for day in range(1, days + 1):
    sold = int(input(f"Cups on day {day}: "))
    cups = sold
print(f"Cups this week: {cups}")
print(f"Tea money: {cups * 3.5:.2f}")
```

**Expected output:**
```text
Weekly tea report
How many days? 3
Cups on day 1: 20
Cups on day 2: 25
Cups on day 3: 15
Cups this week: 60
Tea money: 210.00
```

**Hint:** Python shows only one error at a time. Fix the syntax error first, then run again. The logic error gives no message, so compare with the expected 60.

**AI variant:** For the logic error, give an AI the code, "no error message", the expected result and the actual result. Ask for the cause first.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's member price

**Goal:** An AI wrote this code for a 10 percent member discount and said that a price of 20 gives `Member price: 18.00`. Run it with 20, find the logic error and fix it.

```text
price = float(input("Price before discount: "))
to_pay = price * 0.1
print(f"Member price: {to_pay:.2f}")
```

**Expected output:**
```text
Price before discount: 20
Member price: 18.00
```

**Hint:** Work out the expected result by hand: 20 minus 10 percent of 20. Then compare it with what the code prints.

**AI variant:** Show the AI its own code, the expected result 18.00 and the actual result. Did it name the cause before it gave the fix?

**Solution:** [solutions/task8.py](solutions/task8.py)
