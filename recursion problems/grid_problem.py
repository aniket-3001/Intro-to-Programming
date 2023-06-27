# Take as input from the user dimensions m,n (m for rows and n for columns) of a grid. Find the total no. of paths possible to go from the top left corner to the bottom right.
# constraints: you can only move down or right by 1 unit

def grid_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return grid_paths(m-1, n)+grid_paths(m, n-1)


m, n = map(int, input(
    "enter space separated values for m and n respectively: ").split())
print("total no. of paths possible:", grid_paths(m, n))
