# Run Report: python-01 revision (narration voice)

**Result:** Completed and ready for review. The owner approved the new voice for all future videos.

**Chapter:** Chapter 1, "Your First Program and Your AI Study Partner" (`chapters/python/01-first-program`)
**Commit:** https://github.com/DipurajThapa/CourseVideos/commit/359d2ed

## What changed
- Voice: Kokoro-82M (open source, Apache-2.0, CPU only), voice `bm_lewis` at speed 0.95. It was chosen from ten voices by measured pitch variation and pace, then by the owner. It replaces Piper John, which measured among the most monotone.
- Fluency: each beat's narration is spoken in one take instead of sentence by sentence. Highlight changes are synced to the natural pauses in that take.
- Audio finish: high-pass, warmth and presence EQ, gentle compression, a very quiet generated background pad (no dead silence), and a measured loudness correction.
- Optional voice cloning: `COURSE_VOICE_ENGINE=clone` with `COURSE_VOICE_REF=<recording>` narrates in a cloned voice (Chatterbox, MIT). It was tested on CPU at about 6 s of compute per second of audio, which is roughly 1.5 to 2 hours per chapter. Its output carries Resemble AI's imperceptible watermark.

## Video
- `video/chapter.mp4`: 15:10 (down from 18:09), 38.9 MB, 1920x1080, 12 timed questions, 4 breathers.

## Verification
- `tools/verify_chapter.py`: all 9 checks passed.
- Film QC: -15.0 LUFS, true peak -2.2 dBTP, 265 caption cues within limits, no silences or black frames. The freeze detector still flags held slides (expected).

## Owner action
Approve with `python3 tools/state.py approve python-01`. To use your own voice later, send a clean 10 to 30 second recording.
