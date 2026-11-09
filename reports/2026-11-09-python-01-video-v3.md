# Run Report: python-01 revision (story, design and voice)

**Result:** Completed and ready for review. Two automated warnings remain (see Known issues).

**Chapter:** Chapter 1, "Your First Program and Your AI Study Partner"
**Path:** `chapters/python/01-first-program`
**Commit:** https://github.com/DipurajThapa/CourseVideos/commit/c3884ff

## What changed (owner requests)
- Design: the "Soft Studio" look (pastel gradient, frosted cards, bold capital headings, varied deck layouts, footer tile), now the shared theme for every chapter (`tools/video_theme.py`).
- Story: one connected story. Asha builds the Corner Cafe receipt, then adds an order code with an AI assistant at six stages (plan, write, generate, test, debug, improve). She catches two AI mistakes by checking: wrong spacing (caught by a test) and a wrong claim about alignment (caught by counting). The ending sets up Chapter 2 (prices typed twice).
- Teach, then test: all 12 questions follow the beat that teaches their idea.
- Real AI examples: a new chat screen shows each prompt, an example AI answer (labelled), and Asha's check. All code, outputs and errors shown are verified files.
- Evergreen: no calendar dates or "current version" claims. The AI pair moment now prints an order code (`CAFE-1024-T4`); lesson Step 1 asks for the latest Python, 3.12 or newer.
- Voice: Piper `en_US-john-medium`, chosen by the owner from three tested deep male voices.

## Video
- `video/chapter.mp4`: 18:09, 39.9 MB, 1920x1080, 15 scenes, 12 timed questions, 4 breathers, captions and scene chapters.

## Verification
- `tools/verify_chapter.py`: all 9 checks passed.
- Film QC: 1080p, captions (265 cues within limits), no silences, no black frames; loudness -15.2 LUFS, true peak -1.8 dBTP (within the -14 LUFS tolerance).
- Independent critic: storyline round 1 scored 6.3 and round 2 scored 7.3. All round-2 findings were fixed before the final render; the final render was not re-scored.

## Known issues
- The freeze detector flags held slides with small changes (highlights, timer digits); this is expected for a slide lesson.
- At 18:09 the video is longer than the 12 to 16 minute target (the limit is 20) because of the AI walkthrough.
- Chapter 2's video still uses the earlier format and voice.

## Owner action
Watch the video, then approve with `python3 tools/state.py approve python-01` or request changes by scene and sentence.
