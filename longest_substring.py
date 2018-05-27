# solution 1
def longestSubstringLength(s):
	if len(s) == 1:
		return 1
	seen = {}
	length = 0
	for i in range(len(s)):
		seen[s[i]] = i;
		localLength = 1
		for j in range(i+1,len(s)):
			if s[j] not in seen:
				localLength += 1
			else:
				if  localLength > length:
					length = localLength
					seen = {}
	return length
print(longestSubstringLength("abcba"))
