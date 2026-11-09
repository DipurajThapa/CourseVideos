# AI Prompt Cards: Chapter 1

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private information. Always run the code yourself and compare the output with what you asked for.

## Plan: Break the task into steps first

**Prompt:** "I am a beginner learning Python. I want a program that prints a four-line welcome card for my study group: a border, a title, a date and a border. List the steps in plain English. Do not write any code yet."

**Use it when:** you know what you want to see but not how to start.

**A good answer:** a short numbered list, one step per line of output, in the same order as the card.

**Check it:** each step matches one `print()` you could write. If a step is unclear, ask the AI to explain it in one sentence.

## Write: Write it yourself, then ask for an explanation

**Prompt:** "Here is my Python code: <paste your code>. Do not rewrite it. Explain what each line does in one simple sentence, and tell me if it prints exactly this: <paste the output you want>."

**Use it when:** you have written a program and want to confirm you understand every line.

**A good answer:** one sentence per line, in order, and a clear yes or no about the output, with the reason.

**Check it:** run your program. If the AI said yes but the output differs, the AI was wrong. Trust the real output.

## Generate: Ask for code that produces an exact output

**Prompt:** "Write Python code that uses only the print() function. It must output exactly these lines, with the same spaces and symbols: <paste the exact output>. Show the code, then show the output it produces."

**Use it when:** you want an example to learn from, or you are stuck on spacing.

**A good answer:** short code with one `print()` per line of output, and no features you have not learned yet.

**Check it:** run the code and compare every character, including spaces, with your target. This is how the date flaw in this chapter was caught.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error message>. First explain what the error means and which line causes it. Then show the smallest fix."

**Use it when:** your program stops with an error and you do not understand the message.

**A good answer:** it names the error type, points to the exact line and explains the cause before it shows a one-line fix.

**Check it:** apply the fix and run the program. Then read the original error again and confirm the explanation matches it.

## Test: Compare expected and real output

**Prompt:** "This is the output I expected: <paste>. This is the output my program printed: <paste>. List every difference, character by character, including spaces, line breaks and capital letters."

**Use it when:** the program runs but the output looks slightly wrong.

**A good answer:** a precise list of differences, such as "line 2 has a space where you expected a hyphen".

**Check it:** fix one difference at a time and run the program after each change.

## Improve: Ask for a short, reasoned review

**Prompt:** "Review my Python program for readability. Suggest at most two improvements. For each one, explain in one sentence why it helps a reader. Do not change what the program prints: <paste your code>."

**Use it when:** your program works and you want to learn better habits.

**A good answer:** two specific suggestions with reasons, and no change to the output.

**Check it:** apply only the suggestions you understand. Run the program and confirm the output is the same as before.
