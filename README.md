# Actions Lab

Three small, independent labs that teach GitHub Actions by building things that run on their own.
Course: Arts and Advanced Big Data, week 10. You need a GitHub account and a browser. No API keys.

<!-- CARD:START -->
_Your card of the day will appear here after Lab 1._
<!-- CARD:END -->

## Start here

1. Click **Use this template**, then **Create a new repository**. Name it `actions-lab`, choose **Public**, and create it.
2. Open the **Actions** tab of your new repository. If GitHub shows a button to enable workflows, click it.
3. Open **Settings > Actions > General**. Under **Workflow permissions** choose **Read and write permissions** and save.
4. Pick a lab. They do not depend on each other.

| Lab | You build | Trigger you learn | Time |
| --- | --- | --- | --- |
| [1. Daily card](labs/lab1_daily_card/README.md) | A bot that draws a new picture every day and shows it on this page | `workflow_dispatch`, `schedule`, artifacts, committing from a workflow | 25 min |
| [2. Autograder](labs/lab2_autograder/README.md) | A grader that scores your code every time you push | `push`, matrix builds, job summary, red and green checks | 25 min |
| [3. Issue bot](labs/lab3_issue_bot/README.md) | A bot that answers every new issue with a haiku | `issues`, permissions, safe handling of untrusted text | 25 min |

## Three ideas to remember

- A **workflow** is a YAML file in `.github/workflows/`. GitHub runs it when an **event** happens.
- Each run starts on a **fresh machine**. Anything you want to keep must be uploaded, committed or posted.
- The log is the first place to look. Read the red line, then the lines above it.

## If something goes wrong

| Symptom | Likely cause |
| --- | --- |
| The Actions tab shows only "Get started" | The `.github/workflows` folder is missing. Check that the template copied it |
| The commit step fails with a 403 error | Step 3 above: set Workflow permissions to Read and write |
| `rejected ... (fetch first)` on push | The branch moved during the run. Start a **new** run with Run workflow. Re-run uses the old version of the file |
| A scheduled run did not start | Schedules can be late by many minutes. Use the **Run workflow** button when testing |
| The workflow runs but your edit has no effect | You pushed to a different branch than `main`, or edited a file outside the lab folder |

License: MIT.
