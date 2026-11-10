# AI Prompt Cards: Chapter 23

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste an API key, a password or private customer data. A sample response from a public service is fine, after you remove anything personal. Always run the code yourself, on the real sample.

## Plan: Ask the AI to explain the response

**Prompt:** "I am a beginner learning JSON in Python. Here is a saved response from a web API: <paste the sample>. Do not write code yet. Describe its structure: which parts are objects, which are lists, and which values are strings, numbers, true, false or null. Then give the path to <the value you need>."

**Use it when:** you have a new response and do not yet know where your value lives.

**A good answer:** a short map of the response, level by level, with the exact field names from the sample and a path such as `data["items"][0]["price"]`.

**Check it:** open the sample yourself and follow the path, level by level. Every field name in the answer must appear in the sample, spelled the same way. Note any value in quotation marks: it is a string, even if it holds digits.

## Write: Write your own extraction first

**Prompt:** "I wrote this function myself: <paste it>. Here is the sample response: <paste it>. Do not rewrite my code. What does it return for <item>, and which line handles an item that is not in the response?"

**Use it when:** you have written your own code and want to check your understanding.

**A good answer:** the exact value and its type for your item, and the line number that returns your default for a missing item.

**Check it:** run your function on the sample with the same items, and compare the real results with the AI's answer.

## Generate: Ask for a function from a clear description

**Prompt:** "Write a Python function <name and parameters> for this sample response: <paste it>. It returns <what, with its type>, and <default> when the item is missing. Use only the field names in the sample. Tell me exactly what it returns for <item>."

**Use it when:** you want a second version to compare with your own.

**A good answer:** short code that uses only field names from the sample, loops over lists, and converts text to numbers where needed.

**Check it:** run it on the sample. Compare the result, and its type, with what the AI promised. A crash or a value in quotation marks means the AI misread the structure.

## Debug: Find the cause before the fix

**Prompt:** "My extraction code worked yesterday. Today's response is different: <paste it>. Here is my code: <paste it>, and the full error: <paste it>. First explain which value in the response caused the error. Then show the smallest fix."

**Use it when:** a new response breaks code that worked on the old sample.

**A good answer:** it points at the exact value in the new response, such as a `null` or a missing field, and fixes that case only.

**Check it:** save the new response as a second sample. Run your code on the old sample and the new one, and run every earlier test case again.

## Test: Exact values and types

**Prompt:** "Here is my function: <paste it> and my sample response: <paste it>. Write test cases with the exact value I should get, including its type: a normal item, an item with a decimal price, and an item that is missing."

**Use it when:** you want proof that your code returns numbers, not text, and handles missing items.

**A good answer:** a short list of cases with exact expected values such as `1.2`, `1.85` and `None`.

**Check it:** run every case and print the result with `!r`, so text shows its quotation marks. A case with `'1.20'` where you expected `1.2` fails, even though the digits match.

## Improve: Check every field name

**Prompt:** "All my test cases pass. Suggest one improvement to this function, with one reason. Use only field names that appear in my sample: <paste it>."

**Use it when:** your code works and you want it clearer or safer.

**A good answer:** one small change that keeps the same field names and the same results.

**Check it:** search the sample for every field name the suggestion uses. If a name is not in the sample, reject the suggestion. Then run every test case again.
