# Review Queue

Generated 2026-11-09T15:36:49+00:00 by `tools/build_review_queue.py`. Do not edit by hand.

To approve a chapter: `python3 tools/state.py approve <chapter-id>`.
To ask for changes: `python3 tools/state.py request-changes <chapter-id> "<what to change>"`.
You can also ask Claude to do either.

## Curricula

- python: `curriculum/python.json` (in_review)

## Ready for review

- **python-01**: Your First Program and Your AI Study Partner ([chapters/python/01-first-program](chapters/python/01-first-program)), video: [chapters/python/01-first-program/video/chapter.mp4](chapters/python/01-first-program/video/chapter.mp4). Owner request (2026-11-09): redesign the video screens in a professional, calm 'Soft Studio' style (pastel gradient, frosted cards, bold capital headings, varied deck layouts) and re-render Chapter 1.
- **python-02**: Values and Variables: Giving Data a Name ([chapters/python/02-values-and-variables](chapters/python/02-values-and-variables)), video: [chapters/python/02-values-and-variables/video/chapter.mp4](chapters/python/02-values-and-variables/video/chapter.mp4). Owner request (2026-11-09): add the narrated full-chapter walkthrough video (video/storyboard.json rendered to video/chapter.mp4) under the new STANDARDS section 11, and re-verify on Python 3.15.2.

## Changes requested

None.

## Blocked

None.

## In progress

None.

## Review checklist

- Is every fact correct and current? Check `sources.md`.
- Does each example run and teach one clear idea? See `verification.json`.
- Is the language simple, specific and free of filler?
- Does `## Work with AI` give prompts a beginner can use today?
- Watch `video/chapter.mp4`: is the narration clear, does every picture match what is said, and is it free of errors?
- Is the difficulty right after the previous chapter?
