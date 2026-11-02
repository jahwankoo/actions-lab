# Lab 2. Autograder

**Goal:** a grader that scores `solution.py` every time you push, on two Python versions.

**You will learn:** the `push` trigger, matrix builds, the job summary, and reading red and green checks.

## Steps

1. [ ] **See it fail.** Go to the Actions tab and run `lab2-autograder` with **Run workflow**. Open the run.
   Both jobs (Python 3.11 and 3.12) are red. Open **Summary**: the score is `0 / 8`.
2. [ ] **Fix one function.** Open `labs/lab2_autograder/solution.py`, write `is_palindrome`, and commit to `main`.
   The push starts a run by itself. Watch the score go up.
3. [ ] **Finish the other three** (`fizzbuzz`, `word_count`, `second_largest`). Push after each one.
   Goal: **8 / 8** and green checks on both Python versions.
4. [ ] **Break it on purpose.** Add a typo to `solution.py` (for example, delete a colon), push, and find the error in the log.
   Then fix it.

## Check yourself

- Why does the workflow run on a push to `labs/lab2_autograder/` but not when you edit a different folder?
- What does `fail-fast: false` change? Try deleting it and break one version only.
- Where does the score table in the Summary tab come from? (Open `grade.py`, function `summary`.)

## Stretch goals

- Run the grader on your own computer: `pip install pytest` then `python labs/lab2_autograder/grade.py`.
- Add a fifth function and two tests of your own to `test_solution.py`. Ask a classmate to solve it.
- Add Python 3.13 to the matrix.

## Troubleshooting

- **`pytest produced no report`:** `solution.py` has a syntax error. Read the lines above the message.
- **Red on one Python version only:** the two versions differ. Read the failing job's log, not the other one.
