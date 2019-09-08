# using additional data structure
# We can simply use python set to keep track of already seen numbers.
def isUnique1(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

# without the use of additional data structure.
# We just need to check if the next char to current character is same or not.
def isUnique2(s):
    if s == '':
        return True
    sorted_s = sorted(s)
    for i in range(len(sorted_s)-1):
        if sorted_s[i] == sorted_s[i+1]:
            return False
    return True

assert isUnique1("apple") == False
assert isUnique1("Limbu") == True
assert isUnique1('') == True
assert isUnique2("apple") == False
assert isUnique2("Limbu") == True
assert isUnique2('') == True
