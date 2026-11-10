# AI Prompt Cards: Chapter 24

Use these with an AI assistant such as ChatGPT or Claude. Replace the parts in angle brackets. Never paste API keys, passwords or private data. Never install a package name from an AI answer before you check it on pypi.org, and run every install command inside your virtual environment.

## Plan: Ask for safe steps first

**Prompt:** "I am a beginner. My Python project is <describe it>. I want to add a package that <what it should do>. Do not write code yet. List the steps to add a package to my project safely, from creating a virtual environment to recording the version I installed."

**Use it when:** you are about to add your first package to a project.

**A good answer:** create and activate a virtual environment, check the package on pypi.org, install it with `python -m pip`, test it, and record it with `pip freeze` in `requirements.txt`.

**Check it:** the steps must include checking the name on pypi.org before installing. If that step is missing, add it yourself. Every install command should start with `python -m pip`, and none should use `sudo` or `--break-system-packages`.

## Write: Write your own check first

**Prompt:** "I wrote this function myself: <paste it>. Do not rewrite it. What does it return for <a misspelled package name>, and why?"

**Use it when:** you have written your own code and want to test your understanding of it.

**A good answer:** the exact text your function returns for that name, with a reason that points at a line of your code.

**Check it:** run your function with the same name and compare the real result with the AI's answer.

## Generate: Ask for code that does one more job

**Prompt:** "Here is my function: <paste it>. Write a version that also warns when a name looks like one of my trusted names, using the standard module difflib. Tell me exactly what it returns for <a look-alike name>."

**Use it when:** you want a second version to compare with your own.

**A good answer:** short code that uses only the standard library, with the exact result for the name you gave.

**Check it:** run it with the same name. If the code uses a `cutoff`, work out the similarity score of your name with `difflib.SequenceMatcher` and check that it reaches the cutoff.

## Test: Your own cases on the AI's code

**Prompt:** "Here is the function an AI wrote: <paste it>. My test cases are: <paste names and expected results>. Two of them fail: <paste the output>. Explain the cause of each failure before you change any code."

**Use it when:** you have cases with exact expected results and want to know why some fail.

**A good answer:** one cause for each failing case, such as a cutoff that is too high or a name with capital letters, then the smallest fix.

**Check it:** run every case again on the fixed code, including the cases that passed before.

## Debug: The cause, and a check of every name

**Prompt:** "I ran this code: <paste it>. I got this full error: <paste it>. First explain the cause. Do not tell me to install anything until you have checked the spelling of every name in my code."

**Use it when:** you see `ModuleNotFoundError` and do not know whether a package is missing or a name is wrong.

**A good answer:** it checks the spelling of the import first, then whether the virtual environment is active, and only then whether the package is installed.

**Check it:** if the answer tells you to install a package, check that exact name on pypi.org and with your own name check. A name one letter away from a famous package is a warning sign.

## Improve: One change, checked against your rules

**Prompt:** "My setup works: a virtual environment, pinned versions in requirements.txt and a name check. Suggest one improvement, with one reason. Keep every install inside the virtual environment."

**Use it when:** your project works and you want it safer or easier to share.

**A good answer:** one small change, such as pinning a missing version or adding `.venv` to the files your version control ignores.

**Check it:** reject any suggestion that installs outside the virtual environment, uses `sudo` or `--break-system-packages`, or adds a package you have not checked.
