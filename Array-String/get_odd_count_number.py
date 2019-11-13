# Given an array of numbers where a number has odd number of counts
# You are supposed to get the number

# XOR between two same integers is 0. So, XOR among event count of same
# integers is always 0. Using this idea, this problem can be solved.
def get_odd_count_number(a):
    oddNum = 0
    for num in a:
        oddNum ^= num
    return oddNum

assert get_odd_count_number([1, 1, 2, 3, 2]) is 3
