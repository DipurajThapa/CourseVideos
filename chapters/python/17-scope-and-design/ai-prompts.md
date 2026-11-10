# AI Prompt Cards: Chapter 17

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: List the jobs a function does

**Prompt:** "I am a beginner learning Python functions. Here is one of my functions: <paste it>. Do not write code yet. List every separate job this function does, one per line, and name the line numbers for each job. Then tell me which jobs read or change something outside the function."

**Use it when:** a function has grown long and you are not sure how to split it.

**A good answer:** a short list such as "adds tax (lines 6 to 8), prints a line (line 9), changes the week total (line 10)", with any global variable named.

**Check it:** read each line of your function and tick it against the list. Every line belongs to exactly one job. A line the AI did not mention is a job it missed.

## Write: Save the target output first

**Prompt:** "Here is my program: <paste it>. I will run it and save its exact output before I change anything. Predict that output, line by line, including spaces."

**Use it when:** you are about to change working code and want a fixed target to compare against.

**A good answer:** one predicted line for every `print()`, with the same spacing and the same number of decimal places as your format strings.

**Check it:** run the program and save the real output. The real output is your target, not the AI's prediction. If they differ, find out why before you go on.

## Generate: Ask for a split with rules

**Prompt:** "Split this function into small functions that each do one job: <paste the code>. Rules: use no global variables, pass values in as parameters, return results instead of printing them, and keep the program's output exactly the same. Show the full new program."

**Use it when:** you know the jobs and want a first version of the split.

**A good answer:** two or three short functions with clear names, each ending with `return`, and the printing done only in the main code.

**Check it:** run the new program and compare every line with your saved output. Look for extra lines such as `None`, which mean a function prints instead of returning.

## Test: Ask for test cases with expected lines

**Prompt:** "Here are my new functions: <paste them>. Suggest three test cases for <function name>: a normal day, an empty day and a day with one sale. For each one, give the arguments and the exact expected result."

**Use it when:** the split works for your example and you want to know if it works for others.

**A good answer:** three calls with exact expected values or lines, including the empty case.

**Check it:** work out each expected result yourself or with the original program. Put the cases in a list and print pass or FAIL for each. Run the tests again after every change.

## Debug: The cause, and a fix that keeps your rules

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error>. First explain the cause and the line. Then show the smallest fix that uses no global variables."

**Use it when:** you get a `NameError` or an `UnboundLocalError` after moving code into a function.

**A good answer:** it names the variable and explains whether Python treats it as local or global, then passes the value in and returns the result.

**Check it:** if the fix uses the `global` keyword, ask again for one without it. Run the fix and compare the output with your saved target.

## Improve: One suggestion, tested twice

**Prompt:** "Review my functions for readability: <paste them>. Suggest at most two improvements, each with one reason. Keep the function names, the parameters and the output the same."

**Use it when:** your split works and passes every test.

**A good answer:** small, specific changes with a reason, such as a clearer name or a default argument for a value most calls use.

**Check it:** apply one suggestion at a time and run every test again. If a suggestion adds a default value that is a list, test it with two separate calls: two days, or two customers, must not share one list.
