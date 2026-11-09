# AI Prompt Cards: Chapter 4

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data. Always run the code yourself. The real output decides who is right, not the AI.

## Plan: Decide the questions and their types

**Prompt:** "I am a beginner learning Python input(). I want a program that <describe it, for example: asks for the price of a cake and how many cakes, then prints the total>. Do not write code yet. List each question the program asks, the exact prompt text, and whether the answer should stay a string or become an int or a float, with one reason for each."

**Use it when:** you know what your program should do but not which answers need converting.

**A good answer:** one line per question, with the prompt text and a type: `int` for counts, `float` for amounts of money, and a string for names.

**Check it:** every number your program calculates with must come from an answer that is converted. A name that is only printed can stay a string.

## Write: Explain a line from the inside out

**Prompt:** "Here is one line of my Python code: <paste the line, for example: tea_count = int(input("How many teas? "))>. Do not change it. Explain, step by step, in which order Python works it out and what value exists after each step, including its type."

**Use it when:** you wrote a line with one function inside another and want to check that you understand it.

**A good answer:** the inner function first (`input()` shows the prompt and gives back a string), then the outer function (`int()` makes a number), then the assignment.

**Check it:** run the line, then print the variable and its type with `print(tea_count, type(tea_count))`. The type must match the explanation.

## Generate: Fix the prompt text and one typed answer

**Prompt:** "Write a short Python program for a beginner. Use only variables, input(), int(), float(), f-strings and print(). Use these variable names: <list the names>. Use this exact prompt text: <paste it>. If I type <an answer>, it must print exactly: <paste the exact output>. Show the code, then the output for that answer."

**Use it when:** you want a model program that asks a question and calculates with the answer.

**A good answer:** short code that converts every answer it calculates with, and output that matches your target character by character.

**Check it:** run the code and type the same answer. If it stops with an error, use the Debug card. If it prints something different, compare every character.

## Test: Ask for answers that could break it

**Prompt:** "Here is my program: <paste the code>. Suggest four answers to type when it asks <the question>: a whole number, a decimal number, a number with spaces around it and a word. For each answer, tell me whether the program prints a result or stops with an error, and why."

**Use it when:** your program works with one answer and you want to know what happens with others.

**A good answer:** four answers, each with a predicted result, and a note that a word such as `two` stops `int()` and `float()` with a `ValueError`.

**Check it:** run the program four times and type each answer. Mark each AI prediction as right or wrong.

## Debug: Find the cause before the fix

**Prompt:** "I am a beginner. I ran this Python code: <paste the code>. I typed: <the answer you typed>. I got this exact error: <paste the full error message>. First explain what the error means and which line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** you get a `TypeError` or `ValueError` after typing an answer.

**A good answer:** it names the error type and the line, explains that `input()` gives back a string or that the text cannot be converted, and shows a one-line fix.

**Check it:** apply the fix and run the program with the same answer. Then read the original error again and confirm that the explanation matches it.

## Improve: Ask for a simpler version, then test it

**Prompt:** "Review my Python program for readability. Suggest at most two improvements, each with a one-sentence reason. Do not change what the program prints for any answer: <paste your code>."

**Use it when:** your program works and you want cleaner code.

**A good answer:** a short list of changes, such as clearer prompt text or clearer names, each with a reason.

**Check it:** apply one suggestion at a time. Run the program with at least two kinds of answers, such as `30` and `25.50`. The output must stay the same for both.
