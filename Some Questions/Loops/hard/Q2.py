def input_matrix(m, n):
    l = [list(map(int, input(
        f"enter {n} space separated elements denoting row of your matrix: ").split())) for i in range(n)]
    return l


def add_matrices(m, n, matrices):
    summation_matrix = [[0 for j in range(n)] for i in range(m)]
    for matrix in matrices:
        for i in range(m):
            for j in range(n):
                summation_matrix[i][j] += matrix[i][j]
    return summation_matrix


def print_matrix(l):
    for c in l:
        for d in c:
            print(d, end=' ')
        print()


m, n = list(map(int, input(
    "enter 2 space spearated values for dimensions of the matrices: ").split()))
N = int(input("enter how many matrices do you want to add: "))
print()
print("lets get started with inputting values of the matrices:")
print()

matrices = []
if N > 1:
    for i in range(N):
        matrices += [input_matrix(m, n)]
        print()
        if i < N-1:
            print("now for the next matrix...")
else:
    matrices += [input_matrix(m, n)]

matrices_sum = add_matrices(m, n, matrices)
print("summation of the matrices results in:")
print_matrix(matrices_sum)
