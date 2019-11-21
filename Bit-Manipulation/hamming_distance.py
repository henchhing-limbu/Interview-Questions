"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

# The only time a number n modulo 2 is 1 is when the rightmost bit of the n is
# 1. So, we can go from right and compare if the two numbers rightmost bit are
# same or not. Then we can right shift the numbers by 1 bit to get second
# rightmost bits. We increment count when the bits are different. We do this
# until both numbers are 0s.

def hamming_distance(x, y):
    distance = 0
    while x > 0 or y > 0:
        if x % 2 != y % 2:
            distance += 1
        x >>= 1
        y >>= 1
    return distance

assert hamming_distance(2, 4) is 2
