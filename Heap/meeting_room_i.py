"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,

Given [[0, 30],[5, 10],[15, 20]],
return false.
"""

# We need to figure out if there are any overlapping intervals.
# To find it, we can sort the intervals based on end time.
# Then, we can check for each intervals, if it's next interval's start time is
# after current interval's end time or not. If it's after, then that's
# overlapping interval.

def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x[1])
    for i in range(len(intervals)-1):
        curr_interval, next_interval = intervals[i], intervals[i+1]
        if curr_interval[1] > next_interval[0]:
            return False
    return True

assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) == False
