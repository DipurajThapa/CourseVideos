# Video Script: Chapter 23: JSON and APIs: Talking to Other Programs

Generated from `storyboard.json` by `tools/render_video.py --script`. Do not edit by hand: change the storyboard and render again.

Format: interactive full chapter walkthrough, 1920x1080, 30 fps, narrated. Length: 18:04 (estimate, not rendered yet).

## Scene 1: Introduction

**Section:** Introduction

**Direction:** Open on the Chapter 22 limit: the quiz is data inside data, and a CSV row is flat. Title and AI tease, then the mission code with no output.

- **Narration:** At the Corner Cafe, Asha's quiz has a title, a pass mark, and questions with their own answers. That is data inside data, and a CSV row cannot hold it.
  **On screen:** Data inside data
- **Narration:** This is Code Quest, Chapter 23. Today, your programs talk to other programs.
  **On screen:** JSON and APIs: Talking to Other Programs
- **Narration:** And an AI assistant will read a supplier's price list, and promise you a number. Your tests will decide.
  **On screen:** JSON and APIs: Talking to Other Programs Read it. Check it. Save it.
- **Narration:** Here is today's mission. The daily board reads a weather response, and picks the drink of the day.
  **On screen:** Code `examples/ex08_daily_board.py`, line 11, 12, 13 highlighted, output hidden
- **Narration:** Then it saves the board as JSON, for the screen behind the counter. Let's build it, piece by piece.
  **On screen:** Code `examples/ex08_daily_board.py`, line 19, 20 highlighted, output hidden

## Scene 2: Learning goals

**Section:** Learning goals

**Direction:** Each goal appears as it is spoken.

- **Narration:** Turn data into JSON text and back, and save it in files.
  **On screen:** By the end, you will be able to:
    - Turn Python data into JSON text and back.
    - Save and load JSON files, keeping accents.
- **Narration:** Explain how a web service answers, and read the values you need.
  **On screen:** By the end, you will be able to:
    - Turn Python data into JSON text and back.
    - Save and load JSON files, keeping accents.
    - Explain how a web API answers a request.
    - Read nested values from a saved API response.
- **Narration:** And ask an AI to explain a response, then check its code.
  **On screen:** By the end, you will be able to:
    - Turn Python data into JSON text and back.
    - Save and load JSON files, keeping accents.
    - Explain how a web API answers a request.
    - Read nested values from a saved API response.
    - Ask an AI to explain a JSON response, then check its code.

## Scene 3: Why this matters

**Section:** Why this matters

**Direction:** Define JSON and why programs share it.

- **Narration:** JSON, short for JavaScript Object Notation, is a text format for structured data: dictionaries, lists, text and numbers, inside each other.
  **On screen:** Why this matters
    - **JSON** is a text format for structured data.
- **Narration:** Almost every language can read it. So weather, payment and delivery services all send their answers as JSON.
  **On screen:** Why this matters
    - **JSON** is a text format for structured data.
    - Almost every programming language can read it.
    - Weather, payment and delivery services all answer in JSON.

## Scene 4: The idea: JSON text and Python data

**Section:** The idea

**Direction:** Teach the type table, the two directions, the API conversation and the analogy. Quiz on null. Breather.

- **Narration:** JSON looks almost like a Python dictionary, but it is text. A JSON object becomes a dictionary.
  **On screen:** Table: JSON and Python (row 1 in focus)
- **Narration:** An array becomes a list.
  **On screen:** Table: JSON and Python (row 2 in focus)
- **Narration:** A string becomes a string. JSON allows only double quotation marks.
  **On screen:** Table: JSON and Python (row 3 in focus)
- **Narration:** True and false are written in small letters. And null is JSON's word for nothing.
  **On screen:** Table: JSON and Python (row 6 in focus)
- **Narration:** The json module translates in both directions. Dump s turns Python data into JSON text. Load s turns the text back into data.
  **On screen:** Two directions
- **Narration:** Read the S as string. Without the S, dump and load work with a file instead.
  **On screen:** Two directions
- **Narration:** A web API is a service that other programs can ask for data. Your program sends a request to a web address.
  **On screen:** How a web API answers
- **Narration:** The service sends back a response. The status code says how it went: 200 means OK, and 404 means not found.
  **On screen:** How a web API answers
- **Narration:** The body holds the data, usually as JSON. Many services also want an API key: a secret password for programs. Keep it out of your code, and out of AI chats.
  **On screen:** How a web API answers
- **Narration:** Quick check. What does JSON null become in Python?
  **On screen:** Quick check: "What does JSON `null` become in Python?" (options shown)
- **Interaction:** "What does JSON `null` become in Python?" stays on screen with a 10-second timer.
- **Narration:** D. None. Null and None both mean: nothing here.
  **On screen:** Quick check: "What does JSON `null` become in Python?" (answer revealed: `None`)
- **Narration:** Breather. You know what JSON is, and how a service answers.
  **On screen:** Breather card
    - JSON is text for structured data.
    - `dumps` makes text. `loads` makes data.
    - An API answers with a status code and a body.
- **Narration:** Next, Asha turns her first dictionary into JSON.
  **On screen:** Breather card
    - JSON is text for structured data.
    - `dumps` makes text. `loads` makes data.
    - An API answers with a status code and a body.
- **Breather:** 4 quiet seconds.

## Scene 5: Step 1: Data to JSON text

**Section:** Build it step by step

**Direction:** Teach dumps on the menu item. Ask what line 6 prints for True and None. Reveal.

- **Narration:** Step 1. Lines 4 and 5 hold a Python dictionary for one menu item. It holds a string, a float, True, and None.
  **On screen:** Code `examples/ex01_dumps.py`, line 4, 5 highlighted, output hidden
- **Narration:** Line 6 turns it into JSON text with dump s. Line 7 prints it, and line 8 prints its type.
  **On screen:** Code `examples/ex01_dumps.py`, line 6, 7, 8 highlighted, output hidden
- **Interaction:** "How does line 7 write `True` and `None`?" stays on screen with a 10-second timer.
- **Narration:** True becomes true, in small letters. And None becomes null. Exactly as the table said.
  **On screen:** Code `examples/ex01_dumps.py`, line 7 highlighted, output `examples/ex01_dumps.expected`
- **Narration:** And the result is a string. Now Asha can save it in a file, or send it to another program.
  **On screen:** Code `examples/ex01_dumps.py`, line 8 highlighted, output `examples/ex01_dumps.expected`

## Scene 6: Step 2: JSON text to data

**Section:** Build it step by step

**Direction:** Show the scone file. Teach read_text then loads. Ask what line 8 prints. Reveal, then is None.

- **Narration:** Step 2. Here is a saved file, scone dot json. Look at the sizes: an array of two strings.
  **On screen:** A saved JSON file
- **Narration:** Lines 5 and 6 read the file. Read text gives a string. Line 7 turns that string into data, with load s.
  **On screen:** Code `examples/ex02_loads.py`, line 5, 6, 7 highlighted, output hidden
- **Narration:** Line 8 prints both types. Line 9 picks one size from the list.
  **On screen:** Code `examples/ex02_loads.py`, line 8, 9 highlighted, output hidden
- **Interaction:** "What does line 9 print?" stays on screen with a 10-second timer.
- **Narration:** Large. The text became a dictionary, so sizes is a list, and index 1 is its second item.
  **On screen:** Code `examples/ex02_loads.py`, line 9 highlighted, output `examples/ex02_loads.expected`
- **Narration:** Line 10 shows false and null as Python's False and None.
  **On screen:** Code `examples/ex02_loads.py`, line 10 highlighted, output `examples/ex02_loads.expected`
- **Narration:** To check for None, write is None, as line 11 does. Python's style guide, pep eight, recommends is for None.
  **On screen:** Code `examples/ex02_loads.py`, line 11 highlighted, output `examples/ex02_loads.expected`

## Scene 7: Step 3: Readable JSON

**Section:** Build it step by step

**Direction:** Teach the default escape codes and the two settings. Ask what line 5 prints for the accent. Reveal.

- **Narration:** Step 3. Line 4 holds a drink with an accent: Café au lait.
  **On screen:** Code `examples/ex03_pretty.py`, line 4 highlighted, output hidden
- **Narration:** By default, dump s writes every character outside basic English as a code. So the e with an accent becomes backslash u, 0 0 e 9.
  **On screen:** Code `examples/ex03_pretty.py`, line 5 highlighted, output hidden
- **Narration:** Ensure ascii equals False turns that off. Indent equals 2 puts each value on its own line.
  **On screen:** Code `examples/ex03_pretty.py`, line 6, 7 highlighted, output hidden
- **Interaction:** "How does line 5 write the word `Café`?" stays on screen with a 10-second timer.
- **Narration:** As a code: C a f, then backslash u 0 0 e 9. The data is still correct, but hard for people to read.
  **On screen:** Code `examples/ex03_pretty.py`, line 5 highlighted, output `examples/ex03_pretty.expected`
- **Narration:** Line 6 keeps the real letter. Line 7 also indents, two spaces for each level.
  **On screen:** Code `examples/ex03_pretty.py`, line 6, 7 highlighted, output `examples/ex03_pretty.expected`

## Scene 8: Step 4: Save and load a file

**Section:** Build it step by step

**Direction:** Asha saves her quiz with dump and loads it with load. Ask what line 17 prints. Reveal. Breather.

- **Narration:** Step 4. Here is Asha's quiz: a title, a pass mark, and a list of questions, each a dictionary.
  **On screen:** Code `examples/ex04_save_load.py`, line 4, 5, 6, 7, 8, 9 highlighted, output hidden
- **Narration:** Line 12 uses dump, without the S. It writes straight into the open file.
  **On screen:** Code `examples/ex04_save_load.py`, line 11, 12 highlighted, output hidden
- **Narration:** Line 15 uses load, without the S. It reads the data back from the file.
  **On screen:** Code `examples/ex04_save_load.py`, line 14, 15 highlighted, output hidden
- **Narration:** Line 20 compares the loaded data with the original.
  **On screen:** Code `examples/ex04_save_load.py`, line 20 highlighted, output hidden
- **Interaction:** "What does line 20 print?" stays on screen with a 10-second timer.
- **Narration:** True. The loaded quiz is equal to the original, so nothing was lost.
  **On screen:** Code `examples/ex04_save_load.py`, line 20 highlighted, output `examples/ex04_save_load.expected`
- **Narration:** Line 19 reaches inside: the second question, then its ask.
  **On screen:** Code `examples/ex04_save_load.py`, line 19 highlighted, output `examples/ex04_save_load.expected`
- **Narration:** Breather. Asha's quiz now lives in a file, data inside data. Next, the weather service.
  **On screen:** Breather card
    - `dumps` and `loads` work with strings.
    - `dump` and `load` work with files.
    - `ensure_ascii=False` keeps accents.
- **Breather:** 4 quiet seconds.

## Scene 9: Step 5: A saved API response

**Section:** Build it step by step

**Direction:** Show the illustrative live call, then why programmers save a sample. Show the sample. Ask what line 7 prints. Reveal.

- **Narration:** Step 5. On your own computer, a program can ask a real service for data. The url lib module, from the standard library, sends the request.
  **On screen:** Step 5: Asking a real service
- **Narration:** This address is a placeholder. Live answers change every minute, so programmers save one real response as a file, called a sample response, and test on it.
  **On screen:** Step 5: Asking a real service
- **Narration:** Here is Asha's sample. Location and current are objects. Forecast is a list of three objects.
  **On screen:** Asha's sample response
- **Narration:** Lines 5 and 6 read the file, and turn it into data.
  **On screen:** Code `examples/ex05_weather.py`, line 5, 6 highlighted, output hidden
- **Narration:** Follow the path from the outside in. Line 7 opens location, then name. Line 8 opens current, then temp C, the number inside it.
  **On screen:** Code `examples/ex05_weather.py`, line 7, 8 highlighted, output hidden
- **Interaction:** "What does line 8 print?" stays on screen with a 10-second timer.
- **Narration:** Riverside 31.5. The name from location, and the temperature from current.
  **On screen:** Code `examples/ex05_weather.py`, line 8 highlighted, output `examples/ex05_weather.expected`
- **Narration:** Forecast is a list, so lines 10 and 11 loop over it. Each slot is a dictionary.
  **On screen:** Code `examples/ex05_weather.py`, line 10, 11 highlighted, output `examples/ex05_weather.expected`

## Scene 10: Step 6: Missing fields and bad text

**Section:** Build it step by step

**Direction:** get() with a default, then a KeyError. Then JSONDecodeError with try. Quiz. Breather.

- **Narration:** Step 6. A service can leave a field out. Get, from Chapter 12, returns a default instead of crashing.
  **On screen:** Code `examples/ex06_safe_get.py`, line 8 highlighted, output hidden
- **Narration:** The sample has no wind field. Line 9 asks for it with get. Line 10 asks with square brackets.
  **On screen:** Code `examples/ex06_safe_get.py`, line 9, 10 highlighted, output hidden
- **Interaction:** "What does line 9 print?" stays on screen with a 10-second timer.
- **Narration:** Not sent: the default. Get never crashes.
  **On screen:** Code `examples/ex06_safe_get.py`, line 9 highlighted, error `examples/ex06_safe_get.expected_error`
- **Narration:** Line 10 stops with a key error. Use square brackets for fields the service always sends, and get for fields that may be missing.
  **On screen:** Code `examples/ex06_safe_get.py`, line 10 highlighted, error `examples/ex06_safe_get.expected_error`
- **Narration:** Text that is not valid JSON raises a JSON decode error. Line 4 holds three texts. Look at the quotation marks.
  **On screen:** Code `examples/ex07_bad_json.py`, line 4 highlighted, output hidden
- **Narration:** Lines 6 to 9 catch the error with try, as in Chapter 22. Error dot msg holds the short reason.
  **On screen:** Code `examples/ex07_bad_json.py`, line 6, 7, 8, 9 highlighted, output hidden
- **Interaction:** "Which of the three texts loads?" stays on screen with a 10-second timer.
- **Narration:** Only the first. JSON allows only double quotation marks, so the second fails.
  **On screen:** Code `examples/ex07_bad_json.py`, line 4 highlighted, output `examples/ex07_bad_json.expected`
- **Narration:** The third is empty. That happens when a service sends no body: expecting value.
  **On screen:** Code `examples/ex07_bad_json.py`, line 4 highlighted, output `examples/ex07_bad_json.expected`
- **Narration:** Quick check. Which function writes JSON straight into an open file?
  **On screen:** Quick check: "Which function writes JSON straight into an open file?" (options shown)
- **Interaction:** "Which function writes JSON straight into an open file?" stays on screen with a 10-second timer.
- **Narration:** A. Dump, without the S. Dump s returns a string instead.
  **On screen:** Quick check: "Which function writes JSON straight into an open file?" (answer revealed: `json.dump()`)
- **Narration:** Breather. You can read a service's answer, and survive a missing field. Now, back to the mission.
  **On screen:** Breather card
    - Save a sample response, and test on it.
    - Follow the path from the outside in.
    - `get()` for fields that may be missing.
- **Breather:** 4 quiet seconds.

## Scene 11: See the outcome: the daily board

**Section:** See the outcome

**Direction:** Walk the daily board in groups. Ask which hours land in rain_hours. Reveal. Hand over to the AI story.

- **Narration:** Back to the mission. Lines 6 to 8 are a small function: open a file, and load its JSON.
  **On screen:** Code `examples/ex08_daily_board.py`, line 6, 7, 8 highlighted, output hidden
- **Narration:** Line 12 follows the path to the temperature. Line 13 picks iced tea at 30 degrees or more.
  **On screen:** Code `examples/ex08_daily_board.py`, line 11, 12, 13 highlighted, output hidden
- **Narration:** Lines 14 and 15 keep the hour of every slot with a rain chance of 30 or more.
  **On screen:** Code `examples/ex08_daily_board.py`, line 14, 15 highlighted, output hidden
- **Narration:** Lines 16 and 17 build the board. Lines 19 to 21 save it as JSON, with an accent, and print the file.
  **On screen:** Code `examples/ex08_daily_board.py`, line 16, 17, 19, 20, 21 highlighted, output hidden
- **Narration:** Remember the sample's forecast: three slots, each with its own rain chance.
  **On screen:** Code `examples/ex08_daily_board.py`, line 14, 15 highlighted, output hidden
- **Interaction:** "Which hours end up in `rain_hours`?" stays on screen with a 10-second timer.
- **Narration:** Only 18:00. Its rain chance is 40. The other two slots have 0 and 10.
  **On screen:** Code `examples/ex08_daily_board.py`, line 14, 15 highlighted, output `examples/ex08_daily_board.expected`
- **Narration:** It reads JSON, picks what it needs, and writes new JSON for the cafe's screen.
  **On screen:** Code `examples/ex08_daily_board.py`, line 16, 17 highlighted, output `examples/ex08_daily_board.expected`
- **Narration:** Next, Asha reads her milk supplier's prices, with an AI assistant, one stage at a time.
  **On screen:** Code `examples/ex08_daily_board.py`, output `examples/ex08_daily_board.expected`

## Scene 12: Work with AI: reading a supplier's prices

**Section:** Work with AI

**Direction:** Safety first. Six stages on price_of. Generate treats a list as a dictionary. Test catches text prices. Debug handles null. Improve invents a field.

- **Narration:** This chapter's AI skill: paste a sample response, ask the AI to explain it, then check every field name against the real sample.
  **On screen:** This chapter's AI skill: explain a response
    - Paste a sample response, and ask for its structure.
    - Check every field name and path against the real sample.
- **Narration:** And never paste an API key, or private customer data.
  **On screen:** This chapter's AI skill: explain a response
    - Paste a sample response, and ask for its structure.
    - Check every field name and path against the real sample.
    - Never paste an API key or private customer data.
- **Narration:** Here is the supplier's saved response, prices dot json. Look closely at each price.
  **On screen:** The supplier's saved response
- **Narration:** Stage 1: plan. Asha pastes the sample, and asks for its structure, level by level. No code yet.
  **On screen:** AI chat, stage 1: Plan: explain the structure
    - You: Here is a saved response from my milk supplier's price service. Do not write code yet. Describe its structure, level by level. Which values are text, and which are numbers?
- **Narration:** The AI says items is a list, and every price is text in quotation marks. Asha checks the sample: both are true.
  **On screen:** AI chat, stage 1: Plan: explain the structure
    - You: Here is a saved response from my milk supplier's price service. Do not write code yet. Describe its structure, level by level. Which values are text, and which are numbers?
    - AI (example answer): The response is an object with supplier, currency and items. items is a list. Each entry is an object with name, price and unit. Every price is text in quotation marks, such as "1.20", not a number.
- **Narration:** Stage 2: write. Asha writes her own price of first. It loops over the list, and converts the text with float.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote price_of myself. Do not rewrite it. What does it return for milk, and which line handles an item that is missing? [code `examples/ai_mine.py`]
- **Narration:** The AI says milk gives 1.2, and line 10 handles a missing item.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote price_of myself. Do not rewrite it. What does it return for milk, and which line handles an item that is missing? [code `examples/ai_mine.py`]
    - AI (example answer): For milk it returns 1.2, a float, because line 9 converts the text. Line 10 returns None when no name matches.
- **Narration:** She runs it. Milk gives 1.2, and flour gives None. Her version works.
  **On screen:** AI chat, stage 2: Write it yourself, then check
    - You: I wrote price_of myself. Do not rewrite it. What does it return for milk, and which line handles an item that is missing? [code `examples/ai_mine.py`]
    - AI (example answer): For milk it returns 1.2, a float, because line 9 converts the text. Line 10 returns None when no name matches.
    - You: I ran it for milk and for flour:
- **Narration:** Stage 3: generate. To compare, Asha asks the AI for the same function, and what it returns for milk.
  **On screen:** AI chat, stage 3: Generate: a second version
    - You: Write price_of(data, name) for this response. It returns the price of the named item as a number. What does it return for milk?
- **Narration:** The AI writes one line, and says: milk gives 1.2.
  **On screen:** AI chat, stage 3: Generate: a second version
    - You: Write price_of(data, name) for this response. It returns the price of the named item as a number. What does it return for milk?
    - AI (example answer): Here it is. For milk, it returns 1.2. [code `examples/ai_price_flawed.py`]
- **Narration:** Look at line 7. It asks items for milk, by name. Remember what items is in the sample.
  **On screen:** Code `examples/ai_price_flawed.py`, line 7 highlighted, output hidden
- **Interaction:** "The AI says this returns `1.2` for milk. Is it right?" stays on screen with a 10-second timer.
- **Narration:** No. A type error. Items is a list, and a list needs a number as its index, not the name milk.
  **On screen:** Code `examples/ai_price_flawed.py`, line 7 highlighted, error `examples/ai_price_flawed.expected_error`
- **Narration:** That is what list indices must be integers means. The AI treated the list as a dictionary of names.
  **On screen:** Code `examples/ai_price_flawed.py`, line 7 highlighted, error `examples/ai_price_flawed.expected_error`
- **Narration:** Stage 4: test. Asha reports the error, and asks for test cases with exact values.
  **On screen:** AI chat, stage 4: Test: exact values
    - You: Your code stopped with a TypeError: list indices must be integers. Fix it. Then give me test cases with the exact value I should get.
- **Narration:** The AI's next version loops over the list. And it lists three cases: milk, oat milk, and flour.
  **On screen:** AI chat, stage 4: Test: exact values
    - You: Your code stopped with a TypeError: list indices must be integers. Fix it. Then give me test cases with the exact value I should get.
    - AI (example answer): Here is a version that loops over the list. Cases: milk gives 1.2, oat milk gives 1.85, and flour gives None. [code `examples/ai_tests_flawed.py`]
- **Narration:** Line 9 returns the price. Line 20 prints each result with exclamation r, so text shows its quotation marks.
  **On screen:** Code `examples/ai_tests_flawed.py`, line 9, 20 highlighted, output hidden
- **Interaction:** "Will the milk case pass?" stays on screen with a 10-second timer.
- **Narration:** No. It got 1.20 in quotation marks: text, not a number. Text is never equal to the float 1.2.
  **On screen:** Code `examples/ai_tests_flawed.py`, line 9 highlighted, output `examples/ai_tests_flawed.expected`
- **Narration:** Only flour passes. Plan said every price is text, and the AI forgot its own words.
  **On screen:** Code `examples/ai_tests_flawed.py`, line 9 highlighted, output `examples/ai_tests_flawed.expected`
- **Narration:** Asha shows the AI the failing cases, and asks why.
  **On screen:** AI chat, stage 4: Test: report the failure
    - You: Two cases fail: you return '1.20' as text. Explain why, then fix it.
- **Narration:** The supplier sends prices as strings, so line 9 must convert them with float.
  **On screen:** AI chat, stage 4: Test: report the failure
    - You: Two cases fail: you return '1.20' as text. Explain why, then fix it.
    - AI (example answer): This supplier sends every price as a string. Line 9 returns it unchanged. Fix: return float(item["price"]).
- **Narration:** She runs all three cases again. All pass.
  **On screen:** Code `examples/ai_tests_fixed.py`, line 9 highlighted, output `examples/ai_tests_fixed.expected`
- **Narration:** Stage 5: debug. The next day, oat milk is out of stock, and the supplier sends null as its price. Milk still works. Oat milk crashes on line 9.
  **On screen:** Code `examples/ai_today_crash.py`, line 13, 17 highlighted, error `examples/ai_today_crash.expected_error`
- **Narration:** Asha pastes the error, and asks for the cause first.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: Today's response has null as the oat milk price. My code crashed on line 9 with: TypeError: float() argument must be a string or a real number, not 'NoneType'. Explain the cause first. Then show the smallest fix.
- **Narration:** JSON null became None, and float of None is a type error. The fix checks for it with is None, from step 2.
  **On screen:** AI chat, stage 5: Debug: the cause before the fix
    - You: Today's response has null as the oat milk price. My code crashed on line 9 with: TypeError: float() argument must be a string or a real number, not 'NoneType'. Explain the cause first. Then show the smallest fix.
    - AI (example answer): JSON null becomes None in Python, and float(None) raises a TypeError. Fix: before line 9, check for it: if item["price"] is None: return None.
- **Narration:** Lines 9 and 10 are the fix. She adds the new response as case 4, on line 19, and runs every case again. All four pass.
  **On screen:** Code `examples/ai_tests_final.py`, line 9, 10, 19 highlighted, output `examples/ai_tests_final.expected`
- **Narration:** Stage 6: improve. Asha asks for one improvement, using only field names from her sample.
  **On screen:** AI chat, stage 6: Improve: one suggestion
    - You: All four cases pass. Suggest one improvement, with one reason. Use only field names that are in my sample.
- **Narration:** The AI suggests unit price, and calls it the standard field.
  **On screen:** AI chat, stage 6: Improve: one suggestion
    - You: All four cases pass. Suggest one improvement, with one reason. Use only field names that are in my sample.
    - AI (example answer): Read item["unit_price"] instead of item["price"]. It is the standard field for the price of one unit, so the code is clearer.
- **Narration:** Asha's rule: every field name must appear in the sample. Lines 9 and 11 read unit price.
  **On screen:** Code `examples/ai_unit_price.py`, line 9, 11 highlighted, output hidden
- **Interaction:** "Will this run on Asha's sample?" stays on screen with a 10-second timer.
- **Narration:** No. A key error. The sample has price and unit, but no unit price. The AI invented the field.
  **On screen:** Code `examples/ai_unit_price.py`, line 9 highlighted, error `examples/ai_unit_price.expected_error`
- **Narration:** So Asha keeps her final function. Its four cases still pass, as you saw.
  **On screen:** Code `examples/ai_unit_price.py`, line 9 highlighted, error `examples/ai_unit_price.expected_error`
- **Narration:** Quick check. An AI's code uses a field name. How do you check it?
  **On screen:** Quick check: "An AI's code uses a field name. How do you check it?" (options shown)
- **Interaction:** "An AI's code uses a field name. How do you check it?" stays on screen with a 10-second timer.
- **Narration:** B. Search the real sample for it. Only the sample shows what the service sends.
  **On screen:** Quick check: "An AI's code uses a field name. How do you check it?" (answer revealed: Search the real sample for it)
- **Narration:** Breather. The AI made three confident mistakes, and the sample and the tests caught every one.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Test the exact value and its type.
    - Every field name must be in the sample.
- **Narration:** Next, four mistakes beginners make with JSON.
  **On screen:** Breather card
    - Plan, write, generate, test, debug, improve.
    - Test the exact value and its type.
    - Every field name must be in the sample.
- **Breather:** 4 quiet seconds.

## Scene 13: Common mistakes

**Section:** Common mistakes

**Direction:** Mistakes 1 and 3 are spot-it asks. Mistakes 2 and 4 are explained.

- **Narration:** Mistake 1. You try. Line 4 holds some JSON text. Line 5 loads it.
  **On screen:** Code `examples/err01_single_quotes.py`, line 4 highlighted, output hidden
- **Interaction:** "Why will line 5 fail?" stays on screen with a 10-second timer.
- **Narration:** The text uses single quotation marks. Python accepts both kinds, but JSON accepts only double ones.
  **On screen:** Code `examples/err01_single_quotes.py`, line 4 highlighted, error `examples/err01_single_quotes.expected_error`
- **Narration:** The report runs through the json module's own files. Read the last line: column 2 is the first single quotation mark.
  **On screen:** Code `examples/err01_single_quotes.py`, line 4 highlighted, error `examples/err01_single_quotes.expected_error`
- **Narration:** Mistake 2. Dump writes into a file, so it needs one: F P is the file parameter. To get a string, use dump s.
  **On screen:** Code `examples/err02_dump_no_file.py`, line 5 highlighted, error `examples/err02_dump_no_file.expected_error`
- **Narration:** Mistake 3. Lines 4 and 5 read scone dot json. Line 6 asks for the item.
  **On screen:** Code `examples/err03_text_not_dict.py`, line 5, 6 highlighted, output hidden
- **Interaction:** "Will line 6 work?" stays on screen with a 10-second timer.
- **Narration:** No. Read text gives a string, not a dictionary. A string accepts only number indexes.
  **On screen:** Code `examples/err03_text_not_dict.py`, line 5, 6 highlighted, error `examples/err03_text_not_dict.expected_error`
- **Narration:** The fix: turn the text into data first, with load s.
  **On screen:** Code `examples/err03_text_not_dict.py`, line 5, 6 highlighted, error `examples/err03_text_not_dict.expected_error`
- **Narration:** Mistake 4. JSON object keys are always strings. The table numbers 1 and 2 came back as the text 1 and 2.
  **On screen:** Code `examples/err04_keys_strings.py`, line 4, 5 highlighted, error `examples/err04_keys_strings.expected_error`
- **Narration:** So back, 1 is a key error. Use string keys from the start.
  **On screen:** Code `examples/err04_keys_strings.py`, line 7 highlighted, error `examples/err04_keys_strings.expected_error`

## Scene 14: Think beyond

**Section:** Think beyond

**Direction:** Two open questions. No answers are given.

- **Narration:** First. Some weather services send the temperature in Fahrenheit for some cities. How could your code know which unit a response uses?
  **On screen:** Question card: "Some weather services send Fahrenheit for some cities. How could your code know which unit a response uses?"
- **Interaction:** "Some weather services send Fahrenheit for some cities. How could your code know which unit a response uses?" stays on screen with a 10-second timer.
- **Narration:** Look for a field in the sample that names the unit.
  **On screen:** Question card: "Some weather services send Fahrenheit for some cities. How could your code know which unit a response uses?"
- **Narration:** Second. Why test your code on a saved sample, instead of the live service?
  **On screen:** Question card: "Why test your code on a saved sample, instead of the live service?"
- **Interaction:** "Why test your code on a saved sample, instead of the live service?" stays on screen with a 10-second timer.
- **Narration:** Keep your answer. You will use it in the next boss level.
  **On screen:** Question card: "Why test your code on a saved sample, instead of the live service?"

## Scene 15: Recap

**Section:** Recap

**Direction:** Each recap point appears as it is spoken, a quiz, then the badge.

- **Narration:** Let's recap. Dump s makes JSON text, and load s turns it back into data.
  **On screen:** Recap
    - `json.dumps()` makes JSON text. `json.loads()` turns it back into data.
- **Narration:** Dump and load work with an open file.
  **On screen:** Recap
    - `json.dumps()` makes JSON text. `json.loads()` turns it back into data.
    - `json.dump()` and `json.load()` work with an open file.
- **Narration:** True, false and null become True, False and None.
  **On screen:** Recap
    - `json.dumps()` makes JSON text. `json.loads()` turns it back into data.
    - `json.dump()` and `json.load()` work with an open file.
    - `true`, `false` and `null` become `True`, `False` and `None`.
- **Narration:** An API answers with a status code, and a JSON body.
  **On screen:** Recap
    - `json.dumps()` makes JSON text. `json.loads()` turns it back into data.
    - `json.dump()` and `json.load()` work with an open file.
    - `true`, `false` and `null` become `True`, `False` and `None`.
    - An API answers with a status code and a JSON body.
- **Narration:** Follow the path from the outside in, and use get for missing fields.
  **On screen:** Recap
    - `json.dumps()` makes JSON text. `json.loads()` turns it back into data.
    - `json.dump()` and `json.load()` work with an open file.
    - `true`, `false` and `null` become `True`, `False` and `None`.
    - An API answers with a status code and a JSON body.
    - Follow the path from the outside in. Use `get()` for missing fields.
- **Narration:** And check every field name an AI uses against the real sample.
  **On screen:** Recap
    - `json.dumps()` makes JSON text. `json.loads()` turns it back into data.
    - `json.dump()` and `json.load()` work with an open file.
    - `true`, `false` and `null` become `True`, `False` and `None`.
    - An API answers with a status code and a JSON body.
    - Follow the path from the outside in. Use `get()` for missing fields.
    - Check every field name an AI uses against the real sample.
- **Narration:** One last check. A response says price, 1.20, in quotation marks. What type is it after load s?
  **On screen:** Quick check: "A response says `"price": "1.20"`. What type is the price after `json.loads()`?" (options shown)
- **Interaction:** "A response says `"price": "1.20"`. What type is the price after `json.loads()`?" stays on screen with a 10-second timer.
- **Narration:** C. A string. The quotation marks decide. Convert it with float before you calculate.
  **On screen:** Quick check: "A response says `"price": "1.20"`. What type is the price after `json.loads()`?" (answer revealed: `str`)
- **Narration:** Mission complete! You earned 100 XP and the Connector badge.
  **On screen:** Connector You earned 100 XP.
- **Breather:** 2 quiet seconds.

## Scene 16: Practice

**Section:** Practice

**Direction:** Each tier is highlighted as it is described.

- **Narration:** Now it is your turn. Three warm-up tasks, worth 10 XP each.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 1 in focus)
- **Narration:** Three apply tasks, worth 20 each, including a JSON loader that never crashes.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 2 in focus)
- **Narration:** And two stretch tasks, worth 40 each, including an AI's temperature reader to fix.
  **On screen:** Table: Practice: 8 tasks, 170 XP (row 3 in focus)

## Scene 17: What's next

**Section:** What's next

**Direction:** End card. Tease packages and virtual environments. Hold quietly.

- **Narration:** Many programmers call web services with a package called requests. It is not part of Python, so it must be installed.
  **On screen:** Virtual Environments and Packages Install packages safely, in their own space.
- **Narration:** In Chapter 24, you will create a virtual environment, and install packages safely, after checking that each one is real and trustworthy.
  **On screen:** Virtual Environments and Packages Install packages safely, in their own space.
- **Narration:** Do the warm-up tasks now. They take about ten minutes.
  **On screen:** Virtual Environments and Packages Do the warm-up tasks now. They take about ten minutes.
- **Narration:** See you in Chapter 24.
  **On screen:** Virtual Environments and Packages Do the warm-up tasks now. They take about ten minutes.
- **Breather:** 2 quiet seconds.
