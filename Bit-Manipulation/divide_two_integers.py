"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""

# Since you cannot use multiplication divison and mod operator, my initial go
# to this problem was to subtract divisor from dividend until dividend is
# less than divisor. We keep track of count and we return that as result.
# Time complexity would be O(n)

# However, this can be optimized using Bit operation. Shifting to the left by
# 1 bit equals to dividing the number by 2. How that can be used to solve this
# problem is explained well here.
# https://leetcode.com/problems/divide-two-integers/discuss/303141/Python-beats-99.77-time-(28ms)-and-88-memory

def divide(dividend, divisor):
    sign = 1 if ((dividend < 0) == (divisor < 0)) else -1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    
    while dividend >= divisor:
        shifted_div, i  = divisor, 1
        while shifted_div <= dividend:
            dividend -= shifted_div
            quotient += i 
            i <<= 1
            shifted_div <<= 1
    return min(max(-2**31, quotient * sign), 2**31 - 1) 

assert divide(10, 3) is 3
assert divide(7, -3) is -2
assert divide(-2147483648, -1) == (2**31-1)
