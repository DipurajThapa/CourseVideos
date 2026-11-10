# Chapter 10: Boss Level 2: The Number Guessing Game

> Quest: build a guessing game that picks a secret number, gives hints, counts the tries and never crashes, whatever the player types. Reward: 300 XP and the **Game Maker** badge.

## The mission

The Corner Cafe has a glass jar of biscuits on the counter. Asha wants a game for the customers: guess how many biscuits are in the jar, from 1 to 20, and win a free tea. Each customer gets five guesses, with a hint after each one.

At the end of Chapter 9, Asha's report still trusted every answer. A customer who types a word instead of a number makes a program like that crash. This game must handle every answer: numbers that are too low or too high, numbers outside 1 to 20, words and empty answers.

This boss level uses everything from Chapters 6 to 9, and one new tool:

| Chapter | What you use from it |
|---|---|
| 6 | `if`, `elif` and `else`, comparisons, `and`, `or` and `not` |
| 7 | A `while` loop with a counter, `+=` and `break` |
| 8 | A `for` loop with `range()`, to run a test many times |
| 9 | Reading an error report, and testing with known results |
| New | `import random` and `random.randint()`, to pick the secret number |

## What you will build

A program called `guessing_game.py`. Here is one game. The secret was 7, and the text after each question is what the player typed.

<!-- output: examples/test_high_low.expected -->
```output
BISCUIT JAR: guess 1 to 20. Five tries!
Your guess: 12
Too high! Tries left: 4
Your guess: 3
Too low! Tries left: 3
Your guess: 7
Correct! Free tea! Tries: 3
```

## Acceptance criteria

Your game is finished when all of these are true:

1. It picks a secret number from 1 to 20, and every number from 1 to 20 can be picked.
2. After each guess, it says `Too low!` or `Too high!` and how many tries are left.
3. It stops after a correct guess or after five guesses, and it tells the player the secret.
4. A word, an empty answer or a number outside 1 to 20 gets a clear message, does not count as a try and never crashes the program.
5. You tested it with at least six cases whose results you knew in advance, including the smallest and largest allowed answers.

## Plan it with AI

Asha planned the rules before any code. She asked an AI assistant:

> "I am a beginner. I know variables, input, int, if, elif and else, while loops with break, and for loops with range. I want to build a number guessing game with a secret from 1 to 20 and five tries. Do not write code. List the rules of the game, the values the program must remember, and what happens after each kind of answer."

An example answer looked like this:

> Values to remember: the secret number, the number of tries used, and whether the player has won.
> Each turn: read a guess. If it is lower than the secret, say "Too low". If it is higher, say "Too high". If it is equal, the player wins and the game stops.
> The game also stops after five tries, and then it shows the secret.

The plan covers numbers, but not every answer. Asha played the game on paper and typed a word: the plan had no rule for it. She added two rules. An answer that is not a whole number gets a message. A number outside 1 to 20 gets a message. Neither one counts as a try.

## Build it step by step

**Step 1: One guess, three answers.** Start with a fixed secret, so you know what each guess should print.

```python
# file: examples/ex02_one_guess.py
secret = 7
guess = int(input("Your guess: "))
if guess == secret:
    print("Correct!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")
```

<!-- output: examples/ex02_one_guess.expected -->
```output
Your guess: 12
Too high!
```

Each guess goes down exactly one branch. 12 is not equal to 7 and not lower than 7, so the `else` branch runs.

**Step 2: Five tries.** A `while` loop repeats the guess. The counter `tries` goes up after each guess, and `break` stops the loop when the guess is right. After the loop, line 14 checks the last guess: if it is still wrong, the player ran out of tries.

```python
# file: examples/ex03_tries.py
secret = 7
tries = 0
while tries < 5:
    guess = int(input("Your guess: "))
    tries += 1
    if guess == secret:
        print(f"Correct! Tries: {tries}")
        break
    elif guess < secret:
        print(f"Too low! Tries left: {5 - tries}")
    else:
        print(f"Too high! Tries left: {5 - tries}")
if guess != secret:
    print("Out of tries.")
```

<!-- output: examples/ex03_tries.expected -->
```output
Your guess: 12
Too high! Tries left: 4
Your guess: 3
Too low! Tries left: 3
Your guess: 7
Correct! Tries: 3
```

The loop condition `tries < 5` is true for tries 0 to 4, so the player gets exactly five guesses.

**Step 3: A random secret.** A **module** is a file of ready-made Python code. The line `import random` loads the `random` module, and then `random.randint(1, 20)` picks a whole number from 1 to 20. Both ends are included: 1 and 20 can both be picked. The module also has `random.randrange()`, which works like `range()` from Chapter 8: it stops before its end value. You will learn more about modules in Chapter 18.

Random numbers are hard to test, because each run is different. For a test, `random.seed()` makes the same "random" numbers on every run:

```python
# file: examples/ex01_random.py
import random
random.seed(3)
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
```

<!-- output: examples/ex01_random.expected -->
```output
8
19
18
```

Run it twice, and you get 8, 19 and 18 both times. Delete line 3, and the numbers change on every run. A real game has no seed.

**Step 4: A word crashes the game.** `int()` can only convert text that looks like a whole number. Asha typed `seven`:

```python
# file: examples/ex04_word_crash.py
secret = 7
guess = int(input("Your guess: "))
print("You guessed", guess)
```

<!-- error: examples/ex04_word_crash.expected_error -->
```output
Your guess: seven
Traceback (most recent call last):
  File "ex04_word_crash.py", line 3, in <module>
    guess = int(input("Your guess: "))
ValueError: invalid literal for int() with base 10: 'seven'
```

You met this `ValueError` in Chapter 4. The fix is to check the answer before converting it. The string method `isdigit()` gives `True` only when the text has at least one character and every character is a digit.

```python
# file: examples/ex05_isdigit.py
print("12".isdigit())
print("seven".isdigit())
print("".isdigit())
print("-3".isdigit())
print("7.5".isdigit())
print(" 7".isdigit())
print(" 7".strip().isdigit())
```

<!-- output: examples/ex05_isdigit.expected -->
```output
True
False
False
False
False
False
True
```

An empty answer, a minus sign, a decimal point and a space all give `False`. Line 8 removes the space with `strip()` from Chapter 3 first, so `" 7"` becomes `"7"` and passes.

**Step 5: Check, then convert.** The answer stays text until it passes both checks. Only then does `int()` turn it into a number.

```python
# file: examples/ex06_check.py
answer = input("Your guess: ").strip()
if not answer.isdigit():
    print("Please type a whole number, like 12.")
elif int(answer) < 1 or int(answer) > 20:
    print("The jar holds 1 to 20 biscuits.")
else:
    guess = int(answer)
    print("A fair guess:", guess)
```

<!-- output: examples/ex06_check.expected -->
```output
Your guess: seven
Please type a whole number, like 12.
```

The order matters. Line 5 calls `int(answer)`, and it only runs when line 3 has already found that the answer is all digits.

**Step 6: Put it together.** Here is the complete game.

```python
# file: project/guessing_game.py
import random
print("BISCUIT JAR: guess 1 to 20. Five tries!")
secret = random.randint(1, 20)
tries = 0
while tries < 5:
    answer = input("Your guess: ").strip()
    if not answer.isdigit():
        print("Please type a whole number, like 12.")
    elif int(answer) < 1 or int(answer) > 20:
        print("The jar holds 1 to 20 biscuits.")
    else:
        guess = int(answer)
        tries += 1
        if guess == secret:
            print(f"Correct! Free tea! Tries: {tries}")
            break
        elif guess < secret:
            print(f"Too low! Tries left: {5 - tries}")
        else:
            print(f"Too high! Tries left: {5 - tries}")
if guess != secret:
    print(f"Out of tries. It was {secret}.")
```

Lines 3 to 5 set up the game. Lines 8 to 11 reject an answer that is not a whole number or not from 1 to 20. Only a fair guess reaches line 14, so only a fair guess counts as a try. Lines 22 and 23 run after the loop: if the last guess was wrong, the player ran out of tries.

## Test it

A random secret makes a game impossible to test: you cannot know the right result in advance. So each test is a copy of the game with one change. Line 4 sets a fixed secret, such as `secret = 7  # fixed for this test`. Every other line is the same. Each test also has its own typed answers.

| Test | Secret | Answers typed | Expected last line | Result |
|---|---|---|---|---|
| Win first try | 7 | 7 | `Correct! Free tea! Tries: 1` | Pass |
| Too high, too low, win | 7 | 12, 3, 7 | `Correct! Free tea! Tries: 3` | Pass |
| Words and an empty answer | 7 | (empty), seven, 7 | `Correct! Free tea! Tries: 1` | Pass |
| Out of tries | 7 | 1, 2, 3, 4, 5 | `Out of tries. It was 7.` | Pass |
| Largest secret, outside answers | 20 | 0, 21, 20 | `Correct! Free tea! Tries: 1` | Pass |
| Smallest secret | 1 | 1 | `Correct! Free tea! Tries: 1` | Pass |

Here are two of the runs. The words did not count as tries:

<!-- output: examples/test_words.expected -->
```output
BISCUIT JAR: guess 1 to 20. Five tries!
Your guess: 
Please type a whole number, like 12.
Your guess: seven
Please type a whole number, like 12.
Your guess: 7
Correct! Free tea! Tries: 1
```

<!-- output: examples/test_out_of_tries.expected -->
```output
BISCUIT JAR: guess 1 to 20. Five tries!
Your guess: 1
Too low! Tries left: 4
Your guess: 2
Too low! Tries left: 3
Your guess: 3
Too low! Tries left: 2
Your guess: 4
Too low! Tries left: 1
Your guess: 5
Too low! Tries left: 0
Out of tries. It was 7.
```

**AI pair moment.** While she built Step 3, Asha asked an AI assistant: "Write one line of Python that picks a random whole number from 1 to 20, including both. Name the variable secret." The AI answered `secret = random.randrange(1, 20)` and said it picks every number from 1 to 20. Asha remembered that `randrange()` stops before its end value, like `range()`. She tested the line 10,000 times and printed the lowest and highest numbers it picked. The seed on line 3 makes the test give the same result on every run:

```python
# file: examples/ai_secret_flawed.py
import random
random.seed(1)
lowest = 20
highest = 1
for draw in range(10000):
    secret = random.randrange(1, 20)
    if secret < lowest:
        lowest = secret
    if secret > highest:
        highest = secret
print("Lowest:", lowest)
print("Highest:", highest)
```

<!-- output: examples/ai_secret_flawed.expected -->
```output
Lowest: 1
Highest: 19
```

In 10,000 draws, 20 never appeared. A customer could never win with a jar of 20 biscuits. With `randint(1, 20)`, both ends appear:

```python
# file: examples/ai_secret_fixed.py
import random
random.seed(1)
lowest = 20
highest = 1
for draw in range(10000):
    secret = random.randint(1, 20)
    if secret < lowest:
        lowest = secret
    if secret > highest:
        highest = secret
print("Lowest:", lowest)
print("Highest:", highest)
```

<!-- output: examples/ai_secret_fixed.expected -->
```output
Lowest: 1
Highest: 20
```

## Improve it with AI

When all six tests passed, Asha asked an AI assistant: "Review my game for readability. Suggest at most two changes, each with one reason. Do not change what it prints or which answers it accepts." One suggestion was to remove `.strip()` from line 7, "because `isdigit()` already ignores spaces". Step 4 showed that `" 7".isdigit()` is `False`, so Asha tested the suggestion before accepting it. Phone keyboards often add a space after a word, so she typed `7` with a space after it:

<!-- output: examples/ai_no_strip.expected -->
```output
BISCUIT JAR: guess 1 to 20. Five tries!
Your guess: 7 
Please type a whole number, like 12.
Your guess: 7
Correct! Free tea! Tries: 1
```

Without `.strip()`, the game rejected an answer that looks exactly like 7. The suggestion changed which answers the game accepts, which Asha had said not to do. She kept `.strip()`.

These are the six ways AI helped with this project. The full prompts are in [ai-prompts.md](ai-prompts.md).

| Stage | How AI helped |
|---|---|
| Plan | Listed the rules and the values to remember, before any code. |
| Write | Said which message each guess gets in Asha's own `if`, `elif` and `else` code. |
| Generate | Wrote the secret-number line, with a confident mistake: `randrange(1, 20)`. |
| Test | Helped list cases with expected results, and a loop that proved 20 was never picked. |
| Debug | Explained the `ValueError` from a typed word before suggesting the check. |
| Improve | Suggested removing `.strip()`, which a test showed would reject `7` with a space. |

## Recap

- `import random` loads a module, and `random.randint(1, 20)` picks a whole number with both ends included. `randrange()` stops before its end value, like `range()`.
- `random.seed()` makes the same numbers on every run. Use it for tests, not for real games.
- Check an answer before converting it: `strip()`, then `isdigit()`, then a range check, then `int()`.
- A `while` loop with a counter and `break` runs a game with limited tries.
- Test a random program by fixing its random part, then run every case with a known result.

You earned **300 XP** and the **Game Maker** badge. Module 2 is complete.

The practice tasks for this chapter are in [practice/practice.md](practice/practice.md).

## What's next

In Chapter 11, you will learn lists: one variable that keeps many values in order, so the game can remember and show every guess the player made.
