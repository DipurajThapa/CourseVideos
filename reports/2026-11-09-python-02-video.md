# Run Report: 2026-11-09, python-02 revision (video)

**Result:** Revision completed and ready for review (owner request: add the full-chapter video).

**Chapter:** Chapter 2, "Values and Variables: Giving Data a Name"
**Path:** `chapters/python/02-values-and-variables`
**Run id:** 2026-11-09-3f211e
**Commit:** https://github.com/DipurajThapa/CourseVideos/commit/dd31b64

## Video
- `video/chapter.mp4`: 14:09, 20.5 MB, 1920x1080, 16 scenes, 63 beats, 8 pause points, English captions and scene chapters.
- Direction in `video/storyboard.json`; upload text with timestamps in `video/description.md`; captions in `video/chapter.srt`.
- Narration: Piper text-to-speech, voice en_US-lessac-medium (synthetic voice, disclosed in the description).

## Verification
- All 9 checks passed, including the video check. Examples ran on Python 3.15.2 (current release) and 3.13.18; the error messages shown in the lesson are unchanged on 3.15.

## Changes made
- Added the narrated video. The lesson text, examples and practice are unchanged.

## Outstanding issues
- Tracebacks in the lesson show short file names; learners will see full paths.
- Watch the video once for mispronounced words; fixes go in the renderer's PRONOUNCE list.

## Owner action
Watch the video and review the chapter, then run `python3 tools/state.py approve python-02`, or request changes.

## Next
python-03: Working with Text: Strings and f-strings (the next scheduled run, with its video).
