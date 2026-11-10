# Video Script: Chapter 19: Testing Your Code: assert and pytest

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:17.

## Scene 1: Introduction (0:00 to 0:44)

**Section:** Introduction

**Direction:** Open on the Chapter 18 problem: a False that nobody reads. Then the title and the AI tease, then the mission file with no output.

- **Narration:** At the Corner Cafe, Asha's module from Chapter 18 checks itself. Each check prints True.
  **On screen:** One False, and nobody notices
- **Narration:** But one day, a change breaks a tool, and a check prints False. The program carries on. Nobody reads that line.
  **On screen:** One False, and nobody notices
- **Narration:** This is Code Quest, Chapter 19: tests that stop loudly when something breaks.
  **On screen:** Testing Your Code: assert and pytest
- **Narration:** And an AI assistant will write tests for Asha, and promise they catch any mistake. Will they? You will find out by breaking the code on purpose.
  **On screen:** Testing Your Code: assert and pytest If it breaks, a test should fail.
- **Narration:** Here is today's mission: Asha's test file. Line 2 imports her three tools.
  **On screen:** Code `examples/final/test_cafe_tools.py`, line 2 highlighted, output hidden
- **Narration:** Each block below is one test. One command runs them all, and names any tool that breaks. Let's build it.
  **On screen:** Code `examples/final/test_cafe_tools.py`, line 5, 6, 9, 10, 11, 14, 15, 18, 19, 20, 23, 24, 25, 26 highlighted, output hidden

## Scene 2: Learning goals (0:44 to 0:54)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Your goals: write an assert, write and run a pytest file, read its report, test edge cases and decimals, and check an AI's tests.
  **On screen:** By the end, you will be able to:
    - Write an `assert` with a message.
    - Write and run a `pytest` test file.
    - Read a `pytest` report: the test, the line and the values.
    - Test edge cases and decimal results.
    - Check that an AI's tests can really fail.

## Scene 3: Why this matters (0:54 to 1:11)

**Section:** Why this matters

**Direction:** Define a test, then why tests matter when people and AI change code.

- **Narration:** A test runs your code with a known input, and checks the result against the answer you expect. If the result is wrong, the test fails loudly.
  **On screen:** Why this matters
    - A **test** runs your code with a known input and checks the result against the answer you expect.
    - If the result is wrong, the test fails loudly.
- **Narration:** Tests keep code working. Every time you, a colleague or an AI changes it, you run the tests again.
  **On screen:** Why this matters
    - A **test** runs your code with a known input and checks the result against the answer you expect.
    - If the result is wrong, the test fails loudly.
    - Run the tests after every change, by you, a colleague or an AI.

## Scene 4: The idea: input, run, compare (1:11 to 2:25)

**Section:** The idea

**Direction:** Teach the three parts with the diagram, then the three kinds of check, then the smoke alarm and where it stops working. Then a quiz and a breather.

- **Narration:** Every test has three parts. A known input: 40 biscuits. A run of the code: boxes needed. And a comparison: is it 4? Yes means pass. No means fail.
  **On screen:** Every test has three parts
- **Narration:** There are three ways to check a result. A printed check prints False, and carries on.
  **On screen:** Table: Three ways to check a result (row 1 in focus)
- **Narration:** An assert stops the program with an error.
  **On screen:** Table: Three ways to check a result (row 2 in focus)
- **Narration:** And a pytest test runs every test, then names each one that failed.
  **On screen:** Table: Three ways to check a result (row 3 in focus)
- **Narration:** Think of a test as a smoke alarm in the cafe kitchen. It stays quiet while everything is fine.
  **On screen:** A test is like a smoke alarm
    - It stays quiet while everything is fine.
- **Narration:** And it makes a loud noise the moment something goes wrong.
  **On screen:** A test is like a smoke alarm
    - It stays quiet while everything is fine.
    - It makes a loud noise the moment something goes wrong.
- **Narration:** The comparison stops working at one point. An alarm watches the whole room. A test checks only the inputs you wrote.
  **On screen:** A test is like a smoke alarm
    - It stays quiet while everything is fine.
    - It makes a loud noise the moment something goes wrong.
    - Where it stops working: a test checks only the inputs you wrote.
- **Narration:** Quick check. Which of these stops the program when the result is wrong?
  **On screen:** Quick check: "Which check stops the program when the result is wrong?" (options shown)
- **Interaction:** "Which check stops the program when the result is wrong?" stays on screen with a 10-second timer.
- **Narration:** C. Assert. A printed check only prints False, and a comment does nothing at all.
  **On screen:** Quick check: "Which check stops the program when the result is wrong?" (answer revealed: `assert result == 4`)
- **Narration:** Take a breather. Next, Asha sees why a printed check is not enough.
  **On screen:** Breather card
    - A test: known input, run, compare.
    - A printed check is easy to miss.
    - A test checks only the inputs you wrote.
- **Breather:** 4 quiet seconds.

## Scene 5: Steps 1 and 2: From print to assert (2:25 to 3:50)

**Section:** Build it step by step

**Direction:** Show the quiet False, ask what lines 5 and 6 print. Teach assert, show it passing, then failing with a message, and ask whether the report is saved.

- **Narration:** Step 1. Someone typed 1.01 as the tax rate, instead of 1.1. Look at line 2.
  **On screen:** Code `examples/ex01_print_checks.py`, line 2 highlighted, output hidden
- **Narration:** Line 5 checks the tea price with print. Line 6 saves the report.
  **On screen:** Code `examples/ex01_print_checks.py`, line 5, 6 highlighted, output hidden
- **Interaction:** "What do lines 5 and 6 print?" stays on screen with a 10-second timer.
- **Narration:** False, then Report saved. The check found the problem, but the program saved the report anyway.
  **On screen:** Code `examples/ex01_print_checks.py`, line 5, 6 highlighted, output `examples/ex01_print_checks.expected`
- **Narration:** Step 2. An assertion is a statement that a condition must be true. You write assert, then the condition.
  **On screen:** Code `examples/ex02_assert_pass.py`, line 5, 6 highlighted, output `examples/ex02_assert_pass.expected`
- **Narration:** Here the tax rate is right. Both conditions are true, so assert does nothing, and line 7 saves the report.
  **On screen:** Code `examples/ex02_assert_pass.py`, line 7 highlighted, output `examples/ex02_assert_pass.expected`
- **Narration:** But when a condition is false, assert stops the program with an Assertion Error. After a comma, you can add a message.
  **On screen:** Code `examples/ex02_assert_pass.py`, line 5 highlighted, output `examples/ex02_assert_pass.expected`
- **Narration:** Now the wrong rate again, on line 2.
  **On screen:** Code `examples/ex03_assert_fail.py`, line 2 highlighted, output hidden
- **Narration:** Line 5 checks the tea price with assert, and adds a message. Line 6 saves the report.
  **On screen:** Code `examples/ex03_assert_fail.py`, line 5, 6 highlighted, output hidden
- **Interaction:** "Does line 6 save the report?" stays on screen with a 10-second timer.
- **Narration:** No. Line 5 stops the program, so the report is never saved.
  **On screen:** Code `examples/ex03_assert_fail.py`, line 5 highlighted, error `examples/ex03_assert_fail.expected_error`
- **Narration:** And the message says exactly what was wrong: tea with tax should be 3.85.
  **On screen:** Code `examples/ex03_assert_fail.py`, line 5 highlighted, error `examples/ex03_assert_fail.expected_error`

## Scene 6: Step 3: Your first pytest file (3:50 to 5:49)

**Section:** Build it step by step

**Direction:** Install and run commands in a table, then the module, then the test file with its naming rules, ask how many tests and whether they pass. Then a quiz and a breather.

- **Narration:** Step 3. pytest is a popular testing tool. It does not come with Python, so you install it once with pip, Python's package installer.
  **On screen:** Table: Step 3: Install and run pytest (row 1 in focus)
- **Narration:** On macOS and Linux, type python3 instead of python. You will learn more about packages in Chapter 24.
  **On screen:** Table: Step 3: Install and run pytest (row 1 in focus)
- **Narration:** Then you run a test file like this. The dash q option asks for a short, quiet report.
  **On screen:** Table: Step 3: Install and run pytest (row 2 in focus)
- **Narration:** Here is Asha's module from Chapter 18: with tax, and money.
  **On screen:** Code `examples/cafe_tools.py`, line 6, 7, 8, 11, 12, 13 highlighted, output `examples/cafe_tools.expected`
- **Narration:** She adds boxes needed, from the AI section of Chapter 18. Line 18 rounds up with math dot ceil.
  **On screen:** Code `examples/cafe_tools.py`, line 16, 17, 18 highlighted, output `examples/cafe_tools.expected`
- **Narration:** And she removes the old printed checks from the bottom of the file. Tests will replace them, so the module now prints nothing.
  **On screen:** Code `examples/cafe_tools.py`, output `examples/cafe_tools.expected`
- **Narration:** Here is the safe rule for names. Every test is a function whose name starts with test and an underscore. And the file name starts the same way, so pytest finds it when it searches a folder.
  **On screen:** Code `examples/test_cafe_tools.py`, line 5, 9, 13 highlighted, output hidden
- **Narration:** Line 2 imports the three tools. Each test has one assert, with an exact expected value.
  **On screen:** Code `examples/test_cafe_tools.py`, line 2, 6, 10, 14 highlighted, output hidden
- **Interaction:** "How many tests will pytest run, and will they pass?" stays on screen with a 10-second timer.
- **Narration:** Three tests, and all three pass. Each dot is one passing test.
  **On screen:** Code `examples/test_cafe_tools.py`, line 6, 10, 14 highlighted, output `examples/test_cafe_tools.expected`
- **Narration:** The last line counts them, and shows how long the run took. That time changes on every run.
  **On screen:** Code `examples/test_cafe_tools.py`, line 6, 10, 14 highlighted, output `examples/test_cafe_tools.expected`
- **Narration:** Quick check. Which of these functions will pytest run?
  **On screen:** Quick check: "Which function will `pytest` run as a test?" (options shown)
- **Interaction:** "Which function will `pytest` run as a test?" stays on screen with a 10-second timer.
- **Narration:** D. Test tea. Its name starts with test and an underscore. Tea test ends with it, so pytest skips it.
  **On screen:** Quick check: "Which function will `pytest` run as a test?" (answer revealed: `test_tea()`)
- **Narration:** Breather. Next, Asha breaks her module on purpose, to see what a failure looks like.
  **On screen:** Breather card
    - `assert` stops the program when a check is false.
    - Test files and test functions start with `test_`.
    - Each dot is one passing test.
- **Breather:** 4 quiet seconds.

## Scene 7: Step 4: Read a failure (5:49 to 6:45)

**Section:** Build it step by step

**Direction:** Show the broken copy's line 18, ask which test fails, then read the report from the top.

- **Narration:** Step 4. Asha copies her files into a folder called broken. In the copy, line 18 uses round instead of math dot ceil. That is the AI's mistake from Chapter 18.
  **On screen:** Code `examples/broken/cafe_tools.py`, line 18 highlighted, output hidden
- **Narration:** She runs the same three tests on the broken copy, and adds dash dash t b equals short, for a shorter report. Remember: round goes to the nearest whole number.
  **On screen:** Code `examples/broken/test_cafe_tools.py`, line 6, 10, 14 highlighted, output hidden
- **Interaction:** "Which of the three tests will fail?" stays on screen with a 10-second timer.
- **Narration:** The third one. The first line shows two dots and an F. F means one test failed.
  **On screen:** Code `examples/broken/test_cafe_tools.py`, line 14 highlighted, output `examples/broken/test_cafe_tools.expected`
- **Narration:** The report names the test, and its line: 14.
  **On screen:** Code `examples/broken/test_cafe_tools.py`, line 14 highlighted, output `examples/broken/test_cafe_tools.expected`
- **Narration:** The line that starts with E shows the values. Boxes needed returned 3, but the test expected 4. The last line counts one failed and two passed.
  **On screen:** Code `examples/broken/test_cafe_tools.py`, line 14 highlighted, output `examples/broken/test_cafe_tools.expected`

## Scene 8: Steps 5 and 6: Edge cases and decimals (6:45 to 8:20)

**Section:** Build it step by step

**Direction:** Teach edge cases, ask which one catches round, then decimals: ask which test fails, then round and approx.

- **Narration:** Step 5. An edge case is an unusual input at the limit of what a function must handle.
  **On screen:** Code `examples/test_edges.py`, line 5, 9, 13 highlighted, output `examples/test_edges.expected`
- **Narration:** For boxes, the edges are no biscuits, exactly one full box, and one biscuit more than a box. On the working module, all three pass.
  **On screen:** Code `examples/test_edges.py`, line 6, 10, 14 highlighted, output `examples/test_edges.expected`
- **Narration:** Now Asha runs the edge cases on the broken copy. Remember: round goes to the nearest whole number.
  **On screen:** Code `examples/broken/test_edges.py`, line 6, 10, 14 highlighted, output hidden
- **Interaction:** "On the broken copy, which edge case fails: 0, 12 or 13?" stays on screen with a 10-second timer.
- **Narration:** 13. 13 divided by 12 is about 1.08, and round turns that into 1 box. The test expected 2. The other two still pass.
  **On screen:** Code `examples/broken/test_edges.py`, line 14 highlighted, output `examples/broken/test_edges.expected`
- **Narration:** So good tests check normal values and edge values. Each catches mistakes from a different side.
  **On screen:** Code `examples/broken/test_edges.py`, line 14 highlighted, output `examples/broken/test_edges.expected`
- **Narration:** Step 6. In Chapter 2 you saw that point 1, three times, is not exactly point 3. Here are three tests of that total.
  **On screen:** Code `examples/test_floats.py`, line 5, 6, 7 highlighted, output hidden
- **Narration:** Line 12 rounds the total to two decimal places. Line 17 uses pytest dot approx, which accepts a value that is very close.
  **On screen:** Code `examples/test_floats.py`, line 12, 17 highlighted, output hidden
- **Interaction:** "Which of the three tests fails?" stays on screen with a 10-second timer.
- **Narration:** The first one, test exact. The total is a tiny bit more than 0.3.
  **On screen:** Code `examples/test_floats.py`, line 7 highlighted, output `examples/test_floats.expected`
- **Narration:** The other two pass. For decimals, round the result to two places, or use approx.
  **On screen:** Code `examples/test_floats.py`, line 12, 17 highlighted, output `examples/test_floats.expected`

## Scene 9: Step 7: Write the test first (8:20 to 10:04)

**Section:** Build it step by step

**Direction:** The USD rule. Ask whether the new test passes on the current module, read the diff, then the change. Quiz and breather.

- **Narration:** Step 7. The cafe owner wants every price label to start with U S D. Before Asha changes money, she writes the test for the new rule.
  **On screen:** Code `examples/testfirst/test_money_usd.py`, line 5, 6 highlighted, output hidden
- **Interaction:** "Will this test pass on Asha's current module?" stays on screen with a 10-second timer.
- **Narration:** No, and that is what she expects. The money function still returns 4.00.
  **On screen:** Code `examples/testfirst/test_money_usd.py`, line 6 highlighted, output `examples/testfirst/test_money_usd.expected`
- **Narration:** The minus line shows what the test expected. The plus line shows what the function returned.
  **On screen:** Code `examples/testfirst/test_money_usd.py`, line 6 highlighted, output `examples/testfirst/test_money_usd.expected`
- **Narration:** Now she changes line 13, to add U S D before the amount.
  **On screen:** Code `examples/final/cafe_tools.py`, line 13 highlighted, output hidden
- **Narration:** She runs the new test again, and it passes. This is test first thinking: a test that fails before the change and passes after it proves the change did its job.
  **On screen:** Code `examples/final/test_money_usd.py`, line 6 highlighted, output `examples/final/test_money_usd.expected`
- **Narration:** One more run. Her test file from step 3 still expects 4.00, so it now fails on the new module.
  **On screen:** Code `examples/usd/test_cafe_tools.py`, line 10 highlighted, output `examples/usd/test_cafe_tools.expected`
- **Narration:** The rule changed on purpose, so this old test is out of date. Asha updates it to expect U S D 4.00. When a rule changes, its tests change with it.
  **On screen:** Code `examples/usd/test_cafe_tools.py`, line 10 highlighted, output `examples/usd/test_cafe_tools.expected`
- **Narration:** Quick check. You write a test for a new rule, before you change the code. What should happen the first time you run it?
  **On screen:** Quick check: "You write a test for a new rule before you change the code. What should happen when you first run it?" (options shown)
- **Interaction:** "You write a test for a new rule before you change the code. What should happen when you first run it?" stays on screen with a 10-second timer.
- **Narration:** B. It fails. The code does not follow the new rule yet. After the change, it passes.
  **On screen:** Quick check: "You write a test for a new rule before you change the code. What should happen when you first run it?" (answer revealed: It fails)
- **Narration:** Breather. Now Asha puts everything together, in one test file.
  **On screen:** Breather card
    - Edge cases: zero, an exact limit, one more.
    - Compare decimals with `round()` or `approx`.
    - Test first: fail, change, pass.
- **Breather:** 4 quiet seconds.

## Scene 10: See the outcome: the test file (10:04 to 10:53)

**Section:** See the outcome

**Direction:** Return to the mission file, walk the tests, ask how many dots, reveal, then hand over to the AI feature.

- **Narration:** Back to the mission. Lines 5 and 9 test the tax. Line 11 rounds the decimal total first.
  **On screen:** Code `examples/final/test_cafe_tools.py`, line 5, 6, 9, 10, 11 highlighted, output hidden
- **Narration:** Line 15 is the updated money test, with the new U S D label. Lines 18 to 26 test the boxes: normal values, and then the edges. A test can hold several asserts.
  **On screen:** Code `examples/final/test_cafe_tools.py`, line 15, 18, 19, 20, 23, 24, 25, 26 highlighted, output hidden
- **Interaction:** "How many dots will pytest print?" stays on screen with a 10-second timer.
- **Narration:** Five dots, one for each test function, and five passed. A test with three asserts still counts as one test.
  **On screen:** Code `examples/final/test_cafe_tools.py`, line 23 highlighted, output `examples/final/test_cafe_tools.expected`
- **Narration:** Now, after every change, Asha runs one command. Mission complete!
  **On screen:** Code `examples/final/test_cafe_tools.py`, output `examples/final/test_cafe_tools.expected`
- **Narration:** Next, Asha asks an AI assistant to write tests too, one stage at a time.
  **On screen:** Code `examples/final/test_cafe_tools.py`, output `examples/final/test_cafe_tools.expected`

## Scene 11: Work with AI: six stages, one test file (10:53 to 15:03)

**Section:** Work with AI

**Direction:** Teach the skill. One conversation per stage, all about a test file for cafe_tools. Generate: tests that cannot fail. Test: the broken copy. Debug: an exact decimal. Improve: the AI deletes two useful tests.

- **Narration:** This chapter's AI skill: check that the AI's tests really test something. A test that can never fail looks exactly like a test that passes.
  **On screen:** This chapter's AI skill: check the tests
    - A test that can never fail looks exactly like a test that passes.
- **Narration:** So break a copy of the code on purpose. Good tests fail on it. And never paste private data.
  **On screen:** This chapter's AI skill: check the tests
    - A test that can never fail looks exactly like a test that passes.
    - Break a copy of the code on purpose. Good tests fail on it.
    - Never paste private data. You are responsible for the tests you keep.
- **Narration:** Stage 1: plan. Asha asks for the inputs to test, each with its exact expected result. No code yet.
  **On screen:** AI chat, stage 1: Plan: inputs and expected results
    - You: I am learning pytest. My function boxes_needed rounds up to boxes of 12. Do not write code yet. List the inputs I should test, with the exact expected result for each.
- **Narration:** The AI lists a part box, an exact division, zero, and the edge of one box.
  **On screen:** AI chat, stage 1: Plan: inputs and expected results
    - You: I am learning pytest. My function boxes_needed rounds up to boxes of 12. Do not write code yet. List the inputs I should test, with the exact expected result for each.
    - AI (example answer): 1. 40 biscuits: 4 boxes, a part box. 2. 24 biscuits: 2 boxes, an exact division. 3. 0 biscuits: 0 boxes. 4. 12 and 13 biscuits: 1 and 2 boxes, the edge of one box.
- **Narration:** Asha works out every expected result herself, by hand.
  **On screen:** AI chat, stage 1: Plan: inputs and expected results
    - You: I am learning pytest. My function boxes_needed rounds up to boxes of 12. Do not write code yet. List the inputs I should test, with the exact expected result for each.
    - AI (example answer): 1. 40 biscuits: 4 boxes, a part box. 2. 24 biscuits: 2 boxes, an exact division. 3. 0 biscuits: 0 boxes. 4. 12 and 13 biscuits: 1 and 2 boxes, the edge of one box.
    - You: I checked each one by hand: 40 divided by 12 is 3.33, so 4 boxes. They are all right.
- **Narration:** Stage 2: write. Asha writes two tests herself: 24 biscuits, and 40 biscuits. She asks the AI what they do not test yet.
  **On screen:** AI chat, stage 2: Write: her own tests first
    - You: First I wrote two tests myself. Do not change them. Which behaviour do they not test yet? [code `examples/ai/test_mine.py`]
- **Narration:** The AI names zero, and the edge between 12 and 13. She will check the AI's file for those too.
  **On screen:** AI chat, stage 2: Write: her own tests first
    - You: First I wrote two tests myself. Do not change them. Which behaviour do they not test yet? [code `examples/ai/test_mine.py`]
    - AI (example answer): They test an exact division and a part box. They do not test 0 biscuits, or the edge between 12 and 13.
- **Narration:** Stage 3: generate. Asha asks the AI for a test file that catches any mistake in boxes needed.
  **On screen:** AI chat, stage 3: Generate: a test file from the AI
    - You: Write pytest tests for my cafe_tools module. They must catch any mistake in boxes_needed.
- **Narration:** The AI writes three tests, and makes a big promise.
  **On screen:** AI chat, stage 3: Generate: a test file from the AI
    - You: Write pytest tests for my cafe_tools module. They must catch any mistake in boxes_needed.
    - AI (example answer): Here are three tests. They will catch any mistake in `boxes_needed`. [code `examples/ai/test_ai_tools.py`]
- **Narration:** On Asha's working module, all three pass. Look at the two box tests. Line 10 uses 24 biscuits. And the test on line 14 calls boxes needed with zero.
  **On screen:** Code `examples/ai/test_ai_tools.py`, line 10, 14, 15 highlighted, output `examples/ai/test_ai_tools.expected`
- **Interaction:** "The AI says these tests catch any mistake in `boxes_needed`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. 24 divides exactly, so even round gives 2. And line 15 has no assert, so that test can never fail.
  **On screen:** Code `examples/ai/test_ai_tools.py`, line 10, 15 highlighted, output `examples/ai/test_ai_tools.expected`
- **Narration:** Stage 4: test. Asha asks which of the AI's tests should fail on her broken copy.
  **On screen:** AI chat, stage 4: Test: run them on the broken copy
    - You: My broken copy uses round instead of math.ceil. Which of your three tests should fail on it, and why?
- **Narration:** This time the AI admits it: none of them.
  **On screen:** AI chat, stage 4: Test: run them on the broken copy
    - You: My broken copy uses round instead of math.ceil. Which of your three tests should fail on it, and why?
    - AI (example answer): None of them. 24 divided by 12 is exactly 2, so round gives the right answer. And test_zero has no assert, so it can never fail.
- **Narration:** So she asks for a better file: exact values, normal cases and edge cases, one behaviour per test.
  **On screen:** AI chat, stage 4: Test: run them on the broken copy
    - You: My broken copy uses round instead of math.ceil. Which of your three tests should fail on it, and why?
    - AI (example answer): None of them. 24 divided by 12 is exactly 2, so round gives the right answer. And test_zero has no assert, so it can never fail.
    - You: Then write a better file. Test exact expected values, normal cases and the edge cases from my plan, one behaviour per test.
- **Narration:** She makes a broken copy of her finished module, with round on line 18, and runs them anyway. Three passed. The tests did not see the broken code.
  **On screen:** Code `examples/ai/broken/test_ai_tools.py`, line 10, 15 highlighted, output `examples/ai/broken/test_ai_tools.expected`
- **Narration:** Then she runs her own two tests on the same copy. The test for 40 biscuits fails, as a good test should.
  **On screen:** Code `examples/ai/broken/test_mine.py`, line 10 highlighted, output `examples/ai/broken/test_mine.expected`
- **Narration:** Stage 5: debug. The AI writes the better file, with seven tests. But on Asha's working module, one test fails: test two items, on line 11.
  **On screen:** Code `examples/ai/test_ai_float.py`, line 11 highlighted, output `examples/ai/test_ai_float.expected`
- **Narration:** She pastes the failing test and the values from the report.
  **On screen:** AI chat, stage 5: Debug: is the code or the test wrong?
    - You: Your new test file fails on my working module. Here is the failing test, and the report says: assert 3.3000000000000003 == 3.3. Is the code or the test wrong? Explain why first. [code `examples/ai/test_ai_float.py`]
- **Narration:** She asks whether the code or the test is wrong. The AI reads the values: the test compares decimals exactly. Round the total first.
  **On screen:** AI chat, stage 5: Debug: is the code or the test wrong?
    - You: Your new test file fails on my working module. Here is the failing test, and the report says: assert 3.3000000000000003 == 3.3. Is the code or the test wrong? Explain why first. [code `examples/ai/test_ai_float.py`]
    - AI (example answer): The test is wrong, not the code. 1.1 plus 2.2 is stored as 3.3000000000000003. Round the total to 2 decimal places before you compare.
- **Narration:** With the total rounded on line 11, all seven tests pass on the working module.
  **On screen:** Code `examples/ai/test_ai_v2.py`, line 11 highlighted, output `examples/ai/test_ai_v2.expected`
- **Narration:** And on the broken copy, two tests fail: 40 biscuits and 13 biscuits. Now the tests can see the broken code.
  **On screen:** Code `examples/ai/broken/test_ai_v2.py`, line 23, 31 highlighted, output `examples/ai/broken/test_ai_v2.expected`
- **Narration:** Stage 6: improve. Asha asks for one improvement.
  **On screen:** AI chat, stage 6: Improve: before you delete a test
    - You: All seven tests pass. Suggest at most one improvement, with one reason.
- **Narration:** The AI says: delete the tests for 24 and for zero, because 40 and 13 already check rounding up.
  **On screen:** AI chat, stage 6: Improve: before you delete a test
    - You: All seven tests pass. Suggest at most one improvement, with one reason.
    - AI (example answer): Delete test_full_boxes and test_zero. The tests for 40 and 13 already check rounding up, so those two repeat them.
- **Narration:** Asha remembers her own bug from Chapter 18: double slash, then plus 1. It was wrong for 24 biscuits. She makes a second broken copy with that bug.
  **On screen:** Code `examples/ai/broken2/cafe_tools.py`, line 18 highlighted, output hidden
- **Narration:** Asha tries the AI's shorter file on it. Five passed. Without those two tests, her old bug would slip through.
  **On screen:** Code `examples/ai/broken2/test_ai_short.py`, line 19, 23 highlighted, output `examples/ai/broken2/test_ai_short.expected`
- **Narration:** The full file catches it: 24 biscuits gives 3, and zero biscuits gives 1. So Asha keeps every test. The AI was wrong again.
  **On screen:** Code `examples/ai/broken2/test_ai_v2.py`, line 19, 27 highlighted, output `examples/ai/broken2/test_ai_v2.expected`
- **Narration:** Quick check. All of an AI's tests pass. What is the best next check?
  **On screen:** Quick check: "All of an AI's tests pass. What is the best next check?" (options shown)
- **Interaction:** "All of an AI's tests pass. What is the best next check?" stays on screen with a 10-second timer.
- **Narration:** A. Run them on a copy you broke on purpose. Good tests fail on broken code.
  **On screen:** Quick check: "All of an AI's tests pass. What is the best next check?" (answer revealed: Run them on a copy you broke on purpose)
- **Narration:** Breather. You watched Asha check every AI test, and catch two weak suggestions by breaking the code on purpose.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - A test with no assert can never fail.
    - Before you delete a test, check what it catches.
- **Narration:** Next, the mistakes beginners make with tests.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - A test with no assert can never fail.
    - Before you delete a test, check what it catches.
- **Breather:** 4 quiet seconds.

## Scene 12: Common mistakes (15:03 to 16:19)

**Section:** Common mistakes

**Direction:** Mistake 1 is a spot-it on the naming rule. Mistakes 2 and 3 call back. Mistake 4 is a spot-it on the import.

- **Narration:** Mistake 1. Asha runs this file with pytest. Remember the naming rule from step 3.
  **On screen:** Code `examples/err01_no_prefix.py`, line 5, 6 highlighted, output hidden
- **Interaction:** "pytest says that no tests ran. Which name breaks the rule?" stays on screen with a 10-second timer.
- **Narration:** The function name, tea tax, on line 5. It does not start with test and an underscore, so pytest skips it, even when you give it this file by name. Rename it test tea tax.
  **On screen:** Code `examples/err01_no_prefix.py`, line 5 highlighted, output `examples/err01_no_prefix.expected`
- **Narration:** You have seen mistakes 2 and 3 in the AI's files. A test with no assert always passes. And an exact comparison of decimals can fail on correct code: round the result, or use approx.
  **On screen:** Mistakes 2 and 3: you have seen them
    - A test with no `assert` always passes. Every test needs an `assert` with an exact expected value.
    - Comparing decimals exactly can fail on correct code. Round the result, or use `pytest.approx()`.
- **Narration:** Mistake 4. Look at the import on line 2, and the test on line 6.
  **On screen:** Code `examples/err02_missing_import.py`, line 2, 6 highlighted, output hidden
- **Interaction:** "What is missing?" stays on screen with a 10-second timer.
- **Narration:** Boxes needed is never imported, so the test stops with a Name Error. Add it to line 2.
  **On screen:** Code `examples/err02_missing_import.py`, line 2 highlighted, output `examples/err02_missing_import.expected`
- **Narration:** The report points at line 6 of the test file, not at the module. A Name Error inside a test means the test itself is wrong.
  **On screen:** Code `examples/err02_missing_import.py`, line 2 highlighted, output `examples/err02_missing_import.expected`

## Scene 13: Think beyond (16:19 to 17:05)

**Section:** Think beyond

**Direction:** Two open questions. No answers are given.

- **Narration:** First. Money of minus 2 returns U S D minus 2.00. How should a refund look? Write a test for the label you would want.
  **On screen:** Question card: "`money(-2)` returns `"USD -2.00"`. How should a refund look? Write a test for the label you want."
- **Interaction:** "`money(-2)` returns `"USD -2.00"`. How should a refund look? Write a test for the label you want." stays on screen with a 10-second timer.
- **Narration:** Decide the rule first, then write the test, then change the code.
  **On screen:** Question card: "`money(-2)` returns `"USD -2.00"`. How should a refund look? Write a test for the label you want."
- **Narration:** Second. Ten tests all pass. How could you find out whether they would catch a mistake in with tax?
  **On screen:** Question card: "Ten tests all pass. How do you find out if they would catch a mistake in `with_tax()`?"
- **Interaction:** "Ten tests all pass. How do you find out if they would catch a mistake in `with_tax()`?" stays on screen with a 10-second timer.
- **Narration:** Try it with a broken copy after the video.
  **On screen:** Question card: "Ten tests all pass. How do you find out if they would catch a mistake in `with_tax()`?"

## Scene 14: Recap (17:05 to 17:36)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then the badge.

- **Narration:** Let's recap. A test compares a result with the answer you expect. Assert stops the program when it fails, and pytest names each failure, its line and its values.
  **On screen:** Recap
    - A test runs code with a known input and compares the result with the expected answer.
    - `assert condition, "message"` stops the program when the condition is false.
    - `pytest` runs every `test_` function and reports each failure by name, line and value.
- **Narration:** Test normal values and edge cases, and compare decimals with round or approx.
  **On screen:** Recap
    - A test runs code with a known input and compares the result with the expected answer.
    - `assert condition, "message"` stops the program when the condition is false.
    - `pytest` runs every `test_` function and reports each failure by name, line and value.
    - Test normal values and edge cases. Compare decimals with `round()` or `pytest.approx()`.
- **Narration:** Write the test first. And break a copy of the code on purpose: good tests fail on it.
  **On screen:** Recap
    - A test runs code with a known input and compares the result with the expected answer.
    - `assert condition, "message"` stops the program when the condition is false.
    - `pytest` runs every `test_` function and reports each failure by name, line and value.
    - Test normal values and edge cases. Compare decimals with `round()` or `pytest.approx()`.
    - Write the test first: it fails before the change and passes after it.
    - Break a copy of the code on purpose: good tests fail on broken code.
- **Narration:** Mission complete! You earned 100 XP and the Quality Guard badge.
  **On screen:** Quality Guard You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 15: Practice (17:36 to 17:52)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn: eight tasks, worth 170 XP. Three warm-up tasks, three apply tasks, and two stretch tasks.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** In the last one, you fix an AI's tests, like Asha did. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 16: What's next (17:52 to 18:17)

**Section:** What's next

**Direction:** End card. Tease the Boss Level as tests written first for a bigger program. Hold quietly at the end.

- **Narration:** Asha's tests guard three small tools. But what about a whole program, with several modules?
  **On screen:** Boss Level 4: The Tested Quiz App Write the tests first. Then build the app.
- **Narration:** In Chapter 20, the Boss Level, you will build a quiz app for the cafe. You will write its tests first, let an AI help with the code, and let the tests be the judge.
  **On screen:** Boss Level 4: The Tested Quiz App Write the tests first. Then build the app.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Boss Level 4: The Tested Quiz App Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 20.
  **On screen:** Boss Level 4: The Tested Quiz App Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
