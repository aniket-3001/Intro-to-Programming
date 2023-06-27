def C(n, r):
    if r == 0:
        return 1
    return int((n/r)*C(n-1, r-1))


n, r = map(int, input(
    "Enter space separated integer values for n and r (remember that n > r and n, r >= 0): ").split())

print(C(n, r))
