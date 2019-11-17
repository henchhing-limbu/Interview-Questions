"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

# Juse check first two different characters between two subsequent words are in
# the same order as in given order. 
# Use a dictionary of chars that maps given characters to their position.

def is_alien_sorted(words, order):
    order_map = {char: pos for pos, char in enumerate(order)}
    for i in range(1, len(words)):
        word1 = words[i-1]
        word2 = words[i]
        for char_1, char_2 in zip(word1, word2):
            if char_1 != char_2:
                if order_map[char_1] > order_map[char_2]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False
    return True

assert is_alien_sorted(['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz') is False
