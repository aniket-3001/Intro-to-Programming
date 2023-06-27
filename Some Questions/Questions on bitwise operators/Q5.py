n = int(input("enter no. whose ith bit needs to be set to 1: "))
i = int(input("enter ith bit: "))
print((1 << i) | n)
