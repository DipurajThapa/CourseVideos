# AI Prompt Cards: Chapter 2

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: List the variables before you write code

**Prompt:** "I am a beginner learning Python variables. I want a program that calculates <describe the calculation, for example: the cost of 3 notebooks at 2.50 each and 4 pens at 1.25 each>. Do not write code yet. List the variables I need. For each one, give a clear snake_case name, its type (int, float, str or bool) and its starting value."

**Use it when:** you understand the problem but do not know which values to store.

**A good answer:** a short list of names such as `notebook_price`, each with a type and a value, plus the results you will calculate from them.

**Check it:** every number in your description appears in the list once. Each type fits its value: prices with a decimal point are `float`, counts are `int`.

## Write: Predict first, then run

**Prompt:** "Here is my Python code: <paste your code>. Do not change it and do not run it. Predict the exact output, line by line. For each line, explain in one sentence how Python calculated it."

**Use it when:** you have written a program and want to test your own understanding.

**A good answer:** one predicted line for each `print()`, with the value and its type shown correctly, for example `7.0` and not `7` when a `float` is involved.

**Check it:** write your own prediction first. Then run the code. Compare all three: your prediction, the AI's prediction and the real output. Where they differ, find out why.

## Generate: Ask for code with fixed names and an exact output

**Prompt:** "Write a short Python program for a beginner. Use only variables, arithmetic operators and print(). Use these variable names: <list the names>. It must print exactly: <paste the exact output>. Show the code, then show the output it prints."

**Use it when:** you want a model answer to learn from, or you are stuck on how to start.

**A good answer:** short code that uses your names, one calculation per line and no features you have not learned yet.

**Check it:** run the code and compare every character with your target output. Look for `7` against `7.0`, and for missing brackets in calculations.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error message>. First explain what the error means and which line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** you get a `NameError`, `TypeError` or `SyntaxError` and do not understand it.

**A good answer:** it names the error type, points to the exact line and name, and explains the cause before it shows a one-line fix.

**Check it:** apply the fix and run the program. Then read the original error again and confirm that the explanation matches it.

## Test: Try new values and predict each result

**Prompt:** "Here is my program: <paste the code>. Suggest three sets of starting values to test it: one normal case, one with zero and one with decimal numbers. For each set, tell me which output you expect."

**Use it when:** your program works with one set of values and you want to know if it works with others.

**A good answer:** three sets of values, each with a predicted output, and a note on any value that could cause trouble, such as dividing by zero.

**Check it:** change the values in your code and run it for each set. Mark each AI prediction as right or wrong. Check that each result makes sense: an average must lie between the smallest and largest values.

## Improve: Ask for clearer names

**Prompt:** "Review the variable names in my Python program. Suggest better names only where a name is unclear, too short or does not follow PEP 8. For each suggestion, give one sentence on why it helps a reader. Do not change what the program prints: <paste your code>."

**Use it when:** your program works but you used short names such as `x`, `t` or `p2`.

**A good answer:** a short list of old and new names, such as `t` to `tea_total`, each with a reason.

**Check it:** rename the variables one at a time and run the program after each change. The output must stay exactly the same. A `NameError` means you missed one place where the old name was used.
