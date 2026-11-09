---
name: code-quest-video
description: Design, script and render a Code Quest chapter video in the approved "Soft Studio" style with an interlinked story, teach-then-test questions and stage-by-stage AI conversations. Use whenever a chapter's video/storyboard.json is written, revised or rendered, or when the course owner asks to change how chapter videos look, sound or flow.
---

# Code Quest chapter video

The owner approved this style on 2026-11-09 (Chapter 1). Keep it for every chapter and language. The rules in STANDARDS.md section 11 and RUNBOOK.md step 6 still apply; this skill is the craft guide behind them.

## Look: "Soft Studio" (never change per chapter)
- All drawing lives in `tools/video_theme.py`. Change the look only there, and re-render every chapter in review if you do.
- Pale sky-to-cream gradient, frosted white cards with soft shadows, navy text, sky accent, warm sand highlight. Coral only for errors, amber only for timers.
- Headings: bold capitals (Poppins) with a small spaced kicker and a short accent bar. Body: Inter. Code: JetBrains Mono on a deep navy card with window dots, line numbers, a sky highlight bar and dimmed other lines.
- Layouts vary like a deck: heading column plus right card (bullets, prompts, chats), full-width tables, 2x2 card grids for quick checks, centred hero cards for pause questions and breathers, a title screen with a large chapter tile.
- Footer on every screen: course name, section, chapter tile, progress line.

## Voice
- Kokoro `bm_lewis` (deep, calm, lively British male), speed 0.95, approved by the owner as the course voice for all videos. Pinned in `tools/voice.py`; never change it without the owner.
- Audio finish (automatic in the renderer): one take per beat, light vocal polish (high-pass, warmth, presence, gentle compression), a very quiet generated background pad so there is no dead silence, and a measured loudness correction to about -14 LUFS.
- Write narration for the ear: short sentences, varied rhythm, a few questions and exclamations, and natural spoken connectors ("So", "Now", "Here is the thing"). Monotone audio usually starts in a flat script.
- Each beat is spoken in one take; keep segments as whole sentences so the highlight boundaries land on pauses.
- To narrate in the owner's own voice, set `COURSE_VOICE_ENGINE=clone` and `COURSE_VOICE_REF` to a clean 10 to 30 second recording (Chatterbox, MIT, about 1.5 to 2 hours per chapter on CPU).

## Story (write this before any storyboard JSON)
1. Mission: one concrete, relatable thing the character builds in this chapter, reusing the lesson's running example. Show the finished result in the opening.
2. Character: the course's learner (Asha for Python). She makes the mistakes, asks the AI, and checks its answers.
3. Spine: every section advances the mission. Write one line per section saying how it connects to the one before.
4. Callbacks: the hook pays off later; a mistake shown in the AI section reappears in Common mistakes; the ending teases the next chapter's concept as the fix for a limit the learner has met.
5. Teach, then test. Make a table of every question and the beat that taught it. Delete or move any question without a teaching beat before it.

## Evergreen
- No calendar dates, years or "current version" claims on screen or in narration; examples use timeless data (order codes, prices, times of day). Versions are stated as minimums.

## Interaction
- Every question stays on screen with a 10-second digital timer, beside the code (side card) or below the table or output (strip). The layout is reserved for the whole beat, so nothing moves when the timer appears.
- At least 6 questions, 2 or more quick-check quizzes, and a breather after each major block (at most 3 minutes without one).
- Predict-then-reveal for every new code example; the output appears only after its question.

## Work with AI: six stages, one feature
- Pick one feature to add to the mission (Chapter 1: an order code on the receipt). Use the `chat` visual for each stage, in story order: plan, write, generate, test, debug, improve. The left column shows the stage tracker.
- Each stage: the learner's exact prompt (from ai-prompts.md, adapted), an example AI answer, and the learner's visible check (run it, compare output, count characters).
- Include at least one confident AI mistake that a method taught earlier in the video catches. Never present AI answers as guaranteed; every AI bubble carries the "Example answer" label.
- All code, output and errors in chats are verified files in `examples/` (add small example files when the story needs them, with `.expected` and `.expected_error`). Use `code_lines` to show an excerpt with real line numbers.

## Reference chapters and common critic findings
- Chapter 1 (receipt, order code) and Chapter 2 (self-updating bill, average bill of three tables) are the reference storyboards. Copy their scene shape: intro hook (problem, mission, AI tease), goals, why, idea + quiz + breather, steps with predict-then-reveal, outcome returning to the mission, six AI chats, mistakes with callbacks and spot-it asks, think beyond, recap + quiz + badge, practice, next teaser.
- Writing the storyboard as a small Python builder script (helpers `code()` and `chat()`, message lists per stage) in the scratchpad keeps it editable; the committed JSON is the source of truth.
- Every stage, including Write, works on the same feature: the learner writes part of it and asks the AI to check or predict.
- Checks critics often catch: a highlight left on the previous line when the narration moves on; an operator or idea used in an ask before it is taught; style-guide rules mixed up with language rules; "exact" for floats; a changed value that makes later output print a float glitch (run the variant before you mention it); error words (such as "concatenate") spoken but never explained.

## Process
1. Write the story spine and the teach-then-test table in the run notes.
2. Write `video/storyboard.json` (format: docstring of `tools/storyboard.py`). Narration in short spoken sentences; segments move highlights in step with each sentence.
3. `python3 tools/render_video.py <chapter> --preview <dir>`; read the contact sheets and the code, chat, quiz and question stills at full size. Fix overflow, wrapping, misplaced highlights.
4. Independent critic (Agent tool) with the storyboard, lesson, examples and stills: rubric = teach before test, one interlinked story, six AI stages on one task, accuracy of every claimed line number and output, engagement for second-language beginners, clarity, hook and ending. Fix and re-check; at most two rounds.
5. Optional early look: `--sample <file>` renders the first 60 seconds.
6. Render, then QC (film studio `afs qc`: 1080p, -14 LUFS, captions, no silences over 1.2 s) and `tools/verify_chapter.py`.
