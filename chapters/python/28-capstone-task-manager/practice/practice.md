# Practice: Chapter 28

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: Make a task

**Goal:** Write a `Task` data class with a title, a priority (default 2) and `done` (default `False`). Create two tasks and print them. Then check that two tasks with the same values are equal.

**Expected output:**
```text
Task(title='Open the cafe', priority=1, done=False)
Task(title='Wipe the tables', priority=2, done=False)
True
```

**Hint:** A data class writes `__init__`, a print form and `==` for you, as in Chapter 26.

**AI variant:** Ask an AI assistant what `print()` shows for a data class. Predict it, then run it.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: JSON there and back

**Goal:** Save a list of two task dictionaries as JSON text with `json.dumps()`, load it again with `json.loads()`, and print each title and whether it is done.

**Expected output:**
```text
[{"title": "Restock milk", "priority": 2, "done": false}, {"title": "Call the supplier", "priority": 3, "done": true}]
Restock milk done: False
Call the supplier done: True
```

**Hint:** JSON writes `True` as `true`. After `json.loads()`, it is `True` again.

**AI variant:** Ask an AI assistant which Python types JSON can save. Check its answer by trying to save a set.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: One task line

**Goal:** Write a function `task_line(number, title, done)` that returns a line such as `1. [x] Open the cafe`.

**Expected output:**
```text
1. [x] Open the cafe
2. [ ] Restock milk
```

**Hint:** Use `"x" if done else " "`, as in Chapter 14.

**AI variant:** Ask an AI assistant to write the function. Run it with `done` set to `False` and check the space between the brackets.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Remove a task

**Goal:** Give a small task list a `remove(number)` method. The number counts from 1. It returns the removed title, and raises `ValueError` when there is no task with that number.

**Expected output:**
```text
Removed: Restock milk
['Open the cafe', 'Call the supplier']
Refused: there is no task 5
```

**Hint:** `pop(number - 1)` removes and returns the item at that position.

**AI variant:** Ask an AI assistant for this method. Test it with the number of the last task, and with a number that is too big.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Open and done

**Goal:** Write `summary(tasks)` that returns a line such as `2 open, 1 done`. Check it with three tasks and with an empty list.

**Expected output:**
```text
2 open, 1 done
0 open, 0 done
```

**Hint:** Count the done tasks with a comprehension, then subtract.

**AI variant:** Ask an AI assistant for test cases for `summary()`. Check that its list includes an empty list.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Most important first

**Goal:** Print every task, priority 1 first, then 2, then 3, keeping the order inside each priority.

**Expected output:**
```text
P1 Open the cafe
P1 Bake scones
P2 Restock milk
P3 Call the supplier
```

**Hint:** Loop over the priorities 1, 2 and 3, and inside that loop, over the tasks.

**AI variant:** Ask an AI assistant for a shorter way. Run both versions and compare every line of output.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Load without crashing

**Goal:** Write `load_titles(path)`. A missing file or an empty file gives an empty list. Otherwise, return the titles saved in the JSON file.

**Expected output:**
```text
[]
[]
['Tea', 'Cake']
```

**Hint:** Catch `FileNotFoundError` for the missing file, and check `text.strip()` for the empty one.

**AI variant:** Ask an AI assistant to write the function, then run it on an empty file. Does it crash? Fix it the way Asha did.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Clear the done tasks

**Goal:** Write `clear_done(tasks)` that returns the open tasks and how many done tasks it removed. Run it twice, and check it with an empty list.

**Expected output:**
```text
Removed: 2
['Restock milk']
Removed: 0
All checks passed
```

**Hint:** Build the new list with a comprehension. The count is the old length minus the new length.

**AI variant:** Ask an AI assistant to review your function and suggest one improvement. Run your checks on its version before you accept it.

**Solution:** [solutions/task8.py](solutions/task8.py)
