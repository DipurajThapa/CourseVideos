# AI Prompt Cards: Chapter 21

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste passwords, keys or private data, and that includes files of real customer names or scores: paste a small made-up sample instead. Always run the code yourself on a copy of your data, and look at the file afterwards.

## Plan: Choose the file, the mode and the format

**Prompt:** "I am a beginner learning Python files. My program needs to save <describe the data, for example: a name and a quiz score after every round> so the next run can load it. Do not write code yet. List the steps: which file name, which format (plain text or CSV), which mode for saving and which for loading, and what to do when the file does not exist yet."

**Use it when:** you know what data must survive, but not how to store it.

**A good answer:** a short list with one file, a clear format with a header for CSV, mode `"a"` for adding, a read step for loading and a check for a missing file.

**Check it:** ask yourself what happens on the first run, the second run and the tenth run. If any run would lose old data, the plan is wrong.

## Write: Write your own save function first

**Prompt:** "Here is the function I wrote myself to save <the data>: <paste it>. Do not rewrite it. Explain in plain words what happens to the file on the first call and on the second call. Name one risk, if there is one."

**Use it when:** you have written a file function and want to check your understanding.

**A good answer:** a description of the file after each call, which mode is used, and a specific risk such as a missing encoding or a header written twice.

**Check it:** run your function twice on a test file and read the file. Compare it, line by line, with the AI's description.

## Generate: Ask for a file function with exact rules

**Prompt:** "Write a Python function save_<name>(path, <values>) that adds one row to a CSV file. Use the csv module, open the file with mode 'a', newline='' and encoding='utf-8', and write the header <header> only when the file is new. Take the file name as a parameter. Then show exactly what the file contains after two calls."

**Use it when:** you want a safe file function quickly.

**A good answer:** a short function that uses every rule you listed, plus the exact file text after two calls.

**Check it:** run it on a new file, call it twice, and read the file. If the first row is missing, the function emptied the file with mode `"w"`.

## Debug: Explain a file error before fixing it

**Prompt:** "I am a beginner. I ran this code: <paste the code>. I got this full error report: <paste it>. First explain what the error means and which line causes it. Then show the smallest fix. Do not rewrite the rest of my code."

**Use it when:** you see `FileNotFoundError`, `UnicodeDecodeError` or a `TypeError` from CSV values.

**A good answer:** the error type, the exact file name or byte it names, the cause (a wrong name, a missing folder, the wrong encoding, text used as a number) and a one-line fix.

**Check it:** apply the fix and run the program again. Then run every earlier test case again too.

## Test: Check the file after every case

**Prompt:** "Here is my function: <paste it>. Suggest test cases for it: a new file, two saves to the same file, and a file that already has data. For each case, give the exact text the file should contain afterwards."

**Use it when:** your function works once and you want to know if it keeps working.

**A good answer:** three or more cases, each with the exact expected file text, including the header and the newline at the end of each line.

**Check it:** run each case on its own file name and compare the file's text with the expected text. A case that loses a row is a FAIL, even when there is no error.

## Improve: One suggestion, then every test again

**Prompt:** "My file function passes all my test cases: <paste the function>. Suggest at most one improvement, with one reason. Do not change what the file contains."

**Use it when:** your function works and you want it simpler or safer.

**A good answer:** one specific change and a reason you can check, such as a clearer name or a parameter for the file name.

**Check it:** make the change, then run every test case again. If any case fails, the suggestion changed what the file contains, so do not keep it.
