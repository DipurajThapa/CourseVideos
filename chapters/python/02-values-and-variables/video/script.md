# Video Script: Chapter 2: Values and Variables: Giving Data a Name

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 14:09.

## Scene 1: Introduction (0:00 to 0:47)

**Section:** Introduction

**Direction:** Open on the title card, then cut to the AI's flawed average code to set the hook. Keep the output hidden until the pause.

- **Narration:** Welcome to Code Quest, Chapter 2: Values and Variables. In this chapter, you will learn how a program stores data, gives it a name and calculates with it.
  **On screen:** Values and Variables: Giving Data a Name Store data, name it, calculate with it, and predict every result.
- **Narration:** First, a puzzle. A learner asked an AI assistant for the average of three test scores: 80, 90 and 100. The AI wrote this code, and it said the program would print 90.
  **On screen:** Code `examples/ai_average_flawed.py`, lines 5 highlighted, output hidden (predict first)
- **Narration:** Look closely at line 5. Do you trust the prediction?
  **On screen:** Pause card: "Will this code really print an average of 90?" with a 4-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** Here is the real output: 203 point 3 3. The AI was sure, and it was wrong. By the end of this chapter, you will see why in two seconds.
  **On screen:** Code `examples/ai_average_flawed.py`, lines 5 highlighted, output `examples/ai_average_flawed.expected`

## Scene 2: Learning goals (0:47 to 1:16)

**Section:** Learning goals

**Direction:** Reveal the goals one at a time, in step with the narration.

- **Narration:** Here is what you will be able to do by the end. First, write variables with clear names, and give them values with the equals sign.
  **On screen:** By the end of this chapter, you will be able to:
    - Write variables with clear names and give them values with `=`.
- **Narration:** Second, explain the four basic types of data, and check the type of any value. Third, calculate with the seven arithmetic operators.
  **On screen:** By the end of this chapter, you will be able to:
    - Write variables with clear names and give them values with `=`.
    - Explain the types `int`, `float`, `str` and `bool`, and check a type with `type()`.
    - Calculate with `+`, `-`, `*`, `/`, `//`, `%` and `**`.
- **Narration:** Fourth, predict the output of a program before you run it. And fifth, fix the errors that beginners meet most often with variables.
  **On screen:** By the end of this chapter, you will be able to:
    - Write variables with clear names and give them values with `=`.
    - Explain the types `int`, `float`, `str` and `bool`, and check a type with `type()`.
    - Calculate with `+`, `-`, `*`, `/`, `//`, `%` and `**`.
    - Predict the output of a short program, then check your prediction.
    - Fix the errors beginners meet most often with variables.

## Scene 3: Why this matters (1:16 to 1:56)

**Section:** Why this matters

**Direction:** Show the problem with the Chapter 1 receipt, then the fix in one line.

- **Narration:** In Chapter 1, the cafe receipt typed each price twice: once in the item line, and once in the total. If the price of tea changes, you must find and change every copy. Miss one, and the receipt is wrong.
  **On screen:** The problem: the same price, typed twice ['In Chapter 1, the receipt typed each price in two places:']
- **Narration:** A variable solves this. A variable is a name that refers to a value. You store the price once, under a name such as tea price, and use that name everywhere.
  **On screen:** The fix: give the value a name ['A **variable** is a name that refers to a value.', 'Store the price once, then use the name everywhere:']
- **Narration:** Every real program works this way. A shopping app keeps the items in your basket. A game keeps your score. A banking app keeps your balance. Each of these values has a name inside the program.
  **On screen:** Every real program names its data
    - A shopping app keeps the items in your basket.
    - A game keeps your score.
    - A banking app keeps your balance.

## Scene 4: The idea: values, types and assignment (1:56 to 2:58)

**Section:** The idea

**Direction:** Table first, then the assignment diagram. Finish with the analogy and where it stops working.

- **Narration:** A value is a single piece of data, such as 3, 3.5 or the word Tea. Every value has a type. The type tells Python what kind of data it is, and what you can do with it.
  **On screen:** Table: Every value has a type (4 rows)
- **Narration:** Python has four basic types. An int is a whole number. A float is a number with a decimal point. A string is text inside quotation marks. And a Boolean is either True or False.
  **On screen:** Table: Every value has a type (4 rows)
- **Narration:** Assignment connects a name to a value. You write the name, then the equals sign, then the value. Python works out the right side first. Then it connects the name on the left to the result.
  **On screen:** Assignment connects a name to a value ['Read `=` as **now refers to**, not as **is equal to**.']
- **Narration:** So read the equals sign as now refers to, not as is equal to. Think of a variable as a name label that you stick on a value. You can move the label to a new value at any time.
  **On screen:** A variable is like a name label
    - You stick the label `tea_price` on the value `3`.
    - You can move the label to a new value at any time.
- **Narration:** The comparison stops working at one point. Two labels can point to the same value, and moving one label does not move the other.
  **On screen:** A variable is like a name label
    - You stick the label `tea_price` on the value `3`.
    - You can move the label to a new value at any time.
    - Where the comparison stops: two labels can point to the same value, and moving one label does not move the other.

## Scene 5: Step 1: Your first variables (2:58 to 4:08)

**Section:** Build it step by step

**Direction:** Code first with the output hidden, a pause to predict, then the reveal. Then the naming rules.

- **Narration:** Step 1. Create a file called ex 0 1 first variables. Line 2 stores the text Asha in a variable called customer. Line 3 stores the number 3 in tea price. The next three lines print them.
  **On screen:** Code `examples/ex01_first_variables.py`, lines 2, 3 highlighted, output hidden (predict first)
- **Narration:** Before you run it, predict the three lines of output.
  **On screen:** Pause card: "What are the three lines of output? Write them down." with a 5-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** Here is the output. Asha, then Tea costs 3, then Two teas cost 6. In the print on line 4, the name customer has no quotation marks. So Python prints its value, Asha, and not the word customer.
  **On screen:** Code `examples/ex01_first_variables.py`, lines 4 highlighted, output `examples/ex01_first_variables.expected`
- **Narration:** Good names make code easy to read. The Python style guide, called PEP 8, says: use lowercase letters, and join words with an underscore. A name can contain letters, digits and underscores, but it cannot start with a digit.
  **On screen:** Naming rules (PEP 8)
    - Lowercase words joined by underscores: `tea_price`, not `TeaPrice` or `tp`.
    - Letters, digits and underscores only, and never a digit first.
- **Narration:** Capital letters matter, so price with a small p and Price with a capital P are two different names. And do not use the words Python reserves for itself, such as True, None or class.
  **On screen:** Naming rules (PEP 8)
    - Lowercase words joined by underscores: `tea_price`, not `TeaPrice` or `tp`.
    - Letters, digits and underscores only, and never a digit first.
    - Capital letters matter: `price` and `Price` are different names.
    - Do not use reserved words such as `True`, `None` or `class`.

## Scene 6: Step 2: Check the type of a value (4:08 to 4:45)

**Section:** Build it step by step

**Direction:** Show the code with the output hidden, then reveal the output and point at each type.

- **Narration:** Step 2. The type function tells you the type of any value. This program stores four values: a count of cups, a price, an item name and a yes or no fact. Then it prints each value with its type.
  **On screen:** Code `examples/ex02_types.py`, lines 2, 3, 4, 5 highlighted, output hidden (predict first)
- **Narration:** Run it. The 2 is an int. The 3.5 is a float. Tea is a string, shown as s t r. And True is a bool.
  **On screen:** Code `examples/ex02_types.py`, lines 6, 7, 8, 9 highlighted, output `examples/ex02_types.expected`
- **Narration:** Python chose each type from the way you wrote the value. A decimal point makes a float, and quotation marks make a string. True and False need a capital first letter.
  **On screen:** How Python chooses the type
    - A decimal point makes a `float`: `3.5`.
    - Quotation marks make a `str`: `"Tea"`.
    - `True` and `False` need a capital first letter.

## Scene 7: Step 3: Calculate with operators (4:45 to 6:01)

**Section:** Build it step by step

**Direction:** Pause for the learner to predict all seven lines. After the reveal, use the table to explain the three surprising operators.

- **Narration:** Step 3. An operator is a symbol that does a calculation. Seventeen biscuits are shared between five friends. This program uses all seven arithmetic operators.
  **On screen:** Code `examples/ex03_arithmetic.py`, lines 4, 5, 6, 7, 8, 9, 10 highlighted, output hidden (predict first)
- **Narration:** Pause the video and predict each line. Pay special attention to divide, floor divide and remainder.
  **On screen:** Pause card: "17 biscuits, 5 friends. Predict all seven results." with a 8-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** Here are the results. Add gives 22, subtract gives 12, and multiply gives 85. Divide gives 3.4. Floor divide gives 3. Remainder gives 2. And power gives 25.
  **On screen:** Code `examples/ex03_arithmetic.py`, lines 7, 8, 9 highlighted, output `examples/ex03_arithmetic.expected`
- **Narration:** Three operators often surprise beginners. A single slash is division. It gives the exact answer, 3.4, and the result is always a float. A double slash is floor division. It gives the whole part, so each friend gets 3 whole biscuits.
  **On screen:** Table: Three operators that surprise beginners (3 rows)
- **Narration:** The percent sign gives the remainder, so 2 biscuits are left over. Finally, two stars raise a number to a power. So 5 to the power 2 is 5 times 5, which is 25.
  **On screen:** Table: Three operators that surprise beginners (4 rows)

## Scene 8: Step 4: Change a variable (6:01 to 6:35)

**Section:** Build it step by step

**Direction:** Highlight each assignment line in turn so the learner can follow the value of points.

- **Narration:** Step 4. A variable can get a new value. Here, points starts at 10. Line 4 says: points equals points plus 5.
  **On screen:** Code `examples/ex04_reassign.py`, lines 2, 4 highlighted, output hidden (predict first)
- **Narration:** In mathematics, that line would be impossible. In Python, it means: take the current value of points, add 5, and give points the new value. Python works out the right side first.
  **On screen:** Python works out the right side first ['`points = points + 5` means:', '1. Take the current value of `points`: **10**.', '2. Add 5: **15**.', '3. Give `points` the new value: **15**.']
- **Narration:** So the output shows Start 10, After a quiz 15, and After the bonus 30. Line 6 doubled the value of 15.
  **On screen:** Code `examples/ex04_reassign.py`, lines 6 highlighted, output `examples/ex04_reassign.expected`

## Scene 9: Step 5: The order of operations (6:35 to 7:36)

**Section:** Build it step by step

**Direction:** Pause on the first two lines. After the reveal, explain line 4, then the inexact float on line 5 and round on line 6.

- **Narration:** Step 5. Python follows the same order as mathematics. It calculates powers first. Then it multiplies and divides. Then it adds and subtracts. Brackets change the order.
  **On screen:** Code `examples/ex05_order.py`, lines 2, 3 highlighted, output hidden (predict first)
- **Narration:** Predict lines 2 and 3 before you look.
  **On screen:** Pause card: "2 + 3 * 4 and (2 + 3) * 4: what does each print?" with a 5-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** Line 2 multiplies first, so the result is 14. Line 3 adds first because of the brackets, so it gives 20. Line 4 divides first, and gives 8.0, a float, because division always gives a float.
  **On screen:** Code `examples/ex05_order.py`, lines 2, 3, 4 highlighted, output `examples/ex05_order.expected`
- **Narration:** Line 5 is a surprise. Point 1 plus point 1 plus point 1 does not print exactly point 3. Computers store decimal numbers in binary, so some values, such as point 1, carry a tiny error. On line 6, the round function rounds the result to 2 decimal places, and you get point 3.
  **On screen:** Code `examples/ex05_order.py`, lines 5, 6 highlighted, output `examples/ex05_order.expected`

## Scene 10: See the outcome: the cafe bill (7:36 to 8:38)

**Section:** See the outcome

**Direction:** Walk down the program in three groups: the inputs, the calculations, the prints. Then reveal the output.

- **Narration:** Here is the cafe receipt from Chapter 1, rebuilt with variables. Lines 2 to 7 store the inputs: the customer, two prices, the number of teas, a member flag and a 10 percent discount.
  **On screen:** Code `examples/ex06_cafe_bill.py`, lines 2, 3, 4, 5, 6, 7 highlighted, output hidden (predict first)
- **Narration:** Lines 9 to 12 calculate the tea total, the bill, the discount and the amount to pay. Each calculation uses names, not numbers, so every price appears only once.
  **On screen:** Code `examples/ex06_cafe_bill.py`, lines 9, 10, 11, 12 highlighted, output hidden (predict first)
- **Narration:** Run it. Two teas at 3.5 cost 7.0. The bill is 13.0, the discount is 1.3, and Asha pays 11.7. Notice that 7.0 is a float, because one of its parts was a float.
  **On screen:** Code `examples/ex06_cafe_bill.py`, lines 14, 15, 16, 17, 18, 19, 20 highlighted, output `examples/ex06_cafe_bill.expected`
- **Narration:** Now change tea price to 4 and run it again. Every line that depends on the tea price updates by itself. For now, the discount applies every time. In Chapter 6, you will use the member flag to decide.
  **On screen:** Pause card: "Change tea_price to 4. Which output lines change?" with a 5-second countdown
  **Interaction:** the learner pauses and answers before the reveal.

## Scene 11: Work with AI: predict, then run (8:38 to 10:41)

**Section:** Work with AI

**Direction:** Introduce the prediction skill, show the six stages, show two prompt cards, then replay the hook as the AI pair moment and fix it.

- **Narration:** The AI skill for this chapter is prediction. Before you run a program, ask an AI assistant such as ChatGPT or Claude to predict its output. Write down your own prediction too. Then run the code. The real output is the only answer that counts.
  **On screen:** The AI skill: predict, then run
    - Ask an AI assistant such as ChatGPT or Claude to predict the output.
    - Write down your own prediction too.
    - Run the code. The real output is the only answer that counts.
- **Narration:** The safety habits from Chapter 1 still apply. Never paste passwords, keys or private data. Run every piece of AI code yourself. You are responsible for the code you use.
  **On screen:** Safety habits
    - Never paste passwords, keys or private data into an AI tool.
    - Run every piece of AI code yourself.
    - You are responsible for the code you use.
- **Narration:** AI helps at every stage. Plan the variables you need. Write the code yourself, then compare predictions. Generate examples with fixed names. Debug with the full error. Test with new values. And improve your variable names.
  **On screen:** Table: AI at every stage (6 rows)
- **Narration:** Here is the Write card. Paste your code, and ask the AI to predict the exact output line by line, without running or changing it. Then compare three things: your prediction, the AI's prediction and the real output.
  **On screen:** Prompt card (Write): "Here is my Python code: <paste your code>. Do not change it and do not run it. Predict the exact output, line by line. For each line, explain in one sentence how Python calculated it."
- **Narration:** And here is the Debug card. Give the AI the exact error message, and ask for the cause before the fix.
  **On screen:** Prompt card (Debug): "I am a beginner. I ran this Python code: <paste the code>. I got this exact error: <paste the full error message>. First explain what the error means and which line causes it. Then show the smallest fix."
- **Narration:** Now, the AI pair moment. Remember the puzzle from the start? The AI wrote this average, and predicted 90. It printed 203 point 3 3. Why?
  **On screen:** Code `examples/ai_average_flawed.py`, lines 5 highlighted, output `examples/ai_average_flawed.expected`
- **Narration:** Use what you learned in step 5.
  **On screen:** Pause card: "Which operation does Python do first on line 5? Where do the brackets go?" with a 6-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** The AI forgot the order of operations. Python divided only score 3 by 3, and then added the other two scores. Brackets around the sum fix the order, and the program prints 90.0.
  **On screen:** Code `examples/ai_average_fixed.py`, lines 5 highlighted, output `examples/ai_average_fixed.expected`
- **Narration:** A quick check would also catch this flaw. An average of three scores must be between the lowest and the highest score. A result of 203 is impossible. Code that runs is not always code that is correct.
  **On screen:** The two-second check
    - An average must lie between the lowest and the highest value.
    - 80, 90 and 100 cannot average 203.
    - Predict. Run. Compare.

## Scene 12: Common mistakes (10:41 to 12:03)

**Section:** Common mistakes

**Direction:** One beat per mistake: the code and the real error side by side, then the fix in the narration.

- **Narration:** Now, four common mistakes. Mistake 1 is a typing error in a variable name. Line 4 uses tea prise, spelled with an s. Python only knows the names you created, so it stops with a Name Error. It even suggests the right name.
  **On screen:** Code `examples/err01_name_typo.py`, lines 4 highlighted, error `examples/err01_name_typo.expected_error`
- **Narration:** Mistake 2 is a number stored as text. With quotation marks, 3 is a string, not an int. Python will not add text and a number, so you get a Type Error. The fix is to remove the quotation marks.
  **On screen:** Code `examples/err02_text_number.py`, lines 2, 3 highlighted, error `examples/err02_text_number.expected_error`
- **Narration:** Sometimes this mistake gives no error at all, which is worse. Multiplying the string 3 by 2 repeats the text, so you get 33 instead of 6. If a result looks strange, check the type.
  **On screen:** Code `examples/ex07_text_times.py`, lines 2, 3 highlighted, output `examples/ex07_text_times.expected`
- **Narration:** Mistake 3 is a name that starts with a digit. Python reads the 2 as the start of a number, and does not understand the letters after it. Start the name with a letter, such as second place.
  **On screen:** Code `examples/err03_digit_first.py`, lines 2 highlighted, error `examples/err03_digit_first.expected_error`
- **Narration:** Mistake 4 puts the name and the value on the wrong sides. A literal is a value written directly in the code, such as 10, and it cannot get a new value. The name always goes on the left: points equals 10.
  **On screen:** Code `examples/err04_reversed.py`, lines 2 highlighted, error `examples/err04_reversed.expected_error`
- **Narration:** The habit from Chapter 1 still works. Read the last line of an error first. It names the kind of error. Then look at the line number.
  **On screen:** Table: Read the last line first (4 rows)

## Scene 13: Think beyond (12:03 to 12:45)

**Section:** Think beyond

**Direction:** Two open questions, each with a pause. Do not give the answers: the learner tests them.

- **Narration:** Two questions to think beyond this chapter. First: four friends share a bill of 50. How could you use floor division and remainder to find how much each person pays in whole units, and how much is left over?
  **On screen:** Pause card: "4 friends share a bill of 50. Use // and % to find each share and the amount left over." with a 6-second countdown
  **Interaction:** the learner pauses and answers before the reveal.
- **Narration:** Second: a is 5 and b is 8, and you want to swap them. Why does a equals b, followed by b equals a, not work? Predict the result, test it, then find a fix that uses a third variable.
  **On screen:** Pause card: "a = 5 and b = 8. Why does a = b, then b = a, fail to swap them?" with a 6-second countdown
  **Interaction:** the learner pauses and answers before the reveal.

## Scene 14: Recap (12:45 to 13:25)

**Section:** Recap

**Direction:** Reveal the six recap lines, then the badge.

- **Narration:** Let's recap. A value is a piece of data, and every value has a type: int, float, string or bool. A variable is a name that refers to a value. The equals sign connects the name on the left to the value on the right.
  **On screen:** Recap
    - Every value has a type: `int`, `float`, `str` or `bool`.
    - A variable is a name for a value. `=` connects the name on the left to the value on the right.
- **Narration:** Python works out the right side first. Single slash always gives a float. Double slash gives the whole part, and percent gives the remainder. Brackets control the order of operations.
  **On screen:** Recap
    - Every value has a type: `int`, `float`, `str` or `bool`.
    - A variable is a name for a value. `=` connects the name on the left to the value on the right.
    - Python works out the right side first, so `points = points + 5` is valid.
    - `/` always gives a `float`. `//` gives the whole part, and `%` gives the remainder.
    - Brackets control the order. A `float` can be slightly inexact, and `round()` helps.
- **Narration:** And with AI: ask it to predict, make your own prediction, and let the real run decide.
  **On screen:** Recap
    - Every value has a type: `int`, `float`, `str` or `bool`.
    - A variable is a name for a value. `=` connects the name on the left to the value on the right.
    - Python works out the right side first, so `points = points + 5` is valid.
    - `/` always gives a `float`. `//` gives the whole part, and `%` gives the remainder.
    - Brackets control the order. A `float` can be slightly inexact, and `round()` helps.
    - Ask AI to predict, make your own prediction, and let the real run decide.
- **Narration:** You earned 100 XP and the Name Keeper badge.
  **On screen:** Name Keeper You earned 100 XP.

## Scene 15: Practice (13:25 to 13:52)

**Section:** Practice

**Direction:** List the eight tasks by tier so learners know what to expect.

- **Narration:** Now practise. There are eight tasks in the practice file. The three warm-up tasks are worth 10 XP each: store and print, name the type, and predict the operators.
  **On screen:** Table: Practice: 8 tasks, 160 XP (3 rows)
- **Narration:** The apply tasks are worth 20 XP each, and the two stretch tasks are worth 40 each. In the last task, you fix an AI's temperature converter. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 160 XP (3 rows)

## Scene 16: What's next (13:52 to 14:09)

**Section:** What's next

**Direction:** End card. Hold for two seconds after the narration.

- **Narration:** In Chapter 3, you will work with text. You will join strings and build clear messages from your variables with f-strings. Do the warm-up tasks now. They take about ten minutes. See you in Chapter 3.
  **On screen:** Working with Text: Strings and f-strings Do the warm-up tasks now. They take about ten minutes.
