# Video Script: Chapter 6: Making Decisions: if, elif and else

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:39.

## Scene 1: Introduction (0:00 to 0:58)

**Section:** Introduction

**Direction:** Open on the crash from Chapter 5. Show the finished checkout that decides as the mission, then the AI tease. No question yet.

- **Narration:** Welcome back to Code Quest. This is Chapter 6, the start of Module 2.
  **On screen:** Making Decisions: if, elif and else
- **Narration:** Today your programs learn to decide. They check a fact, and then they choose what to do.
  **On screen:** Making Decisions: if, elif and else Check a fact. Choose what to do.
- **Narration:** And an AI assistant will promise a free biscuit for exactly 15. Its own code will say no.
  **On screen:** Making Decisions: if, elif and else Check a fact. Choose what to do.
- **Narration:** Remember the bill splitter from Chapter 5? Someone typed 0 people, and the program crashed with a Zero Division Error.
  **On screen:** A program that cannot say no
    - The Chapter 5 bill splitter crashed with 0 people: `ZeroDivisionError`.
- **Narration:** And it could not treat customers differently. A member and a visitor got exactly the same bill.
  **On screen:** A program that cannot say no
    - The Chapter 5 bill splitter crashed with 0 people: `ZeroDivisionError`.
    - It could not give a discount only to members.
- **Narration:** It ran every line, every time, whatever the answers were.
  **On screen:** A program that cannot say no
    - The Chapter 5 bill splitter crashed with 0 people: `ZeroDivisionError`.
    - It could not give a discount only to members.
    - It ran every line, every time, whatever the answers were.
- **Narration:** So here is today's mission. Asha's checkout asks three questions, as in Chapter 4.
  **On screen:** Code `examples/ex07_checkout.py`, line 2, 3, 4 highlighted, output `examples/ex07_checkout.expected`
- **Narration:** Then it decides. Members get a 10 percent discount. Everyone else pays the full bill.
  **On screen:** Code `examples/ex07_checkout.py`, line 7, 8, 9, 10 highlighted, output `examples/ex07_checkout.expected`
- **Narration:** And it decides again. Pay 15 or more, and you get a free biscuit.
  **On screen:** Code `examples/ex07_checkout.py`, line 16, 17, 18, 19 highlighted, output `examples/ex07_checkout.expected`
- **Narration:** Two decisions, made by the program itself. Let's build them.
  **On screen:** Code `examples/ex07_checkout.py`, output `examples/ex07_checkout.expected`

## Scene 2: Learning goals (0:58 to 1:17)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Write comparisons, the questions a program can ask.
  **On screen:** By the end, you will be able to:
    - Write comparisons with `==`, `!=`, `<`, `>`, `<=` and `>=`.
- **Narration:** Write if, elif and else blocks, with colons and indentation.
  **On screen:** By the end, you will be able to:
    - Write comparisons with `==`, `!=`, `<`, `>`, `<=` and `>=`.
    - Write `if`, `elif` and `else` blocks with colons and indentation.
- **Narration:** Combine conditions with and, or, and not.
  **On screen:** By the end, you will be able to:
    - Write comparisons with `==`, `!=`, `<`, `>`, `<=` and `>=`.
    - Write `if`, `elif` and `else` blocks with colons and indentation.
    - Combine conditions with `and`, `or` and `not`.
- **Narration:** Compare text answers safely, whatever capital letters the user types.
  **On screen:** By the end, you will be able to:
    - Write comparisons with `==`, `!=`, `<`, `>`, `<=` and `>=`.
    - Write `if`, `elif` and `else` blocks with colons and indentation.
    - Combine conditions with `and`, `or` and `not`.
    - Compare text answers safely with `.strip()` and `.lower()`.
- **Narration:** And fix the errors that beginners meet with if.
  **On screen:** By the end, you will be able to:
    - Write comparisons with `==`, `!=`, `<`, `>`, `<=` and `>=`.
    - Write `if`, `elif` and `else` blocks with colons and indentation.
    - Combine conditions with `and`, `or` and `not`.
    - Compare text answers safely with `.strip()` and `.lower()`.
    - Fix the `SyntaxError` and `IndentationError` that `if` causes.

## Scene 3: Why this matters (1:17 to 1:33)

**Section:** Why this matters

**Direction:** Connect decisions to apps the learner uses every day.

- **Narration:** Real programs decide all the time. A cash machine checks your balance. A shop gives free delivery for a big order.
  **On screen:** Why this matters
    - A cash machine checks your balance before it pays out.
    - A shop gives free delivery when the order is big enough.
- **Narration:** A login page lets you in only when the password matches. Each one checks a fact, and then chooses what to do.
  **On screen:** Why this matters
    - A cash machine checks your balance before it pays out.
    - A shop gives free delivery when the order is big enough.
    - A login page lets you in only when the password matches.

## Scene 4: The idea: conditions are True or False (1:33 to 3:21)

**Section:** The idea

**Direction:** Teach comparison operators with the table, then the if diagram, then the gate analogy. Then a quiz on the boundary, then a breather.

- **Narration:** A condition is a question that Python answers with True or False. You met True and False in Chapter 2. They are the two values of the type bool.
  **On screen:** Table: Six comparison operators
- **Narration:** Double equals asks: are these two values equal?
  **On screen:** Table: Six comparison operators (row 1 in focus)
- **Narration:** Exclamation mark equals asks the opposite: are they different?
  **On screen:** Table: Six comparison operators (row 2 in focus)
- **Narration:** Less than, and greater than. Look closely: 15 is not greater than 15, so that one is False.
  **On screen:** Table: Six comparison operators (row 4 in focus)
- **Narration:** Add an equals sign, and the value itself is included. 15 is greater than or equal to 15, so this one is True.
  **On screen:** Table: Six comparison operators (row 6 in focus)
- **Narration:** And remember: one equals sign gives a name a value. Two equals signs ask a question.
  **On screen:** Table: Six comparison operators
- **Narration:** An if statement asks a condition. If the answer is True, Python runs the block. If it is False, Python skips it.
  **On screen:** if runs a block only when it is True
- **Narration:** The block is the group of lines that are indented, four spaces in, under the line that ends with a colon.
  **On screen:** if runs a block only when it is True
- **Narration:** The last line is not indented, so it always runs.
  **On screen:** if runs a block only when it is True
- **Narration:** Think of a gate at the cafe door. It checks one fact: is this person a member? True, it opens. False, it stays closed.
  **On screen:** A condition is like a gate
    - A gate at the cafe door checks one fact: is this person a member?
    - True: the gate opens. False: it stays closed.
- **Narration:** But unlike a person at a door, the gate cannot guess. Yes with a capital Y and yes with a small y are two different answers.
  **On screen:** A condition is like a gate
    - A gate at the cafe door checks one fact: is this person a member?
    - True: the gate opens. False: it stays closed.
    - Unlike a person, the gate cannot guess: `"Yes"` and `"yes"` are different answers.
- **Narration:** Quick check. To pay is exactly 15. Which of these conditions is True?
  **On screen:** Quick check: "`to_pay` is exactly `15`. Which condition is `True`?" (options shown)
- **Interaction:** "`to_pay` is exactly `15`. Which condition is `True`?" stays on screen with a 10-second timer.
- **Narration:** C. Greater than or equal to. The equals sign includes 15 itself.
  **On screen:** Quick check: "`to_pay` is exactly `15`. Which condition is `True`?" (answer revealed: `to_pay >= 15`)
- **Narration:** Take a breather. Here is what you know so far.
  **On screen:** Breather card
    - A condition is `True` or `False`.
    - `==` asks; one `=` gives a value.
    - `if` runs its indented block only when `True`.
- **Narration:** Next, Asha asks Python her first questions.
  **On screen:** Breather card
    - A condition is `True` or `False`.
    - `==` asks; one `=` gives a value.
    - `if` runs its indented block only when `True`.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Compare values (3:21 to 4:13)

**Section:** Build it step by step

**Direction:** Each comparison is explained before the prediction. Reveal the output after the question.

- **Narration:** Step 1. Asha stores the tea price, 3.5. Line 3 asks: is it greater than 3?
  **On screen:** Code `examples/ex01_compare.py`, line 2, 3 highlighted, output hidden
- **Narration:** Line 4 asks if it equals 3.5, and line 5 asks if it is different from 3.5.
  **On screen:** Code `examples/ex01_compare.py`, line 4, 5 highlighted, output hidden
- **Narration:** Line 6 asks if it is less than or equal to 3. Line 7 compares two words.
  **On screen:** Code `examples/ex01_compare.py`, line 6, 7 highlighted, output hidden
- **Narration:** And line 8 asks for the type of a comparison.
  **On screen:** Code `examples/ex01_compare.py`, line 8 highlighted, output hidden
- **Interaction:** "What do line 5 and line 7 print?" stays on screen with a 10-second timer.
- **Narration:** Lines 3 and 4 are True. Line 5 is False, because the price is not different from 3.5.
  **On screen:** Code `examples/ex01_compare.py`, line 3, 4, 5 highlighted, output `examples/ex01_compare.expected`
- **Narration:** Line 7 is False too. Tea with a capital T and tea with a small t are different text, like the gate.
  **On screen:** Code `examples/ex01_compare.py`, line 7 highlighted, output `examples/ex01_compare.expected`
- **Narration:** And line 8 shows the type of a comparison: bool.
  **On screen:** Code `examples/ex01_compare.py`, line 8 highlighted, output `examples/ex01_compare.expected`

## Scene 6: Step 2: if (4:13 to 4:53)

**Section:** Build it step by step

**Direction:** The file types in. Teach the colon and the block, then ask which lines run for the typed answer 0.

- **Narration:** Step 2. Line 2 asks for the number of people. Line 3 is the if: the condition, people equals 0, and then a colon.
  **On screen:** Code `examples/ex02_if.py`, lines 1 to 3 typed in, line 3 highlighted, output hidden
- **Narration:** Lines 4 and 5 are indented. They are the block.
  **On screen:** Code `examples/ex02_if.py`, lines 1 to 5 typed in, line 4, 5 highlighted, output hidden
- **Narration:** Line 6 is not indented. It is outside the block.
  **On screen:** Code `examples/ex02_if.py`, lines 1 to 6 typed in, line 6 highlighted, output hidden
- **Interaction:** "The user types `0`. Which lines print?" stays on screen with a 10-second timer.
- **Narration:** The condition is True, so both lines of the block run, and then line 6.
  **On screen:** Code `examples/ex02_if.py`, lines 1 to 6 typed in, line 4, 5, 6 highlighted, output `examples/ex02_if.expected`
- **Narration:** Type 4 instead, and the condition is False. Python skips the block, and prints only: Thank you.
  **On screen:** Code `examples/ex02_if.py`, lines 1 to 6 typed in, line 6 highlighted, output `examples/ex02_if.expected`

## Scene 7: Step 3: else (4:53 to 5:38)

**Section:** Build it step by step

**Direction:** Call back to the Chapter 5 crash. Teach that exactly one of two blocks runs, ask, then reveal.

- **Narration:** Step 3. This is the fix for the bill splitter's crash. Line 4 asks: is the number of people greater than 0? If so, lines 5 and 6 share the bill.
  **On screen:** Code `examples/ex03_else.py`, line 4, 5, 6 highlighted, output hidden
- **Narration:** Line 7 says else. Its block runs when the condition is False.
  **On screen:** Code `examples/ex03_else.py`, line 7, 8 highlighted, output hidden
- **Narration:** Exactly one of the two blocks runs, never both. Then line 9 runs either way.
  **On screen:** Code `examples/ex03_else.py`, line 9 highlighted, output hidden
- **Interaction:** "The user types `0` people. Does line 5, the division, run?" stays on screen with a 10-second timer.
- **Narration:** No. 0 is not greater than 0, so the condition is False. Python jumps to the else block.
  **On screen:** Code `examples/ex03_else.py`, line 7, 8 highlighted, output `examples/ex03_else.expected`
- **Narration:** The division never happens, so there is no crash. A clear message instead, and then Done.
  **On screen:** Code `examples/ex03_else.py`, line 9 highlighted, output `examples/ex03_else.expected`

## Scene 8: Step 4: elif and boundary values (5:38 to 6:31)

**Section:** Build it step by step

**Direction:** Teach elif as a ladder checked from the top, ask about the boundary value, then explain why order matters.

- **Narration:** Step 4. The cafe has two rewards. A free cake for 50 or more, on lines 3 and 4.
  **On screen:** Code `examples/ex04_elif.py`, line 3, 4 highlighted, output hidden
- **Narration:** Elif means else if. Lines 5 and 6 give a free biscuit for 15 or more.
  **On screen:** Code `examples/ex04_elif.py`, line 5, 6 highlighted, output hidden
- **Narration:** And the else block catches everything else.
  **On screen:** Code `examples/ex04_elif.py`, line 7, 8 highlighted, output hidden
- **Narration:** Python checks from the top, and runs only the first block whose condition is True. Then it skips the rest.
  **On screen:** Code `examples/ex04_elif.py`, line 3, 5 highlighted, output hidden
- **Interaction:** "The customer pays exactly `15`. Which reward prints?" stays on screen with a 10-second timer.
- **Narration:** A free biscuit. Line 3 is False, because 15 is less than 50. Line 5 is True, because greater than or equal includes 15.
  **On screen:** Code `examples/ex04_elif.py`, line 5, 6 highlighted, output `examples/ex04_elif.expected`
- **Narration:** Exactly 15 is a boundary value: the point where the result changes. And notice the order: the biggest amount comes first. It matters later today.
  **On screen:** Code `examples/ex04_elif.py`, line 3, 5 highlighted, output `examples/ex04_elif.expected`

## Scene 9: Step 5: and, or, not (6:31 to 8:19)

**Section:** Build it step by step

**Direction:** Teach the three rules first, then predict two lines, reveal, then a quiz and a breather.

- **Narration:** Step 5. Sometimes one fact is not enough. And is True only when both sides are True.
  **On screen:** Table: Step 5: Combine conditions (row 1 in focus)
- **Narration:** Or is True when at least one side is True.
  **On screen:** Table: Step 5: Combine conditions (row 2 in focus)
- **Narration:** And not turns True into False, and False into True.
  **On screen:** Table: Step 5: Combine conditions (row 3 in focus)
- **Narration:** Asha is a member, but she pays only 12.
  **On screen:** Code `examples/ex05_and_or.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Line 5 joins two facts with and. Line 6 joins the same two facts with or.
  **On screen:** Code `examples/ex05_and_or.py`, line 5, 6 highlighted, output hidden
- **Interaction:** "What do line 5 and line 6 print?" stays on screen with a 10-second timer.
- **Narration:** Line 5 is False. She is a member, but 12 is not 15 or more, and and needs both.
  **On screen:** Code `examples/ex05_and_or.py`, line 5 highlighted, output `examples/ex05_and_or.expected`
- **Narration:** Line 6 is True. Or needs only one, and she is a member.
  **On screen:** Code `examples/ex05_and_or.py`, line 6 highlighted, output `examples/ex05_and_or.expected`
- **Narration:** Line 7, not a member, is False. And line 8 is True, because the day is Friday. Each side of or needs a full comparison.
  **On screen:** Code `examples/ex05_and_or.py`, line 7, 8 highlighted, output `examples/ex05_and_or.expected`
- **Narration:** Here is why. This line forgets the second day equals. Python checks the word Saturday on its own, and any text that is not empty counts as True.
  **On screen:** Code `examples/ex05_or_wrong.py`, line 3 highlighted, output `examples/ex05_or_wrong.expected`
- **Narration:** So the music plays on a Monday. Always write a full comparison on each side of or.
  **On screen:** Code `examples/ex05_or_wrong.py`, line 3 highlighted, output `examples/ex05_or_wrong.expected`
- **Narration:** Quick check. Is member is False, and to pay is 20. What is: is member, or to pay greater than or equal to 15?
  **On screen:** Quick check: "`is_member` is `False` and `to_pay` is `20`. What is `is_member or to_pay >= 15`?" (options shown)
- **Interaction:** "`is_member` is `False` and `to_pay` is `20`. What is `is_member or to_pay >= 15`?" stays on screen with a 10-second timer.
- **Narration:** A. True. The customer is not a member, but 20 is 15 or more, and or needs only one side.
  **On screen:** Quick check: "`is_member` is `False` and `to_pay` is `20`. What is `is_member or to_pay >= 15`?" (answer revealed: `True`)
- **Narration:** Breather. Roll your shoulders, and take a slow breath.
  **On screen:** Breather card
    - `else` runs when the condition is `False`.
    - Python runs the first `elif` that is `True`.
    - `and` needs both; `or` needs one.
- **Narration:** One more piece, and Asha's checkout is ready: answers typed by real people.
  **On screen:** Breather card
    - `else` runs when the condition is `False`.
    - Python runs the first `elif` that is `True`.
    - `and` needs both; `or` needs one.
- **Breather:** 4 quiet seconds.

## Scene 10: Step 6: Safe text answers (8:19 to 8:58)

**Section:** Build it step by step

**Direction:** Teach strip and lower on the answer, then ask about the typed answer with a capital and a space, then reveal.

- **Narration:** Step 6. Real people type Yes, or yes, or yes with a space at the end. To the gate, those are all different.
  **On screen:** Code `examples/ex06_lower.py`, line 2 highlighted, output hidden
- **Narration:** So line 3 cleans the answer first. Strip removes the spaces at both ends. Lower makes every letter small, as in Chapter 3.
  **On screen:** Code `examples/ex06_lower.py`, line 3 highlighted, output hidden
- **Narration:** Only then does it compare with yes, in small letters.
  **On screen:** Code `examples/ex06_lower.py`, line 3, 4 highlighted, output hidden
- **Interaction:** "The user types `Yes ` with a capital Y and a space. Is the condition on line 3 `True`?" stays on screen with a 10-second timer.
- **Narration:** Yes, it is True. After strip and lower, the answer is exactly yes. So the member discount prints.
  **On screen:** Code `examples/ex06_lower.py`, line 3, 4 highlighted, output `examples/ex06_lower.expected`

## Scene 11: See the outcome: the checkout that decides (8:58 to 10:04)

**Section:** See the outcome

**Direction:** Return to the mission. Explain every group of lines, ask about the reward for Asha's answers, reveal. Hand over to the AI story.

- **Narration:** Back to the mission. Lines 2 to 4 ask the questions. Line 4 cleans the member answer straight away, with strip and lower.
  **On screen:** Code `examples/ex07_checkout.py`, line 2, 3, 4 highlighted, output hidden
- **Narration:** Line 6 works out the bill: the number of teas times 3.5.
  **On screen:** Code `examples/ex07_checkout.py`, line 6 highlighted, output hidden
- **Narration:** Lines 7 to 10 decide the discount. Members get 10 percent. Everyone else gets a discount of 0.
  **On screen:** Code `examples/ex07_checkout.py`, line 7, 8, 9, 10 highlighted, output hidden
- **Narration:** Line 11 takes the discount away, and lines 13 to 15 print the bill.
  **On screen:** Code `examples/ex07_checkout.py`, line 11, 13, 14, 15 highlighted, output hidden
- **Narration:** Lines 16 to 19 decide the reward: a biscuit for 15 or more.
  **On screen:** Code `examples/ex07_checkout.py`, line 16, 17, 18, 19 highlighted, output hidden
- **Interaction:** "Asha types `6` teas and `Yes`. Does she get the free biscuit?" stays on screen with a 10-second timer.
- **Narration:** Six teas cost 21.00. She is a member, so the discount is 2.10.
  **On screen:** Code `examples/ex07_checkout.py`, line 6, 8 highlighted, output `examples/ex07_checkout.expected`
- **Narration:** She pays 18.90. That is 15 or more, so yes: a free biscuit!
  **On screen:** Code `examples/ex07_checkout.py`, line 16, 17 highlighted, output `examples/ex07_checkout.expected`
- **Narration:** Mission complete! And the Chapter 5 crash is gone too: the else from step 3 stops a division by zero. Now Asha wants to be sure her biscuit rule is right. She uses an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex07_checkout.py`, output `examples/ex07_checkout.expected`

## Scene 12: Work with AI: six stages, one rule (10:04 to 14:21)

**Section:** Work with AI

**Direction:** Teach the edge case skill first. Then one conversation per stage, all about the free-biscuit rule. Stage 3 plants the boundary mistake; stage 4 catches it; stage 6 catches a wrong order.

- **Narration:** This chapter's AI skill is asking for edge cases: unusual inputs that can break a condition, like exactly 15, zero, or a capital letter.
  **On screen:** This chapter's AI skill: edge cases
    - An **edge case** is an unusual input that can break a condition.
    - Boundary values, zero, and answers with capitals or spaces are edge cases.
- **Narration:** Ask the AI to list them, then run every one. And the safety habits from Chapter 1 still apply.
  **On screen:** This chapter's AI skill: edge cases
    - An **edge case** is an unusual input that can break a condition.
    - Boundary values, zero, and answers with capitals or spaces are edge cases.
    - Ask AI for the edge cases, then run every one. Never paste private data.
- **Narration:** Stage 1: plan. Asha describes the biscuit rule in words, and asks for the boundary values to test. No code yet.
  **On screen:** AI chat, stage 1: Plan: the rule and its boundary values
    - You: I am a beginner learning if. My cafe gives a free biscuit when the amount to pay is 15 or more. Do not write code yet. List the condition in words, and the boundary values I should test, with the result for each.
- **Narration:** The AI lists 14.99, 15 and 20, with the result for each. 15 is the boundary value, where the result changes.
  **On screen:** AI chat, stage 1: Plan: the rule and its boundary values
    - You: I am a beginner learning if. My cafe gives a free biscuit when the amount to pay is 15 or more. Do not write code yet. List the condition in words, and the boundary values I should test, with the result for each.
    - AI (example answer): 1. The condition: the amount to pay is 15 or more. 2. Test 14.99: no biscuit. 3. Test 15: a biscuit. This is the boundary value, where the result changes. 4. Test 20: a biscuit.
- **Narration:** Stage 2: write. Asha writes the condition herself, and asks what happens at exactly 15. The AI explains that greater than or equal includes 15.
  **On screen:** AI chat, stage 2: Write it yourself, then check the boundary
    - You: I wrote the condition myself. Do not change it. Does the block run when to_pay is exactly 15? Which operator decides it? [code `examples/ai_biscuit_mine.py`]
    - AI (example answer): Yes. `>=` means greater than or equal to, so the value 15 itself is included. The block runs and prints the reward.
- **Narration:** Asha runs it with 15.0. The reward prints. The explanation and the real run agree.
  **On screen:** AI chat, stage 2: Write it yourself, then check the boundary
    - You: I wrote the condition myself. Do not change it. Does the block run when to_pay is exactly 15? Which operator decides it? [code `examples/ai_biscuit_mine.py`]
    - AI (example answer): Yes. `>=` means greater than or equal to, so the value 15 itself is included. The block runs and prints the reward.
    - You: I ran it with 15.0, and it agrees:
- **Narration:** Stage 3: generate. Asha gives the AI her own code. She asks it to add an else, not to change her condition, and to say what 15.0 prints.
  **On screen:** AI chat, stage 3: Generate: add to my code, change nothing
    - You: Here is my code. Add an else that prints 'No biscuit this time'. Do not change my condition. If to_pay is exactly 15.0, tell me exactly what it prints. [code `examples/ai_biscuit_mine.py`]
- **Narration:** The AI sends back the code, and says: a free biscuit. It sounds completely sure.
  **On screen:** AI chat, stage 3: Generate: add to my code, change nothing
    - You: Here is my code. Add an else that prints 'No biscuit this time'. Do not change my condition. If to_pay is exactly 15.0, tell me exactly what it prints. [code `examples/ai_biscuit_mine.py`]
    - AI (example answer): Here is the code. For 15.0 it prints `Reward: a free biscuit`. [code `examples/ai_biscuit_flawed.py`]
- **Narration:** Compare its line 3 with the line Asha gave it.
  **On screen:** AI chat, stage 3: Generate: add to my code, change nothing
    - You: Here is my code. Add an else that prints 'No biscuit this time'. Do not change my condition. If to_pay is exactly 15.0, tell me exactly what it prints. [code `examples/ai_biscuit_mine.py`]
    - AI (example answer): Here is the code. For 15.0 it prints `Reward: a free biscuit`. [code `examples/ai_biscuit_flawed.py`]
- **Interaction:** "The AI says this prints `Reward: a free biscuit` for 15.0. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. The AI quietly changed greater than or equal into greater than. Asha told it not to touch her condition. She will prove the problem with edge cases.
  **On screen:** AI chat, stage 3: Generate: add to my code, change nothing
    - You: Here is my code. Add an else that prints 'No biscuit this time'. Do not change my condition. If to_pay is exactly 15.0, tell me exactly what it prints. [code `examples/ai_biscuit_mine.py`]
    - AI (example answer): Here is the code. For 15.0 it prints `Reward: a free biscuit`. [code `examples/ai_biscuit_flawed.py`]
- **Narration:** Stage 4: test. This is today's skill. Asha asks the AI for the edge cases, and the output each one should give.
  **On screen:** AI chat, stage 4: Test: run every edge case
    - You: Before I trust it, list the edge cases for this rule, with the output each one should give.
- **Narration:** The AI lists 14.99, the boundary value 15, and 20.
  **On screen:** AI chat, stage 4: Test: run every edge case
    - You: Before I trust it, list the edge cases for this rule, with the output each one should give.
    - AI (example answer): 1. `14.99`: No biscuit this time. 2. `15.0`: Reward: a free biscuit. This is the boundary value. 3. `20.0`: Reward: a free biscuit.
- **Narration:** She runs all three on the AI's own code. 14.99 and 20 are right, but 15.0 prints no biscuit.
  **On screen:** AI chat, stage 4: Test: run every edge case
    - You: Before I trust it, list the edge cases for this rule, with the output each one should give.
    - AI (example answer): 1. `14.99`: No biscuit this time. 2. `15.0`: Reward: a free biscuit. This is the boundary value. 3. `20.0`: Reward: a free biscuit.
    - You: I ran your three values on your code. 15.0 fails:
- **Narration:** Now the AI admits it changed her condition. She puts back her greater than or equal.
  **On screen:** AI chat, stage 4: Test: run every edge case
    - You: Before I trust it, list the edge cases for this rule, with the output each one should give.
    - AI (example answer): 1. `14.99`: No biscuit this time. 2. `15.0`: Reward: a free biscuit. This is the boundary value. 3. `20.0`: Reward: a free biscuit.
    - You: I ran your three values on your code. 15.0 fails:
    - AI (example answer): You are right. I changed your `>=` into `>`, so 15 is left out. Put back your condition, `if to_pay >= 15:`.
- **Narration:** With her own condition back on line 3, 15.0 gets the biscuit. The prediction and the real run agree.
  **On screen:** Code `examples/ai_biscuit_fixed.py`, line 3 highlighted, output `examples/ai_biscuit_fixed.expected`
- **Narration:** Stage 5: debug. Back when Asha first typed the rule, she wrote one equals sign. Python stopped with a Syntax Error, before any line ran.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: My first try at the rule gave this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_biscuit_typo.py`]
- **Narration:** She asks for the cause first. The AI points to line 3. Python suggests double equals, but that would reward only exactly 15. The rule is 15 or more, so greater than or equal.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: My first try at the rule gave this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_biscuit_typo.py`]
    - AI (example answer): Line 3 uses one `=`, which gives a name a value. Python suggests `==`, but `to_pay == 15` would reward only exactly 15. Your rule is 15 or more, so write: `if to_pay >= 15:`
- **Narration:** Stage 6: improve. The rewards work. Asha asks for at most two readability improvements that do not change the output.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Here are my reward rules. Suggest at most two improvements for readability, each with one reason. Do not change what it prints for any amount. [code `examples/ex04_elif.py`]
- **Narration:** Suggestion 1, a comment, helps a reader. Suggestion 2 says: check the biscuit rule first, because it is the most common.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Here are my reward rules. Suggest at most two improvements for readability, each with one reason. Do not change what it prints for any amount. [code `examples/ex04_elif.py`]
    - AI (example answer): 1. Add a comment above the rules: `# Rewards: cake for 50 or more, biscuit for 15 or more`. 2. Check the biscuit rule first, because it is the most common reward.
- **Narration:** Remember the order from step 4? Asha does not trust it yet. She tests it with a big amount, 60.
  **On screen:** AI chat, stage 6: Improve: test every suggestion
    - You: Here are my reward rules. Suggest at most two improvements for readability, each with one reason. Do not change what it prints for any amount. [code `examples/ex04_elif.py`]
    - AI (example answer): 1. Add a comment above the rules: `# Rewards: cake for 50 or more, biscuit for 15 or more`. 2. Check the biscuit rule first, because it is the most common reward.
    - You: Before I change anything, I will test suggestion 2 with a big amount, 60.0.
- **Narration:** Here is the suggested order. The biscuit rule on line 3 comes first. The cake rule on line 5 comes second.
  **On screen:** Code `examples/ai_reward_order.py`, line 3, 4, 5, 6 highlighted, output hidden
- **Interaction:** "To pay is `60.0`. Which reward prints?" stays on screen with a 10-second timer.
- **Narration:** A free biscuit, not a cake! 60 is 15 or more, so line 3 is True first, and Python never checks line 5.
  **On screen:** Code `examples/ai_reward_order.py`, line 3, 4 highlighted, output `examples/ai_reward_order.expected`
- **Narration:** The AI was wrong again. Asha keeps her order, with the biggest amount first, and adds only the comment.
  **On screen:** Code `examples/ai_reward_order.py`, line 5 highlighted, output `examples/ai_reward_order.expected`
- **Narration:** Quick check. The rule is 15 or more. Which test value catches greater than written instead of greater than or equal?
  **On screen:** Quick check: "The rule is "15 or more". Which test value catches `>` written instead of `>=`?" (options shown)
- **Interaction:** "The rule is "15 or more". Which test value catches `>` written instead of `>=`?" stays on screen with a 10-second timer.
- **Narration:** B. 15, the boundary value. That is the only value where the two operators disagree.
  **On screen:** Quick check: "The rule is "15 or more". Which test value catches `>` written instead of `>=`?" (answer revealed: `15`)
- **Narration:** Breather. Asha caught two AI mistakes, with two things you learned today: boundary values, and the elif order.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Test the boundary value every time.
    - In an elif ladder, the biggest amount comes first.
- **Narration:** Next, the four mistakes beginners make most with if. You have already met the first one.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Test the boundary value every time.
    - In an elif ladder, the biggest amount comes first.
- **Breather:** 4 quiet seconds.

## Scene 13: Common mistakes (14:21 to 15:58)

**Section:** Common mistakes

**Direction:** Mistake 1 calls back to the debug stage. Mistakes 3 and 4 are spot-it questions on rules taught earlier. Then a summary table and a quiz.

- **Narration:** Mistake 1 is the one Asha debugged: one equals sign in a condition. The message suggests double equals. Ignore the other suggestion; this course does not use it.
  **On screen:** Code `examples/err01_single_equals.py`, line 3 highlighted, error `examples/err01_single_equals.expected_error`
- **Narration:** Mistake 2. Every if, elif and else line ends with a colon. Line 3 has none, and the message says exactly that: expected a colon.
  **On screen:** Code `examples/err02_colon.py`, line 3 highlighted, error `examples/err02_colon.expected_error`
- **Narration:** Now you try. Remember how Python knows which lines belong to the block.
  **On screen:** Code `examples/err03_indent.py`, line 3, 4 highlighted, output hidden
- **Interaction:** "What is wrong with line 4?" stays on screen with a 10-second timer.
- **Narration:** Line 4 is not indented, so the if on line 3 has no block. Python reports an Indentation Error.
  **On screen:** Code `examples/err03_indent.py`, line 3, 4 highlighted, error `examples/err03_indent.expected_error`
- **Narration:** The fix: indent line 4 by four spaces. Most code editors do it for you after the colon.
  **On screen:** Code `examples/err03_indent.py`, line 3, 4 highlighted, error `examples/err03_indent.expected_error`
- **Narration:** One more. Asha is a member, and the answer stored on line 2 is Yes. Think of the gate.
  **On screen:** Code `examples/ex08_case.py`, line 2, 3 highlighted, output hidden
- **Interaction:** "Asha is a member. Why does this program print `No discount`?" stays on screen with a 10-second timer.
- **Narration:** Yes with a capital Y is not equal to yes with a small y. No error at all, a wrong result, and a member pays too much.
  **On screen:** Code `examples/ex08_case.py`, line 2, 3 highlighted, output `examples/ex08_case.expected`
- **Narration:** The fix is the one from step 6: compare the answer after strip and lower.
  **On screen:** Code `examples/ex08_case.py`, line 2, 3 highlighted, output `examples/ex08_case.expected`
- **Narration:** Last breather. These errors will not surprise you any more.
  **On screen:** Breather card
    - `==` compares; `:` ends the line.
    - Indent the block by 4 spaces.
    - Clean text answers before you compare them.
- **Narration:** Two questions to think about on your own come next.
  **On screen:** Breather card
    - `==` compares; `:` ends the line.
    - Indent the block by 4 spaces.
    - Clean text answers before you compare them.
- **Breather:** 4 quiet seconds.

## Scene 14: Think beyond (15:58 to 16:44)

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Asha wants the free biscuit only for members who pay 15 or more. Which word joins the two conditions?
  **On screen:** Question card: "The biscuit is only for members who pay 15 or more. Which word joins the two conditions?"
- **Interaction:** "The biscuit is only for members who pay 15 or more. Which word joins the two conditions?" stays on screen with a 10-second timer.
- **Narration:** Write it, then test it with a member who pays 12, and a visitor who pays 20.
  **On screen:** Question card: "The biscuit is only for members who pay 15 or more. Which word joins the two conditions?"
- **Narration:** Second. Some customers type y, instead of yes. How could one condition accept both answers?
  **On screen:** Question card: "Some customers type `y` instead of `yes`. How could one condition accept both?"
- **Interaction:** "Some customers type `y` instead of `yes`. How could one condition accept both?" stays on screen with a 10-second timer.
- **Narration:** Predict which answers still fail, then test them.
  **On screen:** Question card: "Some customers type `y` instead of `yes`. How could one condition accept both?"

## Scene 15: Recap (16:44 to 17:48)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap.
  **On screen:** Recap
- **Narration:** A condition works out to True or False, the two values of bool.
  **On screen:** Recap
    - A condition works out to `True` or `False`, the two values of `bool`.
- **Narration:** Double equals compares. One equals sign gives a name a value.
  **On screen:** Recap
    - A condition works out to `True` or `False`, the two values of `bool`.
    - `==` compares. One `=` gives a name a value.
- **Narration:** If runs its indented block only when the condition is True, and else runs when it is False.
  **On screen:** Recap
    - A condition works out to `True` or `False`, the two values of `bool`.
    - `==` compares. One `=` gives a name a value.
    - `if` runs its indented block only when the condition is `True`; `else` when it is `False`.
- **Narration:** Only the first True elif block runs, so order matters. And, or, and not combine conditions. Clean text answers before you compare them.
  **On screen:** Recap
    - A condition works out to `True` or `False`, the two values of `bool`.
    - `==` compares. One `=` gives a name a value.
    - `if` runs its indented block only when the condition is `True`; `else` when it is `False`.
    - Python runs only the first `elif` block that is `True`, so order matters.
    - `and`, `or` and `not` combine conditions. Compare text after `.strip().lower()`.
- **Narration:** And with AI: ask for the edge cases, and run every one.
  **On screen:** Recap
    - A condition works out to `True` or `False`, the two values of `bool`.
    - `==` compares. One `=` gives a name a value.
    - `if` runs its indented block only when the condition is `True`; `else` when it is `False`.
    - Python runs only the first `elif` block that is `True`, so order matters.
    - `and`, `or` and `not` combine conditions. Compare text after `.strip().lower()`.
    - Ask AI for edge cases, such as boundary values, and run every one.
- **Narration:** One last check. The cake rule, 50 or more, comes first. Then the biscuit rule, 15 or more. To pay is exactly 50. What prints?
  **On screen:** Quick check: "The rules check `>= 50` (cake) first, then `elif >= 15` (biscuit). `to_pay` is exactly `50`. What prints?" (options shown)
- **Interaction:** "The rules check `>= 50` (cake) first, then `elif >= 15` (biscuit). `to_pay` is exactly `50`. What prints?" stays on screen with a 10-second timer.
- **Narration:** D. A free cake. 50 is greater than or equal to 50, so the first block runs, and Python skips the rest.
  **On screen:** Quick check: "The rules check `>= 50` (cake) first, then `elif >= 15` (biscuit). `to_pay` is exactly `50`. What prints?" (answer revealed: A free cake)
- **Narration:** Mission complete! You earned 100 XP and the Decision Maker badge.
  **On screen:** Decision Maker You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 16: Practice (17:48 to 18:16)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. The practice file has eight tasks, worth 170 XP.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including the cafe's opening hours.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, an AI's delivery rule fails at its boundary value. Fix it.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)
- **Narration:** Test every program with the boundary value. Try each task before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP

## Scene 17: What's next (18:16 to 18:39)

**Section:** What's next

**Direction:** End card. Tease while loops as the fix for a program that gives up after one bad answer. Hold quietly at the end.

- **Narration:** Asha's program now says: people must be 1 or more. But then it simply ends. The customer has to start again.
  **On screen:** Repeat Until Done: while Loops Ask again until the answer is valid.
- **Narration:** In Chapter 7, you will use while loops to ask the question again, and again, until the answer is valid.
  **On screen:** Repeat Until Done: while Loops Ask again until the answer is valid.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Repeat Until Done: while Loops Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 7.
  **On screen:** Repeat Until Done: while Loops Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
