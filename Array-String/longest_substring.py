# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
# k needs to be greater than 0

def longestSubstr(s, k):
	if not s or k < 1:
		return ''
	count = 0
	charIdx = {}
	start_idx = 0
	substr = ""
	
	for i, char in enumerate(s):
		char = s[i]		
		if char not in charIdx:
			count += 1
			charIdx[char] = i
			if count > k:
				length = i - start_idx
				if length > len(substr):
					substr = s[start_idx:i]
				
				# The first character of the index needs to be removed from
				# the substring. We need to update start index to be latest
				# first character's index plus 1. This will make sure that
				# the substring from new start index to current character does
				# not containt the first character.
				start_idx = charIdx[s[start_idx]] + 1
		
		else: # Update the character's old index with the new index.
			charIdx[char] = i
	if (i - start_idx) > len(substr):
		substr = s[start_idx:i]
	
	return substr

assert longestSubstr("abcba", 2) == "bcb"
assert longestSubstr('', 1) is ''
