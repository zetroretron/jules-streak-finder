from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    """
    Returns the length of the longest run of consecutive values strictly greater than 0.
    """
    max_streak = 0
    current_streak = 0

    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            # Non-positive number breaks the streak
            max_streak = max(max_streak, current_streak)
            current_streak = 0

    # Final check for a streak that runs to the end of the list
    max_streak = max(max_streak, current_streak)
    return max_streak