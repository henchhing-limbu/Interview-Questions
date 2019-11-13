# Given a sentence, reverse the words in the sentence. Assume that the words
# are alwyas separated by a space.

def reverse_words_in_str(inp_str):
	if len(inp_str) < 3:
		return inp_str
	
	s = list(inp_str)

	start = 0
	size = len(s)
	for i, char in enumerate(s):
		if char == ' ':
			reverse_helper(s, start, i-1)
			start = i + 1
	reverse_helper(s, start, i)
	reverse_helper(s, 0, i)
	return ''.join(s)

def reverse_helper(s, i, j):
	while i < j:
		s[i], s[j] = s[j], s[i]
		i += 1
		j -= 1

assert reverse_words_in_str(
	"My name is Henchhing Limbu") == "Limbu Henchhing is name My"
assert reverse_words_in_str("howard") == "howard"
assert reverse_words_in_str(" h") == " h"

