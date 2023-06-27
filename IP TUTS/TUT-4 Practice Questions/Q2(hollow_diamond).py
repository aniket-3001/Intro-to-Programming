n = int(input())
for i in range(1, (2*n)+1):
    if i > n:
        i = (2*n)+1-i
    print(('*'*(n-i+1))+(' '*(2*(i-1)))+('*'*(n-i+1)))
# spaces are handled by 2n-2(n-i+1) since total no. of elements in each row is 2n
