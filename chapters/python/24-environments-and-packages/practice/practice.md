# Practice: Chapter 24

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match. Work in a folder with copies of the `.txt` files from `solutions/`. None of these tasks installs anything.

## Warm-up (10 XP each)

### Task 1: Count the packages

**Goal:** Read `requirements.txt` and count the package lines. Skip empty lines and lines that start with `#`.

**Run it:**
```bash
python task1.py
```

**Expected output:**
```text
Packages listed: 3
```

**Hint:** Use `read_text()` and `splitlines()`, then `strip()` each line before you test it.

**AI variant:** Ask an AI assistant what `startswith("#")` does on a line with spaces before the `#`. Test its answer with your own line.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Pinned or not?

**Goal:** Split the list `["rich==13.9.4", "tabulate", "requests>=2.31", "pytest==8.3.4"]` into pinned lines and lines that are not pinned. Print both lists.

**Run it:**
```bash
python task2.py
```

**Expected output:**
```text
Pinned: ['rich==13.9.4', 'pytest==8.3.4']
Not pinned: ['tabulate', 'requests>=2.31']
```

**Hint:** Two list comprehensions from Chapter 14, each with a condition at the end.

**AI variant:** Ask an AI whether `>=` pins a version. Check its answer against Step 5 of the lesson.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Which activate command?

**Goal:** Store the name of a system in a variable. Print the command that activates `.venv` on that system.

**Run it:**
```bash
python task3.py
```

**Expected output:**
```text
On Windows, type: .venv\Scripts\activate
```

**Hint:** Use `if` and `else`. In a Python string, write a backslash as `\\`.

**AI variant:** Ask an AI for the activate command on your own computer. Compare it with the table in Step 2.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Listed twice

**Goal:** Read `dup_requirements.txt`. Print every package that appears twice, ignoring capital letters, then the number of different packages.

**Run it:**
```bash
python task4.py
```

**Expected output:**
```text
Listed twice: requests
Different packages: 3
```

**Hint:** Keep the names you have seen in a set from Chapter 13. Compare names after `lower()`.

**AI variant:** Ask an AI why PyPI treats `Requests` and `requests` as the same name. Check the answer on the Python Packaging User Guide page about name normalization.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Laptop or home?

**Goal:** Compare `laptop_requirements.txt` with `home_requirements.txt`. Print each package whose version is different, with both versions.

**Run it:**
```bash
python task5.py
```

**Expected output:**
```text
requests: laptop 2.32.3, home 2.31.0
```

**Hint:** Write a function that reads a file into a dictionary of name and version, then use `get()`.

**AI variant:** Ask an AI which version Asha should keep. Then decide yourself, and say why: which one has her tests run on?

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Find the look-alikes

**Goal:** Check four suggested names against a trusted list. Print `trusted`, `look-alike of` a trusted name, or `unknown, check pypi.org` for each.

**Run it:**
```bash
python task6.py
```

**Expected output:**
```text
tabluate: look-alike of tabulate
rich: trusted
pytset: look-alike of pytest
flask: unknown, check pypi.org
```

**Hint:** Use `difflib.get_close_matches()` with `n=1` and `cutoff=0.8`.

**AI variant:** Ask an AI to suggest four packages for printing tables. Run every name through your program before you look any of them up.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Requirements as JSON

**Goal:** Read `requirements.txt` into a dictionary of name and version. Save it as `report.json` with an indent of 2, then print the file.

**Run it:**
```bash
python task7.py
```

**Expected output:**
```text
{
  "requests": "2.32.3",
  "tabulate": "0.9.0",
  "pytest": "8.3.4"
}
```

**Hint:** Use `json.dumps()` from Chapter 23 and `write_text()` with `encoding="utf-8"`.

**AI variant:** Ask an AI to write the same program. Check that its file opens with `json.load()` and gives the same dictionary.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's pin checker

**Goal:** An AI wrote `is_pinned(line)` as `return "=" in line` and said it finds pinned lines. Test it on `"requests>=2.31"`, then fix it and print the result for three lines.

**Run it:**
```bash
python task8.py
```

**Expected output:**
```text
tabulate==0.9.0  True
requests>=2.31   False
pytest           False
```

**Hint:** A line is pinned only when it contains two equals signs together.

**AI variant:** Show the AI its own function and the line `requests>=2.31`. Ask it to explain the cause before the fix. Did it name the `>=`?

**Solution:** [solutions/task8.py](solutions/task8.py)
