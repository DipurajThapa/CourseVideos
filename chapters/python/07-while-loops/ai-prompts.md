# AI Prompt Cards: Chapter 7

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: Describe the repeat rule before you write a loop

**Prompt:** "I am a beginner learning Python while loops. My program must repeat this: <describe it in words, for example: ask for the number of teas until the answer is from 1 to 10>. Do not write code yet. Tell me the loop condition in plain words, which variable must change inside the loop, what makes the loop stop, and three sets of test answers with the expected result for each."

**Use it when:** you know what should repeat but not how the loop should stop.

**A good answer:** one condition in plain words, the name of the value that changes on every pass, the stop rule, and test answers such as a valid first answer, one wrong answer and then a valid one, and boundary values.

**Check it:** the value in the condition must be changed by a line inside the loop. If the plan does not say which line changes it, ask again.

## Write: Ask for a trace of your own loop

**Prompt:** "Here is a loop I wrote: <paste your code>. Do not change it. Trace it for these answers: <the answers, for example: 0, then 12, then 3>. Show a table with one row per pass: the values at the check, whether the condition is True or False, and what the pass prints."

**Use it when:** you wrote a loop yourself and want to see each pass before you run it.

**A good answer:** one row per pass, a last row where the condition is `False`, and printed lines that match the questions and messages in your code.

**Check it:** write your own trace first, then run the code with the same answers. All three must agree. Where they differ, find out why.

## Generate: Ask for a change and one exact output

**Prompt:** "Here is my loop: <paste your code>. Add this change: <the change, for example: at most 3 tries, then print 'Too many tries. Using 1 tea.'>. Keep my variable names and my messages. Then tell me exactly what the program prints for these answers: <the answers>."

**Use it when:** you want to extend a working loop with a new rule.

**A good answer:** short code that keeps your lines, adds only what the change needs, and a predicted output with every question and message in order.

**Check it:** run the code with the same answers and compare every line, including the number of questions. Check that every value in the loop condition is changed by a line inside the loop.

## Test: Ask for edge cases and run every one

**Prompt:** "Here is my loop: <paste your code>. List 4 edge cases for it, such as a valid first answer, a boundary value and the most wrong answers allowed. For each one, give the answers to type and the exact expected output."

**Use it when:** your loop works for one set of answers and you want to know if it works for others.

**A good answer:** four sets of answers, each with an expected output that counts the questions exactly.

**Check it:** run every case. Mark each one as passed or failed. A failed case is a bug in the code or in the expected output: find out which.

## Debug: Ask for a trace before a fix

**Prompt:** "I am a beginner. My loop does not stop when it should. Here is the code: <paste the code>. Here is a run that went wrong: <paste the full output, or the full error message>. First trace the loop in a table for these answers, one row per pass. Then tell me which value never changes, and show the smallest fix."

**Use it when:** a loop asks too many times, never ends, or stops too early.

**A good answer:** a trace table that shows the value that stays the same, the reason in one sentence, and a one-line fix inside the loop.

**Check it:** apply the fix and run the same answers again. The number of passes must now match the rule.

## Improve: Ask for a clearer loop, then count the passes

**Prompt:** "Review my loop for readability: <paste your code>. Suggest at most two changes, each with one reason. Do not change how many times it asks or what it prints."

**Use it when:** your loop works and you want it easier to read.

**A good answer:** small changes, such as a clearer name or a simpler condition, each with a reason, and no change to the behaviour.

**Check it:** run the new version with the same test answers. Count the questions in the output. A change from `<` to `<=` in a condition often adds one extra pass.
