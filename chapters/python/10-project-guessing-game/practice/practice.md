# Practice: Chapter 10

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, questions and values can differ from the solution, but the shape of the output should match. In each expected output, the text after a question is what the user typed.

## Warm-up (10 XP each)

### Task 1: Is it a whole number?

**Goal:** Ask how many cups the customer wants. Remove the spaces around the answer, then print whether it is a whole number.

**Expected output:**
```text
How many cups? 12
Whole number: True
```

**Hint:** `strip()` removes the spaces, and `isdigit()` gives `True` only when every character is a digit.

**AI variant:** Ask an AI assistant which of these answers `isdigit()` accepts: `"12"`, `"-3"`, `"7.5"` and `""`. Predict each one yourself, then test them all.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Higher or lower

**Goal:** The price of a sandwich is 9. Ask for one guess and print `Correct!`, `Higher!` or `Lower!`.

**Expected output:**
```text
Guess the price: 4
Higher!
```

**Hint:** Use `if`, `elif` and `else`, as in Step 1 of the project. Think about which message helps the player: the price is higher than the guess.

**AI variant:** Ask an AI assistant for three guesses that test every branch of your program. Check that one of them is exactly 9.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Two dice

**Goal:** Roll two dice with `random.randint()` and print each one. Use `random.seed(5)` so your result matches the expected output.

**Expected output:**
```text
Dice 1: 5
Dice 2: 3
```

**Hint:** A dice shows 1 to 6, and `randint()` includes both ends. Remove the seed when you want a different roll each time.

**AI variant:** Ask an AI assistant whether `random.randrange(1, 6)` can roll a 6. Check its answer against what you learned about `range()` in Chapter 8.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Pick a table

**Goal:** Ask the customer to pick a table from 1 to 10. Keep asking until the answer is a whole number from 1 to 10, then confirm it.

**Expected output:**
```text
Pick a table, 1 to 10: six
Please type a whole number.
Pick a table, 1 to 10: 15
We have tables 1 to 10.
Pick a table, 1 to 10: 6
Table 6 is yours.
```

**Hint:** Use `while True` with `break` from Chapter 7. Check `isdigit()` before you call `int()`.

**AI variant:** Ask an AI assistant to list five answers that could break this program. Run each one and mark it as handled or not handled.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Three tries for the PIN

**Goal:** The manager's PIN is `2468`. Give three tries. After a wrong PIN, say how many tries are left. After the right PIN, print a welcome and stop asking.

**Expected output:**
```text
PIN: 1234
Wrong PIN. Tries left: 2
PIN: 2468
Welcome, manager.
```

**Hint:** Keep the PIN as text and compare text with `==`. Count every try, right or wrong.

**AI variant:** Ask an AI assistant to trace your loop for the answers 1, 1, 1. Check its trace: the loop must ask exactly three times.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Guess the cake price

**Goal:** The price of a cake is 4. Give up to four guesses with `Higher!` or `Lower!` hints. When the guess is right, say how many tries it took.

**Expected output:**
```text
Price of a cake: 6
Lower!
Price of a cake: 2
Higher!
Price of a cake: 4
Correct in 3 tries!
```

**Hint:** This is the loop from Step 2 of the project, with a different secret and a different number of tries.

**AI variant:** Ask an AI assistant for a test where the player uses all four tries and never wins. Run it and check that the program stops after the fourth guess.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Points for speed

**Goal:** Build a guessing game with the secret 13 and five tries. A win on the first guess scores 5 points, on the second 4, and so on. A player who never wins scores 0. Print the number of guesses and the points at the end.

**Expected output:**
```text
Your guess: 10
Too low!
Your guess: 15
Too high!
Your guess: 13
Guesses: 3. Points: 3
```

**Hint:** Start `points` at 0. When the guess is right, set it to `6 - tries`, then `break`.

**AI variant:** Ask an AI assistant to work out the points for a win on each try, 1 to 5. Check every row with your program.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's game

**Goal:** An AI assistant wrote a game that should give exactly three tries, and said it does. Find the mistake by counting the questions, then fix it.

```python
# illustrative
secret = 7
tries = 0
while tries <= 3:
    guess = int(input("Your guess: "))
    tries += 1
    if guess == secret:
        print("Correct!")
        break
    else:
        print(f"Wrong. Tries left: {3 - tries}")
```

**Expected output after the fix:**
```text
Your guess: 1
Wrong. Tries left: 2
Your guess: 2
Wrong. Tries left: 1
Your guess: 3
Wrong. Tries left: 0
```

**Hint:** Trace the loop with a table, as in Chapter 7. How many times is `tries <= 3` true?

**AI variant:** Paste the AI's code back into the AI with your trace table and the output you expected. Ask it to explain the cause before it shows a fix.

**Solution:** [solutions/task8.py](solutions/task8.py)
