# Course Standards

These standards apply to every chapter in every language. The daily run follows them, and `tools/verify_chapter.py` enforces the checkable parts. When a standard and a habit conflict, the standard wins.

## 1. Purpose of the course

The course teaches people to write code and to use AI tools well at every stage of software development. Learners must understand each concept (why it exists, how it works and what result it produces) so they can direct an AI assistant, judge its answer and correct it. Memorising syntax is not a goal. Understanding a concept and applying it step by step to reach the right result is.

## 2. Learner profile

- Absolute beginners aged 15 and over, with no prior coding experience.
- Comfortable using a chat AI such as ChatGPT or Claude.
- Studying on a laptop or desktop, in short daily sessions of 20 to 40 minutes.
- Many read English as a second language, so plain, neutral English matters.

## 3. Chapter structure (fixed)

Every lesson chapter (`lesson.md`) uses these headings, in this order:

1. `## Learning goals`: three to five outcomes, each starting with a verb the learner can demonstrate (write, run, explain, fix).
2. `## Why this matters`: the real problem this concept solves, with a real-world use.
3. `## The idea`: the mental model, with a diagram in text or a table where it helps.
4. `## Build it step by step`: small steps; each step shows code, then the output, then one sentence on why.
5. `## See the outcome`: the complete working example and its exact output.
6. `## Work with AI`: how AI helps with this concept across planning, writing, generating, debugging, testing and improving (see section 5).
7. `## Common mistakes`: the three or four errors beginners actually make, each with the real error message and the fix.
8. `## Think beyond`: one or two "what if" questions that apply the concept to a new situation.
9. `## Recap`: the concept in plain sentences, XP earned and the badge unlocked.
10. `## Practice`: a link to `practice/practice.md`.
11. `## What's next`: one sentence linking to the next chapter.

Project chapters (the "boss level" at the end of each module) use `project.md` instead, with: `## The mission`, `## What you will build`, `## Acceptance criteria`, `## Plan it with AI`, `## Build it step by step`, `## Test it`, `## Improve it with AI`, `## Recap`, `## What's next`.

## 4. Language rules

- Neutral international English. Complete sentences, active voice, addressing the learner as "you".
- Average sentence length of 18 words or fewer; no sentence over 30 words (checked by the tool, excluding code).
- Define each technical term in one simple sentence the first time it appears, then use the same word every time.
- No idioms, slang, cultural references, filler or hype. Banned phrases are listed in `tools/banned_phrases.txt`.
- No em dashes. Use commas, colons or separate sentences.
- Be specific: name the exact value, line or output instead of describing it vaguely.
- Keep content evergreen: no calendar dates, years or "current version is" claims in lessons, examples or videos. State versions as minimums ("Python 3.12 or newer") and point to the official download page. Access dates in `sources.md` are records, not content, and stay.
- Use an analogy only when it maps to the concept precisely, and say where it stops working.
- Avoid repetition. Do not explain the same idea twice in one chapter.

## 5. AI integration rules (every chapter)

`## Work with AI` and `ai-prompts.md` must show how AI helps with all six activities, applied to this chapter's concept:

| Activity | What the learner does |
|---|---|
| Plan | Ask AI to break the task into steps before writing code. |
| Write | Write the code themselves first, then compare with an AI version. |
| Generate | Ask AI for code or examples with a precise, constrained prompt. |
| Debug | Give AI the exact error message and code, ask for the cause before the fix. |
| Test | Ask AI for test cases, including edge cases, then run them. |
| Improve | Ask AI to review for readability or efficiency, then judge each suggestion. |

Each prompt card contains: the exact prompt, when to use it, what a good AI answer contains, and how to check the answer. Never present an AI answer as guaranteed. Each chapter includes one "AI pair moment": a realistic AI-generated answer with a plausible flaw that the learner finds and fixes. The flawed code must be a real file in `examples/` and the tool must confirm it actually produces the wrong result or error.

Name AI tools generically ("an AI assistant such as ChatGPT or Claude"). Do not claim features, model names, prices or limits of AI products unless verified on the vendor's official site during the run, with the source recorded.

Safety habits taught from Chapter 1: never paste passwords, keys or private data into an AI tool; always run and read AI code before trusting it; the learner remains responsible for the code.

## 6. Code rules

- Every code block in a lesson that the learner could run must be a real file, marked by its first line: `# file: examples/<name>.py` (use the language's comment syntax). The tool checks that the block matches the file exactly.
- Every runnable file has a `.expected` file with its exact standard output. If it reads input, a `.stdin` file provides it. If it is meant to fail, an `.expected_error` file holds a line that must appear in the error output.
- Code that is shown only to illustrate (for example a fragment) starts with `# illustrative` and is never presented as runnable.
- Use current, idiomatic style for the language version in `curriculum/<language>.json`. Follow the official style guide (PEP 8 for Python).
- Keep examples short: 25 lines or fewer for lessons, unless a project needs more.
- Use realistic, practical scenarios (bills, lists, messages, files, data), not abstract `foo` and `bar`.

## 7. Practice rules

`practice/practice.md` has exactly 8 tasks: 3 warm-up, 3 apply and 2 stretch, each under `### Task N: <title>`. Each task has the goal, the expected output, a hint, an AI-assisted variant ("ask an AI for X, then check it for Y") and a link to its solution in `practice/solutions/`. Every solution runs and matches its `.expected` file.

## 8. Sources and fact-checking

- Each chapter cites at least three sources in `sources.md`, with URL, the date accessed and what each source confirmed.
- At least one source is the official documentation for the language (see `tools/official_domains.json`).
- Prefer official documentation, then respected teaching sites and standards bodies. Do not cite forums, content farms or AI-generated pages.
- Paraphrase. Never copy passages from a source.
- Facts that change over time (versions, tool installation steps, AI product behaviour) are checked during the run, never taken from memory.

## 9. Gamification

- Lesson chapter: 100 XP. Practice: warm-up 10 XP each, apply 20 XP each, stretch 40 XP each. Project chapter: 300 XP.
- Each chapter unlocks one badge, named in `meta.json` and in the recap.
- Each module ends with a project chapter, the boss level.

## 10. Continuity and difficulty

- A chapter may only use concepts taught in earlier chapters, plus the one it teaches. If an earlier concept is needed, link to its chapter.
- Each chapter is slightly harder than the last. Projects combine every concept in their module.
- Reuse the running examples and names established earlier where it helps learners connect ideas.

## 11. Chapter video

Every chapter ships with a narrated video that walks through the complete chapter. The video is part of the chapter: a chapter without a passing, rendered video cannot be completed.

**Direction: `video/storyboard.json`.** The author writes the storyboard; everything else is generated from it. The full format is documented at the top of `tools/storyboard.py`.
- Scenes follow the chapter: an introduction with a hook, then one or more scenes for every section heading (section 3), in the same order. Each scene has an `id`, a `section` (the exact heading), a `title`, a `direction` note for the editor, and `beats`.
- **One story per chapter.** A relatable learner character (Asha in Python) works toward one concrete mission (Chapter 1: the Corner Cafe receipt). Every section moves that mission forward, and later sections call back to earlier ones. Show the finished result in the opening as the destination; end with a teaser that the next chapter solves (Chapter 1: prices typed twice, solved by variables).
- **Teach, then test.** Never ask a question about something not yet explained on screen. Each question tests the idea taught just before it.
- **AI, stage by stage, on the same task.** In `## Work with AI`, show one realistic conversation per stage (plan, write, generate, test, debug, improve) with the `chat` visual, all about one feature of the mission (Chapter 1: adding an order code to the receipt). Each stage shows the learner's check: running the code, comparing output, counting characters. Include at least one confident AI mistake that a taught method catches. Label every AI answer as an example.
- **The picture follows the narration.** Split each beat's narration into `segments`. Each segment changes the picture while it is spoken: the code `highlight` (the line being talked about), `lines` (code typed in line by line), `output` (revealed after a prediction), `out_highlight` (the output line being talked about), `reveal` and `focus` (bullets), `focus_row` (tables), `focus` (prompt card sentences). Never highlight a line before the narration reaches it. No picture should stay unchanged for more than about 8 seconds of narration.
- **Questions stay on screen.** An `ask` shows the question beside or below the content it is about, with a 10-second digital timer on the same screen, then `after` segments reveal and explain the answer. Use them to predict output, spot a bug, or recall a rule. At least 6 questions per chapter.
- **Quick checks.** At least 2 `quiz` beats: a multiple-choice question, the 10-second timer, then the answer revealed with a one-line reason.
- **Breathers.** A `breather` card after each major block: three recap points, the chapter progress map, a short calm narration and 3 quiet seconds with a soft tone. At least one breather per 4 minutes, and never more than 3 minutes without a question or a breather.
- A `code` beat names a verified file in `examples/` or `practice/solutions/`. Outputs and errors come only from verified files; an error panel shows the real error report, checked against `.expected_error`.
- Narration is spoken English that follows section 4. Write it as you would say it: no symbols such as `_`, `=`, `/`, `%`, `*`, `#` or backticks ("tea price", "double slash", "ex 0 1"). Refer to line numbers as the lesson does.
- Target length 12 to 16 minutes; the tool accepts 8 to 20.

**Screen design: "Soft Studio"** (`tools/video_theme.py`, shared by every chapter). A pale sky-to-cream gradient, frosted white cards with soft shadows, navy text, a sky accent and a warm sand highlight; coral only for errors, amber only for timers. Headings are bold capitals (Poppins) with a small spaced kicker and an accent bar; body text is Inter; code is JetBrains Mono on a deep navy card. Layouts vary like a slide deck: a heading column with a card on the right, full-width tables, card grids for quick checks, centred hero cards for questions and breathers, and a title screen with a chapter tile. A footer carries the course name, the section and a chapter tile. Change the look only in the theme file, never per chapter.

**Rendering: `python3 tools/render_video.py <chapter>`.** It produces, in `video/`:
- `chapter.mp4`: 1920x1080, 30 fps, H.264 video, AAC narration at -14 LUFS, soft English captions and scene chapter markers. Changes of picture crossfade; the timer ticks once a second and its bar drains smoothly.
- `chapter.srt`: captions for upload; `description.md`: an upload description with scene timestamps and the synthetic-voice disclosure; `render.json`: the inputs, voice and tool versions; `script.md`: the human-readable script with real timings.
- Narration uses Kokoro (open source, Apache-2.0, runs on CPU) with one pinned voice, `bm_lewis` (deep, calm, lively British male), chosen by the owner after a measured comparison. Each beat's narration up to its question is spoken in one take so it flows; highlights are synced to the natural pauses. The audio gets a light polish (warmth, presence, gentle compression), a very quiet generated background pad, and loudness of about -14 LUFS. An optional `clone` engine (Chatterbox, MIT) narrates in a cloned voice from a 10 to 30 second recording (`COURSE_VOICE_ENGINE=clone`, `COURSE_VOICE_REF=<file>`); it is about ten times slower. Settings live in `tools/voice.py`. Disclose the synthetic voice wherever the video is published.
- The renderer follows the `video-making` skill: one encoded file per scene with identical settings, joined with the concat demuxer and `-c copy`, sound added with `-c:v copy`, temporary names renamed only on success, held stills without zoom.

Before rendering, review the preview stills and get an independent critic's score (see `RUNBOOK.md` step 6). `tools/verify_chapter.py` checks the storyboard (coverage, verified files, speakable narration, questions, quizzes, breathers, length) and the rendered video (hashes of the storyboard and every file it shows, 1080p video, audio, captions, duration). Any change to the storyboard or to a file the video shows requires a new render.
