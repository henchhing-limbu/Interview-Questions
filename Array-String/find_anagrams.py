"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

# This is a variation of sliding window problem.
# We keep track of characters count of the sliding window in a dictionary.
# First, we make p_counter that contains character of p as key and their count
# as value. Second, we maintain a sliding window and slide it through s. Doing
# this we update and maintain s_counter and check if the two dictionaries are
# same.

# Time complexity is O(n). Where did timecomplexity of comparing dictionary go?
# We always know there can't be more than 26 keys in dictionary. So, that's
# constant time.


from collections import Counter

def find_anagrams(s, p):
    p_counter, s_counter = Counter(p), Counter(s[:len(p)])
    pop_char_idx = 0
    start_indexes = []
    if p_counter == s_counter:
        start_indexes.append(pop_char_idx)

    for i in range(len(p), len(s)):
        pop_char = s[pop_char_idx]
        s_counter[pop_char] -= 1
        pop_char_idx += 1
        if s_counter[pop_char] == 0:
            s_counter.pop(pop_char)
        s_counter[s[i]] += 1
        if s_counter == p_counter:
            start_indexes.append(pop_char_idx)
    return start_indexes

assert find_anagrams('abab', 'ab') == [0, 1, 2]
assert find_anagrams('cbaebabacd', 'abc') == [0, 6]
