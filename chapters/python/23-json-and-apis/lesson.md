# Chapter 23: JSON and APIs: Talking to Other Programs

> Quest: save structured cafe data as JSON, read a saved response from a web service, and pick out exactly the values you need. Reward: 100 XP and the **Connector** badge.

## Learning goals

By the end of this chapter, you will be able to:

- Turn Python data into JSON text with `json.dumps()` and back with `json.loads()`.
- Save and load JSON files with `json.dump()` and `json.load()`, keeping accents with `ensure_ascii=False`.
- Explain how a web API answers a request: a URL, a status code and a JSON body.
- Read nested values from a saved API response, using `get()` for fields that may be missing.
- Ask an AI assistant to explain a JSON response, then check its code against the real data.

## Why this matters

At the end of Chapter 22, Asha's scores were safe in a CSV file. But a CSV row holds only flat values. Her quiz has a title, a pass mark and a list of questions, each with its own answer. That is data inside data.

**JSON** (JavaScript Object Notation) is a text format for structured data. It writes dictionaries, lists, text, numbers, true, false and null in a way that almost every programming language can read.

That is why programs talk to each other in JSON. A weather service, a payment system and a delivery app all send their answers as JSON text. If you can read JSON, your program can use their data.

## The idea

JSON looks almost like a Python dictionary, but it is text. Python's `json` module translates in both directions.

| JSON | Python |
|---|---|
| object `{"item": "Tea"}` | `dict` |
| array `["small", "large"]` | `list` |
| string `"Tea"` (double quotes only) | `str` |
| number `3.5` | `int` or `float` |
| `true` and `false` | `True` and `False` |
| `null` | `None` |

```text
   Python data          json.dumps()         JSON text
  {"vegan": True}   ------------------>   '{"vegan": true}'
                    <------------------
                        json.loads()
```

Read the names as "dump string" and "load string". The functions without the `s`, `json.dump()` and `json.load()`, work with a file instead of a string.

A **web API** (Application Programming Interface) is a service that other programs can ask for data. The conversation always has the same shape:

```text
  Your program                                   Weather service
  REQUEST:  GET https://api.example.com/weather?city=Riverside  -->
                                    <--  RESPONSE: status 200 OK
                                         body: {"current": {"temp_c": 31.5, ...}}
```

The **status code** says how the request went: `200` means OK, and `404` means "not found". The **body** holds the data, usually as JSON. Many services also ask for an API key, a secret password for programs. Keep it out of your code and out of AI chats.

Think of a JSON response as a delivery box with labelled compartments. You open the box, then the compartment, then the item: `data["current"]["temp_c"]`. The comparison stops working at one point: a real box can hide extra items, but a JSON response contains only the fields the service chose to send.

## Build it step by step

**Step 1: Turn a dictionary into JSON text.** `json.dumps()` returns a string.

```python
# file: examples/ex01_dumps.py
import json

menu = {"item": "Tea", "price": 3.5,
        "vegan": True, "offer": None}
text = json.dumps(menu)
print(text)
print(type(text))
```

<!-- output: examples/ex01_dumps.expected -->
```output
{"item": "Tea", "price": 3.5, "vegan": true, "offer": null}
<class 'str'>
```

`True` became `true`, and `None` became `null`. The result is a `str`, so you can save it in a file or send it to another program.

**Step 2: Turn JSON text into Python data.** Here is a saved file, `scone.json`:

```json
{
  "item": "Scone",
  "price": 2.75,
  "sizes": ["small", "large"],
  "vegan": false,
  "offer": null
}
```

```python
# file: examples/ex02_loads.py
import json
from pathlib import Path

path = Path("scone.json")
text = path.read_text(encoding="utf-8")
data = json.loads(text)
print(type(text), type(data))
print(data["sizes"][1])
print(data["vegan"], data["offer"])
print(data["offer"] is None)
```

<!-- output: examples/ex02_loads.expected -->
```output
<class 'str'> <class 'dict'>
large
False None
True
```

`read_text()` gives a string. `json.loads()` turns it into a dictionary, so `data["sizes"][1]` works like any list inside a dictionary. To check for `None`, write `is None`, as line 11 does. The style guide, PEP 8, recommends `is` for `None`.

**Step 3: Make JSON easy to read.** Two settings change how the text looks.

```python
# file: examples/ex03_pretty.py
import json

order = {"drink": "Café au lait", "cups": 2}
print(json.dumps(order))
print(json.dumps(order, ensure_ascii=False))
print(json.dumps(order, indent=2, ensure_ascii=False))
```

<!-- output: examples/ex03_pretty.expected -->
```output
{"drink": "Caf\u00e9 au lait", "cups": 2}
{"drink": "Café au lait", "cups": 2}
{
  "drink": "Café au lait",
  "cups": 2
}
```

By default, `json.dumps()` writes every character outside basic English as a code, so `é` becomes `\u00e9`. The data is still correct, but people cannot read it easily. `ensure_ascii=False` keeps the real character. `indent=2` puts each value on its own line, two spaces deeper for each level.

**Step 4: Save and load a JSON file.** Asha saves her quiz, with its list of questions, and loads it back.

```python
# file: examples/ex04_save_load.py
import json

questions = [
    {"ask": "Price of tea?", "answer": "3.50"},
    {"ask": "Which cake has nuts?", "answer": "carrot"},
]
quiz = {"title": "Menu quiz", "pass_mark": 2,
        "questions": questions}

with open("quiz.json", "w", encoding="utf-8") as file:
    json.dump(quiz, file, indent=2)

with open("quiz.json", encoding="utf-8") as file:
    loaded = json.load(file)

count = len(loaded["questions"])
print(loaded["title"], "has", count, "questions")
print(loaded["questions"][1]["ask"])
print(loaded == quiz)
```

<!-- output: examples/ex04_save_load.expected -->
```output
Menu quiz has 2 questions
Which cake has nuts?
True
```

`json.dump()` writes straight into the open file, and `json.load()` reads from it. The loaded dictionary is equal to the original, so nothing was lost. Always open JSON files with `encoding="utf-8"`, as in Chapter 21.

**Step 5: Read a saved API response.** On your own computer, a program can ask a real service for data. This fragment shows how, with the `urllib.request` module from the standard library. `api.example.com` is a placeholder, not a real weather service:

```python
# illustrative
import json
from urllib.request import urlopen

with urlopen("https://api.example.com/weather?city=Riverside") as response:
    print(response.status)
    data = json.load(response)
```

Live answers change every minute, so they cannot be checked against an expected output. Programmers save one real response as a file, called a **sample response**, and build and test their code on it. Here is Asha's sample, `weather_sample.json`:

```json
{
  "location": {"name": "Riverside"},
  "current": {"temp_c": 31.5, "condition": "Sunny"},
  "forecast": [
    {"hour": "12:00", "temp_c": 33.0, "rain_chance": 0},
    {"hour": "15:00", "temp_c": 34.5, "rain_chance": 10},
    {"hour": "18:00", "temp_c": 29.0, "rain_chance": 40}
  ]
}
```

```python
# file: examples/ex05_weather.py
import json
from pathlib import Path

path = Path("weather_sample.json")
data = json.loads(path.read_text(encoding="utf-8"))
place = data["location"]["name"]
print(place, data["current"]["temp_c"])
print(data["current"]["condition"])
for slot in data["forecast"]:
    print(slot["hour"], "rain:", slot["rain_chance"])
```

<!-- output: examples/ex05_weather.expected -->
```output
Riverside 31.5
Sunny
12:00 rain: 0
15:00 rain: 10
18:00 rain: 40
```

Follow the path from the outside in. `data["current"]` is a dictionary, so `["temp_c"]` comes next. `data["forecast"]` is a list, so you loop over it, and each `slot` is a dictionary.

**Step 6: Expect missing fields and bad text.** A service can leave a field out. `get()`, from Chapter 12, returns a default instead of crashing.

```python
# file: examples/ex06_safe_get.py
import json
from pathlib import Path

path = Path("weather_sample.json")
data = json.loads(path.read_text(encoding="utf-8"))
current = data["current"]
print(current.get("condition", "unknown"))
print(current.get("wind_kph", "not sent"))
print(current["wind_kph"])
```

<!-- error: examples/ex06_safe_get.expected_error -->
```output
Sunny
not sent
Traceback (most recent call last):
  File "ex06_safe_get.py", line 10, in <module>
    print(current["wind_kph"])
          ~~~~~~~^^^^^^^^^^^^
KeyError: 'wind_kph'
```

Use square brackets for fields the service always sends, and `get()` for fields that may be missing. Text that is not valid JSON raises `json.JSONDecodeError`, which you catch with `try`, as in Chapter 22:

```python
# file: examples/ex07_bad_json.py
import json

texts = ['{"item": "Tea"}', "{'item': 'Tea'}", ""]
for text in texts:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        print("Not valid JSON:", error.msg)
    else:
        print("Loaded:", data["item"])
```

<!-- output: examples/ex07_bad_json.expected -->
```output
Loaded: Tea
Not valid JSON: Expecting property name enclosed in double quotes
Not valid JSON: Expecting value
```

JSON allows only double quotation marks, so the second text fails. The third is empty, which happens when a service sends no body. `error.msg` holds the short reason.

## See the outcome

Asha's daily board reads the saved weather response, chooses the drink of the day, lists the rainy hours and saves the board as JSON for the cafe screen.

```python
# file: examples/ex08_daily_board.py
import json
from pathlib import Path


def load_json(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


weather = load_json("weather_sample.json")
temp = weather["current"]["temp_c"]
drink = "Iced tea" if temp >= 30 else "Hot tea"
rain = [slot["hour"] for slot in weather["forecast"]
        if slot["rain_chance"] >= 30]
board = {"drink": drink, "temp_c": temp,
         "rain_hours": rain, "tip": "Café au lait"}

text = json.dumps(board, indent=2, ensure_ascii=False)
Path("board.json").write_text(text, encoding="utf-8")
print(Path("board.json").read_text(encoding="utf-8"))
```

<!-- output: examples/ex08_daily_board.expected -->
```output
{
  "drink": "Iced tea",
  "temp_c": 31.5,
  "rain_hours": [
    "18:00"
  ],
  "tip": "Café au lait"
}
```

The program reads JSON, picks out the values it needs, and writes new JSON that another program, such as the cafe's screen, can read. When Asha replaces the sample with a live response, the rest of the code stays the same.

## Work with AI

The AI skill for this chapter is explaining a JSON response. Paste a sample response into an AI assistant, ask it to describe the structure, then ask for code that extracts a field. Check every field name and every path against the real sample, and run the code.

Never paste an API key, a password or private customer data. A sample response from a public service is fine. Remove anything personal before you paste.

| Stage | How to use AI in this chapter |
|---|---|
| Plan | Paste the sample and ask the AI to describe its structure: which parts are objects, lists, strings and numbers. |
| Write | Write your own extraction code first, then ask the AI which line handles a missing item. |
| Generate | Ask for a function from a clear description, and ask what it returns for a named item. Run it on the sample. |
| Test | Run your cases on the AI's code, with the exact value and type you expect. |
| Debug | Paste the code, the new response and the full error. Ask for the cause before the fix. |
| Improve | Ask for one improvement, then check every field name it uses against the sample. |

The full prompts are in [ai-prompts.md](ai-prompts.md).

**AI pair moment.** Asha's milk supplier has a price API. She saved its answer as `prices.json`:

```json
{
  "supplier": "Fresh Farm",
  "currency": "USD",
  "items": [
    {"name": "milk", "price": "1.20", "unit": "litre"},
    {"name": "oat milk", "price": "1.85", "unit": "litre"},
    {"name": "butter", "price": "3.40", "unit": "pack"}
  ]
}
```

She asked an AI assistant: "Write price_of(data, name) for this response. It returns the price of the named item as a number. What does it return for milk?" The AI answered with this code and said it returns `1.2`.

```python
# file: examples/ai_price_flawed.py
import json
from pathlib import Path


def price_of(data, name):
    return float(data["items"][name]["price"])


text = Path("prices.json").read_text(encoding="utf-8")
data = json.loads(text)
print(price_of(data, "milk"))
```

<!-- error: examples/ai_price_flawed.expected_error -->
```output
Traceback (most recent call last):
  File "ai_price_flawed.py", line 12, in <module>
    print(price_of(data, "milk"))
          ~~~~~~~~^^^^^^^^^^^^^^
  File "ai_price_flawed.py", line 7, in price_of
    return float(data["items"][name]["price"])
                 ~~~~~~~~~~~~~^^^^^^
TypeError: list indices must be integers or slices, not str
```

The AI treated `items` as a dictionary of names. In the sample, `items` is a list, so it needs a number, not `"milk"`. Asha told the AI the error. Its next version looped over the list, but returned the price as text, `'1.20'`. Her test cases caught that too, because they compare the exact value and type:

```python
# file: examples/ai_tests_flawed.py
import json
from pathlib import Path


def price_of(data, name):
    for item in data["items"]:
        if item["name"] == name:
            return item["price"]
    return None


text = Path("prices.json").read_text(encoding="utf-8")
data = json.loads(text)
cases = [("milk", 1.2), ("oat milk", 1.85),
         ("flour", None)]
for name, expected in cases:
    got = price_of(data, name)
    result = "pass" if got == expected else "FAIL"
    print(f"{name}: got {got!r}, {result}")
```

<!-- output: examples/ai_tests_flawed.expected -->
```output
milk: got '1.20', FAIL
oat milk: got '1.85', FAIL
flour: got None, pass
```

This supplier sends prices as strings, with quotation marks. Adding `float()` fixed it, and every case passed:

```python
# file: examples/ai_tests_fixed.py
import json
from pathlib import Path


def price_of(data, name):
    for item in data["items"]:
        if item["name"] == name:
            return float(item["price"])
    return None


text = Path("prices.json").read_text(encoding="utf-8")
data = json.loads(text)
cases = [("milk", 1.2), ("oat milk", 1.85),
         ("flour", None)]
for name, expected in cases:
    got = price_of(data, name)
    result = "pass" if got == expected else "FAIL"
    print(f"{name}: got {got!r}, {result}")
```

<!-- output: examples/ai_tests_fixed.expected -->
```output
milk: got 1.2, pass
oat milk: got 1.85, pass
flour: got None, pass
```

Two habits caught both mistakes: reading the sample yourself, and testing the exact value and type.

## Common mistakes

**Mistake 1: single quotation marks in JSON.** Python accepts both kinds of quotation marks. JSON accepts only double ones.

```python
# file: examples/err01_single_quotes.py
import json

text = "{'item': 'Tea', 'price': 3.5}"
data = json.loads(text)
print(data["item"])
```

<!-- error: examples/err01_single_quotes.expected_error -->
```output
Traceback (most recent call last):
  File "err01_single_quotes.py", line 5, in <module>
    data = json.loads(text)
  ...
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
```

The report goes on through the `json` module's own files, shown here as `...`. Read the last line: column 2 is the first `'`. Fix: write the JSON with double quotation marks, or build the data in Python and use `json.dumps()`.

**Mistake 2: `json.dump()` without a file.** `json.dump()` writes into a file, so it needs one. To get a string, use `json.dumps()`.

```python
# file: examples/err02_dump_no_file.py
import json

order = {"drink": "Tea", "cups": 2}
text = json.dump(order)
print(text)
```

<!-- error: examples/err02_dump_no_file.expected_error -->
```output
Traceback (most recent call last):
  File "err02_dump_no_file.py", line 5, in <module>
    text = json.dump(order)
TypeError: dump() missing 1 required positional argument: 'fp'
```

`fp` is the name of the file parameter. Fix: `text = json.dumps(order)`.

**Mistake 3: using the text as if it were a dictionary.** `read_text()` gives a string. Square brackets with a name do not work on a string.

```python
# file: examples/err03_text_not_dict.py
from pathlib import Path

path = Path("scone.json")
text = path.read_text(encoding="utf-8")
print(text["item"])
```

<!-- error: examples/err03_text_not_dict.expected_error -->
```output
Traceback (most recent call last):
  File "err03_text_not_dict.py", line 6, in <module>
    print(text["item"])
          ~~~~^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

Fix: turn the text into data first with `json.loads(text)`.

**Mistake 4: number keys come back as strings.** JSON object keys are always strings. A dictionary with number keys does not survive the trip unchanged.

```python
# file: examples/err04_keys_strings.py
import json

tables = {1: "Asha", 2: "Omar"}
back = json.loads(json.dumps(tables))
print(back)
print(back[1])
```

<!-- error: examples/err04_keys_strings.expected_error -->
```output
{'1': 'Asha', '2': 'Omar'}
Traceback (most recent call last):
  File "err04_keys_strings.py", line 7, in <module>
    print(back[1])
          ~~~~^^^
KeyError: 1
```

Fix: use string keys from the start, such as `"table_1"`, or look up `back["1"]`.

## Think beyond

1. Some weather services send the temperature in Fahrenheit for some cities. How could your code know which unit a response uses, and what would you look for in the sample?
2. Why is it better to test your extraction code on a saved sample response than on the live service? Think about results that change, and about tests that must give the same answer every time.

## Recap

- JSON is text for structured data. `json.dumps()` turns Python data into JSON text, and `json.loads()` turns it back.
- `json.dump()` and `json.load()` work with an open file. Use `encoding="utf-8"`, and `ensure_ascii=False` to keep accents.
- `true`, `false` and `null` become `True`, `False` and `None`. Check for `None` with `is None`.
- A web API answers a request with a status code and a body, usually JSON. Build and test on a saved sample response.
- Follow the path from the outside in, and use `get()` for fields that may be missing.
- Check every field name and type an AI uses against the real sample, then run your test cases.

You earned **100 XP** and the **Connector** badge.

## Practice

Open [practice/practice.md](practice/practice.md). Complete the warm-up tasks before the apply tasks.

## What's next

In Chapter 24, you will create a virtual environment and install packages such as `requests` safely, after checking that each package is real and trustworthy.
