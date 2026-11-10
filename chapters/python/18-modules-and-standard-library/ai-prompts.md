# AI Prompt Cards: Chapter 18

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The official documentation and the real output decide who is right, not the AI.

## Plan: Find the right module first

**Prompt:** "I am a beginner learning Python modules. I need to <describe the task, for example: round a number up to the next whole number>. Do not write a program yet. Which module from Python's standard library fits, and which function in it? Give the exact module and function names, and one example call with its result."

**Use it when:** you know what you want to do but not which ready-made tool does it.

**A good answer:** one module and one function, such as the `math` module and `math.ceil()`, with an example like `math.ceil(3.2)` giving `4`.

**Check it:** open docs.python.org and find the module's page. Search the page for the function name. Read its one-line description and compare it with the AI's claim. If you cannot find the function, do not use it.

## Write: Write your own version first

**Prompt:** "Here is a function I wrote myself without any module: <paste it>. Here is a version that uses <module function>: <paste it>. Do not change them. Will they give the same result for every input? If not, give me one input where they differ."

**Use it when:** you have your own solution and want to know whether the module's version behaves the same.

**A good answer:** a clear yes or no, and when the answer is no, a specific input where the two results differ.

**Check it:** run both versions on several inputs, including a number that divides exactly and a small number such as 1. The real output decides, even when the AI says "always the same".

## Generate: Ask for a function for your module

**Prompt:** "Write one Python function for my module `<module name>.py`. Name: `<function name>`. Parameters: <list them, with defaults>. It returns <describe the result>. Use only the standard library, and put any import at the top of the file. Add a one-line docstring. Then tell me exactly what `<example call>` returns."

**Use it when:** you know what the function must do and want a short, documented version.

**A good answer:** a short function with a docstring, the import line it needs, and a prediction for your example call.

**Check it:** run the example call. Then run your own test cases. Check that every module function it uses exists in the official documentation.

## Test: Cases before and after every fix

**Prompt:** "Here is my function: <paste it>. Here are my test cases as input and expected result: <list them>. Add any case I missed, such as zero, one, or a number that divides exactly. Do not change my function."

**Use it when:** you want to know whether a function from an AI, or your own, really does what you need.

**A good answer:** your cases plus one or two edge cases, each with an expected result you can work out by hand.

**Check it:** put the cases in a loop that prints `pass` or `FAIL` for each one. Run it before a fix, and run all of it again after every fix.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error report>. First explain what the error means and which line causes it. Then show the smallest fix."

**Use it when:** you get a `ModuleNotFoundError`, an `AttributeError` or a `NameError` after an import.

**A good answer:** it names the error, the line and the missing or misspelled name, and explains the cause before the fix, for example a missing `import math` line.

**Check it:** apply the fix and run every test case again. If the AI names a function, find it in the documentation before you run the fix.

## Improve: Check every name it suggests

**Prompt:** "Review this module for readability: <paste it>. Suggest at most two improvements, each with a one-sentence reason. Do not change what any function returns. For every standard library function you mention, give the module page where I can find it."

**Use it when:** your module works and you want it clearer or shorter.

**A good answer:** one or two small, specific changes, each with a reason and the name of a real module page.

**Check it:** search the module's documentation for each function the AI names. If it is not there, reject the suggestion. If it is, make the change and run all your test cases again.
