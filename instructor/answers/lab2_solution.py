"""Answer key for Lab 2. Copy over labs/lab2_autograder/solution.py to test the grader."""
from __future__ import annotations

import re


def is_palindrome(text: str) -> bool:
    letters = [c.lower() for c in text if c.isalnum()]
    return letters == letters[::-1]


def fizzbuzz(n: int) -> list[str]:
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in re.findall(r"[a-z']+", text.lower()):
        counts[word] = counts.get(word, 0) + 1
    return counts


def second_largest(numbers: list[int]) -> int | None:
    distinct = sorted(set(numbers), reverse=True)
    return distinct[1] if len(distinct) >= 2 else None
