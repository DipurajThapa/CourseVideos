# Run Report: 2026-11-09, python-01 revision (interactive video)

**Result:** DELIVERED WITH KNOWN ISSUES. The chapter passed verification and is ready for review. Two studio gates did not fully pass; see Known issues.

**Chapter:** Chapter 1, "Your First Program and Your AI Study Partner"
**Path:** `chapters/python/01-first-program`
**Run id:** 2026-11-09-f70a58
**Commit:** https://github.com/DipurajThapa/CourseVideos/commit/4aed02b

## What changed (owner request)
- Highlights follow the narration. Each sentence changes the picture: the code line being discussed (others dimmed, marker arrow), code typed in line by line, output lines, bullet items, table rows and prompt-card sentences.
- Questions stay on screen. 16 questions show the question beside or below the code or slide it refers to, with a 10-second digital timer (00:10 to 00:00, a smoothly draining bar, soft ticks). The answer is revealed and explained afterwards.
- 4 multiple-choice quick checks with the answer revealed and a one-line reason.
- 4 breather cards (after the idea, after the build steps, after Work with AI, after the mistakes): three recap points, a chapter progress map, calm narration and 4 quiet seconds with a soft tone.
- Error panels show the real error report (checked against `.expected_error`) with the line number highlighted.
- Content fixes found by the critic: the Step 5 example now prints a time (`10:30:45`) instead of the date, so the AI puzzle's fix is not shown early; the practice XP is 170, not 160.

## Video
- `video/chapter.mp4`: 15:54, 29.6 MB, 1920x1080, 30 fps, 15 scenes, 970 picture states, English captions and scene chapters.
- Narration: Piper text-to-speech, voice en_US-lessac-medium (synthetic, disclosed in `video/description.md`). The timer ticks and breather tone are generated in code.

## Verification
- `tools/verify_chapter.py`: all 9 checks passed on Python 3.15.2 and 3.13.18.
- ai-film-studio QC (`afs qc`): 1080p spec, captions (247 cues, none over 42 characters per line or 20 characters per second), no silences over 1.2 s and no black frames: PASS. Loudness -15.2 LUFS (target -14, inside the 1.5 LU tolerance), true peak -1.3 dBTP.
- Independent critic: round 1 scored 7.0 and round 2 scored 7.2 (bar 8.0). Every problem from both rounds was fixed before this render. The final render was not re-scored, because the studio's limit of two revision rounds was reached.

## Known issues
- `afs qc` freeze check fails. The detector reports held slides because highlight moves and timer digits change a small part of the screen. The picture changes on average every 3 seconds.
- The final film was not re-scored by the critic (see above).
- The video is 15:54, slightly above the 12 to 16 minute target band's midpoint, because of the added questions and breathers.

## Owner action
Watch the video and review the chapter. Then run `python3 tools/state.py approve python-01`, or request changes by naming the scene and the sentence.

## Next
Chapter 2's video uses the older format and the wrong practice XP (160). Under the new storyboard rules it must be redesigned before it can be verified again. Then python-03.
