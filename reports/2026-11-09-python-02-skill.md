# Run Report: python-02 revision (code-quest-video skill)

**Result:** Completed and ready for review.

**Chapter:** Chapter 2, "Values and Variables: Giving Data a Name" (`chapters/python/02-values-and-variables`)
**Commit:** https://github.com/DipurajThapa/CourseVideos/commit/1d02c82

## What changed
- Video rebuilt with the owner-approved style: Soft Studio design and the Kokoro `bm_lewis` voice. Like Chapter 1, each beat is spoken in one take with the audio finish.
- One story: Asha's Chapter 1 receipt typed every price twice. Her mission is a cafe bill that updates itself when one price changes.
- Teach then test throughout, with predict-then-reveal on every example: 16 timed questions, 4 quick-check quizzes and 4 breathers.
- Work with AI covers all six stages on one feature, the average bill of three tables. Asha catches two confident AI mistakes:
  - 52.0 instead of 24.0, from the order of operations;
  - a suggestion to use `//`, which drops the decimals.
- New verified examples: `ai_bills_typo.py` (NameError), `ai_floor_check.py` and `ai_average_final.py`. The AI pair moment now averages bills 18, 24 and 30.
- Lesson corrections found by the critic: only the first naming rule comes from PEP 8; the other three are language rules. `/` gives "the full answer, with decimals", not "the exact answer". The "change the tea price" example now uses 4.5.
- Practice XP corrected to 170.
- Renderer 3.0.1 fixes an off-by-one in the background pad length that crashed long renders.
- Future episodes:
  - RUNBOOK step 6, CLAUDE.md and the daily scheduled task now direct every chapter to `.claude/skills/code-quest-video/SKILL.md`.
  - The skill gained reference notes and common critic findings.

## Video
- `video/chapter.mp4`: 18:25, 45.3 MB, 1920x1080, 16 scenes.
- The independent critic scored the storyboard 7.7/10. All 12 of its fixes were applied before the render.

## Verification
- `tools/verify_chapter.py`: all checks passed (run 2026-11-09-4f3b81).
- Film QC:
  - -15.1 LUFS, true peak -2.2 dBTP;
  - 327 caption cues, none bad and no overlaps;
  - no long silences or black frames.
  - The freeze detector flags held slides, which is expected.

## Outstanding
- The traceback for Mistake 1 shows the short file name.
- The owner should flag any word the voice mispronounces.

## Owner action
Watch the video, then approve with `python3 tools/state.py approve python-02` or request changes.
