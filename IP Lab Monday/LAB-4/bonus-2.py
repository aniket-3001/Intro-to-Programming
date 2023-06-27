# https://www.hackerrank.com/contests/lab-4-monday/challenges/lab-4bonus-2-pattern

def pattern(spaces, brackets):
    for _ in range(spaces+1):
        print(' ', end='')
    for _ in range(brackets):
        print('<>', end=' ')
    print()


print()
n = int(input())
pattern(n-2, 1)
lines = n-1
loops = (lines-1)//3
residue = (lines-1) % 3
for i in range(1, loops+1):
    for j in range(3):
        pattern(n-(3*i)-j, (2*i)-1+j)
if residue == 1:
    pattern(0, (2*loops)+1)
elif residue == 2:
    pattern(1, (2*loops)+1)
    pattern(0, (2*loops)+2)
