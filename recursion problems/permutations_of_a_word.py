def permutation(s):
    if len(s) == 0:
        return ['']
    perm_lst = []
    char_set = set()
    for c in s:
        char_set.add(c)
    for c in char_set:
        for d in permutation(s.replace(c, '', 1)):
            perm_lst.append(c + d)
    return sorted(perm_lst)


s = input()
print(permutation(s))
