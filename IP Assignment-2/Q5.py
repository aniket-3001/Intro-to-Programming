def scale(l, cx, cy):  # function which accepts list of coordinates to be scaled, the respective scaling factors and returns list containing scaled coordinates as tuples
    shape_matrix = [[x, y, 1] for x, y in l]
    transformation_matrix = [[cx, 0, 0], [0, cy, 0], [0, 0, 1]]

    # function call to obtain resultant matrix after multiplication
    res_matrix = matrix_mult(shape_matrix, transformation_matrix)

    # return scaled shape in the form of a list of coordinates
    return [(x, y) for x, y, _ in res_matrix]


def matrix_mult(mat1, mat2):
    # initialize resultant matrix with zeros
    res = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):

            # multiplying the elements and adding them
            res[i][j] = sum(mat1[i][k] * mat2[k][j]
                            for k in range(len(mat2)))

    return res


n = int(input("enter number of coordinates in your 2-D shape: "))
coord = []

print()

for _ in range(n):
    tup = tuple([int(c)
                 for c in input("enter space separated values for x and y coordinates: ").split()])
    coord += [tup]

print()

cx, cy = [int(c) for c in input(
    "enter space separated values for scaling parameters cx and cy: ").split()]

print()

print("initial coordinates:", coord)
print("scaled coordinates:", scale(coord, cx, cy))
