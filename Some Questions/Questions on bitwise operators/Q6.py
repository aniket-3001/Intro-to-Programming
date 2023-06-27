n = int(input("enter no. whose no. of set bits are to be counted: "))
cnt = 0
while n > 0:
    if (n & 1) == 1:
        cnt += 1
    n >>= 1
print(cnt)
