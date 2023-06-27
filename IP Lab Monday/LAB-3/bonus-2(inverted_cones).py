# https://www.hackerrank.com/contests/lab-3-monday/challenges/lab-3q5-sequence-function

n = int(input())
for r in range(1, n+1):
    print(" " * (n-r), end="")
    stars = r - r//3
    if stars % 2 == 1:
        print("*  "*stars, end="")
    else:
        print("*  "*int(stars/2 - 1), end="")
        if r % 3 == 0:
            print("*   ", end="")
        else:
            print("* ", end="")
        print("*  "*int(stars/2), end="")
    print()
