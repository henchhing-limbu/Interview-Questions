"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,

Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

# When we come across an interval, we need to know when the previous intervals
# are going to be over or were over. We need a data structure to keep track of
# previous meetings. We can use a min heap made of end time of intervals. As we
# come across a new interval, we peek the min heap and see if interval's start
# time >= end_time of peeked interval. If so, we can simply use the previous room,
# else we need to book a new room.
# Note: The intervals need to be sorted based on start time.

import heapq
def num_of_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []
    heapq.heapify(heap)
    count = 0

    for interval in intervals:
        start_time, end_time = interval
        if heap:
            # heap[0] is always the root of heap in python.
            if start_time >= heap[0]:
                heapq.heappop(heap)
            else:
                count += 1
            heapq.heappush(heap, end_time)
        else:
            count += 1
            heapq.heappush(heap, end_time)
    return count

assert num_of_rooms([[0, 30], [5, 10], [15, 20]]) == 2
assert num_of_rooms([[2, 10], [3, 5], [7, 8]]) == 2
