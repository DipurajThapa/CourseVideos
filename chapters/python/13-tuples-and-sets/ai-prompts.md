# AI Prompt Cards: Chapter 13

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: Ask for a comparison with trade-offs

**Prompt:** "I am a beginner learning Python collections. My job is: <describe it, for example: remember which customers I have already welcomed today, in the order they arrive>. Do not write code yet. Compare a list, a tuple, a set and a dictionary for this job. Give one strength and one weakness for each. Do not choose for me."

**Use it when:** you know what data you have, but not which collection fits the job.

**A good answer:** all four collections, each with a strength and a weakness that are about your job, not about collections in general.

**Check it:** for each weakness, ask yourself whether it matters for your job. Then choose, and write one sentence on why. If the AI chose for you anyway, ask it to compare again.

## Write: Ask for a worked example of one line

**Prompt:** "Here is a line from my code: <paste the line, for example: seen = set(today)>. My data is <paste it>. Explain what the line does, step by step, with my data as a worked example. Show the values before and after. Do not change my code."

**Use it when:** you wrote a line with a tuple or a set yourself and want to be sure what it does.

**A good answer:** each part of the line explained in order, with your real values, and the result after the line runs.

**Check it:** add `print()` after the line, run it, and compare with the AI's worked example. For a set, compare `sorted(...)`, because a set has no fixed order.

## Generate: Ask for code with the exact output

**Prompt:** "Here is my data: <paste it>. Write a few lines of Python that <describe the job>. Use only lists, tuples, sets, dictionaries, loops, if and f-strings. Use these names: <list them>. Show the exact output, every line."

**Use it when:** you want a model answer for a task with tuples or sets.

**A good answer:** short code that uses your names, makes an empty set with `set()`, and prints sets with `sorted()` so the output is the same every time.

**Check it:** run the code and compare every line with the output the AI promised. Look closely at any empty `{}`: it makes a dictionary, not a set.

## Test: Ask for cases, including an empty one

**Prompt:** "Here is my program: <paste the code>. List three or four test cases with the exact expected output for each. Include an empty list and a name typed with a different capital letter or extra spaces. Do not change my code."

**Use it when:** your program works for one example and you want to know what breaks it.

**A good answer:** each case with its data and its exact expected output, including the empty case.

**Check it:** run every case and write pass or fail for each. When you fix a failure, run every case again.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error report>. First explain what the error means and which line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** you get an error such as `'tuple' object does not support item assignment`, `'set' object is not subscriptable` or `too many values to unpack`.

**A good answer:** it explains the words in the error, points to the line, and gives the cause before a one-line fix.

**Check it:** apply the fix and run the program again, then run all your test cases.

## Improve: Ask for a shorter version that prints the same

**Prompt:** "Here is my working program: <paste the code>. Suggest one change that makes it shorter. The output must stay exactly the same for every test case. Explain the change in one sentence."

**Use it when:** your program works and you want cleaner code.

**A good answer:** one small change, a reason, and a promise that the output stays the same.

**Check it:** run the old and the new version with every test case and compare every line. If any line changes, keep your version.
