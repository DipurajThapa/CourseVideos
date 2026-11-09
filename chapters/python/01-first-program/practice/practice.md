# Practice: Chapter 1

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and words can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: Introduce yourself

**Goal:** Write a program that prints your name on the first line and your city on the second line.

**Expected output:**
```text
My name is Omar.
I live in Nairobi.
```

**Hint:** Use one `print()` for each line.

**AI variant:** Ask an AI assistant to explain why two `print()` calls produce two lines. Check its answer against the "The idea" section of the lesson.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Fix the broken greeting

**Goal:** This program does not run. Find both mistakes and fix them.

```text
print("Good morning)
Print("Ready to learn?")
```

**Expected output:**
```text
Good morning
Ready to learn?
```

**Hint:** Run it and read the last line of each error. Fix one mistake, then run it again.

**AI variant:** Paste the code and the first error into an AI assistant using the Debug card in `ai-prompts.md`. Did it find both mistakes, or only the first one?

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Predict, then run

**Goal:** Write down what you think these lines will print. Then run them and compare.

```text
print("A", "B", "C")
print("A", "B", "C", sep="")
print("A", "B", "C", sep=", ")
```

**Expected output:**
```text
A B C
ABC
A, B, C
```

**Hint:** `sep=""` means "put nothing between the values".

**AI variant:** Ask an AI assistant to predict the output before you run the code. Was its prediction correct?

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: A text business card

**Goal:** Print a five-line business card with a border, a name, a job title and an email address.

**Expected output:**
```text
+------------------------+
|  Priya Shah            |
|  Junior Web Developer  |
|  priya@example.com     |
+------------------------+
```

**Hint:** Count the characters on each line so the right border lines up. Spaces count.

**AI variant:** Ask an AI assistant for code that prints this exact card. Run its code and check that every right border lines up.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: A countdown on one line

**Goal:** Use four `print()` calls to print a countdown on a single line.

**Expected output:**
```text
3... 2... 1... Go!
```

**Hint:** Set `end` to a space for the first three calls.

**AI variant:** Ask an AI assistant for two different ways to print this line. Run both. Which one is easier for you to read?

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Let Python do the maths

**Goal:** Print the number of hours in a week, minutes in a day and seconds in an hour. Let Python calculate each number.

**Expected output:**
```text
Hours in a week: 168
Minutes in a day: 1440
Seconds in an hour: 3600
```

**Hint:** In Python, `*` means multiply. Do not put the calculation inside quotation marks.

**AI variant:** Ask an AI assistant what happens if you write `"24 * 7"` with quotation marks. Test its answer.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: A study timetable

**Goal:** Print a small study timetable with columns separated by `|`, then print the total number of minutes.

**Expected output:**
```text
Day | Topic | Minutes
Mon | print() | 20
Wed | sep and end | 25
Fri | Errors | 30
Total minutes: 75
```

**Hint:** Use `sep=" | "` on each table line. Let Python add the minutes.

**AI variant:** Ask an AI assistant how to make the columns line up perfectly. It may use a feature you have not learned yet. Ask it to explain that feature in two sentences, and save the idea for later chapters.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Check the AI's work

**Goal:** Give an AI assistant this exact output and ask it for a program that uses only `print()`. Run its code. Find every difference from the target and fix it yourself.

**Expected output:**
```text
WEEKLY CODING PLAN
Mon / Wed / Fri
Goal: 90 minutes of practice
Status: on track...ready
```

**Hint:** Check the separators on line 2 and the joined text on line 4. Let Python calculate the 90.

**AI variant:** If the AI's first answer was correct, ask it to explain how `end` creates the last line. If it was wrong, tell it which line was wrong and see if it can fix it.

**Solution:** [solutions/task8.py](solutions/task8.py)
