# Chapter 20: Boss Level 4: The Tested Quiz App

> Quest: build a staff quiz from three modules, write its tests before its code, and let the tests judge every line an AI writes. Reward: 300 XP and the **Software Builder** badge.

## The mission

New staff at the Corner Cafe keep asking the same questions. How much is a scone? Which cake has nuts? Is the soup vegan? A wrong answer about nuts is not only embarrassing. It can make a customer ill.

Asha wants a short quiz that new staff can take on the cafe laptop. It asks four questions, says if each answer is right, and prints a score with a grade at the end.

This time she works like a software team. She writes the tests first, before any rules exist. Then she lets an AI assistant help with the code, and her tests decide if the code is right. This boss level uses everything from Module 4:

| Chapter | What you use from it |
|---|---|
| 16 | Functions with parameters, `return` values and docstrings |
| 17 | Pure functions with one job each: no `input()` and no `print()` inside the rules |
| 18 | Your own modules, imported with `from ... import ...` |
| 19 | A `pytest` file written first, run with `-q`, and a report you can read |
| New | Two more `pytest` options: `--tb=no` hides the details, and `-rf` lists each failed test on one line |

## What you will build

Three files that work together, plus one test file:

| File | Its one job |
|---|---|
| `quiz_data.py` | Holds the questions and answers, as a list of dictionaries |
| `quiz_logic.py` | Holds the rules: check an answer, work out the percentage, the grade and the last line |
| `quiz_app.py` | Asks the questions and prints the results |
| `test_quiz_logic.py` | Eight tests for the rules, written before the rules |

Here is one run. The text after each question is what a new member of staff typed.

<!-- output: project/quiz_app.expected -->
```output
Price of a tea? 3.50
Correct!
Which cake has nuts? carrot
Correct!
Is the soup vegan? no
The answer is yes
Price of a scone? 2.75
Correct!
Score: 3/4 (75%) Ready
```

The soup is vegan, so `no` was wrong. Three answers out of four is 75 percent, which is the grade Ready.

## Acceptance criteria

Your quiz is finished when all of these are true:

1. The questions live in `quiz_data.py`, as a list of dictionaries with a question and an answer.
2. The rules live in `quiz_logic.py`, and no rule calls `input()` or `print()`.
3. An answer counts as right when it matches after removing spaces and ignoring capitals. A blank answer is wrong.
4. The percentage is a whole number, rounded. 75 or more is Ready, 50 or more is Almost, and anything lower is Practise again.
5. The last line looks like `Score: 3/4 (75%) Ready`.
6. You wrote `test_quiz_logic.py` before the rules, and all eight tests pass.
7. You ran the app with at least four sets of typed answers whose results you knew in advance.

## Plan it with AI

Before any code, Asha asked an AI assistant to plan the program. This is the AI skill of this chapter: plan the tests, let AI help with the code, and let the tests decide.

> "I am a beginner. I know functions, modules and pytest. I want a staff quiz with four questions, a check for each answer, a percentage and a grade. I will write the tests first. Do not write code. List the functions I need, and say which file each one goes in."

An example answer looked like this:

> Use three files. In `quiz_logic.py`, write `ask_and_check(question)`: it asks the question with `input()`, checks the answer and returns True or False. Add `percentage()`, `grade()` and `result_line()`. Keep the questions in `quiz_data.py` and the main loop in `quiz_app.py`.

Three files and four functions sound right. Asha checked `ask_and_check()` against Chapter 17. It does two jobs, and one of them waits for a person to type. A test cannot type an answer, so a test cannot check it. She kept the AI's file plan and the last three functions, and replaced the first with a pure function, `check_answer(given, correct)`. The app asks the question, and the rule only compares.

## Build it step by step

**Step 1: Put the questions in their own module.** Each question is a dictionary with two keys, and the list keeps them in order.

```python
# file: project/quiz_data.py
"""Questions for the Corner Cafe staff quiz."""
QUESTIONS = [
    {"question": "Price of a tea?", "answer": "3.50"},
    {"question": "Which cake has nuts?", "answer": "carrot"},
    {"question": "Is the soup vegan?", "answer": "yes"},
    {"question": "Price of a scone?", "answer": "2.75"},
]
```

A short program imports the list and reads the first question.

```python
# file: examples/ex01_data.py
from quiz_data import QUESTIONS

print(len(QUESTIONS), "questions")
first = QUESTIONS[0]
print(first["question"])
print(first["answer"])
```

<!-- output: examples/ex01_data.expected -->
```output
4 questions
Price of a tea?
3.50
```

`QUESTIONS` is in capital letters. Programmers use capitals for a value that the program reads but never changes.

**Step 2: Write the tests first.** Asha writes what each rule must do before any rule exists. Each test is one fact from the acceptance criteria.

```python
# file: project/test_quiz_logic.py
"""Tests for the quiz rules, written first."""
from quiz_logic import check_answer, percentage, grade, result_line


def test_exact_answer():
    assert check_answer("carrot", "carrot")


def test_capitals_and_spaces():
    assert check_answer("  Carrot ", "carrot")


def test_wrong_answer():
    assert not check_answer("lemon", "carrot")


def test_blank_answer():
    assert not check_answer("", "carrot")


def test_three_of_four():
    assert percentage(3, 4) == 75


def test_percentage_rounds():
    assert percentage(2, 3) == 67


def test_grade_boundaries():
    assert grade(75) == "Ready"
    assert grade(74) == "Almost"
    assert grade(50) == "Almost"
    assert grade(49) == "Practise again"


def test_result_line():
    assert result_line(3, 4) == "Score: 3/4 (75%) Ready"
```

`assert not` checks that something is false, so lines 15 and 19 say that a wrong answer and a blank answer must not count. Lines 31 to 34 test the edges of each grade: 75 and 74, then 50 and 49.

To run the tests, the rules need names. Asha writes each function with only its docstring. A function whose body is only a docstring returns `None`.

```python
# file: examples/testfirst/quiz_logic.py
"""Quiz rules: names only, no code yet."""


def check_answer(given, correct):
    """Compare, ignoring spaces and capitals."""


def percentage(points, total):
    """Return the score as a whole percentage."""


def grade(percent):
    """Return a word for the score."""


def result_line(points, total):
    """Return the last line of the quiz."""
```

She runs `pytest -q --tb=no -rf`. The option `--tb=no` hides the details, and `-rf` lists each failed test on one line.

<!-- output: examples/testfirst/test_quiz_logic.expected -->
```output
FF..FFFF                                         [100%]
=============== short test summary info ================
FAILED test_quiz_logic.py::test_exact_answer - Assert...
FAILED test_quiz_logic.py::test_capitals_and_spaces
FAILED test_quiz_logic.py::test_three_of_four - asser...
FAILED test_quiz_logic.py::test_percentage_rounds - a...
FAILED test_quiz_logic.py::test_grade_boundaries - As...
FAILED test_quiz_logic.py::test_result_line - Asserti...
6 failed, 2 passed in 0.01s
```

Six tests fail, as expected: there is no code yet. Two tests pass. `not None` is True, so the wrong-answer and blank-answer tests pass before any rule exists. A test that says "this must be false" is weak on its own. The exact-answer test on line 7 is its partner, and it fails until the rule works.

**Step 3: Make the first rule pass.** Asha writes `check_answer()` herself.

```python
# file: examples/step3/quiz_logic.py
"""Quiz rules: check_answer() is done."""


def check_answer(given, correct):
    """Compare, ignoring spaces and capitals."""
    return given.strip().lower() == correct.lower()


def percentage(points, total):
    """Return the score as a whole percentage."""


def grade(percent):
    """Return a word for the score."""


def result_line(points, total):
    """Return the last line of the quiz."""
```

`strip()` removes the spaces around the answer, and `lower()` removes the capitals. The correct answer gets `lower()` too, so the data may use capitals.

<!-- output: examples/step3/test_quiz_logic.expected -->
```output
....FFFF                                         [100%]
=============== short test summary info ================
FAILED test_quiz_logic.py::test_three_of_four - asser...
FAILED test_quiz_logic.py::test_percentage_rounds - a...
FAILED test_quiz_logic.py::test_grade_boundaries - As...
FAILED test_quiz_logic.py::test_result_line - Asserti...
4 failed, 4 passed in 0.01s
```

The four answer tests now pass: the dots are the first four characters. The four rules without code still fail.

Asha also asked an AI assistant for its own version of `check_answer()`, without showing hers, and compared the two on her four answers.

```python
# file: examples/ai/write_compare.py
def mine(given, correct):
    return given.strip().lower() == correct.lower()


def ai_version(given, correct):
    return given.lower().strip() == correct.lower()


for answer in ["carrot", "  Carrot ", "lemon", ""]:
    print(f"{answer!r:12}", mine(answer, "carrot"), ai_version(answer, "carrot"))
```

<!-- output: examples/ai/write_compare.expected -->
```output
'carrot'     True True
'  Carrot '  True True
'lemon'      False False
''           False False
```

The AI calls `lower()` before `strip()`. The order is different, but every result is the same. `!r` in line 11 prints the answer with its quotation marks, so you can see the spaces and the empty answer.

**Step 4: Let AI write the rest, and let the tests judge.** Asha pasted her test file into the chat and asked for the three other functions. The AI wrote them and said, "This passes all eight of your tests." The full exchange is in [Test it](#test-it), with the fix.

**Step 5: Put the app together.** The app does the talking: it asks, prints and counts. The rules do the deciding.

```python
# file: project/quiz_app.py
"""The Corner Cafe staff quiz."""
from quiz_data import QUESTIONS
from quiz_logic import check_answer, result_line

points = 0
for item in QUESTIONS:
    given = input(item["question"] + " ")
    if check_answer(given, item["answer"]):
        print("Correct!")
        points += 1
    else:
        print("The answer is", item["answer"])
print(result_line(points, len(QUESTIONS)))
```

Line 3 imports the data, and line 4 imports two rules. The loop on lines 7 to 13 asks each question. The `+ " "` on line 8 puts a space after the question mark. Line 14 hands the count to `result_line()` and prints what it returns.

## Test it

**AI pair moment.** In Step 4, the AI wrote this module and said that it passes all eight tests. Asha did not argue. She ran the tests.

```python
# file: examples/ai/flawed/quiz_logic.py
"""Rules for the staff quiz."""


def check_answer(given, correct):
    """Compare, ignoring spaces and capitals."""
    return given.strip().lower() == correct.lower()


def percentage(points, total):
    """Return the score as a whole percentage."""
    return points // total * 100


def grade(percent):
    """Return a word for the score."""
    if percent >= 75:
        return "Ready"
    elif percent >= 50:
        return "Almost"
    else:
        return "Practise again"


def result_line(points, total):
    """Return the last line of the quiz."""
    percent = percentage(points, total)
    return f"Score: {points}/{total} ({percent}%) {grade(percent)}"
```

<!-- output: examples/ai/flawed/test_quiz_logic.expected -->
```output
....FF.F                                         [100%]
=============== short test summary info ================
FAILED test_quiz_logic.py::test_three_of_four - asser...
FAILED test_quiz_logic.py::test_percentage_rounds - a...
FAILED test_quiz_logic.py::test_result_line - Asserti...
3 failed, 5 passed in 0.01s
```

Three tests fail, and all three need `percentage()`. Asha pasted the code and the failure report for one test into the chat and asked for the cause before the fix.

```python
# file: examples/ai/debug/test_percentage.py
from quiz_logic import percentage


def test_three_of_four():
    assert percentage(3, 4) == 75
```

<!-- output: examples/ai/debug/test_percentage.expected -->
```output
F                                                [100%]
======================= FAILURES =======================
__________________ test_three_of_four __________________
test_percentage.py:6: in test_three_of_four
    assert percentage(3, 4) == 75
E   assert 0 == 75
E    +  where 0 = percentage(3, 4)
=============== short test summary info ================
FAILED test_percentage.py::test_three_of_four - asser...
1 failed in 0.01s
```

The report says `percentage(3, 4)` gave 0. The AI explained the cause. `//` is floor division from Chapter 2: `3 // 4` is 0, and `0 * 100` is still 0. The smallest fix divides with `/` first and rounds at the end: `round(points / total * 100)`. Asha made that one change and ran all eight tests again.

<!-- output: project/test_quiz_logic.expected -->
```output
........                                         [100%]
8 passed in 0.01s
```

All eight pass. The AI sounded sure the first time. The tests were the only thing that knew.

Then Asha tested the whole app with typed answers. Each run is a copy of `quiz_app.py` with its own answers.

| Test | Answers typed | Expected last line | Result |
|---|---|---|---|
| Full marks | 3.50, carrot, yes, 2.75 | `Score: 4/4 (100%) Ready` | Pass |
| Zero | 3, lemon, no, 3.00 | `Score: 0/4 (0%) Practise again` | Pass |
| Spaces and capitals | " 3.50", "  CARROT ", "Yes", "2.75 " | `Score: 4/4 (100%) Ready` | Pass |
| Blank answers | four empty answers | `Score: 0/4 (0%) Practise again` | Pass |

Here are two of the runs.

<!-- output: examples/apptest/mixed_case.expected -->
```output
Price of a tea?  3.50
Correct!
Which cake has nuts?   CARROT
Correct!
Is the soup vegan? Yes
Correct!
Price of a scone? 2.75
Correct!
Score: 4/4 (100%) Ready
```

<!-- output: examples/apptest/blank.expected -->
```output
Price of a tea?
The answer is 3.50
Which cake has nuts?
The answer is carrot
Is the soup vegan?
The answer is yes
Price of a scone?
The answer is 2.75
Score: 0/4 (0%) Practise again
```

In the zero test, `3` for the tea is close to `3.50`, but it is not the same text, so it counts as wrong. The quiz compares text, not numbers. Practice Task 2 compares prices as numbers.

## Improve it with AI

With every test passing, Asha asked an AI assistant: "Make `grade()` shorter. Do not change what it returns." The AI suggested dropping `elif` and `else`, because `return` already stops the function. That idea is correct. Its new version also changed one sign, and Asha's tests caught it.

```python
# file: examples/ai/improve/quiz_logic.py
"""Rules for the staff quiz."""


def check_answer(given, correct):
    """Compare, ignoring spaces and capitals."""
    return given.strip().lower() == correct.lower()


def percentage(points, total):
    """Return the score as a whole percentage."""
    return round(points / total * 100)


def grade(percent):
    """Return a word for the score."""
    if percent > 75:
        return "Ready"
    if percent >= 50:
        return "Almost"
    return "Practise again"


def result_line(points, total):
    """Return the last line of the quiz."""
    percent = percentage(points, total)
    return f"Score: {points}/{total} ({percent}%) {grade(percent)}"
```

<!-- output: examples/ai/improve/test_quiz_logic.expected -->
```output
......FF                                         [100%]
=============== short test summary info ================
FAILED test_quiz_logic.py::test_grade_boundaries - As...
FAILED test_quiz_logic.py::test_result_line - Asserti...
2 failed, 6 passed in 0.01s
```

Line 17 says `> 75` instead of `>= 75`. A score of exactly 75 now gets Almost. The boundary test from Step 2 found it in less than a second. Asha kept her own `grade()`.

These are the six ways AI helped with this project. The full prompts are in [ai-prompts.md](ai-prompts.md).

| Stage | How AI helped |
|---|---|
| Plan | Suggested three files and four functions. Asha replaced `ask_and_check()`, which did two jobs, with a pure `check_answer()`. |
| Write | Wrote its own `check_answer()` to compare with Asha's. Both gave the same results for her four answers. |
| Generate | Wrote `percentage()`, `grade()` and `result_line()`, and said they pass all eight tests. |
| Test | Asha's tests ran the AI's module: three failed, all through `percentage()`. |
| Debug | Explained the failure report: `//` gives 0 for 3 out of 4. One change fixed it, and all eight tests passed. |
| Improve | Made `grade()` shorter, but changed `>=` to `>`. The boundary test failed, so Asha kept her version. |

## Recap

- Split a program by job: data in one module, rules in another, and the talking in the app.
- Keep rules pure, with no `input()` and no `print()`, so a test can check them.
- Write the tests first. They fail at the start, and a test that passes with no code checks very little.
- Give an AI your tests with your request. Then run them yourself: the report, not the AI, decides.
- Test the edges, such as exactly 75, because small mistakes such as `>` instead of `>=` live there.

You earned **300 XP** and the **Software Builder** badge. Module 4 is complete.

The practice tasks for this chapter are in [practice/practice.md](practice/practice.md).

## What's next

When the quiz closes, every score disappears. In Chapter 21, you will save data to a file and load it again, so the cafe can keep every score.
