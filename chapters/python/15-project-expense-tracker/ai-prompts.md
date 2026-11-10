# AI Prompt Cards: Chapter 15

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data, and never paste real bank or card details from your expenses. Always run and read the code yourself. A test with a known result decides who is right, not the AI.

## Plan: Review the data model

**Prompt:** "I am a beginner. I know lists, dictionaries, tuples and sets. I want a program that records <describe the records, for example: the cafe's expenses, a category and an amount for each one>. At the end it prints <describe the summary>. Do not write the program. Suggest how to store the data, and give one reason."

**Use it when:** you know what the program must remember but not how to store it.

**A good answer:** one clear model, such as a list of tuples, with a reason, and a note on how the summary is built from it.

**Check it:** write down a real day with a repeated category, such as milk twice. Put it into the suggested model on paper or in a short test. If any record is lost or replaced, the model is wrong for your data.

## Write: Which message does each answer get?

**Prompt:** "I wrote this loop myself: <paste your loop>. Do not change it. For each of these answers, tell me exactly what it prints: <list three answers, such as an allowed category with a space and a capital letter, a category that is not allowed, and done>."

**Use it when:** you have written the input checks and want to be sure every branch works.

**A good answer:** one line for each answer, with the exact message, and a note on what `strip()` and `lower()` change.

**Check it:** run the loop with the same answers and compare every line with the AI's prediction.

## Generate: One step of the summary

**Prompt:** "Here is my dictionary of totals: <paste it>. Write the code that finds <the key with the biggest value>. Tell me exactly what it prints for my dictionary."

**Use it when:** you need one small piece of the summary.

**A good answer:** short code using only what you know, and an exact predicted output that you can check by hand.

**Check it:** work out the right answer yourself first. Then run the code on several dictionaries, including an empty one. `max()` on a dictionary compares the keys, so check that the answer is the key with the biggest value.

## Debug: Explain the crash first

**Prompt:** "I am a beginner. I ran this code: <paste the code>. I got this exact error: <paste the full error report>. First explain what the error means and which line causes it. Then show the smallest fix that works for every day, including a day with no records."

**Use it when:** the program stops with an error on one of your test cases.

**A good answer:** it names the error type and the line, explains why that case caused it, and gives a fix that handles the case instead of hiding the error.

**Check it:** run the fix on every test case again, not only the one that failed.

## Test: Test days with expected results

**Prompt:** "Here is my tracker: <paste the code>. List test days for it. For each day, give the answers I type and the exact last lines the program should print. Include a normal day, an empty day, a bad amount, a category that is not allowed, and a day with one record."

**Use it when:** your tracker works for one day and you want to know it works for every day.

**A good answer:** a numbered list of days, each with typed answers and an expected result that you can check by hand.

**Check it:** run every day and mark it pass or fail. A test can pass by luck, so use different data in each test. After any fix, run every day again.

## Improve: Shorter, but the same

**Prompt:** "Suggest one way to make <lines N to M> of my program shorter. Do not change what the program prints: <paste your code>."

**Use it when:** your tracker passes every test and you want cleaner code.

**A good answer:** one small change with a reason, which keeps every output the same.

**Check it:** apply the change and run every test day again. If any result changes, or the program stops with an error, undo the change.
