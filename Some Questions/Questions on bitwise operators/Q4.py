n = int(input("enter no. n whose ith bit is to be extracted: "))
i = int(input("enter i: "))
print((n >> i) & 1)
