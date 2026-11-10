# Practice: Chapter 18

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: Enough tables

**Goal:** 30 guests are coming to the Corner Cafe, and each table seats 4. Use the `math` module to print how many tables Asha needs (round up) and how many tables will be completely full (round down).

**Expected output:**
```text
Tables needed: 8
Full tables: 7
```

**Hint:** `math.ceil()` rounds up and `math.floor()` rounds down. Divide the guests by the seats per table first.

**AI variant:** Ask an AI assistant which function of the `math` module rounds down. Then find that function in the official documentation of the `math` module.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Three imports, one answer

**Goal:** Print the square root of 81 three times: once after `import math`, once after `from math import sqrt` and once after `import math as m`.

**Expected output:**
```text
9.0
9.0
9.0
```

**Hint:** Each import style changes only how you write the call, not the result.

**AI variant:** Ask an AI assistant which of the three styles PEP 8 prefers and why. Check the answer against the "Imports" section of PEP 8.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Parts of a file name

**Goal:** Build the path `menus/winter_menu.txt` with `Path` and the `/` operator. Print its name, its stem and its suffix.

**Expected output:**
```text
winter_menu.txt
winter_menu
.txt
```

**Hint:** Import `Path` from `pathlib`. No file needs to exist for this task.

**AI variant:** Ask an AI assistant what `Path("menus/winter_menu.txt").parent` gives. Predict it, then run it.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Your own price module

**Goal:** Write a module `price_tools.py` with a function `discount(price, percent)` that returns the price after the discount, rounded to cents. Add a guarded check that prints `True` when you run the module itself. Then write a second program that imports `discount` and prints the discounted prices of a cake (4.0, 10 percent) and a sandwich (6.5, 20 percent).

**Expected output (the second program):**
```text
Cake: 3.6
Sandwich: 5.2
```

**Hint:** Put both files in the same folder. Put the check under `if __name__ == "__main__":` so it does not print in the second program.

**AI variant:** Ask an AI assistant to write the guard line for you. Run your second program and check that the module's check line does not appear.

**Solution:** [solutions/price_tools.py](solutions/price_tools.py) and [solutions/task4.py](solutions/task4.py)

### Task 5: Shift length

**Goal:** A shift starts 7 hours 30 minutes after midnight and ends 16 hours after midnight. Use `timedelta` to print the length of the shift and the number of minutes.

**Expected output:**
```text
Shift: 8:30:00
Minutes: 510.0
```

**Hint:** You can subtract one `timedelta` from another.

**AI variant:** Ask an AI assistant how to get the number of minutes from a `timedelta`. Find the method it names in the official documentation of the `datetime` module.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Drink of the day

**Goal:** Use `random.choice()` to pick a drink of the day for Monday, Tuesday and Wednesday from Tea, Coffee and Juice. Call `random.seed(3)` first, so your program gives the same picks every time you run it.

**Expected output:**
```text
Monday Tea
Tuesday Juice
Wednesday Juice
```

**Hint:** A seed makes the same "random" choices come back on every run of the same Python. Your picks may differ on another version, but they repeat every run.

**AI variant:** Ask an AI assistant which function of the `random` module picks one item from a list. Confirm it in the official documentation before you use it.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: The supply order

**Goal:** Asha needs 40 biscuits (12 per box), 75 cups (50 per pack) and 130 napkins (100 per pack). Store the amounts and the pack sizes in two dictionaries and print how many boxes of each to order, in a neat table.

**Expected output:**
```text
biscuits    40 -> 4 boxes
cups        75 -> 2 boxes
napkins    130 -> 2 boxes
```

**Hint:** Loop over the first dictionary with `items()` and look up the pack size in the second. Round up with `math.ceil()`.

**AI variant:** Ask an AI assistant to predict the three lines before you run your program. Mark each prediction right or wrong.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's cake planner

**Goal:** An AI assistant wrote this function to find how many whole cakes give enough slices, with 8 slices per cake:

```text
import math

def cakes_to_bake(slices, per_cake=8):
    return math.round_up(slices / per_cake)
```

Find the problem in the official documentation of the `math` module, fix the function, add a docstring, and print the results for 20, 16 and 1 slices.

**Expected output:**
```text
3
2
1
```

**Hint:** Run the AI's version first and read the last line of the error. Then search the `math` page for a function that rounds up.

**AI variant:** Paste the error to an AI assistant and ask for the cause before the fix. Did it name a function that really exists?

**Solution:** [solutions/task8.py](solutions/task8.py)
