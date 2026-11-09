# Video Script: Chapter 5: Boss Level 1: The Bill Splitter

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 15:28.

## Scene 1: Introduction (0:00 to 1:13)

**Section:** Introduction

**Direction:** Boss level title, then the table argument as the hook, with one question a learner can answer. No code yet.

- **Narration:** Welcome to Code Quest, Chapter 5. This is your first boss level!
  **On screen:** The Bill Splitter
- **Narration:** No new topic today. You will build a real tool with everything from Chapters 1 to 4.
  **On screen:** The Bill Splitter Plan it. Build it. Test it.
- **Narration:** And an AI assistant will make two confident mistakes about money. Your tests will catch both.
  **On screen:** The Bill Splitter Plan it. Build it. Test it.
- **Narration:** Four friends finish lunch at the Corner Cafe. The bill is 37.45. With a 15 percent tip, the receipt says 43.07, to the cent.
  **On screen:** Four friends, one bill
    - The bill is 37.45, plus a 15% tip. The receipt says 43.07.
- **Narration:** One friend divides 43.07 by 4 on a phone calculator. Each person pays 10.7675.
  **On screen:** Four friends, one bill
    - The bill is 37.45, plus a 15% tip. The receipt says 43.07.
    - A phone calculator says each friend pays **10.7675**.
- **Narration:** Nobody can pay that. So they round it, and each friend pays 10.77.
  **On screen:** Four friends, one bill
    - The bill is 37.45, plus a 15% tip. The receipt says 43.07.
    - A phone calculator says each friend pays **10.7675**.
    - Nobody can pay 10.7675. So each friend pays **10.77**.
- **Narration:** So how much do they pay together?
  **On screen:** Four friends, one bill
    - The bill is 37.45, plus a 15% tip. The receipt says 43.07.
    - A phone calculator says each friend pays **10.7675**.
    - Nobody can pay 10.7675. So each friend pays **10.77**.
    - 10.77 + 10.77 + 10.77 + 10.77 = ?
- **Interaction:** "Four friends each pay 10.77. How much do they pay together?" stays on screen with a 10-second timer.
- **Narration:** 43.08. That is one cent more than the real total, 43.07. Somebody paid a cent too much, and nobody knows who.
  **On screen:** Four friends, one bill
    - The bill is 37.45, plus a 15% tip. The receipt says 43.07.
    - A phone calculator says each friend pays **10.7675**.
    - Nobody can pay 10.7675. So each friend pays **10.77**.
    - 10.77 + 10.77 + 10.77 + 10.77 = ?
- **Narration:** Small? Yes. But a cafe serves hundreds of tables. Asha wants a tool that gets it right every time.
  **On screen:** Four friends, one bill
    - The bill is 37.45, plus a 15% tip. The receipt says 43.07.
    - A phone calculator says each friend pays **10.7675**.
    - Nobody can pay 10.7675. So each friend pays **10.77**.
    - 10.77 + 10.77 + 10.77 + 10.77 = ?

## Scene 2: The mission (1:13 to 1:53)

**Section:** The mission

**Direction:** State the mission, then the table of what each earlier chapter contributes, row by row.

- **Narration:** Here is the mission. Asha's tool asks three questions: the bill, the tip percent and the number of people.
  **On screen:** Build a fair bill splitter
    - Ask three questions: the bill, the tip percent, the number of people.
- **Narration:** It prints a neat receipt, like the one from Chapter 3.
  **On screen:** Build a fair bill splitter
    - Ask three questions: the bill, the tip percent, the number of people.
    - Print a neat receipt with the bill, the tip and the total.
- **Narration:** It tells each person exactly what to pay.
  **On screen:** Build a fair bill splitter
    - Ask three questions: the bill, the tip percent, the number of people.
    - Print a neat receipt with the bill, the tip and the total.
    - Tell each person exactly what to pay.
- **Narration:** And if the money does not share out evenly, it says how many cents are left over.
  **On screen:** Build a fair bill splitter
    - Ask three questions: the bill, the tip percent, the number of people.
    - Print a neat receipt with the bill, the tip and the total.
    - Tell each person exactly what to pay.
    - Say how many cents are left over, so the table can decide who pays them.
- **Narration:** And you already know every piece.
  **On screen:** Table: Everything you need, you already know
- **Narration:** From Chapter 1, print, and the top to bottom order.
  **On screen:** Table: Everything you need, you already know (row 1 in focus)
- **Narration:** From Chapter 2, variables, division with one slash and two slashes, and the remainder operator.
  **On screen:** Table: Everything you need, you already know (row 2 in focus)
- **Narration:** From Chapter 3, f strings for neat columns.
  **On screen:** Table: Everything you need, you already know (row 3 in focus)
- **Narration:** And from Chapter 4, questions with input, and converting the answers.
  **On screen:** Table: Everything you need, you already know (row 4 in focus)

## Scene 3: What you will build (1:53 to 2:21)

**Section:** What you will build

**Direction:** Show the finished run as the destination. The learner does not need to read the code yet.

- **Narration:** Here is where we are going. You do not need to read the code yet. Look at the output on the right.
  **On screen:** Code `project/bill_splitter.py`, output `project/bill_splitter.expected`
- **Narration:** Three friends share a bill of 48, with a 10 percent tip. The tool asks three questions.
  **On screen:** Code `project/bill_splitter.py`, output `project/bill_splitter.expected`
- **Narration:** Then it prints the bill, the tip and the total, lined up in one column, 24 characters wide.
  **On screen:** Code `project/bill_splitter.py`, output `project/bill_splitter.expected`
- **Narration:** Each person pays 17.60, and there are no extra cents this time.
  **On screen:** Code `project/bill_splitter.py`, output `project/bill_splitter.expected`
- **Narration:** About twenty lines of code. By the end of this video, you will understand every one.
  **On screen:** Code `project/bill_splitter.py`, output `project/bill_splitter.expected`

## Scene 4: Acceptance criteria (2:21 to 3:38)

**Section:** Acceptance criteria

**Direction:** Six criteria, revealed one by one. Then a quiz on the types, then a breather.

- **Narration:** Before building, Asha writes down what done means. These are called acceptance criteria. The tool is finished when all six are true.
  **On screen:** Done means all six are true
- **Narration:** One. It asks the three questions, in this order.
  **On screen:** Done means all six are true
    - Asks for the bill, the tip percent and the number of people.
- **Narration:** Two. The bill can have decimals, like 37.45. The tip percent and the number of people are whole numbers.
  **On screen:** Done means all six are true
    - Asks for the bill, the tip percent and the number of people.
    - The bill can have decimals. The tip percent and people are whole numbers.
- **Narration:** Three. Money shows two decimal places, lined up.
  **On screen:** Done means all six are true
    - Asks for the bill, the tip percent and the number of people.
    - The bill can have decimals. The tip percent and people are whole numbers.
    - Shows the bill, the tip and the total with two decimal places, in one column.
- **Narration:** Four. Each share is rounded down to a whole cent.
  **On screen:** Done means all six are true
    - Asks for the bill, the tip percent and the number of people.
    - The bill can have decimals. The tip percent and people are whole numbers.
    - Shows the bill, the tip and the total with two decimal places, in one column.
    - Shows what each person pays, rounded down to a whole cent.
- **Narration:** Five. The extra cents are shown, so the shares and the extra cents add up to the total exactly.
  **On screen:** Done means all six are true
    - Asks for the bill, the tip percent and the number of people.
    - The bill can have decimals. The tip percent and people are whole numbers.
    - Shows the bill, the tip and the total with two decimal places, in one column.
    - Shows what each person pays, rounded down to a whole cent.
    - Shows the extra cents. Shares plus extra cents equal the total exactly.
- **Narration:** And six. It passes at least four tests that you worked out by hand.
  **On screen:** Done means all six are true
    - Asks for the bill, the tip percent and the number of people.
    - The bill can have decimals. The tip percent and people are whole numbers.
    - Shows the bill, the tip and the total with two decimal places, in one column.
    - Shows what each person pays, rounded down to a whole cent.
    - Shows the extra cents. Shares plus extra cents equal the total exactly.
    - Passes at least four tests worked out by hand.
- **Narration:** Quick check, using criterion two. Which answer should the program convert with float?
  **On screen:** Quick check: "Which answer should the program convert with `float()`?" (options shown)
- **Interaction:** "Which answer should the program convert with `float()`?" stays on screen with a 10-second timer.
- **Narration:** A. The bill total. It can have decimals. The other two are whole numbers, so they use int.
  **On screen:** Quick check: "Which answer should the program convert with `float()`?" (answer revealed: The bill total)
- **Narration:** Take a breather. You know the problem, the mission and what done means.
  **On screen:** Breather card
    - Rounding each share can lose a cent.
    - The tool asks three questions.
    - Six criteria say when it is done.
- **Narration:** Next, Asha plans the tool with an AI assistant, before she writes any code.
  **On screen:** Breather card
    - Rounding each share can lose a cent.
    - The tool asks three questions.
    - Six criteria say when it is done.
- **Breather:** 4 quiet seconds.

## Scene 5: Plan it with AI (3:38 to 4:45)

**Section:** Plan it with AI

**Direction:** Stage 1 plan, then Asha adds the whole-cents step, then stage 2: she writes the questions and asks the AI to check them.

- **Narration:** Stage 1: plan. Asha tells the AI what she knows, and what she wants. And she says: no code yet.
  **On screen:** AI chat, stage 1: Plan: no code yet
    - You: I am a beginner. I know print, variables, int and float, the operators including // and %, f-strings and input. I want a program that splits a cafe bill between friends with a tip. Do not write code. List the inputs, the calculations in order and the outputs.
- **Narration:** The AI lists the inputs with their types, the calculations in order, and the outputs. It is a good plan.
  **On screen:** AI chat, stage 1: Plan: no code yet
    - You: I am a beginner. I know print, variables, int and float, the operators including // and %, f-strings and input. I want a program that splits a cafe bill between friends with a tip. Do not write code. List the inputs, the calculations in order and the outputs.
    - AI (example answer): Inputs: the bill total (`float`), the tip percent (`int`) and the number of people (`int`). Calculations: the tip, then the total, then each share: the total divided by the people. Outputs: the bill, the tip, the total and each share, with two decimal places.
- **Narration:** But look at the last calculation: each share is the total, divided by the people. That is exactly what the phone calculator did.
  **On screen:** AI chat, stage 1: Plan: no code yet
    - You: I am a beginner. I know print, variables, int and float, the operators including // and %, f-strings and input. I want a program that splits a cafe bill between friends with a tip. Do not write code. List the inputs, the calculations in order and the outputs.
    - AI (example answer): Inputs: the bill total (`float`), the tip percent (`int`) and the number of people (`int`). Calculations: the tip, then the total, then each share: the total divided by the people. Outputs: the bill, the tip, the total and each share, with two decimal places.
- **Narration:** Asha remembers the mission. 43.07 divided by 4 is 10.7675, and nobody can pay that.
  **On screen:** Asha adds one step
    - 43.07 divided by 4 is 10.7675: not a real amount of money.
- **Narration:** So she adds one step to the plan: work in whole cents. 43.07 is 4307 cents.
  **On screen:** Asha adds one step
    - 43.07 divided by 4 is 10.7675: not a real amount of money.
    - So work in **whole cents**: 43.07 is 4307 cents.
- **Narration:** Whole numbers share out with double slash, and the remainder operator gives what is left over. You did this with biscuits in Chapter 2.
  **On screen:** Asha adds one step
    - 43.07 divided by 4 is 10.7675: not a real amount of money.
    - So work in **whole cents**: 43.07 is 4307 cents.
    - Whole cents share out with `//`, and `%` gives the cents left over.
- **Narration:** Stage 2: write. Asha writes the three questions herself. Then she asks the AI to check the types, without changing anything.
  **On screen:** AI chat, stage 2: Write the questions, then ask for a check
    - You: I wrote the three questions myself. Do not change them. For each answer, tell me its type and whether that type fits what people will type. [code `project/bill_splitter.py`]
- **Narration:** The AI agrees with her: a float for the bill, and an int for the tip percent and for the people. You cannot have half a person!
  **On screen:** AI chat, stage 2: Write the questions, then ask for a check
    - You: I wrote the three questions myself. Do not change them. For each answer, tell me its type and whether that type fits what people will type. [code `project/bill_splitter.py`]
    - AI (example answer): Line 3: `float`, because a bill can have decimals, such as 37.45. Line 4: `int`, because a tip percent such as 10 is a whole number. Line 5: `int`, because you cannot have half a person.

## Scene 6: Step 1: The questions (4:45 to 5:24)

**Section:** Build it step by step

**Direction:** The questions with a type check. Ask about the type of people, then reveal.

- **Narration:** Time to build. Line 2 prints a centred header, with equals signs, as in Chapter 3.
  **On screen:** Code `examples/ex01_questions.py`, line 2 highlighted, output hidden
- **Narration:** Lines 3 to 5 ask the three questions. Each answer is converted as soon as it is read.
  **On screen:** Code `examples/ex01_questions.py`, line 3, 4, 5 highlighted, output hidden
- **Narration:** Line 6 is only a check. It prints the type of each answer.
  **On screen:** Code `examples/ex01_questions.py`, line 6 highlighted, output hidden
- **Interaction:** "The user types 3 for the number of people. Which type does line 6 print for `people`?" stays on screen with a 10-second timer.
- **Narration:** Int. The answer was the text 3, and int on line 5 turned it into a whole number.
  **On screen:** Code `examples/ex01_questions.py`, line 5, 6 highlighted, output `examples/ex01_questions.expected`
- **Narration:** The finished program does not need line 6. It was only there to check.
  **On screen:** Code `examples/ex01_questions.py`, output `examples/ex01_questions.expected`

## Scene 7: Step 2: The tip, with AI (5:24 to 6:42)

**Section:** Build it step by step

**Direction:** Teach the percent rule first. Then stage 3 plants the AI mistake and the learner judges it; stage 4 tests against the hand result.

- **Narration:** Step 2: the tip. First, the maths. A percent is a number out of 100.
  **On screen:** Step 2: What is 10 percent?
- **Narration:** So 10 percent of 48 is 48 times 10, divided by 100. That is 4.80. Asha works this out by hand, before any code.
  **On screen:** Step 2: What is 10 percent?
- **Narration:** Stage 3: generate. Asha asks the AI for the tip and total lines, and asks what they print.
  **On screen:** AI chat, stage 3: Generate: two lines, with a prediction
    - You: Write the lines that calculate the tip and the total for a bill of 48 with a 10 percent tip. Use the names bill, tip_percent, tip and total. Tell me what they print.
- **Narration:** The AI writes a few short lines, and says they print a tip of 4.80. It sounds sure.
  **On screen:** AI chat, stage 3: Generate: two lines, with a prediction
    - You: Write the lines that calculate the tip and the total for a bill of 48 with a 10 percent tip. Use the names bill, tip_percent, tip and total. Tell me what they print.
    - AI (example answer): Here are the lines. They print `Tip: 4.80` and `Total: 52.80`. [code `examples/ai_tip_flawed.py`]
- **Narration:** Read line 4 carefully.
  **On screen:** AI chat, stage 3: Generate: two lines, with a prediction
    - You: Write the lines that calculate the tip and the total for a bill of 48 with a 10 percent tip. Use the names bill, tip_percent, tip and total. Tell me what they print.
    - AI (example answer): Here are the lines. They print `Tip: 4.80` and `Total: 52.80`. [code `examples/ai_tip_flawed.py`]
- **Interaction:** "The AI says this prints `Tip: 4.80`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Line 4 multiplies by 10, and never divides by 100. Let's see what really happens.
  **On screen:** AI chat, stage 3: Generate: two lines, with a prediction
    - You: Write the lines that calculate the tip and the total for a bill of 48 with a 10 percent tip. Use the names bill, tip_percent, tip and total. Tell me what they print.
    - AI (example answer): Here are the lines. They print `Tip: 4.80` and `Total: 52.80`. [code `examples/ai_tip_flawed.py`]
- **Narration:** Stage 4: test. Asha runs the lines. The tip is 480! Ten times bigger than the whole bill. Her hand result catches it immediately.
  **On screen:** AI chat, stage 4: Test: compare with the result you worked out
    - You: I worked it out by hand first: 10 percent of 48 is 4.80. Your lines printed this:
- **Narration:** She shows the AI the real output. This time it names the cause: a percent must be divided by 100.
  **On screen:** AI chat, stage 4: Test: compare with the result you worked out
    - You: I worked it out by hand first: 10 percent of 48 is 4.80. Your lines printed this:
    - AI (example answer): Line 4 multiplies the bill by 10, not by 10 percent. A percent must be divided by 100: [code `examples/ai_tip_fixed.py`]
- **Narration:** She runs the fix. 4.80, and a total of 52.80. Now the code and her hand result agree.
  **On screen:** AI chat, stage 4: Test: compare with the result you worked out
    - You: I worked it out by hand first: 10 percent of 48 is 4.80. Your lines printed this:
    - AI (example answer): Line 4 multiplies the bill by 10, not by 10 percent. A percent must be divided by 100: [code `examples/ai_tip_fixed.py`]
    - You: I ran the fixed lines:

## Scene 8: Step 3: Share in whole cents (6:42 to 8:06)

**Section:** Build it step by step

**Direction:** The cents lines type in one by one, each explained. The learner predicts the check line, then the reveal. Then a quiz on remainders.

- **Narration:** Step 3, the most important part. Asha uses the mission's numbers: a total of 43.07, and 4 people.
  **On screen:** Code `examples/ex03_cents.py`, lines 1 to 4 typed in, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 multiplies by 100 to get cents. It uses round, because a float can be a tiny amount below the whole number you expect.
  **On screen:** Code `examples/ex03_cents.py`, lines 1 to 4 typed in, line 4 highlighted, output hidden
- **Narration:** Line 5 shares the cents with double slash: whole cents only.
  **On screen:** Code `examples/ex03_cents.py`, lines 1 to 5 typed in, line 5 highlighted, output hidden
- **Narration:** Line 6 uses the remainder operator to find the cents left over.
  **On screen:** Code `examples/ex03_cents.py`, lines 1 to 6 typed in, line 6 highlighted, output hidden
- **Narration:** Lines 7 to 9 print the three numbers. And line 10 is a check: each share times the people, plus the extra cents.
  **On screen:** Code `examples/ex03_cents.py`, lines 1 to 10 typed in, line 10 highlighted, output hidden
- **Interaction:** "If no cent is lost, what must the check on line 10 print?" stays on screen with a 10-second timer.
- **Narration:** 4307, the total in cents. And it does! Every cent is accounted for.
  **On screen:** Code `examples/ex03_cents.py`, lines 1 to 10 typed in, line 10 highlighted, output `examples/ex03_cents.expected`
- **Narration:** Each person pays 1076 cents, and 3 cents are left over.
  **On screen:** Code `examples/ex03_cents.py`, lines 1 to 10 typed in, line 5, 6 highlighted, output `examples/ex03_cents.expected`
- **Narration:** Quick check. Seven people share 100 cents. How many extra cents are left over?
  **On screen:** Quick check: "Seven people share 100 cents. How many extra cents are left over?" (options shown)
- **Interaction:** "Seven people share 100 cents. How many extra cents are left over?" stays on screen with a 10-second timer.
- **Narration:** C, 2. Each person gets 14 cents. 14 times 7 is 98, and 2 cents are left.
  **On screen:** Quick check: "Seven people share 100 cents. How many extra cents are left over?" (answer revealed: 2)

## Scene 9: Step 4: Back to money (8:06 to 8:31)

**Section:** Build it step by step

**Direction:** Short beat: why .2f matters for money.

- **Narration:** Step 4. To show money again, divide the cents by 100. 1760 cents becomes 17.6.
  **On screen:** Code `examples/ex04_share.py`, line 2, 3 highlighted, output `examples/ex04_share.expected`
- **Narration:** Line 4 prints 17.6. Python drops the last zero of a float.
  **On screen:** Code `examples/ex04_share.py`, line 4 highlighted, output `examples/ex04_share.expected`
- **Narration:** Line 5 adds dot 2 f, so it looks like money: 17.60.
  **On screen:** Code `examples/ex04_share.py`, line 5 highlighted, output `examples/ex04_share.expected`
- **Narration:** And line 6 puts it in a receipt line: 16 characters for the label, 8 for the amount.
  **On screen:** Code `examples/ex04_share.py`, line 6 highlighted, output `examples/ex04_share.expected`

## Scene 10: Step 5: Put it together (8:31 to 9:46)

**Section:** Build it step by step

**Direction:** Walk the complete program in four groups, then predict the share, then run. Then a breather.

- **Narration:** Step 5: put it together. Lines 2 to 5 are the header and the three questions from step 1.
  **On screen:** Code `project/bill_splitter.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** Lines 7 and 8 are the tip and the total, with the percent divided by 100.
  **On screen:** Code `project/bill_splitter.py`, line 7, 8 highlighted, output hidden
- **Narration:** Lines 9 to 12 are the whole cents from steps 3 and 4.
  **On screen:** Code `project/bill_splitter.py`, line 9, 10, 11, 12 highlighted, output hidden
- **Narration:** Line 14 builds the tip label with an f string, so the receipt says Tip 10 percent. Line 15 makes a line of 24 hyphens.
  **On screen:** Code `project/bill_splitter.py`, line 14, 15 highlighted, output hidden
- **Narration:** Lines 16 to 22 print the receipt. The last line prints the extra cents without dot 2 f, because cents are a whole number.
  **On screen:** Code `project/bill_splitter.py`, line 16, 17, 18, 19, 20, 21, 22 highlighted, output hidden
- **Interaction:** "The total is 52.80, shared by 3. What will the Each pays line show?" stays on screen with a 10-second timer.
- **Narration:** 17.60. 5280 cents, shared by 3, is 1760 cents each, with nothing left over.
  **On screen:** Code `project/bill_splitter.py`, line 10, 21 highlighted, output `project/bill_splitter.expected`
- **Narration:** Every line matches the destination you saw at the start.
  **On screen:** Code `project/bill_splitter.py`, output `project/bill_splitter.expected`
- **Narration:** Breather. The tool is built. Roll your shoulders and breathe out.
  **On screen:** Breather card
    - A percent is divided by 100.
    - Whole cents: `//` shares, `%` is left over.
    - `:.2f` makes amounts look like money.
- **Narration:** But built is not finished. Criterion six says: test it.
  **On screen:** Breather card
    - A percent is divided by 100.
    - Whole cents: `//` shares, `%` is left over.
    - `:.2f` makes amounts look like money.
- **Breather:** 4 quiet seconds.

## Scene 11: Test it (9:46 to 11:48)

**Section:** Test it

**Direction:** The test plan table, then the decimal test predicted from step 3, then stage 5: the zero-people test and the debug chat. Then a breather.

- **Narration:** A test is a set of answers whose correct result you worked out first. Asha plans four.
  **On screen:** Table: Four tests, worked out by hand first
- **Narration:** The normal case, which you ran in step 5.
  **On screen:** Table: Four tests, worked out by hand first (row 1 in focus)
- **Narration:** A bill with decimals: the case from the mission.
  **On screen:** Table: Four tests, worked out by hand first (row 2 in focus)
- **Narration:** A tip of zero.
  **On screen:** Table: Four tests, worked out by hand first (row 3 in focus)
- **Narration:** And one person, who pays it all.
  **On screen:** Table: Four tests, worked out by hand first (row 4 in focus)
- **Narration:** Test 2 runs the same program with the mission's numbers: 37.45, a 15 percent tip, and 4 people.
  **On screen:** Test 2: the mission's bill
- **Narration:** The total is 4307 cents, shared by 4. You already worked these cents out in step 3.
  **On screen:** Test 2: the mission's bill
- **Interaction:** "What will the Each pays and Extra cents lines show?" stays on screen with a 10-second timer.
- **Narration:** Let's run it and see.
  **On screen:** Test 2: the mission's bill
- **Narration:** Each pays 10.76, with 3 extra cents. Four times 10.76 is 43.04, and 3 cents more makes exactly 43.07.
  **On screen:** Code `examples/test_decimal.py`, line 21, 22 highlighted, output `examples/test_decimal.expected`
- **Narration:** The tip, 5.6175, shows as 5.62.
  **On screen:** Code `examples/test_decimal.py`, line 18 highlighted, output `examples/test_decimal.expected`
- **Narration:** Test 3, no tip. The tip is 0.00, and each person pays 10.00, as worked out.
  **On screen:** Code `examples/test_no_tip.py`, line 18 highlighted, output `examples/test_no_tip.expected`
- **Narration:** Test 4, one person. The total is 13.75, and the one person pays all of it. All four tests pass.
  **On screen:** Code `examples/test_one_person.py`, line 21 highlighted, output `examples/test_one_person.expected`
- **Narration:** Stage 5: debug. A friend tries to break the tool, and types 0 for the number of people. The program stops with an error. Asha reads it: line 10.
  **On screen:** AI chat, stage 5: Debug: a test that breaks the program
    - You: A friend typed 0 for the number of people, and the program stopped. Here are the lines and the full error. Explain the cause first. Then suggest the smallest fix I can make with what I know. [code `examples/test_zero_people.py`]
- **Narration:** Asha pastes the lines and the full error, and asks for the cause first. The AI explains: nothing can be shared between zero people.
  **On screen:** AI chat, stage 5: Debug: a test that breaks the program
    - You: A friend typed 0 for the number of people, and the program stopped. Here are the lines and the full error. Explain the cause first. Then suggest the smallest fix I can make with what I know. [code `examples/test_zero_people.py`]
    - AI (example answer): Line 10 divides by `people`, which is 0. Nothing can be shared between zero people, so Python stops with a `ZeroDivisionError`. For now, make the question clear: `Number of people (1 or more): `. Checking the answer needs `if`, which comes later.
- **Narration:** To refuse a bad answer, the program must make a decision. That needs if, which you meet in Chapter 6. For now, a clear question helps.
  **On screen:** AI chat, stage 5: Debug: a test that breaks the program
    - You: A friend typed 0 for the number of people, and the program stopped. Here are the lines and the full error. Explain the cause first. Then suggest the smallest fix I can make with what I know. [code `examples/test_zero_people.py`]
    - AI (example answer): Line 10 divides by `people`, which is 0. Nothing can be shared between zero people, so Python stops with a `ZeroDivisionError`. For now, make the question clear: `Number of people (1 or more): `. Checking the answer needs `if`, which comes later.
- **Narration:** Breather. Four tests passed, and one test found a limit.
  **On screen:** Breather card
    - Work out the result by hand, then run.
    - Four tests passed.
    - Zero people breaks it, for now.
- **Narration:** Last stage: can the AI make the tool better?
  **On screen:** Breather card
    - Work out the result by hand, then run.
    - Four tests passed.
    - Zero people breaks it, for now.
- **Breather:** 4 quiet seconds.

## Scene 12: Improve it with AI (11:48 to 13:41)

**Section:** Improve it with AI

**Direction:** Stage 6: the AI suggests rounding each share. The learner judges it, then the test on its own screen. Then the six stages, a quiz and a breather.

- **Narration:** Stage 6: improve. Asha asks for one way to make the program simpler, without changing what it prints.
  **On screen:** AI chat, stage 6: Improve: a simpler line?
    - You: My splitter passes all four tests. Suggest one way to make it simpler. Do not change what it prints. [code `project/bill_splitter.py`]
- **Narration:** The AI suggests replacing the two share lines, 10 and 12, with one line: round the total divided by the people, to 2 places.
  **On screen:** AI chat, stage 6: Improve: a simpler line?
    - You: My splitter passes all four tests. Suggest one way to make it simpler. Do not change what it prints. [code `project/bill_splitter.py`]
    - AI (example answer): Replace the two share lines, 10 and 12, with one line: `share = round(total / people, 2)`. It is shorter and gives the same result.
- **Narration:** Shorter, yes. Think about the mission before you answer.
  **On screen:** AI chat, stage 6: Improve: a simpler line?
    - You: My splitter passes all four tests. Suggest one way to make it simpler. Do not change what it prints. [code `project/bill_splitter.py`]
    - AI (example answer): Replace the two share lines, 10 and 12, with one line: `share = round(total / people, 2)`. It is shorter and gives the same result.
- **Interaction:** "The AI says one rounded line gives the same result. Is it right?" stays on screen with a 10-second timer.
- **Narration:** Asha does not guess. She tests it with the mission's numbers.
  **On screen:** AI chat, stage 6: Improve: a simpler line?
    - You: My splitter passes all four tests. Suggest one way to make it simpler. Do not change what it prints. [code `project/bill_splitter.py`]
    - AI (example answer): Replace the two share lines, 10 and 12, with one line: `share = round(total / people, 2)`. It is shorter and gives the same result.
- **Narration:** Line 4 is the AI's line. Line 6 adds up the four shares.
  **On screen:** Code `examples/ai_round_share.py`, line 4 highlighted, output hidden
- **Narration:** Each pays 10.77, and the shares add up to 43.08. One cent too much: the exact problem from the mission!
  **On screen:** Code `examples/ai_round_share.py`, line 4, 6 highlighted, output `examples/ai_round_share.expected`
- **Narration:** So Asha keeps her cent lines. A suggestion that changes the result is not a simplification.
  **On screen:** Code `examples/ai_round_share.py`, line 4, 6 highlighted, output `examples/ai_round_share.expected`
- **Narration:** Here are all six stages on one tool.
  **On screen:** Table: Six stages, one tool
- **Narration:** The AI helped every time. It planned, checked, wrote, explained and suggested.
  **On screen:** Table: Six stages, one tool (row 1 in focus)
- **Narration:** And it was wrong twice: the tip, and the rounding.
  **On screen:** Table: Six stages, one tool (row 3 in focus)
- **Narration:** Both times, a test caught it. The same test you work out by hand.
  **On screen:** Table: Six stages, one tool (row 6 in focus)
- **Narration:** Quick check. Your program passes all its tests. An AI suggests a simpler line. What do you do first?
  **On screen:** Quick check: "Your program passes all its tests. An AI suggests a simpler line. What do you do first?" (options shown)
- **Interaction:** "Your program passes all its tests. An AI suggests a simpler line. What do you do first?" stays on screen with a 10-second timer.
- **Narration:** D. Run your tests again with the new line. That is how Asha caught the 43.08.
  **On screen:** Quick check: "Your program passes all its tests. An AI suggests a simpler line. What do you do first?" (answer revealed: Run your tests again with the new line)
- **Narration:** Last breather. You built, tested and improved a real tool, with an AI as a partner, and you made the decisions.
  **On screen:** Breather card
    - AI helped at all six stages.
    - It was wrong twice, and sounded sure.
    - Tests caught both mistakes.
- **Narration:** Let's recap.
  **On screen:** Breather card
    - AI helped at all six stages.
    - It was wrong twice, and sounded sure.
    - Tests caught both mistakes.
- **Breather:** 4 quiet seconds.

## Scene 13: Recap (13:41 to 15:02)

**Section:** Recap

**Direction:** Recap points one by one, a final quiz, the badge and the practice table.

- **Narration:** Here is what you used in this boss level.
  **On screen:** Recap
- **Narration:** Plan first: inputs, calculations in order, then outputs.
  **On screen:** Recap
    - Plan first: inputs, calculations in order, then outputs.
- **Narration:** Convert each answer as you read it. Float for amounts, int for counts.
  **On screen:** Recap
    - Plan first: inputs, calculations in order, then outputs.
    - Convert each answer as you read it: `float()` for amounts, `int()` for counts.
- **Narration:** A percent is divided by 100.
  **On screen:** Recap
    - Plan first: inputs, calculations in order, then outputs.
    - Convert each answer as you read it: `float()` for amounts, `int()` for counts.
    - A percent is divided by 100.
- **Narration:** Share money in whole cents: double slash for each share, and the remainder operator for what is left.
  **On screen:** Recap
    - Plan first: inputs, calculations in order, then outputs.
    - Convert each answer as you read it: `float()` for amounts, `int()` for counts.
    - A percent is divided by 100.
    - Share money in whole cents: `//` for each share, `%` for what is left.
- **Narration:** And test with results you worked out first, including every AI suggestion.
  **On screen:** Recap
    - Plan first: inputs, calculations in order, then outputs.
    - Convert each answer as you read it: `float()` for amounts, `int()` for counts.
    - A percent is divided by 100.
    - Share money in whole cents: `//` for each share, `%` for what is left.
    - Test with results you worked out first, and test every AI suggestion.
- **Narration:** One last check. Which line calculates a 15 percent tip on the bill?
  **On screen:** Quick check: "Which line calculates a 15 percent tip on `bill`?" (options shown)
- **Interaction:** "Which line calculates a 15 percent tip on `bill`?" stays on screen with a 10-second timer.
- **Narration:** B. Times 15, divided by 100. Exactly the fix from stage 4.
  **On screen:** Quick check: "Which line calculates a 15 percent tip on `bill`?" (answer revealed: `tip = bill * 15 / 100`)
- **Narration:** Boss level complete! You earned 300 XP and the Fair Share badge. And Module 1 is done.
  **On screen:** Fair Share You earned 300 XP. Module 1 is complete.
- **Breather:** 2 quiet seconds.
- **Narration:** The practice file has eight more money tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-ups, worth 10 XP each, including sharing sweets.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, such as a fixed service charge.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's splitter.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Work out each result by hand before you run your code.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 14: What's next (15:02 to 15:28)

**Section:** What's next

**Direction:** End card. Tease if as the fix for zero people and the extra cents. Hold quietly at the end.

- **Narration:** Asha's tool still has two limits. It crashes when someone types 0 people. And it shows the extra cents, but cannot say who pays them.
  **On screen:** Making Decisions: if, elif and else Programs that react to the answers.
- **Narration:** Both need the program to make a decision. In Chapter 6, you will learn if, elif and else, and your programs will react to the answers.
  **On screen:** Making Decisions: if, elif and else Programs that react to the answers.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Making Decisions: if, elif and else Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 6.
  **On screen:** Making Decisions: if, elif and else Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
