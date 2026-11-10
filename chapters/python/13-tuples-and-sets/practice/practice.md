# Practice: Chapter 13

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: Weekend hours

**Goal:** At the weekend, the Corner Cafe opens at 9 and closes at 16. Store the hours in a tuple, unpack them into two variables and print them. Then print how many values the tuple holds.

**Expected output:**
```text
Weekend: 9:00 to 16:00
Values: 2
```

**Hint:** Write `opens, closes = weekend`. `len()` works on a tuple.

**AI variant:** Ask an AI assistant what happens if you unpack a tuple of 2 values into 3 names. Check its answer with a run.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Different visitors

**Goal:** Start with `["Ravi", "Lina", "Ravi", "Omar", "Lina", "Ravi"]`. Print the number of visits, the number of different visitors and their names in alphabetical order.

**Expected output:**
```text
Visits: 6
Different: 3
['Lina', 'Omar', 'Ravi']
```

**Hint:** `set(names)` removes the repeats. Print `sorted(...)` for a fixed order.

**AI variant:** Ask an AI assistant why printing a set directly can show the names in a different order. Check the answer against Step 4 of the lesson.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Unpack a menu item

**Goal:** A menu item is the tuple `("Muffin", 3.25, True)`: its name, its price and whether it is vegan. Unpack it into three variables and print two lines.

**Expected output:**
```text
Muffin costs 3.25
Vegan: True
```

**Hint:** Three values need three names on the left of `=`.

**AI variant:** Before you run your code, ask an AI assistant to predict the output. Compare its prediction with your run.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: The lunch specials

**Goal:** Store four lunch specials as a list of tuples: soup 5.5, salad 7.0, toast 3.25 and juice 3.0. Print each one lined up, then the number of items and the total.

**Expected output:**
```text
Soup      5.50
Salad     7.00
Toast     3.25
Juice     3.00
Items        4
Total    18.75
```

**Hint:** Use `for name, price in specials:` and the alignment codes from Chapter 3, such as `<8` and `>6.2f`.

**AI variant:** Ask an AI assistant to compare a list of tuples with a dictionary for this menu, with one strength and one weakness each. Which one would you choose if you often look up a price by name?

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Monday and Tuesday

**Goal:** Monday's customers were Omar, Lina, Sam and Zoe. Tuesday's were Lina, Ravi and Zoe. Print who came on both days, who came only on Monday, and how many different customers came in all.

**Expected output:**
```text
Both days: ['Lina', 'Zoe']
Only Monday: ['Omar', 'Sam']
Everyone: 5
```

**Hint:** Use `&`, `-` and `|`. `len()` counts the items in a set.

**AI variant:** Ask an AI assistant which operator gives "only Monday". Then swap the two sets in your code and explain why the answer changes.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Allergy check

**Goal:** The cake contains egg, milk and wheat. The scone contains milk and wheat. Store each list of allergens as a set. Check which dish contains egg, then print the allergens in either dish and those only in the cake.

**Expected output:**
```text
Cake has egg: True
Scone has egg: False
In either: ['egg', 'milk', 'wheat']
Only in cake: ['egg']
```

**Hint:** `"egg" in cake` gives `True` or `False`.

**AI variant:** Ask an AI assistant for two more checks a customer with allergies might need. Write them and run them.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Welcome and reward

**Goal:** Today's visits are `["Omar", "lina", "Omar", "Sam ", "Lina", "Omar", "Lina", "sam"]`. Clean each name, welcome each customer the first time they appear, count every visit, and give a free tea to everyone with 3 or more visits.

**Expected output:**
```text
Welcome, Omar!
Welcome, Lina!
Welcome, Sam!
Free tea for: ['Lina', 'Omar']
```

**Hint:** Use `strip().title()` on each name, a set for the names you have seen, and a dictionary from Chapter 12 for the counts.

**AI variant:** Ask an AI assistant for test cases, including an empty day and a name with spaces. Run each one and write pass or fail.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's set code

**Goal:** An AI assistant wrote this code to count the different items ordered today and show the first one in alphabetical order. It said the output would be `Different items: 3` and `First in order: cake`. Instead, the program stops with errors. Find both mistakes and fix them.

```python
# illustrative: the AI's version
orders = ["tea", "cake", "tea", "scone", "cake"]
items = {}
for item in orders:
    items.add(item)
first = items[0]
print(f"Different items: {len(items)}")
print(f"First in order: {first}")
```

**Expected output:**
```text
Different items: 3
First in order: cake
```

**Hint:** What does `{}` make? Does a set have positions? Fix one error, run it, then fix the next.

**AI variant:** Paste the code and the first error into an AI assistant. Ask for the cause before the fix. Did it also find the second mistake before you ran the code again?

**Solution:** [solutions/task8.py](solutions/task8.py)
