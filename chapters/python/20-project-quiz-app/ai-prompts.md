# AI Prompt Cards: Chapter 20

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. Your tests decide who is right, not the AI.

## Plan: Files and functions before code

**Prompt:** "I am a beginner. I know functions, modules and pytest. I want <describe the program, for example: a staff quiz with four questions, a check for each answer, a percentage and a grade>. I will write the tests first. Do not write code. List the functions I need, and say which file each one goes in."

**Use it when:** you know what the program must do, but not how to split it into files and functions.

**A good answer:** a short list of files, each with one job, and functions that each do one thing.

**Check it:** for each function, ask "can a test call this without a person typing?" A function that calls `input()` or `print()` mixes a rule with talking. Split it, as Chapter 17 taught.

## Write: Compare your function with the AI's

**Prompt:** "Write a Python function check_answer(given, correct) that returns True when the answer matches, ignoring spaces around it and capital letters. A blank answer is wrong. Show only the function."

**Use it when:** you have written a function yourself and want a second version to compare with.

**A good answer:** a function of one or two lines that uses `strip()` and `lower()`, and returns a value instead of printing it.

**Check it:** run both versions on the same answers, including one with spaces, one with capitals and an empty one. Every result must be the same.

## Generate: Code that must pass your tests

**Prompt:** "Here are my pytest tests: <paste the test file>. Write the module <name>.py with the functions the tests import. Use only what a beginner knows: functions, if, elif, else, round() and f-strings. Do not change my tests."

**Use it when:** your tests are written and you want help with the code.

**A good answer:** one module with exactly the functions the tests import, each with a docstring, and no changes to the tests.

**Check it:** run `pytest -q --tb=no -rf`. Every test must pass. If the AI says "this passes all your tests", that is a prediction. The report is the result.

## Test: Read a failure report with the AI

**Prompt:** "My tests fail on the AI's module. Here is the report: <paste the pytest report>. Which function do the failing tests have in common? Do not fix anything yet."

**Use it when:** several tests fail and you want to find the one rule they share.

**A good answer:** the name of the function that every failing test calls, and the line of the report that shows a wrong value.

**Check it:** read the report yourself. Each `FAILED` line names a test. Open those tests and see which function they call.

## Debug: The cause before the fix

**Prompt:** "This test fails: <paste the test and the full report>. Here is the function: <paste it>. First explain why it returns <the wrong value>. Then show the smallest fix. Do not change the test."

**Use it when:** you know which function is wrong but not why.

**A good answer:** it names the exact operation that goes wrong, such as `//`, explains it with the numbers from the report, and changes one line.

**Check it:** make the one change and run all the tests again, not only the one that failed.

## Improve: Shorter, with the same results

**Prompt:** "Make this function shorter: <paste it>. Do not change what it returns for any input. Explain each change in one sentence."

**Use it when:** your code works and every test passes, and you want it easier to read.

**A good answer:** a shorter version, with a reason for each change and no change in behaviour.

**Check it:** run every test again. Look closely at signs such as `>` and `>=`. The boundary tests exist to catch exactly that.
