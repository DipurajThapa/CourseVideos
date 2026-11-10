# AI Prompt Cards: Chapter 19

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. A test is only useful if it can fail, so check every AI test on broken code too.

## Plan: List what to test before any code

**Prompt:** "I am a beginner learning pytest. Here is my function: <paste it>. Do not write any code yet. List the behaviours I should test. For each one, give one input and the exact expected result. Include normal values and edge cases, and say which mistake each case would catch."

**Use it when:** you have a working function and do not know which inputs to test.

**A good answer:** a short list of input and expected-result pairs, with normal values and edge values such as 0, an exact limit and one more than the limit.

**Check it:** work out every expected result yourself, by hand or with a calculator. If you cannot explain why an expected result is right, do not use it.

## Write: Write your own tests first

**Prompt:** "Here are the tests I wrote myself for <function name>: <paste them>. Do not change them. Which behaviour of the function do they not test yet? Give one missing input and its exact expected result."

**Use it when:** you have written a few tests and want to know what you missed.

**A good answer:** one or two specific missing inputs, each with an exact expected result and a short reason.

**Check it:** add the new case to your file and run `pytest`. Work out the expected result yourself first.

## Generate: Ask for a precise test file

**Prompt:** "Write a pytest file named test_<module>.py for these functions: <paste them>. Import them from <module>. Write one behaviour per test function, with names that start with test_. Every test must have an assert with an exact expected value. Compare decimal results with round() or pytest.approx(). Include edge cases."

**Use it when:** you want a full set of tests quickly.

**A good answer:** short test functions, each with one clear `assert` and an exact expected value, and at least one edge case per function.

**Check it:** look for tests with no `assert`, and for expected values that the AI may have copied from the code's own output. Then run the file with `python -m pytest -q`.

## Test: Break the code on purpose

**Prompt:** "Here are your tests: <paste them>. Here is a broken copy of my function, where I changed <describe the change>: <paste it>. Which of your tests should fail on the broken copy, and why?"

**Use it when:** all the AI's tests pass and you want to know if they could ever fail.

**A good answer:** it names specific tests that should fail and the values that would differ, or it admits that no test catches the change.

**Check it:** save the broken copy in its own folder with a copy of the tests, and run `pytest` there. Good tests fail on broken code. If none fails, the tests are too weak.

## Debug: Is the code or the test wrong?

**Prompt:** "This pytest test fails: <paste the test>. Here is the full pytest report: <paste it>. First explain whether the code or the test is wrong, and why. Then show the smallest fix."

**Use it when:** a test fails and you are not sure where the problem is.

**A good answer:** it reads the values in the `E` lines of the report, decides whether the code or the test is wrong, and explains why before it shows a fix.

**Check it:** apply the fix and run every test again, not only the one that failed.

## Improve: Review the tests before you change them

**Prompt:** "Review my pytest file for readability: <paste it>. Suggest at most two improvements, each with one reason. Do not remove any test that checks a different input."

**Use it when:** your tests pass and you want them clearer.

**A good answer:** small changes, such as clearer test names, with a reason for each.

**Check it:** if the AI suggests deleting a test, first run the shorter file on a broken copy. Keep every test that catches a mistake the others miss.
