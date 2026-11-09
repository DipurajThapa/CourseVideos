# Code Quest: Learn to Code with AI

A practical, gamified programming course that teaches two skills together: how to write code, and how to use AI assistants such as ChatGPT and Claude at every stage of software development. Learners focus on understanding concepts and applying them step by step, not on memorising syntax.

New chapters are produced automatically, one per day, by a scheduled Claude run. Every chapter is researched against current sources, every example is executed before it is published, and every chapter waits in a review queue for the course owner.

## Languages

| Order | Language | Status |
|---|---|---|
| 1 | Python | In production (28 chapters, 6 modules) |
| 2 | JavaScript | Curriculum built after Python |
| 3 | Java | Planned |
| 4 | C | Planned |
| 5 | C++ | Planned |

Live progress is in [`state/progress.json`](state/progress.json) and [`REVIEW.md`](REVIEW.md).

## What each chapter contains

```text
chapters/<language>/<NN>-<slug>/
  lesson.md            the chapter (project.md for boss-level projects)
  examples/            every runnable example with its verified .expected output
  ai-prompts.md        six prompt cards: plan, write, generate, debug, test, improve
  practice/            8 tasks in three tiers, with verified solutions
  video/storyboard.json  the video direction: scenes, beats, narration and what is on screen
  video/chapter.mp4      the narrated full-chapter video (1080p, captions, scene markers)
  video/chapter.srt      captions; video/description.md upload text; video/render.json render record
  video/script.md        human-readable script with timings (generated from the storyboard)
  sources.md           sources, access dates and what each confirmed
  meta.json            metadata, changes and outstanding issues
  verification.json    machine-written proof of what was tested, when and on what
```

## How the daily run works

1. `tools/state.py next` picks the single next item: resume interrupted work, apply requested changes, start the next chapter, or build the next language's curriculum.
2. The run researches the topic on official documentation and credible sources, then writes the chapter on a `wip/<chapter-id>` branch, pushing checkpoints as it goes.
3. `tools/verify_chapter.py` executes every example and solution on every available toolchain, checks lesson code against the tested files, and checks structure, sources and plain-language rules.
4. `tools/render_video.py` turns the storyboard into a narrated walkthrough video of the whole chapter, and the verification tool checks that the video matches the verified files.
5. Only a fully passing chapter is merged into `main` with status `in_review`, and a report lands in `reports/`.

Full procedure: [`RUNBOOK.md`](RUNBOOK.md). Content rules: [`STANDARDS.md`](STANDARDS.md).

## Reviewing

Open [`REVIEW.md`](REVIEW.md), read the chapter, then:

```bash
python3 tools/state.py approve python-01
python3 tools/state.py request-changes python-02 "Use a shopping example instead of the bank example"
```

Approved chapters are never edited by the daily run. If later research finds a problem in one, the run writes a proposal to `corrections/` for you to accept or reject.
