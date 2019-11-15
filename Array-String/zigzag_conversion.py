"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

# The idea is pretty simple.
# The structure in Explaination can be thought of array of strings.
# For first example: the array would be ['PAHN', 'APLSIIG', 'YIR']
# We can populate the array using two pointers.
# One pointer, i,  simply iterates over the input string.
# The other pointer, j,  points to one of the array's string where the new character
# is to be concatenated.

# We start with j = 0 and increment it by 1 to go down in the array.
# Whenever j reaches numRows - 1, we know that it's time to go up. We start
# decrementing j by 1 until j = 0.
# We continue this until i reaches s.size - 1

# At the end, we simply join the strings in the array to get the zigzag string.

def zigzag_conversion(s, num_of_rows):
    if num_of_rows < 2:
        return s
    zigzag_s = ['' for _ in range(num_of_rows)]
    j = 0
    direction = 1
    for char in s:
        zigzag_s[j] += char
        if j == 0:
            direction = 1
        elif j == num_of_rows-1:
            direction = -1
        j += direction
    return ''.join(zigzag_s)
