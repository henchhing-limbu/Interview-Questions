'''
Given:
array of integers
number k where 1 <= k <= len(array)

Goal:
Compute maximum values of each subarray of length k

Example:
Array = [10,5,2,7,8,7], k = 3
Output: [10, 7,8]

'''

'''
Solution:

Use a sliding window
Not trivial as it looks
Need to use deque to keep track of ints to the right of the max value
because those values might be max value when the max value goes out of the sliding window
To bring the complexity down, we don't put every elements to the right of max value in deque
Instead whenever we push a number to the deque, we want to get rid of any smaller values than
the number from the deque. this makes the complexity of the solution O(2n) - O(n) 
'''