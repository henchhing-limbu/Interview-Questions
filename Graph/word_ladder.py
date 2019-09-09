"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from collections import deque
class Word:
	def __init__(self, length, word):
		self.word = word
		self.length = length

	def new_word(self, i, char):
		word = self.word[:i] + char + self.word[i+1:]
		return Word(self.length+1, word)

def ladder_length(begin_word, end_word, word_list):
	word_list = set(word_list)
	if end_word not in word_list:
		return 0
	seen_words = set()
	queue = deque()
	queue.append(Word(1, begin_word))

	while queue:
		word = queue.popleft()
		for i, char in enumerate(word.word):
			replacement_char = 'a'
			# try replacing ith character with all possible alphabets. If it's
			# a valid word, push it to the queue.
			while replacement_char <= 'z':
				if replacement_char != char:
					new_word = word.new_word(i, replacement_char)
					# check if the new word is end_word
					if new_word.word == end_word:
						return new_word.length 
					# Check if the new word is not already seen and is in word list
					if new_word.word not in seen_words and new_word.word in word_list:
						queue.append(new_word)
				replacement_char = chr(ord(replacement_char)+1)
	return 0

assert ladder_length('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == 5
assert ladder_length('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']) == 0

