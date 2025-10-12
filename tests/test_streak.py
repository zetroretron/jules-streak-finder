import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_longest_streak_wins():
    """Test that the function returns the longest of multiple streaks."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Test that zeros and negative numbers correctly break streaks."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6]) == 2

def test_all_positive_numbers():
    """Test a simple case with all positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_no_positive_numbers():
    """Test that a list with no positive numbers returns 0."""
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_streak_at_the_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, -2, 3, 4, 5]) == 3

def test_streak_at_the_beginning():
    """Test when the longest streak is at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, -4, 5]) == 3