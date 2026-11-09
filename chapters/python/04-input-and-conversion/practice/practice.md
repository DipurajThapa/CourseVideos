# Practice: Chapter 4

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, questions and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed.

## Warm-up (10 XP each)

### Task 1: Two questions

**Goal:** Ask for the user's name and their city. Print one greeting that uses both answers.

**Expected output:**
```text
What is your name? Omar
Which city are you from? Nairobi
Hello, Omar from Nairobi!
```

**Hint:** Store each answer in its own variable. A name and a city stay strings, so you do not need to convert them.

**AI variant:** Ask an AI assistant whether this program needs `int()` anywhere. Check its answer against Step 2 of the lesson.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Double and square

**Goal:** Ask for a whole number. Print the number doubled and the number squared.

**Expected output:**
```text
Type a whole number: 7
Double: 14
Square: 49
```

**Hint:** Convert the answer with `int()`. `**` raises a number to a power.

**AI variant:** Before you add `int()`, run the program and type 7. Then ask an AI assistant to explain the output of the double line. Was the explanation right?

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Age next year

**Goal:** Ask for the user's age and print the age they will be next year.

**Expected output:**
```text
How old are you? 17
Next year you will be 18.
```

**Hint:** `int(input("How old are you? "))` gives you a number you can add 1 to.

**AI variant:** Ask an AI assistant what happens if the user types `17.5`. Predict, then run it and compare.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Room area

**Goal:** Ask for the width and the length of a room in metres. Print the area with two decimal places.

**Expected output:**
```text
Width in metres? 3.5
Length in metres? 4.2
Area: 14.70 square metres
```

**Hint:** Measurements can have decimals, so use `float()` for both answers and `:.2f` for the area.

**AI variant:** Use the Test prompt card. Ask for four answers to type for the width, including a word. Run each one and mark each AI prediction as right or wrong.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Minutes to hours

**Goal:** Ask for a number of minutes. Print it as hours and minutes.

**Expected output:**
```text
How many minutes? 135
135 minutes is 2 hours and 15 minutes.
```

**Hint:** Use `// 60` for the whole hours and `% 60` for the minutes that are left, from Chapter 2.

**AI variant:** Ask an AI assistant to predict the output for 59 and for 60 minutes. Run both and check.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: One receipt line

**Goal:** Ask for an item name, the price of one item and how many. Print one receipt line: the cleaned item name and count in 16 characters on the left, and the total in 8 characters on the right with two decimal places.

**Expected output:**
```text
Item:  notebook
Price of one: 2.75
How many: 4
Notebook x 4       11.00
```

**Hint:** Clean the name with `strip()` and `title()`. Build the label with an f-string, then use `:<16` and `:>8.2f` as in Chapter 3.

**AI variant:** Ask an AI assistant which conversion each of the three answers needs, and why. Compare with your code.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Temperature converter

**Goal:** Ask for a temperature in degrees Celsius. Print it in degrees Fahrenheit with one decimal place, and in kelvin with two decimal places.

**Expected output:**
```text
Temperature in Celsius? 21.5
21.5 C is 70.7 F
21.5 C is 294.65 K
```

**Hint:** Fahrenheit is Celsius times 9, divided by 5, plus 32. Kelvin is Celsius plus 273.15. Use `:.1f` and `:.2f`.

**AI variant:** Ask an AI assistant for the Fahrenheit formula, then check it with one known value: 100 degrees Celsius is 212 degrees Fahrenheit.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's ticket program

**Goal:** An AI assistant wrote this program and said that for a ticket price of 12.5 and 3 tickets, it prints `Total: 37.50`. Run it with those answers. It has two flaws, and each one causes a different error. Fix them one at a time.

```text
price = int(input("Price of one ticket? "))
tickets = input("How many tickets? ")
print(f"Total: {price * tickets:.2f}")
```

**Expected output:**
```text
Price of one ticket? 12.5
How many tickets? 3
Total: 37.50
```

**Hint:** Read the last line of each error. One answer has a decimal point. The other answer is used in a calculation.

**AI variant:** Use the Debug prompt card for the first error. Did the AI also find the second flaw before you ran the program again?

**Solution:** [solutions/task8.py](solutions/task8.py)
