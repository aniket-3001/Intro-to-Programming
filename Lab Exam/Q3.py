n = int(input())
L = [i for i in range(1, n+1) if i % 3 == 0 or i %
     5 == 0 or i % 7 == 0 or i % 9 == 0]
print(L)
