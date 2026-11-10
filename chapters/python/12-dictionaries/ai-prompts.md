# AI Prompt Cards: Chapter 12

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: Ask for a data design, then challenge it

**Prompt:** "I am a beginner learning Python dictionaries. I need to store <describe the data, for example: how many cakes, scones and sandwiches are left>. I will use it to <describe the job, for example: find one item by its name and take one away when it sells>. Do not write code yet. Suggest a data structure and explain why it fits this job. Then give one reason it might not fit."

**Use it when:** you know what data you have but not how to store it.

**A good answer:** one structure, such as a dictionary with item names as keys, a reason linked to your job, and an honest weakness.

**Check it:** ask yourself how you would find one item by its name with that structure. If you must search through a list first, ask the AI why it did not use a dictionary.

## Write: Ask for a worked example of one line

**Prompt:** "Here is a line from my code: <paste the line, for example: counts[item] = counts.get(item, 0) + 1>. My dictionary is <paste it>. Explain what the line does, step by step, with a worked example that shows the dictionary before and after. Do not change my code."

**Use it when:** you wrote a dictionary line yourself and want to be sure what it does.

**A good answer:** each part of the line explained in order, with the real values from your dictionary and the dictionary before and after.

**Check it:** add `print()` before and after the line, run it, and compare with the AI's worked example.

## Generate: Ask for code with the exact output

**Prompt:** "Here is my dictionary: <paste it>. Write a few lines of Python that <describe the job>. Use only dictionaries, lists, loops, if and f-strings. Show the exact output, every line."

**Use it when:** you want a model answer for a dictionary task.

**A good answer:** short code that uses your dictionary and your names, with an output that matches the code line by line.

**Check it:** run the code and compare every line with the output the AI promised. A loop over a dictionary gives keys, so check whether the output shows names or values.

## Test: Ask for cases, including a missing key

**Prompt:** "Here is my program: <paste the code>. List four test cases with the exact expected output for each. Include an empty case, a case that reaches zero, and a key that is not in the dictionary. Do not change my code."

**Use it when:** your program works for one example and you want to know what breaks it.

**A good answer:** four cases with the expected output for each, including one that may stop the program with a `KeyError`.

**Check it:** run every case. Write pass or fail for each. When you fix a failure, run every case again.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error report>. First explain what the error means and which line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** you get a `KeyError` or a `TypeError` with `NoneType` and do not understand it.

**A good answer:** it names the missing key or the `None` value, points to the line, and explains the cause before a fix such as `in` or `get()`.

**Check it:** apply the fix and run the program with the input that failed, then with all your other test cases.

## Improve: Ask for a clearer version that prints the same

**Prompt:** "Here is my working program: <paste the code>. Suggest one change that makes it shorter or clearer. The output must stay exactly the same for every test case. Explain the change in one sentence."

**Use it when:** your program works and you want cleaner code.

**A good answer:** one small change, a reason, and a promise that the output stays the same.

**Check it:** run the old and the new version with every test case and compare every line. If any line changes, keep your version.
