# AI Prompt Cards: Chapter 16

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: Write the specification first

**Prompt:** "I am a beginner learning Python functions. I want a function for this job: <describe the job in words>. Do not write code yet. Write a specification: the function's name, each parameter with its type, what it returns, and three examples of a call with the exact value it returns."

**Use it when:** you know what you want a function to do, but not yet its name, inputs and output.

**A good answer:** a clear name in snake_case, parameters in a sensible order, a sentence on the return value, and three examples with exact results, including one unusual case.

**Check it:** work out each example by hand or with a calculator. If one example is wrong, the specification is wrong, and so will be any code built from it.

## Write: Write your own checks

**Prompt:** "Here is my function specification: <paste it>. I wrote these check lines myself: <paste them>. Do not write the function. Predict what each check line prints if the function follows the specification exactly."

**Use it when:** you want test lines ready before any function exists.

**A good answer:** one predicted line for each check, such as `11.0 True`, with the value and the comparison result.

**Check it:** each check should compare the returned value with the exact value from the specification. Later, run the checks on any function, yours or the AI's.

## Generate: Ask for the function from the specification

**Prompt:** "Write a Python function from this specification: <paste the specification>. It must return the value, not print it. Use only what a beginner knows: variables, if, loops, lists and dictionaries. Then tell me exactly what each of my example calls returns."

**Use it when:** you have a clear specification and want a first version.

**A good answer:** a short function with a docstring, a `return` line, the parameters in the order of the specification and the exact results of the examples.

**Check it:** run your own check lines on its function. Look for `print()` where `return` should be, a missing `round()` and parameters in a different order.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this full error: <paste the full error report>. First explain what the error means and which line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** a call to your function stops with a `TypeError`, a `NameError` or another error.

**A good answer:** it reads the last line of the report, names the function and the call, and explains the cause before a one-line fix.

**Check it:** apply the fix and run every check line again, not only the one that failed.

## Test: Run your checks on every version

**Prompt:** "Here is a function: <paste it>. Here are my check lines with the expected values: <paste them>. Which checks will fail, and why? Then suggest two more checks, including one unusual case."

**Use it when:** you have a function and want to know if it really follows the specification.

**A good answer:** a list of the failing checks with a reason for each, and new checks with exact expected values.

**Check it:** run the checks yourself. The AI can be wrong about which checks fail. The printed `True` and `False` decide.

## Improve: Keep the calls working

**Prompt:** "Review this function for readability: <paste it>. Suggest at most two improvements, each with a one-sentence reason. Do not change the function's name, its parameters or what it returns."

**Use it when:** your function works and passes every check.

**A good answer:** small, explained changes, such as a clearer docstring or a better variable name, that keep every call the same.

**Check it:** apply one suggestion at a time and run every check line after each change. If a check fails, the suggestion broke your rule.
