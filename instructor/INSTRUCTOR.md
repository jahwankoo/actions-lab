# Instructor guide: Actions Lab (120 minutes)

## Before class (rehearse once, 30 minutes)

Do everything below with a fresh GitHub account, not your own, so you see what students see.

- [ ] Push this folder to a new repository and tick **Settings > General > Template repository**.
- [ ] On the second account: **Use this template**, create a **public** repository, open the Actions tab.
- [ ] Lab 1: run the workflow, download the artifact, uncomment the commit step, run again, check the README card.
- [ ] Lab 2: run it and confirm `0 / 8`. Then paste `instructor/answers/lab2_solution.py` over `solution.py` and confirm `8 / 8` on both Python versions.
- [ ] Lab 3: open an issue and confirm the comment appears within about a minute.
- [ ] Note down anything that differs from this guide. Items marked **unverified** below were not checked by the author.

## Timeline

| Minutes | Activity |
| --- | --- |
| 0 - 10 | What Actions is and when to use it: events, workflows, runners. Show the Actions tab of a finished run |
| 10 - 35 | Lab 1 (5 explain, 15 hands-on, 5 share cards) |
| 35 - 60 | Lab 2 (5 explain, 15 hands-on, 5 compare scores) |
| 60 - 65 | Break |
| 65 - 90 | Lab 3 (5 explain, 15 hands-on, 5 share haikus) |
| 90 - 110 | Lyric2Poster demo: `collect-charts.yml` combines Lab 1 (schedule, commit back) and secrets; `ci.yml`-style testing is Lab 2 |
| 110 - 120 | Wrap up. Homework: name one task in your final project that a workflow could do |

## Answer keys

- Lab 2: `instructor/answers/lab2_solution.py` (all 8 tests pass).
- Lab 3 stretch: add `("deadline", "Deadlines can be hard. Say the date and what is still missing.")` to `RULES`.
- Lab 1 TODO 2: the commit step is already written in the workflow, only commented out.

## Things that will go wrong (and the fix)

| What | Fix |
| --- | --- |
| Student pushed but nothing runs | Workflows disabled on their copy: Actions tab > enable. Or they edited a file outside the lab folder (Lab 2 only runs for its own folder) |
| Commit step 403 | Settings > Actions > General > Workflow permissions: Read and write |
| `rejected (fetch first)` | Start a new run with Run workflow. The Re-run button uses the old version of the file |
| Schedule never fires in class | Normal. Schedules can be late. Always test with Run workflow |
| Student opens issue and no reply | Check the run in the Actions tab. Issues must be enabled in Settings |

## Unverified (the author could not check these)

- Whether workflows in a repository created from a template start enabled, or need a click.
- Whether new template copies have Issues enabled by default.
- How late scheduled runs can be, and the free usage limits for public repositories with 35 students.
- The exact wording of GitHub buttons: they change over time.
