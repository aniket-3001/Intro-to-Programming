def chk(s):
    if len(s) < 8:
        return False
    for c in s:
        if c in "123456789":
            break
    else:
        return False
    for c in s:
        if c in "@#$%&":
            break
    else:
        return False
    for c in s:
        if c >= 'A' and c <= 'Z':
            break
    else:
        return False
    for c in s:
        if c >= 'a' and c <= 'z':
            break
    else:
        return False
    return True

# A password is strong if it
# contains at least one small letter, at least one Capital letter, at least one digit, and at
# least one of the following characters: @#$%&, and has a length of at least 8


s = input()
print(chk(s))
