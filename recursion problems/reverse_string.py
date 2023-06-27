def rev_str(s):
    if len(s) == 0:
        return s
    return s[-1] + rev_str(s[:-1])


str = input()
print(rev_str(str))
