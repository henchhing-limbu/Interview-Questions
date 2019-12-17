"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""

# The brute force way would be to keep track of every elements in an array and
# we sort the numbers in the array and return mid values when we want to find
# the median. This is bad. We might need to sort for every new number that is
# added to the array.

# We somehow need a way to keep track of mid values at constatnt time. The best
# way to do is to use two heaps, min heap and max heap. Min heap is used to
# keep track of upper half of sorted array and max heap is used to keep track
# of lower half of sorted numbers. We also want to make sure that their size
# difference does not exceed by more than 1.

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_num(self, num):
        if not self.min_heap:
            heapq.heappush(self.min_heap, -num)
        elif num > -self.min_heap[0]:
            heapq.heappush(self.max_heap, num)
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        else:
            heapq.heappush(selfmin_heap, -num)
            if len(self.min_heap) > len(self.max_heap) + 1:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] - self.min_heap[0])/2
        else:
            return -self.min_heap[0]
