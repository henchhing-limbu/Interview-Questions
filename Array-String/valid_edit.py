def valid_edit(s1, s2):
    '''
    * check for size of both strings
    * if diff more than 1, return false
    * if diff is 0, check for replacements
    * if diff is 1, check for deletion or addition

    pale, ple -> True
    pales, pale -> True
    pale, bale -> True
    pale, bae -> False

    * need to know which string is bigger
    * in replacement take count of how many replacements were made
    '''
    size1 = len(s1)
    size2 = len(s2)
    if abs(size1 - size2) > 1:
        return False
    if size2 > size1:
        return valid_edit(s2, s1)
    if size1 == size2:
        return check_replacement(s1, s2)
    else:
        return check_add_del(s1, s2)

def check_replacement(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
            if cnt > 1:
                return False
    return True

def check_add_del(s1, s2):
    i, j = 0, 0
    size2 = len(s2)
    cnt = 0
    while i < size2:
        if s2[i] != s1[j]:
            j += 1
            cnt += 1
            if cnt > 1:
                return False
        else:
            i += 1
            j += 1
    return True
            
assert valid_edit('pale', 'bae') == False
assert valid_edit('pale', 'bale') == True
assert valid_edit('pales', 'pale') == True
assert valid_edit('', 'a') == True
