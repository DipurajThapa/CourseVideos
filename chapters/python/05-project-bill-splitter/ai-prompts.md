# AI Prompt Cards: Chapter 5

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run and read the code yourself. A test result you worked out by hand decides who is right, not the AI.

## Plan: Inputs, calculations and outputs

**Prompt:** "I am a beginner. I know print, variables, int and float, the operators including // and %, f-strings and input. I want a program that <describe the tool, for example: splits a cafe bill between friends with a tip>. Do not write code. List the inputs with their types, the calculations in order and the outputs."

**Use it when:** you know what the tool should do but not where to start.

**A good answer:** a short list in three parts. Every input has a type, and every calculation uses only values from the lines above it.

**Check it:** work through the plan by hand with one set of numbers. If a step gives an amount that nobody can pay, such as 10.7675, add a step that fixes it.

## Write: Check my conversions

**Prompt:** "I wrote these lines myself: <paste your input lines>. Do not change them. For each answer, tell me which type it becomes and whether that type fits what the user will type."

**Use it when:** you have written the questions and want to know that each answer is ready for calculating.

**A good answer:** one line for each question, naming `float` for amounts with decimals and `int` for counts, with a reason.

**Check it:** run your lines and print `type()` of each answer, as in Step 1 of the project.

## Generate: One calculation with a known result

**Prompt:** "Write the lines that calculate <the calculation, for example: the tip and the total for a bill of 48 with a 10 percent tip>. Use these variable names: <names>. Tell me exactly what they print."

**Use it when:** you want a model for one calculation, not the whole program.

**A good answer:** two or three short lines that use your names, plus a prediction of the output.

**Check it:** work out the result by hand before you run the code. Then run it and compare every digit with your own result, not with the AI's prediction.

## Debug: Explain the error first

**Prompt:** "I am a beginner. My program stopped when I typed <the answers>. Here is the code: <paste it>. Here is the full error: <paste the full error>. First explain what the error means and which line causes it. Then suggest the smallest change I can make with what I know."

**Use it when:** a test answer makes the program stop with an error.

**A good answer:** it names the error and the line, explains the cause in one or two sentences, and does not use features you have not learned yet.

**Check it:** read the last line of the error yourself and confirm the line number. If the suggested fix uses something you have not learned, ask for a fix that uses only what you know.

## Test: Answers with known results

**Prompt:** "Here is my program: <paste it>. Suggest four sets of answers to test it, including a bill with decimals, a tip of zero and one person. For each set, work out the expected output by hand and show the steps."

**Use it when:** your program works with one set of answers and you want to know if it always works.

**A good answer:** four sets of answers, each with its calculation shown, so you can check the AI's arithmetic too.

**Check it:** redo each calculation yourself, then run the program for each set and compare every line. Mark each AI result as right or wrong.

## Improve: A review that keeps the output

**Prompt:** "Review my program for readability. Suggest at most two changes, each with one reason. Do not change what it prints: <paste your program>."

**Use it when:** the program passes all your tests and you want it clearer.

**A good answer:** one or two small changes, each with a reason a beginner can check.

**Check it:** before you accept a change, run your four tests again. If any output line changes, the suggestion is not an improvement, however simple it looks.
