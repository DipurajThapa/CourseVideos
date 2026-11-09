# AI Prompt Cards: Chapter 3

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: Describe the exact line you want

**Prompt:** "I am a beginner learning Python f-strings. I want to print this exact line: <paste the line, for example: Sandwich            6.00>. Do not write code yet. Tell me how many characters each part takes, whether each part is aligned left or right, and which format code shows the number."

**Use it when:** you know what the output should look like but not which widths and codes give it.

**A good answer:** a width for each part, an alignment for each part (`<` or `>`), and `.2f` for a price with two decimal places.

**Check it:** count the characters in your target line yourself. The widths in the answer must add up to the length of the whole line.

## Write: Predict the exact output, spaces included

**Prompt:** "Here is my Python code: <paste your code>. Do not change it and do not run it. Predict the exact output. Show every space as a dot, so I can count them."

**Use it when:** you wrote an f-string with widths and want to check that you understand it.

**A good answer:** one predicted line per `print()`, with dots for spaces and the right number of decimal places.

**Check it:** write your own prediction first, then run the code. Compare all three, character by character.

## Generate: Paste the target output into the prompt

**Prompt:** "Write a short Python program for a beginner. Use only variables, f-strings and print(). Use these variable names: <list the names>. It must print exactly this, character by character: <paste the exact output>. Show the code, then the output it prints."

**Use it when:** you want a model answer to learn from, or you are stuck on a format code.

**A good answer:** an f-string with `f` before the quotation mark, your variable names, and a width and format code for each value.

**Check it:** run the code and compare every character with your target. Look for curly brackets printed as text, which means the `f` is missing.

## Test: Ask for values that could break the layout

**Prompt:** "Here is my program: <paste the code>. Suggest four values to test it: a short name, a name longer than the column, a price with no decimal part and a price with three digits before the point. For each, tell me what you expect the output to look like."

**Use it when:** your layout works for one set of values and you want to know if it works for others.

**A good answer:** four test values, a predicted output for each, and a warning that a width is only a minimum, so long text is not cut.

**Check it:** change the values in your code and run each case. Mark each prediction as right or wrong.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error message>. First explain what the error means and which line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** you get a `TypeError`, `IndexError` or `ValueError` with text and do not understand it.

**A good answer:** it names the error type and the exact line, explains the cause (for example, a number stored as text), and then shows a one-line fix.

**Check it:** apply the fix and run the program. Then read the original error again and confirm that the explanation matches it.

## Improve: Ask for a clearer or shorter version, then test it

**Prompt:** "Review my f-strings for readability. Suggest at most two improvements, each with a one-sentence reason. Do not change what the program prints: <paste your code>."

**Use it when:** your output is correct and you want cleaner code.

**A good answer:** a short list of changes, such as clearer names or one width stored in a variable, each with a reason.

**Check it:** apply one suggestion at a time and run the program after each change, with at least two different values. The output must stay exactly the same.
