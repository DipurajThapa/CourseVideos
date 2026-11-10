# AI Prompt Cards: Chapter 27

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data, such as real customer or supplier numbers. Write your tests before you ask for any change, and run them after every change the AI suggests.

## Plan: Ask for an explanation, not a change

**Prompt:** "I am a beginner. Someone else wrote this Python function: <paste it>. Do not change it. Explain what it does in plain words, line by line, and tell me what it returns for this input: <an example input>."

**Use it when:** you have to work on code you did not write and do not understand yet.

**A good answer:** one plain sentence for each part of the code, and an exact predicted result for your example input.

**Check it:** run the code with the example input, and with one more input near a boundary, such as exactly 3 left. Every claim the AI made must match a real run. If one claim is wrong, the explanation is wrong.

## Write: Write characterization tests yourself first

**Prompt:** "Here is a function and the tests I wrote for it: <paste both>. Do not change the function. Which inputs do my tests not cover yet? List up to three, and say what you expect the function returns for each."

**Use it when:** you have written tests that record what the code does now, and want to find a case you missed.

**A good answer:** a short list of inputs your tests do not cover, such as an empty input or a boundary value, each with a predicted result.

**Check it:** run the function on each suggested input and write the real result into a new test. The real run decides the expected value, not the AI's prediction.

## Generate: Ask for one refactoring at a time

**Prompt:** "Refactor this function with clearer names. Keep its behaviour exactly the same, including the edge cases. Do not add features. Show the new code only: <paste the function>."

**Use it when:** your tests pass and you want clearer code.

**A good answer:** the same logic with better names, and nothing new: no sorting, no printing, no changed comparison.

**Check it:** compare the old and the new version with a diff. Look at every changed comparison (`<` against `<=`), every changed number and every new function call. Then run your tests.

## Test: Run your tests on the AI's version

**Prompt:** "I ran my tests on your refactored version. This test failed: <paste the test and the pytest report>. The old version passed it. Which line of your version changed the behaviour?"

**Use it when:** a test fails after an AI refactoring.

**A good answer:** the exact line that changed, for example a comparison, and why the test case now gives a different result.

**Check it:** fix that one line and run every test again. If the tests pass, compare the diff once more to make sure nothing else changed.

## Debug: Find the cause before the fix

**Prompt:** "After a refactoring, this program stopped working: <paste the code>. Here is the full error report: <paste it>. First explain the cause. Then show the smallest fix. Do not change the function's behaviour."

**Use it when:** another program breaks after you rename or move a function.

**A good answer:** it names the cause, such as an old function name that other code still imports, and gives a one-line fix.

**Check it:** apply the fix, run the program that broke, and run all your tests again.

## Improve: One improvement, then every test again

**Prompt:** "My refactored function passes all my tests: <paste the function and the tests>. Suggest one improvement for readability only. It must not change any result. Give one sentence on why it helps."

**Use it when:** your code works and you want to make it clearer.

**A good answer:** one small change with a reason, such as a docstring or a better name.

**Check it:** run every test again. If a test fails, the suggestion changed the behaviour, even if the AI said it would not. A new feature, such as sorting the results, is not a readability change.
