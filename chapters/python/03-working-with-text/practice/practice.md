# Practice: Chapter 3

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: Greeting card

**Goal:** Store a name and a city in variables. Use f-strings to print a greeting and the number of letters in the name.

**Expected output:**
```text
Hello, Omar! Welcome from Nairobi.
Omar has 4 letters.
```

**Hint:** `len(name)` counts the characters. You can put it inside the curly brackets.

**AI variant:** Ask an AI assistant to predict the output for the name `"Li"`. Change the name in your code and check its prediction.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Two decimal places

**Goal:** Store three prices: `2.5` for coffee, `4` for juice and `3.75` for a muffin. Print each one with exactly two decimal places.

**Expected output:**
```text
Coffee: 2.50
Juice: 4.00
Muffin: 3.75
```

**Hint:** Add `:.2f` after the name inside the curly brackets.

**AI variant:** Ask an AI assistant what `.2f` means, word by word. Check its answer against Step 3 of the lesson.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: First, last and middle

**Goal:** Store the word `"Python"`. Print its first letter, its last letter and its third letter, each on its own line.

**Expected output:**
```text
P
n
t
```

**Hint:** Indexes start at 0, and `-1` is the last character. The third letter has index 2.

**AI variant:** Before you run it, ask an AI assistant to predict the three lines. Was every letter correct?

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Clean up a typed name

**Goal:** A customer typed their name as `"   mARIA lopez "`. Remove the extra spaces, then print the name with capital first letters, in capitals and in small letters.

**Expected output:**
```text
Maria Lopez
MARIA LOPEZ
maria lopez
```

**Hint:** Call `strip()` once and store the result. Then call `title()`, `upper()` and `lower()` on the clean name.

**AI variant:** Ask an AI assistant whether `title()` changes the original string. Check its answer by printing the original after the other lines.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: A menu in columns

**Goal:** Print a small menu with a header row. Names take 12 characters on the left, and prices take 8 characters on the right with two decimal places.

**Expected output:**
```text
Item           Price
Coffee          2.50
Orange juice    4.00
Muffin          3.75
```

**Hint:** Use `:<12` for the names and `:>8.2f` for the prices. The header price uses `:>8` without `.2f`, because it is text.

**AI variant:** Paste the expected output into the Generate prompt card. Compare the AI's code with yours, and count the characters in one line of each output.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Change the menu text

**Goal:** Store the menu text `"Tea, coffee and tea cake"`. Replace `tea` with `chai`. Then do it again after `lower()`, and finally print the menu in capitals.

**Expected output:**
```text
Tea, coffee and chai cake
chai, coffee and chai cake
TEA, COFFEE AND TEA CAKE
```

**Hint:** `replace()` only matches the exact letters, so `"Tea"` with a capital T is not changed on the first line.

**AI variant:** Ask an AI assistant to predict the first line before you run it. Did it notice that capital letters matter?

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: A mini bill

**Goal:** Three coffees cost 2.5 each, and a muffin costs 3.75. Print a bill that is 20 characters wide, with a centred title, the two items, a line of `=` and the total.

**Expected output:**
```text
---- TOTAL BILL ----
Coffee x 3      7.50
Muffin          3.75
====================
Total          11.25
```

**Hint:** Use `:-^20` for the title, `:<12` for the labels and `:>8.2f` for the amounts. `"=" * 20` makes the line.

**AI variant:** Ask an AI assistant for one value that could break the layout, such as a price of 1250. Try it. What happens to the columns, and why?

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's receipt line

**Goal:** An AI assistant wrote this line for a cake slice that costs 12.5, and said it prints the price as `12.50`. Run it, find the two flaws and fix them.

```text
item = "Cake slice"
price = 12.5
print("{item:<16}{price:>8.2}")
```

**Expected output:**
```text
Cake slice         12.50
```

**Hint:** Check the start of the string, and check the letter at the end of the price format.

**AI variant:** Show the AI its code and the real output. Ask it to explain each flaw before it gives a fix. Did it find both?

**Solution:** [solutions/task8.py](solutions/task8.py)
