# AI Prompt Cards: Chapter 22

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data, and that includes real files of customer or staff names: paste a small made-up sample instead. Always run the code yourself, and test every case the AI lists.

## Plan: List what could go wrong

**Prompt:** "I am a beginner learning Python exceptions. Here is what my code does: <describe it, for example: reads scores.csv and turns each score into an int>. Do not write code yet. List what could go wrong when it runs. For each problem, name the exception Python raises and say what the program should do: show a message, skip the item, or stop."

**Use it when:** your code works on good data, and you want to know where bad data could break it.

**A good answer:** a short list of real problems, each with an exception name such as `FileNotFoundError` or `ValueError`, and a sensible action for each one.

**Check it:** make one small test file or input for each problem, run your code on it, and confirm that Python raises the exception the AI named.

## Write: Write your own error handling first

**Prompt:** "I wrote this function myself: <paste it>. Do not rewrite it. For each of these problems, <list them>, tell me whether my code handles it, and which line does it."

**Use it when:** you have added `try` and `except` yourself and want to check what they cover.

**A good answer:** one line per problem, with the line number that handles it, or a clear "not handled".

**Check it:** run your code on each problem case. A case the AI says is handled must give your message, not a crash.

## Generate: Ask for specific, small try blocks

**Prompt:** "Write a Python function <name and parameters> that <task>. Catch only these exceptions: <list>. Keep each try block as small as possible, so one bad item does not stop the rest. Show a clear message that names the problem and the value. Do not use a bare except or except Exception."

**Use it when:** you want error handling that does not hide bugs.

**A good answer:** short `try` blocks around the lines that can fail, named exceptions in every `except`, and messages that name the value.

**Check it:** look for a bare `except:`, `except Exception:` or `pass`. Then run every test case, including one item that is damaged in the middle of the data.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. My code crashed with this error report: <paste the full report>. Here is the code: <paste it>. First explain which line raised the exception and why. Then show the smallest fix. Do not catch more exceptions than this one."

**Use it when:** an exception you did not expect stops the program.

**A good answer:** it names the line and the cause in plain words, then a small fix that handles this case only.

**Check it:** apply the fix, run the case that crashed, then run every earlier case again.

## Test: One test case for each problem

**Prompt:** "Here is my function: <paste it>. Write test cases for it: one normal case and one case for each of these problems: <list>. For each case, give the input or the file contents and the exact result I should expect."

**Use it when:** you want proof that each error is handled, not only the normal case.

**A good answer:** small, separate cases with exact expected results, including at least one case where the bad item is in the middle.

**Check it:** run every case. Then break your function on purpose, for example by removing one `except`, and confirm that at least one case fails.

## Improve: One suggestion, then test that it hides nothing

**Prompt:** "All my test cases pass. Suggest at most one improvement to my error handling, with one reason. Do not catch more exceptions than I catch now."

**Use it when:** your code works and you want clearer messages or simpler code.

**A good answer:** one specific change, such as a clearer message, that keeps the same exceptions.

**Check it:** add a deliberate typing error to the code inside `try` and run it. If the change hides your typing error, reject it. Then remove the typing error and run every test case again.
