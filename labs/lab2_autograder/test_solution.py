from solution import fizzbuzz, is_palindrome, second_largest, word_count


def test_palindrome_basic():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("hello") is False


def test_palindrome_edge_cases():
    assert is_palindrome("") is True
    assert is_palindrome("No 'x' in Nixon") is True
    assert is_palindrome("ab") is False


def test_fizzbuzz_basic():
    assert fizzbuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                            "11", "Fizz", "13", "14", "FizzBuzz"]


def test_fizzbuzz_zero_and_one():
    assert fizzbuzz(0) == []
    assert fizzbuzz(1) == ["1"]


def test_word_count_basic():
    assert word_count("The cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}
    assert word_count("Don't stop, don't stop!") == {"don't": 2, "stop": 2}


def test_word_count_empty():
    assert word_count("") == {}
    assert word_count("... !!!") == {}


def test_second_largest_basic():
    assert second_largest([3, 1, 4, 4]) == 3
    assert second_largest([10, 20]) == 10


def test_second_largest_short_or_equal():
    assert second_largest([5, 5]) is None
    assert second_largest([7]) is None
    assert second_largest([]) is None
