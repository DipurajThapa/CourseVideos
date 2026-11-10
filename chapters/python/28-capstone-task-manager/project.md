# Chapter 28: Final Boss: The Personal Task Manager

> Quest: build a complete, tested program with an AI assistant at every stage, and let your tests decide every time. Reward: 300 XP and the **Python Builder** badge.

## The mission

Every morning at the Corner Cafe, Asha writes a list on a scrap of paper: open the cafe, restock milk, call the supplier. By lunch, the paper is lost, and nobody knows what is done.

Asha wants a task manager she can run in a terminal. She types `add`, `done` or `list`, and the program keeps her tasks in a file, so they are still there the next morning. A broken file must give a clear message, not a crash. And this time, the tests come first.

This is the final boss. It uses the whole course.

| Chapters | What you use from them |
|---|---|
| 1 to 4 | `print()`, f-strings, `input()` and `int()` |
| 6 to 8 | `if`, `elif` and `else`, a `while True` loop and `for` loops |
| 11 to 14 | Lists, dictionaries, tuples and comprehensions |
| 16 to 20 | Functions, modules, and tests written first with `pytest` |
| 21 to 23 | Files with `pathlib`, `try` and `except`, and JSON |
| 26 and 27 | A data class, a class with methods, and changing code safely with tests |

## What you will build

Three code files and one data file work together.

| File | Its job |
|---|---|
| `tasks_core.py` | The rules: the `Task` data class, the `TaskList` class, and `save_tasks()` and `load_tasks()` |
| `test_tasks_core.py` | Ten tests for the rules, written before the rules |
| `task_app.py` | The command loop: it reads commands with `input()` and calls the rules |
| `tasks.json` | The saved tasks |

Here is a real session. Asha lists her tasks, marks task 2 as done, adds a new task and lists them again.

<!-- output: project/task_app.expected -->
```output
2 open tasks
Command: list
1. [x] Open the cafe (P1)
2. [ ] Restock milk (P2)
3. [ ] Call the supplier (P3)
Command: done
Number: 2
Command: add
Title: Order paper cups
Priority 1-3: 2
Command: list
1. [x] Open the cafe (P1)
2. [x] Restock milk (P2)
3. [ ] Call the supplier (P3)
4. [ ] Order paper cups (P2)
Command: quit
Saved tasks.json
```

Each line shows the task number, `[x]` for a done task, the title and the priority, from `P1` (most important) to `P3`.

## Acceptance criteria

Your task manager is finished when all of these are true.

1. `add` asks for a title and a priority. An empty title, or a priority other than 1, 2 or 3, is refused with a clear line.
2. `done` asks for a task number, counting from 1. A number with no task is refused.
3. `list` shows every task with its number, its mark and its priority.
4. `quit` saves every task to `tasks.json`.
5. A missing or empty `tasks.json` means no tasks yet. A broken one gives one line that starts with `Tasks not loaded:`.
6. The rules contain no `input()` and no `print()`, so tests can check them.
7. All ten tests pass.

## Plan it with AI

Before any code, Asha asked an AI assistant for a plan. This chapter's AI skill is the whole workflow: plan, build, test, review and improve, with your tests as the judge.

> "I am a beginner. I know classes, data classes, files, JSON, try and except, functions and pytest. I want a command-line task manager with add, done, list and quit, saved in a JSON file. Do not write code. Plan the classes and functions."

An example answer looked like this:

> Make one class, `TaskManager`. Its `run()` method asks for commands with `input()`, prints the tasks, and saves the file after each command.

The plan would work, but nothing in it could be tested. Asha checked it against Chapter 20: a rule that calls `input()` waits for a person, so a test cannot run it. She asked for the rules in one module, with no `input()` and no `print()`, and the conversation in a separate file.

## Build it step by step

**Step 1: Write the tests first.** Asha wrote ten tests before any rule existed, as in Chapter 20. Here are the first three:

```python
# illustrative: lines 7 to 21 of project/test_tasks_core.py
def sample():
    tasks = TaskList()
    tasks.add("Open the cafe", 1)
    tasks.add("Restock milk")
    tasks.add("Call the supplier", 3)
    return tasks


def test_add_keeps_order():
    assert sample().tasks[0].title == "Open the cafe"


def test_add_refuses_empty_title():
    with pytest.raises(ValueError):
        TaskList().add("   ")
```

Then she ran them against empty rules: classes and functions that exist but do nothing.

<!-- output: examples/step1/test_tasks_core.expected -->
```output
FFFFFF...F                                       [100%]
7 failed, 3 passed in 0.01s
```

Seven tests fail, as they should. Three pass already, because empty rules return an empty list, and an empty list looks like "no tasks". A passing test proves something only when it can fail.

**Step 2: Tasks and a task list.** A `Task` is a data class, as in Chapter 26. `TaskList` keeps the tasks in a list and checks every new task.

```python
# illustrative: lines 7 to 11 and 20 to 32 of project/tasks_core.py
@dataclass
class Task:
    title: str
    priority: int = 2
    done: bool = False


class TaskList:
    """Tasks in the order added, numbered from 1."""

    def __init__(self, tasks=None):
        self.tasks = list(tasks or [])

    def add(self, title, priority=2):
        title = title.strip()
        if not title:
            raise ValueError("a task needs a title")
        if priority not in (1, 2, 3):
            raise ValueError("priority must be 1, 2 or 3")
        self.tasks.append(Task(title, priority))
```

A data class writes `__init__` for you, so `Task` needs only its fields. `tasks or []` gives the list that was passed in, or a new empty list when there is none. `list()` makes a copy, so the task list never shares a list with the caller. `add()` removes the spaces around the title first.

```python
# file: examples/step2/list_check.py
from tasks_core import TaskList

tasks = TaskList()
tasks.add("Open the cafe", 1)
tasks.add("  Restock milk  ")
tasks.add("Call the supplier", 3)
for line in tasks.lines():
    print(line)
try:
    tasks.add("   ")
except ValueError as error:
    print("Refused:", error)
```

<!-- output: examples/step2/list_check.expected -->
```output
1. [ ] Open the cafe (P1)
2. [ ] Restock milk (P2)
3. [ ] Call the supplier (P3)
Refused: a task needs a title
```

**Step 3: Numbers that start at 1.** People count tasks from 1, but a list counts from 0. `complete()` checks the number, then marks the task at position `number - 1`.

```python
# illustrative: lines 34 to 49 of project/tasks_core.py
    def complete(self, number):
        if number < 1 or number > len(self.tasks):
            raise ValueError(f"there is no task {number}")
        self.tasks[number - 1].done = True

    def open_tasks(self):
        return [t for t in self.tasks if not t.done]

    def lines(self):
        result = []
        for number in range(1, len(self.tasks) + 1):
            task = self.tasks[number - 1]
            mark = "x" if task.done else " "
            line = f"{number}. [{mark}] {task.title}"
            result.append(f"{line} (P{task.priority})")
        return result
```

```python
# file: examples/step3/done_check.py
from tasks_core import TaskList

tasks = TaskList()
tasks.add("Open the cafe", 1)
tasks.add("Restock milk")
tasks.add("Call the supplier", 3)
tasks.complete(1)
for line in tasks.lines():
    print(line)
print(len(tasks.open_tasks()), "open tasks")
try:
    tasks.complete(4)
except ValueError as error:
    print("Refused:", error)
```

<!-- output: examples/step3/done_check.expected -->
```output
1. [x] Open the cafe (P1)
2. [ ] Restock milk (P2)
3. [ ] Call the supplier (P3)
2 open tasks
Refused: there is no task 4
```

**Step 4: Save and load.** Asha asked the AI to write `save_tasks()` and `load_tasks()` against her tests. The full exchange is in [Test it](#test-it). Here is the finished pair. It saves a list of two tasks and loads it again.

```python
# file: examples/step4/save_check.py
from pathlib import Path
from tasks_core import TaskList, load_tasks, save_tasks

tasks = TaskList()
tasks.add("Open the cafe", 1)
tasks.add("Restock milk")
tasks.complete(1)
save_tasks(Path("tasks.json"), tasks)
print(Path("tasks.json").read_text(encoding="utf-8"))
again = load_tasks(Path("tasks.json"))
print(again.lines())
```

<!-- output: examples/step4/save_check.expected -->
```output
[
  {
    "title": "Open the cafe",
    "priority": 1,
    "done": true
  },
  {
    "title": "Restock milk",
    "priority": 2,
    "done": false
  }
]
['1. [x] Open the cafe (P1)', '2. [ ] Restock milk (P2)']
```

Each task is saved as a dictionary, with the `to_dict()` method that you will meet in [Test it](#test-it). `true` and `false` are how JSON writes `True` and `False`.

**Step 5: The command loop.** `task_app.py` holds the conversation. It loads the tasks, asks for commands until `quit`, then saves.

```python
# file: project/task_app.py
"""Corner Cafe tasks: add, done, list or quit."""
from pathlib import Path
from tasks_core import load_tasks, save_tasks

PATH = Path("tasks.json")


def run(tasks):
    """Ask for commands until the user types quit."""
    while True:
        command = input("Command: ").strip().lower()
        if command == "quit":
            return
        try:
            if command == "add":
                title = input("Title: ")
                priority = int(input("Priority 1-3: "))
                tasks.add(title, priority)
            elif command == "done":
                tasks.complete(int(input("Number: ")))
            elif command == "list":
                for line in tasks.lines():
                    print(line)
            else:
                print("Commands: add, done, list, quit")
        except ValueError as error:
            print("Not done:", error)


try:
    tasks = load_tasks(PATH)
except ValueError as error:
    print("Tasks not loaded:", error)
else:
    print(len(tasks.open_tasks()), "open tasks")
    run(tasks)
    save_tasks(PATH, tasks)
    print("Saved", PATH.name)
```

`run()` returns when the user types `quit`, which ends the loop. Every rule raises only `ValueError`, with a clear message, so one `except` in the loop catches a bad title, a bad priority and a bad number. The `else` block runs only when the tasks loaded.

## Test it

**AI pair moment.** In Step 4, the AI wrote `save_tasks()` and `load_tasks()` and said, "These pass all ten of your tests." Asha did not argue. She ran them.

```python
# illustrative: lines 46 to 61 of examples/ai/flawed/tasks_core.py
def save_tasks(path, task_list):
    text = json.dumps(task_list.tasks, indent=2)
    path.write_text(text, encoding="utf-8")


def load_tasks(path):
    """Return the saved TaskList, or raise ValueError."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return TaskList()
    try:
        rows = json.loads(text)
    except json.JSONDecodeError as error:
        name = path.name
        raise ValueError(f"{name} is not valid JSON: {error.msg}")
```

<!-- output: examples/ai/flawed/test_tasks_core.expected -->
```output
......F.F.                                       [100%]
=============== short test summary info ================
FAILED test_tasks_core.py::test_save_then_load_gives_same_lines
FAILED test_tasks_core.py::test_empty_file_means_no_tasks
2 failed, 8 passed in 0.01s
```

Two tests fail. Asha asked the AI for test cases for loading. It listed a normal file, a missing file and a broken file, and said that an empty file "is broken JSON, so it should raise an error". Her criterion 5 says an empty file means no tasks yet, and her test already checks it. The AI's list had missed the case, and her test caught it.

For the first failure, she saved one task with the AI's code. She read the last line of the error first, as she learned in Chapter 1. Here it is.

<!-- error: examples/ai/debug/save_crash.expected_error -->
```output
TypeError: Object of type Task is not JSON serializable
```

On your computer, the `File` lines show full paths, and Python 3.14 and newer add a short note under the error line: `when serializing list item 0`. Asha pasted the code and the error and asked for the cause first. The AI explained that `json.dumps()` can save numbers, text, `True`, `False`, `None`, lists and dictionaries, but not a `Task` object. The fix is a new method, `to_dict()`, which turns each task into a dictionary, and one changed line in `save_tasks()`. Here they are.

```python
# illustrative: lines 13 to 17 of project/tasks_core.py
    def to_dict(self):
        """Return the task as a dict that JSON can save."""
        return {"title": self.title,
                "priority": self.priority,
                "done": self.done}
```

```python
# illustrative: lines 52 to 55 of project/tasks_core.py
def save_tasks(path, task_list):
    rows = [task.to_dict() for task in task_list.tasks]
    text = json.dumps(rows, indent=2)
    path.write_text(text, encoding="utf-8")
```

For the empty file, `json.loads("")` raises a `JSONDecodeError`, so the AI's code turned an empty file into an error. Two lines fix it, before `json.loads()`:

```python
# illustrative: lines 64 to 65 of project/tasks_core.py
    if not text.strip():
        return TaskList()
```

Then she ran every test again:

<!-- output: examples/ai/fixed/test_tasks_core.expected -->
```output
..........                                       [100%]
10 passed in 0.01s
```

She also ran the whole program on three cases whose results she knew in advance.

| Case | Folder | Expected |
|---|---|---|
| First run | `cases/first_run` | `0 open tasks`, then a new task is added and saved |
| Bad answers | `cases/bad_input` | Each bad answer gives a line that starts with `Not done:` |
| Broken file | `cases/bad_json` | `Tasks not loaded: tasks.json is not valid JSON: ...` |

<!-- output: examples/cases/first_run/task_app.expected -->
```output
0 open tasks
Command: add
Title: Bake scones
Priority 1-3: 1
Command: list
1. [ ] Bake scones (P1)
Command: quit
Saved tasks.json
```

<!-- output: examples/cases/bad_input/task_app.expected -->
```output
2 open tasks
Command: add
Title: Sweep the floor
Priority 1-3: high
Not done: invalid literal for int() with base 10: 'high'
Command: add
Title:
Priority 1-3: 2
Not done: a task needs a title
Command: done
Number: 9
Not done: there is no task 9
Command: dance
Commands: add, done, list, quit
Command: quit
Saved tasks.json
```

The message for `high` comes from `int()` itself. It is still clear enough: `high` is not a whole number.

<!-- output: examples/cases/bad_json/task_app.expected -->
```output
Tasks not loaded: tasks.json is not valid JSON: Expecting ',' delimiter
```

The broken file is missing a comma between its two tasks. All three results matched.

## Improve it with AI

Asha asked the AI to review her finished module: "Suggest one change that makes the code shorter. Do not change what it does." The AI answered:

> Remove the priority check from `add()`. The app already asks for a priority from 1 to 3, so the check is never needed.

Asha ran her tests on the AI's version:

<!-- output: examples/ai/improve/test_tasks_core.expected -->
```output
..F.......                                       [100%]
=============== short test summary info ================
FAILED test_tasks_core.py::test_add_refuses_bad_priority
1 failed, 9 passed in 0.01s
```

The test for a bad priority failed. The prompt in the app only asks for 1 to 3. It does not stop a person who types 5, and it does not protect any other program that uses `TaskList`. The suggestion removed a check that her tests and criterion 1 need. Asha kept her version.

Before she pasted any code into the chat, she checked it for private data. The tasks hold only cafe jobs, with no names, phone numbers or passwords.

These are the six ways AI helped with this project. The full prompts are in [ai-prompts.md](ai-prompts.md).

| Stage | How AI helped |
|---|---|
| Plan | Suggested one class that asks, prints and saves. Asha asked for testable rules and a separate command loop. |
| Write | Wrote its own `complete()` to compare with Asha's. It marked the wrong task. |
| Generate | Wrote `save_tasks()` and `load_tasks()`. Two of Asha's tests failed. |
| Test | Listed test cases for loading, but missed the empty file that her test checks. |
| Debug | Explained the cause first: JSON cannot save a `Task`. `to_dict()` fixed it, and all ten tests passed. |
| Improve | Suggested removing the priority check. One test failed, so Asha kept her version. |

In the Write stage, Asha asked for the same rule as a small function, and named it `ai_complete()`, so both versions fit in one file. Both were asked to complete task 1 on a list of two tasks.

```python
# file: examples/ai/write/write_compare.py
from tasks_core import Task


def asha_complete(tasks, number):
    if number < 1 or number > len(tasks):
        raise ValueError(f"there is no task {number}")
    tasks[number - 1].done = True


def ai_complete(tasks, number):
    tasks[number].done = True


pairs = [("Asha", asha_complete), ("AI", ai_complete)]
for who, complete in pairs:
    tasks = [Task("Open the cafe"), Task("Restock milk")]
    complete(tasks, 1)
    done = [task.title for task in tasks if task.done]
    print(who, "marked", done)
```

<!-- output: examples/ai/write/write_compare.expected -->
```output
Asha marked ['Open the cafe']
AI marked ['Restock milk']
```

The AI's version uses the number as a list position, so task 1 marks the second task. Asha's version subtracts 1.

## Recap

- Plan with AI, but keep the rules free of `input()` and `print()`, so tests can check them.
- Write the tests first. A test that passes on empty rules proves nothing.
- Give every task a number from 1 for people, and subtract 1 for the list.
- JSON saves dictionaries, not objects. A `to_dict()` method turns an object into data.
- A missing or empty file can mean "nothing yet". A broken file gets one clear message.
- Every AI suggestion was judged by your criteria, a run, or your tests.

You earned **300 XP** and the **Python Builder** badge. Module 6 is complete, and so is the course.

The practice tasks for this chapter are in [practice/practice.md](practice/practice.md).

## What's next

You finished all 28 chapters. Keep building small tools for your own life, one test at a time, with an AI assistant at your side. Review any chapter whenever a topic feels unclear, and try the practice tasks you skipped.
