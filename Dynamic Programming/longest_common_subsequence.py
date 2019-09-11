"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

"""

# Dynamic programming

#   |   | a | b | c | d | e 
#--------------------------
#   | 0 | 0 | 0 | 0 | 0 | 0 
#--------------------------
# a | 0 | 1 | 1 | 1 | 1 | 1 
#--------------------------
# c | 0 | 1 | 1 | 2 | 2 | 2 
#--------------------------
# e | 0 | 1 | 1 | 2 | 2 | 3

# If the characters are same, then length of longest common subsequence ending
# at these characters must be longest commong subsequence of ending at
# neighboring characters plus 1.

# if s1[i] == s2[j]:
#	s[i][j] = 1 + s[i-1][j-1] 

# If the characters are not same, then length of longest common subequence must
# be either of longest common substring ending at i and j-1 or longest common
# substring ending at i-1 and j.

# if s1[i] != s2[j]:
# 	s[i][j] = max(s[i-1][j], s[i][j-1])

def longest_common_subsequence(text1, text2):
	text1_size, text2_size = len(text1), len(text2)
	dp = [[0 for _ in range(text2_size + 1)] for _ in range(text1_size + 1)]
	length_of_subs = 0

	for i in range(1, text1_size + 1):
		for j in range(1, text2_size + 1):
			if text1[i-1] == text2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
				if dp[i][j] > length_of_subs:
					length_of_subs = dp[i][j]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return length_of_subs

assert longest_common_subsequence('abc', 'abc') is 3
assert longest_common_subsequence('abc', 'def') is 0
assert longest_common_subsequence('abcde', 'ace') is 3
