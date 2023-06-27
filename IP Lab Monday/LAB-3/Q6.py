# https://www.hackerrank.com/contests/lab-3-monday/challenges/lab-3q6-chefs-cake

n = int(input())
for i in range(1, n+1):
    sub_str = ""
    for j in range(i-1):
        sub_str += chr(66+j)
    str = sub_str[-1::-1]+'A'+sub_str
    print((' '*(n-i))+str)
