# AI Prompt Cards: Chapter 25

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data, such as customer names or card numbers from a till file. Always run the code yourself. Your tests and your real files decide who is right, not the AI.

## Plan: Functions and error handling before code

**Prompt:** "I am a beginner. I know files, CSV, JSON, try and except, functions and pytest. I want <describe the program, for example: a weekly report from a folder of till CSV files with the columns item and amount>. Some rows are damaged. Do not write code. Plan the functions, and say how to handle errors."

**Use it when:** you know what the program must do, but not how to split it or which errors to expect.

**A good answer:** small functions with one job each, and a list of the errors that can happen, each with its own exception.

**Check it:** reject any plan with one big `try` around everything, or `except Exception`. Ask "which line can fail, and which exception does it raise?" for each `try`.

## Write: Compare your function with the AI's

**Prompt:** "Write a Python function parse_amount(text) that turns a price such as '3.50' into a float, and raises ValueError for a word or a negative price. Show only the function."

**Use it when:** you have written a function yourself and want a second version to compare with.

**A good answer:** a short function that calls `float()`, checks for a negative number and raises a `ValueError` with a message.

**Check it:** run both versions on the same texts, including a word and a negative price. Every result must be the same.

## Generate: Code that must pass your tests

**Prompt:** "Here are my tests: <paste the test file>. Write read_sales(path), which returns the good sales in a CSV file and the number of bad rows, and build_week(folder), which adds up every CSV file in a folder. Use only the standard library."

**Use it when:** your tests describe what the code must do, and you want help writing it.

**A good answer:** code that uses the exact column names from your files and catches only the exceptions a damaged row can cause.

**Check it:** run your tests. Then count good and bad rows in each file. If every row is bad, look for a wrong key hidden by a broad `except`.

## Test: Realistic test data

**Prompt:** "Give me a small CSV file of test data for my report. My real files start with this line: <paste the first line of a real file>. Include two damaged rows and one empty file. Say what result you expect for each."

**Use it when:** you want data that tries to break your program before real data does.

**A good answer:** files with the same columns as yours, a few damaged rows and the expected result for each.

**Check it:** compare the first line of the AI's file with a real file, character by character. Run your program on it, and keep any file that finds a problem as a test.

## Debug: The cause before the fix

**Prompt:** "I am a beginner. My report crashed with this error: <paste the full error report>. Here is the function: <paste it>. First explain the cause and which line raised it. Then show the smallest fix."

**Use it when:** your program stops with a traceback you do not understand.

**A good answer:** the cause in one or two sentences, the exact line from the last `File` line, and a fix of one or two lines.

**Check it:** apply the fix, run the failing case again, then run every test again.

## Improve: Review the error handling

**Prompt:** "Review my module for error handling and clarity. Suggest one improvement. Do not change what the totals are: <paste the module>."

**Use it when:** your program works and your tests pass.

**A good answer:** one clear suggestion with a reason, such as a clearer message or a smaller `try` block.

**Check it:** apply the suggestion to a copy and run every test. If a total changes, the suggestion broke your rule, so reject it.
