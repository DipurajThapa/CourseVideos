# Practice: Chapter 17

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names, messages and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: A local message

**Goal:** Write a function `greeting(name)` that builds the text `Welcome to the Corner Cafe, <name>!` in a local variable and returns it. Print the greeting for Lina and for Omar.

**Expected output:**
```text
Welcome to the Corner Cafe, Lina!
Welcome to the Corner Cafe, Omar!
```

**Hint:** The variable inside the function disappears when the function ends, so `return` it and print the call.

**AI variant:** Ask an AI assistant whether your local variable can be printed outside the function. Then try it and read the error.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: A default size

**Goal:** Write `tea_price(size="small")`. It returns `3.5` for `"large"` and `3.0` for anything else. Print `tea_price()`, `tea_price("large")` and `tea_price(size="small")`.

**Expected output:**
```text
3.0
3.5
3.0
```

**Hint:** The first call leaves out the argument, so `size` gets its default value.

**AI variant:** Ask an AI assistant which of your three calls uses a keyword argument. Check its answer against step 5 of the lesson.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Predict the hidden link

**Goal:** Use a global `rate = 1.1` and a function `with_tax(price)` that returns `round(price * rate, 2)`. Print `with_tax(10.0)`, then set `rate = 1.2`, print `with_tax(10.0)` again, and print `round(10.0 * rate, 2)`. Predict all three lines first.

**Expected output:**
```text
11.0
12.0
12.0
```

**Hint:** The function reads `rate` when it runs, not when it is defined.

**AI variant:** Ask an AI assistant to rewrite `with_tax()` so its result depends only on its parameters. Check that it uses a default argument, not the `global` keyword.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Count visits without a global

**Goal:** Write `add_visit(visits)` that returns `visits + 1`. Start with `visits = 0`, call the function three times, storing the result each time, and print the count.

**Expected output:**
```text
Visits today: 3
```

**Hint:** Write `visits = add_visit(visits)`. The function never changes the global variable itself.

**AI variant:** Show an AI assistant a version that changes `visits` inside the function and gives an `UnboundLocalError`. Ask for the cause first, then a fix without `global`.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: A receipt line with keywords

**Goal:** Write `receipt_line(item, price, qty=1, currency="USD")` that returns a line such as `2 x Cake     USD  8.00`. Call it with only the item and price, with `qty=2`, with `currency="EUR"`, and with every argument named in a different order.

**Expected output:**
```text
1 x Tea      USD  3.50
2 x Cake     USD  8.00
1 x Scone    EUR  2.75
3 x Biscuit  USD  4.50
```

**Hint:** Use the format codes from Chapter 3: `{item:<8}` and `{price * qty:>5.2f}`.

**AI variant:** Ask an AI assistant to predict your four lines. Check the spaces in its answer against your real output.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: One job each

**Goal:** Write `order_total(prices)`, which returns the rounded total, and `summary_text(name, total)`, which returns `<name> pays <total>` with two decimal places. Print the summary for Lina's order `[3.5, 4.0, 2.75]`, then two checks: the total equals `10.25`, and an empty order totals `0`.

**Expected output:**
```text
Lina pays 10.25
True
True
```

**Hint:** Neither function prints. Only the main code prints.

**AI variant:** Ask an AI assistant to merge your two functions into one. Explain in one sentence why the split version is easier to test.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: The week report

**Goal:** Write `day_total(prices, rate=1.1)`, which adds tax to each price, and `week_lines(days, rate=1.1)`, which takes a dictionary of day names and price lists and returns a list of report lines, ending with a week total. Print the lines for Monday `[3.5, 4.0, 2.75]`, Tuesday `[4.25, 3.5]` and an empty Sunday.

**Expected output:**
```text
Monday    11.28
Tuesday    8.53
Sunday     0.00
Week      19.81
```

**Hint:** Inside `week_lines()`, keep a local list and a local week total, and `return` the list at the end. Round each taxed price, as in the lesson.

**AI variant:** Ask an AI assistant for three test cases for `week_lines()`, including an empty dictionary. Run each one and mark it pass or FAIL.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's loyalty card

**Goal:** An AI assistant wrote `add_stamp(card=[])`, which appends `"stamp"` and returns the card. With it, a stamp for Omar also appears on Lina's card. Rewrite the function without a default list, give Lina two stamps and Omar one, and print both counts.

**Expected output:**
```text
Lina stamps: 2
Omar stamps: 1
```

**Hint:** Pass a new empty list, `[]`, when a customer gets their first stamp.

**AI variant:** Show the AI's version and its wrong output to an AI assistant. Ask it to explain why the two customers share one card. Check that it says the default list is created once.

**Solution:** [solutions/task8.py](solutions/task8.py)
