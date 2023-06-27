# https://www.hackerrank.com/contests/lab-6-monday/challenges/lab-6q6-diagonal-matrix

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

diagonal = [[l[i][j] for i in range(n-1, -1, -1)] for j in range(n-1, -1, -1)]

for row in diagonal:
    for ele in row:
        print(ele, end=' ')
    print()
