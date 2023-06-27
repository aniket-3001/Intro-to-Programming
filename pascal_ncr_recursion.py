def C(n, r):
    if r == 0:
        return 1
    return (n//r)*C(n-1, r-1)


def pascal(n):
    for i in range(n):
        print(' '*(n-i-1), end='')
        for j in range(i+1):
            print(C(i, j), end=' ')
        print()
