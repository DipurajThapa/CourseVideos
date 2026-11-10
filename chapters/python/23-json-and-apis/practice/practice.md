# Practice: Chapter 23

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match. Work in a folder with copies of the `.json` files from `solutions/`.

## Warm-up (10 XP each)

### Task 1: Turn the special into JSON

**Goal:** Make a dictionary for today's special with a name `"Carrot cake"`, a price `3.2` and `"nuts"` set to `True`. Print it as JSON text.

**Run it:**
```bash
python task1.py
```

**Expected output:**
```text
{"name": "Carrot cake", "price": 3.2, "nuts": true}
```

**Hint:** `json.dumps()` turns a dictionary into a string. Look at how `True` is written in the output.

**AI variant:** Ask an AI assistant how JSON writes `True`, `False` and `None`. Run your program to check its answer.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: Read the opening hours

**Goal:** Read `hours.json` and print one sentence with the opening time, the closing time and the first closed day.

**Run it:**
```bash
python task2.py
```

**Expected output:**
```text
Open 08:00 to 18:00, closed on Sunday
```

**Hint:** Read the text with `Path.read_text()`, then turn it into a dictionary with `json.loads()`. `closed_days` is a list.

**AI variant:** Paste `hours.json` into an AI assistant and ask which Python type each value becomes. Check its answer with `type()`.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Predict the types

**Goal:** Load the JSON text `[1, 2.5, "3", true, null]` with `json.loads()`. Loop over the list and print each value with its Python type. Predict every line before you run it.

**Run it:**
```bash
python task3.py
```

**Expected output:**
```text
1 <class 'int'>
2.5 <class 'float'>
3 <class 'str'>
True <class 'bool'>
None <class 'NoneType'>
```

**Hint:** Quotation marks in JSON make a string, even when the string holds digits.

**AI variant:** Ask an AI assistant to predict the five lines. Compare its prediction with your own and with the real run.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: Save the order

**Goal:** Save the order `{"table": 4, "items": ["tea", "scone"], "paid": False}` to `order.json` with an indent of 2. Then read the file back and print its text.

**Run it:**
```bash
python task4.py
```

**Expected output:**
```text
{
  "table": 4,
  "items": [
    "tea",
    "scone"
  ],
  "paid": false
}
```

**Hint:** `json.dumps(order, indent=2)` gives the text. `Path.write_text()` saves it, with `encoding="utf-8"`.

**AI variant:** Ask an AI assistant for the difference between `json.dump()` and `json.dumps()`. Use each one once and check that both files are the same.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: Today's rain hours

**Goal:** Read the saved weather response `weather_sample.json`. Print the hours where `rain_chance` is 30 or more. If there are none, print "No rain expected."

**Run it:**
```bash
python task5.py
```

**Expected output:**
```text
Rain likely at: ['18:00']
```

**Hint:** `forecast` is a list of dictionaries. A comprehension with a filter, from Chapter 14, collects the hours.

**AI variant:** Ask an AI assistant to write this program from the sample file. Change one `rain_chance` to 35 and check that its program and yours still agree.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: A safe JSON loader

**Goal:** Write `load_json(path)`. It returns the data, or prints a clear message and returns `None` when the file is missing or is not valid JSON. Run it on `good.json`, `missing.json` (which does not exist) and `broken.json`.

**Run it:**
```bash
python task6.py
```

**Expected output:**
```text
good.json -> {'special': 'Carrot cake', 'price': 3.2}
No file called missing.json
missing.json -> None
broken.json is not valid JSON: Expecting property name enclosed in double quotes
broken.json -> None
```

**Hint:** Catch `FileNotFoundError` and `json.JSONDecodeError` in two separate `except` blocks, as in Chapter 22.

**AI variant:** Ask an AI assistant to list what else could go wrong when loading a JSON file. Make a small file for one of its cases and test your function on it.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: Prices in other currencies

**Goal:** `rates_sample.json` is a saved response from an exchange rate service. Its rates are strings. Print the price of tea (3.5) and a scone (2.75) in USD, EUR and GBP, with two decimal places.

**Run it:**
```bash
python task7.py
```

**Expected output:**
```text
Tea: USD 3.50, EUR 3.22, GBP 2.77
Scone: USD 2.75, EUR 2.53, GBP 2.17
```

**Hint:** Turn each rate into a number with `float()` before you multiply.

**AI variant:** Paste `rates_sample.json` into an AI assistant and ask for the code. Check whether it remembered that the rates are strings.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's temperature reader

**Goal:** An AI assistant wrote this function for the weather sample, and said it returns the current temperature:

```python
# illustrative
def current_temp(data):
    return data["current"]["temperature"]
```

The field is not in the sample. Write a fixed `current_temp(data)` that reads the real field, and returns `None` when the response has no `current` part. Test it on the sample and on `{"location": {"name": "Hilltop"}}`.

**Run it:**
```bash
python task8.py
```

**Expected output:**
```text
31.5
None
```

**Hint:** Open the sample and read the exact field names. `get()` with a default of an empty dictionary lets you chain a second `get()`.

**AI variant:** Show the AI its code and the sample, and ask it to find its own mistake. Did it name the missing field?

**Solution:** [solutions/task8.py](solutions/task8.py)
