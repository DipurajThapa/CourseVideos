# Video Script: Chapter 2: Values and Variables: Giving Data a Name

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:26.

## Scene 1: Introduction (0:00 to 0:50)

**Section:** Introduction

**Direction:** Open on the problem from Chapter 1, then show the finished self-updating bill as the mission. No question yet.

- **Narration:** Welcome back to Code Quest. This is Chapter 2.
  **On screen:** Values and Variables: Giving Data a Name
- **Narration:** Today you will give your data names, and make Python do the maths for you.
  **On screen:** Values and Variables: Giving Data a Name Store it once. Use it everywhere.
- **Narration:** And an AI assistant will get the maths wrong, while sounding completely sure. Your job is to catch it.
  **On screen:** Values and Variables: Giving Data a Name Store it once. Use it everywhere.
- **Narration:** Remember Asha's receipt from the Corner Cafe? It had a problem. Every price was typed twice.
  **On screen:** Asha has a problem
    - Her receipt from Chapter 1 typed every price **twice**.
- **Narration:** Now the price of tea goes up. Asha must hunt down every copy and change it.
  **On screen:** Asha has a problem
    - Her receipt from Chapter 1 typed every price **twice**.
    - The price of tea goes up. She must find and change every copy.
- **Narration:** And if she misses one? The receipt is wrong, and nobody notices.
  **On screen:** Asha has a problem
    - Her receipt from Chapter 1 typed every price **twice**.
    - The price of tea goes up. She must find and change every copy.
    - Miss one copy, and the receipt is wrong.
- **Narration:** So here is today's mission. A cafe bill where every price is stored once, with a name.
  **On screen:** Code `examples/ex06_cafe_bill.py`, line 2, 3, 4, 5, 6, 7 highlighted, output `examples/ex06_cafe_bill.expected`
- **Narration:** Python works out the totals, the discount and the amount to pay.
  **On screen:** Code `examples/ex06_cafe_bill.py`, line 9, 10, 11, 12 highlighted, output `examples/ex06_cafe_bill.expected`
- **Narration:** Change one number at the top, and the whole bill updates by itself.
  **On screen:** Code `examples/ex06_cafe_bill.py`, line 3 highlighted, output `examples/ex06_cafe_bill.expected`
- **Narration:** That is the mission. Let's build it, piece by piece.
  **On screen:** Code `examples/ex06_cafe_bill.py`, output `examples/ex06_cafe_bill.expected`

## Scene 2: Learning goals (0:50 to 1:08)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Here is the plan. Five goals, one mission.
  **On screen:** By the end, you will be able to:
- **Narration:** Write variables with clear names.
  **On screen:** By the end, you will be able to:
    - Write variables with clear names and give them values with `=`.
- **Narration:** Know the four basic types, and check them with type.
  **On screen:** By the end, you will be able to:
    - Write variables with clear names and give them values with `=`.
    - Explain the types `int`, `float`, `str` and `bool`, and check one with `type()`.
- **Narration:** Calculate with Python's operators.
  **On screen:** By the end, you will be able to:
    - Write variables with clear names and give them values with `=`.
    - Explain the types `int`, `float`, `str` and `bool`, and check one with `type()`.
    - Calculate with `+`, `-`, `*`, `/`, `//`, `%` and `**`.
- **Narration:** Predict what a program prints, then check it.
  **On screen:** By the end, you will be able to:
    - Write variables with clear names and give them values with `=`.
    - Explain the types `int`, `float`, `str` and `bool`, and check one with `type()`.
    - Calculate with `+`, `-`, `*`, `/`, `//`, `%` and `**`.
    - Predict the output of a short program, then check it.
- **Narration:** And fix the errors that every beginner meets.
  **On screen:** By the end, you will be able to:
    - Write variables with clear names and give them values with `=`.
    - Explain the types `int`, `float`, `str` and `bool`, and check one with `type()`.
    - Calculate with `+`, `-`, `*`, `/`, `//`, `%` and `**`.
    - Predict the output of a short program, then check it.
    - Fix the errors beginners meet most often with variables.

## Scene 3: Why this matters (1:08 to 1:30)

**Section:** Why this matters

**Direction:** Define a variable through Asha's problem, then connect it to apps the learner uses.

- **Narration:** The fix is a variable. A variable is a name that refers to a value.
  **On screen:** Why this matters
    - A **variable** is a name that refers to a value.
- **Narration:** Asha stores the tea price once, under the name tea price, and uses that name everywhere.
  **On screen:** Why this matters
    - A **variable** is a name that refers to a value.
    - Store the price once, as `tea_price`, and use the name everywhere.
- **Narration:** Change the value in one place, and every calculation follows.
  **On screen:** Why this matters
    - A **variable** is a name that refers to a value.
    - Store the price once, as `tea_price`, and use the name everywhere.
    - Change the value in one place, and every calculation follows.
- **Narration:** Every app you use works like this. Your basket, your game score, your bank balance. Each one is a value with a name.
  **On screen:** Why this matters
    - A **variable** is a name that refers to a value.
    - Store the price once, as `tea_price`, and use the name everywhere.
    - Change the value in one place, and every calculation follows.
    - A basket, a game score, a bank balance: each one is a named value.

## Scene 4: The idea: values, types and names (1:30 to 3:10)

**Section:** The idea

**Direction:** Teach types with the table, then assignment with the diagram, then the label analogy. Then a quiz on types, then a breather.

- **Narration:** First, values. A value is one piece of data, like 3, or 3.5, or the word tea. And every value has a type.
  **On screen:** Table: Every value has a type
- **Narration:** An int is a whole number. Use it for counts, like two cups.
  **On screen:** Table: Every value has a type (row 1 in focus)
- **Narration:** A float has a decimal point. Use it for prices, like 3.5.
  **On screen:** Table: Every value has a type (row 2 in focus)
- **Narration:** A string is text, and it always sits inside quotation marks. Even a digit becomes text when it is in quotation marks.
  **On screen:** Table: Every value has a type (row 3 in focus)
- **Narration:** And a bool is a yes or no fact: True or False. Is Asha a member? True.
  **On screen:** Table: Every value has a type (row 4 in focus)
- **Narration:** Now, names. Assignment connects a name to a value. The name goes on the left, then the equals sign, then the value.
  **On screen:** Assignment: name = value
- **Narration:** Python works out the right side first. Then it connects the name on the left to that value.
  **On screen:** Assignment: name = value
- **Narration:** So read the equals sign as: now refers to. Tea price now refers to 3.
  **On screen:** Assignment: name = value
- **Narration:** Think of a variable as a name label. You stick it on a value, and you can move it to a new value whenever you like.
  **On screen:** A variable is like a name label
    - You stick a label on a value. You can move it to a new value at any time.
- **Narration:** The comparison stops working at one point. Two labels can point to the same value.
  **On screen:** A variable is like a name label
    - You stick a label on a value. You can move it to a new value at any time.
    - Where it stops working: two labels can point to the same value.
- **Narration:** And moving one label does not move the other.
  **On screen:** A variable is like a name label
    - You stick a label on a value. You can move it to a new value at any time.
    - Where it stops working: two labels can point to the same value.
    - Moving one label does not move the other.
- **Narration:** Quick check. Here is the digit 3, inside quotation marks. What is its type?
  **On screen:** Quick check: "What is the type of the value `"3"`, with quotation marks?" (options shown)
- **Interaction:** "What is the type of the value `"3"`, with quotation marks?" stays on screen with a 10-second timer.
- **Narration:** C. A string. The quotation marks make it text. Keep this one in mind. It causes a sneaky bug later.
  **On screen:** Quick check: "What is the type of the value `"3"`, with quotation marks?" (answer revealed: `str`)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - Every value has a type.
    - A variable is a name for a value.
    - Python works out the right side of `=` first.
- **Narration:** Next, Asha creates her first variables.
  **On screen:** Breather card
    - Every value has a type.
    - A variable is a name for a value.
    - Python works out the right side of `=` first.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: First variables (3:10 to 4:31)

**Section:** Build it step by step

**Direction:** The file types itself in. Teach the rule about quotation marks, then ask the prediction, then reveal. Then the naming rules.

- **Narration:** Step 1. Asha creates two variables. Customer refers to the text Asha. Tea price refers to the number 3.
  **On screen:** Code `examples/ex01_first_variables.py`, lines 1 to 3 typed in, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 prints customer. Look closely: there are no quotation marks around it.
  **On screen:** Code `examples/ex01_first_variables.py`, lines 1 to 4 typed in, line 4 highlighted, output hidden
- **Narration:** Without quotation marks, Python treats a word as a name, and prints the value it refers to. And in Python, a star means times.
  **On screen:** Code `examples/ex01_first_variables.py`, lines 1 to 6 typed in, line 5, 6 highlighted, output hidden
- **Interaction:** "What do lines 4, 5 and 6 print?" stays on screen with a 10-second timer.
- **Narration:** Line 4 prints Asha, the value, not the word customer.
  **On screen:** Code `examples/ex01_first_variables.py`, lines 1 to 6 typed in, line 4 highlighted, output `examples/ex01_first_variables.expected`
- **Narration:** And line 6 multiplies the tea price by 2, so two teas cost 6.
  **On screen:** Code `examples/ex01_first_variables.py`, lines 1 to 6 typed in, line 6 highlighted, output `examples/ex01_first_variables.expected`
- **Narration:** Good names make code easy to read. Python has rules for names, and its style guide, called pep eight, adds one more.
  **On screen:** Good names: four rules
- **Narration:** One, from the style guide. Lowercase words, joined with underscores. Tea price, not a short code like t p.
  **On screen:** Good names: four rules
    - Style (PEP 8): lowercase words joined by underscores, `tea_price`, not `TeaPrice` or `tp`.
- **Narration:** Two, a rule of Python itself. Letters, digits and underscores are fine, but a name can never start with a digit.
  **On screen:** Good names: four rules
    - Style (PEP 8): lowercase words joined by underscores, `tea_price`, not `TeaPrice` or `tp`.
    - Letters, digits and underscores, but **never a digit first**.
- **Narration:** Three. Capital letters matter. Price with a small p and Price with a capital P are two different names.
  **On screen:** Good names: four rules
    - Style (PEP 8): lowercase words joined by underscores, `tea_price`, not `TeaPrice` or `tp`.
    - Letters, digits and underscores, but **never a digit first**.
    - Capitals matter: `price` and `Price` are two different names.
- **Narration:** Four. Do not use the words Python keeps for itself, like True, None or class.
  **On screen:** Good names: four rules
    - Style (PEP 8): lowercase words joined by underscores, `tea_price`, not `TeaPrice` or `tp`.
    - Letters, digits and underscores, but **never a digit first**.
    - Capitals matter: `price` and `Price` are two different names.
    - Do not use Python's own words, such as `True`, `None` or `class`.

## Scene 6: Step 2: Check a type (4:31 to 5:10)

**Section:** Build it step by step

**Direction:** Show the four values, teach how Python picks a type, ask, then reveal the type() output.

- **Narration:** Step 2. The type function tells you the type of any value. Asha stores four values from her cafe.
  **On screen:** Code `examples/ex02_types.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** Python picks each type from the way you wrote the value. A decimal point makes a float. Quotation marks make a string.
  **On screen:** Code `examples/ex02_types.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** Lines 6 to 9 print each value, followed by its type.
  **On screen:** Code `examples/ex02_types.py`, line 6, 7, 8, 9 highlighted, output hidden
- **Interaction:** "Which type will Python report for `price` on line 7?" stays on screen with a 10-second timer.
- **Narration:** Float, because 3.5 has a decimal point.
  **On screen:** Code `examples/ex02_types.py`, line 3, 7 highlighted, output `examples/ex02_types.expected`
- **Narration:** And True is a bool. It needs a capital T, or Python will not recognise it.
  **On screen:** Code `examples/ex02_types.py`, line 5, 9 highlighted, output `examples/ex02_types.expected`

## Scene 7: Step 3: Operators (5:10 to 6:12)

**Section:** Build it step by step

**Direction:** Teach what the surprising operators mean first, in general terms. Then the biscuits program, the prediction, and the reveal.

- **Narration:** Step 3. An operator is a symbol that calculates. Plus, minus and times work as you expect. Four others need a closer look.
  **On screen:** Table: Step 3: Operators that surprise beginners
- **Narration:** A single slash divides, and gives the full answer, with decimals. The result is always a float.
  **On screen:** Table: Step 3: Operators that surprise beginners (row 1 in focus)
- **Narration:** A double slash is floor division. It keeps only the whole part of the answer.
  **On screen:** Table: Step 3: Operators that surprise beginners (row 2 in focus)
- **Narration:** The percent sign gives the remainder: what is left over after sharing.
  **On screen:** Table: Step 3: Operators that surprise beginners (row 3 in focus)
- **Narration:** And two stars raise a number to a power.
  **On screen:** Table: Step 3: Operators that surprise beginners (row 4 in focus)
- **Narration:** Asha shares 17 biscuits between 5 friends. Add, subtract and multiply are straightforward.
  **On screen:** Code `examples/ex03_arithmetic.py`, line 4, 5, 6 highlighted, output hidden
- **Narration:** Now use what you learned about the other operators.
  **On screen:** Code `examples/ex03_arithmetic.py`, line 7, 8, 9 highlighted, output hidden
- **Interaction:** "Predict lines 7, 8 and 9: divide, floor divide and remainder." stays on screen with a 10-second timer.
- **Narration:** Divide gives 3.4, the full answer, as a float.
  **On screen:** Code `examples/ex03_arithmetic.py`, line 7 highlighted, output `examples/ex03_arithmetic.expected`
- **Narration:** Floor divide gives 3. Each friend gets three whole biscuits.
  **On screen:** Code `examples/ex03_arithmetic.py`, line 8 highlighted, output `examples/ex03_arithmetic.expected`
- **Narration:** And the remainder is 2. Two biscuits are left over, probably for Asha.
  **On screen:** Code `examples/ex03_arithmetic.py`, line 9 highlighted, output `examples/ex03_arithmetic.expected`

## Scene 8: Step 4: Change a variable (6:12 to 6:49)

**Section:** Build it step by step

**Direction:** Teach the right-side-first rule on line 4, then let the learner apply it to line 6.

- **Narration:** Step 4. Asha runs a loyalty game. Points starts at 10.
  **On screen:** Code `examples/ex04_reassign.py`, lines 1 to 3 typed in, line 2 highlighted, output hidden
- **Narration:** Line 4 looks impossible in maths: points equals points plus 5. But remember the rule. Python works out the right side first.
  **On screen:** Code `examples/ex04_reassign.py`, lines 1 to 5 typed in, line 4 highlighted, output hidden
- **Narration:** So it takes the current value, 10, adds 5, and moves the name to 15.
  **On screen:** Code `examples/ex04_reassign.py`, lines 1 to 5 typed in, line 4 highlighted, output hidden
- **Narration:** Now line 6 doubles it, using the same rule.
  **On screen:** Code `examples/ex04_reassign.py`, lines 1 to 7 typed in, line 6, 7 highlighted, output hidden
- **Interaction:** "What does line 7 print?" stays on screen with a 10-second timer.
- **Narration:** After the bonus, 30. Fifteen, times 2.
  **On screen:** Code `examples/ex04_reassign.py`, lines 1 to 7 typed in, line 6, 7 highlighted, output `examples/ex04_reassign.expected`

## Scene 9: Step 5: Order of operations (6:49 to 8:29)

**Section:** Build it step by step

**Direction:** Teach the order rule, then predict two lines, then the float surprise and round(). Then a quiz and a breather.

- **Narration:** Step 5. When a line has several operators, Python follows the same order as maths.
  **On screen:** Step 5: Which part goes first?
- **Narration:** Powers first.
  **On screen:** Step 5: Which part goes first?
    - First: `**`
- **Narration:** Then times, and every kind of division.
  **On screen:** Step 5: Which part goes first?
    - First: `**`
    - Then: `*`, `/`, `//` and `%`
- **Narration:** Plus and minus come last.
  **On screen:** Step 5: Which part goes first?
    - First: `**`
    - Then: `*`, `/`, `//` and `%`
    - Last: `+` and `-`
- **Narration:** And brackets beat everything. Whatever is inside them is calculated first.
  **On screen:** Step 5: Which part goes first?
    - First: `**`
    - Then: `*`, `/`, `//` and `%`
    - Last: `+` and `-`
    - Brackets go before everything.
- **Narration:** Lines 2 and 3 use the same numbers. Only the brackets are different.
  **On screen:** Code `examples/ex05_order.py`, line 2, 3 highlighted, output hidden
- **Interaction:** "What do lines 2 and 3 print?" stays on screen with a 10-second timer.
- **Narration:** Line 2 multiplies first: 3 times 4 is 12, plus 2 is 14.
  **On screen:** Code `examples/ex05_order.py`, line 2 highlighted, output `examples/ex05_order.expected`
- **Narration:** Line 3 adds first, because of the brackets. 5 times 4 is 20.
  **On screen:** Code `examples/ex05_order.py`, line 3 highlighted, output `examples/ex05_order.expected`
- **Narration:** Line 4 divides first, so you get 8.0. A float, because a single slash always gives one.
  **On screen:** Code `examples/ex05_order.py`, line 4 highlighted, output `examples/ex05_order.expected`
- **Narration:** Now line 5. Point 1, three times, should be point 3. But look! Computers store decimals in binary, so some values carry a tiny error.
  **On screen:** Code `examples/ex05_order.py`, line 5 highlighted, output `examples/ex05_order.expected`
- **Narration:** The round function gives you a rounded number. Here, to two decimal places.
  **On screen:** Code `examples/ex05_order.py`, line 6 highlighted, output `examples/ex05_order.expected`
- **Narration:** Quick check. Two plus four, in brackets, times three. What does it give?
  **On screen:** Quick check: "What does `(2 + 4) * 3` give?" (options shown)
- **Interaction:** "What does `(2 + 4) * 3` give?" stays on screen with a 10-second timer.
- **Narration:** B, 18. The brackets go first: 6, times 3.
  **On screen:** Quick check: "What does `(2 + 4) * 3` give?" (answer revealed: 18)
- **Narration:** Breather. Roll your shoulders. You now have every piece of the mission.
  **On screen:** Breather card
    - `/` gives a `float`; `//` keeps the whole part; `%` gives the rest.
    - The right side of `=` runs first.
    - Brackets control the order.
- **Narration:** Let's put them together into Asha's cafe bill.
  **On screen:** Breather card
    - `/` gives a `float`; `//` keeps the whole part; `%` gives the rest.
    - The right side of `=` runs first.
    - Brackets control the order.
- **Breather:** 4 quiet seconds.

## Scene 10: See the outcome: the self-updating bill (8:29 to 9:30)

**Section:** See the outcome

**Direction:** Return to the mission. Walk the three groups of lines, reveal, then ask the change question. Hand over to the AI story.

- **Narration:** Back to the mission, with the new prices: tea is 3.5, and a sandwich is 6. Lines 2 to 7 store every price and fact once.
  **On screen:** Code `examples/ex06_cafe_bill.py`, line 2, 3, 4, 5, 6, 7 highlighted, output hidden
- **Narration:** Lines 9 to 12 calculate. Each line uses the names above it: the tea total, the bill, a 10 percent member discount, and the amount to pay.
  **On screen:** Code `examples/ex06_cafe_bill.py`, line 9, 10, 11, 12 highlighted, output hidden
- **Narration:** Lines 14 to 20 print the bill. Asha runs it.
  **On screen:** Code `examples/ex06_cafe_bill.py`, line 14, 15, 16, 17, 18, 19, 20 highlighted, output `examples/ex06_cafe_bill.expected`
- **Narration:** Notice the tea total is 7.0, a float, because the tea price was a float.
  **On screen:** Code `examples/ex06_cafe_bill.py`, line 9, 15 highlighted, output `examples/ex06_cafe_bill.expected`
- **Interaction:** "Asha changes `tea_price` to 4.5. Which output lines change?" stays on screen with a 10-second timer.
- **Narration:** Four lines change: the teas line, the bill, the discount and the amount to pay. Every line that depends on the tea price.
  **On screen:** Code `examples/ex06_cafe_bill.py`, line 3 highlighted, output `examples/ex06_cafe_bill.expected`
- **Narration:** And she changed only one number. Mission complete!
  **On screen:** Code `examples/ex06_cafe_bill.py`, output `examples/ex06_cafe_bill.expected`
- **Narration:** Then the cafe owner has a new question. What is the average bill of three tables? Asha decides to build it with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex06_cafe_bill.py`, output `examples/ex06_cafe_bill.expected`

## Scene 11: Work with AI: six stages, one average (9:30 to 13:08)

**Section:** Work with AI

**Direction:** Safety first. Then one conversation per stage, all about the average bill. Stage 3 plants the mistake, stage 4 catches it, stage 6 catches a second one.

- **Narration:** This chapter's AI skill is prediction.
  **On screen:** This chapter's AI skill: prediction
- **Narration:** Write your own prediction, ask the AI for its prediction, then run the code.
  **On screen:** This chapter's AI skill: prediction
    - Write your own prediction. Ask the AI for its prediction. Then run the code.
- **Narration:** The real output is the only answer that counts.
  **On screen:** This chapter's AI skill: prediction
    - Write your own prediction. Ask the AI for its prediction. Then run the code.
    - The real output is the only answer that counts.
- **Narration:** And the safety habits from Chapter 1 still apply. No passwords, no private data, and you are responsible for the code.
  **On screen:** This chapter's AI skill: prediction
    - Write your own prediction. Ask the AI for its prediction. Then run the code.
    - The real output is the only answer that counts.
    - Never paste passwords, keys or private data. You are responsible for the code you use.
- **Narration:** Stage 1: plan. Asha describes the average in words, and asks for the variables she needs. No code yet.
  **On screen:** AI chat, stage 1: Plan the variables first
    - You: I am a beginner learning Python variables. I want the average bill of three cafe tables: 18, 24 and 30. Do not write code yet. List the variables I need, with a snake_case name and a type for each.
- **Narration:** The AI lists three bills as ints, and an average as a float. That matches the rule you learned: a single slash always gives a float.
  **On screen:** AI chat, stage 1: Plan the variables first
    - You: I am a beginner learning Python variables. I want the average bill of three cafe tables: 18, 24 and 30. Do not write code yet. List the variables I need, with a snake_case name and a type for each.
    - AI (example answer): 1. `bill_1`, `bill_2` and `bill_3`: type `int`, values 18, 24 and 30. 2. `average`: the sum of the three bills divided by 3. Its type is `float`, because `/` always gives a `float`.
- **Narration:** Stage 2: write. Asha writes the first three lines herself, one bill per table. She asks the AI to check her names and the types, without changing anything.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote the first lines myself. Do not change them. Do my names follow PEP 8, and what type is each value? [code `examples/ai_average_fixed.py`]
- **Narration:** The AI agrees. The names follow the style rule, and each bill is an int, a whole number. Asha predicted the same.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote the first lines myself. Do not change them. Do my names follow PEP 8, and what type is each value? [code `examples/ai_average_fixed.py`]
    - AI (example answer): Yes. All three names are lowercase words joined by underscores. Each value is an `int`, because it is a whole number with no decimal point.
- **Narration:** Stage 3: generate. Asha asks the AI to complete her program with the average, and to say exactly what it prints.
  **On screen:** AI chat, stage 3: Generate: ask for the exact output
    - You: Now complete my program. Keep my three bill lines, add a line that finds the average of the bills with the name average, and print it. Tell me exactly what it prints.
- **Narration:** The AI writes the program, and says it prints 24.0. It sounds sure.
  **On screen:** AI chat, stage 3: Generate: ask for the exact output
    - You: Now complete my program. Keep my three bill lines, add a line that finds the average of the bills with the name average, and print it. Tell me exactly what it prints.
    - AI (example answer): Here is the program. It prints `Average bill: 24.0`. [code `examples/ai_average_flawed.py`]
- **Narration:** Look at line 5. You learned which part Python calculates first.
  **On screen:** AI chat, stage 3: Generate: ask for the exact output
    - You: Now complete my program. Keep my three bill lines, add a line that finds the average of the bills with the name average, and print it. Tell me exactly what it prints.
    - AI (example answer): Here is the program. It prints `Average bill: 24.0`. [code `examples/ai_average_flawed.py`]
- **Interaction:** "The AI says this prints `Average bill: 24.0`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** Asha runs it. 52.0! The AI was wrong, and it sounded completely sure.
  **On screen:** AI chat, stage 3: Generate: ask for the exact output
    - You: Now complete my program. Keep my three bill lines, add a line that finds the average of the bills with the name average, and print it. Tell me exactly what it prints.
    - AI (example answer): Here is the program. It prints `Average bill: 24.0`. [code `examples/ai_average_flawed.py`]
    - You: I ran it. This is what it printed:
- **Narration:** Stage 4: test. Here is a quick sense check for any average. It must lie between the smallest and the largest value. The largest bill is 30, so 52 is impossible.
  **On screen:** AI chat, stage 4: Test: is the result even possible?
    - You: You predicted 24.0, but it printed 52.0. An average must lie between the smallest and the largest bill, and the largest is 30. What is wrong?
- **Narration:** She tells the AI what it predicted and what really happened. Now it names the cause: Python divided before it added. Brackets fix the order.
  **On screen:** AI chat, stage 4: Test: is the result even possible?
    - You: You predicted 24.0, but it printed 52.0. An average must lie between the smallest and the largest bill, and the largest is 30. What is wrong?
    - AI (example answer): Python divides before it adds, so only `bill_3` was divided by 3. Put brackets around the sum: [code `examples/ai_average_fixed.py`]
- **Narration:** Asha runs the fixed version. 24.0. Now the prediction and the real run agree.
  **On screen:** AI chat, stage 4: Test: is the result even possible?
    - You: You predicted 24.0, but it printed 52.0. An average must lie between the smallest and the largest bill, and the largest is 30. What is wrong?
    - AI (example answer): Python divides before it adds, so only `bill_3` was divided by 3. Put brackets around the sum: [code `examples/ai_average_fixed.py`]
    - You: I ran the fixed program:
- **Narration:** Stage 5: debug. Asha types the program into her own file, and Python stops with a Name Error. She pastes the code and the full error.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I typed the program again in my own file and got this error. First explain what it means and which line causes it. Then show the smallest fix. [code `examples/ai_bills_typo.py`]
- **Narration:** She asks for the cause first. The AI points to line 6: averge, with a missing letter. Python only knows the names you created.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I typed the program again in my own file and got this error. First explain what it means and which line causes it. Then show the smallest fix. [code `examples/ai_bills_typo.py`]
    - AI (example answer): It is a `NameError` on line 6. You created `average`, but line 6 uses `averge`, with a missing letter. Python only knows the names you created. The fix: change `averge` to `average`.
- **Narration:** Stage 6: improve. The program works. Asha asks for at most two improvements to her names.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Review my names. Suggest at most two improvements, each with one reason. Do not change what the program prints. [code `examples/ai_average_fixed.py`]
- **Narration:** Suggestion 1 is good. Average bill tells a reader what the average is about. Suggestion 2 says: use a double slash, for a cleaner number.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Review my names. Suggest at most two improvements, each with one reason. Do not change what the program prints. [code `examples/ai_average_fixed.py`]
    - AI (example answer): 1. Rename `average` to `average_bill`, so a reader knows what it is the average of. 2. Use `//` instead of `/`. Bills are whole numbers, so the average will be cleaner.
- **Narration:** But a double slash keeps only the whole part. Asha tests it with new bills. The double slash drops the point 3 3 3. The AI was wrong again.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Review my names. Suggest at most two improvements, each with one reason. Do not change what the program prints. [code `examples/ai_average_fixed.py`]
    - AI (example answer): 1. Rename `average` to `average_bill`, so a reader knows what it is the average of. 2. Use `//` instead of `/`. Bills are whole numbers, so the average will be cleaner.
    - You: Suggestion 2 would change the output. I tested it with a bill of 31 instead of 30: [code `examples/ai_floor_check.py`]
- **Narration:** So Asha keeps suggestion 1 only. Here is the result: a clear name, brackets around the sum, and a single slash.
  **On screen:** Code `examples/ai_average_final.py`, line 5 highlighted, output `examples/ai_average_final.expected`
- **Narration:** The AI helped at every stage. And at every stage, Asha checked its answer herself. Two mistakes caught!
  **On screen:** Code `examples/ai_average_final.py`, line 5 highlighted, output `examples/ai_average_final.expected`
- **Narration:** Quick check. You and an AI predict different outputs. What decides who is right?
  **On screen:** Quick check: "You and an AI predict different outputs. What decides who is right?" (options shown)
- **Interaction:** "You and an AI predict different outputs. What decides who is right?" stays on screen with a 10-second timer.
- **Narration:** C. The real run. Always.
  **On screen:** Quick check: "You and an AI predict different outputs. What decides who is right?" (answer revealed: The real output when you run the code)
- **Narration:** Breather. You watched Asha use AI at all six stages, and catch two mistakes with what you learned today.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - An average must lie between the smallest and largest value.
    - Test every AI suggestion before you accept it.
- **Narration:** Next, the four mistakes every beginner makes with variables. You have already met the first one.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - An average must lie between the smallest and largest value.
    - Test every AI suggestion before you accept it.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes (13:08 to 15:46)

**Section:** Common mistakes

**Direction:** Mistake 1 calls back to the debug stage. Mistake 2 pays off the quiz about quotation marks. Mistakes 3 and 4 are spot-it questions on rules taught earlier.

- **Narration:** Mistake 1 is the one Asha debugged. A name with a typing error. Line 3 printed fine.
  **On screen:** Code `examples/err01_name_typo.py`, line 3 highlighted, error `examples/err01_name_typo.expected_error`
- **Narration:** Line 4 spells it with an s, so Python stops with a Name Error. It even suggests the right name.
  **On screen:** Code `examples/err01_name_typo.py`, line 4 highlighted, error `examples/err01_name_typo.expected_error`
- **Narration:** You also get this error if you use a name before the line that creates it.
  **On screen:** Code `examples/err01_name_typo.py`, line 4 highlighted, error `examples/err01_name_typo.expected_error`
- **Narration:** Mistake 2. Remember the quick check? A digit in quotation marks is a string, not a number.
  **On screen:** Code `examples/err02_text_number.py`, line 2 highlighted, error `examples/err02_text_number.expected_error`
- **Narration:** Concatenate means join. Python can only join text to text, so it stops with a Type Error.
  **On screen:** Code `examples/err02_text_number.py`, line 3 highlighted, error `examples/err02_text_number.expected_error`
- **Narration:** The fix: remove the quotation marks.
  **On screen:** Code `examples/err02_text_number.py`, line 3 highlighted, error `examples/err02_text_number.expected_error`
- **Narration:** Sometimes this mistake gives no error at all, which is worse. Multiplying a string by 2 repeats the text. So you get 33, not 6.
  **On screen:** Code `examples/ex07_text_times.py`, line 2, 3 highlighted, output `examples/ex07_text_times.expected`
- **Narration:** Without quotation marks, you get 6. If a result looks strange, check its type.
  **On screen:** Code `examples/ex07_text_times.py`, line 4, 5 highlighted, output `examples/ex07_text_times.expected`
- **Narration:** Now you try. Remember the four naming rules from step 1.
  **On screen:** Code `examples/err03_digit_first.py`, line 2 highlighted, output hidden
- **Interaction:** "What is wrong with the name on line 2?" stays on screen with a 10-second timer.
- **Narration:** It starts with a digit. Python reads the 2 as the start of a number, and gets confused by the letters after it.
  **On screen:** Code `examples/err03_digit_first.py`, line 2 highlighted, error `examples/err03_digit_first.expected_error`
- **Narration:** The fix: start with a letter, like second place.
  **On screen:** Code `examples/err03_digit_first.py`, line 2 highlighted, error `examples/err03_digit_first.expected_error`
- **Narration:** One more. Think about the assignment diagram from the idea section.
  **On screen:** Code `examples/err04_reversed.py`, line 2 highlighted, output hidden
- **Interaction:** "What is wrong with line 2?" stays on screen with a 10-second timer.
- **Narration:** The name and the value are on the wrong sides. The name always goes on the left.
  **On screen:** Code `examples/err04_reversed.py`, line 2 highlighted, error `examples/err04_reversed.expected_error`
- **Narration:** Ten is a literal: a value written straight into the code. A literal cannot be given a new value.
  **On screen:** Code `examples/err04_reversed.py`, line 2 highlighted, error `examples/err04_reversed.expected_error`
- **Narration:** Here are all four, by the last line of the error.
  **On screen:** Table: Read the last line first
- **Narration:** Not defined: a typing error in a name.
  **On screen:** Table: Read the last line first (row 1 in focus)
- **Narration:** Can only concatenate: a number stored as text.
  **On screen:** Table: Read the last line first (row 2 in focus)
- **Narration:** Invalid decimal literal: a name that starts with a digit.
  **On screen:** Table: Read the last line first (row 3 in focus)
- **Narration:** Cannot assign to literal: the name is on the wrong side.
  **On screen:** Table: Read the last line first (row 4 in focus)
- **Narration:** Quick check. Which of these is a valid variable name?
  **On screen:** Quick check: "Which of these is a valid variable name?" (options shown)
- **Interaction:** "Which of these is a valid variable name?" stays on screen with a 10-second timer.
- **Narration:** B. Second place, with an underscore. No digit first, no space, and not one of Python's own words.
  **On screen:** Quick check: "Which of these is a valid variable name?" (answer revealed: `second_place`)
- **Narration:** Last breather. These four errors will not scare you any more.
  **On screen:** Breather card
    - Spell names exactly as you created them.
    - Quotation marks make text.
    - The name goes on the left.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - Spell names exactly as you created them.
    - Quotation marks make text.
    - The name goes on the left.
- **Breather:** 4 quiet seconds.

## Scene 13: Think beyond (15:46 to 16:32)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Four friends share a bill of 50. How could floor division and the remainder tell you what each person pays, and what is left over?
  **On screen:** Question card: "Four friends share a bill of 50. How do `//` and `%` tell you what each pays, and what is left over?"
- **Interaction:** "Four friends share a bill of 50. How do `//` and `%` tell you what each pays, and what is left over?" stays on screen with a 10-second timer.
- **Narration:** Write it and run it after the video.
  **On screen:** Question card: "Four friends share a bill of 50. How do `//` and `%` tell you what each pays, and what is left over?"
- **Narration:** Second. A is 5 and b is 8. You write: a equals b, then b equals a. Why are they not swapped?
  **On screen:** Question card: "`a = 5` and `b = 8`. Why does `a = b`, then `b = a`, fail to swap them?"
- **Interaction:** "`a = 5` and `b = 8`. Why does `a = b`, then `b = a`, fail to swap them?" stays on screen with a 10-second timer.
- **Narration:** Predict it, test it, then find a fix that uses a third variable.
  **On screen:** Question card: "`a = 5` and `b = 8`. Why does `a = b`, then `b = a`, fail to swap them?"

## Scene 14: Recap (16:32 to 17:36)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap.
  **On screen:** Recap
- **Narration:** A value is a piece of data, and every value has a type.
  **On screen:** Recap
    - A value is a piece of data, and every value has a type.
- **Narration:** A variable is a name for a value. The name goes on the left.
  **On screen:** Recap
    - A value is a piece of data, and every value has a type.
    - A variable is a name for a value. `=` connects the name on the left to the value on the right.
- **Narration:** Python works out the right side first, so a variable can use its own old value.
  **On screen:** Recap
    - A value is a piece of data, and every value has a type.
    - A variable is a name for a value. `=` connects the name on the left to the value on the right.
    - Python works out the right side first, so `points = points + 5` is valid.
- **Narration:** A single slash gives a float. A double slash keeps the whole part, and the percent sign gives the remainder.
  **On screen:** Recap
    - A value is a piece of data, and every value has a type.
    - A variable is a name for a value. `=` connects the name on the left to the value on the right.
    - Python works out the right side first, so `points = points + 5` is valid.
    - `/` always gives a `float`. `//` keeps the whole part; `%` gives the remainder.
- **Narration:** Brackets control the order, and round tidies an inexact float.
  **On screen:** Recap
    - A value is a piece of data, and every value has a type.
    - A variable is a name for a value. `=` connects the name on the left to the value on the right.
    - Python works out the right side first, so `points = points + 5` is valid.
    - `/` always gives a `float`. `//` keeps the whole part; `%` gives the remainder.
    - Brackets control the order. `round()` tidies an inexact `float`.
- **Narration:** And with AI: predict, ask, and let the real run decide.
  **On screen:** Recap
    - A value is a piece of data, and every value has a type.
    - A variable is a name for a value. `=` connects the name on the left to the value on the right.
    - Python works out the right side first, so `points = points + 5` is valid.
    - `/` always gives a `float`. `//` keeps the whole part; `%` gives the remainder.
    - Brackets control the order. `round()` tidies an inexact `float`.
    - Predict, ask the AI to predict, and let the real run decide.
- **Narration:** One last check. Tea price is 3.5, and tea count is 2. What type is the tea price times the tea count?
  **On screen:** Quick check: "`tea_price = 3.5` and `tea_count = 2`. What type is `tea_price * tea_count`?" (options shown)
- **Interaction:** "`tea_price = 3.5` and `tea_count = 2`. What type is `tea_price * tea_count`?" stays on screen with a 10-second timer.
- **Narration:** B. A float. One part was a float, so the result is 7.0, exactly like Asha's bill.
  **On screen:** Quick check: "`tea_price = 3.5` and `tea_count = 2`. What type is `tea_price * tea_count`?" (answer revealed: `float`)
- **Narration:** Mission complete! You earned 100 XP and the Name Keeper badge.
  **On screen:** Name Keeper You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice (17:36 to 18:02)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. The practice file has eight tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including a savings tracker.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's temperature converter, like Asha fixed the average.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Predict first, then run. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 16: What's next (18:02 to 18:26)

**Section:** What's next

**Direction:** End card. Tease f-strings as the fix for the bill's awkward spacing. Hold quietly at the end.

- **Narration:** Look at Asha's bill once more. Teas, 2, x, 3.5, equals 7.0. All those separate pieces and spaces look a little clumsy.
  **On screen:** Working with Text: Strings and f-strings Build clear messages with f-strings.
- **Narration:** In Chapter 3, you will join text and build clear messages from your variables, with f-strings.
  **On screen:** Working with Text: Strings and f-strings Build clear messages with f-strings.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Working with Text: Strings and f-strings Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 3.
  **On screen:** Working with Text: Strings and f-strings Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
