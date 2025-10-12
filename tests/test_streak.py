import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Covers: Empty input."""
    assert longest_positive_streak([]) == 0

def test_longest_streak_wins():
    """Covers: Data with multiple streaks (ensure the longest wins)."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
    assert longest_positive_streak([1, -1, 3, 4, 5, 6, 0, 7, 8]) == 4

def test_inputs_containing_zeros_and_negatives():
    """Covers: Inputs containing zeros and negatives."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6]) == 2
    assert longest_positive_streak([0, 0, -1, -2]) == 0
    assert longest_positive_streak([-10, 1, 2, 3, -5, 4]) == 3

def test_all_positive_numbers():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_single_element_list():
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0