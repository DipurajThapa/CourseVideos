# Video Script: Chapter 28: Final Boss: The Personal Task Manager

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:24 (estimate, not rendered yet).

## Scene 1: Introduction

**Section:** Introduction

**Direction:** Open on the lost paper list. Then the final boss title and the stake.

- **Narration:** Every morning at the Corner Cafe, Asha writes her jobs on a scrap of paper. Open the cafe. Restock milk. Call the supplier.
  **On screen:** The list on the paper
- **Narration:** By lunch, the paper is lost, and nobody knows what is done.
  **On screen:** The list on the paper
- **Narration:** Welcome to Chapter 28. The final boss! In Chapter 1, Asha printed one receipt. Today she builds real software.
  **On screen:** The Personal Task Manager
- **Narration:** Asha will build a task manager that keeps her jobs in a file, with tests written first, and an AI assistant at every stage.
  **On screen:** The Personal Task Manager Plan it. Test it. Build it. Judge every answer.
- **Narration:** The AI will promise that its code passes all of her tests. Her tests will decide.
  **On screen:** The Personal Task Manager Plan it. Test it. Build it. Judge every answer.

## Scene 2: The mission

**Section:** The mission

**Direction:** The four commands and the file, then the whole course in one table.

- **Narration:** Here is the mission. Add a task, with a title and a priority.
  **On screen:** Four commands, one file
    - `add` a task, with a title and a priority.
- **Narration:** Done marks a task as finished.
  **On screen:** Four commands, one file
    - `add` a task, with a title and a priority.
    - `done` marks a task as finished.
- **Narration:** List shows every task, and quit saves them in a file, so they are still there tomorrow.
  **On screen:** Four commands, one file
    - `add` a task, with a title and a priority.
    - `done` marks a task as finished.
    - `list` shows every task. `quit` saves them.
- **Narration:** And a broken file gives a clear message, never a crash.
  **On screen:** Four commands, one file
    - `add` a task, with a title and a priority.
    - `done` marks a task as finished.
    - `list` shows every task. `quit` saves them.
    - A broken file gives a clear message, never a crash.
- **Narration:** This is the final boss, so it uses the whole course. Printing, text and input, from the first chapters.
  **On screen:** Table: This boss uses the whole course (row 1 in focus)
- **Narration:** Decisions and loops.
  **On screen:** Table: This boss uses the whole course (row 2 in focus)
- **Narration:** Lists, dictionaries and comprehensions.
  **On screen:** Table: This boss uses the whole course (row 3 in focus)
- **Narration:** Functions, modules, and tests written first.
  **On screen:** Table: This boss uses the whole course (row 4 in focus)
- **Narration:** Files, error handling and JSON.
  **On screen:** Table: This boss uses the whole course (row 5 in focus)
- **Narration:** And classes, from Chapter 26, with the safe changes from Chapter 27.
  **On screen:** Table: This boss uses the whole course (row 6 in focus)

## Scene 3: What you will build

**Section:** What you will build

**Direction:** The files and their jobs, then a real session as the destination.

- **Narration:** Tasks core holds the rules: a task, a task list, and saving and loading.
  **On screen:** Table: Three code files, one job each (row 1 in focus)
- **Narration:** The test file checks the rules. It comes first.
  **On screen:** Table: Three code files, one job each (row 2 in focus)
- **Narration:** Task app holds the conversation with the user.
  **On screen:** Table: Three code files, one job each (row 3 in focus)
- **Narration:** And tasks dot JSON keeps the tasks between runs.
  **On screen:** Table: Three code files, one job each (row 4 in focus)
- **Narration:** Here is a real session. Asha lists her tasks. Each line shows a number, an x for a done task, the title and the priority.
  **On screen:** Code `project/task_app.py`, output `project/task_app.expected`
- **Narration:** She marks task 2 as done, and adds a new task.
  **On screen:** Code `project/task_app.py`, output `project/task_app.expected`
- **Narration:** The second list shows both changes. Quit saves them in the file.
  **On screen:** Code `project/task_app.py`, output `project/task_app.expected`

## Scene 4: Acceptance criteria

**Section:** Acceptance criteria

**Direction:** Seven criteria in groups, a quiz on why the rules have no input(), then a breather.

- **Narration:** Asha writes down what done means.
  **On screen:** Done means all seven are true
- **Narration:** One. Add refuses an empty title, or a priority that is not 1, 2 or 3.
  **On screen:** Done means all seven are true
    - `add` refuses an empty title, or a priority other than 1, 2 or 3.
- **Narration:** Two and three. Done takes a number, counting from 1. List shows every task.
  **On screen:** Done means all seven are true
    - `add` refuses an empty title, or a priority other than 1, 2 or 3.
    - `done` takes a task number, counting from 1.
    - `list` shows each task's number, mark and priority.
- **Narration:** Four and five. Quit saves every task. A missing or empty file means no tasks yet. A broken file gives one clear line.
  **On screen:** Done means all seven are true
    - `add` refuses an empty title, or a priority other than 1, 2 or 3.
    - `done` takes a task number, counting from 1.
    - `list` shows each task's number, mark and priority.
    - `quit` saves every task to `tasks.json`.
    - A missing or empty file means no tasks yet. A broken one gives one clear line.
- **Narration:** Six. The rules contain no input and no print.
  **On screen:** Done means all seven are true
    - `add` refuses an empty title, or a priority other than 1, 2 or 3.
    - `done` takes a task number, counting from 1.
    - `list` shows each task's number, mark and priority.
    - `quit` saves every task to `tasks.json`.
    - A missing or empty file means no tasks yet. A broken one gives one clear line.
    - The rules contain no `input()` and no `print()`.
- **Narration:** And seven. All ten tests pass.
  **On screen:** Done means all seven are true
    - `add` refuses an empty title, or a priority other than 1, 2 or 3.
    - `done` takes a task number, counting from 1.
    - `list` shows each task's number, mark and priority.
    - `quit` saves every task to `tasks.json`.
    - A missing or empty file means no tasks yet. A broken one gives one clear line.
    - The rules contain no `input()` and no `print()`.
    - All ten tests pass.
- **Narration:** Quick check, from Chapter 20. Why must the rules contain no input?
  **On screen:** Quick check: "Why must the rules contain no `input()`?" (options shown)
- **Interaction:** "Why must the rules contain no `input()`?" stays on screen with a 10-second timer.
- **Narration:** B. A test cannot type. A rule that waits for a person would stop the test. So the conversation lives in its own file.
  **On screen:** Quick check: "Why must the rules contain no `input()`?" (answer revealed: A test cannot type, so it could not run them)
- **Narration:** Take a breather. You know the files, and what done means.
  **On screen:** Breather card
    - Rules in one file, the conversation in another.
    - Tasks count from 1 for people.
    - Done means seven checks.
- **Narration:** Next, Asha plans with an AI assistant.
  **On screen:** Breather card
    - Rules in one file, the conversation in another.
    - Tasks count from 1 for people.
    - Done means seven checks.
- **Breather:** 4 quiet seconds.

## Scene 5: Plan it with AI

**Section:** Plan it with AI

**Direction:** Stage 1: the AI's plan, one class that asks, prints and saves. Asha checks it against Chapter 20.

- **Narration:** In this project, the six AI stages help build one module: the rules. Stage 1: plan. Asha says what she wants, and says: no code yet.
  **On screen:** AI chat, stage 1: Plan: classes and functions
    - You: I am a beginner. I know classes, data classes, files, JSON, try and except, and pytest. I want a command-line task manager with add, done, list and quit, saved as JSON. Do not write code. Plan the classes and functions.
- **Narration:** The AI suggests one class whose run method asks with input, prints the tasks, and saves the file.
  **On screen:** AI chat, stage 1: Plan: classes and functions
    - You: I am a beginner. I know classes, data classes, files, JSON, try and except, and pytest. I want a command-line task manager with add, done, list and quit, saved as JSON. Do not write code. Plan the classes and functions.
    - AI (example answer): Make one class, `TaskManager`. Its `run()` method asks for commands with `input()`, prints the tasks, and saves the file after each command.
- **Narration:** It would work. But nothing in it could be tested, because every method waits for a person. Asha remembers her criterion six.
  **On screen:** AI chat, stage 1: Plan: classes and functions
    - You: I am a beginner. I know classes, data classes, files, JSON, try and except, and pytest. I want a command-line task manager with add, done, list and quit, saved as JSON. Do not write code. Plan the classes and functions.
    - AI (example answer): Make one class, `TaskManager`. Its `run()` method asks for commands with `input()`, prints the tasks, and saves the file after each command.
- **Narration:** So she asks for the rules in one module, with no input and no print, and the conversation in a separate file.
  **On screen:** AI chat, stage 1: Plan: classes and functions
    - You: I am a beginner. I know classes, data classes, files, JSON, try and except, and pytest. I want a command-line task manager with add, done, list and quit, saved as JSON. Do not write code. Plan the classes and functions.
    - AI (example answer): Make one class, `TaskManager`. Its `run()` method asks for commands with `input()`, prints the tasks, and saves the file after each command.

## Scene 6: Step 1: Tests first

**Section:** Build it step by step

**Direction:** Three of the ten tests, then a run against empty rules. Ask whether all ten fail, then reveal 7 failed, 3 passed.

- **Narration:** Time to build. Step 1: as in Chapter 20, Asha writes ten tests before any rule exists. Sample makes a list of three tasks for the tests to use.
  **On screen:** Code `project/test_tasks_core.py`, line 7 highlighted, output hidden
- **Narration:** The first test checks that tasks keep their order.
  **On screen:** Code `project/test_tasks_core.py`, line 15, 16 highlighted, output hidden
- **Narration:** The second checks that an empty title is refused, with pytest raises, from Chapter 22.
  **On screen:** Code `project/test_tasks_core.py`, line 19, 20, 21 highlighted, output hidden
- **Narration:** Then she writes empty rules. The classes and functions exist, but they do nothing.
  **On screen:** Code `examples/step1/tasks_core.py`, line 23, 24 highlighted, output hidden
- **Narration:** Open tasks and lines give back an empty list, and load tasks gives back an empty task list.
  **On screen:** Code `examples/step1/tasks_core.py`, line 23, 24, 26, 27, 34, 35 highlighted, output hidden
- **Interaction:** "Empty rules do nothing. Will all ten tests fail?" stays on screen with a 10-second timer.
- **Narration:** No. Asha runs them to see.
  **On screen:** Code `examples/step1/tasks_core.py`, line 23, 24, 26, 27, 34, 35 highlighted, output hidden
- **Narration:** Seven fail, as they should. But three pass already.
  **On screen:** Code `examples/step1/test_tasks_core.py`, output `examples/step1/test_tasks_core.expected`
- **Narration:** An empty list looks like no tasks. So the tests for a missing file and an empty file pass on rules that do nothing. So does the save test.
  **On screen:** Code `examples/step1/test_tasks_core.py`, line 55, 60 highlighted, output `examples/step1/test_tasks_core.expected`
- **Narration:** A passing test proves something only when it can fail.
  **On screen:** Code `examples/step1/test_tasks_core.py`, output `examples/step1/test_tasks_core.expected`

## Scene 7: Step 2: Tasks and a task list

**Section:** Build it step by step

**Direction:** The Task data class and TaskList.add, then a check run with a predict question about the stripped title.

- **Narration:** Step 2. A task is a data class, as in Chapter 26: a title, a priority that starts at 2, and done, which starts as False.
  **On screen:** Code `project/tasks_core.py`, line 7, 8, 9, 10, 11 highlighted, output hidden
- **Narration:** The task list keeps the tasks in a list. Tasks or empty list gives the list that was passed in, or a new empty one. List makes a copy, so nothing is shared.
  **On screen:** Code `project/tasks_core.py`, line 23, 24 highlighted, output hidden
- **Narration:** Add strips the spaces around the title first.
  **On screen:** Code `project/tasks_core.py`, line 27 highlighted, output hidden
- **Narration:** Then it refuses an empty title, and a priority that is not 1, 2 or 3, each with its own value error.
  **On screen:** Code `project/tasks_core.py`, line 28, 29, 30, 31 highlighted, output hidden
- **Narration:** Asha adds three tasks. Line 6 adds Restock milk with spaces around it, and no priority.
  **On screen:** Code `examples/step2/list_check.py`, line 6 highlighted, output hidden
- **Narration:** Line 9 prints one line per task: its number, a box that is empty until the task is done, the title, and P with the priority.
  **On screen:** Code `examples/step2/list_check.py`, line 8, 9 highlighted, output hidden
- **Interaction:** "What does the second line of the output show for line 6's task?" stays on screen with a 10-second timer.
- **Narration:** 2, the title without spaces, and P2, the default priority.
  **On screen:** Code `examples/step2/list_check.py`, line 8, 9 highlighted, output `examples/step2/list_check.expected`
- **Narration:** And the empty title on line 11 is refused, with the message from add.
  **On screen:** Code `examples/step2/list_check.py`, line 11 highlighted, output `examples/step2/list_check.expected`

## Scene 8: Step 3: Numbers that start at 1

**Section:** Build it step by step

**Direction:** complete() and lines(), a check run, then stage 2: the AI's complete() and an ask, then the comparison run. Breather.

- **Narration:** Step 3. People count tasks from 1, but a list counts from 0, as in Chapter 11. Complete checks the number first, then marks the task at number minus 1.
  **On screen:** Code `project/tasks_core.py`, line 34, 35, 36, 37 highlighted, output hidden
- **Narration:** Open tasks keeps the tasks that are not done, with a comprehension.
  **On screen:** Code `project/tasks_core.py`, line 39, 40 highlighted, output hidden
- **Narration:** Lines makes one line per task: its number, an x when it is done, the title and the priority.
  **On screen:** Code `project/tasks_core.py`, line 42, 43, 44, 45, 46, 47, 48, 49 highlighted, output hidden
- **Narration:** Asha completes task 1. The first task gets its x.
  **On screen:** Code `examples/step3/done_check.py`, line 8 highlighted, output `examples/step3/done_check.expected`
- **Narration:** Two open tasks are left. And task 4 does not exist, so it is refused.
  **On screen:** Code `examples/step3/done_check.py`, line 11, 13 highlighted, output `examples/step3/done_check.expected`
- **Narration:** Stage 2: write. Asha wrote complete herself first. Now she asks the AI for the same rule, as a small function she can test alone, and says: people count from 1.
  **On screen:** AI chat, stage 2: Write it yourself, then compare
    - You: Write a function complete(tasks, number) that marks a task in a list as done. People count tasks from 1. Show only the function.
- **Narration:** The AI's version is one line, and it sounds sure. Asha names it ai complete, so both versions fit in one file.
  **On screen:** AI chat, stage 2: Write it yourself, then compare
    - You: Write a function complete(tasks, number) that marks a task in a list as done. People count tasks from 1. Show only the function.
    - AI (example answer): Here it is. It marks the task as done: [code `examples/ai/write/write_compare.py`]
- **Narration:** She puts both versions in one file. Each one completes task 1 on a list of two tasks.
  **On screen:** Code `examples/ai/write/write_compare.py`, line 17, 18 highlighted, output hidden
- **Narration:** Look at line 12 of the AI's version.
  **On screen:** Code `examples/ai/write/write_compare.py`, line 12 highlighted, output hidden
- **Interaction:** "The AI's line 12 uses `tasks[number]`. Which task does it mark for number 1?" stays on screen with a 10-second timer.
- **Narration:** Restock milk, the second task. Position 1 in a list is the second item.
  **On screen:** Code `examples/ai/write/write_compare.py`, line 12 highlighted, output `examples/ai/write/write_compare.expected`
- **Narration:** Asha's version subtracts 1, so it marks the first task. She keeps her own.
  **On screen:** Code `examples/ai/write/write_compare.py`, line 8 highlighted, output `examples/ai/write/write_compare.expected`
- **Narration:** Breather. Relax your shoulders. The task list works.
  **On screen:** Breather card
    - Tests first, even for empty rules.
    - Every new task is checked.
    - Number minus 1 is the list position.
- **Narration:** Next, saving and loading, written by the AI against her tests.
  **On screen:** Breather card
    - Tests first, even for empty rules.
    - Every new task is checked.
    - Number minus 1 is the list position.
- **Breather:** 4 quiet seconds.

## Scene 9: Step 4: Save and load

**Section:** Build it step by step

**Direction:** Stage 3: the AI's save and load and its promise, the ask, then the run with two failures.

- **Narration:** Step 4: save and load. Stage 3: generate. Asha pastes her ten tests, and asks the AI for the two functions. Do not change my tests.
  **On screen:** AI chat, stage 3: Generate: code that must pass my tests
    - You: Here are my ten tests. Write save_tasks(path, task_list) and load_tasks(path) for my Task and TaskList classes. Do not change my tests. [code `project/test_tasks_core.py`]
- **Narration:** The AI writes both, and says: they pass all ten of your tests.
  **On screen:** AI chat, stage 3: Generate: code that must pass my tests
    - You: Here are my ten tests. Write save_tasks(path, task_list) and load_tasks(path) for my Task and TaskList classes. Do not change my tests. [code `project/test_tasks_core.py`]
    - AI (example answer): Here are both functions. They pass all ten of your tests. [code `examples/ai/flawed/tasks_core.py`]
- **Narration:** Line 47 gives the list of tasks straight to JSON dumps.
  **On screen:** Code `examples/ai/flawed/tasks_core.py`, line 47 highlighted, output hidden
- **Narration:** And load tasks reads the text and gives it to JSON loads, with no other check.
  **On screen:** Code `examples/ai/flawed/tasks_core.py`, line 53, 54, 57, 58 highlighted, output hidden
- **Interaction:** "The AI says these pass all ten tests. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Asha does not argue. She runs her tests.
  **On screen:** Code `examples/ai/flawed/tasks_core.py`, line 53, 54, 57, 58 highlighted, output hidden
- **Narration:** Two fail. Save then load, and the empty file.
  **On screen:** Code `examples/ai/flawed/test_tasks_core.py`, output `examples/ai/flawed/test_tasks_core.expected`
- **Narration:** Eight pass, but a promise of ten is not ten. Her tests caught a confident claim.
  **On screen:** Code `examples/ai/flawed/test_tasks_core.py`, line 46, 58 highlighted, output `examples/ai/flawed/test_tasks_core.expected`

## Scene 10: Step 5: The command loop

**Section:** Build it step by step

**Direction:** Walk run() and the main block, with the finished save and load in place.

- **Narration:** Step 5: the command loop. Task app holds the conversation. Run asks for a command until the user types quit, then returns, which ends the loop.
  **On screen:** Code `project/task_app.py`, line 11, 12, 13, 14 highlighted, output hidden
- **Narration:** Add asks for a title and a priority, and calls the rule.
  **On screen:** Code `project/task_app.py`, line 16, 17, 18, 19 highlighted, output hidden
- **Narration:** Done asks for a number. List prints each line. Anything else shows the commands.
  **On screen:** Code `project/task_app.py`, line 20, 21, 22, 23, 24, 25, 26 highlighted, output hidden
- **Narration:** Every rule raises only value error, with a clear message. So one except catches a bad title, a bad priority and a bad number.
  **On screen:** Code `project/task_app.py`, line 27, 28 highlighted, output hidden
- **Narration:** The main program loads the tasks. A broken file gives one line that starts with tasks not loaded.
  **On screen:** Code `project/task_app.py`, line 31, 32, 33, 34 highlighted, output hidden
- **Narration:** The else block runs only when the tasks loaded. It shows how many are open, runs the loop, and saves.
  **On screen:** Code `project/task_app.py`, line 35, 36, 37, 38, 39 highlighted, output hidden

## Scene 11: Test it

**Section:** Test it

**Direction:** Stage 4: the AI's case list misses the empty file. Stage 5: the last line of the error, cause first, the fix, ten passed. Quiz, then three known-result runs, one with an ask.

- **Narration:** Stage 4: test. Asha asks the AI for test cases for loading, with an expected result for each.
  **On screen:** AI chat, stage 4: Test: cases for loading
    - You: List test cases for load_tasks(path), with the expected result for each. Include unusual files.
- **Narration:** It lists a normal file, a missing file and a broken file. And it says: an empty file is broken JSON, so it should raise an error.
  **On screen:** AI chat, stage 4: Test: cases for loading
    - You: List test cases for load_tasks(path), with the expected result for each. Include unusual files.
    - AI (example answer): 1. A normal file: the saved tasks. 2. A missing file: no tasks. 3. A broken file: a ValueError. 4. An empty file is broken JSON, so it should raise a ValueError too.
- **Narration:** Asha's criterion five says the opposite: an empty file means no tasks yet. Her test already checks it, and it is one of the two that failed. Where the AI and her criteria disagree, her criteria win.
  **On screen:** AI chat, stage 4: Test: cases for loading
    - You: List test cases for load_tasks(path), with the expected result for each. Include unusual files.
    - AI (example answer): 1. A normal file: the saved tasks. 2. A missing file: no tasks. 3. A broken file: a ValueError. 4. An empty file is broken JSON, so it should raise a ValueError too.
- **Narration:** Stage 5: debug. For the other failure, Asha saves one task with the AI's code. It stops with a long error report, through the lines of the JSON module.
  **On screen:** Code `examples/ai/debug/save_crash.py`, line 7 highlighted, error `examples/ai/debug/save_crash.expected_error`
- **Narration:** As she learned in Chapter 1, she finds the error line at the bottom. Type error: object of type Task is not JSON serializable. Serializable means it can be saved as text.
  **On screen:** Code `examples/ai/debug/save_crash.py`, line 7 highlighted, error `examples/ai/debug/save_crash.expected_error`
- **Narration:** Here you see only that error line. On your computer, the report above it shows full file paths, and Python 3.14 and newer add a short note under it.
  **On screen:** Code `examples/ai/debug/save_crash.py`, line 7 highlighted, error `examples/ai/debug/save_crash.expected_error`
- **Narration:** She pastes the code and the error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: save_tasks() stops with TypeError: Object of type Task is not JSON serializable. First explain the cause. Then show the smallest fix.
- **Narration:** The AI explains: JSON can save numbers, text, true and false, None, lists and dictionaries. A task is none of these. So each task becomes a dictionary first, with a new method, to dict.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: save_tasks() stops with TypeError: Object of type Task is not JSON serializable. First explain the cause. Then show the smallest fix.
    - AI (example answer): `json.dumps()` can save numbers, text, True, False, None, lists and dictionaries. A `Task` is none of these. The fix: turn each task into a dictionary first, with a `to_dict()` method. [code `project/tasks_core.py`]
- **Narration:** The new to dict method returns a task as a dictionary.
  **On screen:** Code `examples/ai/fixed/tasks_core.py`, line 13, 14, 15, 16, 17 highlighted, output hidden
- **Narration:** Line 53 turns each task into a dictionary before dumps.
  **On screen:** Code `examples/ai/fixed/tasks_core.py`, line 53 highlighted, output hidden
- **Narration:** And lines 64 and 65 treat an empty file as no tasks, before JSON loads can complain.
  **On screen:** Code `examples/ai/fixed/tasks_core.py`, line 64, 65 highlighted, output hidden
- **Narration:** Then she runs every test again, not only the two that failed. Ten passed.
  **On screen:** Code `examples/ai/fixed/test_tasks_core.py`, output `examples/ai/fixed/test_tasks_core.expected`
- **Narration:** One more check, by hand. Asha saves two tasks, the first one done. Line 10 prints the saved file, and line 11 loads it again.
  **On screen:** Code `examples/step4/save_check.py`, line 8, 9, 10, 11 highlighted, output hidden
- **Interaction:** "After loading the file again, what does line 12 print?" stays on screen with a 10-second timer.
- **Narration:** The same two lines as before saving: task 1 with its x, and task 2 still open.
  **On screen:** Code `examples/step4/save_check.py`, line 12 highlighted, output `examples/step4/save_check.expected`
- **Narration:** And the file shows each task as a dictionary. JSON writes True as true, in small letters.
  **On screen:** Code `examples/step4/save_check.py`, line 10 highlighted, output `examples/step4/save_check.expected`
- **Narration:** Quick check. Which of these can JSON dumps save, as it is?
  **On screen:** Quick check: "Which of these can `json.dumps()` save as it is?" (options shown)
- **Interaction:** "Which of these can `json.dumps()` save as it is?" stays on screen with a 10-second timer.
- **Narration:** C. A dictionary of text, numbers and true. Any other object must become a dictionary first.
  **On screen:** Quick check: "Which of these can `json.dumps()` save as it is?" (answer revealed: A dictionary of text, numbers and `True`)
- **Narration:** Last, Asha runs the whole program on three cases. She writes the expected result first.
  **On screen:** Table: Three runs, with known results
- **Narration:** A first run, with no file yet.
  **On screen:** Table: Three runs, with known results (row 1 in focus)
- **Narration:** Bad answers.
  **On screen:** Table: Three runs, with known results (row 2 in focus)
- **Narration:** And a broken file.
  **On screen:** Table: Three runs, with known results (row 3 in focus)
- **Narration:** No file yet, so zero open tasks. She adds one, lists it, and quits. Pass.
  **On screen:** Code `examples/cases/first_run/task_app.py`, line 32 highlighted, output `examples/cases/first_run/task_app.expected`
- **Narration:** Now bad answers. First, a priority of high. Line 18 turns the answer into a whole number with int, as in Chapter 4.
  **On screen:** Code `examples/cases/bad_input/task_app.py`, line 18 highlighted, output hidden
- **Interaction:** "The user types `high` as the priority. What happens?" stays on screen with a 10-second timer.
- **Narration:** Int raises a value error, and line 28 prints not done, with Python's own message. No crash.
  **On screen:** Code `examples/cases/bad_input/task_app.py`, line 18, 28 highlighted, output `examples/cases/bad_input/task_app.expected`
- **Narration:** An empty title and task 9 are refused too. And an unknown command shows the list of commands. Pass.
  **On screen:** Code `examples/cases/bad_input/task_app.py`, output `examples/cases/bad_input/task_app.expected`
- **Narration:** And the broken file, which is missing a comma between two tasks. Load tasks raises a value error for a broken file.
  **On screen:** Code `examples/cases/bad_json/task_app.py`, line 32 highlighted, output hidden
- **Interaction:** "The file is broken. Will the app crash?" stays on screen with a 10-second timer.
- **Narration:** No. Line 34 prints one clear line: expecting a comma. Pass. All three match.
  **On screen:** Code `examples/cases/bad_json/task_app.py`, line 33, 34 highlighted, output `examples/cases/bad_json/task_app.expected`
- **Narration:** Breather. Every test passes, and every known case matches.
  **On screen:** Breather card
    - Read the error line first.
    - JSON saves dictionaries, not objects.
    - Run every test after every fix.
- **Narration:** Next, the last stage: a review from the AI.
  **On screen:** Breather card
    - Read the error line first.
    - JSON saves dictionaries, not objects.
    - Run every test after every fix.
- **Breather:** 4 quiet seconds.

## Scene 12: Improve it with AI

**Section:** Improve it with AI

**Direction:** Stage 6: remove the priority check. Ask whether the tests still pass, then the run. Six stages table, breather.

- **Narration:** Stage 6: improve. All ten tests pass. Asha asks for one change that makes the module shorter, and says: do not change what it does.
  **On screen:** AI chat, stage 6: Improve: a shorter module
    - You: All ten tests pass. Review my module and suggest one change that makes it shorter. Do not change what it does.
- **Narration:** The AI says: remove the priority check from add. The app already asks for 1 to 3.
  **On screen:** AI chat, stage 6: Improve: a shorter module
    - You: All ten tests pass. Review my module and suggest one change that makes it shorter. Do not change what it does.
    - AI (example answer): Remove the priority check from `add()`. The app already asks for a priority from 1 to 3, so the check is never needed.
- **Narration:** Remember her third test. It adds a task with priority 5, and expects a value error.
  **On screen:** Code `examples/ai/improve/test_tasks_core.py`, line 26 highlighted, output hidden
- **Interaction:** "Without the priority check, will all ten tests still pass?" stays on screen with a 10-second timer.
- **Narration:** No. One fails: the test for a bad priority.
  **On screen:** Code `examples/ai/improve/test_tasks_core.py`, line 26 highlighted, output `examples/ai/improve/test_tasks_core.expected`
- **Narration:** The app's question only asks for 1 to 3. It cannot stop a person who types 5, or another program that uses the task list. The suggestion changed what the code does. Asha keeps her version.
  **On screen:** Code `examples/ai/improve/test_tasks_core.py`, line 26 highlighted, output `examples/ai/improve/test_tasks_core.expected`
- **Narration:** Here are all six stages, on one module of rules.
  **On screen:** Table: Six stages, one module of rules
- **Narration:** The AI helped at every stage, from the plan to the improvement.
  **On screen:** Table: Six stages, one module of rules (row 1 in focus)
- **Narration:** It was confidently wrong five times. A plan that could not be tested.
  **On screen:** Table: Six stages, one module of rules (row 1 in focus)
- **Narration:** The wrong task.
  **On screen:** Table: Six stages, one module of rules (row 2 in focus)
- **Narration:** A promise of ten passes.
  **On screen:** Table: Six stages, one module of rules (row 3 in focus)
- **Narration:** A case list with no empty file.
  **On screen:** Table: Six stages, one module of rules (row 4 in focus)
- **Narration:** And a check it wanted to remove.
  **On screen:** Table: Six stages, one module of rules (row 6 in focus)
- **Narration:** At debug, the AI was right. Asha could tell, because the fix made every test pass.
  **On screen:** Table: Six stages, one module of rules (row 5 in focus)
- **Narration:** Every time, something Asha wrote first decided: her criteria, a side by side run, and her tests.
  **On screen:** Table: Six stages, one module of rules
- **Narration:** Last breather. Before she pasted any code into the chat, Asha checked it for private data, the habit from Chapter 1. Her tasks hold only cafe jobs.
  **On screen:** Breather card
    - A promise is not a result. Run the tests.
    - Your criteria beat the AI's guess.
    - Keep a check your tests need.
- **Narration:** Let's recap.
  **On screen:** Breather card
    - A promise is not a result. Run the tests.
    - Your criteria beat the AI's guess.
    - Keep a check your tests need.
- **Breather:** 4 quiet seconds.

## Scene 13: Recap

**Section:** Recap

**Direction:** Recap points one by one, a final quiz, the badge, a look back at the whole course, and the practice table.

- **Narration:** Here is what you used in the final boss.
  **On screen:** Recap
- **Narration:** Keep the rules free of input and print, so tests can check them.
  **On screen:** Recap
    - Keep the rules free of `input()` and `print()`, so tests can check them.
- **Narration:** Write the tests first. A test that passes on empty rules proves nothing.
  **On screen:** Recap
    - Keep the rules free of `input()` and `print()`, so tests can check them.
    - Write the tests first. A test that passes on empty rules proves nothing.
- **Narration:** Number tasks from 1 for people, and subtract 1 for the list.
  **On screen:** Recap
    - Keep the rules free of `input()` and `print()`, so tests can check them.
    - Write the tests first. A test that passes on empty rules proves nothing.
    - Number tasks from 1 for people, and subtract 1 for the list.
- **Narration:** JSON saves dictionaries, not objects. To dict turns one into the other.
  **On screen:** Recap
    - Keep the rules free of `input()` and `print()`, so tests can check them.
    - Write the tests first. A test that passes on empty rules proves nothing.
    - Number tasks from 1 for people, and subtract 1 for the list.
    - JSON saves dictionaries, not objects. `to_dict()` turns one into the other.
- **Narration:** A missing or empty file can mean nothing yet. A broken one gets a clear message.
  **On screen:** Recap
    - Keep the rules free of `input()` and `print()`, so tests can check them.
    - Write the tests first. A test that passes on empty rules proves nothing.
    - Number tasks from 1 for people, and subtract 1 for the list.
    - JSON saves dictionaries, not objects. `to_dict()` turns one into the other.
    - A missing or empty file can mean nothing yet. A broken one gets a clear message.
- **Narration:** And every AI suggestion was judged by your criteria, a run, or your tests.
  **On screen:** Recap
    - Keep the rules free of `input()` and `print()`, so tests can check them.
    - Write the tests first. A test that passes on empty rules proves nothing.
    - Number tasks from 1 for people, and subtract 1 for the list.
    - JSON saves dictionaries, not objects. `to_dict()` turns one into the other.
    - A missing or empty file can mean nothing yet. A broken one gets a clear message.
    - Every AI suggestion was judged by your criteria, a run, or your tests.
- **Narration:** One last check. An AI says its new code passes all your tests. What do you do?
  **On screen:** Quick check: "An AI says its new code passes all your tests. What do you do?" (options shown)
- **Interaction:** "An AI says its new code passes all your tests. What do you do?" stays on screen with a 10-second timer.
- **Narration:** A. Run the tests yourself. A promise is not a result. Your tests decide.
  **On screen:** Quick check: "An AI says its new code passes all your tests. What do you do?" (answer revealed: Run the tests yourself)
- **Narration:** Final boss complete! You earned 300 XP and the Python Builder badge. Module 6 is done, and so is the course.
  **On screen:** Python Builder You earned 300 XP. The course is complete.
- **Breather:** 2 quiet seconds.
- **Narration:** Look how far you came. In Chapter 1, Asha printed one cafe receipt.
  **On screen:** Look back: 28 chapters
- **Narration:** Then variables, text and input, and the Bill Splitter.
  **On screen:** Look back: 28 chapters
    - Module 1: print, variables, text and input. The Bill Splitter.
- **Narration:** Decisions, loops and debugging, and the Guessing Game.
  **On screen:** Look back: 28 chapters
    - Module 1: print, variables, text and input. The Bill Splitter.
    - Module 2: decisions, loops and debugging. The Guessing Game.
- **Narration:** Lists, dictionaries, tuples and sets, and the Expense Tracker.
  **On screen:** Look back: 28 chapters
    - Module 1: print, variables, text and input. The Bill Splitter.
    - Module 2: decisions, loops and debugging. The Guessing Game.
    - Module 3: lists, dictionaries, tuples, sets. The Expense Tracker.
- **Narration:** Functions, modules and tests, and the Quiz App.
  **On screen:** Look back: 28 chapters
    - Module 1: print, variables, text and input. The Bill Splitter.
    - Module 2: decisions, loops and debugging. The Guessing Game.
    - Module 3: lists, dictionaries, tuples, sets. The Expense Tracker.
    - Module 4: functions, modules and tests. The Quiz App.
- **Narration:** Files, errors, JSON and packages, and the Report Generator.
  **On screen:** Look back: 28 chapters
    - Module 1: print, variables, text and input. The Bill Splitter.
    - Module 2: decisions, loops and debugging. The Guessing Game.
    - Module 3: lists, dictionaries, tuples, sets. The Expense Tracker.
    - Module 4: functions, modules and tests. The Quiz App.
    - Module 5: files, errors, JSON and packages. The Report Generator.
- **Narration:** And classes, safe changes, and today's task manager.
  **On screen:** Look back: 28 chapters
    - Module 1: print, variables, text and input. The Bill Splitter.
    - Module 2: decisions, loops and debugging. The Guessing Game.
    - Module 3: lists, dictionaries, tuples, sets. The Expense Tracker.
    - Module 4: functions, modules and tests. The Quiz App.
    - Module 5: files, errors, JSON and packages. The Report Generator.
    - Module 6: classes, safe changes, and this task manager.
- **Narration:** 28 chapters, 6 boss levels, and one AI habit: check every answer.
  **On screen:** Look back: 28 chapters
    - Module 1: print, variables, text and input. The Bill Splitter.
    - Module 2: decisions, loops and debugging. The Guessing Game.
    - Module 3: lists, dictionaries, tuples, sets. The Expense Tracker.
    - Module 4: functions, modules and tests. The Quiz App.
    - Module 5: files, errors, JSON and packages. The Report Generator.
    - Module 6: classes, safe changes, and this task manager.
- **Narration:** The practice file has eight more tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-ups, worth 10 XP each, such as JSON there and back.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including removing a task.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each, including a load that never crashes.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 14: What's next

**Section:** What's next

**Direction:** End card for the whole course. Next steps: keep building small tools, review chapters, practise. Hold quietly.

- **Narration:** So, what's next? Keep building. Pick a small problem from your own life, plan it, write the tests first, and let an AI help.
  **On screen:** Keep building Small tools, one test at a time, with AI at your side.
- **Narration:** When a topic feels unclear, go back to its chapter. And try the practice tasks you skipped.
  **On screen:** Keep building Small tools, one test at a time, with AI at your side.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Keep building Do the warm-up tasks now. They take about ten minutes.
- **Narration:** Thank you for learning with Asha at the Corner Cafe. Happy coding!
  **On screen:** Keep building Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
