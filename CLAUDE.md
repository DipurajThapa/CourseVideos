# Instructions for Claude

This repository is an automated coding course. When you work here:

1. For the daily scheduled run, follow `RUNBOOK.md` exactly. Produce one item only: the one `python3 tools/state.py next` returns.
2. Follow `STANDARDS.md` for every chapter. The verification tool enforces the checkable parts; you are responsible for teaching quality and factual accuracy.
3. Never edit chapters or curricula with status `approved`. Propose corrections in `corrections/`.
4. Never write or edit `verification.json` by hand, and never say something is verified unless `tools/verify_chapter.py` passed in this run.
5. Change `state/` only on `main`, through `tools/state.py`.
6. Check facts that change over time (language versions, installation steps, AI tool behaviour) on official sites during the run. Record every source with its access date.
7. If you cannot finish, block the chapter with a specific reason and report it. Never mark incomplete work as complete.
8. The course owner is Dipuraj Thapa. When he asks to approve or request changes, use `tools/state.py`.
9. Every chapter ships with a narrated full-chapter video rendered by `tools/render_video.py` from `video/storyboard.json` (STANDARDS.md section 11). Follow the `code-quest-video` skill (`.claude/skills/code-quest-video/SKILL.md`) for the story, look and voice, and load the `video-making` skill before rendering. A chapter whose video is missing or out of date is not complete.
