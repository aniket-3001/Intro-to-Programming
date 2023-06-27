# https://www.hackerrank.com/contests/lab-2-monday/challenges/lab-2bonus-2-weird-sequence

import math


def compute_N(l, s):
    if l % s == 0:
        return l//s
    else:
        return math.ceil(l/s)


def compute_series(a, b, N):
    sum = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            sum += (i*b)
        else:
            sum += (i*a)
    return (N*sum)


a = int(input())
b = int(input())

if a > b:
    larger, smaller = a, b
else:
    larger, smaller = b, a

print(compute_series(smaller, larger, compute_N(larger, smaller)))
