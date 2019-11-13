"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

# TODO(henxing): Finish this
def decode_string(s):
    decode_str = []
    _decode_string_helper(s, 0, 0)
    return ''.join(decode_str)

def _decode_string_helper(s, i, j):
    if j >= len(s):
        return
    # Return the start and end index of substr inside [...]
    elif s[j] == ']':
        return (i, j)
    # Check if it's number
    elif s[j].isdigit():
        # Repeat the substring for specified number
        m, n = _decode_string_helper(s, j+2, j+2)
        substr = s[m:n]
        repeated_substr = ''
        for _ in range(int(s[j])):
            repeated_substr += substr
        _decode_string_helper(s, n+1, n+1)
    else:
        return _decode_string_helper(s, i, j+1)

print(decode_string('3[a]2[bc]'))
print(decode_string('3[a2[c]]'))

# i, j = 0, 0 decode_str = []
# i, j = 2, 2 
# i, j = 2, 3 decode_str = ['a', 'a', 'a']
# i, j = 4, 4
# i, j = 6, 6
# i, j = 6, 7
# i, j = 6, 8 decode_str = ['bc', 'bc', 'bc']
