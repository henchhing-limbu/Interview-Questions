# checks if s1 is permutation of s2
from collections import Counter
def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_ctr = Counter(s1)
    s2_ctr = Counter(s2)
    return s1_ctr == s2_ctr

