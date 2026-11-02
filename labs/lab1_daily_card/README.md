# Lab 1. Daily card

**Goal:** a workflow that draws a new picture every day and puts it on the front page of your repository.

**You will learn:** `workflow_dispatch` (a Run button), `schedule` (cron), artifacts, and committing from a workflow.

## Steps

1. [ ] **Run it by hand.** Actions tab > `lab1-daily-card` > **Run workflow** > **Run workflow**.
   Open the finished run. At the bottom, under **Artifacts**, download `daily-card` and look at the picture.
   The repository did not change. The run machine was thrown away; only the artifact was kept.
2. [ ] **Publish the card (TODO 2).** Open `.github/workflows/lab1-daily-card.yml`, click the pencil icon, and
   remove the leading `# ` from every line of the **Commit the card** step. Commit the change, then run the workflow again.
   Reload the repository front page: today's card is there, and the commit author is `card-bot`.
3. [ ] **Make the design yours.** Edit `labs/lab1_daily_card/make_card.py`: add a palette to `PALETTES`, or change `SHAPE_COUNT`.
   Commit, run the workflow, and compare.
4. [ ] **Schedule it (TODO 3).** Remove the `# ` in front of the three `schedule` lines. Change the cron time to
   about 10 minutes from now in **UTC** and wait. (Seoul is UTC+9, so 21:30 in Seoul is `30 12 * * *`.)
   Scheduled runs can be late. If nothing happens, keep going and check again later.

## Check yourself

- Why did the picture not appear in the repository after step 1?
- Why does running the workflow twice on the same day give the same picture?
- What would happen if two people pushed at the same moment? (Look at the `git pull --rebase` loop.)

## Stretch goals

- Change the date text, or draw the weekday in a different color.
- Make a second workflow that runs on a different day of the week.
- Test the script on your own computer: `pip install pillow` then `python labs/lab1_daily_card/make_card.py --date 2026-12-25`.

## Troubleshooting

- **403 when pushing:** set Workflow permissions to Read and write (Settings > Actions > General).
- **The commit step shows "nothing to commit":** the picture for this date is already in the repository. That is normal.
