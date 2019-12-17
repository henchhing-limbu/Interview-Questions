"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""

# This problem simply breaks down to finding number of overlapping intervals.
# Sorting the intervals based on end time makes it a greedy choice problem.

# Example:
# [[1, 5], [2, 3], [3, 4]]
# After sorting:
# [[2,3], [3,4], [1,5]]
# if interval.st < last_interval.et there is overlap. Get rid of it.
# But keep last_interval unchanged.


def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda interval: interval[1])
    last_interval = intervals[0]
    count = 0

    for interval in intervals[1:]:
        # Check if the last non overlapping interval's finish time is less than
        # or equal to current interval's start time.
        if interval[0] >= last_interval[1]:
            last_interval = interval
        else:
            count += 1
    return count

assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) is 1
assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) is 2
assert erase_overlap_intervals([[1, 2], [2, 3]]) is 0
assert erase_overlap_intervals([[1, 5], [2,3], [3,4]]) is 1
