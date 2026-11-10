# AI Prompt Cards: Chapter 28

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data, such as names or phone numbers in your task list. Always run the code yourself. Your tests decide who is right, not the AI.

## Plan: Testable rules before code

**Prompt:** "I am a beginner. I know classes, data classes, files, JSON, try and except, functions and pytest. I want <describe the program, for example: a command-line task manager with add, done, list and quit, saved in a JSON file>. Do not write code. Plan the classes and functions."

**Use it when:** you know what the program must do, but not how to split it into parts.

**A good answer:** a module of rules with no `input()` and no `print()`, and a separate file for the conversation with the user.

**Check it:** for each planned function, ask "can a test call this without a person typing?" If the answer is no, ask for a split.

## Write: Compare your method with the AI's

**Prompt:** "Write a Python method complete(self, number) for a TaskList class that keeps tasks in self.tasks. The user counts tasks from 1. Raise ValueError when there is no task with that number. Show only the method."

**Use it when:** you have written a method yourself and want a second version to compare with.

**A good answer:** a short method that checks the number and marks the task at position `number - 1`.

**Check it:** run both versions on the same small list, and complete task 1. The first task must be the one marked.

## Generate: Code that must pass your tests

**Prompt:** "Here are my tests: <paste the test file>. Write save_tasks(path, task_list) and load_tasks(path) for my Task data class and TaskList class. Use only the standard library."

**Use it when:** your tests describe what the code must do, and you want help writing it.

**A good answer:** two short functions that pass every test, with no changes to the tests.

**Check it:** run every test. If the AI says the code passes, that is a claim, not a result.

## Test: Ask for cases, then compare with your criteria

**Prompt:** "List test cases for load_tasks(path), with the expected result for each. Include unusual files."

**Use it when:** you want to find cases you have not thought of.

**A good answer:** a normal file, a missing file, an empty file and a broken file, each with an expected result.

**Check it:** compare each expected result with your acceptance criteria. Where the AI and your criteria disagree, your criteria win, and a test should prove it.

## Debug: The cause before the fix

**Prompt:** "This test fails: <paste the test>. This is the error: <paste the full error>. Here is my code: <paste the function>. Explain the cause first. Then show the smallest fix."

**Use it when:** a test fails and you do not know why.

**A good answer:** one cause that matches the last line of the error, and a fix that changes only a few lines.

**Check it:** apply the fix, then run every test, not only the one that failed.

## Improve: A review that keeps the behaviour

**Prompt:** "Review my module: <paste the code>. Suggest one change that makes it shorter or clearer. Do not change what it does."

**Use it when:** your tests pass and you want cleaner code.

**A good answer:** one small change, with a reason, that keeps every check.

**Check it:** run every test on the changed code. A suggestion that removes a check, or that makes a test fail, changes what the code does. Keep your version.
