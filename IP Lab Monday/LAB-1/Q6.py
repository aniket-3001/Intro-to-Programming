# https://www.hackerrank.com/contests/lab-1-monday/challenges/lab-1q6-bits-game/problem

def C(n, r):
    if r == 0:
        return 1
    return int((n/r)*C(n-1, r-1))


def set_bits(n):
    cnt = 0
    while n > 0:
        if (n & 1) == 1:
            cnt += 1
        n >>= 1
    return cnt


num = int(input())
print(C(5, set_bits(num)))
