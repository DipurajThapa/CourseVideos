# AI Prompt Cards: Chapter 10

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run and read the code yourself. A test with a known result decides who is right, not the AI.

## Plan: The rules before the code

**Prompt:** "I am a beginner. I know variables, input, int, if, elif and else, while loops with break, and for loops with range. I want to build <describe the game, for example: a number guessing game with a secret from 1 to 20 and five tries>. Do not write code. List the rules of the game, the values the program must remember, and what happens after each kind of answer."

**Use it when:** you know the game you want but not the steps to build it.

**A good answer:** a short list of rules, the values to remember (such as the secret and the number of tries), and one line for each kind of answer: too low, too high, correct, and not a number.

**Check it:** play the game on paper with the plan. If an answer such as a word or a 0 has no rule, add one before you write code.

## Write: Check my branches

**Prompt:** "I wrote this code myself: <paste your if, elif and else lines>. Do not change it. For each of these answers, tell me which message it prints: <list three answers, one below, one equal to and one above the secret>."

**Use it when:** you have written the decisions and want to be sure every branch can happen.

**A good answer:** one line for each answer, naming the exact message, and a note if any branch can never be reached.

**Check it:** run your code with each answer and compare the message with the AI's.

## Generate: One line with exact limits

**Prompt:** "Write one line of Python that picks a random whole number from <smallest> to <largest>, including both. Name the variable <name>. Tell me exactly which numbers it can pick."

**Use it when:** you need a small piece of code with a precise range.

**A good answer:** one line that uses `random.randint(<smallest>, <largest>)`, with the statement that both ends can be picked.

**Check it:** if the line uses `randrange()`, remember that it stops before its end value, like `range()`. Run the line many times in a loop and print the lowest and highest numbers it picked.

## Debug: Explain the crash first

**Prompt:** "I am a beginner. I ran this code: <paste the code>. I typed <what you typed>, and I got this exact error: <paste the full error report>. First explain what the error means and which line causes it. Then show the smallest fix that keeps my program running."

**Use it when:** an answer the player typed made the program stop with an error.

**A good answer:** it names the error type and the line, explains why that answer caused it, and checks the answer before converting it, instead of hiding the error.

**Check it:** run the fixed program with the same answer. It must not crash, and it must still work for a normal answer.

## Test: A list of cases with expected results

**Prompt:** "Here is my game: <paste the code>. List test cases for it. For each case, give the answers the player types and the exact last line the program should print. Include a win, a loss, a word instead of a number, and the smallest and largest allowed answers."

**Use it when:** your game works once and you want to know it works every time.

**A good answer:** a numbered list of cases, each with typed answers and an expected result, covering every branch and both boundary values (the smallest and largest allowed answers).

**Check it:** fix the secret for testing, run every case and mark each one pass or fail. After any fix, run every case again.

## Improve: A review that keeps the behaviour

**Prompt:** "Review my game for readability. Suggest at most two changes, each with one reason. Do not change what it prints or which answers it accepts: <paste your code>."

**Use it when:** your game works and passes its tests.

**A good answer:** small, clear suggestions, each with a reason, that keep the behaviour the same.

**Check it:** apply one suggestion at a time and run every test case again. If any result changes, the suggestion broke your rule, so undo it.
