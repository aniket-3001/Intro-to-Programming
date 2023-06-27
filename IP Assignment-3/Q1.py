def top(row):  # function to print pattern for top part
    global n
    if row > n:
        return
    print(('*'*(n-row+1))+(' '*(2*(row-1)))+('*'*(n-row+1)))
    top(row+1)


def bottom(row):  # function to print pattern for bottom part
    global n
    if row < 1:
        return
    print(('*'*(n-row+1))+(' '*(2*(row-1)))+('*'*(n-row+1)))
    bottom(row-1)


n = int(input("enter value of n: "))
print()

top(1)
bottom(n-1)
