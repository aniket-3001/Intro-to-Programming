def C(n, r):
    if r == 0:
        return 1
    return int((n/r)*C(n-1, r-1))


n = int(input())
for i in range(n):
    print(' '*(n-i), end=' ')
    for j in range(i+1):
        print(C(i, j), end=' ')
    print()
