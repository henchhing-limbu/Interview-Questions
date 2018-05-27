# using additional data structure
def isUnique1(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

# without the use of additional data structure
def isUnique2(s):
    if s == '':
        return True
    largest = s[0]
    sorted_s = ''.join(sorted(s))
    for i in range(len(s)-1):
        if sorted_s[i] == sorted_s[i+1]:
            return False
    return True

print(isUnique1("apple"))
print(isUnique1("Limbu"))
print(isUnique1(''))
print(isUnique2("apple"))
print(isUnique2("Limbu"))
print(isUnique2(''))
