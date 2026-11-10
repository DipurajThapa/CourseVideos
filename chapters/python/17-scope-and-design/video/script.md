# Video Script: Chapter 17: Scope and Good Function Design

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:36.

## Scene 1: Introduction (0:00 to 0:50)

**Section:** Introduction

**Direction:** Open on Asha's oldest function doing three jobs, in her words. Then the title with the AI tease, then the redesigned day report as the mission, with no output yet.

- **Narration:** At the Corner Cafe, Asha's oldest function closes the day. It adds the tax, prints a line, and changes a week total, all at once.
  **On screen:** One function, three jobs
- **Narration:** When one part goes wrong, she has to read all of it. And Chapter 16 ended with a question: day total has a variable called total inside it. Can the rest of the program see it?
  **On screen:** One function, three jobs
- **Narration:** This is Code Quest, Chapter 17: where variables live, and how to design small functions.
  **On screen:** Scope and Good Function Design
- **Narration:** And an AI assistant will split Asha's function, and promise the output stays the same. Her saved output will decide.
  **On screen:** Scope and Good Function Design Pass values in. Return results out.
- **Narration:** Here is today's mission: Asha's day report from Chapter 16, redesigned. Three functions, and each one returns its result.
  **On screen:** Code `examples/ex08_day_report.py`, line 2, 6, 13 highlighted, output hidden
- **Narration:** Only the last three lines print. Let's build it.
  **On screen:** Code `examples/ex08_day_report.py`, line 18, 19, 20 highlighted, output hidden

## Scene 2: Learning goals (0:50 to 1:01)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Your goals: know where a variable lives, fix two scope errors, use default and keyword arguments, and split a function that does too much, with an AI's help.
  **On screen:** By the end, you will be able to:
    - Explain local and global variables, and predict which one a line uses.
    - Fix a `NameError` and an `UnboundLocalError` caused by scope.
    - Write default arguments and call functions with keyword arguments.
    - Split a function that does several jobs into small functions.
    - Ask AI to split a function, and check the split against saved output.

## Scene 3: Why this matters (1:01 to 1:14)

**Section:** Why this matters

**Direction:** Connect small, self-contained functions to testing and to safe AI changes.

- **Narration:** Real programs have hundreds of functions. A small function that gets its values as parameters and returns its result can be tested on its own, and an AI can change it safely.
  **On screen:** Why this matters
    - Real programs have hundreds of functions.
    - A small function that gets its values as parameters and returns its result can be tested on its own.
    - An AI can change one small function without breaking the rest.

## Scene 4: The idea: where a variable lives (1:14 to 2:44)

**Section:** The idea

**Direction:** Teach scope with the table and the diagram, then the kitchen analogy and where it stops working, then the rule. Then a quiz and a breather.

- **Narration:** The scope of a variable is the part of the program where its name can be used. A local variable is created inside a function. It exists only while that function runs.
  **On screen:** Table: Two scopes (row 1 in focus)
- **Narration:** A global variable is created at the top level of the file. Every function can read it.
  **On screen:** Table: Two scopes (row 2 in focus)
- **Narration:** Think of the cafe. The menu board on the wall is global: everyone can read it, even the cook. The kitchen whiteboard is local: its notes are wiped when the job is done.
  **On screen:** The menu board and the whiteboard
- **Narration:** Where it stops working: suppose the cook writes a note with the same name as something on the menu board. Python treats that name as a kitchen note for the whole function, even on the lines before the note.
  **On screen:** The menu board and the whiteboard
- **Narration:** So good functions follow one rule: pass values in as parameters, and return results out.
  **On screen:** The design rule
    - Pass values in as parameters. Return results out.
- **Narration:** A function that uses only its parameters and returns its result, without printing or changing anything outside, is called a pure function. One line can test it.
  **On screen:** The design rule
    - Pass values in as parameters. Return results out.
    - A **pure function** uses only its parameters and returns its result. It prints nothing and changes nothing outside.
    - A pure function gives the same result for the same arguments, so one line can test it.
- **Narration:** Quick check. A variable is created inside a function. Where can you use it?
  **On screen:** Quick check: "A variable is created inside a function. Where can you use it?" (options shown)
- **Interaction:** "A variable is created inside a function. Where can you use it?" stays on screen with a 10-second timer.
- **Narration:** C. Only inside that function, while it runs. It is local.
  **On screen:** Quick check: "A variable is created inside a function. Where can you use it?" (answer revealed: Only inside that function, while it runs)
- **Narration:** Take a breather. Next, Asha tests these rules with real code.
  **On screen:** Breather card
    - Local: inside a function, while it runs.
    - Global: the top level of the file.
    - Pass values in, return results out.
- **Breather:** 4 quiet seconds.

## Scene 5: Steps 1 and 2: Local and global (2:44 to 4:06)

**Section:** Build it step by step

**Direction:** Ask what lines 8 and 9 of ex01 print, then what lines 7 and 9 of ex02 print.

- **Narration:** Step 1. Inside day total, line 3 creates a variable called total. That makes it local.
  **On screen:** Code `examples/ex01_local.py`, line 3, 4, 5, 6 highlighted, output hidden
- **Narration:** Line 8 calls the function and prints what it returns. Line 9 tries to print total itself.
  **On screen:** Code `examples/ex01_local.py`, line 8, 9 highlighted, output hidden
- **Interaction:** "What do lines 8 and 9 print?" stays on screen with a 10-second timer.
- **Narration:** Line 8 prints 7.5, the returned value.
  **On screen:** Code `examples/ex01_local.py`, line 8 highlighted, error `examples/ex01_local.expected_error`
- **Narration:** Line 9 stops with a Name Error. Total existed only while the function ran. To use a result outside, return it and store it.
  **On screen:** Code `examples/ex01_local.py`, line 9 highlighted, error `examples/ex01_local.expected_error`
- **Narration:** Step 2. Line 2 creates tax rate at the top level, so it is global. With tax reads it on line 5.
  **On screen:** Code `examples/ex02_global_read.py`, line 2, 5 highlighted, output hidden
- **Narration:** Line 7 calls with tax. Line 8 changes tax rate to 1.2. And line 9 makes exactly the same call again.
  **On screen:** Code `examples/ex02_global_read.py`, line 7, 8, 9 highlighted, output hidden
- **Interaction:** "What do lines 7 and 9 print?" stays on screen with a 10-second timer.
- **Narration:** 3.85, then 4.2. The same call gives two results, because the function reads tax rate at the moment it runs.
  **On screen:** Code `examples/ex02_global_read.py`, line 7, 9 highlighted, output `examples/ex02_global_read.expected`
- **Narration:** Nothing in the call shows that hidden link to line 8. That is why good functions take what they need as parameters.
  **On screen:** Code `examples/ex02_global_read.py`, line 7, 9 highlighted, output `examples/ex02_global_read.expected`

## Scene 6: Step 3: Changing a global inside a function (4:06 to 5:08)

**Section:** Build it step by step

**Direction:** Teach the assignment rule, ask where Python stops, reveal the UnboundLocalError, then the pass-in, return-out fix.

- **Narration:** Step 3. Asha counts sales with a global variable, sales count, on line 2.
  **On screen:** Code `examples/ex03_unbound.py`, line 2 highlighted, output hidden
- **Narration:** Line 5 assigns to sales count inside the function. Remember the rule: an assignment makes the name local for the whole function.
  **On screen:** Code `examples/ex03_unbound.py`, line 5 highlighted, output hidden
- **Interaction:** "Where does Python stop, and why?" stays on screen with a 10-second timer.
- **Narration:** On line 5. The right side reads the local sales count before it has a value. Python calls this an Unbound Local Error.
  **On screen:** Code `examples/ex03_unbound.py`, line 5 highlighted, error `examples/ex03_unbound.expected_error`
- **Narration:** The traceback shows the call on line 7, then the failing line 5 inside the function.
  **On screen:** Code `examples/ex03_unbound.py`, line 7 highlighted, error `examples/ex03_unbound.expected_error`
- **Narration:** Python has a keyword, global, that allows the change. But it brings back the hidden link from step 2. There is a better fix.
  **On screen:** Code `examples/ex03_unbound.py`, error `examples/ex03_unbound.expected_error`
- **Narration:** Add sale now takes the count as a parameter, and returns the count plus 1.
  **On screen:** Code `examples/ex04_pass_in.py`, line 2, 3 highlighted, output `examples/ex04_pass_in.expected`
- **Narration:** Lines 6 and 7 store each returned value. Two sales, so line 8 prints 2.
  **On screen:** Code `examples/ex04_pass_in.py`, line 6, 7, 8 highlighted, output `examples/ex04_pass_in.expected`

## Scene 7: Steps 4 and 5: Default and keyword arguments (5:08 to 7:20)

**Section:** Build it step by step

**Direction:** Teach defaults and ask about lines 5 and 7. Teach keyword arguments and their order rule, ask about line 7. Then a quiz and a breather.

- **Narration:** Step 4. A default argument is a value a parameter gets when the call leaves it out. Here, rate equals 1.1 in the def line.
  **On screen:** Code `examples/ex05_defaults.py`, line 2 highlighted, output hidden
- **Narration:** Parameters with a default must come after the parameters without one. Line 6 passes a rate of 1.2. Lines 5 and 7 leave the rate out.
  **On screen:** Code `examples/ex05_defaults.py`, line 5, 6, 7 highlighted, output hidden
- **Interaction:** "What do lines 5 and 7 print?" stays on screen with a 10-second timer.
- **Narration:** 3.85 and 4.4. Both calls leave out the rate, so it is 1.1.
  **On screen:** Code `examples/ex05_defaults.py`, line 5, 7 highlighted, output `examples/ex05_defaults.expected`
- **Narration:** Line 6 prints 4.2 with its own rate. Now nothing is hidden: the rate is a parameter.
  **On screen:** Code `examples/ex05_defaults.py`, line 6 highlighted, output `examples/ex05_defaults.expected`
- **Narration:** One more fact about defaults: Python creates a default value once, when the def line runs, not at each call. For a number, that makes no difference. Remember it for later.
  **On screen:** Code `examples/ex05_defaults.py`, line 2 highlighted, output `examples/ex05_defaults.expected`
- **Narration:** Step 5. A keyword argument names the parameter in the call. On line 7, q t y equals 2 says at once what the 2 means.
  **On screen:** Code `examples/ex06_keywords.py`, line 7 highlighted, output hidden
- **Narration:** A positional argument is matched by its position: first to first. Keyword arguments can come in any order, but after any positional ones. Line 8 names both, in a new order.
  **On screen:** Code `examples/ex06_keywords.py`, line 8 highlighted, output hidden
- **Interaction:** "What does line 8 print?" stays on screen with a 10-second timer.
- **Narration:** 1 x Scone, 2.75. Q t y keeps its default, 1, and the names put each value in the right place.
  **On screen:** Code `examples/ex06_keywords.py`, line 8 highlighted, output `examples/ex06_keywords.expected`
- **Narration:** Line 6 uses the default too, and line 7 gives 2 cakes for 8.00.
  **On screen:** Code `examples/ex06_keywords.py`, line 6, 7 highlighted, output `examples/ex06_keywords.expected`
- **Narration:** Quick check. Which of these calls is not allowed?
  **On screen:** Quick check: "`def order_line(item, price, qty=1):` Which call is NOT allowed?" (options shown)
- **Interaction:** "`def order_line(item, price, qty=1):` Which call is NOT allowed?" stays on screen with a 10-second timer.
- **Narration:** A. A positional argument cannot come after a keyword argument.
  **On screen:** Quick check: "`def order_line(item, price, qty=1):` Which call is NOT allowed?" (answer revealed: `order_line(item="Tea", 3.5)`)
- **Narration:** Breather. Relax for a moment. Next, the most important design rule: one job per function.
  **On screen:** Breather card
    - Change a value by returning it.
    - Defaults go last in the `def` line.
    - Keywords go last in the call.
- **Breather:** 4 quiet seconds.

## Scene 8: Step 6: One job per function (7:20 to 7:41)

**Section:** Build it step by step

**Direction:** Show a calculation function and a text function, and why line 13 can test the first one.

- **Narration:** Step 6. Day total has one job: it calculates and returns.
  **On screen:** Code `examples/ex07_one_job.py`, line 2, 3, 4, 5, 6 highlighted, output `examples/ex07_one_job.expected`
- **Narration:** Total line has one job: it builds the text. Neither function prints.
  **On screen:** Code `examples/ex07_one_job.py`, line 8, 9 highlighted, output `examples/ex07_one_job.expected`
- **Narration:** Only the main code prints. And line 13 tests day total with one comparison: True. A function that only prints could never be tested like that.
  **On screen:** Code `examples/ex07_one_job.py`, line 12, 13 highlighted, output `examples/ex07_one_job.expected`

## Scene 9: See the outcome: the day report, redesigned (7:41 to 8:42)

**Section:** See the outcome

**Direction:** Return to the mission. Walk the three functions, the default rate and the two local totals, ask what line 19 prints, reveal, then hand over to the AI feature.

- **Narration:** Back to the mission. With tax takes the rate as a default argument, instead of a fixed number.
  **On screen:** Code `examples/ex08_day_report.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Day total and report line take the rate too, and pass it on to the next function.
  **On screen:** Code `examples/ex08_day_report.py`, line 6, 10, 13, 15 highlighted, output hidden
- **Narration:** Report line has its own local variable called total, on line 15. Day total has one too. The two never meet: each lives only inside its own function.
  **On screen:** Code `examples/ex08_day_report.py`, line 8, 15 highlighted, output hidden
- **Narration:** Line 19 reports Friday, a day with a higher tax, using a keyword argument for the rate.
  **On screen:** Code `examples/ex08_day_report.py`, line 19 highlighted, output hidden
- **Interaction:** "What does line 19 print?" stays on screen with a 10-second timer.
- **Narration:** Friday, 2 sales, 9.30. The rate of 1.2 travels from the call into every function.
  **On screen:** Code `examples/ex08_day_report.py`, line 19 highlighted, output `examples/ex08_day_report.expected`
- **Narration:** Line 18 uses the default rate, and line 20 tests a total in one line: True. Mission complete!
  **On screen:** Code `examples/ex08_day_report.py`, line 18, 20 highlighted, output `examples/ex08_day_report.expected`
- **Narration:** Now Asha wants to split her oldest function, close day. She asks an AI assistant to help, one stage at a time.
  **On screen:** Code `examples/ex08_day_report.py`, output `examples/ex08_day_report.expected`

## Scene 10: Work with AI: six stages, one split (8:42 to 13:42)

**Section:** Work with AI

**Direction:** Teach the skill. One conversation per stage, all about splitting close_day. Generate: None lines. Test: cases, then the split matches the target. Debug: the AI's first fix uses global. Improve: a list default shares one list.

- **Narration:** This chapter's AI skill: ask an AI which functions do too much, and how to split them.
  **On screen:** This chapter's AI skill: a safe split
    - Ask AI which functions do too much, and how to split them.
- **Narration:** A split must not change what the program prints. So save the output first, and compare it after every change.
  **On screen:** This chapter's AI skill: a safe split
    - Ask AI which functions do too much, and how to split them.
    - A split must not change what the program prints.
    - Save the output first. Compare after every change. Never paste private data.
- **Narration:** Stage 1: plan. Asha pastes her old close day function and asks the AI to list each job, with line numbers. No code yet.
  **On screen:** AI chat, stage 1: Plan: list the jobs
    - You: Here is my oldest function. Do not write code yet. List every separate job it does, with the line numbers for each job. [code `examples/ai_close_day_original.py`]
- **Narration:** The AI finds three jobs: the tax and the total, a printed line, and the global week total. Asha ticks every line against the list.
  **On screen:** AI chat, stage 1: Plan: list the jobs
    - You: Here is my oldest function. Do not write code yet. List every separate job it does, with the line numbers for each job. [code `examples/ai_close_day_original.py`]
    - AI (example answer): 1. It adds tax and totals the prices (lines 6 to 9). 2. It prints a report line (line 10). 3. It changes the global `week_total` (lines 5 and 11).
- **Narration:** Stage 2: write. Before asking for a split, Asha writes the calculation herself, as a pure day total. The AI predicts 11.28 and 8.53, and her run agrees.
  **On screen:** AI chat, stage 2: Write: your own function first
    - You: Before any split, I wrote the calculation myself as a pure function. Do not change it. Predict exactly what the last two lines print. [code `examples/ai_own_total.py`]
    - AI (example answer): `11.28`, then `8.53`.
- **Narration:** Then she runs the original program and saves its real output. That is her target for every change.
  **On screen:** AI chat, stage 2: Write: your own function first
    - You: Before any split, I wrote the calculation myself as a pure function. Do not change it. Predict exactly what the last two lines print. [code `examples/ai_own_total.py`]
    - AI (example answer): `11.28`, then `8.53`.
    - You: Correct. I also ran the original program and saved its output. This is my target:
- **Narration:** Stage 3: generate. Asha asks for a split with clear rules: no global variables, return instead of print, and exactly the same output.
  **On screen:** AI chat, stage 3: Generate: a split with rules
    - You: Split close_day into small functions with one job each. Use no global variables. Return results instead of printing them. The output must stay exactly the same.
- **Narration:** The AI writes day total and report line, and promises the same output. Its day total matches the one Asha wrote herself.
  **On screen:** AI chat, stage 3: Generate: a split with rules
    - You: Split close_day into small functions with one job each. Use no global variables. Return results instead of printing them. The output must stay exactly the same.
    - AI (example answer): Here is the split: `day_total()` and `report_line()`, and no globals. The output stays exactly the same. [code `examples/ai_split_flawed.py`]
- **Narration:** Here is the whole split. Look at line 10, inside report line. Then look at lines 14 and 15.
  **On screen:** Code `examples/ai_split_flawed.py`, line 10, 14, 15 highlighted, output hidden
- **Interaction:** "The AI says the output is exactly the same. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Two extra lines say None. Report line prints instead of returning, so it returns None.
  **On screen:** Code `examples/ai_split_flawed.py`, line 10 highlighted, output `examples/ai_split_flawed.expected`
- **Narration:** Lines 14 and 15 print that None too. Asha's saved target caught it at once. The AI broke its own rule, and it sounded sure.
  **On screen:** Code `examples/ai_split_flawed.py`, line 14, 15 highlighted, output `examples/ai_split_flawed.expected`
- **Narration:** Stage 4: test. Asha tells the AI what happened. She asks for the fix, and for three test cases with the exact expected line: a normal day, an empty day, and one sale.
  **On screen:** AI chat, stage 4: Test: cases with expected lines
    - You: Your report_line prints instead of returning, so my program printed None twice. Fix it. Then give me three test cases with the exact expected line: a normal day, an empty day and a day with one sale.
- **Narration:** The AI changes print to return on line 10, and lists the three cases. Asha checks Monday against her target, and counts the spaces in the other two.
  **On screen:** AI chat, stage 4: Test: cases with expected lines
    - You: Your report_line prints instead of returning, so my program printed None twice. Fix it. Then give me three test cases with the exact expected line: a normal day, an empty day and a day with one sale.
    - AI (example answer): Change `print(` to `return` on line 10. Test cases: Monday `[3.5, 4.0, 2.75]` gives `Monday   3 sales  11.28`. Sunday `[]` gives `Sunday   0 sales   0.00`. Friday `[2.0]` gives `Friday   1 sales   2.20`.
- **Narration:** First, she runs the three cases on the AI's first version. Every case fails, because report line still prints and returns None.
  **On screen:** Code `examples/ai_split_tests_flawed.py`, line 16, 17 highlighted, output `examples/ai_split_tests_flawed.expected`
- **Narration:** Lines 12 to 14 hold the three cases: a day, its prices, and the expected line. The loop on line 15 runs each one through report line.
  **On screen:** Code `examples/ai_split_tests_fixed.py`, line 12, 13, 14, 15, 16 highlighted, output `examples/ai_split_tests_fixed.expected`
- **Narration:** Line 17 prints pass or FAIL, with the if else from Chapter 14. All three pass, including the empty day.
  **On screen:** Code `examples/ai_split_tests_fixed.py`, line 17 highlighted, output `examples/ai_split_tests_fixed.expected`
- **Narration:** Stage 5: debug. Asha moves the week total into its own function, and Python stops. She pastes the code and the full error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I added a function for the week total, and got this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_week_unbound.py`]
- **Narration:** The AI explains the cause well: line 5 assigns to week total, so it is local, and it is read before it has a value. But its fix is to add the global keyword.
  **On screen:** AI chat, stage 5: Debug: a fix that keeps the rules
    - You: I added a function for the week total, and got this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_week_unbound.py`]
    - AI (example answer): Line 5 assigns to `week_total`, so Python treats it as local in `add_to_week()`. Then it reads that local name before it has a value. The fix: add `global week_total` as the first line of the function.
    - You: My plan says no global variables. Show a fix that passes the week total in and returns the new total.
- **Narration:** That breaks Asha's own plan: no global variables. So she asks for a fix that passes the week total in, and returns the new one.
  **On screen:** AI chat, stage 5: Debug: a fix that keeps the rules
    - You: I added a function for the week total, and got this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_week_unbound.py`]
    - AI (example answer): Line 5 assigns to `week_total`, so Python treats it as local in `add_to_week()`. Then it reads that local name before it has a value. The fix: add `global week_total` as the first line of the function.
    - You: My plan says no global variables. Show a fix that passes the week total in and returns the new total.
- **Narration:** Add to week now takes the week total in, and returns the new one. Lines 19 and 20 add Monday and Tuesday.
  **On screen:** Code `examples/ai_split_final.py`, line 12, 13, 19, 20 highlighted, output `examples/ai_split_final.expected`
- **Narration:** Asha runs everything again. The output matches her target exactly, week total 19.81, and all three cases pass.
  **On screen:** Code `examples/ai_split_final.py`, line 17, 18, 21, 25, 26 highlighted, output `examples/ai_split_final.expected`
- **Narration:** Stage 6: improve. Asha asks for one improvement that keeps the output the same.
  **On screen:** AI chat, stage 6: Improve: one suggestion
    - You: My split passes every test. Suggest one improvement, with one reason. Keep the output the same.
- **Narration:** The AI suggests a record sale function with a default empty list, so she can record sales one by one.
  **On screen:** AI chat, stage 6: Improve: one suggestion
    - You: My split passes every test. Suggest one improvement, with one reason. Keep the output the same.
    - AI (example answer): Add `record_sale(price, sales=[])`. With a default empty list, you can record a day's sales one by one without making a list first. Everything else stays the same.
- **Narration:** Asha tests it with two separate days. Lines 6 and 7 record two Monday sales. Line 8 records one Tuesday sale, and leaves out the list.
  **On screen:** Code `examples/ai_record_flawed.py`, line 6, 7, 8 highlighted, output hidden
- **Interaction:** "Will Tuesday's list hold only `4.25`?" stays on screen with a 10-second timer.
- **Narration:** No. Both lists hold all three sales. Python creates a default value once, when the def line runs, not at each call.
  **On screen:** Code `examples/ai_record_flawed.py`, line 2 highlighted, output `examples/ai_record_flawed.expected`
- **Narration:** Remember step 4: the default is created once, so every call that leaves out the list shares it. Asha rejects the suggestion, and her final program still matches the target.
  **On screen:** Code `examples/ai_record_flawed.py`, line 6, 8 highlighted, output `examples/ai_record_flawed.expected`
- **Narration:** Quick check. An AI split your function, and says the output is the same. What do you do?
  **On screen:** Quick check: "An AI split your function and says the output is the same. What do you do?" (options shown)
- **Interaction:** "An AI split your function and says the output is the same. What do you do?" stays on screen with a 10-second timer.
- **Narration:** D. Run it, and compare with the output you saved.
  **On screen:** Quick check: "An AI split your function and says the output is the same. What do you do?" (answer revealed: Run it and compare with the output you saved)
- **Narration:** Breather. Asha caught three AI problems: a print instead of a return, a fix that used global, and a list as a default.
  **On screen:** Breather card
    - Save the output before any change.
    - No globals: pass in, return out.
    - Test a default with two separate calls.
- **Breather:** 4 quiet seconds.

## Scene 11: Common mistakes (13:42 to 15:06)

**Section:** Common mistakes

**Direction:** Mistake 1 is a spot-it question on a local name. Mistake 2 calls back to the quiz. Mistake 3 is a spot-it question on parameter order. Mistake 4 calls back to the Improve stage.

- **Narration:** Now you try. Line 3 creates message inside the function. Line 6 prints it.
  **On screen:** Code `examples/err01_local_outside.py`, line 3, 6 highlighted, output hidden
- **Interaction:** "What happens on line 6, and why?" stays on screen with a 10-second timer.
- **Narration:** A Name Error. Message is local, so it disappeared when the function ended.
  **On screen:** Code `examples/err01_local_outside.py`, line 6 highlighted, error `examples/err01_local_outside.expected_error`
- **Narration:** The fix: return message, and store the returned value.
  **On screen:** Code `examples/err01_local_outside.py`, line 6 highlighted, error `examples/err01_local_outside.expected_error`
- **Narration:** Mistake 2 is the quick check from step 5. After a keyword argument, every argument needs a name, so Python cannot even read the file.
  **On screen:** Code `examples/err02_keyword_order.py`, line 6 highlighted, error `examples/err02_keyword_order.expected_error`
- **Narration:** One more. Look at the def line, and remember the rule from step 4.
  **On screen:** Code `examples/err03_default_order.py`, line 2 highlighted, output hidden
- **Interaction:** "What is wrong with line 2?" stays on screen with a 10-second timer.
- **Narration:** The parameter with a default, rate, comes before price, which has none. Parameters with a default go last.
  **On screen:** Code `examples/err03_default_order.py`, line 2 highlighted, error `examples/err03_default_order.expected_error`
- **Narration:** The fix: price first, then rate equals 1.1.
  **On screen:** Code `examples/err03_default_order.py`, line 2 highlighted, error `examples/err03_default_order.expected_error`
- **Narration:** Mistake 4 is the AI's suggestion again, with no error. Lina and Omar share one order. The fix: no default list; pass a new empty list in each call.
  **On screen:** Code `examples/err04_shared_list.py`, line 2, 6, 7 highlighted, output `examples/err04_shared_list.expected`
- **Narration:** Breather. Two questions to think about come next.
  **On screen:** Breather card
    - Return what you need outside.
    - Defaults last, keywords last.
    - Never a list as a default.
- **Breather:** 4 quiet seconds.

## Scene 12: Think beyond (15:06 to 15:54)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Report line returns its text instead of printing it. How does that help if Asha later wants to send the line somewhere else?
  **On screen:** Question card: "`report_line()` returns its text instead of printing it. How does that help if Asha later wants to send the line to a file or a chat message?"
- **Interaction:** "`report_line()` returns its text instead of printing it. How does that help if Asha later wants to send the line to a file or a chat message?" stays on screen with a 10-second timer.
- **Narration:** Think about who decides where the text goes.
  **On screen:** Question card: "`report_line()` returns its text instead of printing it. How does that help if Asha later wants to send the line to a file or a chat message?"
- **Narration:** Second. A thirty line function reads input, calculates, prints and saves. Which smaller functions would you split it into, and which could be pure?
  **On screen:** Question card: "A 30-line `close_day()` reads input, calculates, prints and saves. Which smaller functions would you split it into? Which could be pure?"
- **Interaction:** "A 30-line `close_day()` reads input, calculates, prints and saves. Which smaller functions would you split it into? Which could be pure?" stays on screen with a 10-second timer.
- **Narration:** Write the list of jobs first, as Asha did in stage 1.
  **On screen:** Question card: "A 30-line `close_day()` reads input, calculates, prints and saves. Which smaller functions would you split it into? Which could be pure?"

## Scene 13: Recap (15:54 to 16:53)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap. A local variable lives inside its function. A function can read a global, but its result then depends on a hidden line.
  **On screen:** Recap
    - A local variable lives inside its function, only while it runs.
    - A function can read a global, but then its result depends on a hidden line.
- **Narration:** Assigning to a name inside a function makes it local for the whole function. So pass values in, and return results out.
  **On screen:** Recap
    - A local variable lives inside its function, only while it runs.
    - A function can read a global, but then its result depends on a hidden line.
    - Assigning to a name inside a function makes it local for the whole function.
    - Pass values in, return results out. A pure function does only that.
- **Narration:** Defaults make a parameter optional, keywords name it, and a list is never a default. And with AI: save the output, and compare after every change.
  **On screen:** Recap
    - A local variable lives inside its function, only while it runs.
    - A function can read a global, but then its result depends on a hidden line.
    - Assigning to a name inside a function makes it local for the whole function.
    - Pass values in, return results out. A pure function does only that.
    - Defaults make a parameter optional. Keywords name it in the call. Never a list as a default.
    - Save the output before an AI change, and compare after every change.
- **Narration:** One last check. With tax is called with 10.0, and rate equals 1.2. What does it return?
  **On screen:** Quick check: "`with_tax(price, rate=1.1)` multiplies the price by the rate. What does `with_tax(10.0, rate=1.2)` return?" (options shown)
- **Interaction:** "`with_tax(price, rate=1.1)` multiplies the price by the rate. What does `with_tax(10.0, rate=1.2)` return?" stays on screen with a 10-second timer.
- **Narration:** B. 12.0. The keyword argument replaces the default rate.
  **On screen:** Quick check: "`with_tax(price, rate=1.1)` multiplies the price by the rate. What does `with_tax(10.0, rate=1.2)` return?" (answer revealed: `12.0`)
- **Narration:** Mission complete! You earned 100 XP and the Architect badge.
  **On screen:** Architect You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 14: Practice (16:53 to 17:12)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn: eight tasks, worth 170 XP. Three warm-up tasks at 10 XP, and three apply tasks at 20.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks at 40, including an AI's loyalty card to fix. Try each one before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 15: What's next (17:12 to 17:36)

**Section:** What's next

**Direction:** End card. Tease Chapter 18: functions in their own file, and ready-made modules. Hold quietly at the end.

- **Narration:** Asha's functions are small and clean now. But they live in one file, and she copies with tax into every new program.
  **On screen:** Modules and the Standard Library Put your functions in a file, and import them.
- **Narration:** In Chapter 18, you will put your functions in their own file, import them, and use ready-made modules from Python's standard library.
  **On screen:** Modules and the Standard Library Put your functions in a file, and import them.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Modules and the Standard Library Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 18.
  **On screen:** Modules and the Standard Library Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
