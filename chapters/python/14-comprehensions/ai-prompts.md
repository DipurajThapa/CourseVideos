# AI Prompt Cards: Chapter 14

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: List what must stay the same

**Prompt:** "I am a beginner learning Python comprehensions. I want to rewrite this loop as one line: <paste the loop>. Do not write code yet. List everything the new line must keep exactly the same: which items it keeps, their order, how it rounds, and the type of the result."

**Use it when:** you are about to refactor a loop and want a checklist before any code changes.

**A good answer:** a short list that names the filter, the order of the items, the rounding and whether the result is a list or a dictionary.

**Check it:** read your loop line by line. Every `if`, every `round()` and the empty list at the start should appear somewhere in the list. If one is missing, add it yourself.

## Write: Write the loop, then ask for a prediction

**Prompt:** "Here is a loop I wrote: <paste the code>. Do not change it and do not run it. Predict its exact output, and explain in one sentence what each line does."

**Use it when:** you wrote a loop yourself and want to be sure you understand it before you rewrite it.

**A good answer:** the exact printed list, with the right number of items and the right decimal places, and one plain sentence per line.

**Check it:** write your own prediction first, then run the code. Compare all three: your prediction, the AI's prediction and the real output.

## Generate: Ask for the comprehension and its output

**Prompt:** "Rewrite this loop as a list comprehension: <paste the loop>. Keep the output exactly the same. Use my names. Show the new line and tell me exactly what it prints."

**Use it when:** you want to see your own loop written as one line.

**A good answer:** one comprehension that uses your names and keeps every part of the loop: the new value, the loop, and any filter at the end.

**Check it:** run the new line and compare its output with your loop's output, item by item. A missing `if` at the end is the most common slip.

## Test: Ask for cases, then run both versions

**Prompt:** "Here is my loop: <paste it>. Here is the comprehension that should replace it: <paste it>. List three test cases with the expected result for each: a normal case, a case where no item passes the filter, and a case with two equal values. Do not change my code."

**Use it when:** your comprehension works on one example and you want proof that it matches the loop.

**A good answer:** three cases, each with its data and the exact list the loop gives.

**Check it:** run your loop and the comprehension on every case and print `pass` or `FAIL` for each. When you fix a failure, run every case again.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error report>. First explain what the error means and which part of the line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** you get an error such as `expected 'else' after 'if' expression` or `invalid syntax` inside a comprehension.

**A good answer:** it explains where the `if` belongs: at the end to filter, or at the start with an `else` to choose a value for every item.

**Check it:** apply the fix, run the program, then run all your test cases again.

## Improve: Ask for a better version that prints the same

**Prompt:** "Here is my working comprehension: <paste it>. Suggest one change that makes it clearer or faster. The output must stay exactly the same for every test case. Explain the change in one sentence."

**Use it when:** your comprehension works and you want a second opinion.

**A good answer:** one small change, a reason, and code whose output is still the same list.

**Check it:** run every test case with the new version. If any line of output changes, such as square brackets becoming curly brackets, keep your version.
