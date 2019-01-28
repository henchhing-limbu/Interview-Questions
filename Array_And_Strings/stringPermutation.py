def permutation(s):
    permutHelper(s, "")

def permutHelper(s, prefix):
    if s == "":
        print(prefix)
    for i in range(len(s)):
        rem = s[:i] + s[i+1:]
        permutHelper(rem, prefix + s[i])

permutation("name")

