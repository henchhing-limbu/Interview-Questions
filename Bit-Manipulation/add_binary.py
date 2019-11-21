"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

def add_binary(a, b):
    size = max(len(a), len(b))
    a = reversed(a.zfill(size))
    b = reversed(b.zfill(size))
    carry = 0
    result = []

    for a_bit, b_bit in zip(a, b):
        if a_bit == '1':
            carry += 1
        if b_bit == '1':
            carry += 1
        result.append(str(carry%2))
        carry //= 2
    if carry:
        result.append('1')
    result.reverse()
    return ''.join(result)

assert add_binary('11', '1') == '100'
assert add_binary('1010', '1011') == '10101'
