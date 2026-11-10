# Video Script: Chapter 24: Virtual Environments and Packages

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 19:06.

## Scene 1: Introduction (0:00 to 0:30)

**Section:** Introduction

**Direction:** Open on the AI's install command with the swapped letters. Then the title, then Asha's draft file as the mission, with no answers.

- **Narration:** At the Corner Cafe, Asha's new weather script says a package is missing. She asks an AI assistant what to do.
  **On screen:** Two swapped letters
- **Narration:** Read the package name slowly. Would you run it?
  **On screen:** Two swapped letters
- **Narration:** Welcome to Chapter 24. Today Asha gives her project its own Python, installs packages safely, and checks every name first.
  **On screen:** Virtual Environments and Packages Its own Python. Exact versions. Checked names.
- **Narration:** Here is Asha's draft list of packages for the weather board. By the end, her own program will check it before anything is installed.
  **On screen:** Today's mission: check the list first

## Scene 2: Learning goals (0:30 to 0:41)

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Create and activate a virtual environment, and install a package into it.
  **On screen:** By the end, you will be able to:
    - Create a virtual environment, then activate and leave it.
    - Install a package with `python -m pip`, and list what is installed.
- **Narration:** Record exact versions, and check a package name before you install it.
  **On screen:** By the end, you will be able to:
    - Create a virtual environment, then activate and leave it.
    - Install a package with `python -m pip`, and list what is installed.
    - Record pinned versions in `requirements.txt`, and install from it.
    - Check a package name before you install it.

## Scene 3: Why this matters (0:41 to 1:01)

**Section:** Why this matters

**Direction:** Packages, PyPI and the risk; two computers that must match.

- **Narration:** Asha needs requests for live weather, and tabulate for a neat table. They are packages: code that other people shared. Most live on PyPI, at pypi dot org.
  **On screen:** Why this matters
    - A **package** is code from someone else that you install, such as `requests`.
    - Most packages live on **PyPI**, at pypi.org. Anyone can publish there.
- **Narration:** Anyone can publish there, so a look-alike name can hide harmful code. And her board must run the same way on two laptops.
  **On screen:** Why this matters
    - A **package** is code from someone else that you install, such as `requests`.
    - Most packages live on **PyPI**, at pypi.org. Anyone can publish there.
    - A name one letter away from a famous package can hide harmful code.
    - The cafe laptop and the home laptop must run the board the same way.

## Scene 4: The idea: one toolbox per project (1:01 to 2:25)

**Section:** The idea

**Direction:** Teach the diagram, the toolbox analogy and where it stops, then the words table. Quiz, then a breather.

- **Narration:** Here is the big idea. A virtual environment is a folder that holds its own Python and its own packages, for one project.
  **On screen:** A virtual environment
- **Narration:** Without one, every project's packages get mixed together in the computer's Python.
  **On screen:** A virtual environment
- **Narration:** Think of a separate toolbox for each project. The weather board's tools never get mixed up with the quiz app's tools.
  **On screen:** Like a toolbox for each project
    - The weather board's tools never mix with the quiz app's tools.
- **Narration:** The comparison stops working at one point. A virtual environment is built for one computer. You cannot carry it to another one.
  **On screen:** Like a toolbox for each project
    - The weather board's tools never mix with the quiz app's tools.
    - Where it stops working: you cannot carry the toolbox to another computer.
- **Narration:** On a new computer, you build a new one, from a list of what the project needs.
  **On screen:** Like a toolbox for each project
    - The weather board's tools never mix with the quiz app's tools.
    - Where it stops working: you cannot carry the toolbox to another computer.
    - On a new computer, you build a new one from a list.
- **Narration:** Pip is the tool that installs packages from PyPI.
  **On screen:** Table: Five words for this chapter (row 3 in focus)
- **Narration:** The virtual environment is usually a folder called dot v e n v.
  **On screen:** Table: Five words for this chapter (row 4 in focus)
- **Narration:** And a pinned version names one exact version, with two equals signs. A list of them is called requirements dot t x t.
  **On screen:** Table: Five words for this chapter (row 5 in focus)
- **Narration:** Quick check. Where should Asha install tabulate for the weather board?
  **On screen:** Quick check: "Where should Asha install `tabulate` for the weather board?" (options shown)
- **Interaction:** "Where should Asha install `tabulate` for the weather board?" stays on screen with a 10-second timer.
- **Narration:** C. Into the weather board's own virtual environment. Each project has its own toolbox.
  **On screen:** Quick check: "Where should Asha install `tabulate` for the weather board?" (answer revealed: Into the weather board's `.venv`)
- **Narration:** Breather. Next, Asha builds the toolbox for her weather board.
  **On screen:** Breather card
    - A package is code someone else shared.
    - One virtual environment per project.
    - A pinned version names one exact version.
- **Breather:** 4 quiet seconds.

## Scene 5: Steps 1 and 2: Create and activate (2:25 to 4:11)

**Section:** Build it step by step

**Direction:** Create command per system, what is inside, activate per system, the prompt and the sys.prefix check. Ask about a new terminal.

- **Narration:** Step 1. Asha opens a terminal in her project folder. She runs v e n v, the standard module that makes virtual environments, and names the folder dot v e n v.
  **On screen:** Table: Step 1: Create a virtual environment
- **Narration:** On Windows, she types p y, dash m, v e n v, dot v e n v.
  **On screen:** Table: Step 1: Create a virtual environment (row 1 in focus)
- **Narration:** On macOS and Linux, python3, dash m, v e n v, dot v e n v. Nothing prints, but a new folder appears, with its own python and pip.
  **On screen:** Table: Step 1: Create a virtual environment (row 2 in focus)
- **Narration:** Step 2. Activating tells this terminal to use the Python inside dot v e n v.
  **On screen:** Table: Step 2: Activate it
- **Narration:** On Windows, dot v e n v, backslash, Scripts, backslash, activate.
  **On screen:** Table: Step 2: Activate it (row 1 in focus)
- **Narration:** In PowerShell, the script ends in dot p s 1. The lesson shows what to do if PowerShell refuses it.
  **On screen:** Table: Step 2: Activate it (row 2 in focus)
- **Narration:** On macOS and Linux, source, dot v e n v, slash, bin, slash, activate.
  **On screen:** Table: Step 2: Activate it (row 3 in focus)
- **Narration:** To leave it, type deactivate. And one rule: activate it again every time you open a new terminal.
  **On screen:** Table: Step 2: Activate it (row 4 in focus)
- **Narration:** Now the prompt starts with dot v e n v in brackets. Asha checks it with one line of Python.
  **On screen:** Am I inside?
- **Narration:** Sys dot prefix is the folder of the Python that is running. Sys dot base prefix is the computer's own Python. They differ only inside a virtual environment, so this prints True.
  **On screen:** Am I inside?
- **Narration:** The next morning, Asha opens a new terminal, and types python straight away.
  **On screen:** Am I inside?
- **Interaction:** "In that new terminal, which Python runs: the one in `.venv`, or the computer's own?" stays on screen with a 10-second timer.
- **Narration:** The computer's own Python. A new terminal starts outside, so she must activate dot v e n v again. The prompt tells her: no dot v e n v in brackets, not inside.
  **On screen:** Am I inside?

## Scene 6: Steps 3 and 4: Install, record, reinstall (4:11 to 5:51)

**Section:** Build it step by step

**Direction:** Install and list, freeze and install -r, then read the pinned file with ex01 and predict line 10.

- **Narration:** Step 3. With dot v e n v active, Asha installs tabulate. She types python, dash m, pip install, tabulate.
  **On screen:** Step 3: Install a package
- **Narration:** Python dash m makes sure pip installs into the Python she is running. Pip list then shows what is installed here. Your version numbers may differ.
  **On screen:** Step 3: Install a package
- **Narration:** In Chapter 19, you installed pytest once, with no virtual environment. From now on, each project's packages go inside its own dot v e n v.
  **On screen:** Step 3: Install a package
- **Narration:** Step 4. Pip freeze prints every installed package as a pinned line. The greater than sign saves it into requirements dot t x t.
  **On screen:** Step 4: Record, then reinstall
- **Narration:** At home, Asha creates and activates a new dot v e n v. Then pip install, dash r, requirements dot t x t, installs exactly the same versions.
  **On screen:** Step 4: Record, then reinstall
- **Narration:** Here is the board's file. The hash sign line is a comment. Each other line pins one package.
  **On screen:** The board's requirements file
- **Narration:** Asha's program reads that file. Lines 4 and 5 read the text, and line 6 goes through it.
  **On screen:** Code `examples/ex01_read_requirements.py`, line 4, 5 highlighted, output hidden
- **Narration:** Lines 8 and 9 skip empty lines and comments.
  **On screen:** Code `examples/ex01_read_requirements.py`, line 8, 9 highlighted, output hidden
- **Narration:** Line 10 splits each line at the two equals signs, so name gets the package, and version gets the number.
  **On screen:** Code `examples/ex01_read_requirements.py`, line 10 highlighted, output hidden
- **Narration:** Line 11 prints the name in ten spaces, then the version.
  **On screen:** Code `examples/ex01_read_requirements.py`, line 11 highlighted, output hidden
- **Interaction:** "What does line 11 print for each package?" stays on screen with a 10-second timer.
- **Narration:** Requests and 2.32.3, then tabulate and 0.9.0. The comment line never reaches line 11.
  **On screen:** Code `examples/ex01_read_requirements.py`, line 11 highlighted, output `examples/ex01_read_requirements.expected`

## Scene 7: Step 5: Pinned or not? (5:51 to 7:11)

**Section:** Build it step by step

**Direction:** Teach what makes a line pinned, then predict ex02, then a quiz and a breather.

- **Narration:** Step 5. A line without two equals signs lets pip choose the version. That version can change next month.
  **On screen:** Code `examples/ex02_pins.py`, line 2 highlighted, output hidden
- **Narration:** Greater than, equals, 8 means 8 or newer. That is not exact either.
  **On screen:** Code `examples/ex02_pins.py`, line 2 highlighted, output hidden
- **Narration:** Line 4 calls a line pinned only if it contains two equals signs together.
  **On screen:** Code `examples/ex02_pins.py`, line 4 highlighted, output hidden
- **Interaction:** "Which of the three lines does this program call pinned?" stays on screen with a 10-second timer.
- **Narration:** Only the first: requests, pinned at 2.32.3. Tabulate has no version, and pytest only says 8 or newer.
  **On screen:** Code `examples/ex02_pins.py`, line 4, 5 highlighted, output `examples/ex02_pins.expected`
- **Narration:** Those two lines could install different code on Asha's two laptops.
  **On screen:** Code `examples/ex02_pins.py`, line 6, 7 highlighted, output `examples/ex02_pins.expected`
- **Narration:** Quick check. Which line installs exactly the same version on every computer?
  **On screen:** Quick check: "Which line installs exactly the same version on every computer?" (options shown)
- **Interaction:** "Which line installs exactly the same version on every computer?" stays on screen with a 10-second timer.
- **Narration:** D. Two equals signs pin one exact version. Look closely at C. It has only one.
  **On screen:** Quick check: "Which line installs exactly the same version on every computer?" (answer revealed: `tabulate==0.9.0`)
- **Narration:** Breather. Asha's board now has its own toolbox, and a list of exact versions. Next, the most important habit: checking a name first.
  **On screen:** Breather card
    - Create `.venv`, then activate it.
    - Install with `python -m pip`.
    - Pin exact versions with `==`.
- **Breather:** 4 quiet seconds.

## Scene 8: Step 6: Check a name first (7:11 to 8:39)

**Section:** Build it step by step

**Direction:** The four checks on a PyPI page, then difflib scores. Speak the score, then ask what line 7 prints.

- **Narration:** Step 6. Before Asha installs a package, she opens its page on pypi dot org, and makes four checks.
  **On screen:** Table: Step 6: Four checks before you install
- **Narration:** One. The exact name: every letter must match. PyPI ignores capital letters, so Requests with a capital R is the same package.
  **On screen:** Table: Step 6: Four checks before you install (row 1 in focus)
- **Narration:** Two, links to its code and documentation.
  **On screen:** Table: Step 6: Four checks before you install (row 2 in focus)
- **Narration:** Three, its release history.
  **On screen:** Table: Step 6: Four checks before you install (row 3 in focus)
- **Narration:** Four, who publishes it.
  **On screen:** Table: Step 6: Four checks before you install (row 4 in focus)
- **Narration:** A name one or two letters away from a famous one is a warning sign. People publish look-alike names on purpose, hoping for a spelling mistake.
  **On screen:** Code `examples/ex03_lookalike.py`, line 2 highlighted, output hidden
- **Narration:** The standard module diff lib measures how alike two names are. Its score goes from 0, nothing alike, to 1, the same.
  **On screen:** Code `examples/ex03_lookalike.py`, line 2 highlighted, output hidden
- **Narration:** Line 5 compares reqeusts with requests. Its first argument, None, means no characters are ignored. Even with two letters swapped, line 6 prints a score of 0.875.
  **On screen:** Code `examples/ex03_lookalike.py`, line 5, 6 highlighted, output hidden
- **Narration:** Line 7 uses get close matches. It returns a list of the trusted names whose score is at least the cutoff, here 0.8.
  **On screen:** Code `examples/ex03_lookalike.py`, line 7 highlighted, output hidden
- **Interaction:** "What do lines 7 and 8 print?" stays on screen with a 10-second timer.
- **Narration:** Line 7 prints a list with requests, because 0.875 is at least 0.8.
  **On screen:** Code `examples/ex03_lookalike.py`, line 7 highlighted, output `examples/ex03_lookalike.expected`
- **Narration:** Line 8 prints an empty list. Num py is not like any trusted name.
  **On screen:** Code `examples/ex03_lookalike.py`, line 8 highlighted, output `examples/ex03_lookalike.expected`

## Scene 9: See the outcome: Asha's list check (8:39 to 10:09)

**Section:** See the outcome

**Direction:** Walk the program in two excerpts, ask which lines of the draft are reported, then reveal. Hand over to the AI story.

- **Narration:** Back to the mission. Line 5 is the trusted list, lines 6 and 7 read the draft, and line 8 counts problems.
  **On screen:** Code `examples/ex04_check_requirements.py`, line 5 highlighted, output hidden
- **Narration:** Line 13 takes the name before the two equals signs, in small letters.
  **On screen:** Code `examples/ex04_check_requirements.py`, line 13 highlighted, output hidden
- **Narration:** Lines 14 to 16 report a line with no pin, and count it.
  **On screen:** Code `examples/ex04_check_requirements.py`, line 14, 15, 16 highlighted, output hidden
- **Narration:** Line 17 catches a pinned name that is not on the trusted list.
  **On screen:** Code `examples/ex04_check_requirements.py`, line 17 highlighted, output hidden
- **Narration:** Line 18 finds the closest trusted names. Line 19 takes the first one, with the if else from Chapter 14, in case nothing is close.
  **On screen:** Code `examples/ex04_check_requirements.py`, line 18, 19 highlighted, output hidden
- **Narration:** Lines 20 and 21 report it and count it. Any other line is OK, and line 24 prints the total.
  **On screen:** Code `examples/ex04_check_requirements.py`, line 20, 21, 22, 23, 24 highlighted, output hidden
- **Narration:** Here is the draft again. Use the program's two rules: a line needs a pin, and a pinned name must be trusted.
  **On screen:** Asha's draft, again
- **Interaction:** "Which package lines will the check report as problems?" stays on screen with a 10-second timer.
- **Narration:** Three of the four. Tabulate and pytest are not pinned, and reqeusts is not a trusted name.
  **On screen:** Asha's draft, again
- **Narration:** Asha runs it. Line 3 of the output shows the look-alike: unknown, close to requests.
  **On screen:** Code `examples/ex04_check_requirements.py`, line 20 highlighted, output `examples/ex04_check_requirements.expected`
- **Narration:** Problems found: 3. Mission solved: three problems found. She pins tabulate and pytest, and fixes the spelling of requests, before she installs anything.
  **On screen:** Code `examples/ex04_check_requirements.py`, line 20 highlighted, output `examples/ex04_check_requirements.expected`
- **Narration:** Then she builds her name check into a function, with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex04_check_requirements.py`, output `examples/ex04_check_requirements.expected`

## Scene 10: Work with AI: adding a package safely (10:09 to 15:00)

**Section:** Work with AI

**Direction:** Six stages on adding a package safely with name_check(). Plan misses the name check. Generate's cutoff misses reqeusts. Test fails two cases, then all pass. Debug: the AI says install the look-alike. Improve: sudo is rejected.

- **Narration:** This chapter's AI skill: check every package an AI suggests. It can name a package that does not exist, and attackers can publish exactly those names.
  **On screen:** This chapter's AI skill: check every name
    - An AI can name a package that does not exist, or one with a spelling mistake.
    - Attackers can publish packages with exactly those names.
- **Narration:** So never install a name from a chat before you check it. And never paste keys, passwords or private data.
  **On screen:** This chapter's AI skill: check every name
    - An AI can name a package that does not exist, or one with a spelling mistake.
    - Attackers can publish packages with exactly those names.
    - Never install a name from a chat before you check it.
- **Narration:** Stage 1: plan. Asha asks for the steps to add a package to her project safely. No code yet.
  **On screen:** AI chat, stage 1: Plan: safe steps first
    - You: My weather board needs a package to fetch live weather. Do not write code yet. List the steps to add a package to my project safely.
- **Narration:** Four good steps. But one is missing: check the name and its page on pypi dot org, before installing. Asha adds it as step 2.
  **On screen:** AI chat, stage 1: Plan: safe steps first
    - You: My weather board needs a package to fetch live weather. Do not write code yet. List the steps to add a package to my project safely.
    - AI (example answer): 1. Create and activate a virtual environment. 2. Install requests with python -m pip. 3. Test the board. 4. Record the version with pip freeze in requirements.txt.
- **Narration:** Stage 2: write. Asha writes her own name check first. It only knows exact names.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote this name check myself. Do not rewrite it. What does it return for reqeusts? [code `examples/ai_mine.py`]
- **Narration:** The AI says reqeusts gives unknown. She runs it: right. But her version cannot warn about look-alikes.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote this name check myself. Do not rewrite it. What does it return for reqeusts? [code `examples/ai_mine.py`]
    - AI (example answer): It returns "unknown: check pypi.org". Only exact names in TRUSTED return "trusted".
    - You: I ran it. That is right:
- **Narration:** Stage 3: generate. Asha asks for a version that warns about look-alike names, using diff lib.
  **On screen:** AI chat, stage 3: Generate: warn about look-alikes
    - You: Write a version that also warns when a name looks like a trusted name. Use difflib. What does it return for reqeusts?
- **Narration:** The AI says reqeusts will return: look-alike of requests.
  **On screen:** AI chat, stage 3: Generate: warn about look-alikes
    - You: Write a version that also warns when a name looks like a trusted name. Use difflib. What does it return for reqeusts?
    - AI (example answer): Here it is. For reqeusts, it returns "look-alike of requests".
- **Narration:** Look at line 10. The cutoff is 0.9. Remember the score of reqeusts from step 6.
  **On screen:** Code `examples/ai_check_flawed.py`, line 10 highlighted, output hidden
- **Interaction:** "The AI says line 16 prints `look-alike of requests`. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. Reqeusts scores only 0.875, below the cutoff of 0.9. So line 13 says unknown.
  **On screen:** Code `examples/ai_check_flawed.py`, line 10, 13 highlighted, output `examples/ai_check_flawed.expected`
- **Narration:** Stage 4: test. Asha writes four cases with the exact result she expects, including Requests with a capital R.
  **On screen:** AI chat, stage 4: Test: four cases on the AI's code
    - You: My four cases: requests is trusted. reqeusts is a look-alike of requests. Requests is trusted. numpy is unknown. I will run them on your code.
- **Narration:** The AI says all four will pass.
  **On screen:** AI chat, stage 4: Test: four cases on the AI's code
    - You: My four cases: requests is trusted. reqeusts is a look-alike of requests. Requests is trusted. numpy is unknown. I will run them on your code.
    - AI (example answer): All four will pass.
- **Narration:** Lines 16 to 19 hold the four cases. Line 23 prints pass or fail for each.
  **On screen:** Code `examples/ai_tests_flawed.py`, line 16, 17, 18, 19, 23 highlighted, output hidden
- **Narration:** Remember: PyPI ignores capital letters. Look at line 8.
  **On screen:** Code `examples/ai_tests_flawed.py`, line 8 highlighted, output hidden
- **Interaction:** "Which of the four cases fail?" stays on screen with a 10-second timer.
- **Narration:** Two fail. Reqeusts, because of the cutoff. And Requests, because line 8 compares the exact text, with its capital R.
  **On screen:** Code `examples/ai_tests_flawed.py`, line 8 highlighted, output `examples/ai_tests_flawed.expected`
- **Narration:** Asha shows the AI the two failures, and asks for the cause of each first.
  **On screen:** AI chat, stage 4: Test: the cause, then the fix
    - You: Two cases fail: reqeusts and Requests. Explain the cause of each, then fix them.
- **Narration:** The AI lowers the cutoff to 0.8, and changes the name to small letters before comparing.
  **On screen:** AI chat, stage 4: Test: the cause, then the fix
    - You: Two cases fail: reqeusts and Requests. Explain the cause of each, then fix them.
    - AI (example answer): reqeusts scores 0.875, below my cutoff of 0.9. Use 0.8. Requests has a capital R. Change the name to small letters with lower() first.
- **Narration:** Line 8 lowers the name, and line 11 uses 0.8. She runs all four cases again. All four pass.
  **On screen:** Code `examples/ai_tests_fixed.py`, line 8, 11 highlighted, output `examples/ai_tests_fixed.expected`
- **Narration:** Stage 5: debug. Asha copies an import line from a chat into her weather script. It stops with a module not found error. She asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: My weather script stopped with this error. Explain the cause first. [code `examples/ai_debug_crash.py`]
- **Narration:** The AI says the package is not installed, and gives her the install command for reqeusts.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: My weather script stopped with this error. Explain the cause first. [code `examples/ai_debug_crash.py`]
    - AI (example answer): The package is not installed. Run this command: python -m pip install reqeusts
- **Interaction:** "Should Asha run the command the AI gave her?" stays on screen with a 10-second timer.
- **Narration:** No. Not before she checks the name. It is the same look-alike from her draft.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: My weather script stopped with this error. Explain the cause first. [code `examples/ai_debug_crash.py`]
    - AI (example answer): The package is not installed. Run this command: python -m pip install reqeusts
- **Narration:** She runs her name check. Reqeusts: look-alike of requests.
  **On screen:** Code `examples/ai_debug_check.py`, line 17, 18 highlighted, output `examples/ai_debug_check.expected`
- **Narration:** So the real problem is a spelling mistake in her import line, not a missing package. She fixes it to requests, and installs requests inside her virtual environment.
  **On screen:** Code `examples/ai_debug_check.py`, line 17, 18 highlighted, output `examples/ai_debug_check.expected`
- **Narration:** The look-alike could have run someone else's code on the cafe laptop.
  **On screen:** Code `examples/ai_debug_check.py`, line 17, 18 highlighted, output `examples/ai_debug_check.expected`
- **Narration:** She runs her four cases again on the name check. All four still pass.
  **On screen:** Code `examples/ai_tests_fixed.py`, line 17, 18, 19, 20 highlighted, output `examples/ai_tests_fixed.expected`
- **Narration:** Stage 6: improve. Her setup works. Asha asks for at most two improvements.
  **On screen:** AI chat, stage 6: Improve: one suggestion
    - You: My setup works. Suggest at most two improvements, each with one reason.
- **Narration:** One. Remove spaces with strip, because a name copied from a chat can carry spaces. That is useful.
  **On screen:** AI chat, stage 6: Improve: one suggestion
    - You: My setup works. Suggest at most two improvements, each with one reason.
    - AI (example answer): 1. Remove spaces with strip(). A name copied from a chat can carry spaces. 2. Skip the virtual environment. Install with sudo, and add --break-system-packages if pip refuses.
- **Narration:** Two. Skip the virtual environment, and force the install with break system packages. That forces pip to change the computer's own Python, which other programs need. It breaks this chapter's first rule, so Asha says no.
  **On screen:** AI chat, stage 6: Improve: one suggestion
    - You: My setup works. Suggest at most two improvements, each with one reason.
    - AI (example answer): 1. Remove spaces with strip(). A name copied from a chat can carry spaces. 2. Skip the virtual environment. Install with sudo, and add --break-system-packages if pip refuses.
- **Narration:** She keeps suggestion one. Line 8 now strips spaces, and line 21 adds a fifth case: requests, with spaces around it. She runs every case again. All five pass.
  **On screen:** Code `examples/ai_tests_final.py`, line 8, 21 highlighted, output `examples/ai_tests_final.expected`
- **Narration:** Quick check. An AI says: install this package to fix the error. What do you do first?
  **On screen:** Quick check: "An AI says: install this package to fix the error. What do you do first?" (options shown)
- **Interaction:** "An AI says: install this package to fix the error. What do you do first?" stays on screen with a 10-second timer.
- **Narration:** B. Check the exact name and its page on pypi dot org. Then decide.
  **On screen:** Quick check: "An AI says: install this package to fix the error. What do you do first?" (answer revealed: Check the exact name and its pypi.org page)
- **Narration:** Breather. The AI made four confident mistakes. A score, test cases, her name check and one rule caught them all.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Check every package name an AI gives you.
    - Install only inside `.venv`.
- **Narration:** Next, four mistakes beginners make with environments and packages.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Check every package name an AI gives you.
    - Install only inside `.venv`.
- **Breather:** 4 quiet seconds.

## Scene 11: Common mistakes (15:00 to 16:38)

**Section:** Common mistakes

**Direction:** Mistake 1 calls back to activating. Mistake 2 is a spot-it on the pin. Mistakes 3 and 4 are messages and habits.

- **Narration:** Mistake 1. Asha installs a package in her virtual environment, opens a new terminal, and runs her board. Here, weather tables stands for that package. It stops with a module not found error.
  **On screen:** Code `examples/err01_missing_module.py`, line 2 highlighted, error `examples/err01_missing_module.expected_error`
- **Narration:** Check the prompt first. With no dot v e n v in brackets, the terminal uses the computer's Python, where the package is not installed. Activate, then run again.
  **On screen:** Code `examples/err01_missing_module.py`, line 2 highlighted, error `examples/err01_missing_module.expected_error`
- **Narration:** Mistake 2. Remember the pinned lines from step 5.
  **On screen:** Code `examples/err02_one_equals.py`, line 2 highlighted, output hidden
- **Interaction:** "What is wrong with the pin on line 2?" stays on screen with a 10-second timer.
- **Narration:** It has only one equals sign. So line 3 finds no two equals signs to split at, and gets only one part.
  **On screen:** Code `examples/err02_one_equals.py`, line 2, 3 highlighted, error `examples/err02_one_equals.expected_error`
- **Narration:** Not enough values to unpack means: two names are waiting, but only one value arrived. Write two equals signs. Pip refuses the single one too.
  **On screen:** Code `examples/err02_one_equals.py`, line 2, 3 highlighted, error `examples/err02_one_equals.expected_error`
- **Narration:** Mistake 3. Some systems refuse a plain pip install outside a virtual environment. Do not force it, as the AI suggested. Activate a virtual environment, and install there.
  **On screen:** Mistake 3: installing into the computer's Python
- **Narration:** Mistake 4. A virtual environment holds paths for one computer. Copied to another computer or folder, it may stop working.
  **On screen:** Mistake 4: copying the .venv folder
    - A virtual environment holds paths for one computer.
    - Copied to another computer or folder, it may stop working.
- **Narration:** So never share dot v e n v. Share requirements dot t x t, and build a new environment on each computer.
  **On screen:** Mistake 4: copying the .venv folder
    - A virtual environment holds paths for one computer.
    - Copied to another computer or folder, it may stop working.
    - Share `requirements.txt` instead, and build a new `.venv` on each computer.
- **Narration:** Last breather. Two questions to think about on your own come next.
  **On screen:** Breather card
    - No `(.venv)` in the prompt: activate first.
    - Pins need two equals signs.
    - Share `requirements.txt`, never `.venv`.
- **Breather:** 4 quiet seconds.

## Scene 12: Think beyond (16:38 to 17:24)

**Section:** Think beyond

**Direction:** Two open questions. No answers are given.

- **Narration:** First. A new version of tabulate comes out. How could Asha try it, without breaking the cafe laptop?
  **On screen:** Question card: "A new version of `tabulate` comes out. How could Asha try it without breaking the cafe laptop?"
- **Interaction:** "A new version of `tabulate` comes out. How could Asha try it without breaking the cafe laptop?" stays on screen with a 10-second timer.
- **Narration:** Keep your answer for the practice tasks.
  **On screen:** Question card: "A new version of `tabulate` comes out. How could Asha try it without breaking the cafe laptop?"
- **Narration:** Second. An AI suggests a package called cafe weather easy. Which checks would you make on its page, and which result would make you stop?
  **On screen:** Question card: "An AI suggests `cafe-weather-easy`. Which checks would you make, and which result would make you stop?"
- **Interaction:** "An AI suggests `cafe-weather-easy`. Which checks would you make, and which result would make you stop?" stays on screen with a 10-second timer.
- **Narration:** Write your list down. You will use it every time you add a package.
  **On screen:** Question card: "An AI suggests `cafe-weather-easy`. Which checks would you make, and which result would make you stop?"

## Scene 13: Recap (17:24 to 18:20)

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** A virtual environment is a project folder with its own Python and packages.
  **On screen:** Recap
    - A virtual environment is a project folder, `.venv`, with its own Python and packages.
- **Narration:** Look for dot v e n v in the prompt, then install with python dash m pip.
  **On screen:** Recap
    - A virtual environment is a project folder, `.venv`, with its own Python and packages.
    - Look for `(.venv)` in the prompt before you install anything.
    - `python -m pip install` adds a package. `pip list` shows what is installed.
- **Narration:** Requirements dot t x t pins exact versions for every computer.
  **On screen:** Recap
    - A virtual environment is a project folder, `.venv`, with its own Python and packages.
    - Look for `(.venv)` in the prompt before you install anything.
    - `python -m pip install` adds a package. `pip list` shows what is installed.
    - `requirements.txt` pins versions with `==`. `pip install -r` installs the same versions.
- **Narration:** And check every name before you install it, especially a name from an AI.
  **On screen:** Recap
    - A virtual environment is a project folder, `.venv`, with its own Python and packages.
    - Look for `(.venv)` in the prompt before you install anything.
    - `python -m pip install` adds a package. `pip list` shows what is installed.
    - `requirements.txt` pins versions with `==`. `pip install -r` installs the same versions.
    - Check every name on pypi.org. A look-alike name is a warning sign.
    - Never install a name from an AI before you check it.
- **Narration:** One last check. Which command records the exact versions in the active environment, in a file?
  **On screen:** Quick check: "Which command records the exact versions in the active environment?" (options shown)
- **Interaction:** "Which command records the exact versions in the active environment?" stays on screen with a 10-second timer.
- **Narration:** A. Pip freeze prints pinned lines, and the greater than sign saves them in requirements dot t x t. Pip list only shows them.
  **On screen:** Quick check: "Which command records the exact versions in the active environment?" (answer revealed: `python -m pip freeze > requirements.txt`)
- **Narration:** Mission complete! You earned 100 XP and the Toolsmith badge.
  **On screen:** Toolsmith You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 14: Practice (18:20 to 18:39)

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. Eight tasks, worth 170 XP. None of them installs anything.
  **On screen:** Table: Practice: 8 tasks, 170 XP
- **Narration:** Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each. In the last one, you fix an AI's pin checker.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 15: What's next (18:39 to 19:06)

**Section:** What's next

**Direction:** End card. Tease the boss level as the place to use files, errors and JSON together. Hold quietly at the end.

- **Narration:** Asha's quiz scores sit in a CSV file, her weather board saves JSON, and her loaders handle bad rows. But her day's numbers are still scattered across files.
  **On screen:** Boss Level 5: The Data Report Generator Files, errors and JSON, in one tool.
- **Narration:** In Chapter 25, Boss Level 5, you will build the Data Report Generator: a tool that reads a data file, handles bad rows, and writes one clear report.
  **On screen:** Boss Level 5: The Data Report Generator Files, errors and JSON, in one tool.
- **Narration:** Do the warm-up tasks now.
  **On screen:** Boss Level 5: The Data Report Generator Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you at the boss level.
  **On screen:** Boss Level 5: The Data Report Generator Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
