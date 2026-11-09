# AI Prompt Cards: Chapter 6

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: List the conditions and the boundary values

**Prompt:** "I am a beginner learning Python if, elif and else. My program must follow this rule: <describe the rule in words, for example: a free biscuit when the amount to pay is 15 or more, and a free cake when it is 50 or more>. Do not write code yet. List each condition in plain words, the order in which the program should check them, and the boundary values I should test, with the result each one should give."

**Use it when:** you know the rule in words but not how many conditions you need or in which order.

**A good answer:** one line per condition, the biggest or most specific condition first, and boundary values such as 14.99, 15, 49.99 and 50, each with its expected result.

**Check it:** each boundary value sits exactly where the result changes. The order must make every condition reachable: a smaller amount checked first would hide a bigger one.

## Write: Check your own condition at the boundary

**Prompt:** "Here is a condition I wrote: <paste your if line, for example: if to_pay >= 15:>. Do not change it. Tell me whether the block runs when the value is exactly <the boundary value>, and explain which comparison operator decides it."

**Use it when:** you wrote a condition yourself and want to check that the boundary value goes the right way.

**A good answer:** a clear yes or no for the boundary value, and the meaning of the operator, such as "`>=` includes 15, `>` does not".

**Check it:** set the variable to the boundary value and run the code. The real output must match the explanation.

## Generate: Ask for an exact rule and one exact output

**Prompt:** "Write a short Python if block for a beginner. Use only variables, comparison operators, if, elif, else and print(). Rule: <the rule, with the exact numbers>. Use the variable name <name>. Then tell me exactly what it prints when <name> is <a boundary value>."

**Use it when:** you want a model answer for a rule, or you are not sure how to start.

**A good answer:** short code with one comparison per rule, the operator that matches the words ("15 or more" is `>=`), and a prediction for the boundary value.

**Check it:** run the code with the boundary value. Compare the real output with the AI's prediction, character by character.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error message>. First explain what the error means and which line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** you get a `SyntaxError` or an `IndentationError` near an `if` line and do not understand it.

**A good answer:** it names the line and the cause, such as a single `=`, a missing colon or a block that is not indented, before it shows a one-line fix.

**Check it:** apply the fix and run the program. Read the original error again and confirm that the explanation matches its last line.

## Test: Ask for edge cases

**Prompt:** "Here is my program: <paste the code>. List the edge cases that could break its conditions: boundary values, zero, negative numbers and text answers with capital letters or spaces. For each one, give the value to type and the exact output the program should print."

**Use it when:** your program works for one normal answer and you want to know where it could fail.

**A good answer:** a short list with the boundary value itself, a value slightly below it, zero, and text answers such as `Yes` and ` yes `, each with an expected output.

**Check it:** run the program once for each edge case. Mark each one as passed or failed. A failed case shows you which condition to fix.

## Improve: Ask for clearer conditions, then retest

**Prompt:** "Review the if, elif and else blocks in my program for readability. Suggest at most two improvements, each with one reason. Do not change what the program prints for any input: <paste your code>."

**Use it when:** your conditions work but are hard to read, or you repeat the same check.

**A good answer:** small changes such as a clearer variable name or one combined condition with `and`, each with a reason.

**Check it:** run every edge case from your test list again after each change. If any output changes, the suggestion changed the program's behaviour, so do not accept it.
