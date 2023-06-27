# https://www.hackerrank.com/contests/lab-2-monday/challenges/lab-2q6-bits-flip/problem

s = input()
n = int(s, 2)
n += 1
one = bin(n)[2:]
if len(one) != len(s):
    one = '0'*(len(s)-len(one)) + one
two = ''
for c in one:
    if c == '0':
        two += '1'
    else:
        two += '0'
print(two)
