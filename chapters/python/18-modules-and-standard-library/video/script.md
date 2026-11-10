# Video Script: Chapter 18: Modules and the Standard Library

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 17:59 (estimate, not rendered yet).

## Scene 1: Introduction

**Section:** Introduction

**Direction:** Open on three programs with three copies of with_tax, in Asha's words. Then the title with the AI tease, then the day report as the mission, with no output yet.

- **Narration:** At the Corner Cafe, Asha now has three programs. And each one has its own copy of with tax.
  **On screen:** Three programs, three copies
- **Narration:** Chapter 17 ended with exactly this problem. If she finds a bug in with tax, she must fix it three times. Miss one copy, and two programs disagree.
  **On screen:** Three programs, three copies
- **Narration:** This is Code Quest, Chapter 18: write your tools once, and import them everywhere.
  **On screen:** Modules and the Standard Library
- **Narration:** And an AI assistant will recommend a ready-made function, and name the page where it lives. You will check that page yourself.
  **On screen:** Modules and the Standard Library Write it once. Import it everywhere.
- **Narration:** Here is today's mission: Asha's day report. It has no copy of with tax. Lines 2 to 5 import it, together with three of Python's own modules.
  **On screen:** Code `examples/ex07_day_report.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** Lines 13 to 16 print a total, a biscuit order, a closing time and a file name. Let's build it.
  **On screen:** Code `examples/ex07_day_report.py`, line 13, 14, 15, 16 highlighted, output hidden

## Scene 2: Learning goals

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Your goals: import modules in three ways, write your own module, use three standard modules, check an AI's suggestion in the documentation, and fix import errors.
  **On screen:** By the end, you will be able to:
    - Import a module in three ways.
    - Write your own module and protect its test lines with the main guard.
    - Use `math`, `datetime` and `pathlib` to round up, add times and read file names.
    - Check an AI's suggested function in the official documentation, then run it.
    - Fix the errors beginners meet with imports.

## Scene 3: Why this matters

**Section:** Why this matters

**Direction:** Define module and standard library through Asha's problem, with the Chapter 10 callback.

- **Narration:** A module is a Python file whose functions other programs can use. Write with tax once, fix it once, and every program gets the fix.
  **On screen:** Why this matters
    - A **module** is a Python file whose functions other programs can use.
    - Write `with_tax()` once. Fix it once. Every program gets the fix.
- **Narration:** Python also comes with a large set of modules, already written and tested. It is called the standard library. You met one in Chapter 10: random.
  **On screen:** Why this matters
    - A **module** is a Python file whose functions other programs can use.
    - Write `with_tax()` once. Fix it once. Every program gets the fix.
    - The **standard library** is the set of modules that comes with Python. You met `random` in Chapter 10.

## Scene 4: The idea: importing

**Section:** The idea

**Direction:** Teach importing with the diagram, then the three import forms, then the toolbox analogy and where it stops working. Then a quiz and a breather.

- **Narration:** Importing makes a module's functions available in your program. Python finds the module file, runs it once, and gives you a name for it.
  **On screen:** One file, many programs
- **Narration:** There are three common ways to import. Import math keeps the module name in front: math dot ceil.
  **On screen:** Table: Three ways to import (row 1 in focus)
- **Narration:** From math import ceil brings only that one function in, so you call it on its own.
  **On screen:** Table: Three ways to import (row 2 in focus)
- **Narration:** And import math as m gives the module a short name. A short name like this is called an alias.
  **On screen:** Table: Three ways to import (row 3 in focus)
- **Narration:** Think of a module as a toolbox on a shelf. Import takes the whole box to your table.
  **On screen:** A module is like a toolbox
    - `import` takes the whole toolbox to your table.
- **Narration:** You still say which tool you want, as in math dot ceil.
  **On screen:** A module is like a toolbox
    - `import` takes the whole toolbox to your table.
    - You still name the tool you want: `math.ceil`.
- **Narration:** Where the comparison stops working: Python runs the whole module file when it imports it. So a print at the bottom of that file runs too.
  **On screen:** A module is like a toolbox
    - `import` takes the whole toolbox to your table.
    - You still name the tool you want: `math.ceil`.
    - Where it stops working: Python runs the whole module file when it imports it.
- **Narration:** Quick check. After from math import ceil, which call works?
  **On screen:** Quick check: "After `from math import ceil`, which call works?" (options shown)
- **Interaction:** "After `from math import ceil`, which call works?" stays on screen with a 10-second timer.
- **Narration:** C. Ceil on its own. From import brings in only that one function, not the name math.
  **On screen:** Quick check: "After `from math import ceil`, which call works?" (answer revealed: `ceil(2.1)`)
- **Narration:** Take a breather. Next, Asha imports her first standard module.
  **On screen:** Breather card
    - A module is a Python file you can import.
    - Three ways: import, from import, import as.
    - Importing runs the whole file once.
- **Breather:** 4 quiet seconds.

## Scene 5: Steps 1 and 2: Import a standard module

**Section:** Build it step by step

**Direction:** Teach ceil and floor, ask what lines 7 and 8 print. Then the three import forms side by side.

- **Narration:** Step 1. Asha orders biscuits in boxes of 12, and she needs 40. Line 2 imports the math module.
  **On screen:** Code `examples/ex01_import_math.py`, line 2, 4, 5 highlighted, output hidden
- **Narration:** Line 6 divides. Line 7 uses math dot ceil, which rounds up to the next whole number. Line 8 uses math dot floor, which rounds down.
  **On screen:** Code `examples/ex01_import_math.py`, line 6, 7, 8 highlighted, output hidden
- **Interaction:** "What do lines 7 and 8 print?" stays on screen with a 10-second timer.
- **Narration:** 4 and 3. 40 divided by 12 is 3.33, so ceil rounds up to 4 boxes, and floor rounds down to 3.
  **On screen:** Code `examples/ex01_import_math.py`, line 7, 8 highlighted, output `examples/ex01_import_math.expected`
- **Narration:** Line 9 prints the square root of 49: 7.0. The dot means: the function that lives in the math module.
  **On screen:** Code `examples/ex01_import_math.py`, line 9 highlighted, output `examples/ex01_import_math.expected`
- **Narration:** Step 2. Lines 2 to 4 import in the three ways from the table. Lines 6 to 8 call the same function in those three ways.
  **On screen:** Code `examples/ex02_import_forms.py`, line 2, 3, 4, 6, 7, 8 highlighted, output hidden
- **Narration:** All three print 3. In your own programs, pick one style, so readers are not confused.
  **On screen:** Code `examples/ex02_import_forms.py`, line 2, 3, 4, 6, 7, 8 highlighted, output `examples/ex02_import_forms.expected`

## Scene 6: Step 3: Your own module

**Section:** Build it step by step

**Direction:** Teach the module file and the main guard, run the module itself, then ask what an importing program prints. Then from-import, a quiz and a breather.

- **Narration:** Step 3. Asha moves her tools into their own file, cafe tools dot p y. The name of a module is its file name without dot p y.
  **On screen:** Code `examples/cafe_tools.py`, line 2 highlighted, output hidden
- **Narration:** It holds with tax and money, each with a docstring.
  **On screen:** Code `examples/cafe_tools.py`, line 4, 5, 6, 8, 9, 10 highlighted, output hidden
- **Narration:** Lines 12 to 15 are test lines, under a special if. Python gives every file a hidden variable called name, with two underscores on each side.
  **On screen:** Code `examples/cafe_tools.py`, line 12, 13, 14, 15 highlighted, output hidden
- **Narration:** When you run the file itself, that variable holds the text main. When another program imports the file, it holds the module's name instead.
  **On screen:** Code `examples/cafe_tools.py`, line 12 highlighted, output hidden
- **Narration:** Asha runs the module itself, so the test lines run: two times True.
  **On screen:** Code `examples/cafe_tools.py`, line 13, 14, 15 highlighted, output `examples/cafe_tools.expected`
- **Narration:** Now a second program, in the same folder, imports the module on line 2.
  **On screen:** Code `examples/ex03_use_tools.py`, line 2 highlighted, output hidden
- **Narration:** Line 4 calls cafe tools dot with tax, with 4.0. Line 6 shows the result with money.
  **On screen:** Code `examples/ex03_use_tools.py`, line 4, 5, 6 highlighted, output hidden
- **Interaction:** "What does this program print? Do the module's test lines appear?" stays on screen with a 10-second timer.
- **Narration:** 4.4, then 4.40. And no test lines. The module was imported, so its name was not main, and the if skipped them.
  **On screen:** Code `examples/ex03_use_tools.py`, line 5, 6 highlighted, output `examples/ex03_use_tools.expected`
- **Narration:** A third program uses from import, so it calls with tax and money on their own.
  **On screen:** Code `examples/ex04_from_tools.py`, line 2 highlighted, output `examples/ex04_from_tools.expected`
- **Narration:** The loop prints three prices with tax: 3.85, 4.40 and 3.03. One copy of with tax, used by two programs.
  **On screen:** Code `examples/ex04_from_tools.py`, line 4, 5 highlighted, output `examples/ex04_from_tools.expected`
- **Narration:** Python looks for cafe tools in the folder of the program you run. So keep your module next to the programs that import it.
  **On screen:** Code `examples/ex04_from_tools.py`, line 4, 5 highlighted, output `examples/ex04_from_tools.expected`
- **Narration:** Quick check. When do the lines under the main guard run?
  **On screen:** Quick check: "When do the lines under `if __name__ == "__main__":` run?" (options shown)
- **Interaction:** "When do the lines under `if __name__ == "__main__":` run?" stays on screen with a 10-second timer.
- **Narration:** B. Only when you run that file itself. When it is imported, the guard skips them.
  **On screen:** Quick check: "When do the lines under `if __name__ == "__main__":` run?" (answer revealed: Only when you run that file itself)
- **Narration:** Breather. Relax your shoulders. Next, two more standard modules: one for time, and one for file names.
  **On screen:** Breather card
    - A module's name is its file name without `.py`.
    - Keep the module next to its programs.
    - The main guard hides test lines on import.
- **Breather:** 4 quiet seconds.

## Scene 7: Steps 4 and 5: Times and file names

**Section:** Build it step by step

**Direction:** Teach timedelta, ask what line 7 prints. Teach Path parts, ask what lines 6 and 7 print. Then a quiz.

- **Narration:** Step 4. The datetime module works with time. A time delta is a length of time. Line 2 imports it.
  **On screen:** Code `examples/ex05_hours.py`, line 2 highlighted, output hidden
- **Narration:** Line 4: the cafe opens 8 hours after midnight. Line 5: it stays open for 9 hours and 30 minutes. Line 6 adds the two lengths.
  **On screen:** Code `examples/ex05_hours.py`, line 4, 5, 6 highlighted, output hidden
- **Interaction:** "What does line 7 print?" stays on screen with a 10-second timer.
- **Narration:** Closes at 17:30:00. Python carries the minutes into hours for you.
  **On screen:** Code `examples/ex05_hours.py`, line 7 highlighted, output `examples/ex05_hours.expected`
- **Narration:** Line 8: total seconds gives the length in seconds. Divided by 60, that is 570.0 minutes.
  **On screen:** Code `examples/ex05_hours.py`, line 8 highlighted, output `examples/ex05_hours.expected`
- **Narration:** Step 5. Pathlib builds file names, without touching any file. A path is the address of a file: its folders and its name.
  **On screen:** Code `examples/ex06_paths.py`, line 2 highlighted, output hidden
- **Narration:** Line 4 joins a folder and a file name. Here, the forward slash joins the parts. It does not divide.
  **On screen:** Code `examples/ex06_paths.py`, line 4 highlighted, output hidden
- **Narration:** Name is the whole file name. Stem is the name without its ending. Suffix is the ending.
  **On screen:** Code `examples/ex06_paths.py`, line 5, 6, 7 highlighted, output hidden
- **Interaction:** "What do lines 6 and 7 print?" stays on screen with a 10-second timer.
- **Narration:** Monday, then dot t x t. Line 5 printed the whole name, monday dot t x t.
  **On screen:** Code `examples/ex06_paths.py`, line 6, 7 highlighted, output `examples/ex06_paths.expected`
- **Narration:** Windows writes paths with backslashes. So line 8, as posix, shows the path with forward slashes on every system.
  **On screen:** Code `examples/ex06_paths.py`, line 8 highlighted, output `examples/ex06_paths.expected`
- **Narration:** Quick check. A path joins menus and winter dot t x t. What is its suffix?
  **On screen:** Quick check: "`Path("menus") / "winter.txt"`. What is its `suffix`?" (options shown)
- **Interaction:** "`Path("menus") / "winter.txt"`. What is its `suffix`?" stays on screen with a 10-second timer.
- **Narration:** D. Dot t x t. The suffix is the ending. Winter would be the stem.
  **On screen:** Quick check: "`Path("menus") / "winter.txt"`. What is its `suffix`?" (answer revealed: `.txt`)

## Scene 8: See the outcome: the day report

**Section:** See the outcome

**Direction:** Return to the mission. Walk the imports and lines 7 to 11, ask what line 13 prints, reveal, then hand over to the AI feature.

- **Narration:** Back to the mission. Lines 2 to 5 put every import at the top, as the style guide asks: three standard modules, then Asha's own.
  **On screen:** Code `examples/ex07_day_report.py`, line 2, 3, 4, 5 highlighted, output hidden
- **Narration:** Line 8 adds tax to each sale with with tax, in a comprehension from Chapter 14, and sum adds the results.
  **On screen:** Code `examples/ex07_day_report.py`, line 7, 8 highlighted, output hidden
- **Narration:** Line 9 rounds up the biscuit boxes, line 10 adds the opening hours, and line 11 builds the report's file name. It does not save a file yet.
  **On screen:** Code `examples/ex07_day_report.py`, line 9, 10, 11 highlighted, output hidden
- **Interaction:** "What does line 13 print?" stays on screen with a 10-second timer.
- **Narration:** Total: 11.28. That is 3.85, plus 4.40, plus 3.03: the three prices from step 3.
  **On screen:** Code `examples/ex07_day_report.py`, line 13 highlighted, output `examples/ex07_day_report.expected`
- **Narration:** Then 4 boxes, closing at 17:30, and the file name. No copy of with tax anywhere. Mission complete!
  **On screen:** Code `examples/ex07_day_report.py`, line 14, 15, 16 highlighted, output `examples/ex07_day_report.expected`
- **Narration:** Now Asha wants one more tool for her module: how many boxes to order. She builds it with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex07_day_report.py`, output `examples/ex07_day_report.expected`

## Scene 9: Work with AI: six stages, one function

**Section:** Work with AI

**Direction:** Teach the skill. One conversation per stage, all about boxes_needed. Write: her own version and the AI's false claim. Generate: round. Test: two FAIL. Debug: missing import. Improve: an invented function.

- **Narration:** This chapter's AI skill: ask an AI which standard module fits a task.
  **On screen:** This chapter's AI skill: check the documentation
    - Ask AI which standard module and function fit a task.
- **Narration:** Then find that function in the official documentation, at docs dot python dot org, and run it on your own test cases.
  **On screen:** This chapter's AI skill: check the documentation
    - Ask AI which standard module and function fit a task.
    - Find that function in the official documentation at docs.python.org.
    - Run it on your own test cases. Never paste private data.
- **Narration:** Stage 1: plan. Asha describes the task: boxes of 12, always round up. She asks for the exact module and function, and says she will check them.
  **On screen:** AI chat, stage 1: Plan: find the right module
    - You: I order biscuits in boxes of 12, and I always round up. Which standard module and function do this? Give the exact names and one example. I will check the official documentation.
- **Narration:** The AI names the math module and math dot ceil, with an example.
  **On screen:** AI chat, stage 1: Plan: find the right module
    - You: I order biscuits in boxes of 12, and I always round up. Which standard module and function do this? Give the exact names and one example. I will check the official documentation.
    - AI (example answer): The `math` module. `math.ceil(x)` returns the smallest whole number that is greater than or equal to x. For example, `math.ceil(3.2)` is `4`.
- **Narration:** Asha opens the math page of the official documentation and finds ceil, with the same meaning.
  **On screen:** AI chat, stage 1: Plan: find the right module
    - You: I order biscuits in boxes of 12, and I always round up. Which standard module and function do this? Give the exact names and one example. I will check the official documentation.
    - AI (example answer): The `math` module. `math.ceil(x)` returns the smallest whole number that is greater than or equal to x. For example, `math.ceil(3.2)` is `4`.
    - You: I found `ceil` on the `math` page of docs.python.org. Its description matches yours.
- **Narration:** Stage 2: write. Before using the module, Asha writes her own version: double slash, then plus 1. For 40 biscuits, it gives 4.
  **On screen:** AI chat, stage 2: Write: her own version first
    - You: First I wrote my own version, without any module. Do not change it. Does it give the same result as a `math.ceil` version for every number of biscuits? [code `examples/ai_own_boxes.py`]
- **Narration:** She asks the AI whether her version always matches a ceil version. The AI says yes, always.
  **On screen:** AI chat, stage 2: Write: her own version first
    - You: First I wrote my own version, without any module. Do not change it. Does it give the same result as a `math.ceil` version for every number of biscuits? [code `examples/ai_own_boxes.py`]
    - AI (example answer): Yes. Both versions always give the same number of boxes.
- **Narration:** Asha tests two numbers: 40, and 24, which divides exactly. Line 5 is her version. Line 6 uses ceil.
  **On screen:** Code `examples/ai_compare_boxes.py`, line 4, 5, 6, 7 highlighted, output hidden
- **Interaction:** "The AI says both versions always match. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. For 24 biscuits, her version orders 3 boxes, and ceil orders 2. Her version adds a box even when nothing is left over.
  **On screen:** Code `examples/ai_compare_boxes.py`, line 5 highlighted, output `examples/ai_compare_boxes.expected`
- **Narration:** The AI missed her bug. A number that divides exactly found it.
  **On screen:** Code `examples/ai_compare_boxes.py`, line 5 highlighted, output `examples/ai_compare_boxes.expected`
- **Narration:** Stage 3: generate. Asha asks for boxes needed, with a docstring, and asks exactly what it returns for 40 biscuits.
  **On screen:** AI chat, stage 3: Generate: a function for the module
    - You: Write `boxes_needed(biscuits, per_box=12)` for my module. It must round up. Add a docstring, and tell me exactly what `boxes_needed(40)` returns.
- **Narration:** The AI writes the function, and says it returns 4.
  **On screen:** AI chat, stage 3: Generate: a function for the module
    - You: Write `boxes_needed(biscuits, per_box=12)` for my module. It must round up. Add a docstring, and tell me exactly what `boxes_needed(40)` returns.
    - AI (example answer): Here it is. `boxes_needed(40)` returns `4`. [code `examples/ai_boxes_flawed.py`]
- **Narration:** Here is the AI's function. Line 4 divides, then calls round, from Chapter 2. Line 6 asks for 40 biscuits.
  **On screen:** Code `examples/ai_boxes_flawed.py`, line 4, 6 highlighted, output hidden
- **Interaction:** "The AI says `boxes_needed(40)` returns 4. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. It prints 3. Round goes to the nearest whole number, so 3.33 becomes 3. Asha would be 4 biscuits short.
  **On screen:** Code `examples/ai_boxes_flawed.py`, line 4 highlighted, output `examples/ai_boxes_flawed.expected`
- **Narration:** Stage 4: test. Asha writes four cases with the result she expects: a remainder, an exact division, one biscuit, and zero. She asks the AI if any case is missing.
  **On screen:** AI chat, stage 4: Test: cases with expected results
    - You: Your version gives 3 for 40 biscuits. Here are my test cases: 40 gives 4, 24 gives 2, 1 gives 1, 0 gives 0. Is any case missing?
- **Narration:** The AI says the set is good, and tells her to run it on every version.
  **On screen:** AI chat, stage 4: Test: cases with expected results
    - You: Your version gives 3 for 40 biscuits. Here are my test cases: 40 gives 4, 24 gives 2, 1 gives 1, 0 gives 0. Is any case missing?
    - AI (example answer): Your cases cover a remainder, an exact division, one biscuit and zero. That is a good set. Run them on every version.
- **Narration:** Line 5 holds the cases, in a dictionary: biscuits, and the expected boxes. The loop prints pass or FAIL for each one.
  **On screen:** Code `examples/ai_boxes_tests_flawed.py`, line 5, 6, 7, 8, 9 highlighted, output `examples/ai_boxes_tests_flawed.expected`
- **Narration:** On the AI's version, 40 and 1 fail. Round never rounds 1 twelfth up to a whole box.
  **On screen:** Code `examples/ai_boxes_tests_flawed.py`, line 3 highlighted, output `examples/ai_boxes_tests_flawed.expected`
- **Narration:** Stage 5: debug. Asha changes round to math dot ceil, runs it, and Python stops. She pastes the code and the full error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: I changed it to `math.ceil` and got this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_boxes_noimport.py`]
- **Narration:** The AI names line 4: the file uses math, but never imports it. The error even asks: did you forget to import math? The fix: add import math at the top.
  **On screen:** AI chat, stage 5: Debug: the AI's answer
    - You: I changed it to `math.ceil` and got this error. First explain the cause and the line. Then show the smallest fix. [code `examples/ai_boxes_noimport.py`]
    - AI (example answer): It is a `NameError` on line 4. The file uses `math`, but it never imports it. The fix: add `import math` as the first line of the file.
- **Narration:** Line 2 imports math, and line 5 uses ceil. Asha runs every case again.
  **On screen:** Code `examples/ai_boxes_tests_fixed.py`, line 2, 5 highlighted, output `examples/ai_boxes_tests_fixed.expected`
- **Narration:** All four pass, including the exact division and zero.
  **On screen:** Code `examples/ai_boxes_tests_fixed.py`, line 7, 8, 9, 10, 11 highlighted, output `examples/ai_boxes_tests_fixed.expected`
- **Narration:** Stage 6: improve. Asha asks for one improvement, and for the documentation page of any function it uses.
  **On screen:** AI chat, stage 6: Improve: one suggestion
    - You: My function passes every case. Suggest one improvement, with one reason. Name the documentation page for any function you use.
- **Narration:** The AI suggests math dot ceil div. It divides and rounds up in one step, and the AI says it is on the math page.
  **On screen:** AI chat, stage 6: Improve: one suggestion
    - You: My function passes every case. Suggest one improvement, with one reason. Name the documentation page for any function you use.
    - AI (example answer): Use `math.ceildiv(biscuits, per_box)`. It divides and rounds up in one step, so the code is shorter. You will find it on the `math` module page.
- **Narration:** Asha searches the math page for ceil div, and does not find it. To be sure, she runs one line.
  **On screen:** Code `examples/ai_ceildiv.py`, line 2, 4 highlighted, output hidden
- **Interaction:** "Will line 4 run?" stays on screen with a 10-second timer.
- **Narration:** No. Attribute Error: module math has no attribute ceil div. Here, attribute means a name inside the module. That function does not exist.
  **On screen:** Code `examples/ai_ceildiv.py`, line 4 highlighted, error `examples/ai_ceildiv.expected_error`
- **Narration:** The AI made it up, and named a real page for it. Asha keeps math dot ceil. Her four cases still pass.
  **On screen:** Code `examples/ai_ceildiv.py`, line 4 highlighted, error `examples/ai_ceildiv.expected_error`
- **Narration:** Quick check. An AI names a function you have never seen. What do you do first?
  **On screen:** Quick check: "An AI names a function you have never seen. What do you do first?" (options shown)
- **Interaction:** "An AI names a function you have never seen. What do you do first?" stays on screen with a 10-second timer.
- **Narration:** A. Find it in the official documentation, then run it.
  **On screen:** Quick check: "An AI names a function you have never seen. What do you do first?" (answer revealed: Find it in the official documentation, then run it)
- **Narration:** Breather. Asha caught three AI problems: a false promise about her own code, round instead of ceil, and a function that does not exist.
  **On screen:** Breather card
    - Find every function in the documentation.
    - Test a number that divides exactly.
    - Run every case after every fix.
- **Breather:** 4 quiet seconds.

## Scene 10: Common mistakes

**Section:** Common mistakes

**Direction:** Mistake 1 is a spot-it question on a module name. Mistake 2 calls back to the quiz. Mistake 3 shows a file named random.py. Mistake 4 is a predict question on a module without the guard.

- **Narration:** Now you try. Line 2 imports Asha's module. Compare it with step 3.
  **On screen:** Code `examples/err01_module_typo.py`, line 2 highlighted, output hidden
- **Interaction:** "Why will line 2 fail?" stays on screen with a 10-second timer.
- **Narration:** The name is cafe tool, without the s. Python looks for a file with exactly that name, finds none, and stops with a Module Not Found Error.
  **On screen:** Code `examples/err01_module_typo.py`, line 2 highlighted, error `examples/err01_module_typo.expected_error`
- **Narration:** Newer versions of Python even suggest the right name. The fix: spell it like the file.
  **On screen:** Code `examples/err01_module_typo.py`, line 2 highlighted, error `examples/err01_module_typo.expected_error`
- **Narration:** Mistake 2 is the quick check from the idea section, in reverse. After import math, the full name is math dot ceil. Ceil on its own is not defined.
  **On screen:** Code `examples/err02_no_prefix.py`, line 2, 4 highlighted, error `examples/err02_no_prefix.expected_error`
- **Narration:** The fix: write math dot ceil, or import it with from math import ceil.
  **On screen:** Code `examples/err02_no_prefix.py`, line 2, 4 highlighted, error `examples/err02_no_prefix.expected_error`
- **Narration:** Mistake 3. Asha saved a test file called random dot p y, next to this program. Now import random finds her file first, not Python's module.
  **On screen:** Code `examples/shadow/err03_shadow.py`, line 2 highlighted, error `examples/shadow/err03_shadow.expected_error`
- **Narration:** The first output line comes from her test file. Then her file has no rand int, so Python stops with an Attribute Error.
  **On screen:** Code `examples/shadow/err03_shadow.py`, line 4 highlighted, error `examples/shadow/err03_shadow.expected_error`
- **Narration:** Python 3.13 and newer add advice: consider renaming the file. The fix: rename it, for example to random test dot p y.
  **On screen:** Code `examples/shadow/err03_shadow.py`, line 4 highlighted, error `examples/shadow/err03_shadow.expected_error`
- **Narration:** Mistake 4. This module has a test line at the bottom, line 5, with no main guard. Run on its own, it prints its test line.
  **On screen:** Code `examples/noguard/menu_tools.py`, line 5 highlighted, output `examples/noguard/menu_tools.expected`
- **Narration:** Another program imports money from that module, and prints the tea price.
  **On screen:** Code `examples/noguard/ex08_no_guard.py`, line 2, 4 highlighted, output hidden
- **Interaction:** "What does this program print?" stays on screen with a 10-second timer.
- **Narration:** Two lines: the module's test line, then the tea. Importing runs the whole file, so the test line appears in every program that imports it.
  **On screen:** Code `examples/noguard/ex08_no_guard.py`, line 2, 4 highlighted, output `examples/noguard/ex08_no_guard.expected`
- **Narration:** There is no error, which makes it easy to miss. The fix: put test lines under the main guard.
  **On screen:** Code `examples/noguard/ex08_no_guard.py`, line 2, 4 highlighted, output `examples/noguard/ex08_no_guard.expected`
- **Narration:** Breather. Two questions to think about come next.
  **On screen:** Breather card
    - Spell the module like its file.
    - Never name a file like a standard module.
    - Test lines go under the main guard.
- **Breather:** 4 quiet seconds.

## Scene 11: Think beyond

**Section:** Think beyond

**Direction:** Two open questions that apply what was taught. No answers are given.

- **Narration:** First. Asha wants to pick a random winner from a list of customer names. Which function of the random module fits?
  **On screen:** Question card: "Asha wants to pick a random winner from a list of customer names. Which function of the `random` module fits?"
- **Interaction:** "Asha wants to pick a random winner from a list of customer names. Which function of the `random` module fits?" stays on screen with a 10-second timer.
- **Narration:** Ask an AI, then find the function in the official documentation, and run it.
  **On screen:** Question card: "Asha wants to pick a random winner from a list of customer names. Which function of the `random` module fits?"
- **Narration:** Second. Two folders of programs both need cafe tools. Asha copies it into both folders, then fixes a bug in one copy. What happens?
  **On screen:** Question card: "Two folders of programs both need `cafe_tools.py`. Asha copies it into both, then fixes a bug in one copy. What happens?"
- **Interaction:** "Two folders of programs both need `cafe_tools.py`. Asha copies it into both, then fixes a bug in one copy. What happens?" stays on screen with a 10-second timer.
- **Narration:** Think back to the three copies at the start of this chapter.
  **On screen:** Question card: "Two folders of programs both need `cafe_tools.py`. Asha copies it into both, then fixes a bug in one copy. What happens?"

## Scene 12: Recap

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, then a final quick check, then the badge.

- **Narration:** Let's recap. A module is a Python file whose functions other programs can import, and the standard library is the set of modules that comes with Python.
  **On screen:** Recap
    - A module is a Python file whose functions other programs can import.
    - The standard library is the set of modules that comes with Python.
- **Narration:** There are three ways to import. Importing runs the whole file once, and the main guard keeps test lines quiet.
  **On screen:** Recap
    - A module is a Python file whose functions other programs can import.
    - The standard library is the set of modules that comes with Python.
    - `import math`, `from math import ceil` and `import math as m` all work.
    - Importing runs the whole file once. The main guard keeps test lines quiet.
- **Narration:** Ceil rounds up, time delta adds times, and Path reads file names. And when an AI names a function, find it in the documentation, then run it.
  **On screen:** Recap
    - A module is a Python file whose functions other programs can import.
    - The standard library is the set of modules that comes with Python.
    - `import math`, `from math import ceil` and `import math as m` all work.
    - Importing runs the whole file once. The main guard keeps test lines quiet.
    - `math.ceil()` rounds up, `timedelta` adds times, `Path` reads file names.
    - Find every function an AI names in the documentation, then run it.
- **Narration:** One last check. After import math as m, which call works?
  **On screen:** Quick check: "After `import math as m`, which call works?" (options shown)
- **Interaction:** "After `import math as m`, which call works?" stays on screen with a 10-second timer.
- **Narration:** C. M dot square root. The alias m is the only name that import creates.
  **On screen:** Quick check: "After `import math as m`, which call works?" (answer revealed: `m.sqrt(16)`)
- **Narration:** Mission complete! You earned 100 XP and the Librarian badge.
  **On screen:** Librarian You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 13: Practice

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn: eight tasks, worth 170 XP. Three warm-up tasks at 10 XP, and three apply tasks at 20, including your own price module.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks at 40, including an AI's cake planner that calls a function the math module does not have. Try each one before you open the solution.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 14: What's next

**Section:** What's next

**Direction:** End card. Tease Chapter 19: the module's True checks become real tests. Hold quietly at the end.

- **Narration:** Asha's module checks itself with lines that print True. But if one prints False, nothing stops her, and she might not notice.
  **On screen:** Testing Your Code: assert and pytest Checks that stop you when something breaks.
- **Narration:** In Chapter 19, you will turn these checks into real tests, with assert and pytest.
  **On screen:** Testing Your Code: assert and pytest Checks that stop you when something breaks.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Testing Your Code: assert and pytest Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 19.
  **On screen:** Testing Your Code: assert and pytest Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
