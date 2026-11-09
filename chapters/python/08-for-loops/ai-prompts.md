# AI Prompt Cards: Chapter 8

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: Choose the loop before you write it

**Prompt:** "I am a beginner learning Python for loops. My program must repeat this: <describe it, for example: print a line for each of 10 stamps on a loyalty card>. Do not write code yet. Tell me whether a for loop or a while loop fits better and why. If it is a for loop, tell me the exact range() and the first and last value it gives."

**Use it when:** you know what should repeat and want to pick the right kind of loop.

**A good answer:** one loop type with a reason (a known number of passes means `for`), one `range()` and its first and last value.

**Check it:** write out the values of the `range()` yourself. The last value is the stop value minus the step. If the AI's last value includes the stop value, the plan is wrong.

## Write: Ask for the values your loop takes

**Prompt:** "Here is a loop I wrote: <paste your code>. Do not change it and do not run it. List every value the loop variable takes, in order, and say how many passes there are."

**Use it when:** you wrote a `for` loop yourself and want to check its first pass, its last pass and the number of passes.

**A good answer:** the full list of values in order, and a count that matches the list.

**Check it:** write your own list first. Then run the code and count the lines of output. All three must agree.

## Generate: Ask for a for version with the exact output

**Prompt:** "Here is my loop: <paste your code>. Rewrite it with a for loop and range(). Keep my variable names and my messages. Show the exact output, every line."

**Use it when:** you have a working `while` loop with a counter and want a shorter `for` loop that does the same job.

**A good answer:** a `for` loop with one `range()` and no counter line, and an output with exactly as many lines as your version.

**Check it:** run both loops and compare the outputs line by line. Count the lines and read the last line first: off-by-one errors hide there.

## Test: Ask for checks with expected results

**Prompt:** "Here is my loop and its job: <paste code and job>. List 4 checks for its output, such as the first line, the last line, the number of lines and one special line. For each check, give the exact expected result."

**Use it when:** your loop runs and you want to be sure it does the whole job.

**A good answer:** four short checks, each with an exact expected line or count.

**Check it:** run the code and mark each check as passed or failed. After any fix, run every check again, not only the one that failed.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I typed: <the answers, if any>. I got this exact error: <paste the full error message>. First explain what the error means and which line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** your loop stops with a `TypeError`, `NameError` or `SyntaxError` and you do not understand why.

**A good answer:** it names the error type, points to the line and the value that caused it, and explains the cause before it shows a one-line fix.

**Check it:** apply the fix and run the program with the same answers. Then read the original error again and confirm that the explanation matches it.

## Improve: Ask which loop is clearer

**Prompt:** "Here are two loops that should do the same job: <paste loop A> and <paste loop B>. Which one is easier for a beginner to read, and why? Suggest at most one change to make it clearer. Do not change what it prints."

**Use it when:** you have two working versions and must choose one to keep.

**A good answer:** one choice with reasons a reader can check, such as "the range shows the real stamp numbers", and at most one small change.

**Check it:** run both versions and compare the outputs line by line. A suggestion that changes the output, even one word, breaks the instruction: reject that part.
