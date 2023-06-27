# https://www.hackerrank.com/contests/lab-3-monday/challenges/lab-3q3-number-sequence

n = int(input())
for i in range(1, n+1):
    j = 0
    for k in range(1, i+1):
        print(i+j, end=' ')
        j += n-k
    print()
