"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# When we look at the problem, we figure out that there are different cases we
# need to take care of.
# 1 is 'I'
# 2 is 'II'
# 3 is 'III'
# We think 4 is 'IIII'. However it's, 'IV'.
# We need to worry about similar cases for 'XC', 'XL', 'CM', 'CD'.

# We can simply make if statements for every cases and come up with the
# solution below.

def intToRoman(num):
    roman = ''
    while num != 0:
        if num >= 1000:
            roman += 'M'
            num -= 1000
        elif 900 <= num < 1000:
            roman += 'CM'
            num -= 900
        elif num >= 500:
            roman += 'D'
            num -= 500
        elif 400 <= num < 500:
            roman += 'CD'
            num -= 400
        elif num >= 100:
            roman += 'C'
            num -= 100
        elif 90 <= num < 100:
            roman += 'XC'
            num -= 90
        elif num >= 50:
            roman += 'L'
            num -= 50
        elif 40 <= num < 50:
            roman += 'XL'
            num -= 40
        elif num >= 10:
            roman += 'X'
            num -= 10
        elif num == 9:
            roman += 'IX'
            num -= 9
        elif num >= 5:
            roman += 'V'
            num -= 5
        elif num == 4:
            roman += 'IV'
            num -= 4
        else:
            roman += 'I'
            num -= 1
    return roman


# These if statements can be removed completely.
def int_to_roman(num):
    integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L',
            'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman_num = ''

    for integer, roman in zip(integers, romans):
        roman_num += (num//integer) * roman
        num %= integer
    return roman_num

assert int_to_roman(58) == 'LVIII'
assert int_to_roman(1994) == 'MCMXCIV'
assert int_to_roman(9) == 'IX'
