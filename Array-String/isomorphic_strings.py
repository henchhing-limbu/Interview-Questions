"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""

def isIsomorphic(s, t):
	if len(s) != len(t):
		return False
	s_to_t_char_map = {}
	seen_t_chars = set()
	for s_char, t_char in zip(s, t):
		if s_char not in s_to_t_char_map: # this char is not mapped until now.
			if t_char in seen_t_chars: # checking if t_char is mapped to two s_chars
				return False
			s_to_t_char_map[s_char] = t_char
			seen_t_chars.add(t_char)
		else: # already mapped. Check if it's mapped to right character.
			if s_to_t_char_map[s_char] != t_char:
				return False
	return True

assert isIsomorphic('egg', 'add') == True
assert isIsomorphic('foo', 'bar') == False
assert isIsomorphic('paper', 'title') == True
assert isIsomorphic('fear', 'feel') == False
assert isIsomorphic('pear', 'pearl') == False  
