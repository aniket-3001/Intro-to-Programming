# https://www.hackerrank.com/contests/ip-lab-8/challenges/l8-q5-hritiks-problem/submissions/code/1354728005

tgt = int(input())
maxd = int(input())
moves = 0
while tgt > 1:
    if (tgt % 2 == 0) and (maxd > 0):
        tgt /= 2
        maxd -= 1
    else:
        tgt -= 1
    moves += 1
print(moves)
