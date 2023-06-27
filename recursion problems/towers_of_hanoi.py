'''Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and they are on rod A. The objective of the puzzle is to move the entire stack to another rod (here considered C), obeying the following simple rules: 

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk. '''


def hanoi(n, start_rod, end_rod):
    if n == 1:
        pm(start_rod, end_rod)
    else:
        other_rod = 6-(start_rod+end_rod)
        hanoi(n-1, start_rod, other_rod)
        pm(start_rod, end_rod)
        hanoi(n-1, other_rod, end_rod)


def pm(start, end):
    print(start, '->', end)


n, start, end = list(map(int, input(
    "enter space separated values for number of discs, start rod and end rod respectively: ").split()))
hanoi(n, start, end)
