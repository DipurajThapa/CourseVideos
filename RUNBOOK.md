# Daily Run Runbook

This is the procedure the scheduled run follows every day. It produces exactly one unit of work: the next pending chapter, or a new language's curriculum when the previous language is finished. A chapter is the written lesson plus its narrated full-chapter video; one is not complete without the other. Read `STANDARDS.md` before starting.

## Golden rules

1. Process only the next item from `python3 tools/state.py next`. Never skip ahead or work on two chapters.
2. Never edit a chapter or curriculum whose status is `approved`. Record a needed correction in `corrections/` instead (see step 10).
3. Never say that code or content is verified unless the tool ran and passed in this run. `verification.json` is the only proof.
4. Never mark incomplete work as finished. If a step fails, block the chapter with a clear reason and report it.
5. Commit and push work in progress to the `wip/<chapter-id>` branch at every checkpoint, so an interrupted run can resume.

## Status model

| Status | Meaning | Who sets it |
|---|---|---|
| `pending` | Not started | Curriculum |
| `in_progress` | A run is working on it; work lives on `wip/<chapter-id>` | Run |
| `blocked` | A run could not finish; the reason is recorded | Run |
| `in_review` | Complete, verified and merged to `main`; waiting for review | Run |
| `approved` | Reviewed and accepted; read-only for runs | Course owner |
| `changes_requested` | Owner asked for changes; the reason is in `notes` | Course owner |

The owner approves by setting the status to `approved` with `python3 tools/state.py approve <chapter-id>`, or by asking Claude to do it. Runs keep going while chapters wait in review, so review can happen in batches.

## Procedure

### 1. Prepare
```bash
cd <repo>
git checkout main && git pull --ff-only
python3 tools/setup_check.py
```
`setup_check.py` confirms the toolchains, installs the latest stable Python with an up-to-date `uv`, and prepares the video toolchain (ffmpeg, Pillow, Piper and the pinned narration voice, downloaded once to `~/.cache/coursevideos`). If a required toolchain or the video toolchain is missing and cannot be installed, block the item with the exact error and report.

### 2. Decide the work
```bash
python3 tools/state.py next
```
The output is one of:
- `{"action": "resume", ...}`: a chapter is `in_progress` or `blocked`. Fetch its `wip/` branch if it exists and continue from what is already there. A `revise` action reuses the chapter's old branch name, so start it fresh from `main` with `git checkout -B wip/<chapter-id> main`. Re-run every check; do not trust earlier results.
- `{"action": "revise", ...}`: a chapter is `changes_requested`. Apply the owner's notes on a `wip/` branch, then follow steps 4 to 11. If the notes change anything the video shows, update the storyboard and render the video again.
- `{"action": "chapter", ...}`: start the named chapter.
- `{"action": "curriculum", ...}`: the next language has no curriculum. Build it (see "Building a curriculum"), and that is the whole run.
- `{"action": "done"}`: every language is complete. Report this and stop.

Then mark the start on `main` (this records the run id), and only then create or resume the branch. State files change only on `main`, so merges never conflict:
```bash
python3 tools/state.py start <chapter-id>
git add state/ && git commit -m "chore(state): start <chapter-id>" && git push origin main
git fetch origin
git checkout -B wip/<chapter-id> origin/wip/<chapter-id>   # when resuming and the branch exists
git checkout -B wip/<chapter-id>                           # otherwise
git merge main                                             # resumed branch picks up the new run id
```

### 3. Review before writing
- Read `curriculum/<language>.json`: this chapter's concept, outcome, prerequisites and AI skill.
- Read the two previous chapters (`lesson.md`, `practice/practice.md`) to keep names, tone, running examples and difficulty consistent.
- Check `corrections/` and open issues in earlier chapters' `meta.json` that affect this chapter.
- If the curriculum entry is wrong, outdated or impractical, correct the entry on the `wip/` branch and record the change and reason in the chapter's `meta.json` (`changes`). If the language curriculum is `approved`, write a proposal in `corrections/` instead and follow the approved plan.

### 4. Research and validate
- Use web search and page fetching (the shell usually cannot reach websites).
- Read the official documentation for every feature the chapter uses, and at least two other credible sources (see `STANDARDS.md` section 8).
- Confirm current versions, installation steps and any AI tool behaviour on official sites today.
- Record every source in `sources.md` as you go: URL, date accessed, what it confirmed.
- Remove anything outdated, unsupported or impractical; note removals in `meta.json` (`changes`).

Push a checkpoint: `git add -A && git commit -m "wip(<chapter-id>): research" && git push -u origin wip/<chapter-id>`. Never change files in `state/` on the `wip/` branch.

### 5. Write the chapter
Copy `templates/lesson/` (or `templates/project/` for project chapters) to `chapters/<language>/<NN>-<slug>/` and fill it in:
- `lesson.md` or `project.md`, following `STANDARDS.md` sections 3 to 6.
- `examples/`: every runnable file with its `.expected` (and `.stdin` or `.expected_error` where needed). Generate `.expected` files by running the code, then read the output and confirm it is what the lesson says.
- `ai-prompts.md`: the six prompt cards.
- `practice/practice.md` and `practice/solutions/`.
- `video/storyboard.json`: the video direction for the complete chapter, following `STANDARDS.md` section 11. Start from the template, write one or more scenes per section, and point every code beat at a verified file. Do not write `video/script.md` by hand; the renderer generates it.
- `meta.json`: fill every field.

Push a checkpoint after each major file.

### 6. Produce the video
First run `python3 tools/verify_chapter.py <chapter>` once and fix every failure except the `video` check, so the video is built from final, verified files. Then:

1. Load the video skill with the Skill tool: `video-making` (listed as `anthropic-skills:video-making`). Follow it; the renderer already applies its encoding rules.
2. Preview every beat as a still, without audio:
   ```bash
   python3 tools/render_video.py chapters/<language>/<NN>-<slug> --preview <scratch-dir>/preview
   ```
   Open each `contact_N.png` with the Read tool, and open full-size frames for every code, table and pause beat. Fix the storyboard until no text overflows, is cut off, overlaps or is too small to read, every highlight points at the line the narration names, and every output appears only after its pause.
3. Render the video (about 3 to 6 minutes for a 15-minute video; use a long timeout or run it in the background):
   ```bash
   python3 tools/render_video.py chapters/<language>/<NN>-<slug>
   ```
4. Check the result: extract three frames from different scenes with `ffmpeg -ss <seconds> -i video/chapter.mp4 -frames:v 1 <scratch-dir>/check_N.png` and look at them, read `video/script.md`, and confirm the length in `render.json` is 10 to 15 minutes.

Push a checkpoint. The rendered files (`chapter.mp4`, `chapter.srt`, `description.md`, `render.json`, `script.md`) are committed with the chapter. If rendering fails and cannot be fixed in the run, block the chapter with the renderer's error (step 9).

### 7. Verify
```bash
python3 tools/verify_chapter.py chapters/<language>/<NN>-<slug>
```
The tool runs every example and solution on each available interpreter or compiler, compares output exactly, checks lesson code blocks against files, checks structure, practice count, sources, banned phrases and sentence length, checks the storyboard and the rendered video, and writes `verification.json`. If you change the storyboard or any file the video shows, render the video again (step 6) before verifying. Fix every failure and re-run until it passes. Then read the lesson once as a beginner would and fix anything unclear, wrong or vague. The tool cannot judge teaching quality; you must.

### 8. Merge and complete
```bash
git add -A && git commit -m "feat(<chapter-id>): <title>" && git push origin wip/<chapter-id>
git checkout main && git pull --ff-only
git merge --no-ff wip/<chapter-id> -m "Merge chapter <chapter-id> for review"
python3 tools/state.py complete <chapter-id>
python3 tools/build_review_queue.py
```
`complete` refuses unless `verification.json` passed in this run and its fingerprint matches the chapter files now on `main`. Then write the report (step 11), commit everything on `main` and push:
```bash
git add -A && git commit -m "chore(state): <chapter-id> ready for review" && git push origin main
```
Leave the finished `wip/<chapter-id>` branch in place as a record of the work. Do not delete branches; the environment does not allow it, and an old branch for a completed chapter is harmless.
If the merge conflicts or `complete` refuses, abort the merge (`git merge --abort`), block the chapter (step 9) and report. Never force-push `main`.

### 9. On a blocker
Push whatever exists on the branch, then record the block on `main`:
```bash
git add -A && git commit -m "wip(<chapter-id>): checkpoint before block" && git push origin wip/<chapter-id>
git checkout main && git pull --ff-only
python3 tools/state.py block <chapter-id> "<specific reason and what is needed>"
git add state/ && git commit -m "chore(state): <chapter-id> blocked" && git push origin main
```
Then write the report. The next run resumes the same chapter. Never skip a blocked chapter.

### 10. Corrections to approved content
If research shows an approved chapter is wrong or outdated, do not edit it. Create `corrections/<chapter-id>-<YYYY-MM-DD>.md` with the problem, the evidence (sources), and the proposed change, and mention it in the report.

### 11. Report
Write `reports/<YYYY-MM-DD>-<chapter-id>.md` and add one line to `CHANGELOG.md` (both on `main`, in the same merge). The report contains:
- Result: completed for review, blocked or curriculum built.
- Chapter title, path and commit link.
- Video: path of `video/chapter.mp4`, its length, size and scene count from `render.json`.
- Verification summary from `verification.json`: checks passed, interpreters used.
- Sources consulted and the date.
- Changes made to the curriculum or plan, with reasons.
- Outstanding issues and blockers, and what the owner needs to do.
- Next item in the queue.

Deliver the video to the owner with the SendUserFile tool (`video/chapter.mp4`, status `proactive`), then finish the run with a concise completion report in the same format as the final message.

## Building a curriculum

When `next` returns `curriculum`:
1. Research the language's current stable version, official documentation and current industry practice.
2. Write `curriculum/<language>.json` following `curriculum/python.json`: modules of 4 to 6 chapters, each module ending in a project chapter, every chapter with `concept`, `why`, `outcome`, `ai_skill`, `prerequisites`, `badge`.
3. Teach concepts that learners already met in earlier languages as differences ("what changes and why"), not from zero.
4. Run `python3 tools/state.py add-language <language>` to register the chapters as `pending`, set the curriculum status to `in_review`, and report. The first chapter of the language is produced on the next run.

## Time budget

Rendering a video takes about 3 to 6 minutes. If the run is close to its limit before the video is rendered or verification passes, push the checkpoint, block the chapter with "run ended before verification; resume" (or "before the video was rendered") and report. The next run resumes it.
