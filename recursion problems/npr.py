def P(n, r):
    if r == 0:
        return 1
    return n*P(n-1, r-1)


n, r = map(int, input(
    "Enter space separated integer values for n and r (always remember that n > r and n, r >= 0): ").split())

print(P(n, r))
