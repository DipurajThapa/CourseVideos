# Run Report: 2026-11-09, python-01 revision (video)

**Result:** Revision completed and ready for review (owner request: add the full-chapter video).

**Chapter:** Chapter 1, "Your First Program and Your AI Study Partner"
**Path:** `chapters/python/01-first-program`
**Run id:** 2026-11-09-74d87e
**Commit:** https://github.com/DipurajThapa/CourseVideos/commit/2eaa1ac

## Video
- `video/chapter.mp4`: 11:32, 16.4 MB, 1920x1080, 15 scenes, 48 beats, 9 pause points, English captions and scene chapters.
- Direction in `video/storyboard.json`; upload text with timestamps in `video/description.md`; captions in `video/chapter.srt`.
- Narration: Piper text-to-speech, voice en_US-lessac-medium (synthetic voice, disclosed in the description).

## Verification
- All 9 checks passed, including the new video check (storyboard covers all 11 sections, only verified files are shown, the video matches the storyboard and files, 1080p with audio and captions).
- Examples ran on Python 3.15.2 (current release) and 3.13.18. The setup tool now installs 3.15.2; previously a stale uv binary missed it.

## Changes made
- Added the narrated video. The lesson text, examples and practice are unchanged.

## Outstanding issues
- Installation steps are checked against official documentation only.
- Watch the video once for mispronounced words; fixes go in the renderer's PRONOUNCE list.

## Owner action
Watch the video and review the chapter, then run `python3 tools/state.py approve python-01`, or request changes.

## Next
python-02 revision (video), then python-03.
