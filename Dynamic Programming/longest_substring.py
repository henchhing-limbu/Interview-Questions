# solution 1
# This must be longest substring without repeating characters question.
# TODO(henxing): Make sure this is the question mentioned above.
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
