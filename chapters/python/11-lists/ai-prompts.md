# AI Prompt Cards: Chapter 11

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: List the steps before the code

**Prompt:** "I am a beginner learning Python lists. I have this list: <paste the list>. I want to <describe the job, for example: print the three biggest sales>. Do not write code yet. List the steps in plain English, and name the list method or function for each step."

**Use it when:** you know what you want from a list but not which methods to use.

**A good answer:** three to five short steps, each with one method or function, such as `sorted()` or a slice, and the order of the steps.

**Check it:** follow the steps by hand with your list on paper. If a step changes the original list and you still need it, the plan is wrong.

## Write: Ask for a worked example of one slice or method

**Prompt:** "Explain what <the slice or method, for example: sales[:3]> does. Use my list <paste the list> as a worked example: show the code and the exact result. Do not change my code."

**Use it when:** you wrote a slice or a method call yourself and want to be sure what it gives.

**A good answer:** a short explanation, the code and the exact result, with the indexes of the items it takes.

**Check it:** run the AI's example. If the result differs from its explanation, trust the run and ask the AI why.

## Generate: Ask for code with the exact output

**Prompt:** "Here is my list: <paste the list>. Write a few lines of Python that <describe the job>. Use only lists, loops, if and f-strings. Show the exact output, every line."

**Use it when:** you want a model answer for a list task.

**A good answer:** short code that keeps your list and your names, and an output you can compare line by line.

**Check it:** run the code. Compare every line with the AI's output. Check one fact by hand, such as the first item of a top list against `max()`.

## Test: Ask for test lists with expected results

**Prompt:** "Here is my code: <paste the code>. Suggest four test lists: a normal one, one with equal values, one shorter than my slice and one empty list. For each, give the expected output."

**Use it when:** your code works for one list and you want to know if it works for others.

**A good answer:** four lists, an expected output for each, and a note on any list that could cause an error.

**Check it:** run each list and mark the AI's expected output as pass or fail. If a test fails, find out whether the code or the expectation is wrong.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error>. First explain what the error means and which line causes it. Then show the smallest fix."

**Use it when:** you get an `IndexError`, a `ValueError` from `remove()` or a `TypeError` that mentions `NoneType`.

**A good answer:** it names the error type, the line and the cause, such as "sort() gives back None", before the fix.

**Check it:** apply the fix and run the program. Read the original error again and confirm the explanation matches it.

## Improve: Ask for a clearer version that prints the same

**Prompt:** "Review my list code for readability. Suggest at most two changes, each with one reason. Do not change what it prints: <paste the code and its output>."

**Use it when:** your code works and you want it easier to read.

**A good answer:** one or two changes, each with a reason, and the same output.

**Check it:** run the new version and compare every line of output with the old one, including the order of the items. A different order is a different output.
