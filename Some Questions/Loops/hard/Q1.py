m, n = list(map(int, input(
    "enter 2 space spearated values for dimensions of the matrix: ").split()))
l = [list(map(int, input(
    f"enter {n} space separated elements denoting row of your matrix: ").split())) for i in range(n)]

for c in l:
    for d in c:
        print(d, end=' ')
    print()
