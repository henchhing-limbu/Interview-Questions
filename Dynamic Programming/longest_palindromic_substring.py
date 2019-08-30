def get_longest_palindromic_substring(s):
	lookup_table = [[False for _ in range(len(s))] for _ in range(len(s))]
	for i in range(len(s)):
		lookup_table[i][i] = True
	# Check if two adjacent characters are same.
	for i in range(len(s) - 2):
		lookup_table[i][i+1] = True if s[i] == s[i+1] else False
	
	longest_substr = (0, 1)
	# Diagonal 1 and 2 are already computed.
	# Diagonal 3 needs to computed. As such, the outer loop is start index of
	# column of diagonal 3. The inside loop is simply looping through each row.
	for k in range(1, len(s)):
		j = k + 1
		for i in range(len(s)):
			# Looking up in the table is constant time.
			# Brings down the runtime from O(n^3) to O(n^2)
			if j < len(s) and s[i] == s[j] and lookup_table[i+1][j-1]:
				longest_substr = (i, j)
				lookup_table[i][j] = True
			j += 1
	# 1 needs to be added to get last character of longest substr.
	return s[longest_substr[0]:longest_substr[1]+1]

print(get_longest_palindromic_substring('babad'))
	

	
