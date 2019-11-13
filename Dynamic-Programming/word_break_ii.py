"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

def word_break(s, word_dict):
    word_dict = set(word_dict)
    word_ends = []
    for i in range(len(s)):
        i_valid_words = []
        if s[:i+1] in word_dict:
            i_valid_words.append(0)

        for j, j_valid_words in enumerate(word_ends):
            if j_valid_words and s[j+1:i+1] in word_dict:
                i_valid_words.append(j+1)
        word_ends.append(i_valid_words)

    possible_sentences = []
    def dfs(j, sentence):
        if j < 0:
            possible_sentences.append(' '.join(sentence[::-1]))
            return
        
        for i in word_ends[j]:
            sentence.append(s[i:j+1])
            dfs(i-1, sentence)
            sentence.pop()

    if word_ends[-1]:
        dfs(len(word_ends)-1, [])
    return possible_sentences

word_dict = ['cat', 'cats', 'and', 'sand', 'dog']
word_break('catsanddog', word_dict)

