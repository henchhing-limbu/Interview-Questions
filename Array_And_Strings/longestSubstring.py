# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
# k needs to be greater than 0

def longestSubstr(s, k):
	count = 0
	charIdx = {}
	start_idx = 0
	substr = ""
	
	for i in range(len(s)):
		char = s[i]		
		if char not in charIdx:
			count += 1
			charIdx[char] = i
			if count > k:
				length = i - start_idx
				if length > len(substr):
					substr = s[start_idx:i]
				
				# start idx is char prev idx + 1
				start_idx = charIdx[s[start_idx]] + 1
				
		charIdx[char] = i
	if (i - start_idx) > len(substr):
		substr = s[start_idx:i]
	
	return substr

print(longestSubstr("abcba", 2))
