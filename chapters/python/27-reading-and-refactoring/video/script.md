# Video Script: Chapter 27: Reading and Improving Code with AI

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:39 (estimate, not rendered yet).

## Scene 1: Introduction

**Section:** Introduction

**Direction:** Open on Sam's unreadable till code at the Corner Cafe. Then the title, the AI tease and the mission, with no output.

- **Narration:** At the Corner Cafe, Asha finds the old till code. Sam, who helped before her, wrote it in a hurry.
  **On screen:** Code `examples/till_old.py`, line 2 highlighted, output hidden
- **Narration:** A function called f. Values called a, b and t 2. Numbers with no names. And no tests.
  **On screen:** Code `examples/till_old.py`, line 2, 7, 8 highlighted, output hidden
- **Narration:** It works. But nobody can read it, and nobody dares to change it.
  **On screen:** Code `examples/till_old.py`, output hidden
- **Narration:** This is Code Quest, Chapter 27. Today, you read code someone else wrote, and you improve it safely.
  **On screen:** Reading and Improving Code with AI
- **Narration:** And an AI assistant will tidy some code for Asha. It will say the behaviour is exactly the same. Her tests will decide.
  **On screen:** Reading and Improving Code with AI Change the structure. Keep the behaviour.
- **Narration:** Here is today's mission: Sam's till, with clear names, named numbers and small functions.
  **On screen:** Code `examples/till_final.py`, line 3, 4, 7, 15 highlighted, output hidden
- **Narration:** It must give exactly the same results as Sam's code. Let's get there, one small step at a time.
  **On screen:** Code `examples/till_final.py`, output hidden

## Scene 2: Learning goals

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Read unfamiliar code, write tests that record what it does now, and refactor in small steps.
  **On screen:** By the end, you will be able to:
    - Read unfamiliar code from the top, and trace one input.
    - Write characterization tests that record what code does now.
    - Refactor in small steps, and run the tests after each one.
- **Narration:** Read a diff, and review an AI's changes with your tests.
  **On screen:** By the end, you will be able to:
    - Read unfamiliar code from the top, and trace one input.
    - Write characterization tests that record what code does now.
    - Refactor in small steps, and run the tests after each one.
    - Read a unified diff.
    - Review an AI's refactoring with your tests.

## Scene 3: Why this matters

**Section:** Why this matters

**Direction:** Define refactoring, and why tests come first.

- **Narration:** Most programming work is changing code that already exists, often written by someone else.
  **On screen:** Why this matters
    - Most programming work is changing code that already exists.
- **Narration:** Refactoring means changing the structure of code, without changing what it does. And the proof is a set of tests, written before you change anything.
  **On screen:** Why this matters
    - Most programming work is changing code that already exists.
    - **Refactoring** means changing the structure of code without changing what it does.
    - Tests, written before any change, prove the behaviour stayed the same.

## Scene 4: The idea: a safe refactoring loop

**Section:** The idea

**Direction:** Teach the loop, characterization tests and the diff format. Then the kitchen analogy, a breather.

- **Narration:** Here is the big idea: a safe refactoring loop. First, tests that record what the code does now.
  **On screen:** A safe refactoring loop
- **Narration:** Then one small change. Then run the tests. Same results? Keep it. Different? Undo it. Then review, and go round again.
  **On screen:** A safe refactoring loop
- **Narration:** A test that records what the code does now, even the odd parts, is called a characterization test. It does not ask whether the result is right. It asks whether it is the same as before.
  **On screen:** A safe refactoring loop
- **Narration:** To review a change, you read a diff. A diff shows two versions of a file, line by line.
  **On screen:** How to read a diff
- **Narration:** A line that starts with minus was removed. A line that starts with plus was added. A line that starts with a space did not change.
  **On screen:** How to read a diff
- **Narration:** Think of rearranging the cafe kitchen. The shelves move, but every recipe must taste exactly the same afterwards.
  **On screen:** Like rearranging a kitchen
    - The shelves move, but every recipe must taste the same.
- **Narration:** The comparison stops at one point. In code, your tests check every recipe automatically, every time you move a shelf.
  **On screen:** Like rearranging a kitchen
    - The shelves move, but every recipe must taste the same.
    - Unlike a kitchen, you can check every recipe automatically, every time.
- **Narration:** Breather. Tests first, then one small change at a time.
  **On screen:** Breather card
    - Refactoring keeps the behaviour.
    - Tests first, then one small change.
    - In a diff, minus was removed and plus was added.
- **Narration:** Next, Asha reads Sam's code.
  **On screen:** Breather card
    - Refactoring keeps the behaviour.
    - Tests first, then one small change.
    - In a diff, minus was removed and plus was added.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Read from the top

**Section:** Build it step by step

**Direction:** Read till_old part by part, then ask about the empty order. Then trace one input with prints, and ask about the second pass.

- **Narration:** Step 1. Before you change anything, read the code from the first line, and say in words what each part does. Line 2 defines f, with two values, a and b.
  **On screen:** Code `examples/till_old.py`, line 2 highlighted, output hidden
- **Narration:** Lines 4 and 5 go through a. Each x is a tuple, so x 1 and x 2 are its second and third values. So a is an order of name, price and count.
  **On screen:** Code `examples/till_old.py`, line 4, 5 highlighted, output hidden
- **Narration:** Line 6 checks b, and line 7 takes 10 percent off. So b says whether the customer is a member.
  **On screen:** Code `examples/till_old.py`, line 6, 7 highlighted, output hidden
- **Narration:** Line 8 adds tax, and line 9 rounds. Lines 14 to 16 call f three times.
  **On screen:** Code `examples/till_old.py`, line 8, 9, 14, 15, 16 highlighted, output hidden
- **Interaction:** "What does line 16 print, for an empty order?" stays on screen with a 10-second timer.
- **Narration:** Zero point zero. The loop never runs, so t stays 0. But 0 times 1.1 is a float, so round gives 0.0, not 0.
  **On screen:** Code `examples/till_old.py`, line 16 highlighted, output `examples/till_old.expected`
- **Narration:** Lines 14 and 15 print 12.38, and 11.14 for a member. Remember these three results.
  **On screen:** Code `examples/till_old.py`, line 14, 15 highlighted, output `examples/till_old.expected`
- **Narration:** To check her reading, Asha traces one input. Line 8 prints the running total inside the loop, as in Chapter 9.
  **On screen:** Code `examples/ex02_trace.py`, line 6, 7, 8 highlighted, output hidden
- **Narration:** On the first pass, two teas at 3.5 make 7.0.
  **On screen:** Code `examples/ex02_trace.py`, line 6, 7, 8 highlighted, output `examples/ex02_trace.expected`
- **Interaction:** "What does line 8 print on the second pass?" stays on screen with a 10-second timer.
- **Narration:** Cake, 4.25, 1, t equals 11.25. 7.0, plus one cake.
  **On screen:** Code `examples/ex02_trace.py`, line 6, 7, 8 highlighted, output `examples/ex02_trace.expected`
- **Narration:** And with tax, 12.38. Asha's reading of the code was right.
  **On screen:** Code `examples/ex02_trace.py`, line 9 highlighted, output `examples/ex02_trace.expected`

## Scene 6: Step 2: Characterization tests

**Section:** Build it step by step

**Direction:** Asha records the three results from Step 1 as pytest tests, run them, then a quiz on the idea.

- **Narration:** Step 2. Now Asha records what f does today, before any change. Line 2 imports f, and line 4 is the order from step 1.
  **On screen:** Code `examples/test_till_old.py`, line 2, 4 highlighted, output hidden
- **Narration:** Each test uses one result from step 1. The normal order, the member order, and the odd one: an empty order gives 0.0.
  **On screen:** Code `examples/test_till_old.py`, line 7, 8, 11, 12, 15, 16 highlighted, output hidden
- **Narration:** She runs pytest. Three dots, three passed. From now on, any change that breaks one of them has changed the behaviour.
  **On screen:** Code `examples/test_till_old.py`, line 7, 8, 11, 12, 15, 16 highlighted, output `examples/test_till_old.expected`
- **Narration:** Quick check. Why does Asha's test expect 0.0 for an empty order?
  **On screen:** Quick check: "Why does Asha's test expect `0.0` for an empty order, even though it looks odd?" (options shown)
- **Interaction:** "Why does Asha's test expect `0.0` for an empty order, even though it looks odd?" stays on screen with a 10-second timer.
- **Narration:** C. A characterization test records what the code does now. It is not a judgement of right or wrong.
  **On screen:** Quick check: "Why does Asha's test expect `0.0` for an empty order, even though it looks odd?" (answer revealed: Because the test records what the code does now)

## Scene 7: Step 3: Rename for the reader

**Section:** Build it step by step

**Direction:** Rename f, a, b and t. Tests call the new name, with the same expected values. Ask what pytest reports.

- **Narration:** Step 3: the first small change, the names. F becomes order total, a becomes items, and b becomes is member.
  **On screen:** Code `examples/till_v2.py`, line 2 highlighted, output hidden
- **Narration:** Line 4 unpacks each tuple into name, price and count, as in Chapter 13. So x 1 and x 2 disappear.
  **On screen:** Code `examples/till_v2.py`, line 4, 5 highlighted, output hidden
- **Narration:** And t 2 becomes with tax, a name that says what it holds.
  **On screen:** Code `examples/till_v2.py`, line 8 highlighted, output hidden
- **Narration:** The tests change in one way only: line 2 imports the new name. Every expected value stays exactly as it was.
  **On screen:** Code `examples/test_till_v2.py`, line 2 highlighted, output hidden
- **Interaction:** "Asha changed only names. What will pytest report?" stays on screen with a 10-second timer.
- **Narration:** Three passed. The names changed, and the behaviour did not.
  **On screen:** Code `examples/test_till_v2.py`, line 2 highlighted, output `examples/test_till_v2.expected`

## Scene 8: Step 4: Name the magic numbers

**Section:** Build it step by step

**Direction:** Teach magic numbers and constants, run the tests, then read the diff between Step 3 and Step 4. Quiz, breather.

- **Narration:** Step 4. A magic number is a number in the code with no name, like 0.1 or 1.1. A reader cannot tell what it means.
  **On screen:** Code `examples/till_v3.py`, line 2, 3 highlighted, output hidden
- **Narration:** A constant gives it a name. In Python, constants are written in capital letters, at the top of the file. Lines 11 and 12 now use the names.
  **On screen:** Code `examples/till_v3.py`, line 11, 12 highlighted, output hidden
- **Narration:** Then she runs the tests.
  **On screen:** Code `examples/till_v3.py`, output hidden
- **Narration:** Line 2 imports the version with constants. Three passed, again.
  **On screen:** Code `examples/test_till_v3.py`, line 2 highlighted, output `examples/test_till_v3.expected`
- **Narration:** Now Asha reviews the change. The diff lib module compares Step 3 with Step 4. Lines 7 and 8 skip the file comment on line 1 of each file.
  **On screen:** Code `examples/ex05_diff.py`, line 5, 6, 7, 8 highlighted, output `examples/ex05_diff.expected`
- **Narration:** The plus lines at the top add the two constants.
  **On screen:** Code `examples/ex05_diff.py`, line 5, 6, 7, 8 highlighted, output `examples/ex05_diff.expected`
- **Narration:** And these minus and plus pairs swap 0.1 and 1.1 for their names. Every other line is unchanged.
  **On screen:** Code `examples/ex05_diff.py`, line 5, 6, 7, 8 highlighted, output `examples/ex05_diff.expected`
- **Narration:** Quick check. In a diff, what does a line that starts with minus mean?
  **On screen:** Quick check: "In a unified diff, what does a line that starts with `-` mean?" (options shown)
- **Interaction:** "In a unified diff, what does a line that starts with `-` mean?" stays on screen with a 10-second timer.
- **Narration:** B. It was removed. Plus means added.
  **On screen:** Quick check: "In a unified diff, what does a line that starts with `-` mean?" (answer revealed: The line was removed)
- **Narration:** Breather. Two small changes done, and the tests passed after each one.
  **On screen:** Breather card
    - Read first, then trace one input.
    - Characterization tests before any change.
    - One small change, then run the tests.
- **Narration:** Next, the last step, and Sam's code side by side with Asha's.
  **On screen:** Breather card
    - Read first, then trace one input.
    - Characterization tests before any change.
    - One small change, then run the tests.
- **Breather:** 4 quiet seconds.

## Scene 9: See the outcome: the readable till

**Section:** See the outcome

**Direction:** Step 5 extracts subtotal. Walk the final module, show the tests, then run old and new side by side with an ask.

- **Narration:** Step 5 extracts a function. The loop that adds up the order becomes its own function, subtotal, on lines 7 to 12, with a docstring.
  **On screen:** Code `examples/till_final.py`, line 7, 8, 9, 10, 11, 12 highlighted, output hidden
- **Narration:** Line 12 returns the total. Without that return, the result would never come back out.
  **On screen:** Code `examples/till_final.py`, line 12 highlighted, output hidden
- **Narration:** Order total now calls subtotal on line 17, takes off the discount, and adds tax with the two constants.
  **On screen:** Code `examples/till_final.py`, line 15, 17, 18, 19, 20 highlighted, output hidden
- **Narration:** And line 2 is a docstring for the whole module.
  **On screen:** Code `examples/till_final.py`, line 2 highlighted, output hidden
- **Narration:** The tests pass on the final version too: three passed.
  **On screen:** Code `examples/test_till_final.py`, line 2 highlighted, output `examples/test_till_final.expected`
- **Narration:** To be sure, Asha runs Sam's f, and her order total, side by side. Line 5 has three orders: the one from step 1, three juices, and an empty one.
  **On screen:** Code `examples/ex07_same.py`, line 2, 3, 5 highlighted, output hidden
- **Narration:** Lines 6 and 7 try each order with and without the member discount. Line 10 prints the old result, the new result, and whether they are equal.
  **On screen:** Code `examples/ex07_same.py`, line 6, 7, 8, 9, 10 highlighted, output hidden
- **Interaction:** "What is the last word on every line that line 10 prints?" stays on screen with a 10-second timer.
- **Narration:** True, six times. Every pair is equal.
  **On screen:** Code `examples/ex07_same.py`, line 6, 7, 8, 9, 10 highlighted, output `examples/ex07_same.expected`
- **Narration:** Mission complete! The code is easy to read, and it does exactly what Sam's code did.
  **On screen:** Code `examples/ex07_same.py`, line 6, 7, 8, 9, 10 highlighted, output `examples/ex07_same.expected`
- **Narration:** But Sam left one more function, a stock checker. Asha decides to tidy it with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex07_same.py`, line 6, 7, 8, 9, 10 highlighted, output `examples/ex07_same.expected`

## Scene 10: Work with AI: Sam's stock checker

**Section:** Work with AI

**Direction:** Safety first. Then the six stages on the stock checker. The explanation, the comparison, the rename and the sorted feature are each caught by a run or a test.

- **Narration:** This chapter's AI skill: a safe refactoring loop. Tests first, then the AI's suggestion, then your review, then the tests again.
  **On screen:** This chapter's AI skill: a safe refactoring loop
    - Tests first, then the AI's suggestion, then your review, then the tests again.
- **Narration:** Check every claim with a real run. And never paste private data. Use made-up stock numbers.
  **On screen:** This chapter's AI skill: a safe refactoring loop
    - Tests first, then the AI's suggestion, then your review, then the tests again.
    - Check every claim the AI makes with a real run.
    - Never paste private data. Use made-up stock numbers.
- **Narration:** Stage 1: plan. Sam's stock checker has the shortest names yet. Asha asks the AI to explain it, without changing it.
  **On screen:** AI chat, stage 1: Plan: ask for an explanation, not a change
    - You: Someone else wrote this function. Do not change it. Explain what it does, in plain words. [code `examples/stock_old.py`]
- **Narration:** The AI says c h k returns the items that will run out after the order. It sounds sure.
  **On screen:** AI chat, stage 1: Plan: ask for an explanation, not a change
    - You: Someone else wrote this function. Do not change it. Explain what it does, in plain words. [code `examples/stock_old.py`]
    - AI (example answer): chk takes the stock s and an order o. It returns the items that will run out after the order.
- **Narration:** Asha checks the claim with a run. Line 6 calls c h k, and lines 7 and 8 print what is left of each item.
  **On screen:** Code `examples/ai_explain_check.py`, line 4, 5, 6 highlighted, output `examples/ai_explain_check.expected`
- **Narration:** Cake has 2 left. It has not run out, but it is in the list. And Scone, with exactly 3 left, is not.
  **On screen:** Code `examples/ai_explain_check.py`, line 4, 5, 6 highlighted, output `examples/ai_explain_check.expected`
- **Narration:** So c h k returns the items that will have fewer than 3 left. The AI's explanation was close, but wrong.
  **On screen:** Code `examples/ai_explain_check.py`, line 4, 5, 6 highlighted, output `examples/ai_explain_check.expected`
- **Narration:** Stage 2: write. Asha writes her own characterization tests first, with the results of real runs.
  **On screen:** Table: Write: Asha's own tests, from real runs
- **Narration:** Exactly 3 left is the boundary, so it gets its own test.
  **On screen:** Table: Write: Asha's own tests, from real runs (row 2 in focus)
- **Narration:** And one test checks that the results keep the order of the order: Scone, then Cake.
  **On screen:** Table: Write: Asha's own tests, from real runs (row 4 in focus)
- **Narration:** Here are two of them. Line 12 expects an empty list for exactly 3 left. Line 21 expects Scone before Cake.
  **On screen:** Code `examples/test_stock.py`, line 12, 21 highlighted, output `examples/test_stock.expected`
- **Narration:** On Sam's code, all five pass.
  **On screen:** Code `examples/test_stock.py`, output `examples/test_stock.expected`
- **Narration:** Then she asks the AI which inputs her tests do not cover yet.
  **On screen:** AI chat, stage 2: Write: her tests first, then ask what is missing
    - You: I wrote my own tests first, from real runs. Which inputs do they not cover yet? [code `examples/test_stock.py`]
- **Narration:** It suggests an item that is not in the stock. A fair idea, for later.
  **On screen:** AI chat, stage 2: Write: her tests first, then ask what is missing
    - You: I wrote my own tests first, from real runs. Which inputs do they not cover yet? [code `examples/test_stock.py`]
    - AI (example answer): You cover plenty left, exactly 3 left, 2 left, the order of the results and an empty order. You could add an item that is not in the stock.
- **Narration:** Stage 3: generate. Asha asks for clear names, exactly the same behaviour, and no new features.
  **On screen:** AI chat, stage 3: Generate: one refactoring, same behaviour
    - You: Refactor chk with clear names. Keep the behaviour exactly the same. Do not add features.
- **Narration:** The AI gives her low stock, with a constant, and says the behaviour is exactly the same.
  **On screen:** AI chat, stage 3: Generate: one refactoring, same behaviour
    - You: Refactor chk with clear names. Keep the behaviour exactly the same. Do not add features.
    - AI (example answer): Here it is. The behaviour is exactly the same. [code `examples/stock_ai.py`]
- **Narration:** Asha reads the change as a diff. Because the name changed, every line shows as changed: six minus lines, and nine plus lines.
  **On screen:** Code `examples/ai_diff.py`, line 9, 10 highlighted, output `examples/ai_diff.expected`
- **Narration:** So she reads them in pairs. Look at the old if line, and the new one.
  **On screen:** Code `examples/ai_diff.py`, line 9, 10 highlighted, output `examples/ai_diff.expected`
- **Interaction:** "Every line changed. Which change can change the result?" stays on screen with a 10-second timer.
- **Narration:** The comparison. The old line says less than 3. The new line says less than or equal to LOW LIMIT. With less than or equal, exactly 3 left now counts as low.
  **On screen:** Code `examples/ai_diff.py`, line 9, 10 highlighted, output `examples/ai_diff.expected`
- **Narration:** Stage 4: test. Line 2 imports the AI's function under the old name, so the same five tests run on the new code.
  **On screen:** Code `examples/test_stock_ai.py`, line 2 highlighted, output `examples/test_stock_ai.expected`
- **Narration:** One failed: the test for exactly 3 left. The AI changed the behaviour, and it said it had not.
  **On screen:** Code `examples/test_stock_ai.py`, line 10, 11, 12 highlighted, output `examples/test_stock_ai.expected`
- **Narration:** She shows the AI the failing test, and asks which line changed the behaviour.
  **On screen:** AI chat, stage 4: Test: which line changed the behaviour?
    - You: I ran my five tests on your version. One failed, and the old version passed it. Which line changed the behaviour?
- **Narration:** Now the AI names line 8, and the comparison. Change it back to less than.
  **On screen:** AI chat, stage 4: Test: which line changed the behaviour?
    - You: I ran my five tests on your version. One failed, and the old version passed it. Which line changed the behaviour?
    - AI (example answer): Line 8. I changed < 3 to <= LOW_LIMIT, so an item with exactly 3 left now counts as low. Fix: change <= back to <.
- **Narration:** Asha changes less than or equal back to less than, and keeps the clear names. She runs every test again. Five passed.
  **On screen:** Code `examples/test_stock_v2.py`, line 2 highlighted, output `examples/test_stock_v2.expected`
- **Narration:** Stage 5: debug. Then Asha's daily report stops working. She pastes the code and the full error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: After the rename, my report stopped working. First explain the cause. Then show the smallest fix. [code `examples/ai_report_crash.py`]
- **Narration:** Cannot import name c h k. Her report still uses the old name. The AI suggests keeping the old name as a second name for the same function.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: After the rename, my report stopped working. First explain the cause. Then show the smallest fix. [code `examples/ai_report_crash.py`]
    - AI (example answer): Line 2 imports chk, but stock_v2 now only has low_stock. Smallest fix: keep the old name as a second name, chk = low_stock, at the end of the module.
- **Narration:** Line 14 says c h k equals low stock. Now both names lead to the same function. And line 6 is a docstring with the true behaviour: fewer than 3 left.
  **On screen:** Code `examples/stock_final.py`, line 14 highlighted, output hidden
- **Narration:** Her report imports c h k again, and it runs.
  **On screen:** Code `examples/ai_report.py`, line 2 highlighted, output `examples/ai_report.expected`
- **Narration:** And all five tests still pass on the final version. That rerun is her regression check.
  **On screen:** Code `examples/test_stock_final.py`, line 2 highlighted, output `examples/test_stock_final.expected`
- **Narration:** Stage 6: improve. Asha asks for one readability change that keeps every result.
  **On screen:** AI chat, stage 6: Improve: one change, then every test
    - You: My function passes all my tests. Suggest one improvement for readability only. It must not change any result.
- **Narration:** The AI suggests a comprehension, and sorted, so the list is tidier.
  **On screen:** AI chat, stage 6: Improve: one change, then every test
    - You: My function passes all my tests. Suggest one improvement for readability only. It must not change any result.
    - AI (example answer): Use a comprehension, and return sorted(low), so the list is tidier. [code `examples/stock_sorted.py`]
- **Interaction:** "Will all five of Asha's tests pass on this version?" stays on screen with a 10-second timer.
- **Narration:** No. Sorted puts Cake before Scone, so the test for the order fails. Sorting is a new feature that nobody asked for.
  **On screen:** AI chat, stage 6: Improve: one change, then every test
    - You: My function passes all my tests. Suggest one improvement for readability only. It must not change any result.
    - AI (example answer): Use a comprehension, and return sorted(low), so the list is tidier. [code `examples/stock_sorted.py`]
- **Narration:** One failed: keeps order of the order.
  **On screen:** Code `examples/test_stock_sorted.py`, line 21 highlighted, output `examples/test_stock_sorted.expected`
- **Narration:** So she keeps her final version. A refactoring that changes the output is not a refactoring.
  **On screen:** Code `examples/test_stock_sorted.py`, line 21 highlighted, output `examples/test_stock_sorted.expected`
- **Narration:** Quick check. An AI says its refactoring keeps the behaviour. What decides?
  **On screen:** Quick check: "An AI says its refactoring keeps the behaviour exactly the same. What decides?" (options shown)
- **Interaction:** "An AI says its refactoring keeps the behaviour exactly the same. What decides?" stays on screen with a 10-second timer.
- **Narration:** A. Your tests, and a real run. Today they caught a wrong explanation, a changed comparison and a feature nobody asked for.
  **On screen:** Quick check: "An AI says its refactoring keeps the behaviour exactly the same. What decides?" (answer revealed: Your tests and a real run)
- **Narration:** Breather. You watched Asha catch three AI mistakes, each with a run or a test.
  **On screen:** Breather card
    - Check every AI claim with a run.
    - Read every AI change as a diff.
    - Run every test after every change.
- **Narration:** Next, four mistakes people make when they refactor.
  **On screen:** Breather card
    - Check every AI claim with a run.
    - Read every AI change as a diff.
    - Run every test after every change.
- **Breather:** 4 quiet seconds.

## Scene 11: Common mistakes

**Section:** Common mistakes

**Direction:** Mistake 1 shows too few test cases. Mistakes 2 and 3 are spot-it asks. Mistake 4 is changing a test to match.

- **Narration:** Mistake 1. This tidy version rounds each line inside the loop, on line 8. It passes all three tests from step 2.
  **On screen:** Code `examples/err01_tidy_rounding.py`, line 8 highlighted, output `examples/err01_tidy_rounding.expected`
- **Narration:** With two teas, both results are 11.14.
  **On screen:** Code `examples/err01_tidy_rounding.py`, line 8 highlighted, output `examples/err01_tidy_rounding.expected`
- **Narration:** But with one tea, they are 7.67 and 7.68. Test several different inputs. And never move rounding into a loop during a refactoring.
  **On screen:** Code `examples/err01_tidy_rounding.py`, line 8 highlighted, output `examples/err01_tidy_rounding.expected`
- **Narration:** Mistake 2. The function has a new name on line 2. Look at line 9.
  **On screen:** Code `examples/err02_old_name.py`, line 2, 9 highlighted, output hidden
- **Interaction:** "What will line 9 do?" stays on screen with a 10-second timer.
- **Narration:** It stops with a name error. F is not defined, because Python only knows the new name.
  **On screen:** Code `examples/err02_old_name.py`, line 2, 9 highlighted, error `examples/err02_old_name.expected_error`
- **Narration:** The fix: change every call, or keep the old name as a second name, as Asha did with c h k.
  **On screen:** Code `examples/err02_old_name.py`, line 2, 9 highlighted, error `examples/err02_old_name.expected_error`
- **Narration:** Mistake 3. Lines 2 to 5 are an extracted function, subtotal. Line 9 uses its result.
  **On screen:** Code `examples/err03_no_return.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Interaction:** "What is missing in subtotal?" stays on screen with a 10-second timer.
- **Narration:** A return. Without it, subtotal gives back None, and line 9 cannot multiply None by 1.1.
  **On screen:** Code `examples/err03_no_return.py`, line 9 highlighted, error `examples/err03_no_return.expected_error`
- **Narration:** The fix: return total, as on line 12 of the finished till.
  **On screen:** Code `examples/err03_no_return.py`, line 9 highlighted, error `examples/err03_no_return.expected_error`
- **Narration:** Mistake 4. This version forgot the member discount. Old says 11.14, new says 12.38.
  **On screen:** Code `examples/err04_changed_test.py`, line 5, 6, 7, 8, 9 highlighted, output `examples/err04_changed_test.expected`
- **Narration:** Changing the test to expect 12.38 would hide the bug. Never change expected values during a refactoring. Undo the change instead.
  **On screen:** Code `examples/err04_changed_test.py`, line 5, 6, 7, 8, 9 highlighted, output `examples/err04_changed_test.expected`
- **Narration:** Breather. Now you know the four most common refactoring mistakes.
  **On screen:** Breather card
    - Test several different inputs.
    - Rename every call, or keep the old name.
    - Never change a test to match new output.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - Test several different inputs.
    - Rename every call, or keep the old name.
    - Never change a test to match new output.
- **Breather:** 4 quiet seconds.

## Scene 12: Think beyond

**Section:** Think beyond

**Direction:** Two open questions. No answers are given.

- **Narration:** First. Sam's sales function adds up the day and prints a report, in the same loop. How would you split it, and which tests would you write first?
  **On screen:** Question card: "Sam's sales function adds up the day and prints a report in the same loop. How would you split it, and which tests come first?"
- **Interaction:** "Sam's sales function adds up the day and prints a report in the same loop. How would you split it, and which tests come first?" stays on screen with a 10-second timer.
- **Narration:** Keep your answer for the practice tasks.
  **On screen:** Question card: "Sam's sales function adds up the day and prints a report in the same loop. How would you split it, and which tests come first?"
- **Narration:** Second. Sometimes refactoring is not worth it, for example code that will be deleted next week. What would you ask before you decide?
  **On screen:** Question card: "When is refactoring someone else's code not worth it? What would you ask first?"
- **Interaction:** "When is refactoring someone else's code not worth it? What would you ask first?" stays on screen with a 10-second timer.
- **Narration:** Think about it after the video.
  **On screen:** Question card: "When is refactoring someone else's code not worth it? What would you ask first?"

## Scene 13: Recap

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a quiz, then the badge.

- **Narration:** Let's recap. Read from the top, say what each part does, and trace one input.
  **On screen:** Recap
    - Read from the top, say what each part does, and trace one input.
- **Narration:** A characterization test records what the code does now. Write these tests before any change.
  **On screen:** Recap
    - Read from the top, say what each part does, and trace one input.
    - A characterization test records what the code does now.
- **Narration:** Refactor in small steps, and run the tests after every step.
  **On screen:** Recap
    - Read from the top, say what each part does, and trace one input.
    - A characterization test records what the code does now.
    - Refactor in small steps: rename, constants, extract a function.
    - Run the tests after every step.
- **Narration:** In a diff, minus was removed and plus was added.
  **On screen:** Recap
    - Read from the top, say what each part does, and trace one input.
    - A characterization test records what the code does now.
    - Refactor in small steps: rename, constants, extract a function.
    - Run the tests after every step.
    - In a diff, `-` was removed and `+` was added.
- **Narration:** And check every AI claim with a run, and every AI change with your tests.
  **On screen:** Recap
    - Read from the top, say what each part does, and trace one input.
    - A characterization test records what the code does now.
    - Refactor in small steps: rename, constants, extract a function.
    - Run the tests after every step.
    - In a diff, `-` was removed and `+` was added.
    - Check every AI claim with a run, and every AI change with your tests.
- **Narration:** One last check. During a refactoring, a test fails. What do you do?
  **On screen:** Quick check: "During a refactoring, one of your tests fails. What do you do?" (options shown)
- **Interaction:** "During a refactoring, one of your tests fails. What do you do?" stays on screen with a 10-second timer.
- **Narration:** D. Undo the change, and try a smaller step. The test is telling you the truth.
  **On screen:** Quick check: "During a refactoring, one of your tests fails. What do you do?" (answer revealed: Undo the change and try a smaller step)
- **Narration:** Quest complete! You earned 100 XP and the Code Reviewer badge.
  **On screen:** Code Reviewer You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 14: Practice

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. Three warm-up tasks at 10 XP, and three apply tasks at 20.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's refactor that changed a boundary.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 15: What's next

**Section:** What's next

**Direction:** End card. Tease the Final Boss: the complete AI-assisted workflow. Hold quietly.

- **Narration:** Today, Asha improved code that someone else wrote. Next, she builds a complete program of her own, from the first plan.
  **On screen:** Final Boss: The Personal Task Manager Plan, build, test, review and improve, with AI.
- **Narration:** In Chapter 28, the Final Boss, you will build a personal task manager with an AI assistant: plan, build, test, review and improve.
  **On screen:** Final Boss: The Personal Task Manager Plan, build, test, review and improve, with AI.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Final Boss: The Personal Task Manager Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 28.
  **On screen:** Final Boss: The Personal Task Manager Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
