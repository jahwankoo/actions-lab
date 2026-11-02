"""Lab 2: make the autograder turn green.

Replace each `raise NotImplementedError` with working code. Push after each function and watch the
Actions tab: the score goes up one test at a time.
"""
from __future__ import annotations


def is_palindrome(text: str) -> bool:
    """True if `text` reads the same backwards, ignoring case, spaces and punctuation.

    "A man, a plan, a canal: Panama" -> True.  "" -> True.
    """
    raise NotImplementedError("TODO: is_palindrome")


def fizzbuzz(n: int) -> list[str]:
    """Return the strings for 1..n: "Fizz" for multiples of 3, "Buzz" for 5, "FizzBuzz" for both,
    otherwise the number as text. fizzbuzz(0) -> [].
    """
    raise NotImplementedError("TODO: fizzbuzz")


def word_count(text: str) -> dict[str, int]:
    """Count words, ignoring case. A word is a run of letters or apostrophes.

    "The cat and the hat" -> {"the": 2, "cat": 1, "and": 1, "hat": 1}.  "" -> {}.
    """
    raise NotImplementedError("TODO: word_count")


def second_largest(numbers: list[int]) -> int | None:
    """The second largest DISTINCT value, or None if there are fewer than two distinct values.

    [3, 1, 4, 4] -> 3.  [5, 5] -> None.  [] -> None.
    """
    raise NotImplementedError("TODO: second_largest")
