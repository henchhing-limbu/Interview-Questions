"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.



Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
"""

# This a greedy algorithm question.
# We for sure know that the tasks needs to be arranged in such a way that in
# between the cooling time of each task, other taks can be carried out.


from collections import Counter
import heapq
def least_interval(tasks, n):
    cycles = 0
    # find the number of occurences of each task
    task_occurences = Counter(tasks)
    # put the count of each task into a heap
    heap = [-1 * value for value in task_occurences.values()]
    heapq.heapify(heap)
    while heap:
        executed_tasks = []
        # Insert as many unique tasks that can be executed in n time.
        for _ in range(n+1):
            if not heap:
                break
            executed_tasks.append(heapq.heappop(heap))

        # Decrement the count of the executed tasks.
        # Insert the new task count into the heap.
        for i in executed_tasks:
            j = i + 1
            if j < 0:
                heapq.heappush(heap, j)
        # All job execution did not take more than n+1.
        if not heap:
            cycles += len(executed_tasks)
        else:
            cycles += n+1
    return cycles

assert least_interval(['A', 'A', 'A', 'B', 'B', 'B'], 2) is 8




