# Video Script: Chapter 10: Boss Level 2: The Number Guessing Game

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:47.

## Scene 1: Introduction (0:00 to 1:00)

**Section:** Introduction

**Direction:** Open on the Chapter 9 limit: a typed word crashes the program. One recall question, then the boss level title and the jar.

- **Narration:** At the end of Chapter 9, Asha's report still trusted every answer. Before she builds a game, she checks what one guess does with a word.
  **On screen:** Code `examples/ex04_word_crash.py`, line 3 highlighted, output hidden
- **Narration:** Here is the problem, in lines 2 and 3. Line 3 asks for a guess, and converts the answer with int at once. A customer types the word seven.
  **On screen:** Code `examples/ex04_word_crash.py`, line 2, 3 highlighted, output hidden
- **Interaction:** "The customer types `seven`. What does `int()` do with it?" stays on screen with a 10-second timer.
- **Narration:** It crashes, with a Value Error. You met this error in Chapter 4. Int can only convert text that looks like a whole number.
  **On screen:** Code `examples/ex04_word_crash.py`, line 2, 3 highlighted, error `examples/ex04_word_crash.expected_error`
- **Narration:** Today, Asha builds a game that handles a word, an empty answer or a wrong number, without crashing.
  **On screen:** Code `examples/ex04_word_crash.py`, line 2, 3 highlighted, error `examples/ex04_word_crash.expected_error`
- **Narration:** Welcome to Chapter 10, the second boss level!
  **On screen:** The Number Guessing Game
- **Narration:** You will combine decisions, loops and careful checks into one game.
  **On screen:** The Number Guessing Game Guess. Check. Never crash.
- **Narration:** And an AI assistant will promise you a number it can never pick. A test will prove it.
  **On screen:** The Number Guessing Game Guess. Check. Never crash.

## Scene 2: The mission (1:00 to 1:38)

**Section:** The mission

**Direction:** The biscuit jar game, then the table of what each chapter contributes, row by row.

- **Narration:** The Corner Cafe has a glass jar of biscuits on the counter. It holds from 1 to 20.
  **On screen:** The biscuit jar game
    - A glass jar on the counter holds 1 to 20 biscuits.
- **Narration:** Each customer gets five guesses, with a hint after each one. Guess right, and you win a free tea.
  **On screen:** The biscuit jar game
    - A glass jar on the counter holds 1 to 20 biscuits.
    - Each customer gets five guesses, with a hint after each one.
    - Guess right, and win a free tea.
- **Narration:** And this time, no answer may crash the game. Not a word, not an empty answer, not a number outside 1 to 20.
  **On screen:** The biscuit jar game
    - A glass jar on the counter holds 1 to 20 biscuits.
    - Each customer gets five guesses, with a hint after each one.
    - Guess right, and win a free tea.
    - Words, empty answers and numbers outside 1 to 20 must never crash the game.
- **Narration:** You already know almost every piece: decisions from Chapter 6, and a while loop from Chapter 7.
  **On screen:** Table: Everything you need (row 1 in focus)
- **Narration:** A for loop from Chapter 8, and testing from Chapter 9.
  **On screen:** Table: Everything you need (row 3 in focus)
- **Narration:** And two new tools: the random module, to pick the secret number, and is digit, to check an answer.
  **On screen:** Table: Everything you need (row 5 in focus)

## Scene 3: What you will build (1:38 to 1:59)

**Section:** What you will build

**Direction:** Show one finished game as the destination. The secret was fixed at 7 for this run.

- **Narration:** Here is where we are going. Look at the game on the right: the header, with the rules.
  **On screen:** Code `examples/test_high_low.py`, output `examples/test_high_low.expected`
- **Narration:** The player guesses 12. Too high, four tries left. Then 3. Too low, three tries left.
  **On screen:** Code `examples/test_high_low.py`, output `examples/test_high_low.expected`
- **Narration:** Then 7. Correct! Three guesses used, and a free tea.
  **On screen:** Code `examples/test_high_low.py`, output `examples/test_high_low.expected`
- **Narration:** About twenty lines of code. By the end of this video, you will understand every one.
  **On screen:** Code `examples/test_high_low.py`, output `examples/test_high_low.expected`

## Scene 4: Acceptance criteria (1:59 to 3:07)

**Section:** Acceptance criteria

**Direction:** Five criteria, revealed one by one. A quiz on criterion four, then a breather.

- **Narration:** Asha writes down what done means first. The game is finished when all five are true.
  **On screen:** Done means all five are true
- **Narration:** One. It picks a secret from 1 to 20, and every number can be picked. Remember that one!
  **On screen:** Done means all five are true
    - Picks a secret from 1 to 20. Every number can be picked.
- **Narration:** Two and three. Hints after each guess, and a clear end after a win or five guesses.
  **On screen:** Done means all five are true
    - Picks a secret from 1 to 20. Every number can be picked.
    - After each guess: Too low or Too high, and the tries left.
    - Stops after a win or five guesses, and shows the secret.
- **Narration:** Four. A word, an empty answer, or a number outside 1 to 20 gets a message. It does not count as a try, and it never crashes the game.
  **On screen:** Done means all five are true
    - Picks a secret from 1 to 20. Every number can be picked.
    - After each guess: Too low or Too high, and the tries left.
    - Stops after a win or five guesses, and shows the secret.
    - A word, an empty answer or a number outside 1 to 20 gets a message, is not a try, and never crashes the game.
- **Narration:** And five. It passes at least six tests with known results.
  **On screen:** Done means all five are true
    - Picks a secret from 1 to 20. Every number can be picked.
    - After each guess: Too low or Too high, and the tries left.
    - Stops after a win or five guesses, and shows the secret.
    - A word, an empty answer or a number outside 1 to 20 gets a message, is not a try, and never crashes the game.
    - Passes at least six tests with known results.
- **Narration:** Quick check, using criterion four. Which answer counts as one of the five tries?
  **On screen:** Quick check: "Which answer counts as one of the five tries?" (options shown)
- **Interaction:** "Which answer counts as one of the five tries?" stays on screen with a 10-second timer.
- **Narration:** D, 12. It is a whole number from 1 to 20. A word, an empty answer and 25 get a message, and the player keeps the try.
  **On screen:** Quick check: "Which answer counts as one of the five tries?" (answer revealed: `12`)
- **Narration:** Take a breather. You know the game, and what done means.
  **On screen:** Breather card
    - The game: 1 to 20, five tries, a free tea.
    - Every answer is handled.
    - Five criteria say when it is done.
- **Narration:** Next, Asha plans the rules with an AI assistant, before any code.
  **On screen:** Breather card
    - The game: 1 to 20, five tries, a free tea.
    - Every answer is handled.
    - Five criteria say when it is done.
- **Breather:** 4 quiet seconds.

## Scene 5: Plan it with AI (3:07 to 3:54)

**Section:** Plan it with AI

**Direction:** Stage 1 plan, then Asha plays it on paper and adds two rules.

- **Narration:** In this project, all six AI stages work on one game, turn by turn as Asha builds it. Stage 1: plan. Asha says what she knows, and what she wants. And she says: no code yet.
  **On screen:** AI chat, stage 1: Plan: the rules before the code
    - You: I am a beginner. I know variables, input, int, if, elif and else, while loops with break, and for loops with range. I want a number guessing game with a secret from 1 to 20 and five tries. Do not write code. List the rules, the values to remember, and what happens after each kind of answer.
- **Narration:** The AI lists the values to remember: the secret, the tries, and whether the player has won. Then a rule for low, high and equal.
  **On screen:** AI chat, stage 1: Plan: the rules before the code
    - You: I am a beginner. I know variables, input, int, if, elif and else, while loops with break, and for loops with range. I want a number guessing game with a secret from 1 to 20 and five tries. Do not write code. List the rules, the values to remember, and what happens after each kind of answer.
    - AI (example answer): Values to remember: the secret, the tries used, and whether the player has won. Each turn: lower than the secret, say Too low. Higher, say Too high. Equal, the player wins and the game stops. The game also stops after five tries, and shows the secret.
- **Narration:** It is a good plan for numbers. But what about a customer who types a word?
  **On screen:** AI chat, stage 1: Plan: the rules before the code
    - You: I am a beginner. I know variables, input, int, if, elif and else, while loops with break, and for loops with range. I want a number guessing game with a secret from 1 to 20 and five tries. Do not write code. List the rules, the values to remember, and what happens after each kind of answer.
    - AI (example answer): Values to remember: the secret, the tries used, and whether the player has won. Each turn: lower than the secret, say Too low. Higher, say Too high. Equal, the player wins and the game stops. The game also stops after five tries, and shows the secret.
- **Narration:** Asha plays the game on paper, and types a word. The plan has no rule for it.
  **On screen:** Asha adds two rules
    - She plays the game on paper and types a word. The plan has no rule for it.
- **Narration:** So she adds a rule. An answer that is not a whole number gets a message.
  **On screen:** Asha adds two rules
    - She plays the game on paper and types a word. The plan has no rule for it.
    - Rule: an answer that is not a whole number gets a message.
- **Narration:** And a second rule. A number outside 1 to 20 gets a message too.
  **On screen:** Asha adds two rules
    - She plays the game on paper and types a word. The plan has no rule for it.
    - Rule: an answer that is not a whole number gets a message.
    - Rule: a number outside 1 to 20 gets a message.
- **Narration:** Neither one costs the player a try. A typing mistake should not lose a free tea!
  **On screen:** Asha adds two rules
    - She plays the game on paper and types a word. The plan has no rule for it.
    - Rule: an answer that is not a whole number gets a message.
    - Rule: a number outside 1 to 20 gets a message.
    - Neither one counts as a try.

## Scene 6: Step 1: One guess, three answers (3:54 to 4:52)

**Section:** Build it step by step

**Direction:** A fixed secret so every answer is known. Teach the three branches, ask, reveal. Then stage 2: the AI checks Asha's branches.

- **Narration:** Time to build. Step 1 starts with a fixed secret, 7, so Asha knows what every guess should print.
  **On screen:** Code `examples/ex02_one_guess.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 asks for one guess and converts it.
  **On screen:** Code `examples/ex02_one_guess.py`, line 3 highlighted, output hidden
- **Narration:** Lines 4 and 5: if the guess equals the secret, Correct.
  **On screen:** Code `examples/ex02_one_guess.py`, line 4, 5 highlighted, output hidden
- **Narration:** Lines 6 and 7: if it is lower, Too low.
  **On screen:** Code `examples/ex02_one_guess.py`, line 6, 7 highlighted, output hidden
- **Narration:** And lines 8 and 9: anything else is higher, so Too high.
  **On screen:** Code `examples/ex02_one_guess.py`, line 8, 9 highlighted, output hidden
- **Interaction:** "The secret is 7. The player types 12. Which message prints?" stays on screen with a 10-second timer.
- **Narration:** Too high! 12 is not equal to 7, and not lower, so the else branch runs.
  **On screen:** Code `examples/ex02_one_guess.py`, line 8, 9 highlighted, output `examples/ex02_one_guess.expected`
- **Narration:** Stage 2: write. Asha wrote these branches herself. She asks the AI which message each guess gets, below, equal to and above the secret.
  **On screen:** AI chat, stage 2: Write it yourself, then check the branches
    - You: I wrote this guess check myself, with the secret 7. Do not change it. Which message does each guess get: 6, 7 and 12? [code `examples/ex02_one_guess.py`]
- **Narration:** The AI names one message for each guess. Every branch can happen.
  **On screen:** AI chat, stage 2: Write it yourself, then check the branches
    - You: I wrote this guess check myself, with the secret 7. Do not change it. Which message does each guess get: 6, 7 and 12? [code `examples/ex02_one_guess.py`]
    - AI (example answer): 6 is lower than 7, so it gets `Too low!`. 7 is equal, so it gets `Correct!`. 12 is higher, so it goes to `else` and gets `Too high!`.
- **Narration:** She runs her code with 12, and gets the AI's answer: Too high.
  **On screen:** AI chat, stage 2: Write it yourself, then check the branches
    - You: I wrote this guess check myself, with the secret 7. Do not change it. Which message does each guess get: 6, 7 and 12? [code `examples/ex02_one_guess.py`]
    - AI (example answer): 6 is lower than 7, so it gets `Too low!`. 7 is equal, so it gets `Correct!`. 12 is higher, so it goes to `else` and gets `Too high!`.
    - You: I ran it and typed 12:

## Scene 7: Step 2: Five tries (4:52 to 5:48)

**Section:** Build it step by step

**Direction:** Teach the loop, the counter, break and the bool, then predict the last line.

- **Narration:** Step 2: five tries. Line 3 counts the tries, starting at 0.
  **On screen:** Code `examples/ex03_tries.py`, line 3 highlighted, output hidden
- **Narration:** Line 4 repeats while tries is less than 5. That is true for 0, 1, 2, 3 and 4: exactly five guesses.
  **On screen:** Code `examples/ex03_tries.py`, line 4 highlighted, output hidden
- **Narration:** Line 6 adds one try after each guess.
  **On screen:** Code `examples/ex03_tries.py`, line 6 highlighted, output hidden
- **Narration:** When the guess is right, line 8 prints Correct with the tries used, and line 9 breaks out of the loop.
  **On screen:** Code `examples/ex03_tries.py`, line 7, 8, 9 highlighted, output hidden
- **Narration:** The hints on lines 11 and 13 also say how many tries are left: 5, minus the tries used.
  **On screen:** Code `examples/ex03_tries.py`, line 11, 13 highlighted, output hidden
- **Narration:** And after the loop, line 14 checks the last guess. If it is still wrong, the player ran out of tries.
  **On screen:** Code `examples/ex03_tries.py`, line 14, 15 highlighted, output hidden
- **Interaction:** "The player types 12, then 3, then 7. What is the last line of output?" stays on screen with a 10-second timer.
- **Narration:** Correct! Tries: 3. The third guess was right, so break stopped the loop, and line 15 never ran.
  **On screen:** Code `examples/ex03_tries.py`, line 8, 9 highlighted, output `examples/ex03_tries.expected`

## Scene 8: Step 3: A random secret (5:48 to 9:08)

**Section:** Build it step by step

**Direction:** Teach import, randint with both ends, randrange like range, and the seed. Then stage 3 plants the AI mistake, a test loop proves it, and stage 4 confirms. Quiz, breather.

- **Narration:** Step 3: a real secret. A fixed 7 is no game. Python has a module for random numbers. A module is a file of ready-made Python code, and import loads it.
  **On screen:** Step 3: The random module
    - A **module** is a file of ready-made Python code. `import random` loads one.
- **Narration:** Random dot rand int, 1 comma 20, picks a whole number from 1 to 20. Both ends are included: 1 and 20 can both be picked.
  **On screen:** Step 3: The random module
    - A **module** is a file of ready-made Python code. `import random` loads one.
    - `random.randint(1, 20)` picks a whole number from 1 to 20. **Both ends** are included.
- **Narration:** The module also has rand range. It works like range from Chapter 8: it stops before its end value. So rand range 1 comma 20 never picks 20.
  **On screen:** Step 3: The random module
    - A **module** is a file of ready-made Python code. `import random` loads one.
    - `random.randint(1, 20)` picks a whole number from 1 to 20. **Both ends** are included.
    - `random.randrange(1, 20)` works like `range()`: it **stops before** 20.
- **Narration:** And a seed makes the same random numbers on every run. That sounds strange, but it is useful for testing.
  **On screen:** Step 3: The random module
    - A **module** is a file of ready-made Python code. `import random` loads one.
    - `random.randint(1, 20)` picks a whole number from 1 to 20. **Both ends** are included.
    - `random.randrange(1, 20)` works like `range()`: it **stops before** 20.
    - `random.seed(3)` makes the same numbers on every run: useful for tests.
- **Narration:** Line 2 imports the module. Line 3 sets the seed to 3.
  **On screen:** Code `examples/ex01_random.py`, line 2, 3 highlighted, output `examples/ex01_random.expected`
- **Narration:** Lines 4 to 6 pick three numbers: 8, 19 and 18.
  **On screen:** Code `examples/ex01_random.py`, line 4, 5, 6 highlighted, output `examples/ex01_random.expected`
- **Narration:** On the same Python, the same numbers come back on every run. Your numbers may differ on another version. Delete line 3, and the numbers change on every run. A real game has no seed.
  **On screen:** Code `examples/ex01_random.py`, line 3 highlighted, output `examples/ex01_random.expected`
- **Narration:** Stage 3: generate. Asha asks the AI for the secret line, from 1 to 20, including both. And she asks exactly which numbers it can pick.
  **On screen:** AI chat, stage 3: Generate: one line with exact limits
    - You: Write one line of Python that picks a random whole number from 1 to 20, including both. Name the variable secret. Tell me exactly which numbers it can pick.
- **Narration:** The AI writes one line with rand range, 1 comma 20. And it says every number from 1 to 20 can be picked. It sounds sure.
  **On screen:** AI chat, stage 3: Generate: one line with exact limits
    - You: Write one line of Python that picks a random whole number from 1 to 20, including both. Name the variable secret. Tell me exactly which numbers it can pick.
    - AI (example answer): Here is the line: `secret = random.randrange(1, 20)` It can pick every whole number from 1 to 20.
- **Interaction:** "The AI says `randrange(1, 20)` can pick every number from 1 to 20. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Rand range stops before its end value, like range. But Asha does not argue. She tests it.
  **On screen:** AI chat, stage 3: Generate: one line with exact limits
    - You: Write one line of Python that picks a random whole number from 1 to 20, including both. Name the variable secret. Tell me exactly which numbers it can pick.
    - AI (example answer): Here is the line: `secret = random.randrange(1, 20)` It can pick every whole number from 1 to 20.
- **Narration:** Line 6 is a for loop from Chapter 8. It runs line 7, the AI's line, ten thousand times.
  **On screen:** Code `examples/ai_secret_flawed.py`, line 6, 7 highlighted, output hidden
- **Narration:** Lines 4 and 5 start lowest at 20 and highest at 1, the opposite ends, so the first number picked replaces both.
  **On screen:** Code `examples/ai_secret_flawed.py`, line 4, 5 highlighted, output hidden
- **Narration:** Lines 8 to 11 keep the lowest and the highest number so far. Line 3 is a seed, so the test gives the same result every run.
  **On screen:** Code `examples/ai_secret_flawed.py`, line 8, 9, 10, 11 highlighted, output hidden
- **Interaction:** "If 20 can be picked, what should line 13 print?" stays on screen with a 10-second timer.
- **Narration:** Highest, 20. But it prints 19! In ten thousand draws, 20 never appeared.
  **On screen:** Code `examples/ai_secret_flawed.py`, line 13 highlighted, output `examples/ai_secret_flawed.expected`
- **Narration:** A customer with a jar of 20 biscuits could never win.
  **On screen:** Code `examples/ai_secret_flawed.py`, output `examples/ai_secret_flawed.expected`
- **Narration:** Stage 4: test. Asha shows the AI the line and the result: highest, 19.
  **On screen:** AI chat, stage 4: Test: show the AI the evidence
    - You: You said randrange(1, 20) can pick 20. I ran your line 10,000 times and kept the lowest and the highest: [code `examples/ai_secret_flawed.py`]
- **Narration:** Now the AI agrees. Rand range stops before 20. It suggests rand int, 1 comma 20.
  **On screen:** AI chat, stage 4: Test: show the AI the evidence
    - You: You said randrange(1, 20) can pick 20. I ran your line 10,000 times and kept the lowest and the highest: [code `examples/ai_secret_flawed.py`]
    - AI (example answer): You are right, and I was wrong. `randrange()` stops before its end value, like `range()`, so 20 is never picked. Use `random.randint(1, 20)`, which includes both ends.
- **Narration:** Asha runs the same test with rand int. Highest, 20. Both ends appear.
  **On screen:** AI chat, stage 4: Test: show the AI the evidence
    - You: You said randrange(1, 20) can pick 20. I ran your line 10,000 times and kept the lowest and the highest: [code `examples/ai_secret_flawed.py`]
    - AI (example answer): You are right, and I was wrong. `randrange()` stops before its end value, like `range()`, so 20 is never picked. Use `random.randint(1, 20)`, which includes both ends.
    - You: I ran the same test with randint:
- **Narration:** Quick check. Which line picks a whole number from 1 to 6, like a dice?
  **On screen:** Quick check: "Which line picks a whole number from 1 to 6, like a dice?" (options shown)
- **Interaction:** "Which line picks a whole number from 1 to 6, like a dice?" stays on screen with a 10-second timer.
- **Narration:** B. Rand int, 1 comma 6. Both ends are included. Rand range would never roll a 6.
  **On screen:** Quick check: "Which line picks a whole number from 1 to 6, like a dice?" (answer revealed: `random.randint(1, 6)`)
- **Narration:** Breather. The secret is random now, and you know every number can be picked.
  **On screen:** Breather card
    - `randint(1, 20)` includes both ends.
    - `randrange()` stops before its end.
    - A test with 10,000 draws caught the AI.
- **Narration:** Next, the crash from the start of this video.
  **On screen:** Breather card
    - `randint(1, 20)` includes both ends.
    - `randrange()` stops before its end.
    - A test with 10,000 draws caught the AI.
- **Breather:** 4 quiet seconds.

## Scene 9: Step 4: Check before you convert (9:08 to 10:13)

**Section:** Build it step by step

**Direction:** Stage 5 debug: cause first. Then teach isdigit with its rule, ask which lines are True, reveal.

- **Narration:** Stage 5: debug. Asha pastes the two lines and the full error from the start of this video. She asks for the cause first, then the smallest fix.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: A customer typed seven, and my game stopped. Here are my lines and the full error. Explain the cause first. Then show the smallest fix that keeps the game running. [code `examples/ex04_word_crash.py`]
- **Narration:** The AI names line 3. Int cannot convert the word seven. The fix: keep the answer as text, check it first, and only then convert it.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: A customer typed seven, and my game stopped. Here are my lines and the full error. Explain the cause first. Then show the smallest fix that keeps the game running. [code `examples/ex04_word_crash.py`]
    - AI (example answer): Line 3 converts the answer with `int()` at once. `int()` cannot turn the text 'seven' into a number, so Python raises a `ValueError`. The fix: keep the answer as text, check it first, and call `int()` only when every character is a digit.
- **Narration:** Step 4: the check. The string method is digit gives True only when the text has at least one character, and every character is a digit.
  **On screen:** Code `examples/ex05_isdigit.py`, line 2 highlighted, output hidden
- **Narration:** So no letters, no minus sign, no decimal point, and no spaces. An empty answer has no characters at all.
  **On screen:** Code `examples/ex05_isdigit.py`, line 3, 4, 5, 6, 7 highlighted, output hidden
- **Narration:** Line 8 removes the space with strip from Chapter 3 first, then checks.
  **On screen:** Code `examples/ex05_isdigit.py`, line 8 highlighted, output hidden
- **Interaction:** "Which of lines 2 to 8 print `True`?" stays on screen with a 10-second timer.
- **Narration:** Only two. Line 2, the text 12. And line 8, where strip removed the space first.
  **On screen:** Code `examples/ex05_isdigit.py`, line 2, 8 highlighted, output `examples/ex05_isdigit.expected`
- **Narration:** Line 7 is the surprise: a space before the 7 is enough to give False.
  **On screen:** Code `examples/ex05_isdigit.py`, line 7 highlighted, output `examples/ex05_isdigit.expected`

## Scene 10: Step 5: Check, then convert (10:13 to 10:57)

**Section:** Build it step by step

**Direction:** The check ladder: is digit, then range, then int. Ask what happens with seven, reveal.

- **Narration:** Step 5 puts the check in order. Line 2 reads the answer and strips the spaces. It stays text.
  **On screen:** Code `examples/ex06_check.py`, line 2 highlighted, output hidden
- **Narration:** Line 3: if it is not all digits, line 4 asks for a whole number.
  **On screen:** Code `examples/ex06_check.py`, line 3, 4 highlighted, output hidden
- **Narration:** Line 5: if it is outside 1 to 20, line 6 says so. Line 5 can safely call int, because line 3 already found that the answer is made of digits.
  **On screen:** Code `examples/ex06_check.py`, line 5, 6 highlighted, output hidden
- **Narration:** Only a fair answer reaches the else, where line 8 converts it.
  **On screen:** Code `examples/ex06_check.py`, line 7, 8, 9 highlighted, output hidden
- **Interaction:** "The customer types `seven`. Which line prints, and does `int()` ever see the word?" stays on screen with a 10-second timer.
- **Narration:** Line 4 prints: please type a whole number. And int never sees the word, so nothing crashes.
  **On screen:** Code `examples/ex06_check.py`, line 3, 4 highlighted, output `examples/ex06_check.expected`

## Scene 11: Step 6: Put it together (10:57 to 12:14)

**Section:** Build it step by step

**Direction:** Walk the complete game in groups, ask about an answer of 0, then a breather.

- **Narration:** Step 6: the complete game. Lines 2 to 5 set it up: the module, the header with the rules, the secret and the counter. In the real game, line 4 is random dot rand int, 1 comma 20. Here it is fixed at 7, so you can follow one run.
  **On screen:** Code `examples/test_high_low.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** Line 6 is the loop from step 2. Line 7 reads and strips the answer.
  **On screen:** Code `examples/test_high_low.py`, line 6, 7 highlighted, output hidden
- **Narration:** Lines 8 to 11 are the checks from step 5.
  **On screen:** Code `examples/test_high_low.py`, line 8, 9, 10, 11 highlighted, output hidden
- **Narration:** Only a fair guess reaches line 14, so only a fair guess counts as a try.
  **On screen:** Code `examples/test_high_low.py`, line 12, 13, 14 highlighted, output hidden
- **Narration:** Lines 15 to 21 are the win and the hints from step 2, and lines 22 and 23 run after the loop.
  **On screen:** Code `examples/test_high_low.py`, line 15, 16, 17, 18, 19, 20, 21, 22, 23 highlighted, output hidden
- **Interaction:** "A player types `0`. Does it count as a try?" stays on screen with a 10-second timer.
- **Narration:** No. 0 is all digits, so it passes line 8. But it is less than 1, so line 11 prints the message. Line 14 never runs, so the try is not counted.
  **On screen:** Code `examples/test_high_low.py`, line 10, 11, 14 highlighted, output hidden
- **Narration:** Breather. Relax your hands. The game is built.
  **On screen:** Breather card
    - Check, then convert.
    - Only a fair guess counts as a try.
    - The game is built.
- **Narration:** But criterion five says: test it. And a random secret makes testing hard.
  **On screen:** Breather card
    - Check, then convert.
    - Only a fair guess counts as a try.
    - The game is built.
- **Breather:** 4 quiet seconds.

## Scene 12: Test it (12:14 to 14:12)

**Section:** Test it

**Direction:** Explain the fixed-secret copies, the case table with pass marks revealed row by row, then two predictions with their real runs.

- **Narration:** How do you test a random game? If the secret changes every run, you cannot know the right result. So each test is a copy of the game, where line 4 sets a fixed secret, such as 7, and has its own typed answers.
  **On screen:** How do you test a random game?
- **Narration:** Asha writes six tests, each with the result she expects.
  **On screen:** Table: Six tests with known results
- **Narration:** A win on the first try.
  **On screen:** Table: Six tests with known results (row 1 in focus)
- **Narration:** The high, low, win game you saw at the start.
  **On screen:** Table: Six tests with known results (row 2 in focus)
- **Narration:** Words and an empty answer, which must not count as tries.
  **On screen:** Table: Six tests with known results (row 3 in focus)
- **Narration:** Five wrong guesses, to reach the end of the tries.
  **On screen:** Table: Six tests with known results (row 4 in focus)
- **Narration:** And the boundary values. The largest secret, 20, with the answers 0 and 21 outside the jar.
  **On screen:** Table: Six tests with known results (row 5 in focus)
- **Narration:** And the smallest secret, 1.
  **On screen:** Table: Six tests with known results (row 6 in focus)
- **Narration:** Test 3. The secret is 7. The player presses enter with no answer, then types seven, then 7.
  **On screen:** Code `examples/test_words.py`, line 4 highlighted, output hidden
- **Interaction:** "What number does the last line show for Tries?" stays on screen with a 10-second timer.
- **Narration:** One. The empty answer and the word each got a message, and only the 7 counted. Pass!
  **On screen:** Code `examples/test_words.py`, line 4 highlighted, output `examples/test_words.expected`
- **Narration:** Test 4. The secret is 7, and the player guesses 1, 2, 3, 4 and 5.
  **On screen:** Code `examples/test_out_of_tries.py`, line 4 highlighted, output hidden
- **Interaction:** "What is the last line of this game?" stays on screen with a 10-second timer.
- **Narration:** Out of tries. It was 7. The tries left counted down to 0, and the loop stopped after the fifth guess. Pass!
  **On screen:** Code `examples/test_out_of_tries.py`, line 4 highlighted, output `examples/test_out_of_tries.expected`
- **Narration:** Test 5. The secret is 20. Answers 0 and 21 are outside the jar, so each gets a message.
  **On screen:** Code `examples/test_edges.py`, line 4 highlighted, output `examples/test_edges.expected`
- **Narration:** Remember the question about 0 in step 6? Here is the proof: 0 got a message, and did not count as a try.
  **On screen:** Code `examples/test_edges.py`, line 4 highlighted, output `examples/test_edges.expected`
- **Narration:** Then 20. Correct, with one guess used. Pass!
  **On screen:** Code `examples/test_edges.py`, line 4 highlighted, output `examples/test_edges.expected`
- **Narration:** Test 6. The secret is 1, and the player guesses 1. Correct. Pass! All six tests match their expected results.
  **On screen:** Code `examples/test_one.py`, line 4 highlighted, output `examples/test_one.expected`

## Scene 13: Improve it with AI (14:12 to 15:55)

**Section:** Improve it with AI

**Direction:** Stage 6: the AI suggests removing strip. The learner judges it from step 4, then the test on its own screen. Then the six stages, a quiz and a breather.

- **Narration:** Stage 6: improve. All six tests pass. Asha asks for a readability review, and says: do not change what it prints, or which answers it accepts.
  **On screen:** AI chat, stage 6: Improve: a shorter line?
    - You: All six tests pass. Review my game for readability. Suggest at most two changes, each with one reason. Do not change what it prints or which answers it accepts. [code `examples/test_high_low.py`]
- **Narration:** The AI suggests removing strip from line 7. It says is digit already ignores spaces.
  **On screen:** AI chat, stage 6: Improve: a shorter line?
    - You: All six tests pass. Review my game for readability. Suggest at most two changes, each with one reason. Do not change what it prints or which answers it accepts. [code `examples/test_high_low.py`]
    - AI (example answer): One change: remove `.strip()` from line 7. `isdigit()` already ignores spaces, so the line is shorter and works the same.
- **Interaction:** "The AI says `isdigit()` already ignores spaces. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. In step 4, a space before the 7 gave False. Asha tests the suggestion anyway, with an easy typing slip: 7, with a space after it.
  **On screen:** AI chat, stage 6: Improve: a shorter line?
    - You: All six tests pass. Review my game for readability. Suggest at most two changes, each with one reason. Do not change what it prints or which answers it accepts. [code `examples/test_high_low.py`]
    - AI (example answer): One change: remove `.strip()` from line 7. `isdigit()` already ignores spaces, so the line is shorter and works the same.
- **Narration:** Line 7 has no strip now. The player types 7, with a space after it.
  **On screen:** Code `examples/ai_no_strip.py`, line 7 highlighted, output `examples/ai_no_strip.expected`
- **Narration:** Please type a whole number! The answer looks exactly like 7, and the game rejects it.
  **On screen:** Code `examples/ai_no_strip.py`, line 7 highlighted, output `examples/ai_no_strip.expected`
- **Narration:** The suggestion changed which answers the game accepts, and Asha said not to. She keeps strip.
  **On screen:** Code `examples/ai_no_strip.py`, line 7 highlighted, output `examples/ai_no_strip.expected`
- **Narration:** Here are all six stages on one game.
  **On screen:** Table: Six stages while building one game
- **Narration:** The AI helped at every stage.
  **On screen:** Table: Six stages while building one game (row 1 in focus)
- **Narration:** And it was confidently wrong twice: the secret line, and the spaces.
  **On screen:** Table: Six stages while building one game (row 3 in focus)
- **Narration:** Both times, a test with a known result caught it.
  **On screen:** Table: Six stages while building one game (row 6 in focus)
- **Narration:** Quick check. How do you test a game whose secret is random?
  **On screen:** Quick check: "How do you test a game whose secret is random?" (options shown)
- **Interaction:** "How do you test a game whose secret is random?" stays on screen with a 10-second timer.
- **Narration:** A. Fix the secret in a test copy, then run answers with known results. Exactly what Asha did.
  **On screen:** Quick check: "How do you test a game whose secret is random?" (answer revealed: Fix the secret in a test copy)
- **Narration:** Last breather. You built a game that handles every answer, and you made the decisions.
  **On screen:** Breather card
    - AI helped at all six stages.
    - It was wrong twice, and sounded sure.
    - Tests with known results caught both.
- **Narration:** Let's recap.
  **On screen:** Breather card
    - AI helped at all six stages.
    - It was wrong twice, and sounded sure.
    - Tests with known results caught both.
- **Breather:** 4 quiet seconds.

## Scene 14: Recap (15:55 to 17:23)

**Section:** Recap

**Direction:** Recap points one by one, a final quiz, the badge and the practice table.

- **Narration:** Here is what you used in this boss level.
  **On screen:** Recap
- **Narration:** Import loads a module, and rand int includes both ends.
  **On screen:** Recap
    - `import random` loads a module. `randint(1, 20)` includes both ends.
- **Narration:** Rand range stops before its end value, like range.
  **On screen:** Recap
    - `import random` loads a module. `randint(1, 20)` includes both ends.
    - `randrange()` stops before its end value, like `range()`.
- **Narration:** A seed repeats the same numbers. Use it for tests, not for real games.
  **On screen:** Recap
    - `import random` loads a module. `randint(1, 20)` includes both ends.
    - `randrange()` stops before its end value, like `range()`.
    - A seed repeats the same numbers: for tests, not for real games.
- **Narration:** Check, then convert: strip, is digit, a range check, and only then int.
  **On screen:** Recap
    - `import random` loads a module. `randint(1, 20)` includes both ends.
    - `randrange()` stops before its end value, like `range()`.
    - A seed repeats the same numbers: for tests, not for real games.
    - Check, then convert: `strip()`, `isdigit()`, a range check, then `int()`.
- **Narration:** And test a random program by fixing its random part.
  **On screen:** Recap
    - `import random` loads a module. `randint(1, 20)` includes both ends.
    - `randrange()` stops before its end value, like `range()`.
    - A seed repeats the same numbers: for tests, not for real games.
    - Check, then convert: `strip()`, `isdigit()`, a range check, then `int()`.
    - Test a random program by fixing its random part.
- **Narration:** One last check. A player types 15, with spaces around it. The secret is 9. What does the game print?
  **On screen:** Quick check: "A player types ` 15 ` with spaces around it. The secret is 9. What does the game print?" (options shown)
- **Interaction:** "A player types ` 15 ` with spaces around it. The secret is 9. What does the game print?" stays on screen with a 10-second timer.
- **Narration:** C. Strip removes the spaces, so 15 passes both checks. It is the first fair guess, and it is higher than 9. Too high, four tries left.
  **On screen:** Quick check: "A player types ` 15 ` with spaces around it. The secret is 9. What does the game print?" (answer revealed: Too high! Tries left: 4)
- **Narration:** Boss level complete! You earned 300 XP and the Game Maker badge. And Module 2 is done.
  **On screen:** Game Maker You earned 300 XP. Module 2 is complete.
- **Breather:** 2 quiet seconds.
- **Narration:** The practice file has eight more tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-ups, worth 10 XP each, including two dice.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, such as three tries for a PIN.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's game by counting how many times it asks for a guess.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Write down the expected result before you run each one.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 15: What's next (17:23 to 17:47)

**Section:** What's next

**Direction:** End card. Tease lists as the way to remember every guess. Hold quietly at the end.

- **Narration:** Asha's game forgets each guess as soon as the next one arrives. At the end, it cannot show the player all five guesses.
  **On screen:** Lists: Keeping Many Values in Order One name, many values.
- **Narration:** In Chapter 11, you will learn lists: one variable that keeps many values in order. Then the game can remember every guess.
  **On screen:** Lists: Keeping Many Values in Order One name, many values.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Lists: Keeping Many Values in Order Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 11.
  **On screen:** Lists: Keeping Many Values in Order Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
