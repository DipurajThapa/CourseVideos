# Video Script: Chapter 2, Values and Variables: Giving Data a Name

Target length: about 5 minutes. Format: landscape 1920x1080. Uses only code and output verified in this chapter.

## Scene 1: Hook

**Duration:** 20 seconds

**Narration:** An AI assistant said this code prints an average of 90. We ran it. It printed 203. The AI was sure, and it was wrong. By the end of this video, you will spot the problem in two seconds.

**On screen:** The code `ai_average_flawed.py` and a speech bubble: "This prints Average: 90.0". Then the real output `Average: 203.33333333333334` appears in red.

**Interaction:** On-screen question: "Can you find the bug before the end?"

## Scene 2: Why

**Duration:** 25 seconds

**Narration:** In Chapter 1, our cafe receipt typed every price twice. Change the price of tea, and you must change it everywhere. Variables fix this. You store a value once, give it a name and use the name everywhere.

**On screen:** The Chapter 1 receipt with the two copies of each price highlighted. Then one line, `tea_price = 3`, with arrows to every place that uses it.

**Interaction:** None. The progress map shows "Chapter 2 of 28".

## Scene 3: Mental model

**Duration:** 40 seconds

**Narration:** Every value has a type. Whole numbers are int. Numbers with a decimal point are float. Text in quotation marks is str. True and False are bool. A variable is a name label on a value. Python works out the right side of the equals sign first, then sticks the label on the result.

**On screen:** The four-row type table from the lesson. Then the assignment diagram: `tea_price = 3`, with an arrow from the value back to the name.

**Interaction:** Quick quiz: "What type is "3" with quotation marks?" A three-second countdown, then the answer: `str`.

## Scene 4: Build

**Duration:** 70 seconds

**Narration:** Seventeen biscuits, five friends. Plus, minus and times work as you expect. Slash gives the exact answer, 3.4, and it is always a float. Double slash gives whole biscuits each: 3. Percent gives what is left: 2. Now a score. Points equals points plus five. Python takes the old value, adds five and stores the new value.

**On screen:** `ex03_arithmetic.py` with each output line appearing after its code line. Then `ex04_reassign.py`, with the value of `points` shown in a box that changes from 10 to 15 to 30.

**Interaction:** Pause card: "Predict the floor divide and remainder lines. Pause now." A five-second countdown, then the reveal.

## Scene 5: Outcome

**Duration:** 35 seconds

**Narration:** Here is the cafe bill with variables. Every price appears once. Change the tea price, run it again, and every total updates. Notice that 7.0 has a decimal point. A float in a calculation makes the result a float.

**On screen:** `ex06_cafe_bill.py` on the left and its output on the right. The value `3.5` is highlighted, then `7.0` in the output glows.

**Interaction:** On-screen question: "Which variable would you change if the sandwich price went up?"

## Scene 6: AI pair moment

**Duration:** 45 seconds

**Narration:** Back to the average. Python divides before it adds. So it divided only the last score by three, then added the others. Brackets fix the order. Now it prints 90.0. Here is a two-second check: an average must sit between the lowest and highest values. 203 cannot be right.

**On screen:** `ai_average_flawed.py` with `score_3 / 3` highlighted. Then `ai_average_fixed.py` with the brackets highlighted and the output `Average: 90.0`. Then the habit card: "Predict. Run. Compare."

**Interaction:** On-screen question: "Where would you put the brackets?" A four-second countdown before the fix appears.

## Scene 7: Think beyond

**Duration:** 30 seconds

**Narration:** A typing mistake in a name gives a NameError, and Python suggests the right name. A number in quotation marks is text, so 3 times 2 can print 33. Now try this. You want to swap the values of a and b. Why does a equals b, then b equals a, not work?

**On screen:** `err01_name_typo.py` with the last error line highlighted. Then `ex07_text_times.py` with the output `33` and `6`. Then the swap question card.

**Interaction:** Prompt: "Test your idea, then post your fix in the comments."

## Scene 8: Recap

**Duration:** 20 seconds

**Narration:** Values have types. Variables are names for values. Python works out the right side first. Slash gives a float, double slash gives whole parts and percent gives the remainder. Predict, run and compare. You earned 100 XP and the Name Keeper badge. Next, working with text.

**On screen:** Five recap lines appear one by one. The XP bar fills to 200 in total. The Name Keeper badge appears. The progress map moves to Chapter 3.

**Interaction:** End card: "Do the warm-up tasks now. They take ten minutes."
