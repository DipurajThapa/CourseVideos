# Video Script: Chapter 16: Functions: Reusable Blocks of Logic

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:32 (estimate, not rendered yet).

## Scene 1: Introduction

**Section:** Introduction

**Direction:** Open on Asha's three copies of the summary code and the missed fix, in her words. Then the title with the AI tease, then the day report as the mission, with no output yet.

- **Narration:** At the Corner Cafe, Asha wanted a summary for three days. So she copied the same lines three times.
  **On screen:** The same lines, three times
- **Narration:** Then she found a mistake. She fixed it in two copies, and missed the third. Copying code means copying its mistakes.
  **On screen:** The same lines, three times
- **Narration:** This is Code Quest, Chapter 16: functions. Write it once, use it many times.
  **On screen:** Functions: Reusable Blocks of Logic
- **Narration:** And an AI assistant will write a function for Asha, and promise exactly what it prints. Your checks will decide.
  **On screen:** Functions: Reusable Blocks of Logic Write it once. Name it. Test it.
- **Narration:** So here is today's mission: the day report. Three small functions, each with one job.
  **On screen:** Code `examples/ex08_day_report.py`, line 2, 6, 13 highlighted, output hidden
- **Narration:** And three short lines at the bottom print a report for three different days.
  **On screen:** Code `examples/ex08_day_report.py`, line 17, 18, 19 highlighted, output hidden
- **Narration:** If the tax changes, Asha edits one line. Let's build it.
  **On screen:** Code `examples/ex08_day_report.py`, output hidden

## Scene 2: Learning goals

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Write and call functions, return values, write docstrings, and read a longer traceback.
  **On screen:** By the end, you will be able to:
    - Write a function with `def`, call it, and give it inputs with parameters.
    - Explain `return` versus `print()`, and recognise `None`.
    - Write a docstring that says what a function does.
    - Read a traceback through several functions, from the bottom up.
- **Narration:** And write a specification, ask an AI for the code, and test it with your own checks.
  **On screen:** By the end, you will be able to:
    - Write a function with `def`, call it, and give it inputs with parameters.
    - Explain `return` versus `print()`, and recognise `None`.
    - Write a docstring that says what a function does.
    - Read a traceback through several functions, from the bottom up.
    - Write a specification, ask AI for the code, and test it with your own checks.

## Scene 3: Why this matters

**Section:** Why this matters

**Direction:** Define a function through Asha's copied code, then connect it to functions the learner already uses.

- **Narration:** A function is a named block of code. You write it once, and run it whenever you need it. Fix a mistake inside it, and every call gets the fix.
  **On screen:** Why this matters
    - A **function** is a named block of code you write once and run whenever you need it.
    - Fix a mistake inside it, and every call gets the fix.
- **Narration:** You have used functions since Chapter 1: print, len, round and input. Now you write your own.
  **On screen:** Why this matters
    - A **function** is a named block of code you write once and run whenever you need it.
    - Fix a mistake inside it, and every call gets the fix.
    - You already use functions: `print()`, `len()`, `round()`, `input()`.
    - Every real program is built from many small functions.

## Scene 4: The idea: define once, call many times

**Section:** The idea

**Direction:** Teach the parts with the diagram, then the five words in a table, then the recipe card and where it stops working. Then a quiz and a breather.

- **Narration:** Here is a whole function. The def line gives it a name, with tax, and one parameter, price.
  **On screen:** One definition, many calls
- **Narration:** The indented line is the body. Return hands a value back to whoever called the function.
  **On screen:** One definition, many calls
- **Narration:** The last line is a call. A value goes in, and the returned value comes out and is stored in tea.
  **On screen:** One definition, many calls
- **Narration:** Five words. To define means to write the function, and nothing runs yet. To call means to run it, with its name and brackets.
  **On screen:** Table: Five words for functions (row 2 in focus)
- **Narration:** A parameter is a name in the def line. An argument is the value you pass in a call.
  **On screen:** Table: Five words for functions (row 4 in focus)
- **Narration:** And the return value is what the function hands back.
  **On screen:** Table: Five words for functions (row 5 in focus)
- **Narration:** Think of a recipe card in the cafe kitchen. The cook follows the same steps every time. Today's ingredients go in, and one dish comes out.
  **On screen:** A recipe card in the kitchen
    - The card has a name and its ingredients. The cook follows the same steps every time.
    - Today's ingredients go in. One dish comes out.
- **Narration:** But unlike a cook, a function cannot taste the dish and adjust it. It does exactly what its body says, every time.
  **On screen:** A recipe card in the kitchen
    - The card has a name and its ingredients. The cook follows the same steps every time.
    - Today's ingredients go in. One dish comes out.
    - Unlike a cook, a function cannot taste and adjust. It does exactly what its body says.
- **Narration:** Quick check. In this def line, what is name?
  **On screen:** Quick check: "In `def greet(name):`, what is `name`?" (options shown)
- **Interaction:** "In `def greet(name):`, what is `name`?" stays on screen with a 10-second timer.
- **Narration:** B. A parameter. It is a name in the def line. The value you pass when you call the function is the argument.
  **On screen:** Quick check: "In `def greet(name):`, what is `name`?" (answer revealed: a parameter)
- **Narration:** Take a breather. Here is what you know so far. Next, Asha writes her first function.
  **On screen:** Breather card
    - `def` defines. A call runs.
    - Parameters receive arguments.
    - `return` hands a value back.
- **Breather:** 4 quiet seconds.

## Scene 5: Steps 1 and 2: Define, call, and pass a value

**Section:** Build it step by step

**Direction:** Teach that defining does not run the body and that each call runs all of it, then ask how many lines appear. Then a parameter, and ask what line 6 prints.

- **Narration:** Step 1. Line 2 defines a function called welcome. It has no parameters, so the brackets are empty.
  **On screen:** Code `examples/ex01_welcome.py`, line 2 highlighted, output hidden
- **Narration:** Lines 3 and 4 are its body, indented by four spaces. Defining the function does not run them.
  **On screen:** Code `examples/ex01_welcome.py`, line 3, 4 highlighted, output hidden
- **Narration:** Lines 6 and 7 are two calls. Each call runs the whole body.
  **On screen:** Code `examples/ex01_welcome.py`, line 6, 7 highlighted, output hidden
- **Interaction:** "How many lines does this program print?" stays on screen with a 10-second timer.
- **Narration:** Four. Each call prints the welcome and the special, so the two lines appear twice.
  **On screen:** Code `examples/ex01_welcome.py`, line 6, 7 highlighted, output `examples/ex01_welcome.expected`
- **Narration:** Step 2. Now the def line has a parameter, name. Line 3 uses it inside an f string.
  **On screen:** Code `examples/ex02_greet.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 5 calls greet with the argument Omar. In that call, name refers to Omar.
  **On screen:** Code `examples/ex02_greet.py`, line 5 highlighted, output hidden
- **Interaction:** "What does line 6 print?" stays on screen with a 10-second timer.
- **Narration:** Hello, Lina! Your tea is ready. In the second call, name refers to Lina.
  **On screen:** Code `examples/ex02_greet.py`, line 6 highlighted, output `examples/ex02_greet.expected`

## Scene 6: Steps 3 and 4: Return, or print?

**Section:** Build it step by step

**Direction:** Teach return with ex03 and ask about lines 7 and 8. Then teach that a function without return gives back None, and ask what line 6 of ex04 prints.

- **Narration:** Step 3. Return ends the function and hands a value back to the line that called it.
  **On screen:** Code `examples/ex03_with_tax.py`, line 3 highlighted, output hidden
- **Narration:** Line 5 stores the returned value in tea, and line 6 prints it.
  **On screen:** Code `examples/ex03_with_tax.py`, line 5, 6 highlighted, output hidden
- **Narration:** Line 7 prints a returned value directly. Line 8 compares one with 3, so it prints True or False.
  **On screen:** Code `examples/ex03_with_tax.py`, line 7, 8 highlighted, output hidden
- **Interaction:** "What do lines 7 and 8 print?" stays on screen with a 10-second timer.
- **Narration:** 4.4, and True. With tax, 2.75 becomes 3.03, which is more than 3.
  **On screen:** Code `examples/ex03_with_tax.py`, line 7, 8 highlighted, output `examples/ex03_with_tax.expected`
- **Narration:** And line 6 prints 3.85, the value stored in tea. A returned value can be stored, printed or compared.
  **On screen:** Code `examples/ex03_with_tax.py`, line 6 highlighted, output `examples/ex03_with_tax.expected`
- **Narration:** Step 4. Print shows a value on the screen. Return hands a value back to the program. They are not the same.
  **On screen:** Code `examples/ex04_print_not_return.py`, line 3 highlighted, output hidden
- **Narration:** A function without return hands back a special value: None. It means no value at all.
  **On screen:** Code `examples/ex04_print_not_return.py`, line 2, 3 highlighted, output hidden
- **Narration:** This function prints the price with tax. Line 5 stores whatever it hands back in result.
  **On screen:** Code `examples/ex04_print_not_return.py`, line 5 highlighted, output hidden
- **Interaction:** "What does line 6 print?" stays on screen with a 10-second timer.
- **Narration:** Result is None. The function printed 3.85 on the screen, but it returned nothing.
  **On screen:** Code `examples/ex04_print_not_return.py`, line 6 highlighted, output `examples/ex04_print_not_return.expected`
- **Narration:** So if the caller needs the value, the function must return it.
  **On screen:** Code `examples/ex04_print_not_return.py`, line 3 highlighted, output `examples/ex04_print_not_return.expected`

## Scene 7: Step 5: Several parameters and a docstring

**Section:** Build it step by step

**Direction:** Teach that arguments fill parameters in order, and the docstring. Ask what line 7 prints. Then a quiz and a breather.

- **Narration:** Step 5. Line 2 has two parameters, separated by a comma: price and count.
  **On screen:** Code `examples/ex05_line_total.py`, line 2 highlighted, output hidden
- **Narration:** Line 3 is a docstring: a string on the first line of the body that says what the function does.
  **On screen:** Code `examples/ex05_line_total.py`, line 3 highlighted, output hidden
- **Narration:** In a call, the arguments fill the parameters in order. The first argument is the price, the second is the count.
  **On screen:** Code `examples/ex05_line_total.py`, line 6 highlighted, output hidden
- **Interaction:** "What does line 7 print?" stays on screen with a 10-second timer.
- **Narration:** 8.25. The price is 2.75, the count is 3, and 2.75 times 3 is 8.25.
  **On screen:** Code `examples/ex05_line_total.py`, line 7 highlighted, output `examples/ex05_line_total.expected`
- **Narration:** And line 8 prints the docstring. Python keeps it under the name doc, with two underscores on each side.
  **On screen:** Code `examples/ex05_line_total.py`, line 8 highlighted, output `examples/ex05_line_total.expected`
- **Narration:** Quick check. The function area is called with 3 and 5. What is height?
  **On screen:** Quick check: "`def area(width, height):` is called as `area(3, 5)`. What is `height`?" (options shown)
- **Interaction:** "`def area(width, height):` is called as `area(3, 5)`. What is `height`?" stays on screen with a 10-second timer.
- **Narration:** D. 5. Arguments fill the parameters in order. Width gets 3, and height gets 5.
  **On screen:** Quick check: "`def area(width, height):` is called as `area(3, 5)`. What is `height`?" (answer revealed: `5`)
- **Narration:** Breather. Relax your shoulders for a moment. Next, functions that call other functions, and what happens when one of them fails.
  **On screen:** Breather card
    - A call runs the whole body.
    - Without `return`, you get `None`.
    - Arguments fill parameters in order.
- **Breather:** 4 quiet seconds.

## Scene 8: Step 6: Functions that call functions

**Section:** Build it step by step

**Direction:** Show day_total calling with_tax. Then the same code with a text price: ask where Python stops, reveal the traceback through three functions, read it bottom-up (Chapter 9 promised this).

- **Narration:** Step 6. A function can call another function. Day total starts a total at 0, on line 6.
  **On screen:** Code `examples/ex06_calls.py`, line 5, 6 highlighted, output `examples/ex06_calls.expected`
- **Narration:** For every price, line 8 calls with tax, and adds the returned value to the total.
  **On screen:** Code `examples/ex06_calls.py`, line 7, 8 highlighted, output `examples/ex06_calls.expected`
- **Narration:** Line 9 returns the total, rounded. Line 11 prints 11.28 for three prices.
  **On screen:** Code `examples/ex06_calls.py`, line 9, 11 highlighted, output `examples/ex06_calls.expected`
- **Narration:** Now line 11 passes a list with one price written as text: 4.0, in quotation marks.
  **On screen:** Code `examples/ex07_traceback.py`, line 11 highlighted, output hidden
- **Narration:** Day total passes each price to with tax, one at a time.
  **On screen:** Code `examples/ex07_traceback.py`, line 8 highlighted, output hidden
- **Interaction:** "In which function will Python stop?" stays on screen with a 10-second timer.
- **Narration:** In with tax, on line 3. Here is the error report. It lists every call on the way, one block for each function.
  **On screen:** Code `examples/ex07_traceback.py`, line 3 highlighted, error `examples/ex07_traceback.expected_error`
- **Narration:** Read it from the bottom up, as in Chapter 9. The last line names the error. The block directly above it shows where it happened: line 3, in with tax.
  **On screen:** Code `examples/ex07_traceback.py`, line 3 highlighted, error `examples/ex07_traceback.expected_error`
- **Narration:** The block above that shows who called it: line 8, in day total. And the top block is line 11, the main program. Most recent call last means the deepest call is at the bottom.
  **On screen:** Code `examples/ex07_traceback.py`, line 11 highlighted, error `examples/ex07_traceback.expected_error`
- **Narration:** The cause is on line 11: the price in quotation marks.
  **On screen:** Code `examples/ex07_traceback.py`, line 11 highlighted, error `examples/ex07_traceback.expected_error`

## Scene 9: See the outcome: the day report

**Section:** See the outcome

**Direction:** Return to the mission. Walk the three functions and their docstrings, ask what line 19 prints, then reveal. Hand over to the AI feature.

- **Narration:** Back to the mission. Each function has one job and a docstring. With tax, on lines 2 to 4, adds the tax to one price.
  **On screen:** Code `examples/ex08_day_report.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Day total, on lines 6 to 11, adds up a whole day. It calls with tax for every price.
  **On screen:** Code `examples/ex08_day_report.py`, line 6, 7, 8, 9, 10, 11 highlighted, output hidden
- **Narration:** Report, on lines 13 to 15, prints one line: the day, the number of sales, and the total from day total.
  **On screen:** Code `examples/ex08_day_report.py`, line 13, 14, 15 highlighted, output hidden
- **Narration:** Line 19 asks for the report of a day with no sales at all: an empty list.
  **On screen:** Code `examples/ex08_day_report.py`, line 19 highlighted, output hidden
- **Interaction:** "What does line 19 print?" stays on screen with a 10-second timer.
- **Narration:** Friday, 0 sales, 0.00. The loop in day total runs zero times, so the total stays 0.
  **On screen:** Code `examples/ex08_day_report.py`, line 19 highlighted, output `examples/ex08_day_report.expected`
- **Narration:** And Monday and Tuesday get their own lines from the same three functions. To change the tax, Asha edits one line: line 4. Mission complete!
  **On screen:** Code `examples/ex08_day_report.py`, line 17, 18 highlighted, output `examples/ex08_day_report.expected`
- **Narration:** Next, Asha wants a function for her bill splitter from Chapter 5. This time, an AI assistant writes the code, one stage at a time.
  **On screen:** Code `examples/ex08_day_report.py`, output `examples/ex08_day_report.expected`

## Scene 10: Work with AI: six stages, one function

**Section:** Work with AI

**Direction:** Teach the specification skill. One conversation per stage, all about share(). Generate: print instead of return. Test: no rounding, two checks False, then all True. Debug: missing argument. Improve: swapped parameters fail every check.

- **Narration:** This chapter's AI skill is the specification. A specification says a function's name, its parameters, what it returns, and a few examples with exact results.
  **On screen:** This chapter's AI skill: a specification
    - A **specification** says a function's name, its parameters, what it returns, and examples with exact results.
- **Narration:** You write the specification and your own checks. The AI writes the code. And your checks decide if the code is right.
  **On screen:** This chapter's AI skill: a specification
    - A **specification** says a function's name, its parameters, what it returns, and examples with exact results.
    - You write the specification and your own checks. The AI writes the code.
    - Your checks decide. Never paste private data into an AI tool.
- **Narration:** Stage 1: plan. Asha describes the job: a total, a number of people, and a tip. She asks for a specification, and no code yet.
  **On screen:** AI chat, stage 1: Plan: the specification first
    - You: I want a function for my bill splitter. It takes a total, a number of people and a tip percent. Do not write code yet. Write a specification: the name, the parameters, what it returns, and three examples with exact results.
- **Narration:** The AI gives a name, three parameters, the return value, and three examples. Asha checks example 1 by hand: 40 plus 10 percent is 44, and 44 shared by 4 is 11.
  **On screen:** AI chat, stage 1: Plan: the specification first
    - You: I want a function for my bill splitter. It takes a total, a number of people and a tip percent. Do not write code yet. Write a specification: the name, the parameters, what it returns, and three examples with exact results.
    - AI (example answer): Name: `share(total, people, tip_percent)`. Returns each person's share with the tip, rounded to cents. Examples: `share(40.0, 4, 10)` returns `11.0`. `share(43.07, 4, 0)` returns `10.77`. `share(10.0, 3, 0)` returns `3.33`.
- **Narration:** Stage 2: write. Asha writes three check lines herself, one for each example. Each prints the returned value, then whether it equals the expected result.
  **On screen:** AI chat, stage 2: Write: your own checks
    - You: I wrote these check lines myself, from the three examples. Do not write the function. Predict what each line prints if the function follows the specification. [code `examples/ai_share_fixed.py`]
- **Narration:** She asks the AI to predict them for a correct function: 11.0 True, 10.77 True, 3.33 True. Asha predicted the same.
  **On screen:** AI chat, stage 2: Write: your own checks
    - You: I wrote these check lines myself, from the three examples. Do not write the function. Predict what each line prints if the function follows the specification. [code `examples/ai_share_fixed.py`]
    - AI (example answer): Each line prints the returned value, then `True`: `11.0 True`, then `10.77 True`, then `3.33 True`.
- **Narration:** Stage 3: generate. Asha asks the AI to write the function, and to say exactly what her f string line prints.
  **On screen:** AI chat, stage 3: Generate: the function from the specification
    - You: Write the function from my specification. Then tell me exactly what this line prints: `print(f"Each pays {share(40.0, 4, 10):.2f}")`
- **Narration:** The AI writes three lines, and promises: Each pays 11.00.
  **On screen:** AI chat, stage 3: Generate: the function from the specification
    - You: Write the function from my specification. Then tell me exactly what this line prints: `print(f"Each pays {share(40.0, 4, 10):.2f}")`
    - AI (example answer): Here is the function. Your line prints `Each pays 11.00`. [code `examples/ai_share_print.py`]
- **Narration:** Here is the AI's function with Asha's line, line 6. Look at line 4, and remember step 4.
  **On screen:** Code `examples/ai_share_print.py`, line 4, 6 highlighted, output hidden
- **Interaction:** "The AI promises `Each pays 11.00`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Line 4 prints the share, and the function returns nothing. So the call gives back None.
  **On screen:** Code `examples/ai_share_print.py`, line 4, 6 highlighted, error `examples/ai_share_print.expected_error`
- **Narration:** The f string cannot format None with two decimal places, so Python stops with a Type Error. The AI broke its own specification, and it sounded sure.
  **On screen:** Code `examples/ai_share_print.py`, line 4, 6 highlighted, error `examples/ai_share_print.expected_error`
- **Narration:** Stage 4: test. Asha tells the AI what happened, and asks for a function that returns the value.
  **On screen:** AI chat, stage 4: Test: run the checks on the new version
    - You: Your function printed instead of returning, so my line crashed. Fix it so that it returns the value.
- **Narration:** The AI gives a corrected version. It returns the share now. Asha does not trust it yet. She runs her three checks on it.
  **On screen:** AI chat, stage 4: Test: run the checks on the new version
    - You: Your function printed instead of returning, so my line crashed. Fix it so that it returns the value.
    - AI (example answer): You are right. Here is the corrected function. It now returns the share. [code `examples/ai_share_noround.py`]
- **Narration:** Line 3 returns the share. Compare it with the specification: rounded to cents.
  **On screen:** Code `examples/ai_share_noround.py`, line 3 highlighted, output hidden
- **Narration:** Lines 5 to 10 are Asha's checks: three calls with the three examples, then three prints.
  **On screen:** Code `examples/ai_share_noround.py`, line 5, 6, 7, 8, 9, 10 highlighted, output hidden
- **Interaction:** "Which checks will print `False`?" stays on screen with a 10-second timer.
- **Narration:** Lines 6 and 7. The AI forgot to round, so the second share is 10.7675, and the third has many digits.
  **On screen:** Code `examples/ai_share_noround.py`, line 9, 10 highlighted, output `examples/ai_share_noround.expected`
- **Narration:** And the first check passed only by luck: its exact answer has no extra digits. One passing check proves nothing. Run them all.
  **On screen:** Code `examples/ai_share_noround.py`, line 8 highlighted, output `examples/ai_share_noround.expected`
- **Narration:** Asha adds round, with 2 places, on line 3, as the specification says.
  **On screen:** Code `examples/ai_share_fixed.py`, line 3 highlighted, output `examples/ai_share_fixed.expected`
- **Narration:** Then she runs every check again. 11.0 True, 10.77 True, 3.33 True. All three pass.
  **On screen:** Code `examples/ai_share_fixed.py`, line 8, 9, 10 highlighted, output `examples/ai_share_fixed.expected`
- **Narration:** Stage 5: debug. Asha uses the function in her program, and it stops with a Type Error. She pastes the code and the full error report, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I used your function in my program, and it stopped with this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_share_missing.py`]
- **Narration:** The AI reads the last line: share is missing one required argument, tip percent.
  **On screen:** AI chat, stage 5: Debug: the AI's answer
    - You: I used your function in my program, and it stopped with this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_share_missing.py`]
    - AI (example answer): `share()` has three parameters, but the call on line 6 passes only two arguments. Python cannot fill `tip_percent`. The fix: pass the tip too, such as `share(40.0, 4, 10)`.
- **Narration:** The function has three parameters, but line 6 passes only two arguments. The fix: pass the tip too. Asha adds it, and you will see her program run at the end of this section.
  **On screen:** AI chat, stage 5: Debug: the AI's answer
    - You: I used your function in my program, and it stopped with this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_share_missing.py`]
    - AI (example answer): `share()` has three parameters, but the call on line 6 passes only two arguments. Python cannot fill `tip_percent`. The fix: pass the tip too, such as `share(40.0, 4, 10)`.
- **Narration:** Stage 6: improve. Asha asks for one improvement. And she adds a rule: do not change the name, the parameters, or what the function returns.
  **On screen:** AI chat, stage 6: Improve: better, but the same?
    - You: My function passes every check. Suggest one improvement, with one reason. Do not change its name, its parameters or what it returns.
- **Narration:** The AI suggests putting people first, because it reads more naturally. It promises the same results.
  **On screen:** AI chat, stage 6: Improve: better, but the same?
    - You: My function passes every check. Suggest one improvement, with one reason. Do not change its name, its parameters or what it returns.
    - AI (example answer): Put `people` first: `share(people, total, tip_percent)`. People come before money, so it reads more naturally. The results stay the same.
- **Narration:** Asha tries it. Line 2 now has people first. Her check lines stay the same: they still pass the total first.
  **On screen:** Code `examples/ai_share_swapped.py`, line 2, 5 highlighted, output hidden
- **Interaction:** "Will every check still print `True`?" stays on screen with a 10-second timer.
- **Narration:** No. Every check prints False. The calls pass 40 as people and 4 as the total, so the shares are tiny.
  **On screen:** Code `examples/ai_share_swapped.py`, line 5 highlighted, output `examples/ai_share_swapped.expected`
- **Narration:** The AI broke Asha's rule: it changed the parameters. Arguments fill parameters in order, so every call now means something else. Asha keeps her version.
  **On screen:** Code `examples/ai_share_swapped.py`, line 5 highlighted, output `examples/ai_share_swapped.expected`
- **Narration:** Here is Asha's final function, with a docstring from the specification, on line 3.
  **On screen:** Code `examples/ai_share_final.py`, line 3 highlighted, output `examples/ai_share_final.expected`
- **Narration:** Lines 6 and 7 use it in her bill splitter: 11.00 for table 4, and 10.77 for table 7.
  **On screen:** Code `examples/ai_share_final.py`, line 6, 7 highlighted, output `examples/ai_share_final.expected`
- **Narration:** Quick check. An AI wrote a function from your specification. Who decides if it is right?
  **On screen:** Quick check: "An AI wrote a function from your specification. Who decides if it is right?" (options shown)
- **Interaction:** "An AI wrote a function from your specification. Who decides if it is right?" stays on screen with a 10-second timer.
- **Narration:** C. Your checks, run on its code. The AI's promise is not proof.
  **On screen:** Quick check: "An AI wrote a function from your specification. Who decides if it is right?" (answer revealed: Your checks, run on its code)
- **Narration:** Breather. Asha wrote a specification and her own checks, and caught three AI mistakes: a print instead of a return, a missing round, and swapped parameters.
  **On screen:** Breather card
    - Specification first, then code.
    - Run every check after every change.
    - Never change the parameters without changing every call.
- **Breather:** 4 quiet seconds.

## Scene 11: Common mistakes

**Section:** Common mistakes

**Direction:** Mistake 1 is shown with its error. Mistake 2 is a spot-it question on the call brackets. Mistake 3 calls back to step 4. Mistake 4 asks what a return inside the loop gives.

- **Narration:** Mistake 1. Line 2 calls welcome, but the def comes later, on line 4. Python runs from top to bottom, so it does not know that name yet.
  **On screen:** Code `examples/err01_call_before_def.py`, line 2, 4 highlighted, error `examples/err01_call_before_def.expected_error`
- **Narration:** Python stops with a Name Error. The fix: move the call below the function.
  **On screen:** Code `examples/err01_call_before_def.py`, line 2, 4 highlighted, error `examples/err01_call_before_def.expected_error`
- **Narration:** Now you try. Look closely at line 5, and remember what a call needs.
  **On screen:** Code `examples/err02_no_brackets.py`, line 5 highlighted, output hidden
- **Interaction:** "What is wrong with line 5?" stays on screen with a 10-second timer.
- **Narration:** The brackets are missing. Without them, tea refers to the function itself, not to a price. Line 6 tries to add 1 to a function.
  **On screen:** Code `examples/err02_no_brackets.py`, line 5, 6 highlighted, error `examples/err02_no_brackets.expected_error`
- **Narration:** The fix: call it with an argument, such as with tax of 3.5.
  **On screen:** Code `examples/err02_no_brackets.py`, line 5, 6 highlighted, error `examples/err02_no_brackets.expected_error`
- **Narration:** Mistake 3 is step 4 again, and the AI's first mistake. The function prints 3.85, but it returns None.
  **On screen:** Code `examples/err03_none_plus.py`, line 3, 5 highlighted, error `examples/err03_none_plus.expected_error`
- **Narration:** So line 5 tries to add 1 to None. None Type is the type of None. The fix: return instead of print.
  **On screen:** Code `examples/err03_none_plus.py`, line 3, 5 highlighted, error `examples/err03_none_plus.expected_error`
- **Narration:** Mistake 4. Look at the indentation of line 6. The return is inside the loop.
  **On screen:** Code `examples/ex09_return_too_early.py`, line 6 highlighted, output hidden
- **Narration:** A return ends the whole function at once, even in the middle of a loop.
  **On screen:** Code `examples/ex09_return_too_early.py`, line 4, 5, 6 highlighted, output hidden
- **Interaction:** "What does line 8 print?" stays on screen with a 10-second timer.
- **Narration:** 3.5. The loop added the first price, and then return ended the function. There is no error, only a wrong answer.
  **On screen:** Code `examples/ex09_return_too_early.py`, line 6, 8 highlighted, output `examples/ex09_return_too_early.expected`
- **Narration:** The fix: move return four spaces to the left, so it runs after the loop has finished.
  **On screen:** Code `examples/ex09_return_too_early.py`, line 6, 8 highlighted, output `examples/ex09_return_too_early.expected`
- **Narration:** Last breather. Now you know the four function mistakes that catch most beginners.
  **On screen:** Breather card
    - Define before you call.
    - A call needs brackets.
    - Return after the loop, not inside it.
- **Breather:** 4 quiet seconds.

## Scene 12: Think beyond

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Asha wants a function that gives members 10 percent off. Write its specification first: the return value, and three examples, one for a non-member.
  **On screen:** Question card: "Write the specification for `member_price(price, is_member)`: 10 percent off for members. Give three examples, one for a non-member."
- **Interaction:** "Write the specification for `member_price(price, is_member)`: 10 percent off for members. Give three examples, one for a non-member." stays on screen with a 10-second timer.
- **Narration:** Then write the function, and your checks.
  **On screen:** Question card: "Write the specification for `member_price(price, is_member)`: 10 percent off for members. Give three examples, one for a non-member."
- **Narration:** Second. A function can return two values at once, as a tuple. How would you unpack them in the line that calls it?
  **On screen:** Question card: "A function can `return total, count`. How do you unpack the two values in the caller?"
- **Interaction:** "A function can `return total, count`. How do you unpack the two values in the caller?" stays on screen with a 10-second timer.
- **Narration:** Write a day summary function that returns both, and test it.
  **On screen:** Question card: "A function can `return total, count`. How do you unpack the two values in the caller?"

## Scene 13: Recap

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap. Def defines a function, and a call with brackets runs it.
  **On screen:** Recap
    - A function is a named block of code. `def` defines it; a call with brackets runs it.
- **Narration:** Parameters receive the arguments, in order. Return hands a value back, and without it you get None.
  **On screen:** Recap
    - A function is a named block of code. `def` defines it; a call with brackets runs it.
    - Parameters are names in the `def` line. Arguments are the values in a call, in order.
    - `return` hands a value back. Without `return`, a function gives back `None`.
- **Narration:** A docstring says what the function does. A long traceback reads from the bottom up.
  **On screen:** Recap
    - A function is a named block of code. `def` defines it; a call with brackets runs it.
    - Parameters are names in the `def` line. Arguments are the values in a call, in order.
    - `return` hands a value back. Without `return`, a function gives back `None`.
    - A docstring on the first line of the body says what the function does.
    - Read a long traceback from the bottom up: the bottom block is where it happened.
- **Narration:** And with AI: write the specification and your checks first. The checks decide.
  **On screen:** Recap
    - A function is a named block of code. `def` defines it; a call with brackets runs it.
    - Parameters are names in the `def` line. Arguments are the values in a call, in order.
    - `return` hands a value back. Without `return`, a function gives back `None`.
    - A docstring on the first line of the body says what the function does.
    - Read a long traceback from the bottom up: the bottom block is where it happened.
    - Write the specification and your checks first. The checks decide.
- **Narration:** One last check. This function calculates n times 2, but has no return. What does print of double of 4 show?
  **On screen:** Quick check: "`def double(n):` has the body `n * 2`, with no `return`. What does `print(double(4))` show?" (options shown)
- **Interaction:** "`def double(n):` has the body `n * 2`, with no `return`. What does `print(double(4))` show?" stays on screen with a 10-second timer.
- **Narration:** A. None. The body calculates 8, but hands nothing back.
  **On screen:** Quick check: "`def double(n):` has the body `n * 2`, with no `return`. What does `print(double(4))` show?" (answer revealed: `None`)
- **Narration:** Mission complete! You earned 100 XP and the Function Forger badge.
  **On screen:** Function Forger You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 14: Practice

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn: eight tasks, worth 170 XP. Three warm-up tasks at 10 XP, and three apply tasks at 20, including menu lines.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each: an average with an empty day, and an AI's member price to fix. Try each one before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 15: What's next

**Section:** What's next

**Direction:** End card. Tease Chapter 17: where variables live, and small functions with one job each. Hold quietly at the end.

- **Narration:** Asha's functions work. But inside day total there is a variable called total. Can the rest of the program see it? And how big should one function be?
  **On screen:** Scope and Good Function Design Where variables live, and functions that do one job.
- **Narration:** In Chapter 17, you will learn where variables live, and how to design small functions that each do one job.
  **On screen:** Scope and Good Function Design Where variables live, and functions that do one job.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Scope and Good Function Design Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 17.
  **On screen:** Scope and Good Function Design Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
