def print_matrix(l):
    for c in l:
        for d in c:
            print(d, end=' ')
        print()


def matrix_mult(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        print("incompatible matrix dimensions")
        return

    # initialize resultant matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):

            # multiplying the elements and adding them
            result[i][j] = sum(mat1[i][k] * mat2[k][j]
                               for k in range(len(mat2)))

    print("resultant matrix:")
    print_matrix(result)


print("For first matrix:")
m1, n1 = list(map(int, input(
    "enter 2 space spearated values for dimensions of the matrix: ").split()))
l1 = [list(map(int, input(
    f"enter {n1} space separated elements denoting row of your matrix: ").split())) for _ in range(m1)]

print()

print("For second matrix:")
m2, n2 = list(map(int, input(
    "enter 2 space spearated values for dimensions of the matrix: ").split()))
l2 = [list(map(int, input(
    f"enter {n2} space separated elements denoting row of your matrix: ").split())) for _ in range(m2)]

print()

matrix_mult(l1, l2)
