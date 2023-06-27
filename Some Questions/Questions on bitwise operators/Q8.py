n = int(input())
for i in range(1 << n):
    for j in range(n-1, -1, -1):
        print((i >> j) & 1, end='')
    print()
