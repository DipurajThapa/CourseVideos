# Practice: Chapter 8

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed.

## Warm-up (10 XP each)

### Task 1: Count to ten

**Goal:** Use a `for` loop and `range()` to print the numbers 1 to 10, one per line. Then print `Done counting.`

**Expected output:**
```text
1
2
3
4
5
6
7
8
9
10
Done counting.
```

**Hint:** The stop value is one more than the last number you want.

**AI variant:** Ask an AI assistant to list the values of your `range()` before you run it. Check that the list has 10 values.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Countdown

**Goal:** Count down from 5 to 1, printing `5...` to `1...`, then print `Go!`.

**Expected output:**
```text
5...
4...
3...
2...
1...
Go!
```

**Hint:** Use a step of -1. The stop value must be 0, so that 1 is the last value.

**AI variant:** Ask an AI assistant what `range(5, 1, -1)` gives. Predict the answer first, then check it by running a loop.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Spell it out

**Goal:** Print each letter of the word `Tea` in capitals on its own line. Then print how many letters the word has.

**Expected output:**
```text
T
E
A
Tea has 3 letters.
```

**Hint:** Loop over the string itself. `.upper()` and `len()` come from Chapter 3.

**AI variant:** Ask an AI assistant for two different ways to print the letters. Run both and compare the outputs.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Times table

**Goal:** Print the 3 times table from 1 to 5, as `3 x 1 = 3` and so on.

**Expected output:**
```text
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
```

**Hint:** The loop variable is the number you multiply by. Put the calculation inside the f-string.

**AI variant:** Ask an AI assistant for 3 checks for your output, such as the first line, the last line and the number of lines. Run them.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Tips for four shifts

**Goal:** Ask for the tips of 4 shifts and print the total with two decimal places.

**Expected output:**
```text
Tips for shift 1: 12.5
Tips for shift 2: 8
Tips for shift 3: 15.25
Tips for shift 4: 9.75
Total tips: 45.50
```

**Hint:** Set the total to 0 before the loop. Ask and add inside the loop.

**AI variant:** Ask an AI assistant to predict the total for these four answers. Check its arithmetic against your run.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Count the words

**Goal:** Count the words in the sentence `Two teas and one cake for table four` by counting its spaces. Print the number of words.

**Expected output:**
```text
Words: 8
```

**Hint:** Loop over the characters. A sentence with one space between words has one more word than spaces.

**AI variant:** Ask an AI assistant when this method gives a wrong count. Test its example, such as a sentence with two spaces in a row.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Cake price chart

**Goal:** Print a price chart for 1 to 8 cakes at 4.00 each. From 5 cakes, the customer gets 10 percent off the whole order. Line up the columns.

**Expected output:**
```text
Cakes   Price
    1    4.00
    2    8.00
    3   12.00
    4   16.00
    5   18.00
    6   21.60
    7   25.20
    8   28.80
```

**Hint:** Inside the loop, work out the full cost, then use an `if` to apply the discount. Use the format specifications from Chapter 3.

**AI variant:** Ask an AI assistant to write the same chart. Run both versions and compare every line. Which one is easier to read?

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's total

**Goal:** An AI assistant wrote this loop to add the numbers 1 to 10 and said it prints 55. It prints 45. Find the cause and fix it.

```python
# illustrative: the AI's version
total = 0
for number in range(1, 10):
    total += number
print(f"The numbers 1 to 10 add up to {total}")
```

**Expected output:**
```text
The numbers 1 to 10 add up to 55
```

**Hint:** List the values the `range()` gives. Which number is missing?

**AI variant:** Show the AI its own code and the real output, 45. Ask it to explain the cause before the fix. Did it name the stop value?

**Solution:** [solutions/task8.py](solutions/task8.py)
