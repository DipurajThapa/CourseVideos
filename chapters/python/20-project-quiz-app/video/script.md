# Video Script: Chapter 20: Boss Level 4: The Tested Quiz App

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 15:46.

## Scene 1: Introduction (0:00 to 0:33)

**Section:** Introduction

**Direction:** Open on the staff problem with a safety stake. Then the boss level title and the test-first promise.

- **Narration:** At the Corner Cafe, new staff ask Asha the same questions every week. How much is a scone? Which cake has nuts? Is the soup vegan?
  **On screen:** Which cake has nuts?
- **Narration:** A wrong price is embarrassing. A wrong answer about nuts can make a customer ill.
  **On screen:** Which cake has nuts?
- **Narration:** Welcome to Chapter 20, the fourth boss level!
  **On screen:** The Tested Quiz App
- **Narration:** Asha will build a staff quiz from three modules, and she will write its tests before its code.
  **On screen:** The Tested Quiz App Tests first. Then the code.
- **Narration:** An AI assistant will write part of the code, and promise that it passes every test. The tests will have the last word.
  **On screen:** The Tested Quiz App Tests first. Then the code.

## Scene 2: The mission (0:33 to 1:14)

**Section:** The mission

**Direction:** The quiz's job, then the chapters it uses, row by row.

- **Narration:** Here is the mission. A quiz with four questions about prices and allergens.
  **On screen:** The staff quiz
    - Four questions about prices and allergens.
- **Narration:** After each answer, it says Correct, or it gives the right answer.
  **On screen:** The staff quiz
    - Four questions about prices and allergens.
    - After each answer: right, or the correct answer.
- **Narration:** At the end, a score, a percentage and a grade.
  **On screen:** The staff quiz
    - Four questions about prices and allergens.
    - After each answer: right, or the correct answer.
    - At the end: a score, a percentage and a grade.
- **Narration:** And this time, Asha works like a software team. The tests come first.
  **On screen:** The staff quiz
    - Four questions about prices and allergens.
    - After each answer: right, or the correct answer.
    - At the end: a score, a percentage and a grade.
    - This time, the tests come first.
- **Narration:** Every piece comes from Module 4. Functions from Chapter 16.
  **On screen:** Table: Everything from Module 4 (row 1 in focus)
- **Narration:** Pure functions with one job each, from Chapter 17.
  **On screen:** Table: Everything from Module 4 (row 2 in focus)
- **Narration:** Your own modules, from Chapter 18.
  **On screen:** Table: Everything from Module 4 (row 3 in focus)
- **Narration:** And pytest from Chapter 19.
  **On screen:** Table: Everything from Module 4 (row 4 in focus)
- **Narration:** Plus one new pytest option. Dash dash t b equals no hides the details of each failure, so the report is a short list.
  **On screen:** Table: Everything from Module 4 (row 5 in focus)

## Scene 3: What you will build (1:14 to 1:47)

**Section:** What you will build

**Direction:** The three files and the test file, then one finished run as the destination.

- **Narration:** The quiz has three files, each with one job. Quiz data holds the questions.
  **On screen:** Table: Three files, one job each (row 1 in focus)
- **Narration:** Quiz logic holds the rules.
  **On screen:** Table: Three files, one job each (row 2 in focus)
- **Narration:** Quiz app does the talking: it asks and prints.
  **On screen:** Table: Three files, one job each (row 3 in focus)
- **Narration:** And a test file checks the rules.
  **On screen:** Table: Three files, one job each (row 4 in focus)
- **Narration:** Here is one finished run. A new barista answers four questions.
  **On screen:** Code `project/quiz_app.py`, output `project/quiz_app.expected`
- **Narration:** The soup is vegan, so no was wrong. The quiz gives the right answer.
  **On screen:** Code `project/quiz_app.py`, output `project/quiz_app.expected`
- **Narration:** Three out of four is 75 percent: the grade Ready.
  **On screen:** Code `project/quiz_app.py`, output `project/quiz_app.expected`
- **Narration:** The app itself is only fourteen lines. The rules live in another file.
  **On screen:** Code `project/quiz_app.py`, output `project/quiz_app.expected`

## Scene 4: Acceptance criteria (1:47 to 2:48)

**Section:** Acceptance criteria

**Direction:** Six criteria in groups, a quiz on the pure-rule criterion, then a breather.

- **Narration:** Asha writes down what done means.
  **On screen:** Done means all six are true
- **Narration:** One and two. The questions live in one module, and the rules in another. No rule asks or prints.
  **On screen:** Done means all six are true
    - The questions live in `quiz_data.py`.
    - The rules live in `quiz_logic.py`, with no `input()` or `print()`.
- **Narration:** Three. Spaces and capitals do not matter, and a blank answer is wrong.
  **On screen:** Done means all six are true
    - The questions live in `quiz_data.py`.
    - The rules live in `quiz_logic.py`, with no `input()` or `print()`.
    - Spaces and capitals do not matter. A blank answer is wrong.
- **Narration:** Four and five. A whole-number percentage, a grade, and a last line like this one.
  **On screen:** Done means all six are true
    - The questions live in `quiz_data.py`.
    - The rules live in `quiz_logic.py`, with no `input()` or `print()`.
    - Spaces and capitals do not matter. A blank answer is wrong.
    - A whole-number percentage: 75 or more is Ready, 50 or more is Almost.
    - The last line looks like `Score: 3/4 (75%) Ready`.
- **Narration:** And six. Eight tests, written first, all pass, and four typed runs give known results.
  **On screen:** Done means all six are true
    - The questions live in `quiz_data.py`.
    - The rules live in `quiz_logic.py`, with no `input()` or `print()`.
    - Spaces and capitals do not matter. A blank answer is wrong.
    - A whole-number percentage: 75 or more is Ready, 50 or more is Almost.
    - The last line looks like `Score: 3/4 (75%) Ready`.
    - Eight tests, written first, all pass. Four typed runs give known results.
- **Narration:** Quick check, from Chapter 17. Why must the check answer rule not call input?
  **On screen:** Quick check: "Why must the rule `check_answer()` not call `input()`?" (options shown)
- **Interaction:** "Why must the rule `check_answer()` not call `input()`?" stays on screen with a 10-second timer.
- **Narration:** B. A test calls the rule with fixed values. A rule that waits for a person to type cannot be tested.
  **On screen:** Quick check: "Why must the rule `check_answer()` not call `input()`?" (answer revealed: A test cannot type an answer)
- **Narration:** Take a breather. You know the files, and what done means.
  **On screen:** Breather card
    - Three files, one job each.
    - Rules never ask or print.
    - Eight tests say when it is done.
- **Narration:** Next, Asha plans the functions with an AI assistant.
  **On screen:** Breather card
    - Three files, one job each.
    - Rules never ask or print.
    - Eight tests say when it is done.
- **Breather:** 4 quiet seconds.

## Scene 5: Plan it with AI (2:48 to 3:31)

**Section:** Plan it with AI

**Direction:** Stage 1: the AI's plan puts input() inside a rule. Asha checks it against criterion two and replaces it.

- **Narration:** In this project, all six AI stages help build one module: the rules. Stage 1: plan. Asha asks for the functions she needs, and says: no code yet.
  **On screen:** AI chat, stage 1: Plan: files and functions
    - You: I am a beginner. I know functions, modules and pytest. I want a staff quiz with four questions, a check for each answer, a percentage and a grade. I will write the tests first. Do not write code. List the functions I need, and the file for each one.
- **Narration:** The AI suggests three files and four functions. The first one, ask and check, asks the question with input, checks the answer and returns True or False.
  **On screen:** AI chat, stage 1: Plan: files and functions
    - You: I am a beginner. I know functions, modules and pytest. I want a staff quiz with four questions, a check for each answer, a percentage and a grade. I will write the tests first. Do not write code. List the functions I need, and the file for each one.
    - AI (example answer): Use three files. In `quiz_logic.py`, write `ask_and_check(question)`: it asks with `input()`, checks the answer and returns True or False. Also add `percentage()`, `grade()` and `result_line()`.
- **Narration:** Asha checks it against criterion two. Ask and check does two jobs, and one of them waits for a person to type. No test can check it.
  **On screen:** AI chat, stage 1: Plan: files and functions
    - You: I am a beginner. I know functions, modules and pytest. I want a staff quiz with four questions, a check for each answer, a percentage and a grade. I will write the tests first. Do not write code. List the functions I need, and the file for each one.
    - AI (example answer): Use three files. In `quiz_logic.py`, write `ask_and_check(question)`: it asks with `input()`, checks the answer and returns True or False. Also add `percentage()`, `grade()` and `result_line()`.
- **Narration:** So she keeps the three files and the last three functions. She replaces the first one with a pure rule: check answer, given and correct. The app asks. The rule only compares.
  **On screen:** AI chat, stage 1: Plan: files and functions
    - You: I am a beginner. I know functions, modules and pytest. I want a staff quiz with four questions, a check for each answer, a percentage and a grade. I will write the tests first. Do not write code. List the functions I need, and the file for each one.
    - AI (example answer): Use three files. In `quiz_logic.py`, write `ask_and_check(question)`: it asks with `input()`, checks the answer and returns True or False. Also add `percentage()`, `grade()` and `result_line()`.

## Scene 6: Step 1: The questions (3:31 to 4:20)

**Section:** Build it step by step

**Direction:** The data module, then a short program that reads it, with an ask.

- **Narration:** Time to build. Step 1: the data. Each question is a dictionary with two keys, a question and an answer.
  **On screen:** Code `project/quiz_data.py`, line 4 highlighted, output hidden
- **Narration:** The list on lines 3 to 8 keeps the four questions in order.
  **On screen:** Code `project/quiz_data.py`, line 3, 4, 5, 6, 7, 8 highlighted, output hidden
- **Narration:** The name is in capital letters. Programmers use capitals for a value that the program reads but never changes.
  **On screen:** Code `project/quiz_data.py`, line 3 highlighted, output hidden
- **Narration:** This short program imports the list from the module, as in Chapter 18.
  **On screen:** Code `examples/ex01_data.py`, line 2 highlighted, output hidden
- **Narration:** Line 5 takes the first dictionary. Lines 6 and 7 print its question and its answer.
  **On screen:** Code `examples/ex01_data.py`, line 5, 6, 7 highlighted, output hidden
- **Interaction:** "What do lines 4, 6 and 7 print?" stays on screen with a 10-second timer.
- **Narration:** 4 questions. Then the first question, price of a tea, and its answer, 3.50.
  **On screen:** Code `examples/ex01_data.py`, line 4, 6, 7 highlighted, output `examples/ex01_data.expected`

## Scene 7: Step 2: Tests first (4:20 to 6:25)

**Section:** Build it step by step

**Direction:** Walk the test file in groups, teach assert not and the docstring-only stub returning None, then predict how many tests pass. Quiz on test-first.

- **Narration:** Step 2 is the big change. Asha writes the tests before any rule exists. Line 3 imports the four rules she plans to write, by name.
  **On screen:** Code `project/test_quiz_logic.py`, line 3 highlighted, output hidden
- **Narration:** Lines 6 and 7: an exact answer is right. Lines 10 and 11: spaces and capitals are still right.
  **On screen:** Code `project/test_quiz_logic.py`, line 6, 7, 10, 11 highlighted, output hidden
- **Narration:** Lines 14 to 19 use assert not. It checks that something is false. A wrong answer and a blank answer must not count.
  **On screen:** Code `project/test_quiz_logic.py`, line 14, 15, 18, 19 highlighted, output hidden
- **Narration:** Lines 22 and 23: three out of four is 75. Lines 26 and 27: two out of three rounds to 67.
  **On screen:** Code `project/test_quiz_logic.py`, line 22, 23, 26, 27 highlighted, output hidden
- **Narration:** Lines 31 to 34 test the edges of each grade: 75 and 74, then 50 and 49.
  **On screen:** Code `project/test_quiz_logic.py`, line 30, 31, 32, 33, 34 highlighted, output hidden
- **Narration:** And line 38 tests the whole last line.
  **On screen:** Code `project/test_quiz_logic.py`, line 37, 38 highlighted, output hidden
- **Narration:** To run the tests, the rules need names. Asha writes each function with only its docstring. No code yet.
  **On screen:** Code `examples/testfirst/quiz_logic.py`, line 5, 6 highlighted, output hidden
- **Narration:** A function whose body is only a docstring returns None, as in Chapter 16.
  **On screen:** Code `examples/testfirst/quiz_logic.py`, line 5, 6, 9, 10, 13, 14, 17, 18 highlighted, output hidden
- **Interaction:** "With these empty rules, how many of the eight tests pass?" stays on screen with a 10-second timer.
- **Narration:** Asha runs pytest with dash q and dash dash t b equals no.
  **On screen:** Code `examples/testfirst/quiz_logic.py`, line 5, 6, 9, 10, 13, 14, 17, 18 highlighted, output hidden
- **Narration:** Two pass, and six fail. The six fail as expected, because there is no code.
  **On screen:** Code `examples/testfirst/test_quiz_logic.py`, output `examples/testfirst/test_quiz_logic.expected`
- **Narration:** Here is something new. If and not treat None as false, so not None is True. That is why the wrong-answer and blank-answer tests pass already.
  **On screen:** Code `examples/testfirst/test_quiz_logic.py`, line 14, 15, 18, 19 highlighted, output `examples/testfirst/test_quiz_logic.expected`
- **Narration:** A test that says this must be false is weak on its own. The exact-answer test is its partner, and it fails until the rule works.
  **On screen:** Code `examples/testfirst/test_quiz_logic.py`, output `examples/testfirst/test_quiz_logic.expected`
- **Narration:** Quick check. You write the tests first. What should most of them do before any code exists?
  **On screen:** Quick check: "You write the tests first. What should most of them do before any code exists?" (options shown)
- **Interaction:** "You write the tests first. What should most of them do before any code exists?" stays on screen with a 10-second timer.
- **Narration:** C. Fail. A test that checks real behaviour fails until the code is right. That failure is the starting line.
  **On screen:** Quick check: "You write the tests first. What should most of them do before any code exists?" (answer revealed: Fail)

## Scene 8: Step 3: The first rule (6:25 to 7:57)

**Section:** Build it step by step

**Direction:** Asha writes check_answer herself, predicts the run, then stage 2: the AI's version, compared on four answers. Breather.

- **Narration:** Step 3. Asha writes the first rule herself.
  **On screen:** Code `examples/step3/quiz_logic.py`, line 5, 6, 7 highlighted, output hidden
- **Narration:** Line 7: strip removes the spaces around the answer, and lower removes the capitals. The correct answer gets lower too, so the data may use capitals.
  **On screen:** Code `examples/step3/quiz_logic.py`, line 7 highlighted, output hidden
- **Interaction:** "With this rule done, which tests pass now?" stays on screen with a 10-second timer.
- **Narration:** Asha runs the tests again.
  **On screen:** Code `examples/step3/quiz_logic.py`, line 7 highlighted, output hidden
- **Narration:** The four answer tests pass. The first four characters of the report are dots.
  **On screen:** Code `examples/step3/test_quiz_logic.py`, line 6, 7, 10, 11, 14, 15, 18, 19 highlighted, output `examples/step3/test_quiz_logic.expected`
- **Narration:** The four rules without code still fail. One step at a time, the dots replace the F's.
  **On screen:** Code `examples/step3/test_quiz_logic.py`, output `examples/step3/test_quiz_logic.expected`
- **Narration:** Stage 2: write. Asha wrote her rule first. Now she asks the AI for its own version, without showing hers.
  **On screen:** AI chat, stage 2: Write it yourself, then compare
    - You: Write a function check_answer(given, correct) that returns True when the answer matches, ignoring spaces and capitals. Show only the function.
- **Narration:** The AI calls lower before strip. A different order. Asha renames it ai version, so both functions can sit in one file. Does the order matter?
  **On screen:** AI chat, stage 2: Write it yourself, then compare
    - You: Write a function check_answer(given, correct) that returns True when the answer matches, ignoring spaces and capitals. Show only the function.
    - AI (example answer): Here is the function: [code `examples/ai/write_compare.py`]
- **Narration:** Asha runs both on the same four answers. Line 10 holds the answers.
  **On screen:** Code `examples/ai/write_compare.py`, line 10 highlighted, output `examples/ai/write_compare.expected`
- **Narration:** Exclamation mark r in line 11 prints each answer with its quotation marks, so you can see the spaces and the empty answer.
  **On screen:** Code `examples/ai/write_compare.py`, line 11 highlighted, output `examples/ai/write_compare.expected`
- **Narration:** Every row matches: True, True, False, False. Both versions agree, so she keeps her own.
  **On screen:** Code `examples/ai/write_compare.py`, line 11 highlighted, output `examples/ai/write_compare.expected`
- **Narration:** Breather. Relax your shoulders. One rule is done, and the tests say so.
  **On screen:** Breather card
    - Tests first: six failed, two passed.
    - `not None` is True, so pair weak tests.
    - One rule done, four tests pass.
- **Narration:** Next, Asha lets the AI write the other three rules.
  **On screen:** Breather card
    - Tests first: six failed, two passed.
    - `not None` is True, so pair weak tests.
    - One rule done, four tests pass.
- **Breather:** 4 quiet seconds.

## Scene 9: Step 4: Let the tests judge the AI (7:57 to 10:29)

**Section:** Build it step by step

**Direction:** Stage 3: the AI's percentage rule and its promise; the learner predicts percentage(3, 4). Stage 4: the run, three failures, the shared function. Stage 5: the report, the cause, the fix, all eight again. Quiz, breather.

- **Narration:** Step 4. Stage 3: generate. Asha pastes her tests and asks for the other three rules. Do not change my tests.
  **On screen:** AI chat, stage 3: Generate: code that must pass my tests
    - You: Here are my eight tests. check_answer() is done. Write percentage(), grade() and result_line() so that all eight pass. Do not change my tests. [code `project/test_quiz_logic.py`]
- **Narration:** The AI writes the module, and says: this passes all eight of your tests. It sounds sure.
  **On screen:** AI chat, stage 3: Generate: code that must pass my tests
    - You: Here are my eight tests. check_answer() is done. Write percentage(), grade() and result_line() so that all eight pass. Do not change my tests. [code `project/test_quiz_logic.py`]
    - AI (example answer): Here is the percentage rule. The other two follow the grades in your tests. This module passes all eight of your tests. [code `examples/ai/flawed/quiz_logic.py`]
- **Narration:** Look at line 12. Remember floor division from Chapter 2: the double slash keeps only the whole part.
  **On screen:** AI chat, stage 3: Generate: code that must pass my tests
    - You: Here are my eight tests. check_answer() is done. Write percentage(), grade() and result_line() so that all eight pass. Do not change my tests. [code `project/test_quiz_logic.py`]
    - AI (example answer): Here is the percentage rule. The other two follow the grades in your tests. This module passes all eight of your tests. [code `examples/ai/flawed/quiz_logic.py`]
- **Interaction:** "With the AI's line 12, what does `percentage(3, 4)` return?" stays on screen with a 10-second timer.
- **Narration:** 0. Three double slash four is 0, and 0 times 100 is still 0. The AI's promise is wrong. Asha runs the tests to be sure.
  **On screen:** AI chat, stage 3: Generate: code that must pass my tests
    - You: Here are my eight tests. check_answer() is done. Write percentage(), grade() and result_line() so that all eight pass. Do not change my tests. [code `project/test_quiz_logic.py`]
    - AI (example answer): Here is the percentage rule. The other two follow the grades in your tests. This module passes all eight of your tests. [code `examples/ai/flawed/quiz_logic.py`]
- **Narration:** Stage 4: test. Asha runs her eight tests on the AI's module. The first four dots are her own rule. Then F, F, a dot, and F.
  **On screen:** Code `examples/ai/flawed/test_quiz_logic.py`, output `examples/ai/flawed/test_quiz_logic.expected`
- **Narration:** Three tests fail: three of four, percentage rounds, and result line.
  **On screen:** Code `examples/ai/flawed/test_quiz_logic.py`, line 22, 23, 26, 27, 37, 38 highlighted, output `examples/ai/flawed/test_quiz_logic.expected`
- **Narration:** She asks the AI what the three failing tests have in common, and says: do not fix anything yet.
  **On screen:** AI chat, stage 4: Test: which rule do the failures share?
    - You: I ran my eight tests on your module. Three failed: test_three_of_four, test_percentage_rounds and test_result_line. Which function do they have in common? Do not fix anything yet.
- **Narration:** All three call percentage. Two test it directly, and result line uses it for the score.
  **On screen:** AI chat, stage 4: Test: which rule do the failures share?
    - You: I ran my eight tests on your module. Three failed: test_three_of_four, test_percentage_rounds and test_result_line. Which function do they have in common? Do not fix anything yet.
    - AI (example answer): All three failing tests call `percentage()`. Two test it directly, and `result_line()` uses it for the score.
- **Narration:** Stage 5: debug. Asha copies one failing test into a small file of its own, and runs it with the details on, using dash dash t b equals short from Chapter 19.
  **On screen:** Code `examples/ai/debug/test_percentage.py`, line 6 highlighted, output `examples/ai/debug/test_percentage.expected`
- **Narration:** The report shows the test line, and the real value: 0, not 75. The where line says the 0 came from percentage of 3 and 4.
  **On screen:** Code `examples/ai/debug/test_percentage.py`, line 6 highlighted, output `examples/ai/debug/test_percentage.expected`
- **Narration:** She pastes the report and asks for the cause first, then the smallest fix.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: The report says percentage(3, 4) gives 0. First explain why. Then show the smallest fix. Do not change the test.
- **Narration:** The AI explains the double slash. Its fix divides with a single slash first, and rounds at the end. One line changes.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: The report says percentage(3, 4) gives 0. First explain why. Then show the smallest fix. Do not change the test.
    - AI (example answer): `//` is floor division. 3 // 4 is 0, and 0 times 100 is still 0. The fix: divide with `/` first, and round at the end. [code `project/quiz_logic.py`]
- **Narration:** Asha does not run only the test that failed. She runs all eight again.
  **On screen:** Code `project/test_quiz_logic.py`, line 22, 23, 26, 27 highlighted, output `project/test_quiz_logic.expected`
- **Narration:** Eight dots. Eight passed. The AI sounded sure the first time. The tests were the only thing that knew.
  **On screen:** Code `project/test_quiz_logic.py`, line 22, 23, 26, 27 highlighted, output `project/test_quiz_logic.expected`
- **Narration:** Quick check. You fix one rule. Which tests do you run next?
  **On screen:** Quick check: "You fix one rule. Which tests do you run next?" (options shown)
- **Interaction:** "You fix one rule. Which tests do you run next?" stays on screen with a 10-second timer.
- **Narration:** D. All of them. A small fix can break something else, and only a full run shows it.
  **On screen:** Quick check: "You fix one rule. Which tests do you run next?" (answer revealed: All of them)
- **Narration:** Breather. The rules are finished, and every test passes.
  **On screen:** Breather card
    - The AI said all eight pass. Three failed.
    - `//` gave 0 for 3 out of 4.
    - After the fix, all eight ran again.
- **Narration:** Now, the app that does the talking.
  **On screen:** Breather card
    - The AI said all eight pass. Three failed.
    - `//` gave 0 for 3 out of 4.
    - After the fix, all eight ran again.
- **Breather:** 4 quiet seconds.

## Scene 10: Step 5: The app (10:29 to 11:14)

**Section:** Build it step by step

**Direction:** Walk the app in groups, then predict the last line for full marks, revealed with a verified run.

- **Narration:** Step 5. Lines 3 and 4 import the data and two rules.
  **On screen:** Code `project/quiz_app.py`, line 3, 4 highlighted, output hidden
- **Narration:** The loop on line 7 takes each question. Line 8 asks it. Plus a space puts a space after the question mark.
  **On screen:** Code `project/quiz_app.py`, line 7, 8 highlighted, output hidden
- **Narration:** Lines 9 to 11: if the rule says right, print Correct, and add a point.
  **On screen:** Code `project/quiz_app.py`, line 9, 10, 11 highlighted, output hidden
- **Narration:** Otherwise, lines 12 and 13 give the right answer.
  **On screen:** Code `project/quiz_app.py`, line 12, 13 highlighted, output hidden
- **Narration:** Line 14 hands the count to result line and prints what it returns.
  **On screen:** Code `project/quiz_app.py`, line 14 highlighted, output hidden
- **Narration:** Your turn. A new barista gets all four answers right.
  **On screen:** Code `examples/apptest/full_marks.py`, line 14 highlighted, output hidden
- **Interaction:** "What is the last line of the quiz?" stays on screen with a 10-second timer.
- **Narration:** Score, 4 out of 4, 100 percent, Ready.
  **On screen:** Code `examples/apptest/full_marks.py`, line 14 highlighted, output `examples/apptest/full_marks.expected`

## Scene 11: Test it (11:14 to 12:20)

**Section:** Test it

**Direction:** Four typed runs with expected last lines, a prediction on spaces and capitals, the blank run as proof, then the results table.

- **Narration:** The rules pass their tests. Now Asha tests the whole app. Each run is a copy of the app with its own typed answers, and a last line she knows in advance.
  **On screen:** Table: Four typed runs
- **Narration:** Full marks, which you predicted.
  **On screen:** Table: Four typed runs (row 1 in focus)
- **Narration:** Zero. Three for the tea is close to 3.50, but it is not the same text, so it is wrong.
  **On screen:** Table: Four typed runs (row 2 in focus)
- **Narration:** Spaces and capitals.
  **On screen:** Table: Four typed runs (row 3 in focus)
- **Narration:** And four blank answers.
  **On screen:** Table: Four typed runs (row 4 in focus)
- **Narration:** The spaces and capitals run. For the cake, the barista types CARROT in capitals, with spaces around it.
  **On screen:** Code `examples/apptest/mixed_case.py`, line 9 highlighted, output hidden
- **Interaction:** "Does `"  CARROT "` count as a right answer?" stays on screen with a 10-second timer.
- **Narration:** Yes. Strip removes the spaces, and lower removes the capitals. Correct! All four count: 100 percent. Pass.
  **On screen:** Code `examples/apptest/mixed_case.py`, line 9 highlighted, output `examples/apptest/mixed_case.expected`
- **Narration:** Four blank answers. Each one gets the right answer printed, and the score is 0. No crash. Pass.
  **On screen:** Code `examples/apptest/blank.py`, line 9 highlighted, output `examples/apptest/blank.expected`
- **Narration:** Here are the results. Every real last line matches what Asha expected.
  **On screen:** Table: Four typed runs: results
- **Narration:** All four runs pass, and so do the eight tests.
  **On screen:** Table: Four typed runs: results

## Scene 12: Improve it with AI (12:20 to 13:57)

**Section:** Improve it with AI

**Direction:** Stage 6: a shorter grade() that changes one sign. Ask what grade(75) returns, then the test run. Six stages table, breather.

- **Narration:** Stage 6: improve. Every test passes. Asha asks the AI to make grade shorter, and says: do not change what it returns.
  **On screen:** AI chat, stage 6: Improve: a shorter grade()
    - You: Every test passes. Make grade() shorter. Do not change what it returns. [code `project/quiz_logic.py`]
- **Narration:** The AI says: drop elif and else, because return already stops the function. That idea is correct.
  **On screen:** AI chat, stage 6: Improve: a shorter grade()
    - You: Every test passes. Make grade() shorter. Do not change what it returns. [code `project/quiz_logic.py`]
    - AI (example answer): Drop `elif` and `else`. `return` already stops the function, so the next line runs only when the first check is false.
- **Narration:** Here is the AI's shorter version. Read line 17 carefully, and compare it with Asha's rule: 75 or more is Ready.
  **On screen:** Code `examples/ai/improve/quiz_logic.py`, line 17 highlighted, output hidden
- **Interaction:** "With the AI's version, what does `grade(75)` return?" stays on screen with a 10-second timer.
- **Narration:** Almost. Line 17 says greater than 75, not greater than or equal. The AI changed one sign.
  **On screen:** Code `examples/ai/improve/quiz_logic.py`, line 17 highlighted, output hidden
- **Narration:** Asha runs her tests. Two fail: the grade boundaries, and the last line, which now ends in Almost, because it uses grade.
  **On screen:** Code `examples/ai/improve/test_quiz_logic.py`, line 31 highlighted, output `examples/ai/improve/test_quiz_logic.expected`
- **Narration:** Line 31, the boundary test from step 2, found it in less than a second.
  **On screen:** Code `examples/ai/improve/test_quiz_logic.py`, line 31 highlighted, output `examples/ai/improve/test_quiz_logic.expected`
- **Narration:** Asha keeps her own grade, and runs all eight tests one more time. Eight passed.
  **On screen:** Code `project/test_quiz_logic.py`, line 31 highlighted, output `project/test_quiz_logic.expected`
- **Narration:** Here are all six stages, on one module of rules.
  **On screen:** Table: Six stages, one module of rules
- **Narration:** The AI helped at every stage, from the plan to the improvement.
  **On screen:** Table: Six stages, one module of rules (row 1 in focus)
- **Narration:** And it was confidently wrong three times: the plan, the percentage, and the shorter grade.
  **On screen:** Table: Six stages, one module of rules (row 3 in focus)
- **Narration:** Every time, something Asha wrote first caught it: criterion two, then her tests.
  **On screen:** Table: Six stages, one module of rules (row 6 in focus)
- **Narration:** Last breather. You built software with tests, and you made the decisions.
  **On screen:** Breather card
    - Tests first, then the code.
    - The AI's promises were checked by tests.
    - Edge tests caught a one-sign change.
- **Narration:** Let's recap.
  **On screen:** Breather card
    - Tests first, then the code.
    - The AI's promises were checked by tests.
    - Edge tests caught a one-sign change.
- **Breather:** 4 quiet seconds.

## Scene 13: Recap (13:57 to 15:23)

**Section:** Recap

**Direction:** Recap points one by one, a final quiz on a boundary, the badge and the practice table.

- **Narration:** Here is what you used in this boss level.
  **On screen:** Recap
- **Narration:** Split a program by job: data, rules, and the app that talks.
  **On screen:** Recap
    - Split a program by job: data, rules and the app that talks.
- **Narration:** Keep rules pure, with no input and no print, so a test can check them.
  **On screen:** Recap
    - Split a program by job: data, rules and the app that talks.
    - Keep rules pure, with no `input()` and no `print()`, so a test can check them.
- **Narration:** Write the tests first. With no code yet, most of them should fail.
  **On screen:** Recap
    - Split a program by job: data, rules and the app that talks.
    - Keep rules pure, with no `input()` and no `print()`, so a test can check them.
    - Write the tests first. With no code yet, most of them should fail.
- **Narration:** Give an AI your tests. Then run them yourself. The report decides, not the AI.
  **On screen:** Recap
    - Split a program by job: data, rules and the app that talks.
    - Keep rules pure, with no `input()` and no `print()`, so a test can check them.
    - Write the tests first. With no code yet, most of them should fail.
    - Give an AI your tests. Then run them yourself: the report decides.
- **Narration:** And test the edges, such as exactly 75.
  **On screen:** Recap
    - Split a program by job: data, rules and the app that talks.
    - Keep rules pure, with no `input()` and no `print()`, so a test can check them.
    - Write the tests first. With no code yet, most of them should fail.
    - Give an AI your tests. Then run them yourself: the report decides.
    - Test the edges, such as exactly 75.
- **Narration:** One last check, on an edge. With Asha's final rules, what does grade of 50 return?
  **On screen:** Quick check: "With Asha's final rules, what does `grade(50)` return?" (options shown)
- **Interaction:** "With Asha's final rules, what does `grade(50)` return?" stays on screen with a 10-second timer.
- **Narration:** A. Almost. 50 is not 75 or more, but it is 50 or more. An edge, and the test on line 33 checks it.
  **On screen:** Quick check: "With Asha's final rules, what does `grade(50)` return?" (answer revealed: Almost)
- **Narration:** Boss level complete! You earned 300 XP and the Software Builder badge. And Module 4 is done.
  **On screen:** Software Builder You earned 300 XP. Module 4 is complete.
- **Breather:** 2 quiet seconds.
- **Narration:** The practice file has eight more tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-ups, worth 10 XP each, such as checks before you trust a rule.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including tests first for the change a customer gets.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's counter that skips the first answer.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Write the checks first, then the code.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 14: What's next (15:23 to 15:46)

**Section:** What's next

**Direction:** End card. Tease files: the scores disappear when the quiz closes. Hold quietly at the end.

- **Narration:** The quiz works, and every test passes. But when the quiz closes, every score disappears. Asha cannot see who needs more practice.
  **On screen:** Files and Paths: Saving and Loading Data Keep your data when the program closes.
- **Narration:** In Chapter 21, you will save data to a file and load it again, so the cafe keeps every score.
  **On screen:** Files and Paths: Saving and Loading Data Keep your data when the program closes.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Files and Paths: Saving and Loading Data Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 21.
  **On screen:** Files and Paths: Saving and Loading Data Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
