# AI Prompt Cards: Chapter 26

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data, such as a real list of customers. Run every class the AI writes, and test it with your own cases before you trust it.

## Plan: Ask for a design, not code

**Prompt:** "I am a beginner learning Python classes. I want to model <describe the thing, for example: a cafe loyalty card with one stamp per drink and a free tea for every 10 stamps>. Do not write code yet. List the attributes each object should store and the methods it needs. Give each method one job, in one sentence."

**Use it when:** you know what you want to model but not which data to store.

**A good answer:** a short list of attributes, such as `customer` and `stamps`, and methods that each do one job, such as `add_stamp()` and `free_teas()`.

**Check it:** cross out any method that prints, saves a file or sends a message as well as calculating; each of those is a separate job. If an attribute can be worked out from other attributes, it should be a method instead.

## Write: Write your own class first

**Prompt:** "I wrote this class myself: <paste it>. Do not change it. Predict exactly what the last line prints, and explain which line of my class each part of the output comes from."

**Use it when:** you have written a small class and want to check your understanding of `self` and attributes.

**A good answer:** the exact output, with each value traced to an attribute set in `__init__` or changed by a method.

**Check it:** write your own prediction first, then run the code. Compare all three: your prediction, the AI's prediction and the real output.

## Generate: Ask for one method with an exact example

**Prompt:** "Add one method to my class: <describe it>. Keep my attributes and methods as they are. Tell me exactly what it returns for <an example object, such as a card with 25 stamps>."

**Use it when:** you want to add one behaviour to a class you understand.

**A good answer:** one new method, using only the attributes the class already has, with the exact result for your example.

**Check it:** run the example and compare the real result with the AI's claim. Look for a new attribute that stores a number: it may go stale when another method changes the data.

## Test: Cases with expected results

**Prompt:** "Here is my class: <paste it>. Suggest test cases for <the method>, each with the starting values and the exact expected result. Include an object that is created with data already in it."

**Use it when:** your class works for one example and you want to know if it works for others.

**A good answer:** four to six cases, including a boundary such as exactly 10 stamps and an object created with old data, each with an expected result.

**Check it:** write each case in a small test loop or a pytest file, and run every case. A case that fails shows where the design is wrong.

## Debug: The cause before the fix

**Prompt:** "I am a beginner. I ran this code: <paste the code>. I got this exact error: <paste the full error report>. First explain what the error means and which line causes it. Then show the smallest fix."

**Use it when:** you get a `TypeError` or `AttributeError` from your class and do not understand it.

**A good answer:** it names the method or attribute, explains the message in plain words (for example, a method with no parameter for `self`), and shows a one-line fix.

**Check it:** apply the fix, run the program, and then run all your test cases again.

## Improve: Test the suggestion with two objects

**Prompt:** "Review my class for clarity. Suggest at most two improvements, each with a one-sentence reason. Do not change what my existing methods return: <paste your class>."

**Use it when:** your class works and passes its tests.

**A good answer:** small, specific suggestions with reasons, such as a clearer method name or a readable `__str__`.

**Check it:** apply one suggestion at a time. Create two objects and check that changing one does not change the other. Then run every test again.
