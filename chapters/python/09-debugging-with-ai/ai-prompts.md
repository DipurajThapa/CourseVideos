# AI Prompt Cards: Chapter 9

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: Ask for a plan to find the bug

**Prompt:** "I am a beginner learning Python. My program <describe what goes wrong, for example: crashes when I type 0 sales>. Do not fix anything yet and do not write code. Give me a short plan to find the cause, step by step, using the error message and print debugging."

**Use it when:** something is wrong and you do not know where to start.

**A good answer:** a short list of steps you can do yourself, such as reading the last line of the traceback, finding the line number, checking the values on that line and testing again.

**Check it:** follow the plan yourself. Each step should tell you something new. If a step only says "rewrite the program", the plan is not a debugging plan.

## Write: Read the traceback yourself, then check your reading

**Prompt:** "Here is my code: <paste the code>. Here is the full error: <paste the traceback>. My reading: the kind of error is <kind>, it happened on line <number>, and I think the cause is <your idea>. Do not fix the code. Tell me if my reading is right, and correct only what is wrong."

**Use it when:** you want to learn to read tracebacks, not only to get a fix.

**A good answer:** it confirms or corrects each of your three points: the kind of error, the line and the cause.

**Check it:** find the line number in your editor and look at the part the `^` or `~` markers point at. The AI's explanation must match that part of the line.

## Generate: Ask for a fix with an exact output

**Prompt:** "Here is my program: <paste the code>. Change only what is needed to <describe the change, for example: print No sales today. when the number of sales is 0>. Keep everything else the same. Show the full program and tell me exactly what it prints for <the input you will test>."

**Use it when:** you know what the program should do and want a small, checkable change.

**A good answer:** a short change in one place, and an exact predicted output for your input.

**Check it:** run the code with the same input and compare every line with the AI's prediction. A crash or a different line means the AI was wrong, however sure it sounded.

## Test: Ask for test cases with expected results

**Prompt:** "Here is my program: <paste the code>. List four test cases. For each one, give the exact input and the exact output you expect. Include an edge case, a case at the boundary of a condition and the case that failed before: <describe it>."

**Use it when:** you have fixed a bug and want to be sure the fix works and nothing else broke.

**A good answer:** a numbered list of cases, each with its input and expected output, including the unusual ones such as 0 or 1.

**Check it:** work out each expected output by hand before you trust it. Then run every case and mark it as pass or fail. A **regression** is a bug that a fix brings back or creates elsewhere, so run the old cases too.

## Debug: The structured debugging prompt

**Prompt:** "I am a beginner. Code: <paste the code>. Exact error: <paste the full traceback, or write: no error message>. Expected result: <what you wanted>. Actual result: <what it printed>. First explain the cause and the line. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** you have a bug of any kind, and especially a logic error with no error message.

**A good answer:** it names the line and the cause, connects the cause to the difference between the expected and actual results, and changes as little as possible.

**Check it:** apply the fix, run the program with the same input, and compare with your expected result. Then run the cases that already worked.

## Improve: Ask how to make future bugs easier to find

**Prompt:** "Here is my working program: <paste the code>. Suggest at most two changes that make future bugs easier to find, each with one reason. Do not change what the program prints."

**Use it when:** your program works and you want it to be easier to debug next time.

**A good answer:** small changes such as clearer variable names, each with a reason, and no change to the output.

**Check it:** run the program before and after each change with the same input. The output must stay exactly the same. If a suggestion adds extra lines to the output, it breaks your instruction, so leave it out.
